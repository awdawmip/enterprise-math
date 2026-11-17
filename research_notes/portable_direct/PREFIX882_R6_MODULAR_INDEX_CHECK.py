#!/usr/bin/env python3
"""PREFIX-882 exact residue-index collision checker for the auxiliary named-source observer.
No external dependencies; arbitrary-precision Python arithmetic.
"""
from math import gcd
import json, random


def dp_witness(p,a,d,e):
    N=1<<p
    L=max(0,-a,-d,-a-e)
    U=min(N-1,N-1-a,N-1-d,N-1-a-e)
    if L>U: return None
    di=abs(d).bit_length()-1 if d else -1
    ei=abs(e).bit_length()-1 if e else -1
    states={(0,0,0):0}
    for i in range(p):
        ai=(a>>i)&1; li=(L>>i)&1; ui=(U>>i)&1
        nxt={}
        for (carry,lower,upper),prefix in states.items():
            for bit in (0,1):
                sum_=bit+ai+carry
                ybit=sum_&1
                if (i==di and bit!=(0 if d>0 else 1)) or (i==ei and ybit!=(0 if e>0 else 1)):
                    continue
                kl=(bit < li+lower)
                ku=(ui < bit+upper)
                key=(sum_>>1,int(kl),int(ku))
                if key not in nxt: nxt[key]=prefix+(bit<<i)
        states=nxt
        if not states:return None
    for (carry,lower,upper),x in states.items():
        if lower==upper==0:
            assert L<=x<=U
            assert (x+d)==(x^abs(d)) if d else True
            assert ((x+a+e)==((x+a)^abs(e))) if e else True
            return x
    return None


def indexed_collision(p,q1,q2,stats=False):
    if not (p>=1 and q1>0 and q2>0): raise ValueError
    N=1<<p
    K=(N-1)//q1
    g=gcd(q1,q2)
    m=q2//g
    inv=pow(q1//g,-1,m) if m>1 else 0
    D=(0,)+tuple(v for i in range(p) for v in (1<<i,-(1<<i)))
    n_pairs=n_k=n_dp=0
    for d in D:
        for e in D:
            n_pairs+=1
            delta=d-e
            if delta%g: continue
            k0=(delta//g*inv)%m if m>1 else 0
            for k in range(k0,K+1,m):
                n_k+=1
                if k==0 and d==e: continue
                a=k*q1
                n_dp+=1
                x=dp_witness(p,a,d,e)
                if x is None:continue
                X=(x,x+d); Y=(x+a,x+a+e)
                assert X!=Y
                assert all(0<=v<N for v in X+Y)
                assert X[0]^X[1] in ((0,)+(tuple(1<<i for i in range(p))))
                assert Y[0]^Y[1] in ((0,)+(tuple(1<<i for i in range(p))))
                assert (X[0]%q1,X[1]%q2)==(Y[0]%q1,Y[1]%q2)
                out={'p':p,'q1':q1,'q2':q2,'gcd':g,'period':m,'K':K,'k':k,'a':a,'d':d,'e':e,'X':X,'Y':Y}
                if stats:out.update({'pairs_checked':n_pairs,'admissible_ks_checked':n_k,'DP_checked':n_dp})
                return out
    if stats:return {'p':p,'q1':q1,'q2':q2,'gcd':g,'period':m,'K':K,'injective':True,'pairs_checked':n_pairs,'admissible_ks_checked':n_k,'DP_checked':n_dp}
    return None


def brute_collision(p,q1,q2):
    N=1<<p
    seen=set()
    for u in range(N):
        for v in (u,)+tuple(u^(1<<i) for i in range(p)):
            obs=(u%q1,v%q2)
            if obs in seen:return True
            seen.add(obs)
    return False


def main():
    n=0; neq=0
    per=[]
    for p,Q in ((3,15),(4,31),(5,63),(6,15),(7,15)):
        col=inj=0
        for q1 in range(1,Q+1,2):
            for q2 in range(1,Q+1,2):
                got=indexed_collision(p,q1,q2) is not None
                expect=brute_collision(p,q1,q2)
                assert got==expect,(p,q1,q2,got,expect)
                n+=1
                col+=got;inj+=not got
        per.append({'p':p,'Q':Q,'pairs':col+inj,'collision':col,'injective':inj})
    rng=random.Random(882)
    cases=[]
    for _ in range(128):
        q1=rng.randrange(500001,524288,2)
        q2=rng.randrange(500001,524288,2)
        v=indexed_collision(32,q1,q2,True)
        assert (v is None or v.get('injective') or tuple(v['X'])!=tuple(v['Y']))
        cases.append(v)
    sample=cases[:8]
    strip=[]
    strip_injective=[]
    max_strip_dp=0
    max_strip_pairs=0
    for q1 in range(523001,524288,2):
        for q2 in range(523001,524288,2):
            z=indexed_collision(32,q1,q2,True)
            if 'X' not in z:
                strip_injective.append([q1,q2])
            max_strip_dp=max(max_strip_dp,z['DP_checked'])
            max_strip_pairs=max(max_strip_pairs,z['pairs_checked'])
    assert not strip_injective
    out={
        'schema':'PREFIX882_EXACT_MODULAR_INDEX_RESULTS_V1',
        'method':'Exact modular inverse and bit carry-borrow feasibility DP',
        'exhaustive_small_cases':per,
        'exhaustive_pair_count':n,
        'p32_deterministic_seed':882,
        'p32_q_range':[500001,524287],
        'p32_pairs_tested':len(cases),
        'p32_collision_pairs':sum('X' in c for c in cases),
        'p32_injective_pairs':sum(c.get('injective',False) for c in cases),
        'p32_max_DP_checked':max(c['DP_checked'] for c in cases),
        'p32_mean_DP_checked':round(sum(c['DP_checked'] for c in cases)/len(cases),3),
        'p32_sample_witnesses':sample,
        'p32_complete_strip':{
            'odd_q1_q2_from':523001,
            'odd_q1_q2_to':524287,
            'odd_moduli_count':644,
            'ordered_pairs_checked':414736,
            'explicit_collisions_found':414736,
            'injective_pairs':strip_injective,
            'max_dp_calls_per_pair':max_strip_dp,
            'max_d_e_pairs_before_witness':max_strip_pairs,
            'verification':'exact candidate enumeration, complete carry/borrow DP and independently checked XOR/remainders per witness'
        },
        'conclusion':'EXACT_ALGORITHM_AND_DECLARED_FINITE_TESTS_ONLY'
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
