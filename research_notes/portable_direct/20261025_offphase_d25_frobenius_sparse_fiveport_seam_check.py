#!/usr/bin/env python3
"""Author-side exact F_p[[z]] source-port and sparse Frobenius seam test."""
def unit(x,p):
    v=x%p
    assert v,(x,p)
    return pow(v,-1,p)
def zeros(d): return [0]*d
def one(d): return [1]+[0]*(d-1)
def mul(f,g,p):
    d=len(f); h=zeros(d)
    for i,a in enumerate(f):
        if a:
            for j,b in enumerate(g[:d-i]): h[i+j]=(h[i+j]+a*b)%p
    return h
def add(f,g,p): return [(a+b)%p for a,b in zip(f,g)]
def lin(a,b,p,d): return [a%p,b%p]+[0]*(d-2)
def inverse(f,p):
    d=len(f); inv0=unit(f[0],p); out=zeros(d); out[0]=inv0
    for n in range(1,d):
        out[n]=(-inv0*sum(f[k]*out[n-k] for k in range(1,n+1)))%p
    return out
def rat(num,den,p,d): return mul(num,inverse(den,p),p)
def apply(f,c,e,p):
    d=len(f); c%=p
    if e>0:
        for _ in range(e):
            for i in range(d-1,0,-1): f[i]=(f[i]+c*f[i-1])%p
    else:
        for _ in range(-e):
            for i in range(1,d): f[i]=(f[i]-c*f[i-1])%p
    return f
def fermat_q_modp(a,p): return (pow(a,p-1,p*p)-1)//p
def products(p,d,compressed=False):
    m=(p-1)//6; n=2*m
    t=fermat_q_modp(108,p); a=fermat_q_modp(2,p); b=fermat_q_modp(3,p)
    f=one(d)
    apply(f,t,-1,p)
    for k in range(2,n+1): apply(f,-unit(k,p),2,p)
    if compressed: apply(f,-1,-2,p)
    else:
        for j in range(1,p-1): apply(f,unit(j,p),2,p)
    for j in range(1,n): apply(f,unit(j,p),-1,p)
    s=one(d)
    for c,e in [(-1,2),(2,2),(5,2),(8,1),(11,1)]:
        apply(s,unit(c,p),-e,p)
    apply(s,a,-2,p); apply(s,b,-3,p)
    for j in range(1,n): apply(s,-unit(j,p),2,p)
    if not compressed:
        for j in range(1,p): apply(s,unit(j,p),2,p)
    for j in range(1,6): apply(s,unit(j,p),1,p)
    for j in range(1,5): apply(s,2*unit(j,p),1,p)
    apply(s,2,1,p)
    for j in range(1,3): apply(s,unit(j,p),-2,p)
    for j in range(1,n+5): apply(s,unit(j,p),-1,p)
    return f,s
def poly_rational(p,d):
    def polys(*factor_list):
        f=one(d)
        for a,b in factor_list: f=mul(f,lin(a,b,p,d),p)
        return f
    Cnum=mul(polys((1,1),(-1,2),(-1,2)),[40,77,30]+[0]*(d-3),p)
    Cden=polys((2,0),(2,1),(1,2),(-1,4),(5,4))
    C=rat(Cnum,Cden,p,d)
    R={}
    for k in (1,2,3):
        num=polys((2*k+3,2),(3*k-1,2),(3*k,2))
        den=polys((4,0),(3*k+1,2),(k+2,1),(3*k+11,4))
        R[k]=rat(num,den,p,d)
    B=zeros(d); accum=one(d)
    for j in range(1,5):
        B=add(B,mul(lin(6*j+7,6,p,d),accum,p),p)
        if j<4: accum=mul(accum,R[j],p)
    return C,B
def source_quotient(p,d,f,s):
    C,B=poly_rational(p,d)
    m=(p-1)//6
    left=[(2*m*x)%p for x in mul(C,f,p)]
    sb=mul(B,s,p)
    right=[0]+[(3*unit(220,p)*sb[i])%p for i in range(d-1)]
    return add(left,right,p)
def sparse_shift(f,p):
    d=len(f); h=zeros(d)
    for i,v in enumerate(f):
        h[i]=(h[i]+v)%p
        if i+p-1<d: h[i+p-1]=(h[i+p-1]-2*v)%p
        if i+2*(p-1)<d: h[i+2*(p-1)]=(h[i+2*(p-1)]+v)%p
    return h
def sparse_unshift(f,p):
    d=len(f); h=zeros(d); step=p-1
    for i,v in enumerate(f):
        if v:
            for j in range((d-1-i)//step+1):
                h[i+j*step]=(h[i+j*step]+(j+1)*v)%p
    return h
def run():
    params=[(13,171),(19,63),(31,93),(37,111),(43,129),(61,183)]
    for p,d in params:
        direct_u,direct_s=products(p,d,False)
        small_u,small_s=products(p,d,True)
        assert direct_u==sparse_shift(small_u,p),('U',p,d)
        assert direct_s==sparse_shift(small_s,p),('sigma',p,d)
        direct_q=source_quotient(p,d,direct_u,direct_s)
        small_q=source_quotient(p,d,small_u,small_s)
        assert direct_q==sparse_shift(small_q,p),('five port',p,d)
        assert small_q==sparse_unshift(direct_q,p),('inverse',p,d)
        assert (direct_q[p-1]-small_q[p-1])%p==(-4*unit(3,p))%p
        print('PASS',p,d,'h(p-1)=',small_q[p-1],
              'q(p-1)=',direct_q[p-1])
    print('ALL',len(params),'SUCCESS')
if __name__=='__main__': run()
