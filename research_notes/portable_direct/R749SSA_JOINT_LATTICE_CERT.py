#!/usr/bin/env python3
"""R749SSA exact mixed numerator+denominator integer feasibility and thresholds.
Uses only Fraction and integers; imports the frozen R749SRZ model routines.
"""
import json
from fractions import Fraction as Q
from itertools import product
from R749SRZ_JOINT_COUNT_ERROR_CERT import counts,observe,smooth4,J,S,P


def ceilq(x):return -(-x.numerator//x.denominator)


def mixed_failure(r,M,K,C,T):
    """Complete 2*k extreme-anchor test, O(k^2*K) arithmetic per rival."""
    a=r%6
    q=[r+h for h in J]
    ext=[]
    for v in q:
        c,t=C[v],T[v]; dmin=max(-K,1-c)
        emin=-M; emax=M
        d_at_min= K if t+emin>=0 else dmin
        d_at_max= dmin if t+emax>=0 else K
        ext.append(((emin,d_at_min,observe(v,C,T,emin,d_at_min)),
                    (emax,d_at_max,observe(v,C,T,emax,d_at_max))))
    for b in range(6):
        if b==a:continue
        for j in range(3):
            for ej,dj,yj in ext[j]:
                radius=abs(yj-S[a][j]);
                if abs(yj-S[b][j])>radius:continue
                cand=[None]*3; cand[j]=[ej,dj]
                for i in range(3):
                    if i==j:continue
                    v=q[i]; c,t=C[v],T[v]
                    lo=max(S[a][i]-radius,S[b][i]-radius)
                    hi=min(S[a][i]+radius,S[b][i]+radius)
                    if lo>hi:break
                    sm=smooth4(v)
                    for di in range(max(-K,1-c),K+1):
                        elow=ceilq((lo+sm)*(c+di)/v**3-t)
                        ehigh=((hi+sm)*(c+di)/v**3-t)//1
                        ev=max(-M,elow)
                        if ev<=min(M,ehigh):
                            cand[i]=[ev,di];break
                    else:break
                else:return {'r':r,'phase':a,'rival':b,
                             'numerator_errors':[z[0] for z in cand],
                             'denominator_errors':[z[1] for z in cand]}
    return None


def brute_failure(r,M,K,C,T):
    a=r%6
    choices=[]
    for h in J:
        c=C[r+h]
        choices.append([(e,d) for e in range(-M,M+1) for d in range(max(-K,1-c),K+1)])
    for pairs in product(*choices):
        vals=[observe(r+h,C,T,e,d) for h,(e,d) in zip(J,pairs)]
        t=max(abs(vals[i]-S[a][i]) for i in range(3))
        if any(b!=a and max(abs(vals[i]-S[b][i]) for i in range(3))<=t for b in range(6)):
            return True
    return False


def main():
    end=1350
    C,T=counts(end+max(J)+2)
    grid=[]
    for K in range(3):
        for M in range(3):
            last=None
            for r in range(1,end):
                f=mixed_failure(r,M,K,C,T)
                if f:last=f
            assert last
            grid.append({'M':M,'K':K,'N':last['r']+1,'last_failure':last})
    for row in grid:
        if row['K']==0: assert [35,53,65][row['M']]==row['N']
        if row['M']==0: assert [35,261,507][row['K']]==row['N']
    crosscheck=0
    for r in range(1,25):
        for M,K in product((0,1),(0,1)):
            assert bool(mixed_failure(r,M,K,C,T))==brute_failure(r,M,K,C,T),(r,M,K)
            crosscheck+=1
    # Analytic infinite tail: predecessor residual <=1600/r, C>=r^5/4320,
    # T/C<r/6+1 for r>=1350, and exact difference D=r^3(Ce-Td)/(C(C+d)).
    r=end; M=2;K=2
    tail=Q(1600,r)+ (Q(4320,r*r)*(M+K*(Q(r,6)+1)))/(1-Q(4320*K,r**5))
    assert tail<Q(15,4)
    return {'status':'PASS','unit':'R749SSA',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'exact_criterion':'Two global extreme observed-value anchors for a max-norm coordinate and integer interval test for e at each admissible denominator d',
      'complexity_per_rival':'O(k^2*(2K+1)) exact arithmetic checks independent of M (aside from integer bit length)',
      'global_thresholds_M_0_to_2_K_0_to_2':grid,
      'finite_cutoffs_per_pair':end-1,
      'total_cutoff_budget_pairs':9*(end-1),
      'independent_direct_cube_checks':crosscheck,
      'certified_infinite_tail_start':end,
      'tail_noise_bound_for_M_K_le_2':str(tail),
      'ideal_half_min_separation':'15/4',
      'next_question':'Reduce the O(K) denominator scan to lattice floor-sum or polyhedral integer feasibility; characterize exact additive phase offsets for large simultaneous budgets.'}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
