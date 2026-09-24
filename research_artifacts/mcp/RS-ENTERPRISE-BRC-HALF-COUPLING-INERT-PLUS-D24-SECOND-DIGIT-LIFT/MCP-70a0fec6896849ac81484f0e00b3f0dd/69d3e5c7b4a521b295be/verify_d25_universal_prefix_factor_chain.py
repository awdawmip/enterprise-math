from fractions import Fraction as F

def lam(s):
    return F(s*s*(6*s+1),(s+1)*(2*s+1)*(3*s+2))

def rho(s):
    return F((2*s+1)*(3*s+1)*(3*s+2)*(6*s+7),36*(s+1)**3*(6*s+1))

def mu(s):
    return rho(s)*lam(s+1)

def main(N=200):
    t=[F(0)]*(N+2); w=[F(0)]*(N+2); P=[F(0)]*(N+2)
    d=[F(0)]*(N+2); c=[F(0)]*(N+2); R=[F(0)]*(N+2)
    t[0]=F(1); d[0]=F(1)
    for s in range(N+1):
        w[s]=(6*s+1)*t[s]
        if s+1<=N+1:
            t[s+1]=t[s]*F((2*s+1)*(3*s+1)*(3*s+2),36*(s+1)**3)
            d[s+1]=d[s]*F((6*s+1)*(s+1),(2*s+1)*(3*s+2))
    for s in range(1,N+2):
        P[s]=P[s-1]+w[s-1]
        c[s]=d[s]/(6*s*s)
        R[s]=R[s-1]+c[s]*P[s]
    assert R[0]==0 and R[1]==F(1,12) and R[2]==F(143,1296)
    U=[F(0)]*(N+2); V=[F(0)]*(N+1)
    for s in range(1,N+2):
        U[s]=R[s]-R[s-1]
        assert U[s]==c[s]*P[s]
    assert U[1]==F(1,12)
    for s in range(1,N+1):
        V[s]=U[s+1]-lam(s)*U[s]
        assert V[s]==c[s+1]*w[s]
    assert V[1]==F(49,6480)
    for s in range(1,N):
        assert V[s+1]==mu(s)*V[s]
        A=(1+rho(s))*lam(s+1)
        B=rho(s)*lam(s)*lam(s+1)
        assert R[s+2]-(1+A)*R[s+1]+(A+B)*R[s]-B*R[s-1]==0
    print('exact_rational_indices_checked',N)
    print('failures',0)

if __name__=='__main__':
    main()
