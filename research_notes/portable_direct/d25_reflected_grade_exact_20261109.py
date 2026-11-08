"""Original W216 grade-1 / grade-2 mirror (author-side exact regression)."""
from math import comb
P = [7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373]
def A(n,p,k):
    z=p**k
    return comb(2*n,n)**2 * comb(3*n,n) * pow(216,-n,z) % z
def inv(x,p):
    return pow(x,-1,p)
def check(p):
    m=(p-1)//6; q0=2*m+1; n0=3*m+1
    K1=A(q0,p,2)//p; K2=A(n0,p,3)//(p*p)
    U=[1]; V=[1]
    for j in range(m-1):
        U.append(U[-1]*(6*j+7)*(j+1)*(3*j+4)*27 *
                 inv(36*(3*j+5)**3,p)%p)
        V.append(V[-1]*(j+1)*(6*j+5)*(6*j+7)*8 *
                 inv(72*(2*j+3)**3,p)%p)
    total=0
    for j in range(m):
        q=q0+j; n=p-q
        a=A(q,p,2)//p; b=A(n,p,3)//(p*p)
        assert a and b and a==K1*U[j]%p and b==K2*V[m-1-j]%p
        assert a*b%p == inv(36*q**3,p)
        total=(total+(1-6*q)*inv(36*q**3*a,p))%p
    return m,total
if __name__=='__main__':
    results={p:check(p) for p in P}
    print('all exact reciprocal pairs:',sum(r[0] for r in results.values()))
    print('grade2 reflected sums:', {p: x[1] for p,x in results.items()})
