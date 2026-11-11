from itertools import product
from pathlib import Path
import json
from lifetime_certificates import *
here=Path(__file__).resolve().parent

def main():
    setups=[((0,0),(1,0)),((0,0),(0,1),(0,0)),((1,1),(2,0)),((2,0),(1,1),(2,1))]
    tables=list(product(range(10),repeat=2)); out=[]; fallback=match=0
    for tau in setups:
        values=[]; hints={}
        for x in tables:
            p=optimal_certificate(x,tau)
            assert p[0]==sequential_oracle(2,tau,x)
            values.append(p[0]);hints[p]=1
        for p in hints:
            for x in tables:
                def read(i,b):return (x[i]>>b)&1
                tag,keys,n=verify_or_fallback(2,tau,p,read)
                live=list(x)
                for ((t,d),k) in zip(tau,keys):
                    assert k not in live and t*3<k<=(t+1)*3
                    live[d]=k
                if tag=='certificate':
                    match+=1
                    assert 8*n+sum(weight(2,k) for k in keys)==p[0]
                else:fallback+=1
        out.append(dict(rounds=tau,distinct_hints=len(hints),pointwise_range=[min(values),max(values)],uniform_full_identity_minimax=sequential_oracle(2,tau)))
    tau=setups[0]; p=optimal_certificate((1,1),tau)
    assert p[:2]==(22,(2,6))
    physical=(22,(2,6),(2,2),(0,0))
    assert verify_or_fallback(2,tau,physical,lambda i,b: (1>>b)&1)==('certificate',(2,6),2)
    H=(8,9,10,12,11,13,14,15);G=H[:-1]+(4,)
    def W(keys,T):return (T//8)*sum(weight(14,k) for k in keys)+sum(weight(14,k) for k in keys[:T%8])
    th=[]
    for t in (8,216,223,224,225,231,232):
        high=112+82*t+W(H,t);extra=168+82*t+W(G,t)
        th.append(dict(T=t,high=high,expanded=extra,optimal=min(high,extra)))
    assert th[-1]['high']==20296 and th[-1]['expanded']==20294
    for missing in H[:4]:
        rem=sorted(weight(14,k) for k in range(1,16) if k!=missing)[:8]
        for j in range(9):assert sum(rem[:j])>=sum(weight(14,k) for k in H[:j])
    ret=dict(basis="full identity, independent initial table 0..9, fixed target library of three; values exclude fixed business words unless marked",table_schedule_equalities=len(tables)*len(setups),cases=out,hint_matches=match,hint_fallbacks=fallback,alias_example=dict(initial=[1,1],rounds=tau,variable=22,fixed=127,total=149,keys=p[1],minimum_masks=p[2],answers=p[3],physical_masks=physical[2],physical_answers=physical[3]),threshold_r14=th)
    (here/'certificate_results.json').write_text(json.dumps(ret,indent=2)+'\n');print(json.dumps(ret))
if __name__=='__main__':main()
