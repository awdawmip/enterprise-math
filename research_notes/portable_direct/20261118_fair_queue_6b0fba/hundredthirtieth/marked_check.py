"""Four-round exact replay and separate finite combinatorial tests. Python 3.10+."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys

BANK_SHA = "79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c"
VENDOR_BLOB = "4e6b3132580e3cd70a20a0d8bd4d28792b961afb"
INPUTS = [(3,1),(3,2),(7,2),(5,2),(11,3),(21,2),(29,7),(17,2),(19,4),
          (11,2),(23,2),(13,2),(53,10),(29,4),(31,7),(17,3),(103,8)]


def is_dyadic(x):
    return x.denominator & (x.denominator-1) == 0


def first_window(D):
    """Only for comparing to the independent address model, not used by mark()."""
    assert D >= 3 and D % 2
    j = D.bit_length()+1
    M = 1 << (j-1)
    s, h = M-D, (D-1)//2
    piece = 8 if s<h else 9 if s==h else 6 if s==h+1 else 2
    return j,M,s,h,piece


def mask_counts(u, D):
    # Weights for minority, interior majority, and the two boundary vertices.
    counts = [1,0,0,0,0]
    for w in [2]*u + [-2]*(u-1) + [-1]*2:
        counts = [v + counts[(i-w)%5] for i,v in enumerate(counts)]
    return counts[0] << (D-2*u-1)


def integer_tests():
    windows, param_cases = 0,0
    pieces = Counter()
    for D in range(3,512,2):
        j,M,s,h,piece = first_window(D)
        n = Counter(z%D for z in range(M))
        defect = Counter()
        hetero = 0
        for r in range(D):
            parents = [((r-bit)*pow(2,-1,D))%D for bit in (0,1)]
            a,b = (n[z] for z in parents)
            if a!=b:
                assert {a,b}=={1,2}
                hetero += 1
                for z in parents:
                    defect[z]+=1
        u = min(s,D-s)
        assert hetero==2*u and len(defect)==2*u+1
        assert sum(n[z]**2*defect[z] for z in (0,D-1))==piece
        assert Counter(defect.values())=={2:2*u-1,1:2}
        pieces[piece]+=1
        # Direct dynamic programming with actual weights, independent of types.
        masks=[1,0,0,0,0]
        for z in range(D):
            w=n[z]**2*defect[z]
            masks=[v+masks[(i-w)%5] for i,v in enumerate(masks)]
        assert masks[0]==mask_counts(u,D)
        windows+=1
    for t in range(2,15,2):
        for d in range(1,(1<<t)+4):
            D=d//(d&-d)
            bad = D>1 and d<(1<<(t-1))
            if D>1:
                j=D.bit_length()+1
                assert bad==(j<=t-(d&-d).bit_length()+1)
            param_cases+=1
    return dict(address_windows=windows,phase_multipliers=dict(sorted(pieces.items())),
                schedule_period_pairs=param_cases)


def load_source(repo,stage):
    rec=repo/"research_notes/directed_recovery"
    pkg=rec/"20260926_C6438C"
    old=rec/"20260926_0C08F0"
    os.environ.update(BRC_STAGE87_SOURCE=str(stage),BRC_STREAMING_PREVIOUS=str(old),
                      BRC_ZERO_ENDPOINT_SOURCE=str(old/"adversarial/zero_endpoint_extension.py"))
    for p in (stage,pkg/"new_word_compiler",pkg/"optimization/streaming",
              rec/"20260927_C6438C/qft_row_queries/gram_research"):
        sys.path.insert(0,str(p))
    from stage45.brc_loop_recheck import CALLS,verify_vendor
    from compiled_streaming import bank_from_compilation
    from lazy_streaming import LazyStreamingProgram
    from single_walker import PointRowOracle,transition_plan,QueryBudgetExhausted
    assert verify_vendor()["git_blob"]==VENDOR_BLOB
    raw=gzip.decompress((pkg/"direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz").read_bytes())
    assert hashlib.sha256(raw).hexdigest()==BANK_SHA
    before=len(CALLS)
    bank=bank_from_compilation(json.loads(raw)["phase_compilation"],t=4,epsilon=F(1))["bank"]
    data=(bank,LazyStreamingProgram,PointRowOracle,transition_plan,QueryBudgetExhausted,CALLS)
    return data,len(CALLS)-before


def checked_mark(program, old, j, calls, fees):
    if j==1 or old==1:
        return int(j>1)
    table=program.tables[j-2]
    before_calls=len(calls)
    before=dict(table.stats)
    result=int(table[old]==1)
    fees["forward_lookups"]+=1
    for k in ("computed_columns","cache_hits","column_adder_digit_replays",
              "column_host_bit_wiring_operations"):
        fees[k]+=table.stats[k]-before[k]
    fees["native_calls_inside_mark_lookup"]+=len(calls)-before_calls
    return result


def actual_case(native,d,N,g):
    bank,Program,Oracle,plan,_,calls=native
    base=len(calls)
    prog=Program(N,g,4,bank,61)
    setup=len(calls)-base
    live={((),1):[F(1),F(0)]}
    fees=Counter()
    live_calls=0
    branch_checks=0
    class_mass={}
    row_requests=0
    nonzero_frames=0
    max_bits=[0,0]
    max_prob_bits=0
    step_calls=[]
    for j in range(1,5):
        child=defaultdict(lambda:[F(0),F(0)])
        oracles={}
        prior_calls=len(calls)
        watch=defaultdict(F)
        edges=defaultdict(list)
        for (h,z),mu in live.items():
            if h not in oracles:
                oracles[h]=Oracle(prog,h)
            for coin in (0,1):
                info=plan(oracles[h],z,coin)
                live_calls+=1
                target=info["candidate"]
                p0=info["bit_probability_given_proposed_label"]
                max_prob_bits=max(max_prob_bits,p0.denominator.bit_length())
                for bit,prob in ((0,p0),(1,1-p0)):
                    if not prob:
                        continue
                    nxt=child[h+(bit,),target]
                    if bit==1 and not any(h):
                        assert not mu[1]
                        value=mu[0]*prob/2
                        code=checked_mark(prog,z,j,calls,fees)
                        branch_checks+=1
                        nxt[code]+=value
                        watch[z]+=value
                        edges[target].append(value)
                    else:
                        for b,mass in enumerate(mu):
                            nxt[b]+=mass*prob/2
        class_mass[j]=(dict(watch),dict(edges))
        assert sum(sum(v) for v in child.values())==1
        for oracle in oracles.values():
            row_requests+=oracle.stats["query_requests"]
            nonzero_frames+=oracle.stats["native_phase_vector_applications"]
            max_bits[0]=max(max_bits[0],oracle.stats["max_numerator_bits"])
            max_bits[1]=max(max_bits[1],oracle.stats["max_denominator_bits"])
        step_calls.append(len(calls)-prior_calls)
        live=child

    # Projection verification uses exact actual terminal rows and a separate cache.
    # The marked sampler itself does not walk the order or enumerate a work orbit.
    before_verify=len(calls)
    cycle=[1]
    z=prog.tables[-1][1]
    while z!=1:
        assert z not in cycle
        cycle.append(z)
        z=prog.tables[-1][z]
    assert len(cycle)==d
    words=defaultdict(lambda:[F(0),F(0)])
    checks=0
    for h in sorted({h for h,_ in live}):
        oracle=Oracle(prog,h)
        for z in cycle:
            row=oracle.query(4,z)
            w=oracle.norm_observation(row)
            a,b=live.get((h,z),[F(0),F(0)])
            assert w==a+b and is_dyadic(w)
            checks+=1
            words[h][0]+=a
            words[h][1]+=b
    assert sum(sum(ab) for ab in words.values())==1
    bad=d not in (1,2,4) and d<8
    significant=sum(not is_dyadic(m) for masses in words.values() for m in masses)
    assert bool(significant)==bad
    witness=None
    if bad:
        D=d//(d&-d)
        j,M,s,h,piece=first_window(D)
        marked=sum(ab[1] for w,ab in words.items() if w[:j]==(0,)*(j-1)+(1,))
        assert marked==F(piece,20*M*M)
        watch,edges=class_mass[j]
        u=min(s,D-s)
        assert len(watch)==2*u+1 and len(edges)==2*u
        assert all(sorted(vals)==[F(1,20*M*M),F(4,20*M*M)] for vals in edges.values())
        masks=[F(0)]
        for v in list(watch.values())+[F(0)]*(D-len(watch)):
            masks+=[a+v for a in masks]
        blind=sum(is_dyadic(x) for x in masks)
        assert blind==mask_counts(u,D)
        witness=dict(j=j,marked_mass=str(marked),first_one_at_j=str(sum(watch.values())),
                     nonzero_old_labels={str(z):str(v) for z,v in sorted(watch.items())},
                     independent_single_parent_given_minus="1/5",
                     blind_masks=blind,all_masks=len(masks))
    return dict(N=N,g=g,verified_order=d,terminal_words=len(words),
                non_dyadic_marked_word_atoms=significant,
                full_terminal_label_checks=checks,setup_calls=setup,
                marked_dp_BRC_calls_by_round=step_calls,transition_plans=live_calls,
                mark_evaluations_in_positive_branches=branch_checks,mark_cost=dict(fees),
                row_query_requests=row_requests,nonzero_feedback_applications=nonzero_frames,
                max_row_numerator_and_denominator_bits=max_bits,
                max_readout_probability_denominator_bits=max_prob_bits,
                extra_BRC_calls_for_terminal_and_order_audit=len(calls)-before_verify,
                witness=witness)


def rejected(native):
    bank,Program,Oracle,plan,Exhausted,_=native
    prog=Program(7,2,4,bank,61)
    o=Oracle(prog)
    checks=[("nonunit_base",lambda:Program(9,3,4,bank,61),ValueError),
            ("odd_width",lambda:Program(7,2,3,bank,61),ValueError),
            ("omitted_mode",lambda:Program(7,2,4,bank,60),ValueError),
            ("missing_word",lambda:Program(7,2,4,{i:v for i,v in bank.items() if i!=3},61),KeyError),
            ("invalid_history",lambda:Oracle(prog,(True,)),ValueError),
            ("boolean_coin",lambda:plan(o,1,True),ValueError),
            ("zero_parent_row",lambda:plan(o,0,0),ValueError),
            ("out_of_range",lambda:plan(o,8,0),ValueError),
            ("completed_history",lambda:plan(Oracle(prog,(0,)*4),1,0),ValueError),
            ("empty_budget",lambda:plan(Oracle(prog,query_budget=0),1,0),Exhausted)]
    ret={}
    for name,fn,error in checks:
        try:
            fn()
        except error as ex:
            ret[name]=type(ex).__name__
        else:
            raise AssertionError(name)
    return ret


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",type=Path,default=Path("/workspace/enterprise-math"))
    parser.add_argument("--stage",type=Path,required=True)
    args=parser.parse_args()
    native,setup=load_source(args.repo.resolve(),args.stage.resolve())
    rows=[actual_case(native,d,N,g) for d,(N,g) in enumerate(INPUTS,1)]
    composite=[actual_case(native,3,g**3-1,g) for g in (4,6,8)]
    assert all(r["witness"]["marked_mass"]=="9/320" and
               r["nonzero_feedback_applications"]>0 for r in composite)
    before=len(native[-1])
    controls=rejected(native)
    out=dict(bank_sha256=BANK_SHA,vendor_git_blob=VENDOR_BLOB,bank_BRC_calls=setup,
             actual_four_round_replay=rows,additional_composite_family=composite,
             total_plans=sum(r["transition_plans"] for r in rows),
             extra_BRC_calls_for_rejection_controls=len(native[-1])-before,
             typed_rejections=controls,independent_integer_tests=integer_tests())
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
