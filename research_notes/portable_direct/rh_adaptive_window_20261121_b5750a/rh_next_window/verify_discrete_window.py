#!/usr/bin/env python3
"""Crosscheck exact recurrences and proved discrete/continuous window bounds.

Non-interval 70-digit numerical evidence. General theorems are proved in NOTES.md.
All integer/composite road terms from n=2 to the window horizon are retained.
"""
from pathlib import Path
from math import comb
import json
import mpmath as mp
mp.mp.dps=70


def J(r,k,y):
    logy=mp.log(y)
    if r==0:return logy**(k+1)/(k+1)
    if k==0:return y**r/r
    if k==1:return y**r*(logy/r-1/r**2)
    return y**r*(logy**2/r-2*logy/r**2+2/r**3)


def primitive(d,b,theta,y):
    p=2-2*theta;q=1-2*theta;r=-2*theta
    return d*d*J(p,0,y)-2*d*J(p,1,y)+J(p,2,y)-2*b*d*J(q,0,y)+2*b*J(q,1,y)+b*b*J(r,0,y)


def positive_energy(d,b,theta,l,r):
    if b>0:
        if b>=mp.exp(d-1):return mp.mpf(0)
        z=-b*mp.exp(-d)
        lo=-b/mp.lambertw(z,-1);hi=-b/mp.lambertw(z,0)
    elif b==0:
        lo=mp.mpf(0);hi=mp.exp(d)
    else:
        lo=mp.mpf(0);hi=-b/mp.lambertw(-b*mp.exp(-d),0)
    lo=max(l,mp.re(lo));hi=min(r,mp.re(hi))
    return primitive(d,b,theta,hi)-primitive(d,b,theta,lo) if lo<hi else mp.mpf(0)


def case(Y_string,m,mode,h_string=None):
    Y=mp.mpf(Y_string);theta=mp.mpf('0.75');lam=mp.mpf('1.5');Z=Y*mp.sqrt(Y)
    A=int(mp.ceil(Y));B=int(mp.floor(Z));p=2*theta+1
    if mode=='MATCHED':
        h=((mp.mpf(m)+1)/2)**(mp.mpf(1)/m)*Y**(-lam*(1-theta)/m)/(lam*mp.log(Y))**(1+mp.mpf(2)/m)
    else:h=mp.mpf(h_string)
    weights=[(-1)**(j+1)*comb(m,j)for j in range(1,m+1)]
    K=sum(abs(w)for w in weights)
    factors=[[]for _ in range(B+1)]
    for prime in range(2,B+1):
        if not factors[prime]:
            for n in range(prime,B+1,prime):factors[n].append(prime)
    prime_terms={prime:[-mp.expm1(-j*h*mp.log(prime))for j in range(1,m+1)]for prime in range(2,B+1)if factors[prime]==[prime]}
    D=[mp.mpf(0)for _ in range(B+1)];ports={1:(mp.mpf(0),mp.mpf(0))};q={1:1+mp.euler}
    ca=mp.mpf(0);cb=mp.mpf(0);max_error=mp.mpf(0)
    for n in range(2,B+1):
        terms=[mp.fprod([prime_terms[prime][j-1]for prime in factors[n]])/(j*h)for j in range(1,m+1)]
        D[n]=mp.fsum(weights[j]*terms[j]for j in range(m))
        ca+=D[n]/n;cb+=D[n];ports[n]=(ca,cb)
        q[n]=n*(ca+1+mp.euler-mp.log(n))-cb
        vonmangoldt=mp.log(factors[n][0]) if len(factors[n])==1 else mp.mpf(0)
        max_error=max(max_error,abs(D[n]-vonmangoldt))
    tol=mp.mpf('1e-56');max_recurrence_error=mp.mpf(0)
    recurrence={1:1+mp.euler,2:2*(1+mp.euler-mp.log(2))}
    kappa_checks=[]
    for n in range(2,B):
        nn=mp.mpf(n)
        kappa=nn*((nn+1)*mp.log(nn+1)-2*nn*mp.log(nn)+(nn-1)*mp.log(nn-1))
        assert 1+1/(6*nn**2)<=kappa+tol<=1+1/(6*(nn**2-1))+tol
        recurrence[n+1]=2*recurrence[n]-recurrence[n-1]+(D[n]-kappa)/nn
        max_recurrence_error=max(max_recurrence_error,abs(recurrence[n+1]-q[n+1]))
    assert max_recurrence_error<tol
    eta_bound=h**m*mp.log(Z)**(m+1)/(m+1)
    if mode=='MATCHED':
        assert eta_bound<mp.mpf('.5') and max_error<=eta_bound+tol
        P=mp.mpf(1);M=None
        delta=lambda n:1/mp.mpf(n)
    else:
        assert K<=3
        P=mp.mpf(K+1)/2;M=mp.mpf(K-1)/2
        delta=lambda n:(1+M*mp.log(n))/n
        for n in range(2,B+1):
            assert -M*mp.log(n)-tol<=D[n]<=P*mp.log(n)+tol
    for n in range(A+1,B):
        assert max(q[n-1],q[n+1])>=q[n]-delta(n)-tol
    E=mp.mpf(0);Ecore=mp.mpf(0)
    for n in range(int(mp.floor(Y)),B+1):
        l=max(Y,mp.mpf(n));r=min(Z,mp.mpf(n+1))
        if l>=r:continue
        ca,cb=ports[n]
        e=positive_energy(ca+1+mp.euler,cb,theta,l,r)
        E+=e
        if n>=A and n<B:Ecore+=e
    S=mp.fsum(max(q[n],0)**2/mp.mpf(n)**p for n in range(A,B+1))
    Sint=mp.fsum(max(q[n],0)**2/mp.mpf(n)**p for n in range(A+1,B))
    trace=max(q[A],0)**2/mp.mpf(A)**p+max(q[B],0)**2/mp.mpf(B)**p
    U=(1+(1+1/mp.mpf(A))**p)/2
    C=mp.sqrt(2)*(1+1/mp.mpf(A+1))**(p/2)
    R=mp.sqrt(mp.fsum(delta(mp.mpf(n))**2/mp.mpf(n)**p for n in range(A+1,B)))
    eps=(1+1/mp.mpf(A))/(8*mp.sqrt(2*theta+2))*mp.mpf(A)**(-theta-1)
    frag=(A-Y)*Y**(1-2*theta)*(P*mp.log(A)**2+2)**2+(Z-B)*mp.mpf(B)**(1-2*theta)*(P*mp.log(Z)**2+2)**2
    trace_bound=mp.mpf(A)**(1-2*theta)*(P*mp.log(A)**2+2)**2+mp.mpf(B)**(1-2*theta)*(P*mp.log(B)**2+2)**2
    assert mp.sqrt(Sint)<=C*mp.sqrt(Ecore)+R+tol
    assert mp.sqrt(Ecore)<=mp.sqrt(U)*mp.sqrt(S)+eps+tol
    assert mp.sqrt(S)<=C*mp.sqrt(E)+R+mp.sqrt(trace)+tol
    assert E-Ecore<=frag+tol and trace<=trace_bound+tol
    upper=(mp.sqrt(U)*mp.sqrt(S)+eps)**2+frag
    lower=(max(mp.sqrt(Sint)-R,0)/C)**2
    assert lower<=E+tol<=upper+tol
    rr=2*theta+2
    if mode=='MATCHED':R_bound=mp.mpf(A)**(-theta-1)/mp.sqrt(rr)
    else:
        term=1+M*mp.log(A)
        R_bound=mp.sqrt(mp.mpf(A)**(-2*theta-2)/rr*(term**2+2*M*term/rr+2*M*M/(rr*rr)))
    assert R<=R_bound+tol
    return {
      'mode':mode,'Y':str(Y),'Z':str(Z),'theta':str(theta),'lambda':str(lam),'m':m,'h':str(h),'weights':weights,'weight_l1':K,'integer_core':[A,B],
      'max_pointwise_D_minus_Lambda':str(max_error),'pointwise_error_bound':str(eta_bound),'max_recurrence_error':str(max_recurrence_error),'negative_D_nodes_in_core':sum(D[n]<0 for n in range(A,B+1)),
      'positive_integer_nodes':sum(q[n]>0 for n in range(A,B+1)),
      'continuous_positive_energy':str(E),'integer_core_positive_energy':str(Ecore),'integer_positive_square_sum':str(S),'interior_positive_square_sum':str(Sint),'integer_to_continuous_ratio':str(S/E) if E>0 else None,
      'actual_endpoint_trace':str(trace),'endpoint_trace_upper':str(trace_bound),'actual_fragment_energy':str(E-Ecore),'fragment_energy_upper':str(frag),
      'C_lower_norm':str(C),'U_upper_energy':str(U),'discrete_shape_remainder_norm':str(R),'shape_remainder_global_bound':str(R_bound),'curvature_remainder_norm':str(eps),
      'energy_lower_from_discrete':str(lower),'energy_upper_from_discrete_and_fragments':str(upper),'checks_passed':True
    }


def main():
    cases=[case('16',2,'MATCHED'),case('17.25',3,'MATCHED'),case('9',2,'BOUNDED_L1_3','1')]
    result={'status':'PASS_DISCRETE_WINDOW_CROSSCHECKS','precision_digits':mp.mp.dps,'interval_arithmetic':False,'theorem_source':'NOTES.md','scientific_scope':'Finite whole-road windows; no inference of arbitrarily remote window existence.','cases':cases}
    Path(__file__).with_name('discrete_window_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'cases':[{k:c[k]for k in ['mode','Y','Z','m','h','weight_l1','continuous_positive_energy','integer_positive_square_sum','integer_to_continuous_ratio','max_recurrence_error','checks_passed']}for c in cases]},ensure_ascii=False))

if __name__=='__main__':main()
