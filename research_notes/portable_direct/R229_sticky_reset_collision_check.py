#!/usr/bin/env python3
"""R229 exact scalar observable spectrum and collisions; standard library only.
No native Heartbeat/BRC dynamics executed.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
import json
ZERO=Q(0); ONE=Q(1)
def trim(f):
    f=list(f)
    while len(f)>1 and f[-1]==0: f.pop()
    return f
def add(a,b):
    return trim([(a[i] if i<len(a) else ZERO)+(b[i] if i<len(b) else ZERO) for i in range(max(len(a),len(b)))])
def mul(a,b):
    c=[ZERO]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return trim(c)
def divrem(a,b):
    a=trim(a); b=trim(b)
    if b==[ZERO]: raise ZeroDivisionError
    q=[ZERO]*max(1,len(a)-len(b)+1)
    while a!=[ZERO] and len(a)>=len(b):
        i=len(a)-len(b); t=a[-1]/b[-1]; q[i]=t
        for j,v in enumerate(b): a[i+j]-=t*v
        a=trim(a)
    return trim(q),a
def monic(p):
    return [x/p[-1] for x in p] if p!=[ZERO] else p
def gcd(a,b):
    while b!=[ZERO]: a,b=b,divrem(a,b)[1]
    return monic(a)
def lcm(a,b):
    return monic(mul(divrem(a,gcd(a,b))[0],b))
def P_of(alpha,pi):
    return [[(alpha[i] if i==j else ZERO)+(ONE-alpha[i])*pi[j] for j in range(len(pi))] for i in range(len(pi))]
def stationary(alpha,pi):
    u=[pi[i]/(ONE-alpha[i]) for i in range(len(pi))]
    return [v/sum(u) for v in u]
def stirling(n,j):
    if n==0:return int(j==0)
    if j==0:return 0
    a=[[0]*(j+1) for _ in range(n+1)]
    a[0][0]=1
    for i in range(1,n+1):
        for h in range(1,min(i,j)+1):a[i][h]=h*a[i-1][h]+a[i-1][h-1]
    return a[n][j]
def weights(m,k,L):
    return [factorial(r)*m**L*sum(stirling(L+1,j+1) for j in range(min(r,L)+1)) for r in range(k+1)]
def ideal_T(W,k):
    return [sum(comb(k-r,j-r)*W[j] for j in range(r,k+1)) for r in range(k+1)]
def projected_char(alpha,pi,D):
    """Characteristic polynomial of the observable group-compressed killed block."""
    groups={}
    for i in D: groups[alpha[i]]=groups.get(alpha[i],ZERO)+pi[i]
    B=sorted(groups)
    pol=[ONE]
    for beta in B: pol=mul(pol,[-beta,ONE])
    for beta in B:
        prod=[ONE]
        for other in B:
            if other!=beta: prod=mul(prod,[-other,ONE])
        term=[(ONE-beta)*groups[beta]*z for z in prod]
        pol=add(pol,[-v for v in term])
    return monic(pol)
def spectrum_polynomial(alpha,pi):
    k=len(pi)-1; out=[ONE]; blocks=[]
    for mask in range(1<<k):
        if mask==(1<<k)-1:continue
        D=[0]+[i for i in range(1,k+1) if mask&(1<<(i-1))]
        cp=projected_char(alpha,pi,D)
        blocks.append({'source_set':[i for i in D if i>0], 'poly':cp})
        out=lcm(out,cp)
    out=lcm(out,[-ONE,ONE])
    return out,blocks
def expected_ideals(m,k,L,alpha,pi,upto):
    P=P_of(alpha,pi);rho=stationary(alpha,pi)
    W=weights(m,k,L);T=ideal_T(W,k)
    states={(i,1<<(i-1) if i else 0):rho[i] for i in range(k+1)}
    res=[]
    for n in range(1,upto+1):
        if n>=L:res.append((n,sum(w*T[mask.bit_count()] for (i,mask),w in states.items())))
        nxt={}
        for (i,mask),w in states.items():
            for j,v in enumerate(P[i]):
                key=(j,mask | (1<<(j-1) if j else 0))
                nxt[key]=nxt.get(key,ZERO)+w*v
        states=nxt
    return res
def rank(M):
    a=[list(row) for row in M];R=len(a);C=len(a[0]) if R else 0
    r=0
    for j in range(C):
        pivot=next((i for i in range(r,R) if a[i][j]!=0),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        q=a[r][j];a[r]=[v/q for v in a[r]]
        for i in range(r+1,R):
            if a[i][j]:
                t=a[i][j];a[i]=[a[i][s]-t*a[r][s] for s in range(C)]
        r+=1
        if r==R:break
    return r
def fraction_str(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def test_one(m,k,L,alpha,pi):
    assert all(0<a<1 for a in alpha) and all(x>0 for x in pi) and sum(pi)==1
    poly,blocks=spectrum_polynomial(alpha,pi);d=len(poly)-1
    data=expected_ideals(m,k,L,alpha,pi,L+2*d+1)
    f={n:v for n,v in data}
    for n in range(L,L+d+2):
        assert sum(poly[j]*f[n+j] for j in range(d+1))==0,(m,k,L,alpha,pi,n)
    H=[[f[L+i+j] for j in range(d)] for i in range(d)]
    assert rank(H)==d,(m,k,L,alpha,pi,d)
    return {'degree':d,'poly':[fraction_str(z) for z in poly], 'f_L':fraction_str(f[L]),'f_L_plus_1':fraction_str(f[L+1]),'block_degrees':[len(b['poly'])-1 for b in blocks]}
def main():
    a=(Q(1,5),Q(1,3),Q(1,2))
    witness=(Q(11,56),Q(25,56),Q(20,56))
    poly,blocks=spectrum_polynomial(a,witness)
    assert len(poly)-1==5
    assert projected_char(a,witness,[0,1])==mul([-Q(3,4),ONE],[-Q(5,21),ONE])
    assert projected_char(a,witness,[0,2])==mul([-Q(3,4),ONE],[-Q(2,7),ONE])
    assert projected_char(a,witness,[0])==[-Q(5,14),ONE]
    assert stationary(a,witness)==[Q(11,73),Q(30,73),Q(32,73)]
    target=mul(mul(mul(mul([-ONE,ONE],[-Q(3,4),ONE]),[-Q(5,21),ONE]),[-Q(2,7),ONE]),[-Q(5,14),ONE])
    assert poly==target
    x=test_one(1,2,2,a,witness)
    generic=test_one(1,2,2,a,(Q(1,7),Q(2,7),Q(4,7)))
    symmetric=test_one(1,2,2,(Q(1,4),)*3,(Q(1,3),)*3)
    assert generic['degree']==6 and symmetric['degree']==3
    trials=0;degree_hist={}
    for k in (1,2,3):
        for vec in product((1,2),repeat=k+1):
            if k==3 and sum(vec)>6:continue
            pi=tuple(Q(v,sum(vec)) for v in vec)
            for a_case in range(3):
                if a_case==0:alpha=tuple(Q(1,4) for _ in vec)
                elif a_case==1:alpha=tuple(Q(i+1,2*(k+2)) for i in range(k+1))
                else:alpha=tuple(Q(1+(i%2),5) for i in range(k+1))
                result=test_one(1,k,2,alpha,pi)
                trials+=1;d=result['degree'];degree_hist[str(d)]=degree_hist.get(str(d),0)+1
    native_alphabet=test_one(12,2,2,a,witness)
    assert native_alphabet['degree']==5
    result={
        'schema':'EM_R229_EXACT_SCALAR_SPECTRAL_CHECK_V1',
        'scope':'source-support principal-ideal scalar readout on J_(m,k,L), stationary sticky-reset Markov source chain',
        'arithmetic':'Python Fraction exact rationals; polynomial Euclidean gcd/lcm; exact source-mask dynamic programming; exact Hankel Gaussian rank',
        'status':'PASS',
        'witness':{'pi':[fraction_str(i) for i in witness],'alpha':[fraction_str(i) for i in a],
                   'rho':[fraction_str(i) for i in stationary(a,witness)],
                   'spectrum':['5/14','5/21','2/7','3/4','1'],
                   'proper_block_polynomials':[{'U':b['source_set'],'coefficients_low_to_high':[fraction_str(v) for v in b['poly']]} for b in blocks],**x},
        'noncolliding_degree':generic['degree'],
        'equal_holding_equal_probability_degree':symmetric['degree'],
        'native_12_direction_alphabet_degree':native_alphabet['degree'],
        'test_parameter_configs':trials+4,
        'regression_degree_histogram':degree_hist,
        'limitations':['No native physical BRC EffectHistogram integration','No independent reviewer',
                       'General arbitrary-k theorem is author-proved, finite tests are not universal proof']}
    with open(__file__.replace('.py','_verification.json'),'w') as h:json.dump(result,h,indent=2,ensure_ascii=False)
    print('PASS',json.dumps({'trials':trials,'witness_degree':x['degree'],'generic_degree':generic['degree'],'symmetric_degree':symmetric['degree'],'histogram':degree_hist},ensure_ascii=False))
if __name__=='__main__':main()
