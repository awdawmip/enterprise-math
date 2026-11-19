"""Marked visits and first returns of the frozen iid signed six-axis kernel."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from math import comb, log, pi, e
from pathlib import Path
import json

SOURCE_SHA="4931b82017d44ba1d6b3a1b4c91c0d7a8557739f15d065a455dbdf4a72f03436"
STEPS=(1,2,3,4,6,8,12,16,24,32,48,64,96,128)
DIGEST="5b0835054cce814727fedd4a10879eeef753616c29ca17f66c8a2ca8967ee1d9"


def single_triple(horizon):
    """Labelled signed words ending at (a,a,a); interleave the three one-axis words."""
    hits=[{} for _ in range(horizon+1)]
    for a in range(horizon//3+1):
        ways=[int(j>=a and (j-a)%2==0)*comb(j,(j-a)//2) if j>=a else 0
              for j in range(horizon+1)]
        prev=ways
        for _ in range(2):
            prev=[sum(comb(n,j)*ways[j]*prev[n-j] for j in range(a,n+1,2))
                  for n in range(horizon+1)]
        for n,weight in enumerate(prev):
            if weight:
                hits[n][a]=weight
                hits[n][-a]=weight
    return hits


def marked_counts(horizon):
    group=single_triple(horizon)
    visits=[]
    first=[{}]
    for n in range(horizon+1):
        row=defaultdict(int)
        for j in range(n+1):
            shuffle=comb(n,j)
            for a,left in group[j].items():
                base=shuffle*left
                for b,right in group[n-j].items():
                    row[a-b]+=base*right
        visits.append(dict(row))
        if not n: continue
        taboo=dict(row)
        for j in range(1,n):
            for h,x in first[j].items():
                for k,y in visits[n-j].items():
                    taboo[h+k]-=x*y
        assert all(i>0 for i in taboo.values())
        valid=set(range(-n//3-1,n//3+1))
        valid={i for i in valid if 3*abs(i)<=n and (n-i)%2==0}
        assert set(taboo)==valid
        first.append(taboo)
    return visits,first


def raw_walk(cut):
    """Propagate actual integer coordinates; remove the full H4-plane after its first visit."""
    zero=(0,)*6
    live=Counter({zero:1})
    out=[{}]
    for n in range(1,cut+1):
        next_state=Counter()
        hit=Counter()
        for x,v in live.items():
            for axis in range(6):
                for sign in (-1,1):
                    y=x[:axis]+(x[axis]+sign,)+x[axis+1:]
                    if y[0]==y[2]==y[4] and y[1]==y[3]==y[5]:
                        hit[y[0]-y[1]]+=v
                    else:
                        next_state[y]+=v
        assert sum(next_state.values())+sum(hit.values())==12*sum(live.values())
        out.append(dict(hit))
        live=next_state
    return out


def interval(lo,hi):
    scale=10**8
    return [lo.numerator*scale//lo.denominator,-((-hi.numerator*scale)//hi.denominator)]


def digest_rows(table):
    s="\n".join(f"{n},{m},{value}" for n,row in enumerate(table) for m,value in sorted(row.items()))+"\n"
    return sha256(s.encode()).hexdigest()


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",type=Path,help="optional official frozen hidden_plane_results.json")
    p.add_argument("--out",type=Path)
    args=p.parse_args()
    visits,first=marked_counts(128)
    assert raw_walk(10)==first[:11]
    marginal=[F(sum(row.values()),12**n) for n,row in enumerate(visits)]
    certificate="\n".join(str(marginal[n]) for n in STEPS)+"\n"
    assert sha256(certificate.encode()).hexdigest()==DIGEST
    if args.source:
        raw=args.source.read_bytes()
        assert sha256(raw).hexdigest()==SOURCE_SHA
        native=json.loads(raw)
        assert native["U"]==[["1","0"]*3,["0","1"]*3]
        assert native["routing_cases"][0]["axis_probabilities"]==["1/6"]*6
        rows=native["hidden_returns"]["rows"]
        assert tuple(j["n"] for j in rows)==STEPS
        assert all(F(j["hidden_zero_probability"])==marginal[j["n"]] for j in rows)
    N=128
    g0=sum(marginal)
    # Fourier bound u_n <= 6/n^2 + 2^-n.
    # On [-1,1]^4 integration of the full triangular quadratic form costs < 3/(4*n^2).
    # On its complement a positive mode is <= 133/144, and all negative modes have modulus <= 1/2.
    t=F(133,144)
    g1=g0+F(3,4*N)+t**(N+1)/(1-t)+F(1,2**N)
    assert g1<2
    r0,r1=1-1/g0,1-1/g1
    rows=[]
    for n in STEPS:
        f=first[n]
        total=sum(f.values())
        # The support statement applies even if an early time has no positive return event.
        H=-sum((x/total)*log(x/total) for x in f.values()) if total else None
        rows.append({"n":n,"visits":str(marginal[n]),"first_mass":str(F(total,12**n)),
                     "labels":sorted(f),"first_integer_counts":{str(m):x for m,x in sorted(f.items())},
                     "entropy_nats":None if H is None else f"{H:.12g}",
                     "entropy_leading_nats":f"{0.5*log(2*pi*e*n/9)-log(2):.12g}"})
    truncated=sum(F(sum(r.values()),12**n) for n,r in enumerate(first))
    assert truncated<r1
    r0=max(r0,truncated)
    g32=sum(marginal[:33])
    assert g32+F(6,32)+F(1,2**32)<2
    result={"published_hidden_source_sha256":SOURCE_SHA,"published_probability_digest":DIGEST,
            "horizon":N,"horizon_full_visits_integer_hash":digest_rows(visits),
            "horizon_full_first_integer_hash":digest_rows(first),"whole_native_killed_DP_to":10,
            "outward_interval_scale":10**8,"G4":interval(g0,g1),"return_prob":interval(r0,r1),
            "escape_prob":interval(1/g1,1/g0),"rho_by_horizon":interval(truncated,truncated),
            "strict_G4_bound_using_only_32_steps":interval(g32,g32+F(6,32)+F(1,2**32)),
            "first_hit_rows":rows}
    content=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.out: args.out.write_text(content)
    else: print(content,end="")


if __name__=="__main__":
    main()
