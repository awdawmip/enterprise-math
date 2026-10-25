#!/usr/bin/env python3
"""R4-EC16: exact audit of left/right grade-edge BRC source asymmetry.
Author-side finite/symbolic checks; not a proof of uniform infinite asymptotics.
"""
import json
from collections import defaultdict
from math import comb, log
import sympy as sp

EDGE={0:{0:(2,-1,-1),1:(2,1,-1)},1:{0:(0,-1,-1),1:(0,1,-1)},2:{0:(1,1,1),1:(2,1,-1)}}
STATES=((0,0,-1),(0,0,1),(1,1,-1),(1,1,1),(2,0,-1),(2,0,1),(2,1,-1),(2,1,1))
INDEX={s:i for i,s in enumerate(STATES)}
TRANS=[]
def step(q,r,e,bit):
    qq,eta,b=EDGE[q][bit]
    rr=0 if bit else (1 if r==0 else 2)
    ee=e*eta
    grade=int(ee*b==-1)
    assert ee*b==e*(1-2*bit)
    return (qq,rr,ee),grade
for i,(q,r,e) in enumerate(STATES):
    for bit in (0,1):
        nxt,g=step(q,r,e,bit)
        if nxt[1]!=2:TRANS.append((i,INDEX[nxt],g,bit))

def matrix_counts(maxn):
    current=[defaultdict(int) for _ in STATES]
    current[INDEX[(0,0,1)]][0]=1
    output=[{0:1}]
    for n in range(1,maxn+1):
        new=[defaultdict(int) for _ in STATES]
        for a,b,g,_ in TRANS:
            for j,v in current[a].items():new[b][j+g]+=v
        current=new
        counts=defaultdict(int)
        for row in current:
            for j,v in row.items():counts[j]+=v
        output.append(dict(counts))
    return output

def poly_counts(maxn,maxj,reflected=False):
    rows=[]
    forcing={(0,0):1,(2,1):-1,(3,2 if reflected else 1):-1,(5,3 if reflected else 2):1}
    for n in range(maxn+1):
        row=[0]*(min(maxj,n)+1)
        for j in range(len(row)):
            v=forcing.get((n,j),0)
            if n>=1:
                v+=rows[n-1][j] if j<len(rows[n-1]) else 0
                if j: v+=rows[n-1][j-1]
            if n>=4 and j>=2 and j-2<len(rows[n-4]): v-=2*rows[n-4][j-2]
            if n>=6 and j>=3 and j-3<len(rows[n-6]): v+=rows[n-6][j-3]
            row[j]=v
        rows.append(row)
    return rows

def raw_counts(n):
    by_grade=defaultdict(int)
    for code in range(1<<n):
        q,r,e=0,0,1
        j=0
        for idx in range(n):
            (q,r,e),g=step(q,r,e,(code>>idx)&1)
            j+=g
            if r==2: break
        else:by_grade[j]+=1
    return by_grade

def symbolic_check():
    x,u,a=sp.symbols('x u a')
    den=1-(1+u)*x+2*u**2*x**4-u**3*x**6
    nleft=(1-u*x*x)*(1-u*x**3)
    nright=(1-u*x*x)*(1-u*u*x**3)
    assert sp.expand(nright-nleft)==sp.expand(u*(1-u)*x**3*(1-u*x*x))
    assert sp.expand(den.subs({x:u*x,u:1/u},simultaneous=True)-den)==0
    la=1+u-2*u**2+7*u**3-29*u**4+135*u**5
    assert sp.series(la**6-(1+u)*la**5+2*u*u*la**2-u**3,u,0,6).removeO()==0
    rho=sp.series(1/la,u,0,5).removeO()
    L=sp.series(sp.log((1-u**2*rho**3)/(1-u*rho**3)),u,0,5)
    ua=a+5*a*a+22*a**3+86*a**4
    La=sp.series(L.removeO().subs(u,ua),a,0,4)
    assert sp.simplify(La.removeO()-(a+sp.Rational(3,2)*a*a-sp.Rational(2,3)*a**3))==0,La
    # The first 3 fixed-edge defects are eventually constant/polynomial.
    coef=[]
    rseries=sp.series(u*(1-u)*x**3*(1-u*x*x)/den,u,0,4).removeO()
    for k in (1,2,3):
        coef.append(sp.factor(sp.expand(rseries).coeff(u,k)))
    return {'defect_u1':str(coef[0]),'defect_u2':str(coef[1]),'defect_u3':str(coef[2]),'log_right_left_u':str(L),'log_right_left_alpha':str(La)}

def main():
    assert len(TRANS)==12
    full=matrix_counts(180)
    left=poly_counts(2000,160)
    right=poly_counts(2000,160,True)
    for n in range(181):
        for k in range(min(n,160)+1):
            assert left[n][k]==full[n].get(k,0),(n,k,'left')
            assert right[n][k]==full[n].get(n-k,0),(n,k,'right')
    for n in range(13):
        truth=raw_counts(n)
        assert all(full[n].get(k,0)==truth.get(k,0) for k in range(n+1))
    for n in range(3,2001):
        assert right[n][1]-left[n][1]==1
    for n in range(5,2001):
        assert right[n][2]-left[n][2]==n-5
    for n in range(6,2001):
        assert right[n][3]-left[n][3]==(n-9)*(n-6)//2
    assert right[7][3]-left[7][3]==-1
    certificate=symbolic_check()
    samples=[]
    for n,k in [(500,40),(1000,70),(1500,100),(2000,150)]:
        l=left[n][k];h=right[n][k];alpha=k/n
        difference=log(h)-log(l)
        samples.append({'n':n,'k':k,'alpha':alpha,'low':str(l),'high':str(h),
                        'log_high_low':difference,'alpha_prediction':alpha,
                        'second_order_prediction':alpha+1.5*alpha*alpha-2*alpha**3/3})
    report={
        'schema':'ENTERPRISE_MATH_R4_EC16_AUTHOR_EXACT_V1',
        'scope':'positive ordered binary affine auxiliary BRC, clean-source grade observer; no native X6 execution',
        'proved_identity':'C(ux,1/u)-C(x,u)=u(1-u)x^3(1-u*x^2)/Delta(x,u)',
        'symbolic':certificate,'raw_words_through_n':12,'raw_word_count':sum(1<<i for i in range(13)),
        'direct_8state_DP_n':180,'exact_left_right_recurrence_n':2000,'max_grade':160,
        'exact_fixed_edge_differences':'D_n1=1(n>=3); D_n2=n-5(n>=5); D_n3=(n-9)(n-6)/2(n>=6)',
        'strict_positive_high_edge_n7_k3':False,
        'asymptotic_scope':'proved in associated manuscript using shared uniform moving saddle with two numerator amplitudes, NOT by finite tests',
        'samples':samples,'verification':'PASS','native_x6':'NOT_RUN','independent_review':'NOT_PERFORMED'}
    with open('/mnt/data/R4_EC16_AUTHOR_REPORT.json','w',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
    print('PASS: symbolic / 8191 words / 8-state DP n<=180 / 2 recurrences n<=2000 k<=160 / fixed edge formulas')
    print('SYMBOLIC',certificate)
    print('SAMPLES',[(s['n'],s['k'],s['log_high_low'],s['second_order_prediction']) for s in samples])

if __name__=='__main__':main()
