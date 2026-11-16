#!/usr/bin/env python3
"""R749SRZ independent exact numerator/denominator perturbation certificate.
Only Python standard-library integers and Fraction. Analytic asymptotic theorem
proved in paired paper; this program verifies finite cases and tail hypotheses.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
import json

W=(1,1,2,3,6)
J=(0,1,5)
P=tuple(Q(v,36) for v in (455,-295,-25,185,-25,-295))
S=tuple(tuple(P[(a+h)%6] for h in J) for a in range(6))
H=(Q(1,6),Q(1,2),-Q(115,36),Q(115,6),-Q(16315,108))

def counts(n):
    c=[0]*n; t=[0]*n; c[0]=1
    for i,w in enumerate(W):
        for j in range(w,n):
            t[j]+=t[j-w]+(c[j-w] if i==0 else 0)
            c[j]+=c[j-w]
    C=[0]; T=[0]
    for j in range(n):
        C.append(C[-1]+c[j]); T.append(T[-1]+t[j])
    return C,T

def smooth4(r):
    return sum(v*r**(4-i) for i,v in enumerate(H))

def observe(r,C,T,e=0,d=0):
    assert C[r]+d>0
    return Q(r**3*(T[r]+e),C[r]+d)-smooth4(r)

def denom_failure(r,k,C,T):
    """Exact: extremal denominator on one max-norm coordinate suffices."""
    a=r%6
    vv=[]
    for h in J:
        v=r+h; lo=max(-k,1-C[v]); ds=list(range(lo,k+1))
        vv.append((ds,[observe(v,C,T,d=d) for d in ds]))
    for b in range(6):
        if a==b: continue
        for j in range(3):
            for d,y in ((vv[j][0][0],vv[j][1][0]),(vv[j][0][-1],vv[j][1][-1])):
                rad=abs(y-S[a][j])
                if abs(y-S[b][j])>rad: continue
                witness=[None]*3; witness[j]=d
                for i in range(3):
                    if i==j: continue
                    found=next((di for di,yi in zip(*vv[i])
                                if abs(yi-S[a][i])<=rad and abs(yi-S[b][i])<=rad),None)
                    if found is None: break
                    witness[i]=found
                else: return {'r':r,'rival':b,'denominator_errors':witness}
    return None

def brute_denom_failure(r,k,C,T):
    a=r%6; choices=[range(max(-k,1-C[r+h]),k+1) for h in J]
    for ds in product(*choices):
        y=tuple(observe(r+h,C,T,d=ds[i]) for i,h in enumerate(J))
        da=max(abs(y[i]-S[a][i]) for i in range(3))
        if any(b!=a and max(abs(y[i]-S[b][i]) for i in range(3))<=da for b in range(6)):
            return True
    return False

def mixed_witness(r,k,m,C,T):
    assert r%6==0
    e=(-m,m,m); d=(k,-k,-k)
    y=[observe(r+h,C,T,e[i],d[i]) for i,h in enumerate(J)]
    actual=max(abs(y[i]-S[0][i]) for i in range(3))
    rival=max(abs(y[i]-S[3][i]) for i in range(3))
    return {'r':r,'M':m,'K':k,'numerator_errors':list(e),'denominator_errors':list(d),
            'true_distance':str(actual),'rival_distance':str(rival),
            'rival_ties_or_wins':rival<=actual}

def main():
    end=1350
    C,T=counts(end+J[-1]+2)
    finite={}; checks=0
    for k in range(5):
        last=None
        for r in range(1,end):
            z=denom_failure(r,k,C,T)
            if z is not None: last=z
        assert last is not None
        finite[str(k)]={'global_N':last['r']+1,'last_failure':last}
    assert [finite[str(k)]['global_N'] for k in range(5)]==[35,261,507,759,1005]
    for k in (0,1,2):
        for r in range(1,49):
            assert bool(denom_failure(r,k,C,T))==brute_denom_failure(r,k,C,T),(r,k)
            checks+=1
    # Previous certified 0<R-P<1600/r (r>=516), and T/C<r/6+1 then
    # give a uniform strict upper bound on signature displacement.
    r=end; k=4
    tail=Q(1600,r)+(Q(4320*k,1)*(Q(r,6)+1)/r**2)/(1-Q(4320*k,r**5))
    assert tail<Q(15,4)
    # Supportive exact witnesses for the two-parameter critical surface.
    examples=[]
    for k,m in ((5,0),(10,0),(10,100),(20,400),(50,2500)):
        # Exact floor approximation to rho=96k+sqrt(9216k^2+1152m).
        root=isqrt(9216*k*k+1152*m)
        rr=6*((96*k+root)//6)
        if rr+J[-1]>=len(C): C,T=counts(rr+J[-1]+8)
        ex=mixed_witness(rr,k,m,C,T)
        assert ex['rival_ties_or_wins'],(k,m,rr)
        examples.append(ex)
    return {
      'status':'PASS','unit':'R749SRZ',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'W=(1,1,2,3,6); J=(0,1,5); both count channels may have independent signed bounded integer errors',
      'new_analytic_theorem':'N(M,K) = 96K+sqrt(9216K^2+1152M)+O(1) as M+K -> infinity, with absolute implied constant',
      'denominator_only_exact_N_for_K_0_to_4':finite,
      'finite_r_examined_per_K':end-1,
      'independent_cube_brute_comparisons':checks,
      'prior_proven_tail_residual_bound':'0<R(r)-P[r mod 6]<1600/r for r>=516',
      'tail_r_start':end,
      'tail_bound_for_all_r_ge_1350_K_le_4':str(tail),
      'tail_bound_float':float(tail),
      'ideal_signature_half_separation':str(Q(15,4)),
      'selected_joint_failure_witnesses':examples,
      'proof_scope':'Analytic asymptotic proof in paired Markdown; finite exact proof of K=0..4 thresholds via endpoint lemma, scan and certified infinite tail.',
      'next_question':'Derive exact eventual offsets/quasiperiodic changes beyond the leading joint asymptotic and solve integer-error two-channel exact interval feasibility.'}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
