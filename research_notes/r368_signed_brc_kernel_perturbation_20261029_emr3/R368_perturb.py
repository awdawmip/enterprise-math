#!/usr/bin/env python3
"""R368: exact signed-BRC numerator deformation A_theta=A+theta*x*t.

Usage from project checkout:
  python research_notes/r368_signed_brc_kernel_perturbation_20261029_emr3/R368_perturb.py \
    [path/to/R365_Q345_352_FULL_COEFFICIENTS.txt]

Computes all linear/quadratic response coefficients in the Newton basis for
r=345..352. The signed 12-term K is untouched, its signed J contributions are
retained. Everything decisive uses unbounded Python ints and Fraction.
"""
from __future__ import annotations
import sys, json, hashlib, time
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
RESEARCH=HERE.parent
sys.path.insert(0,str(RESEARCH/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,K,J,add,mul,forward_differences as fd,eval_newton

START,END=345,352
DATA_HASH='50bf1a56fabe89d4752ed71634cbb95d6c7c320d61b09aba1c501857650555a7'

def direct(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def bound_for_finite_rows(rows,aa,bb):
    # M is maximum for |theta|<=1 of the elementary bound (|a|+|b|)/c.
    M=Fraction(0); arg=None; num=0
    for (r,j),c in rows.items():
        assert c>0
        t=Fraction(abs(aa[(r,j)])+abs(bb[(r,j)]),c)
        if t>M: M,arg=t,(r,j)
        num+=1
    assert num==5584 and M>0
    # Sharp all-coefficient radius R367 is defined by minimum baseline Turan ratio.
    # For relative error <= M/p, strict PF2 follows from
    # ((p+M)/(p-M))**2 < T; ULC j=1 is robust when the smallest ULC
    # ratio is > T. No floating-point signs are used.
    T=min(Fraction(rows[(r,j)]**2,rows[(r,j-1)]*rows[(r,j+1)])
          for r in range(START,END+1) for j in range(1,2*r))
    U=min(Fraction(4*r*rows[(r,0)]*rows[(r,2)],(2*r-1)*rows[(r,1)]**2)
          for r in range(START,END+1))
    assert T==Fraction(rows[(352,340)]**2,rows[(352,339)]*rows[(352,341)])
    assert U==Fraction(4*345*rows[(345,0)]*rows[(345,2)],(2*345-1)*rows[(345,1)]**2)
    assert 1<T<U
    p=1
    while p<=M or (p-M)**2*T <= (p+M)**2:
        p+=1
    assert p>1 and ((p-1)<=M or (p-1-M)**2*T <= (p-1+M)**2)
    return M,arg,p,T,U

def main(input_path: Path | None):
    t0=time.monotonic()
    baseline={}
    if input_path is not None:
        raw=input_path.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==DATA_HASH
        for line in raw.splitlines():
            r,j,c=map(int,line.split(b','))
            assert START<=r<=END and 0<=j<=2*r and (r,j) not in baseline
            baseline[(r,j)]=c
        assert len(baseline)==5584
    # With no input file, rebuild the entire historical R365 baseline from
    # the signed K/J kernel and verify its original 7,668,800-byte SHA256.
    maxs=3*(END+1)+2;lim=2*(END+1)+2
    kernels=[None]+[K(i) for i in range(1,13)]
    B0=[[1,1]]
    B1=[[0]]
    for s in range(1,maxs+1):
        z0=J(s)
        z1=[0,1] if s==1 else [0]
        for i in range(1,min(s,12)+1):
            z0=add(z0,mul(kernels[i],B0[s-i],lim),lim)
            z1=add(z1,mul(kernels[i],B1[s-i],lim),lim)
        B0.append(z0);B1.append(z1)
    print('B0/B1',maxs,'sec',round(time.monotonic()-t0,2),flush=True)
    L0={};L1={}
    for r in range(START-1,END+2):
        d0=fd([Fraction(direct(B0,r+u,u),5**u) for u in range(r+2)])
        d1=fd([Fraction(direct(B1,r+u,u),5**u) for u in range(r+2)])
        assert d0[-1]==0 and d1[-1]==0
        l0=[x*5**r for x in d0[:-1]]
        l1=[x*5**r for x in d1[:-1]]
        assert all(x.denominator==1 for x in l0+l1)
        L0[r]=eval_newton([int(x) for x in l0],2*END+3)
        L1[r]=eval_newton([int(x) for x in l1],2*END+3)
    print('L0/L1',len(L0),'sec',round(time.monotonic()-t0,2),flush=True)
    aa,bb={},{}
    sha0,sha_a,sha_b=hashlib.sha256(),hashlib.sha256(),hashlib.sha256()
    use_input=bool(baseline)
    for r in range(START,END+1):
        q0=[];q1=[];q2=[]
        for v in range(2*r+1):
            a,b=L0[r][v+1],L0[r][v+2]
            c,d=L0[r-1][v+2],L0[r+1][v+1]
            e,f=L1[r][v+1],L1[r][v+2]
            g,h=L1[r-1][v+2],L1[r+1][v+1]
            q0.append(a*b-c*d)
            q1.append(e*b+a*f-g*d-c*h)
            q2.append(e*f-g*h)
        c0,c1,c2=fd(q0),fd(q1),fd(q2)
        assert len(c0)==2*r+1
        for j,x in enumerate(c0):
            sha0.update(f'{r},{j},{x}\n'.encode())
            if use_input:
                assert x==baseline[(r,j)], ('baseline mismatch',r,j)
            else:
                baseline[(r,j)]=x
        for j,(x,y) in enumerate(zip(c1,c2)):
            aa[(r,j)]=x;bb[(r,j)]=y
            sha_a.update(f'{r},{j},{x}\n'.encode())
            sha_b.update(f'{r},{j},{y}\n'.encode())
        print('row',r,'all base checks',len(c0),'sec',round(time.monotonic()-t0,2),flush=True)
    assert len(baseline)==5584 and sha0.hexdigest()==DATA_HASH, "R365 baseline sha mismatch"
    M,arg,p,T,U=bound_for_finite_rows(baseline,aa,bb)
    print("BOUND",p,"sec",round(time.monotonic()-t0,2),flush=True)
    theta=Fraction(1,p)
    # Demonstrate deformation is not trivial global rescaling of Q_r:
    # unequal relative derivatives at j=0 and j=1 for r=345.
    witness=(345,0,1)
    d00=Fraction(aa[(345,0)],baseline[(345,0)])
    d01=Fraction(aa[(345,1)],baseline[(345,1)])
    assert d00!=d01, ('shape-deformation witness failed',d00,d01)
    # Strong exact bound on each coefficient, strictly within R367's sharp radius.
    assert (p-M)**2*T>(p+M)**2 and 0<M<p
    assert all(abs(theta*aa[k]+theta*theta*bb[k])<=theta*M*baseline[k] for k in baseline)
    print("RELATIVE",round(time.monotonic()-t0,2),flush=True)
    # PF2 and strict ULC j=1 failure directly at theta = +/- 1/p,
    # exercising the actual polynomial response, not only a norm bound.
    trial={}
    for sign in [-1,1]:
        th=sign*theta
        checks=0
        for r in range(START,END+1):
            cv=[baseline[(r,j)]+th*aa[(r,j)]+th*th*bb[(r,j)] for j in range(2*r+1)]
            assert all(x>0 for x in cv)
            assert all(cv[j]*cv[j]>cv[j-1]*cv[j+1] for j in range(1,2*r))
            assert (2*r-1)*cv[1]**2 < 4*r*cv[0]*cv[2]
            checks+=2*r-1
        trial[str(sign)]={'strict_turan_pass':checks,'ULC_j1_fail_rows':8}
    print("ENDPOINTS",round(time.monotonic()-t0,2),flush=True)
    # Raw D minors, independently assembled from signed B0+theta*B1 arrays,
    # agree with the extracted polynomial Q at both endpoints.
    raw_checks=0
    for sign in (-1,1):
        th=sign*theta
        for r in (345,352):
            for k in (1,2,4,8):
                q=r+k
                DT=lambda Q,kk:direct(B0,Q,kk)+th*direct(B1,Q,kk)
                minor=DT(q,k)*DT(q+1,k+1)-DT(q,k+1)*DT(q+1,k)
                v=k-1
                def ell(rr,offset):return L0[rr][v+offset]+th*L1[rr][v+offset]
                Qv=ell(r,1)*ell(r,2)-ell(r-1,2)*ell(r+1,1)
                assert minor==Qv*Fraction(5**(2*k+1),5**(2*r)) and minor>0,(r,k,sign)
                raw_checks+=1
    assert raw_checks==16
    print("RAW",round(time.monotonic()-t0,2),flush=True)
    def ratio(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
    out={'schema':'EM_R368_SIGNED_BRC_NUMERATOR_PERTURBATION_V1','source_full_coeff_sha256':DATA_HASH,
         'input_model':'A_theta=A+theta*t*x; K_theta=K unchanged (all signed twelve K branches)',
         'r_range':[START,END],'base_count':len(baseline),'baseline_regenerated_without_data_file':not use_input, 'response_order':2,'B_max':maxs,
         'response_linear_sha256':sha_a.hexdigest(),'response_quadratic_sha256':sha_b.hexdigest(),
         'max_amplitude_bound_M':ratio(M),'max_M_location':{'r':arg[0],'j':arg[1]},
         'safe_theta_abs_leq':f'1/{p}','safe_theta_denominator':str(p),
         'safe_coefficient_relative_error':'strictly < epsilon_star from R367, exact squared rational comparison',
         'R367_T':ratio(T),'R367_U':ratio(U),
         'integer_reciprocal_threshold_is_optimal_for_M_majorant':True,
         'raw_D_minor_endpoint_checks':raw_checks,
         'not_global_rescaling_witness':{'r':345,'j_first':0,'j_second':1,'linear_relative_response_0':ratio(d00),'linear_relative_response_1':ratio(d01)},
         'exact_endpoint_trials':trial,
         'guarantee':f'For every real |theta|<=1/{p}, all r=345..352 Q_theta Newton coefficient sequences are positive and strictly PF2 but not PF-infinity',
         'generic_extraction_dependency':'R363 polynomial extraction theorem applies as signed K unchanged and [t] A_theta degree bound; author-side, independent review pending',
         'native_X6':'no native embedding or observable-preserving transfer demonstrated',
         'admission':'AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED'}
    ev=HERE/'R368_EVIDENCE.json';ev.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('SUMMARY',json.dumps({k:v for k,v in out.items() if k not in {'max_amplitude_bound_M','not_global_rescaling_witness'}},ensure_ascii=False),flush=True)
    return out

if __name__=='__main__':
    p=Path(sys.argv[1]) if len(sys.argv)>1 else None
    main(p)
