#!/usr/bin/env python3
"""R284ES exact finite checker; no external packages or Port recomputation."""
from itertools import combinations
import json
from pathlib import Path

def subsets(t,b):
    return tuple(combinations(range(t),b))

def conflict(t,s,J,K):
    return len(set(J)|set(K)) >= t-2*s

def possible(t,s,a,J,w):
    j=set(J)
    return sum(((w>>p)&1)!=a for p in range(t) if p not in j)<=s

def graph(t,b,s=0):
    v=subsets(t,b)
    return v,[(i,j) for i in range(len(v)) for j in range(i+1,len(v)) if conflict(t,s,v[i],v[j])]

def verify_code(t,b,s,u,code,h):
    v,E=graph(t,b,s)
    assert len(code)==len(v) and all(0<=x<(1<<h) for x in code)
    assert t>=2*s+b+1
    for i,j in E:
        assert (code[i]^code[j]).bit_count()>=2*u+1
    for i,J in enumerate(v):
        for j,K in enumerate(v):
            metadata_overlap=(code[i]^code[j]).bit_count()<=2*u
            data_overlap=any(possible(t,s,0,J,w) and possible(t,s,1,K,w) for w in range(1<<t))
            assert not(metadata_overlap and data_overlap)
    return len(E)

def main():
    checked=0
    for t in range(1,8):
        for b in range(min(t,3)+1):
            v=subsets(t,b)
            for s in range(2):
                for J in v:
                    for K in v:
                        observed=any(possible(t,s,0,J,w) and possible(t,s,1,K,w) for w in range(1<<t))
                        assert observed==conflict(t,s,J,K)
                        checked+=1
    t6_v,_=graph(6,3)
    t6_codes=[0 if J<tuple(i for i in range(6) if i not in J) else 7 for J in t6_v]
    cases=[
        (4,3,0,0,[0,1,2,3],2),
        (4,3,0,1,[0b00000,0b11100,0b10011,0b01111],5),
        (5,3,0,1,[0,1,2,5,6,7,9,10,11,15],4),
        (6,3,0,1,t6_codes,3),
        (7,3,0,1,[0]*35,0),
    ]
    out=[]
    for t,b,s,u,codes,h in cases:
        e=verify_code(t,b,s,u,codes,h)
        out.append(dict(t=t,b=b,s=s,u=u,metadata_bits=h,total_bits=t+h,conflict_edges=e,codewords=[format(x,'0%db'%h) if h else '' for x in codes]))
    cycle=[(2,3,4),(0,1,4),(1,2,3),(0,3,4),(0,1,2)]
    assert all(conflict(5,0,cycle[i],cycle[(i+1)%5]) for i in range(5))
    cert=dict(schema='R284ES_EXACT_METADATA_AMBIGUITY_CERT_V1',exhaustive_pair_scenarios=checked,
              cases=out,odd_cycle_t5_b3=cycle,sharp_global_total_b3_s0={'metadata_flips_0':6,'metadata_flips_at_least_1':7},independent_review=False)
    print(json.dumps(cert,ensure_ascii=False,indent=2))
    assert checked==5402
    assert [x['conflict_edges'] for x in out]==[6,6,15,10,0]

if __name__=='__main__':
    main()
