"""Exact rational certificate for direct occupancy Markovization, N=3 BRC tree.
Independent recomputation of the finite tree and sample policies, no network used.
"""
from fractions import Fraction as F
from random import Random
import json

NODES={
'':(0,('a','b')),'a':(1,('ax','ay')),'b':(1,('bu','bv')),
'ax':(2,('axL','axM','axH')),'ay':(2,('ayT',)),
'bu':(2,('buL','buM','buH')),'bv':(2,('bvT',)),
'axL':(3,()),'axM':(3,()),'axH':(3,()),'ayT':(3,()),
'buL':(3,()),'buM':(3,()),'buH':(3,()),'bvT':(3,())}
R={'':F(1),'a':F(3,2),'b':F(1,2),'ax':F(1),'ay':F(2),
'bu':F(1),'bv':F(1,3),'axL':F(1,2),'axM':F(1),'axH':F(3,2),
'buL':F(1,2),'buM':F(1),'buH':F(3,2),'ayT':F(2),'bvT':F(1,3)}
def qmass(sa,sb):
    q={'':F(1),'a':F(1,2),'b':F(1,2),'ax':F(1,4),'ay':F(1,4),
        'bu':F(1,8),'bv':F(3,8),'ayT':F(1,4),'bvT':F(3,8)}
    for h,s,m in [('ax',sa,F(1,4)),('bu',sb,F(1,8))]:
        for k,p in zip('LMH',(s,1-2*s,s)):
            q[h+k]=m*p
    for h,(t,ch) in NODES.items():
        assert q[h]>0 and q[h]*R[h]>0
        if ch:
            assert sum((q[c] for c in ch),F(0)) == q[h]
            assert sum((q[c]*R[c] for c in ch),F(0)) == q[h]*R[h]
    return q
def normalize(ws):
    s=sum(ws)
    return tuple(F(w,s) for w in ws) if s else tuple([F(1,len(ws))]*len(ws))
def random_policy(rng):
    return {h:normalize([rng.randrange(9) for _ in range(2 if t==3 else 3)])
            for h,(t,_) in NODES.items()}
def visits(policy,q):
    v={}
    def go(h,s):
        v[h]=q[h]*s
        for c in NODES[h][1]:go(c,s*policy[h][2])
    go('',F(1))
    return v
def direct_markovize(pi,sa,sb):
    # Average actions using the actual Q-law occupation masses.
    q=qmass(sa,sb); v=visits(pi,q); A={}
    for h,(t,_) in NODES.items():
        z=(t,R[h])
        if z not in A: A[z]=[F(0)]*len(pi[h])
        for j,prob in enumerate(pi[h]): A[z][j]+=v[h]*prob
    by_state={z:normalize(actions) for z,actions in A.items()}
    return {h:by_state[(NODES[h][0],R[h])] for h in NODES}
def law(policy,sa,sb,which):
    q=qmass(sa,sb); v=visits(policy,q)
    out={(t,d):F(0) for t in range(4) for d in ('P','Q')}
    for h,(t,_) in NODES.items():
        m=v[h]*(R[h] if which=='P' else 1)
        out[(t,'P')]+=m*policy[h][0]
        out[(t,'Q')]+=m*policy[h][1]
    assert sum(out.values())==1
    return out
def tv(x,y):return sum((abs(x[k]-y[k]) for k in x),F(0))/2
def times(x):return {t:sum((v for (j,d),v in x.items() if j==t),F(0)) for t in range(4)}
def exact_collision_data(pi,sa,sb):
    q=qmass(sa,sb);v=visits(pi,q)
    wa,wb=v['ax'],v['bu']
    k=wa*wb/(wa+wb) if wa+wb else F(0)
    ca,cb=pi['ax'][2],pi['bu'][2]
    return wa,wb,k,ca,cb
def witness():
    pi={h:((F(1),F(0)) if t==3 else (F(1),F(0),F(0)))
        for h,(t,_) in NODES.items()}
    for h in ('','a','b','ax'):pi[h]=(F(0),F(0),F(1))
    for h in ('axL','axH','buL','buH'):pi[h]=(F(0),F(1))
    for h in ('axM','buM'):pi[h]=(F(1),F(0))
    return pi
def main():
    pairs=[(F(2,5),F(1,3)),(F(1,6),F(1,5)),
           (F(1,100),F(49,100)),(F(1,3),F(1,3)),
           (F(7,20),F(31,100)),(F(49,100),F(1,100))]
    rng=Random(2026102720); trials=0; maxratio=F(0)
    for sa,sb in pairs:
        delta=abs(sa-sb)
        for _ in range(128):
            pi=random_policy(rng); sigma=direct_markovize(pi,sa,sb)
            wa,wb,k,ca,cb=exact_collision_data(pi,sa,sb)
            assert k<=F(1,12)
            for which in ('P','Q'):
                original=law(pi,sa,sb,which)
                compressed=law(sigma,sa,sb,which)
                gap=tv(original,compressed)
                assert times(original)==times(compressed)
                assert gap<=2*k*abs(ca-cb)*delta, (gap,k,ca,cb,delta)
                assert gap<=delta/6
                if delta:maxratio=max(maxratio,gap/delta)
            trials+=1
    wa,wb,k,ca,cb=exact_collision_data(witness(),F(2,5),F(1,3))
    assert (wa,wb,k,ca,cb)==(F(1,4),F(1,8),F(1,12),F(1),F(0))
    witness_tv={}
    for which in ('P','Q'):
        pi=witness();sig=direct_markovize(pi,F(2,5),F(1,3))
        witness_tv[which]=str(tv(law(pi,F(2,5),F(1,3),which),law(sig,F(2,5),F(1,3),which)))
        assert witness_tv[which]=='1/90'
    # Sharpness of this direct algorithm is not global compression sharpness:
    sa,sb=F(2,5),F(1,3)
    pi=witness();sig=direct_markovize(pi,sa,sb)
    for h,(t,_) in NODES.items():
        if t==3: sig[h]=(F(1)-2*sa,2*sa)
    for which in ('P','Q'):
        assert law(pi,sa,sb,which)==law(sig,sa,sb,which)
    print(json.dumps({'status':'PASS_EXACT_FRACTION','model':'15_prefix_8_terminal_N3',
        'parameter_pairs':[[str(x),str(y)] for x,y in pairs],
        'sampled_history_policies':trials,'probability_laws':['P','Q'],
        'uniform_direct_shadow_coefficient':'1/6',
        'pointwise_bound':'TV_R <= 2*k*abs(ca-cb)*abs(sa-sb) for R=P,Q',
        'k_bound':'1/12','witness_parameters':['2/5','1/3'],
        'witness_k':'1/12','witness_direct_markovized_TV':witness_tv,
        'witness_direct_coefficient_sharp':True,
        'same_witness_other_compressor_exact':True,
        'stop_time_laws_exact':True,
        'qualification':'1/6 is sharp for direct Q-occupancy Markovization; global optimum over all compressors remains open.'},ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()
