#!/usr/bin/env python3
"""R749SSD. Exact joint numerator/denominator error-partition recovery certificate.
Frozen auxiliary source pin a72226e2430ffa4786321ac86e7f0c599d5f0389.
Python standard library only. The infinite tail uses the explicitly cited
R749SSC/R749SSA independently certified all-numerator bound (see paper).
"""
from fractions import Fraction as Q
from itertools import product
import json

WEIGHTS=(1,1,2,3,6)
OFFSETS=(0,1,5)
PHASE=(455,-295,-25,185,-25,-295)
PARTITIONS={
    'all-common': (0,0,0),
    '01|2': (0,0,1),
    '02|1': (0,1,0),
    '12|0': (1,0,0),
    'independent': (0,1,2),
}
ORDER=list(PARTITIONS)
# Proven sharp N for independent numerator errors and each denominator partition,
# rows K=0,1,2; columns M=0,1,2 (R749SSC, immutable PR #2549).
PREDECESSOR_UPPER={
    'all-common': ((35,53,65),(41,55,67),(41,59,71)),
    '01|2': ((35,53,65),(261,267,273),(497,503,503)),
    '02|1': ((35,53,65),(261,267,273),(507,513,513)),
    '12|0': ((35,53,65),(249,255,261),(409,415,415)),
    'independent': ((35,53,65),(261,267,273),(507,513,513)),
}

def counts(maxq):
    # Exact nonnegative integer coin-vector DP for exact total source weight.
    c=[0]*maxq; t=[0]*maxq; c[0]=1
    for j,w in enumerate(WEIGHTS):
        for n in range(w,maxq):
            oldc=c[n-w]
            c[n]+=oldc
            t[n]+=t[n-w]+(oldc if j==0 else 0)
    C=[0]*(maxq+1); T=[0]*(maxq+1)
    for n in range(maxq):
        C[n+1]=C[n]+c[n]
        T[n+1]=T[n]+t[n]
    return C,T

C,T=counts(522)
SIGNATURES=tuple(tuple(Q(PHASE[(a+h)%6],36) for h in OFFSETS)
                 for a in range(6))

def smooth_scaled(q):
    return Q(18*q**4+54*q**3-345*q*q+2070*q-16315,108)

def observation(q,e,d):
    assert C[q]+d>0
    return Q(q**3*(T[q]+e),C[q]+d)-smooth_scaled(q)

def group_vectors(partition,budget):
    groups=sorted(set(partition))
    for choices in product(range(-budget,budget+1),repeat=len(groups)):
        yield tuple(choices[groups.index(partition[i])] for i in range(3))

def first_failure(r,M,K,num_partition,den_partition):
    a=r%6
    qs=tuple(r+h for h in OFFSETS)
    es=tuple(group_vectors(num_partition,M))
    for ds in group_vectors(den_partition,K):
        if any(C[qs[i]]+ds[i]<=0 for i in range(3)):
            continue
        possible=tuple(tuple(observation(q,e,ds[i]) for e in range(-M,M+1))
                       for i,q in enumerate(qs))
        for ev in es:
            obs=tuple(possible[i][ev[i]+M] for i in range(3))
            da=max(abs(obs[i]-SIGNATURES[a][i]) for i in range(3))
            for b in range(6):
                if b==a: continue
                db=max(abs(obs[i]-SIGNATURES[b][i]) for i in range(3))
                if db<=da:
                    return {'r':r,'phase':a,'rival':b,
                            'numerator_errors':list(ev),'denominator_errors':list(ds),
                            'true_distance':str(da),'rival_distance':str(db)}
    return None

def refines(finer,coarser):
    return all(finer[i]!=finer[j] or coarser[i]==coarser[j]
               for i in range(3) for j in range(3))

def independent_population(q):
    # Independent direct nested enumeration for small q (not the coin DP).
    total=marked=0
    for a in range(q):
      for b in range(q):
       for c in range((q-1-a-b)//2+1):
        for d in range((q-1-a-b-2*c)//3+1):
         for e in range((q-1-a-b-2*c-3*d)//6+1):
          total+=1;marked+=a
    return total,marked

def main():
    for q in range(1,13):
        assert independent_population(q)==(C[q],T[q]),q
    table={}; witnesses={}; tested=0
    for K in range(3):
      for M in range(3):
        key=f'M{M}K{K}'
        matrix=[]; wrows=[]
        for dname,dp in PARTITIONS.items():
          row=[]; wr=[]
          for ename,ep in PARTITIONS.items():
            upper=PREDECESSOR_UPPER[dname][K][M]
            failure=None
            # Every integer between predecessor upper and last failure is
            # exhaustively checked. Beyond upper, the cited exact infinite
            # predecessor theorem certifies correctness by set containment.
            for r in range(upper-1,0,-1):
                tested+=1
                failure=first_failure(r,M,K,ep,dp)
                if failure is not None: break
            cutoff=failure['r']+1 if failure else 1
            assert cutoff<=upper
            row.append(cutoff);wr.append(failure)
          matrix.append(row);wrows.append(wr)
        table[key]=matrix
        if M==K==2:witnesses=wrows
    # Exact recovery of all 45 predecessor-denominator thresholds.
    for K in range(3):
      for M in range(3):
        mat=table[f'M{M}K{K}']
        for di,dname in enumerate(ORDER):
          assert mat[di][-1]==PREDECESSOR_UPPER[dname][K][M]
        for i,pi in enumerate(ORDER):
          for j,pj in enumerate(ORDER):
            if refines(PARTITIONS[pj],PARTITIONS[pi]):
              # Refinement enlarges admissible errors in either coordinate.
              assert all(mat[i][k]<=mat[j][k] for k in range(5))
              assert all(mat[k][i]<=mat[k][j] for k in range(5))
    for K in range(3):
      for M in range(3):
        if K<2:
          assert all(table[f'M{M}K{K}'][i][j]<=table[f'M{M}K{K+1}'][i][j]
                     for i in range(5) for j in range(5))
        if M<2:
          assert all(table[f'M{M}K{K}'][i][j]<=table[f'M{M+1}K{K}'][i][j]
                     for i in range(5) for j in range(5))
    # Cross-check exhaustive search on fixed small cases; separate integer
    # numerator/denominator assignments are filtered by partition relations.
    crosschecks=0
    for r in (1,2,7,12):
      for K,M in ((0,0),(1,1),(2,2)):
        for di,dname in enumerate(ORDER):
          for ei,ename in enumerate(ORDER):
            found=first_failure(r,M,K,PARTITIONS[ename],PARTITIONS[dname])
            # Repeat by independent coordinate cubes, filtering joint equality.
            brute=False;a=r%6;qs=tuple(r+h for h in OFFSETS)
            for ds in product(range(-K,K+1),repeat=3):
              if any(C[qs[i]]+ds[i]<=0 for i in range(3)):continue
              if any(ds[i]!=ds[j] for i in range(3) for j in range(i+1,3)
                     if PARTITIONS[dname][i]==PARTITIONS[dname][j]):continue
              for ev in product(range(-M,M+1),repeat=3):
                if any(ev[i]!=ev[j] for i in range(3) for j in range(i+1,3)
                       if PARTITIONS[ename][i]==PARTITIONS[ename][j]):continue
                obs=tuple(observation(qs[i],ev[i],ds[i]) for i in range(3))
                da=max(abs(obs[i]-SIGNATURES[a][i]) for i in range(3))
                if any(max(abs(obs[i]-SIGNATURES[b][i]) for i in range(3))<=da
                       for b in range(6) if b!=a):
                    brute=True;break
              if brute:break
            assert (found is not None)==brute,(r,M,K,dname,ename)
            crosschecks+=1
    result={'unit':'R749SSD','status':'PASS','review':'AUTHOR_EXACT_NOT_REVIEWED',
            'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'model_weights':WEIGHTS,'marked_source':0,'offsets':OFFSETS,
            'partitions_order_denominator_rows_numerator_columns':ORDER,
            'sharp_global_thresholds_M0_to_2_K0_to_2':table,
            'M2K2_last_failure_witnesses':witnesses,
            'finite_cutoff_tests_from_predecessor_uppers':tested,
            'independent_small_q_population_checks':12,
            'independent_cube_crosschecks':crosschecks,
            'tail_dependency':'R749SSC exact denominator-partition independent-numerator sharp thresholds; ultimately R749SSA infinite-tail certificate',
            'scope':'finite exact search plus predecessor infinite-tail theorem, not independent review or native BRC/X6 acceptance'}
    return result

if __name__=='__main__':
    result=main()
    with open('R749SSD_JOINT_PARTITION_EXACT_RESULTS.json','w',encoding='utf8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    print('PASS',result['finite_cutoff_tests_from_predecessor_uppers'],result['independent_cube_crosschecks'])
