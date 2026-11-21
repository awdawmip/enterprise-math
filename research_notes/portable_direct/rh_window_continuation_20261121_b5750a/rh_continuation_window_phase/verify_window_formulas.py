#!/usr/bin/env python3
"""High-precision numerical crosschecks of the new finite-window formulas.

The general statements are proved in NOTES.md. This script uses non-interval
mpmath, separately from verify_positive_window.py's exact rational certificate.
"""
from pathlib import Path
import json
import mpmath as mp
mp.mp.dps=70


def J(p,k,y):
    z=mp.log(y)
    if p==0:return z**(k+1)/(k+1)
    if k==0:return y**p/p
    if k==1:return y**p*(z/p-1/p**2)
    if k==2:return y**p*(z*z/p-2*z/p**2+2/p**3)
    raise ValueError(k)


def primitive(d,b,t,y):
    p=2-2*t;q=1-2*t;r=-2*t
    return d*d*J(p,0,y)-2*d*J(p,1,y)+J(p,2,y)-2*b*d*J(q,0,y)+2*b*J(q,1,y)+b*b*J(r,0,y)


def full_energy(d,b,t,l,r):return primitive(d,b,t,r)-primitive(d,b,t,l)


def positive_interval(d,b,l,r):
    if b<0:
        hi=-b/mp.lambertw(-b*mp.exp(-d),0)
        lo=mp.mpf(0)
    elif b==0:
        lo=mp.mpf(0);hi=mp.exp(d)
    else:
        if b>=mp.exp(d-1):return None
        arg=-b*mp.exp(-d)
        lo=-b/mp.lambertw(arg,-1);hi=-b/mp.lambertw(arg,0)
    lo=max(l,mp.re(lo));hi=min(r,mp.re(hi))
    return (lo,hi) if lo<hi else None


def positive_energy(d,b,t,l,r):
    z=positive_interval(d,b,l,r)
    return full_energy(d,b,t,*z) if z else mp.mpf(0)


def linear_energy(p,q,t,l,r,positive=True):
    if positive:
        fl=p*l+q;fr=p*r+q
        if fl<=0 and fr<=0:return mp.mpf(0)
        if p>0 and fl<0:l=-q/p
        if p<0 and fr<0:r=-q/p
    def P(y):return p*p*J(2-2*t,0,y)+2*p*q*J(1-2*t,0,y)+q*q*J(-2*t,0,y)
    return P(r)-P(l)


def road_coefficients(h,m,Z):
    factors=[[]for _ in range(Z+1)]
    for p in range(2,Z+1):
        if not factors[p]:
            for n in range(p,Z+1,p):factors[n].append(p)
    A=[mp.mpf(0)for _ in range(m)];B=A.copy();rows={}
    rows[1]=[(1+mp.euler,mp.mpf(0))for _ in range(m)]
    for n in range(2,Z+1):
        for j in range(m):
            a=(j+1)*h
            road=mp.fprod([-mp.expm1(-a*mp.log(p))for p in factors[n]])/a
            A[j]+=road/n;B[j]+=road
        rows[n]=[(1+mp.euler+A[j],B[j])for j in range(m)]
    return rows


def window_case(Y,Z,h,weights,t):
    rows=road_coefficients(h,len(weights),Z)
    full=mp.mpf(0);pos=mp.mpf(0);chord=mp.mpf(0);quadrature=mp.mpf(0)
    delta_bound_sq=mp.mpf(0);anchor_pos=mp.mpf(0);defect_pos=mp.mpf(0)
    gram=[[mp.mpf(0)for _ in weights]for _ in weights]
    for n in range(Y,Z):
        l=mp.mpf(n);r=l+1
        ds=[x[0]for x in rows[n]];bs=[x[1]for x in rows[n]]
        d=sum(w*x for w,x in zip(weights,ds));b=sum(w*x for w,x in zip(weights,bs))
        f=lambda y:y*(d-mp.log(y))-b
        full+=full_energy(d,b,t,l,r);pos+=positive_energy(d,b,t,l,r)
        active=positive_interval(d,b,l,r)
        if active:quadrature+=mp.quad(lambda y:f(y)**2*y**(-2*t-1),list(active))
        gl=f(l);gr=f(r);p=(gr-gl)/(r-l);q=gl-p*l
        chord+=linear_energy(p,q,t,l,r)
        delta=1/(8*l)
        mass=(l**(-2*t)-r**(-2*t))/(2*t)
        delta_bound_sq+=delta*delta*mass
        anchor_pos+=positive_energy(ds[0],bs[0],t,l,r)
        defect_pos+=linear_energy(d-ds[0],-(b-bs[0]),t,l,r)
        for i in range(len(weights)):
            for j in range(len(weights)):
                # Exact bilinear product, including the common -y log y center.
                di,dj,bi,bj=ds[i],ds[j],bs[i],bs[j]
                def P(y):
                    return di*dj*J(2-2*t,0,y)-(di+dj)*J(2-2*t,1,y)+J(2-2*t,2,y)-(di*bj+dj*bi)*J(1-2*t,0,y)+(bi+bj)*J(1-2*t,1,y)+bi*bj*J(-2*t,0,y)
                gram[i][j]+=P(r)-P(l)
    from_gram=sum(weights[i]*weights[j]*gram[i][j]for i in range(len(weights))for j in range(len(weights)))
    upper=(mp.sqrt(chord)+mp.sqrt(delta_bound_sq))**2
    defect_upper=(mp.sqrt(anchor_pos)+mp.sqrt(defect_pos))**2
    tol=mp.mpf('1e-50')
    assert abs(from_gram-full)<tol*max(1,abs(full))
    assert abs(quadrature-pos)<tol*max(1,abs(pos))
    assert chord<=pos+tol and pos<=upper+tol
    assert pos<=defect_upper+tol
    return {'Y':Y,'Z':Z,'h':str(h),'weights':weights,'theta':str(t),'full_energy':str(full),'positive_energy_exact_formula':str(pos),'positive_energy_quadrature':str(quadrature),'chord_positive_lower':str(chord),'curvature_norm_bound':str(mp.sqrt(delta_bound_sq)),'chord_curvature_upper':str(upper),'anchor_positive_energy':str(anchor_pos),'exact_linear_defect_positive_energy':str(defect_pos),'anchor_plus_defect_upper':str(defect_upper),'full_gram':[[str(x)for x in row]for row in gram],'full_energy_from_gram':str(from_gram),'checks_passed':True}


def main():
    # Mixed signs / zero b / two active roots / theta=1/2 primitive branch.
    synthetic=[]
    for d,b,t,l,r in [(mp.mpf('1.5'),mp.mpf('1.2'),mp.mpf('.75'),mp.mpf('.2'),mp.mpf('8')),(mp.mpf('0'),mp.mpf('-1'),mp.mpf('.5'),mp.mpf('.2'),mp.mpf('8')),(mp.mpf('1'),mp.mpf('0'),mp.mpf('.75'),mp.mpf('.2'),mp.mpf('8'))]:
        active=positive_interval(d,b,l,r);e=positive_energy(d,b,t,l,r)
        numerical=mp.quad(lambda y:(y*(d-mp.log(y))-b)**2*y**(-2*t-1),list(active)) if active else mp.mpf(0)
        assert abs(e-numerical)<mp.mpf('1e-55')
        synthetic.append({'d':str(d),'b':str(b),'theta':str(t),'active_interval':list(map(str,active)) if active else None,'energy':str(e),'quadrature_error':str(abs(e-numerical))})
    cases=[window_case(25,125,mp.mpf('.1'),[2,-1],mp.mpf('.75')),window_case(16,64,mp.mpf('.05'),[3,-3,1],mp.mpf('.75'))]
    output={'status':'PASS_NUMERICAL_FORMULA_CROSSCHECKS','precision_digits':mp.mp.dps,'interval_arithmetic':False,'general_claims_source':'NOTES.md proofs','synthetic_branch_cases':synthetic,'actual_road_windows':cases}
    Path(__file__).with_name('window_formula_results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'actual_road_windows':[{k:c[k]for k in ['Y','Z','h','weights','positive_energy_exact_formula','chord_positive_lower','chord_curvature_upper','anchor_positive_energy','exact_linear_defect_positive_energy']}for c in cases]},ensure_ascii=False))

if __name__=='__main__':main()
