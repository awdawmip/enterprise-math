#!/usr/bin/env python3
"""R281 exact identities and finite BRC source-histogram checks.

SymPy is used only for algebraic identity checks. Integer DP uses unbounded
Python ints and retains q, previous-source-bit, affine sign, and translation.
Finite checks corroborate, but do not prove, eventual mode selection.
"""
from collections import defaultdict
import json
from math import exp, log, pi, sqrt
import sympy as S

x, s = S.symbols('x s', real=True)
rho = (S.sqrt(5)-1)/2
sigma2_expected = (15+7*S.sqrt(5))/10
D = 1+2*x**4-x**6-2*x*S.cosh(s)
Dx=S.diff(D,x)
N={+1:1+x**2+x**4-x*S.exp(-s)-x*(1+x**2)*S.exp(s),
   -1:x**4*S.exp(-2*s)-x**5*S.exp(-s)}
mu={+1:-2-S.sqrt(5),-1:-(5+S.sqrt(5))/2}

def simple(y):
    return S.simplify(S.radsimp(y))

def ev(expr):
    return simple(expr.subs({x:rho,s:0}))

assert simple(rho**2+rho-1)==0
r2 = simple(2*rho/ev(Dx))
sigma2 = simple(-r2/rho)
assert simple(sigma2-sigma2_expected)==0
alpha=r2/2
beta=simple(-(ev(S.diff(D,x,2))*alpha**2/2
        +ev(S.diff(D,x,s,2))*alpha/2
        +ev(S.diff(D,s,4))/24)/ev(Dx))
kappa4=simple(-24*(beta/rho-alpha**2/(2*rho**2)))
assert simple(kappa4 + (3825+1711*S.sqrt(5))/50)==0

# r'(0)=0 and r''(0)=r2. Differentiate log pole residue.
a2={}
for e,ne in N.items():
    n0=ev(ne);ns=ev(S.diff(ne,s));nx=ev(S.diff(ne,x));nss=ev(S.diff(ne,s,2))
    A0=simple(-n0/(rho*(1+rho**2)*ev(Dx)))
    this_mu=simple(ns/n0)
    a2[e]=simple((nss+nx*r2)/n0-this_mu**2
        -r2/rho-(2*rho/(1+rho**2))*r2
        -(ev(S.diff(Dx,s,2))+ev(S.diff(Dx,x))*r2)/ev(Dx))
    assert A0==S.Rational(1,10) and simple(this_mu-mu[e])==0
assert simple(a2[+1]-a2[-1])==0
assert simple(a2[+1]+(119+53*S.sqrt(5))/10)==0
K=simple(kappa4/(8*sigma2**2)-a2[+1]/(2*sigma2))
assert simple(K-(1+3*S.sqrt(5)/8))==0

def choose_nearest(e,parity):
    return min(range(-30,31),key=lambda k: (k%2!=parity,abs(float(mu[e])-k)))

pred={0:(+1,-4),1:(-1,-3)}
even_gap=simple(((-4-mu[-1])**2)-((-4-mu[+1])**2))
odd_gap=simple(((-5-mu[+1])**2)-((-3-mu[-1])**2))
assert simple(even_gap-(5*S.sqrt(5)-11)/2)==0
assert simple(odd_gap-(25-11*S.sqrt(5))/2)==0
assert float(even_gap)>0 and float(odd_gap)>0
assert [choose_nearest(+1,0),choose_nearest(-1,0),
        choose_nearest(+1,1),choose_nearest(-1,1)]==[-4,-4,-5,-3]

T={0:{0:(2,-1,-1),1:(2,+1,-1)},
   1:{0:(0,-1,-1),1:(0,+1,-1)},
   2:{0:(1,+1,+1),1:(2,+1,-1)}}

def add(d,key,value):
    d[key]=d.get(key,0)+value

def direct_counts(Nmax):
    state={(0,False,+1,0):1}
    ret=[]
    for n in range(Nmax+1):
        bins={+1:{},-1:{}}
        for (q,last_zero,e,k),value in state.items():
            if q==0:add(bins[e],k,value)
        ret.append(bins)
        if n==Nmax:break
        nxt={}
        for (q,last_zero,e,k),value in state.items():
            for bit,(qn,eta,b) in T[q].items():
                if last_zero and bit==0:continue
                add(nxt,(qn,bit==0,eta*e,eta*k+b),value)
        state=nxt
    return ret

# Exact rational Laurent recurrence from H=(1+x^2)*[1+2x^4-x^6-x(z+z^-1)]
def generating_function_counts(Nmax):
    numer={+1:{(0,0):1,(2,0):1,(4,0):1,(1,-1):-1,(1,1):-1,(3,1):-1},
           -1:{(4,-2):1,(5,-1):-1}}
    out=[]
    for n in range(Nmax+1):
        bins={+1:{},-1:{}}
        for e in [+1,-1]:
            z={}
            for lag,coef,offsets in [
                 (1,1,[-1,1]),(2,-1,[0]),(3,1,[-1,1]),
                 (4,-2,[0]),(6,-1,[0]),(8,1,[0])]:
                if n<lag:continue
                for k,value in out[n-lag][e].items():
                    for delta in offsets:add(z,k+delta,coef*value)
            for (j,k),v in numer[e].items():
                if n==j:add(z,k,v)
            bins[e]={k:v for k,v in z.items() if v!=0}
        out.append(bins)
    return out

max_n=400
hist=direct_counts(max_n)
gf=generating_function_counts(150)
matched=0
for n in range(151):
    for e in (+1,-1):
        assert hist[n][e]==gf[n][e],(n,e,'GF discrepancy')
        matched+=len(hist[n][e])

exceptions=[]
examples=[]
for n,bins in enumerate(hist):
    for e in (+1,-1):
        assert all(k%2==n%2 and value>0 for k,value in bins[e].items())
    if n<9:continue
    mx=max(v for e in (+1,-1) for v in bins[e].values())
    modes=sorted((e,k) for e in (+1,-1) for k,v in bins[e].items() if v==mx)
    if modes!=[pred[n%2]]:exceptions.append({'n':n,'modes':modes})
    if n in (78,79,80,81,82,83,100,101,150,151,200,201,300,400):
        lead=n*log((1+sqrt(5))/2)-log(5)-.5*log(2*pi*float(sigma2)*n)
        k=pred[n%2][1]; e=pred[n%2][0]
        c=float(K)-((k-float(mu[e]))**2)/(2*float(sigma2))
        # Evaluate log ratio safely even for hundreds of digits.
        ratio=exp(log(mx)-lead)
        v1=1+c/n
        examples.append({'n':n,'mode':modes,'predicted_mode':pred[n%2],
                 'count':str(mx),'peak_ratio':round(ratio,12),
                 'edgeworth_ratio_at_predicted_mode':round(v1,12),
                 'scaled_difference_n2':round(n*n*(ratio-v1),8)})
assert exceptions and max(v['n'] for v in exceptions)==80
assert all(not(n>=81) or all((e,k)==pred[n%2] for e in (+1,-1)
   for k,v in hist[n][e].items() if v==max(x for e2 in (+1,-1)
   for x in hist[n][e2].values())) for n in (81,82,100,101,200,201,300,400))

res={'status':'PASS','scope':'AUTHOR_SIDE_FINITE_CHECK_NOT_ADMISSION',
     'sources':['R279 signed rational GF','R280 signed local limit'],
     'symbolic':{'sigma_squared':str(sigma2),'kappa_four':str(kappa4),
       'amplitude_log_second_plus':str(a2[+1]),
       'amplitude_log_second_minus':str(a2[-1]),
       'common_edgeworth_constant':str(K),
       'even_signed_distance_gap':str(even_gap),
       'odd_signed_distance_gap':str(odd_gap)},
     'finite':{'source_max_n':max_n,'rational_gf_max_n':150,
       'exact_matching_nonzero_coefficients':matched,
       'observed_stability_range':'81..400 (not a proof of threshold)',
       'max_nonconforming_n':80,
       'nonconforming_count_9_to_400':len(exceptions),
       'latest_nonconforming':exceptions[-5:],
       'examples':examples},
     'proof_boundary':'Eventually unique signed peak requires R280 fixed-window localization and a uniform bounded-k Edgeworth expansion; finite DP cannot prove the all-n claim.'}
print(json.dumps(res,indent=2,ensure_ascii=False))
