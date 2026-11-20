#!/usr/bin/env python3
"""PREFIX-957B: complete lossless Q19 k=21,23 named XOR joint census.
No prior pair population is used for primary generation.
Optional --prior-ids independently audits all named source equations.
Exact integers; no third-party packages.
"""
import argparse, hashlib, json, struct, time
from collections import defaultdict, Counter
from pathlib import Path

P=19
K=21
H=1<<(P-1)
LOW=H+1
HI=2*H-1
N=H//2
PRIOR_HASH="1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75"

def dictionary(p):
    data=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1,1):
                data[(1<<i)-s*(1<<j)].append((i,j,s))
    return dict(data)

def actual_count(prod, triples):
    return sum(s==1-2*((prod>>j)&1) for i,j,s in triples)

def generate():
    begin=time.perf_counter()
    D=dictionary(P)
    named=Counter()
    gaps=defaultdict(Counter)
    stats=Counter()
    # PREVIOUSLY PROVED bounded gap: 0<=m<=6.
    for m in range(7):
        for c, cs in D.items():
            for C, Cs in D.items():
                delta=C-c
                if m%2 and delta%2!=1: continue
                if m%4==0 and delta%4!=2: continue
                if m%4==2 and delta%4!=0: continue
                stats["numeric_residual_pairs_after_mod4"]+=1
                B=K*C-(K+2)*c
                # Any positive quotient t lies in [1,2*k].
                for t in range(1,2*K+1):
                    T=t+m
                    d=2*t-K*m
                    if d==0:
                        # For k21, the only cases are (m,t)=(2,21) or (4,42):
                        # a=b or a=2b; both excluded from offdiagonal Q19.
                        stats["resonance_divisor_zero_tests"]+=1
                        continue
                    stats["scalar_divisibility_tests"]+=1
                    if B%d:continue
                    b=B//d
                    if not(LOW<=b<=HI and b&1):continue
                    A=t*C-T*c
                    if A%d:continue
                    a=A//d
                    if not(LOW<=a<=HI and a&1 and a!=b):continue
                    stats["ordered_domain_candidate_tests"]+=1
                    assert K*a-t*b==c
                    assert (K+2)*a-T*b==C
                    v=actual_count(K*a,cs)
                    w=actual_count((K+2)*a,Cs)
                    stats["source_triples_checked"]+=len(cs)+len(Cs)
                    if v and w:
                        ident=((a-LOW)//2)*N+(b-LOW)//2
                        named[ident]+=v*w
                        gaps[m][ident]+=v*w
    counts={m:sum(gaps[m].values()) for m in range(7)}
    pair_counts={m:len(gaps[m]) for m in range(7)}
    assert [counts[m] for m in range(7)]==[6,614,6509,1286,231,3,0]
    assert [pair_counts[m] for m in range(7)]==[6,442,4724,839,190,3,0]
    assert len(named)==6203 and sum(named.values())==8649
    binary=b"".join(struct.pack("<Q",ident) for ident in sorted(named))
    digest=hashlib.sha256(binary).hexdigest()
    assert digest==PRIOR_HASH
    return named,gaps,binary,{"population":"ordered Q19 offdiagonal p=19 k=21,23",
        "frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "numeric_residual_count":len(D),
        "numeric_residual_formula":"(3*p*p-5*p+10)//2",
        "distinct_pairs":len(named),"named_joint_histories":sum(named.values()),
        "gap_named_histories":counts,"gap_pair_memberships":pair_counts,
        "source_multiplicity_histogram":dict(sorted(Counter(named.values()).items())),
        "binary_sha256":digest,"binary_bytes":len(binary),
        "stats":dict(stats),"primary_seconds_observed":round(time.perf_counter()-begin,6),
        "review":"AUTHOR_COMPUTED_NOT_INDEPENDENTLY_ADMITTED"}

def direct_audit(named,old):
    assert hashlib.sha256(old).hexdigest()==PRIOR_HASH
    assert len(old)==6203*8
    ids=struct.unpack("<6203Q",old)
    assert ids==tuple(sorted(set(ids)))
    direct=Counter()
    by_gap=Counter()
    for ident in ids:
        a=LOW+2*(ident//N)
        b=LOW+2*(ident%N)
        assert a!=b
        fibers=[]
        for k in (K,K+2):
            f=Counter()
            v=k*a
            for i in range(P):
                for j in range(P):
                    x=(v^(1<<j))-(1<<i)
                    if x>0 and x%b==0:
                        f[x//b]+=1
            fibers.append(f)
        for t,v in fibers[0].items():
            for T,w in fibers[1].items():
                assert 0<=T-t<=6
                direct[ident]+=v*w
                by_gap[T-t]+=v*w
    assert direct==named
    return {"original_named_xor_tests":len(ids)*2*P*P,
        "all_per_pair_multiplicities_equal":True,
        "offdiagonal_pairs":len(direct),"joint_histories":sum(direct.values()),
        "gap_named_histories":dict(by_gap)}

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--prior-ids",type=Path)
    cli.add_argument("--prefix",default="PREFIX957B_R6")
    args=cli.parse_args()
    named,gaps,binary,report=generate()
    Path(args.prefix+"_NONDIAGONAL_IDS.bin").write_bytes(binary)
    if args.prior_ids:
        report["independent_original_xor_audit"]=direct_audit(named,args.prior_ids.read_bytes())
    Path(args.prefix+"_EXACT_RESULTS.json").write_text(json.dumps(report,sort_keys=True,indent=2)+"\n")
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
