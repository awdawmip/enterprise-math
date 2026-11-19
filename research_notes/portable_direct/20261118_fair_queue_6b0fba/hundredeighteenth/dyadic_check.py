"""Audit of the finite-bit classifier on the original four-round readout."""
import argparse
import gzip
import hashlib
import json
import os
import sys
from collections import Counter,defaultdict
from fractions import Fraction
from math import gcd
from pathlib import Path

BANK_SHA="79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c"
VENDOR="4e6b3132580e3cd70a20a0d8bd4d28792b961afb"
INPUTS=[(3,1),(3,2),(7,2),(5,2),(11,3),(21,2),(29,7),(17,2),(19,4),
        (11,2),(23,2),(13,2),(53,10),(29,4),(31,7),(17,3),(103,8)]


def two_power(q):
    return q>0 and q & (q-1)==0


def structure(t,d):
    D=d//(d & -d)
    j0=D.bit_length()+1
    bounded=(D==1 or d>=2**(t-1))
    first=None
    for j in range(1,t+1):
        modulus=d//gcd(d,2**(t-j))
        # Each preimage is k=r+l*modulus in [0,2^j); the two arms are its parities.
        widths=(2**j//modulus,(2**j+modulus-1)//modulus)
        if bounded and D!=1 and modulus%2==1:
            assert widths[1]<=2
        if modulus%2==1 and 3 in widths and D!=1 and first is None:
            first=j
    if not bounded:
        assert first==j0
        return j0,min(2**j0-2*D,4*D-2**j0)
    assert first is None
    return None,0


def run_native(repo,stage):
    rec=repo/"research_notes/directed_recovery"
    pkg,earlier=rec/"20260926_C6438C",rec/"20260926_0C08F0"
    os.environ.update(BRC_STAGE87_SOURCE=str(stage),BRC_STREAMING_PREVIOUS=str(earlier),
                      BRC_ZERO_ENDPOINT_SOURCE=str(earlier/"adversarial/zero_endpoint_extension.py"))
    for path in (stage,pkg/"new_word_compiler",pkg/"optimization/streaming",
                 rec/"20260927_C6438C/qft_row_queries/gram_research"):
        sys.path.insert(0,str(path))
    from compiled_streaming import bank_from_compilation
    from lazy_streaming import LazyStreamingProgram
    from single_walker import PointRowOracle,transition_plan
    from stage45.brc_loop_recheck import CALLS,verify_vendor
    assert verify_vendor()["git_blob"]==VENDOR
    raw=gzip.decompress((pkg/"direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz").read_bytes())
    assert hashlib.sha256(raw).hexdigest()==BANK_SHA
    start=len(CALLS)
    bank=bank_from_compilation(json.loads(raw)["phase_compilation"],t=4,epsilon=Fraction(1))["bank"]
    bank_calls=len(CALLS)-start
    result=[]
    for d,(N,a) in enumerate(INPUTS,1):
        start=len(CALLS)
        prog=LazyStreamingProgram(N,a,4,bank,61)
        labels=[1]
        while True:
            z=prog.tables[-1][labels[-1]]
            if z==1:
                break
            assert z not in labels
            labels.append(z)
        assert len(labels)==d
        j0,wcount=structure(4,d)
        live={((),1):Fraction(1)}
        cells_total=0
        alternate=Counter()
        nondyadic=[]
        peaks=[]
        terminals=0
        for j in range(1,5):
            child=defaultdict(Fraction)
            cells={}
            raw_calls=0
            for h in sorted({h for h,_ in live}):
                oracle=PointRowOracle(prog,h)
                for (hh,prev),mass in live.items():
                    if h!=hh:continue
                    for coin in (0,1):
                        plan=transition_plan(oracle,prev,coin)
                        raw_calls+=1
                        z=plan["candidate"]
                        prob=plan["bit_probability_given_proposed_label"]
                        key=(h,z)
                        recp=cells.setdefault(key,[prob,Fraction(0)])
                        assert recp[0]==prob
                        recp[1]+=mass/2
                        for bit,f in ((0,prob),(1,1-prob)):
                            if f:
                                child[h+(bit,),z]+=mass*f/2
            assert sum(child.values())==sum(x[1] for x in cells.values())==1
            for (h,z),(prob,w) in cells.items():
                if not two_power(prob.denominator):
                    nondyadic.append((j,h,z,prob,w))
                    if j==j0 and not any(h) and prob==Fraction(9,10):
                        alternate[z]=w
            peaks.append([len(cells),raw_calls,max(p.denominator.bit_length()-1 for p,_ in cells.values() if two_power(p.denominator))])
            cells_total+=len(cells)
            live=child
        assert all(two_power(x.denominator) for x in live.values())
        assert bool(nondyadic)==bool(wcount) and len(alternate)==wcount
        if wcount:
            assert set(alternate.values())=={Fraction(5,2*4**(j0-1))}
        result.append({"input_N_a":[N,a],"order_checked_by_native_columns":d,
                       "positive_cells_and_transition_calls_and_max_dyadic_exponent_by_round":peaks,
                       "nondyadic_cells":len(nondyadic),"first_zeros_round":j0,
                       "zeros_witness_label_masses":{str(k):str(v) for k,v in sorted(alternate.items())},
                       "positive_terminal_joint_histories_labels":len(live),
                       "actual_BRC_calls":len(CALLS)-start})
    return {"bank_sha256":BANK_SHA,"vendor_git_blob":VENDOR,"bank_creation_calls":bank_calls,"runs":result}


def periodic_check():
    windows,classes,full=0,0,0
    for d in range(1,144):
        D=d//(d & -d)
        if D==1: continue
        for j in range(1,11):
            # Align the j-th window no later than t-v2(d).
            counts=Counter(k%D for k in range(2**j))
            k0=2*((2**j)//(2*D))+1
            rem=2**j%(2*D)
            c=min(rem,2*D-rem)
            odds=[k for k in counts.values() if k%2]
            assert len(odds)==c and all(k==k0 for k in odds)
            mass=sum(Fraction(((k+1)//2)**2+(k//2)**2, 2*4**(j-1))
                     for k in counts.values() if k%2 and k>1)
            assert mass==(Fraction(c*(k0*k0+1),4**j) if k0>1 else 0)
            windows+=1
            classes+=len(counts)
    for D in range(3,128,2):
        orbit=[1]
        while (v:=2*orbit[-1]%D)!=1: orbit.append(v)
        lifted=set(orbit)|{(-v)%D for v in orbit}
        if len(lifted)==sum(gcd(x,D)==1 for x in range(D)):
            pset=[p for p in range(2,D+1) if D%p==0 and all(p%j for j in range(2,int(p**0.5)+1))]
            rad=1
            for p in pset:rad*=p
            avg=Fraction(2*sum(min(v,D-v) for v in orbit),D*D*len(orbit))
            assert avg==Fraction(1,2*D)-Fraction((-1)**len(pset)*rad,2*D**3)
            full+=1
    return dict(zero_history_windows=windows,positive_label_classes=classes,closed_period_means=full)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,default=Path("/workspace/enterprise-math"))
    ap.add_argument("--stage",type=Path,required=True,help="pinned RP14_Run directory")
    args=ap.parse_args()
    extra=0
    for t in range(2,13,2):
        for d in range(1,2**t+4):
            j,n=structure(t,d)
            if n:
                D=d//(d&-d)
                occ=Counter(k%D for k in range(2**j))
                assert sum(b==3 for b in occ.values())==n
            extra+=1
    data=run_native(args.repo.resolve(),args.stage.resolve())
    data["independent_address_cases"]=extra
    data["zero_history_mass_checks"]=periodic_check()
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
