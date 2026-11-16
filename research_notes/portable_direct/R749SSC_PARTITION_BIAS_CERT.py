#!/usr/bin/env python3
"""Exact partition-preserving denominator-error six-phase recovery.
Requires R749SSB_SHARED_DENOMINATOR_CERT.py in same directory; standard library only.
"""
import json
from fractions import Fraction as Q
from itertools import product
from R749SSB_SHARED_DENOMINATOR_CERT import C, T, H_scaled, J, S, y, ceil, floor

PARTITIONS = {
    'all-common': (0,0,0),
    '01|2': (0,0,1),
    '02|1': (0,1,0),
    '12|0': (1,0,0),
    'independent': (0,1,2),
}
N_INDEP = ((35,261,507),(53,267,513),(65,273,513))

def group_choices(r,K,partition):
    groups = sorted(set(partition))
    options = []
    for g in groups:
        qs = [r+J[i] for i in range(3) if partition[i]==g]
        lower = max(-K, max(1-C[q] for q in qs))
        options.append(range(lower,K+1))
    for vals in product(*options):
        ds = [vals[groups.index(partition[i])] for i in range(3)]
        yield ds

def failure(r,M,K,partition):
    a=r%6
    qs=tuple(r+h for h in J)
    bound = max(abs(y(q,e,d)-S[a][i])
                for i,q in enumerate(qs)
                for d in range(max(-K,1-C[q]),K+1)
                for e in set((-M,M)))
    if bound<Q(15,4):return None, True
    for ds in group_choices(r,K,partition):
        for b in range(6):
            if b==a:continue
            for j,q in enumerate(qs):
                d=ds[j]
                for ej in set((-M,M)):
                    obs=y(q,ej,d)
                    u=abs(obs-S[a][j])
                    if abs(obs-S[b][j])>u:continue
                    es=[None]*3
                    es[j]=ej
                    for i,qi in enumerate(qs):
                        if i==j:continue
                        lowv=max(S[a][i]-u,S[b][i]-u)
                        highv=min(S[a][i]+u,S[b][i]+u)
                        lo=max(-M,ceil((lowv+H_scaled[qi])*Q(C[qi]+ds[i],qi**3)-T[qi]))
                        hi=min(M,floor((highv+H_scaled[qi])*Q(C[qi]+ds[i],qi**3)-T[qi]))
                        if lo>hi:break
                        es[i]=lo
                    if all(e is not None for e in es):
                        vals=[y(q,es[i],ds[i]) for i,q in enumerate(qs)]
                        td=max(abs(vals[i]-S[a][i]) for i in range(3))
                        rd=max(abs(vals[i]-S[b][i]) for i in range(3))
                        assert rd<=td
                        return {'r':r,'phase':a,'rival':b,'denominator_errors':ds,
                                'numerator_errors':es,'true_distance':str(td),
                                'rival_distance':str(rd)},False
    return None, False

def naive(r,M,K,p):
    a=r%6
    for ds in group_choices(r,K,p):
        vs=[[y(r+h,e,ds[i]) for e in range(-M,M+1)] for i,h in enumerate(J)]
        for obs in product(*vs):
            da=max(abs(obs[i]-S[a][i]) for i in range(3))
            if any(max(abs(obs[i]-S[b][i]) for i in range(3))<=da for b in range(6) if b!=a):
                return True
    return False

def main():
    result={}
    for label,p in PARTITIONS.items():
        entries=[]
        for K in range(3):
            for M in range(3):
                upper=N_INDEP[M][K]
                last=None;pruned=0
                for r in range(1,upper):
                    f,skip=failure(r,M,K,p)
                    if skip:pruned+=1
                    if f is not None:last=f
                N=(last['r']+1) if last else 1
                assert N<=upper
                entries.append({'M':M,'K':K,'N':N,'independent_upper':upper,
                                'last_failure':last,'finite_cutoffs_checked':upper-1,
                                'pruned':pruned})
                print(label,M,K,N,flush=True)
        result[label]=entries
    for idx in range(9):
        common=result['all-common'][idx]['N']
        independent=result['independent'][idx]['N']
        assert common==[35,53,65,41,55,67,41,59,71][idx]
        assert independent==[35,53,65,261,267,273,507,513,513][idx]
        for name in ('01|2','02|1','12|0'):
            n=result[name][idx]['N']
            assert common<=n<=independent
    direct=0
    for label,p in PARTITIONS.items():
        for M in range(3):
            for K in range(3):
                for r in range(1,17):
                    assert naive(r,M,K,p)==(failure(r,M,K,p)[0] is not None),(label,r,M,K)
                    direct+=1
    out={'unit':'R749SSC','status':'PASS',
         'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
         'bias_group_partition_maps':PARTITIONS,
         'model':'W=(1,1,2,3,6), J=(0,1,5); one integer denominator bias per partition block; individual integer numerator errors',
         'sharp_thresholds':'For every r>=N; counterexample at N-1; infinity-norm nearest ideal signature, ties fail',
         'tail':'R749SSA independent-denominator exact global thresholds for M,K=0..2 upper-bound every partition',
         'bruteforce_crosschecks':direct,
         'cases':result}
    with open('R749SSC_PARTITION_BIAS_RESULTS.json','w') as f:json.dump(out,f,indent=2)
    print('PASS', direct)
if __name__=='__main__':main()
