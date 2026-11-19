"""Exact source replay and randomized two-Bernoulli finite-sample certification."""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


M = 4
L = 1 << M
# First two fields are the only native inputs. The third is a post-run assertion.
CASES = [(51,2,8),(27,4,9),(25,4,10),(69,4,11),(35,2,12),(159,10,13),
         (49,6,14),(77,4,15),(77,2,None)]
HELPER_SHA = "b79a92b28b0528e7e8a3b026c9716e9379f1ef21f891ad8f4db36f6a384dc62e"
BANK_SHA = "79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c"
VENDOR_BLOB = "4e6b3132580e3cd70a20a0d8bd4d28792b961afb"
STREAM_SHA = "635d0c4aee0aaa8d58bb0244835e08e5caa0f6a94926a5213519f40db992a257"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def sign(r, word):
    k = sum(b << i for i,b in enumerate(word))
    return 1 if ((r*k) % L) // (L//4) in (0,3) else -1


def native_tree(lib, program):
    current = {(): program.initial()}
    cost = Counter()
    peaks = Counter()
    for i in range(M):
        nxt = {}
        for h,(state,den) in current.items():
            plan = program.branch_plan(state,den,h)
            cost["branch_plans"] += 1
            for bit,mass in enumerate(plan.masses):
                if not mass:
                    cost["zero_children"] += 1
                    continue
                child = program.materialize(plan,bit)
                cost["positive_children"] += 1
                row = lib.raw_field(*child)
                direct = sum(x*x for vector in row.values() for x in vector.values())
                assert direct == mass
                nxt[h+(bit,)] = child
                peaks["max_cell_denominator_bits"] = max(peaks["max_cell_denominator_bits"],child[1].bit_length())
                peaks["max_work_labels_per_positive_child"] = max(peaks["max_work_labels_per_positive_child"],len(row))
                peaks["max_leaf_mass_denominator_bits"] = max(peaks["max_leaf_mass_denominator_bits"],mass.denominator.bit_length())
        current = nxt
    leaves = {}
    for h,child in current.items():
        row = lib.raw_field(*child)
        leaves[h] = sum(x*x for vector in row.values() for x in vector.values())
    assert sum(leaves.values())==1
    return leaves,dict(cost),dict(peaks)


def feedback_table(lib, rd, program):
    table = {}
    stats = Counter()
    for h in product((0,1),repeat=M):
        op = rd.Ops()
        word = lib.bind_word(rd,op,program,h)
        v = [rd.alpha(op,word,x) for x in range(L)]
        table[h] = {}
        for r in range(1,L//2+1):
            table[h][r] = sum(op.dot(v[x],v[L-r+x]) for x in range(r))
            stats["address_inner_products"] += r
        stats["ordered_words"] += 1
        stats["native_ordered_address_vectors"] += L
        stats["positive_path_observer_operations"] += len(op.observer.operations)
    return table,dict(stats)


def test_at_size(n,p0,p1,delta):
    """Most powerful test at size delta under p0. Return type-II <= delta."""
    den = p0.denominator**n
    A = p0.numerator
    B = p0.denominator-A
    term, mass = B**n, 0
    for k in range(n+1):
        if (mass+term)*delta.denominator >= den*(delta.denominator-delta.numerator):
            break
        mass += term
        term = term*(n-k)*A//((k+1)*B)
    # Accept below k; at k reject with beta_num / beta_den.
    beta_num = (mass+term)*delta.denominator - den*(delta.denominator-delta.numerator)
    beta_den = term*delta.denominator
    assert 0<=beta_num<=beta_den
    if p1==1:
        fits = (k<n or beta_num*delta.denominator >=
                beta_den*(delta.denominator-delta.numerator))
    else:
        A = p1.numerator
        B = p1.denominator-A
        den = p1.denominator**n
        term, mass = B**n,0
        for j in range(k):
            mass += term
            term = term*(n-j)*A//((j+1)*B)
        fits=((mass+term)*beta_den-term*beta_num)*delta.denominator <= den*beta_den*delta.numerator
    return fits,k


def minimum_size(p0,p1,delta=F(1,8)):
    lo,hi=0,1
    while not test_at_size(hi,p0,p1,delta)[0]:
        lo,hi=hi,2*hi
    while hi-lo>1:
        mid=(lo+hi)//2
        if test_at_size(mid,p0,p1,delta)[0]:
            hi=mid
        else:
            lo=mid
    before,after=test_at_size(lo,p0,p1,delta),test_at_size(hi,p0,p1,delta)
    assert not before[0] and after[0]
    return dict(n=hi,tie_bin_at_n=after[1],tie_bin_at_n_minus_one=before[1])


def replay(repo,stage,audit,prior):
    assert digest(prior.read_bytes())==HELPER_SHA
    pkg=repo/"research_notes/directed_recovery/20260926_C6438C"
    assert digest((pkg/"optimization/streaming/lazy_streaming.py").read_bytes())==STREAM_SHA
    raw=gzip.decompress((pkg/"direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz").read_bytes())
    assert digest(raw)==BANK_SHA
    booked=json.loads(raw)["compiled_error_certificate"]
    bounds={r["m"]:F(r["phase_operator_error_bound"]) for r in booked["phase_occurrence_rows"]}
    assert bounds=={2:F(0),3:F(1,8),4:F(1,4)}
    total=sum((M-j+1)*e for j,e in bounds.items())
    assert total==F(booked["operator_norm_bound"])==F(1,2)
    spec=importlib.util.spec_from_file_location("prior_defect",prior)
    lib=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    cls,_,calls,bank,rd,vendor=lib.imports(repo,stage,audit)
    assert vendor["git_blob"]==VENDOR_BLOB
    start_records=len(calls)
    fixtures=[]
    for ix,(N,g,expected) in enumerate(CASES):
        start=len(calls)
        program=cls(N,g,M,bank,61)
        admission=len(calls)-start
        if ix==0:
            words,feedback_cost=feedback_table(lib,rd,program)
        before=len(calls)
        requests,hits=0,[]
        for R in range(1,L):
            ok,cols=lib.certify(program,M,R)
            requests+=len(cols)
            if ok:
                hits.append(R)
        assert hits==([] if expected is None else [expected])
        probe_calls=len(calls)-before
        before=len(calls)
        leaves,cost,peaks=native_tree(lib,program)
        cost.update(peaks)
        cost.update(program_admission_stage45_records=admission,
                    probe_forward_column_requests=requests,probe_stage45_records=probe_calls,
                    tree_stage45_records=len(calls)-before)
        pm=[leaves.get(h,F(0)) for h in words]
        assert all(p==(F(1,L) if not hits else F(1,L)+F(2,L*L)*words[h][L-hits[0]])
                   for h,p in zip(words,pm))
        row=dict(N=N,g=g,returns_checked=hits,native_cost=cost,
                 positive_leaves=len(leaves),full_word_probabilities=list(map(str,pm)))
        if hits:
            r=L-hits[0]
            plus=sum(p for h,p in zip(words,pm) if sign(r,h)==1)
            z=pm[0]
            C=(plus-F(1,2))*L/r
            mu=sum(K[r]**2 for K in words.values())/(L*r*r)
            chi=sum((p*L-1)**2 for p in pm)/L
            assert C==sum(sign(r,h)*K[r] for h,K in words.items())/(L*r)
            assert F(1,10)<C<=1 and C*C<=mu<=1
            assert chi==4*F(r*r,L*L)*mu
            assert z==F(1,L)+F(2*r,L*L)
            tv=sum(abs(p-F(1,L)) for p in pm)/2
            row.update(r=r,score_plus=str(plus),zero_word=str(z),
                       normalized_score_correlation=str(C),normalized_lag_second_moment=str(mu),
                       full_chi_squared=str(chi),score_information_fraction=str(C*C/mu),
                       score_preserves_exact_full_TV=(plus-F(1,2)==tv),
                       full_chi_squared_gain_over_zero=str((L-1)*mu),
                       size_delta_one_eighth=dict(score=minimum_size(F(1,2),plus),
                                                  zero=minimum_size(F(1,L),z)))
            if r==1:
                assert row["score_preserves_exact_full_TV"]
                assert row["size_delta_one_eighth"]["score"]["n"]==857
                assert row["size_delta_one_eighth"]["zero"]["n"]==5374
        else:
            assert all(p==F(1,L) for p in pm)
            assert all(sum(p for h,p in zip(words,pm) if sign(r,h)==1)==F(1,2)
                       for r in range(1,L//2+1))
        fixtures.append(row)
    return dict(bank_sha256=BANK_SHA,whole_carrier=61,vendor_blob=VENDOR_BLOB,
                verified_error_bounds={str(j):str(x) for j,x in bounds.items()},
                weighted_bank_error=str(total),stage45_records_after_import=start_records,
                ordered_inner_product_audit=feedback_cost,actual_cases=fixtures)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--stage",type=Path,required=True)
    p.add_argument("--audit",type=Path,required=True)
    p.add_argument("--wave18",type=Path,default=Path(__file__).resolve().parents[1]/
                   "eighteenth/return_defect_check.py")
    args=p.parse_args()
    print(json.dumps(replay(args.repo.resolve(),args.stage.resolve(),args.audit.resolve(),
                            args.wave18.resolve()),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
