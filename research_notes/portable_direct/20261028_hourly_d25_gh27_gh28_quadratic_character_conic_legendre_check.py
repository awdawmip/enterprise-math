"""GH-27/GH-28 exact finite-field checker; author evidence only, not native EM."""
from math import comb

def ps(N):
    a=bytearray(b'\1')*N; a[:2]=b'\0\0'
    for j in range(2,int(N**0.5)+1):
        if a[j]: a[j*j:N:j]=b'\0'*((N-1-j*j)//j+1)
    return [p for p in range(11,N) if a[p] and p%8==3]

def chi(a,p):
    x=a%p
    return 0 if not x else (1 if pow(x,(p-1)//2,p)==1 else -1)

def poly_even(p,m):
    # P_n((2/3)*sqrt(2)) as (rational, sqrt(2) coefficient).
    q=2*pow(3,-1,p)%p
    v0=(1,0); v1=(0,q)
    for n in range(1,2*m):
        xv=(2*q*v1[1]%p,q*v1[0]%p)
        iv=pow(n+1,-1,p)
        v2=tuple(((2*n+1)*xv[i]-n*v0[i])*iv%p for i in range(2))
        v0,v1=v1,v2
    return v1

def run():
    cnt=[0,0,0]; cases=[]
    for p in ps(2001):
        m=(p-3)//8; inv2=pow(2,-1,p)
        # Original GH-26 fibers: full nonexcluded x-source, not a fitted sigma.
        f={}
        bad={0,p-1,(-pow(9,-1,p))%p}
        for x in range(p):
            if x in bad: continue
            v=(1+9*x)*pow(9*x*(1+x)%p,-1,p)%p
            f[v]=f.get(v,0)+chi(1+x,p)
        for u in range(1,p):
            v=u*u*inv2%p
            qplus=3*u*u+8*u+6; qminus=3*u*u-8*u+6
            assert f.get(v,0)==chi(3,p)*(chi(qplus,p)+chi(qminus,p)),(p,u)
        sf=sum(chi(x,p)*pow(x*(1+x),3*m+1,p)*pow(1+9*x,m,p)
               for x in range(p))%p
        coeff=sum(comb(3*m+1,m-j)*comb(m,j)*pow(9,j,p)
                  for j in range(m+1))%p
        quad=pow(9*inv2,m,p)*chi(3,p)*sum(
            pow(u,2*m,p)*chi(3*u*u+8*u+6,p) for u in range(p))%p
        conic=pow(2,-m,p)*sum(
            pow(w-4,2*m,p)*chi(w*w+2,p) for w in range(p))%p
        psum=pow(2,-3*m,p)*sum(
            pow(s-8-2*pow(s,-1,p),2*m,p) for s in range(1,p))%p
        ct=sum(comb(2*m,2*j)*comb(2*j,j)*(-2)**j*8**(2*m-2*j)
               for j in range(m+1))%p
        c0,c1=1,-8
        for n in range(1,2*m):
            c0,c1=c1,(-8*(2*n+1)*c1-72*n*c0)*pow(n+1,-1,p)%p
        assert ct==c1%p
        pe,podd=poly_even(p,m)
        assert podd==0
        assert sf==-coeff%p==quad==conic==psum==(-pow(2,-3*m,p)*ct)%p==(-pow(9,m,p)*pe)%p,(p,sf,coeff,quad,conic,psum,ct,pe)
        cnt[0]+=1
        if p%24==19: cnt[1]+=int(sf==0)
        else: cnt[2]+=int(sf==0)
        if p in (11,19,43,67,83,139): cases.append((p,m,sf,coeff,pe))
    print("PASS_GH27_SIGNED_FIBER",cnt[0])
    print("PASS_GH28_ORIGINAL_SOURCE_CONIC_CT_LEGENDRE",cnt[0])
    print("FINITE_OBSERVATIONS_CLASS19_ZERO",cnt[1],"of",sum(p%24==19 for p in ps(2001)))
    print("FINITE_OBSERVATIONS_CLASS11_ZERO",cnt[2],"of",sum(p%24==11 for p in ps(2001)))
    print("SAMPLES",cases)

if __name__=="__main__": run()
