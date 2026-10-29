#!/usr/bin/env python3
"""PREFIX-348: strict rational 1e-14 bracket of unique T6 MEB2=L crossing.

Run prior PREFIX-347 global derivative certificate (and 342/346 exact source checks)
and then at the two new rational endpoints independently certify the exact
five-contact min-ball with outward rational intervals. No float decisions.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
from sympy import Matrix, Rational as Q
import json, runpy

prev = runpy.run_path(str(Path(__file__).with_name('verify_prefix347.py')))
IV,ci = prev['IV'],prev['ci']
zmul,zconj,zscalar,zdotconj = (prev[k] for k in ('zmul','zconj','zscalar','zdotconj'))
rvec,rdot = prev['rvec'],prev['rdot']
sources,ports,q3,L = (prev[k] for k in ('sources','ports','q3','L'))
# Reuse exactly the previously certified source intervals and their BRC ports.
b=[[zmul(zscalar(1/q3,zconj(w)),ak) for ak in a]
   for a,w in zip(sources,ports)]
contact=[(0,'-'),(1,'+'),(3,'-'),(3,'+'),(4,'+')]
h_left=F(166639681327965,10**14)  # 1.66639681327965
h_right=F(166639681327966,10**14) # 1.66639681327966
assert prev['hlo']<h_left<h_right<prev['hhi']
assert h_right-h_left == F(1,10**14)

def midpoint(x):return (x.lo+x.hi)/2
def maxabs(x):return max(abs(x.lo),abs(x.hi))
def rounded(x,n):
    scale=10**n
    return F((x.numerator*scale)//x.denominator,scale)
def sqrti(x,n):
    assert x>0
    s=10**n;k=isqrt((x.numerator*s*s)//x.denominator)
    lo,hi=F(k,s),F(k+1,s)
    assert lo*lo<=x<hi*hi
    return IV(lo,hi)
def outward(x,n):
    s=10**n
    return [str(F((x.lo.numerator*s)//x.lo.denominator,s)),
            str(F(-((-x.hi.numerator*s)//x.hi.denominator),s))]

def evaluate(h):
    y=h-1;rad=q3-y*y
    s=sqrti(rad,42)
    z={'+':ci(s,y),'-':ci(-s,y)}
    P={(j,sgn):[zmul(z[sgn],ak) for ak in b[j]]
       for j in range(6) for sgn in ('-','+')}
    R=[rvec(P[k]) for k in contact]
    D=[[q-p for p,q in zip(R[0],R[k])] for k in range(1,5)]
    G=[[rdot(D[i],D[j]) for j in range(4)] for i in range(4)]
    rhs=[G[i][i]/2 for i in range(4)]
    # Rational approximate inverse: error accounted for via Neumann residual.
    GM=Matrix([[Q(rounded(midpoint(G[i][j]),31).numerator,
                  rounded(midpoint(G[i][j]),31).denominator)
                for j in range(4)] for i in range(4)])
    assert GM.det()!=0
    Binv=GM.inv()
    B=[[F(int(Binv[i,j].p),int(Binv[i,j].q)) for j in range(4)]
       for i in range(4)]
    beta0=[rounded(sum((B[i][j]*midpoint(rhs[j]) for j in range(4)),F(0)),31)
           for i in range(4)]
    E=[[IV(int(i==j))-sum((B[i][k]*G[k][j] for k in range(4)),IV(0))
        for j in range(4)] for i in range(4)]
    e=max(sum((maxabs(E[i][j]) for j in range(4)),F(0)) for i in range(4))
    res=[sum((B[i][k]*(rhs[k]-sum((G[k][j]*beta0[j] for j in range(4)),IV(0)))
              for k in range(4)),IV(0)) for i in range(4)]
    assert e<F(1,10**20),('inverse residual too wide',e)
    delta=max(maxabs(x) for x in res)/(1-e)
    assert delta<F(1,10**19),('beta enclosure too wide',delta)
    beta=[IV(v-delta,v+delta) for v in beta0]
    alpha=[IV(1)-sum(beta,IV(0))]+beta
    assert all(a.lo>F(1,10000) for a in alpha),('weight nonpositive',h,alpha)
    C=[R[0][i]+sum((beta[j]*D[j][i] for j in range(4)),IV(0)) for i in range(6)]
    Fh=rdot([R[0][k]-C[k] for k in range(6)],[R[0][k]-C[k] for k in range(6)])
    slack=[]
    for key,p in P.items():
        if key in contact:continue
        pp=rvec(p)
        d=rdot([u-v for u,v in zip(pp,C)],[u-v for u,v in zip(pp,C)])
        g=Fh-d
        slack.append(g.lo)
        assert g.lo>F(3,1000),('noncontact outside',h,key,g)
    cen=[(C[2*i],C[2*i+1]) for i in range(3)]
    convexity=[]
    for a,w in zip(sources,ports):
        t=zscalar(1/q3,zmul(zdotconj(cen,a),zconj(w)))
        assert t[1].hi<-F(97,100),('arc convexity fails',h,t[1])
        convexity.append(t[1].hi)
    return {
      'h':str(h),'radius_sq_lower':str(Fh.lo),'radius_sq_upper':str(Fh.hi),
      'radius_sq_outward_22dp':outward(Fh,22),
      'radius_minus_L_interval_22dp':outward(Fh-IV(L),22),
      'sign': 'ABOVE_L' if Fh.lo>L else 'BELOW_L' if Fh.hi<L else 'UNKNOWN',
      'inverse_neumann_error':str(e),
      'beta_error_upper':str(delta),
      'min_alpha_lower':str(min(v.lo for v in alpha)),
      'min_noncontact_slack_lower':str(min(slack)),
      'max_arc_Im_t_upper':str(max(convexity))}

left=evaluate(h_left);right=evaluate(h_right)
assert left['sign']=='ABOVE_L' and right['sign']=='BELOW_L', (left,right)
report={
 'schema':'PREFIX348_EXACT_RATIONAL_T6_ROOT_BRACKET_V1',
 'status':'PASS_AUTHOR_SIDE_EXACT_RATIONAL_T6_ROOT_ISOLATION',
 'source_coverage':'6 Newton-Banach roots, five labelled BRC port constraints, 45 ordered BRC path pairs, exact previously proven full-I derivative bound',
 'model':'static auxiliary retained-phase C3 S7-3; six explicitly constructed phase arcs T6',
 'global_knowledge_main':'43f732595432c4e32d7656c3cb32add46e127ba8',
 'enterprise_math_main_scientific_input':'9085a8bd7842858d679d29c9305c6993cdcb2fd0',
 'L':str(L),'left':left,'right':right,
 'width':str(h_right-h_left),
 'strict_monotonicity':'PREFIX347 verifies -19811/10000 < Fprime(h) < -19808/10000 for entire [1.66639681,1.66639682]',
 'conclusion':'There exists exactly one hc in (left,right) with MEB²(T6(hc))=L. Strict full-arc endpoint certificates hold at both bounds.',
 'limitation':'No certified all-source exhaustion S=T6; no unconditional S(h_right)<L; no native X6 physical transfer or independent Driver review.'}
Path(__file__).with_name('RESULTS_PREFIX348.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(report['status'])
for r in (left,right):
    print('h',r['h'],'F-L outward (22dp)',r['radius_minus_L_interval_22dp'],r['sign'])
print('root bracket width =',report['width'],'strictly unique via PREFIX347')
