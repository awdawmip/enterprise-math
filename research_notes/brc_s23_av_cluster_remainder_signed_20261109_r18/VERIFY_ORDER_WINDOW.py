#!/usr/bin/env python3
"""Verify the stronger G_r(n)>0 circular order window with exact Fractions."""
from fractions import Fraction as F
from math import gcd
from VERIFY_CLUSTER_MIXED import direct_risk


def risk_order(theta,p,q,m,n):
    assert 0<theta<1 and n>=m>=q>=1 and gcd(p,q)==1
    eps=theta-F(p,q); assert eps
    eta=abs(eps); k=p if eps>0 else q-p
    inv=pow(k,-1,q) if q>1 else 0
    d=q*eta
    corr=F(0); min_gap=F(1)
    for r in range(q):
        e_m=r+q*((m-1-r)//q)
        e_n=r+q*((n-1-r)//q)
        next_r=(r+inv)%q if q>1 else 0
        G=F(1,q)+(next_r-e_n)*eta
        min_gap=min(min_gap,G)
        if e_n>e_m:
            corr+=max(F(0),d-G)
    return (n-m)*d-corr,min_gap


def general_experiment():
    total=0; beyond_old=0; corrected=0
    for q in range(1,9):
      for p in range(q+1):
       if gcd(p,q)!=1:continue
       for sign in (-1,1):
        if (sign==1 and p==q) or (sign==-1 and p==0):continue
        for m in (q,q+1,2*q+2):
         for n in range(m,m+q*3+5):
          for factor in (F(1,2),F(9,10),F(11,10),F(7,5),F(9,5)):
           eta=factor/F(q*n)
           theta=F(p,q)+sign*eta
           if not 0<theta<1:continue
           v,ming=risk_order(theta,p,q,m,n)
           if ming<=0:continue
           assert v==direct_risk(theta,m,n),(q,p,sign,m,n,theta,v)
           total+=1
           beyond_old+=int(n*eta>=F(1,q))
           corrected+=int(v != (n-m)*q*eta)
    assert beyond_old>0 and corrected>0
    return total,beyond_old,corrected


def s23_window():
    xlo=F(262204504569236716045286,10**24)
    xhi=F(262204504569236716045287,10**24)
    end=[]
    for theta in (xlo,xhi):
        for n in range(128,226):
            v,g=risk_order(theta,16,61,128,n)
            assert g>0 and v==direct_risk(theta,128,n)
            if n<=164:assert v==(n-128)*(16-61*theta)
            else:assert v==36*(16-61*theta)+(n-164)*(164*theta-43)
        v,g=risk_order(theta,16,61,128,226)
        assert g<0
        ref=direct_risk(theta,128,226)
        assert v != ref and ref==-2090+7972*theta
        end.append((-2047+7808*theta,ref,g))
    return end


if __name__=='__main__':
    total,beyond,corrected=general_experiment()
    end=s23_window()
    print('PASS_CLUSTER_ORDER_POSITIVE_GAP_WINDOW')
    print('general_direct_exact_cases',total,'beyond_n_eta_bound',beyond,'nonlinear_correction_cases',corrected)
    print('S23_proved_n_range','128..225 inclusive','checked_theta_enclosure_endpoints',2)
    print('S23_n225_R','-2047+7808*theta')
    print('S23_first_order_break_n',226,'first_break_r=42, ell=225, r_plus=0')
    print('S23_n226_R','-2090+7972*theta','naive_cluster_formula_wrong=True')
