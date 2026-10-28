#!/usr/bin/env python3
"""R370: certified low-corank phase diagram for the signed BRC K3 branch.

Run from the R345/PR1592 Enterprise Math checkout:
 python research_notes/r370_signed_k3_low_corank_phase_20261029_emr3/R370_exact_phase.py

This deliberately reuses original signed R346 and R369 kernel code, rather than
substituting a new kernel. All equality, sign and root-count checks are exact
integer/rational/symbolic operations (SymPy Sturm real-root counting).
"""
from __future__ import annotations
from pathlib import Path
import sys, json, hashlib
from math import comb
from sympy import (Symbol, Poly, Rational, oo, factor, expand, discriminant,
                   sqrt, sign, N)

HERE=Path(__file__).resolve().parent
RESEARCH=HERE.parent
sys.path.insert(0,str(RESEARCH/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
from R369_check import compute_rows,fd  # derives all rows from original signed R346 K/J
x=Symbol('theta')


def rt_count(f,lo,hi):
    return int(Poly(f,x).count_roots(lo,hi))


def str_sign(f,q):
    v=expand(f).subs(x,q)
    assert v!=0,(f,q)
    return 1 if v>0 else -1


def isolate(f,lo,hi,all_real=None):
    assert lo<hi
    assert rt_count(f,lo,hi)==1,(factor(f),lo,hi)
    assert str_sign(f,lo)*str_sign(f,hi)==-1,(factor(f),lo,hi)
    if all_real is not None:
        assert rt_count(f,-oo,oo)==all_real,(factor(f),all_real)
    return {'lower':str(lo),'upper':str(hi),'roots_in_bracket':1,
            'endpoint_signs':[str_sign(f,lo),str_sign(f,hi)]}


def main():
    raw_newton={}
    rows,D=compute_rows(x,2)
    for r in (1,2):
        vals=[]
        for v in range(2*r+1):
            k=v+1;q=r+k
            m=expand(D(q,k)*D(q+1,k+1)-D(q,k+1)*D(q+1,k))
            vals.append(expand(Rational(5)**(2*r-2*k-1)*m))
        direct=list(map(expand,fd(vals)))
        assert len(direct)==2*r+1
        assert all(expand(direct[j]-rows[r][j])==0 for j in range(2*r+1))
        raw_newton[r]=direct

    a,b,c=raw_newton[1]
    d=raw_newton[2]
    e1=[512*x*x-2400*x+2620,768*x*x-2880*x+2520,(30-16*x)**2]
    e2=[-80*(3072*x**3-21056*x*x+56360*x-59885),
        16*(12288*x**4-145920*x**3+592960*x*x-1038800*x+677475),
        16*(32768*x**4-299520*x**3+998080*x*x-1457000*x+796425),
        16*(8*x-15)**3*(56*x-135),32*(8*x-15)**4]
    assert all(expand(v-e1[j])==0 for j,v in enumerate(raw_newton[1]))
    assert all(expand(v-e2[j])==0 for j,v in enumerate(raw_newton[2]))

    T1=expand(b*b-a*c)
    U1=expand(b*b-4*a*c)
    T2=[None]+[expand(d[j]**2-d[j-1]*d[j+1]) for j in range(1,4)]
    # Newton's ultra-log-concavity, for n=4, with CORRECT normalization:
    # j*(n-j)*a_j^2 - (j+1)*(n-j+1)*a_{j-1}*a_{j+1}.
    U2_first=expand(3*d[1]**2-8*d[0]*d[2])

    z=Rational(1,1000)
    cuts={
      'r1_PF2_first_failure_tau1':isolate(T1,1054*z,1055*z,2),
      'r2_PF2_first_failure_tau2':isolate(T2[1],1301*z,1302*z,2),
      'r2_c0_zero_eta':isolate(d[0],2773*z,2774*z,1),
      'r2_c1_first_zero':isolate(d[1],2039*z,2040*z,2),
      'r2_c1_second_zero':isolate(d[1],5748*z,5750*z,2),
      'r2_c2_first_zero':isolate(d[2],2202*z,2204*z,2),
      'r1_ordinary_T_second_zero':isolate(T1,1506*z,1508*z,2)
    }
    delta=Rational(15,8)
    alpha2=(75+sqrt(385))/32
    beta1=(15-sqrt(15))/8
    assert Rational(1390,1000)<beta1<Rational(1391,1000)
    assert Rational(2956,1000)<alpha2<Rational(2957,1000)
    assert Rational(1055,1000)<beta1
    assert Rational(1302,1000)<delta
    assert Rational(2774,1000)<alpha2
    assert Rational(2039,1000)>delta
    assert Rational(2202,1000)>delta
    assert Rational(2410,1000)<Rational(135,56)<Rational(2411,1000)
    assert Rational(2774,1000)<Rational(5748,1000)

    # Sturm-certified counts and exact sign evaluations prove the whole intervals.
    root_counts={
      'r1_T_in_(-1,beta1)_one':rt_count(T1,-1,Rational(1391,1000)),
      'r1_U_in_(-1,beta1)_zero':rt_count(U1,-1,Rational(1391,1000)),
      'r1_U_in_(alpha2,infinity)_zero':rt_count(U1,Rational(2956,1000),oo),
      'r2_T1_in_(-1,delta)_one':rt_count(T2[1],-1,delta),
      'r2_T2_in_(-1,tau2upper)_zero':rt_count(T2[2],-1,Rational(1302,1000)),
      'r2_T3_in_(-1,tau2upper)_zero':rt_count(T2[3],-1,Rational(1302,1000)),
      'r2_U1_in_(-1,tau2upper)_zero':rt_count(U2_first,-1,Rational(1302,1000)),
      'r2_c1_total_real_two':rt_count(d[1],-oo,oo),
      'r2_c2_total_real_two':rt_count(d[2],-oo,oo),
      'r2_c0_total_real_one':rt_count(d[0],-oo,oo),
    }
    assert root_counts=={
      'r1_T_in_(-1,beta1)_one':1,
      'r1_U_in_(-1,beta1)_zero':0,
      'r1_U_in_(alpha2,infinity)_zero':0,
      'r2_T1_in_(-1,delta)_one':1,
      'r2_T2_in_(-1,tau2upper)_zero':0,
      'r2_T3_in_(-1,tau2upper)_zero':0,
      'r2_U1_in_(-1,tau2upper)_zero':0,
      'r2_c1_total_real_two':2,
      'r2_c2_total_real_two':2,
      'r2_c0_total_real_one':1}
    assert str_sign(T1,0)>0 and str_sign(T1,Rational(5,4))<0
    assert str_sign(U1,0)<0 and str_sign(U1,3)>0
    assert str_sign(T2[1],0)>0 and str_sign(T2[1],Rational(3,2))<0
    assert str_sign(T2[2],0)>0 and str_sign(T2[3],0)>0
    assert str_sign(U2_first,0)<0
    assert str_sign(d[0],0)>0 and str_sign(d[0],3)<0
    assert str_sign(d[1],0)>0 and str_sign(d[1],Rational(5,2))<0
    assert str_sign(d[2],0)>0 and str_sign(d[2],Rational(5,2))<0
    assert str_sign(d[0],alpha2)<0

    # Direct D(q,k) r=2 k=1, no polynomial-extraction extension required.
    m31=expand(D(3,1)*D(4,2)-D(3,2)*D(4,1))
    assert expand(5*m31-d[0])==0
    assert m31.subs(x,3)==-42160
    # Under this sign preserving theta=3 the r1 short polynomial is PF-infinity.
    assert [expand(v.subs(x,3)) for v in raw_newton[1]]==[28,792,324]
    assert U1.subs(x,3)==590976
    # The same parameter violates positive raw r2 TP2.
    assert d[0].subs(x,3)==-210800

    # Optional decimal approximations for readability only; do NOT prove signs.
    approximations={
      'tau1':str(Poly(T1,x).intervals(eps=Rational(1,10**12))[0][0]),
      'tau2':str(Poly(T2[1],x).intervals(eps=Rational(1,10**12))[0][0]),
      'eta':str(Poly(d[0],x).intervals(eps=Rational(1,10**12))[0][0]),
      'beta1':str(N(beta1,16)),
      'alpha2':str(N(alpha2,16))}

    record={
      'schema':'EM_R370_SIGNED_K3_LOW_CORANK_EXACT_PHASE_V1',
      'date':'2026-10-29',
      'input_commit':'762855f46bf7f699448e0d8471d60f83fdc2747b',
      'basis':'R369_original_signed_R346_KJ; K3[t2]=-8*(1+theta); theta>-1',
      'direct_D_verification':{'r1_minors':3,'r2_minors':5,'equal_to_L_interpolation':True},
      'r1_coefficients_factored':[str(factor(v)) for v in raw_newton[1]],
      'r2_coefficients_factored':[str(factor(v)) for v in raw_newton[2]],
      'r1_turan_factored':str(factor(T1)),
      'r1_ulc_factored':str(factor(U1)),
      'r2_turan_factored':[str(factor(v)) for v in T2[1:]],
      'r2_first_ulc_factored':str(factor(U2_first)),
      'root_intervals_certified':cuts,
      'root_counts_sturm':root_counts,
      'r1_phase':'r1 PF2 iff -1 < theta <= tau1 OR theta >= alpha2; PF-infinity iff theta >= alpha2; all nonnegative iff -1<theta<=beta1 OR theta>=alpha2',
      'r2_phase':'r2 PF2 iff -1 < theta <= tau2; PF-infinity never; all nonnegative iff -1<theta<=15/8',
      'simultaneous_PF2':'r1 and r2 PF2 iff -1<theta<=tau1',
      'simultaneous_PFinfty':'empty for theta>-1',
      'raw_D_minor_3_1':'one_fifth_of_r2_c0; equals -42160 at theta=3; strictly negative for theta>=alpha2',
      'r1_PFinfty_theta_3':[28,792,324],
      'numeric_display_only':approximations,
      'arithmetic':'exact integer/rational/symbolic polynomials; Sturm real root count; no floating sign inference',
      'scope':'finite r=1,2 coefficient polynomials; raw D minors exact; entire Q_r mapping conditional on independently unreviewed R363',
      'classification':'AUTHOR_SIDE_EXACT / FINITE_ROOT_ISOLATION / UNREVIEWED / NOT_ADMITTED',
      'native_X6_transfer':'not established'
    }
    out=HERE/'R370_EVIDENCE.json'
    out.write_text(json.dumps(record,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print('R370_EXACT_PASS')
    print(json.dumps({
      'isolations':cuts,'root_counts':root_counts,'m31_theta3':str(m31.subs(x,3)),
      'evidence_sha256':hashlib.sha256(out.read_bytes()).hexdigest()
    },indent=2,ensure_ascii=False))
    return record

if __name__=='__main__':main()
