"""D25/LIFT R33 author-side finite-field audit. Not native H0/B0 or independent review."""

def primes_below(n):
    out=[]
    for q in range(2,n):
        if all(q % p for p in out if p*p<=q):
            out.append(q)
    return out

def inv(x,p):
    return pow(x%p,-1,p)

def factorial(n,p):
    k=1
    for i in range(1,n+1):
        k=k*i%p
    return k

def carrier(p):
    m=(p-1)//6
    a,h=[1],[1]
    for r in range(1,m):
        a.append(a[-1]*2*(3*r-1)**3*inv(3*r*(6*r+1)*(3*r+1),p)%p)
        h.append(h[-1]*48*r*(3*r+1)*inv((12*r-1)*(12*r+5),p)%p)
    omega=[(2*r+1)*pow(2,r,p)%p for r in range(m)]
    sigma=[(24*r+13)*inv(3,p)*pow(9,r,p)*h[r]%p for r in range(m)]
    C=3*pow(216,2*m,p)*pow(factorial(2*m,p),5,p)*inv(factorial(4*m+1,p),p)%p
    D=2*pow(2304,2*m,p)*pow(factorial(2*m,p),4,p)*inv(factorial(2*m+2,p),p)%p
    assert C and D
    psi=[C*inv(D,p)*w%p for w in omega]
    return a,h,omega,sigma,psi,C,D

def dot(w,v,p):
    return sum(wr*vr for wr,vr in zip(w,v))%p

def pf_w(f,p):
    m=len(f)
    g=[0]*(m+1)
    for t in range(1,m):
        A=t*(6*t+1)*(3*t+1)*inv(18,p)%p
        B=(3*t-1)**3*inv(27,p)%p
        g[t]=(A*f[t]-B*f[t-1])%p
    g[m]=-(3*m-1)**3*inv(27,p)*f[-1]%p
    return g

def pf_s(f,p):
    m=len(f)
    g=[0]*(m+1)
    for t in range(1,m):
        A=t*(12*t-1)*(6*t+1)*(12*t+5)*inv(864,p)%p
        B=t*(3*t-1)**3*inv(27,p)%p
        g[t]=(A*f[t]-B*f[t-1])%p
    g[m]=-m*(3*m-1)**3*inv(27,p)*f[-1]%p
    return g

def transform(p,f,sigma,psi,mu):
    m=len(f); s=m-1
    delta=(dot(psi,f,p)-mu*dot(sigma,f,p))*inv(sigma[s],p)%p
    y=[mu*x%p for x in f]
    y[s]=(y[s]+delta)%p
    return y,delta

def main():
    classes={13:0,19:0}
    pf_checks=0; fixed_zero=0; fixed_one=0; certificates=[]
    for p in primes_below(2000):
        if p%24 not in classes:
            continue
        classes[p%24]+=1
        m=(p-1)//6; s=m-1
        a,h,omega,sigma,psi,C,D=carrier(p)
        assert s>=1 and sigma[s] and psi[s]
        U=C*dot(omega,a,p)%p
        M=D*dot(sigma,a,p)%p
        phi_a=dot(sigma,a,p)
        psi_a=dot(psi,a,p)
        assert psi_a==U*inv(D,p)%p
        c=a[s]*inv(8,p)%p
        assert pf_w(a,p)==[0]*m+[c]
        for mu in (1,2,3):
            # Three independent free-input families; the map is NOT a claim about original fixed input.
            for seed in range(3):
                f=[(seed+2*r*r+3*r+1)%p for r in range(m)]
                y,delta=transform(p,f,sigma,psi,mu)
                assert dot(sigma,y,p)==dot(psi,f,p)
                assert y[0]==mu*f[0]%p
            y,delta=transform(p,a,sigma,psi,mu)
            expected=[0]*(m+1)
            As=s*(6*s+1)*(3*s+1)*inv(18,p)%p
            Bm=(3*m-1)**3*inv(27,p)%p
            expected[s]=delta*As%p
            expected[m]=(mu*c-delta*Bm)%p
            assert pf_w(y,p)==expected
            assert pf_s([h[r]*y[r]%p for r in range(m)],p)==(
                [0]+[t*h[t-1]*expected[t]%p for t in range(1,m+1)])
            assert (sum(bool(v) for v in expected[1:m])==bool(delta))
            pf_checks+=m
        y,delta=transform(p,a,sigma,psi,1)
        assert (delta!=0)==(U!=M)
        fixed_zero+=U==M
        fixed_one+=U!=M
        # Unrestricted minimal zero-source condition: both observer values are zero or both nonzero.
        if bool(phi_a)==bool(psi_a):
            mu=psi_a*inv(phi_a,p)%p if phi_a else 1
            z,dd=transform(p,a,sigma,psi,mu)
            assert mu and dd==0 and pf_w(z,p)[1:m]==[0]*(m-1)
        else:
            assert (phi_a==0)!=(psi_a==0)
        if p in (13,19,37,181,373,733):
            certificates.append((p,m,U,M,phi_a,psi_a,delta,pf_w(y,p)[s],pf_w(y,p)[m]))
    print("D25_R33_RANKONE_SINGLE_PF_PORT_PASS",
          "classes",classes,"PF_coefficient_checks",pf_checks,
          "normalized_min_zero",fixed_zero,"normalized_min_one",fixed_one,
          "certificates",certificates)

if __name__=="__main__":
    main()
