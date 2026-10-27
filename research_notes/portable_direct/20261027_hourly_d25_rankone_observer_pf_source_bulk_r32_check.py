"""D25/LIFT R32: exact finite-field author check; not native H0/B0 or formal admission."""

def primes_below(limit):
    out = []
    for n in range(2, limit):
        if all(n % q for q in out if q*q <= n):
            out.append(n)
    return out

def inv(x, p):
    return pow(x % p, -1, p)

def carrier(p):
    m = (p-1)//6
    a, h = [1], [1]
    for r in range(1,m):
        h.append(h[-1]*48*r*(3*r+1)*inv((12*r-1)*(12*r+5),p)%p)
        a.append(a[-1]*2*(3*r-1)**3*inv(3*r*(6*r+1)*(3*r+1),p)%p)
    W = [(2*r+1)*pow(2,r,p)%p for r in range(m)]
    S = [(24*r+13)*inv(3,p)*pow(9,r,p)*h[r]%p for r in range(m)]
    return a,h,W,S

def transport(p, W, S):
    m=len(W)
    d=[W[r]*inv(S[r],p)%p if S[r] else 1 for r in range(m)]
    if p%24==19:
        assert all(S)
        return d,None,None,0
    assert p%24==13
    q=(p-13)//24
    assert S[q]==0 and sum(v==0 for v in S)==1
    s=q+1
    assert s<m and S[s]
    return d,q,s,W[q]*inv(S[s],p)%p

def applyT(p,f,d,q,s,beta):
    y=[d[r]*f[r]%p for r in range(len(f))]
    if q is not None:
        y[s]=(y[s]+beta*f[q])%p
    return y

def pf_w(p,f):
    m=len(f); out=[0]*(m+1)
    for t in range(1,m):
        A=t*(6*t+1)*(3*t+1)*inv(18,p)%p
        B=(3*t-1)**3*inv(27,p)%p
        out[t]=(A*f[t]-B*f[t-1])%p
    out[m]=-(3*m-1)**3*inv(27,p)*f[m-1]%p
    return out

def pf_s(p,f):
    m=len(f); out=[0]*(m+1)
    for t in range(1,m):
        A=t*(12*t-1)*(6*t+1)*(12*t+5)*inv(864,p)%p
        B=t*(3*t-1)**3*inv(27,p)%p
        out[t]=(A*f[t]-B*f[t-1])%p
    out[m]=-m*(3*m-1)**3*inv(27,p)*f[m-1]%p
    return out

def A(t):
    return 216*t*(2*t-1)*(3*t+1)*(24*t+13)

def B(t):
    return (2*t+1)*(24*t-11)*(12*t-1)*(12*t+5)

def main():
    byclass={13:0,19:0}; pf_coeff_checks=0; records=[]
    for p in primes_below(2000):
        if p%24 not in byclass:
            continue
        m=(p-1)//6
        a,h,W,S=carrier(p)
        d,q,s,beta=transport(p,W,S)
        byclass[p%24]+=1
        assert all(a) and all(h) and all(d) and all(W)
        for seed in range(3):
            f=[(seed+3*r*r+5*r+1)%p for r in range(m)]
            y=applyT(p,f,d,q,s,beta)
            assert sum(S[r]*y[r] for r in range(m))%p==sum(W[r]*f[r] for r in range(m))%p
            g=pf_w(p,y)
            gs=pf_s(p,[h[r]*y[r]%p for r in range(m)])
            for t in range(1,m+1):
                assert gs[t]==t*h[t-1]*g[t]%p,(p,t)
                pf_coeff_checks+=1
        y=applyT(p,a,d,q,s,beta)
        g=pf_w(p,y)
        assert pf_w(p,a)[1:m]==[0]*(m-1)
        c=a[m-1]*inv(8,p)%p
        assert pf_w(p,a)[m]==c
        u=[y[r]*inv(a[r],p)%p for r in range(m)]
        nonzero=0
        excluded={q,q+1,s,s+1} if q is not None else set()
        for t in range(1,m):
            At=t*(6*t+1)*(3*t+1)*inv(18,p)%p
            assert g[t]==At*a[t]*(u[t]-u[t-1])%p
            nonzero+=bool(g[t])
            if t not in excluded:
                assert A(t)%p and B(t)%p
                assert (d[t]*A(t)-d[t-1]*B(t))%p==0
                assert (g[t]==0)==((A(t)-B(t))%p==0)
        assert g[m]==c*u[-1]%p
        assert nonzero>=max(0,m-(9 if q is not None else 5))
        if p in (13,19,43,181,373,733):
            records.append((p,m,q,s,beta,nonzero,g[m]))
    print("D25_R32_ONE_SHEAR_SOURCE_BULK_PASS",
          "p13",byclass[13],"p19",byclass[19],
          "PF_coefficient_checks",pf_coeff_checks,
          "samples",records)

if __name__=="__main__":
    main()
