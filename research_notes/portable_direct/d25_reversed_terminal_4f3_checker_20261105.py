"""Exact finite-field certification of the D25 reversed 216 shell.
No network, third-party packages, floating point, or native H0/B0 substitution.
"""
import json

def primes_upto(limit):
    sv = bytearray(b'\x01') * (limit + 1)
    sv[:2] = b'\x00\x00'
    for i in range(2,int(limit**0.5)+1):
        if sv[i]: sv[i*i::i]=b'\x00'*(((limit-i*i)//i)+1)
    return [i for i in range(7,limit+1) if sv[i] and i%6==1]

def inv(x,p):
    return pow(x%p,-1,p)

def checked(p):
    n=(p-1)//6
    f=[1]*p
    for j in range(1,p): f[j]=f[j-1]*j%p
    C=pow(216,2*n,p)*pow(f[2*n],5,p)*inv(f[4*n+1],p)%p
    h=[1]
    for r in range(n-1):
        num=2*pow(3*r+2,3,p)
        den=3*(6*r+7)*(3*r+4)*(r+1)
        h.append(h[-1]*num*inv(den,p)%p)
    g=[1]
    for k in range(n-1):
        num=2*(k+1)*(6*k+5)*(6*k+7)
        den=9*pow(2*k+3,3)
        g.append(g[-1]*num*inv(den,p)%p)
    assert len(g)==len(h)==n and h[-1]!=0
    for k in range(n):
        assert h[n-1-k]==h[-1]*g[k]%p, ('reverse',p,k)
    for j in range(1,n):
        a=(j*pow(2*j+1,3,p)*g[j])%p
        b=(j*j*(6*j-1)*(6*j+1)*g[j-1])%p
        assert (9*a-2*b)%p==0, ('operator',p,j)
    assert (n*n*(6*n-1)*(6*n+1)*g[-1])%p==0, ('terminal',p)
    assert h[-1]*inv(8,p)%p !=0
    twoinv=inv(2,p)
    front=sum((2*r+1)*h[r]*pow(2,r,p) for r in range(n))%p
    upper=3*C*front%p
    end=C*h[-1]*pow(2,n-1,p)%p
    revsum=sum((3*k+2)*g[k]*pow(twoinv,k,p) for k in range(n))%p
    reverse=(-2*end*revsum)%p
    assert reverse==upper, ('observation',p,upper,reverse)
    raw=0
    for j in range(2*n+1,3*n+1):
        num=(6*j-1)*pow(216,j-1,p)*pow(f[j-1],5,p)
        den=f[2*j-1]*f[3*j-p-1]
        raw=(raw+num*inv(den,p))%p
    assert raw==upper, ('source shell',p,raw,upper)
    return dict(p=p,n=n,source_shell=raw,forward=upper,reverse=reverse,
                terminal_unweighted=end,dual_weighted=revsum,
                homogeneous_order_four=True,forward_terminal_coefficient=h[-1]*inv(8,p)%p)

if __name__=='__main__':
    cases=[checked(p) for p in primes_upto(10000)]
    anchors=[x for x in cases if x['p'] in (7,13,19,139,373)]
    out={'status':'EXACT_CHECKED','count':len(cases),'prime_filter':'7<=p<=10000, prime p=1 mod 6',
         'source':'Original factorial shell and independent forward/reversed rational coefficients',
         'nonzero_forward_source_count':sum(1 for x in cases if x['forward_terminal_coefficient']!=0),
         'anchors':anchors,'failures':0,
         'scope':'Finite exact check; algebraic proof is separate; NOT native H0/B0'}
    print(json.dumps(out,indent=2))
