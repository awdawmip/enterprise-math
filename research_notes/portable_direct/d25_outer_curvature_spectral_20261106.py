"""Independent F_p curvature: reflected binomial spectral recurrence,
second-order harmonic head/carry-tail, and full mod-p^3 finite differences.
TASK_RESEARCH author-side evidence; UNREVIEWED/NOT_ADMITTED.
"""
from math import comb, factorial, isqrt


def primes(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for q in range(2,isqrt(n)+1):
        if sieve[q]:
            sieve[q*q:n+1:q]=b'\x00'*((n-q*q)//q+1)
    return [q for q in range(7,n+1) if sieve[q] and q%6==1]


def spectral(p):
    assert p%6==1
    m=(p-1)//6; a=2*m; b=3*m
    inv=[0]+[pow(k,-1,p) for k in range(1,b+1)]
    A,B,C=1,0,0
    v=1
    first=0; curv=0
    h=0; t=0
    for j in range(b+1):
        w=(6*j+1)*v%p
        first=(first+w*B)%p
        curv=(curv+w*C)%p
        if j<=a: h=(h+w*C)%p
        else: t=(t+w*C)%p
        if j<b:
            r=inv[j+1]**2%p
            L=(a-j)*(a+j+1)%p
            A,B,C=(L*A*r)%p, ((L*B+(2*j+1)*A)*r)%p, ((L*C+(2*j+1)*B-A)*r)%p
            v=v*(b-j)*pow(2,-1,p)*inv[j+1]%p
    return first,curv,h,t


def harmonic(p):
    m=(p-1)//6;a=2*m;b=3*m
    inv=[0]+[pow(k,-1,p) for k in range(1,a+b+1)]
    H=[0]*(a+b+1);H2=[0]*(a+b+1)
    for k in range(1,a+b+1):
        H[k]=(H[k-1]+inv[k])%p
        H2[k]=(H2[k-1]+inv[k]*inv[k])%p
    inv2=pow(2,-1,p)
    head=tail=first=0
    fact=[1]*(a+b+1)
    for k in range(1,a+b+1):fact[k]=fact[k-1]*k%p
    ifact=[1]*(a+b+1)
    ifact[-1]=pow(fact[-1],-1,p)
    for k in range(a+b,0,-1):ifact[k-1]=ifact[k]*k%p
    choose=lambda n,k:fact[n]*ifact[k]*ifact[n-k]%p
    wt=1
    for j in range(b+1):
        w=(6*j+1)*wt%p
        if j<=a:
            A=choose(a,j)*choose(a+j,j)%p
            D=(2*H[a]-H[a-j]-H[a+j])%p
            E=(H2[a+j]-H2[a-j])%p
            first=(first+w*A*D)%p
            head=(head+w*A*(D*D-E)*inv2)%p
        else:
            # derivative of binom(a+t,j) at t=0, times binom(a+j,j)
            B=(-1 if (j-a-1)%2 else 1)*fact[a]*fact[j-a-1]*ifact[j]*choose(a+j,j)%p
            D=(2*H[a]-H[j-a-1]-H[a+j])%p
            first=(first+w*B)%p
            tail=(tail+w*B*D)%p
        if j<b:wt=wt*(b-j)*inv[j+1]*inv2%p
    return first,(head+tail)%p,head,tail


def full_sum(p, shift):
    # shift in the outer two labelled coordinates; central source fixed.
    mod=p**3;m=(p-1)//6;s=(2*m,3*m,4*m)
    i=[0]+[pow(j,-1,mod) for j in range(1,p)]
    bh=pow(2,-1,mod); u=1; fac=[1,1,1]; total=0
    for j in range(p):
        total=(total+(6*j+1)*u*fac[0]*fac[1]*fac[2])%mod
        if j!=p-1:
            for k in range(3):
                fac[k]=(fac[k]*(s[k]+(p*shift if k!=1 else 0)-j)*i[j+1])%mod
            u=u*(-bh)%mod
    return total


def direct(p):
    mod=p**3
    w0=full_sum(p,0); wp=full_sum(p,1); wm=full_sum(p,-1)
    d=(wp+wm-2*w0)%mod
    assert d%p**2==0,(p,d)
    return d//p**2*pow(2,-1,p)%p


def jet_poly(p, order=3, reflected=True):
    """F_p(t) coefficients modulo p through t**order, p=6m+1 prime.
    reflected: Legendre-type paired recurrence. False: original unreflected
    (a+t)(c+t) source factors, with the original -1/2 prefactor.
    """
    m=(p-1)//6;a=2*m;b=3*m;c=4*m
    inv=[0]+[pow(k,-1,p) for k in range(1,b+1)]
    g=[1]+[0]*order
    wt=1
    out=[0]*(order+1)
    for j in range(b+1):
        w=(6*j+1)*wt%p
        out=[(out[k]+w*g[k])%p for k in range(order+1)]
        if j==b:break
        if reflected:
            L=(a-j)*(a+j+1)
            M=2*j+1
            N=-1
            ratio=pow(2*(j+1),-1,p)
        else:
            L=(a-j)*(c-j)
            M=a+c-2*j
            N=1
            ratio=-pow(2*(j+1),-1,p)
        d=inv[j+1]**2%p
        g=[(L*g[k] + (M*g[k-1] if k>=1 else 0) + (N*g[k-2] if k>=2 else 0))*d%p for k in range(order+1)]
        wt=wt*(b-j)*ratio%p
    return out

def main():
    count=0
    for p in primes(5000):
        s=spectral(p); h=harmonic(p)
        assert s==h,(p,s,h)
        assert s[0]==0,(p,s)
        a=jet_poly(p);b=jet_poly(p,reflected=False)
        assert a==b,(p,a,b)
        assert a[:3]==[0,s[0],s[1]],(p,a,s)
        count+=1
    print('spectral_vs_harmonic_vs_unreflected_third_jet',count,'/','330', 'PASS')
    examples=[7,13,19,109,211,229,373,1093,3511,5113]
    print('p,first,c,head,tail,direct')
    for p in examples:
        s=spectral(p); h=harmonic(p); x=direct(p)
        assert s==h and s[1]==x,(p,s,h,x)
        print(p,*s,x,jet_poly(p)[3],sep=',')
    assert jet_poly(5113)==[0,0,0,3783]
    assert jet_poly(5113,reflected=False)==[0,0,0,3783]
    print('exact_direct_checks',len(examples),'PASS')
    print('p5113_jet',jet_poly(5113),'triple_root_certificate=PASS')

if __name__=='__main__':main()
