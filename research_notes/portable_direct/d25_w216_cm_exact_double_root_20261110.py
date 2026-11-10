"""D25/W216 finite polynomial Clausen square and CM precise double root.
All p>3, p=6m+1: coefficientwise. CM0/SIMPLE are frozen source inputs.
Pure stdlib; finite regression does not serve as universal proof or native run.
"""

def prime(n):
    return n >= 2 and all(n % k for k in range(2, int(n**0.5) + 1))

def check(p):
    assert p % 6 == 1 and prime(p)
    m = (p-1)//6
    inv36 = pow(36,-1,p)
    beta=[1]
    for n in range(m):
        beta.append(beta[-1]*(6*n+1)*(3*n+1)*inv36
                    *pow(n+1,-2,p)%p)
    alpha=[1]
    for k in range(2*m):
        alpha.append(alpha[-1]*(3*k+1)*(3*k+2)*(2*k+1)
                     *inv36*pow(k+1,-3,p)%p)
    for k in range(2*m+1):
        square=sum(beta[i]*beta[k-i]
                   for i in range(max(0,k-m),min(k,m)+1))%p
        assert square == alpha[k],(p,k,alpha[k],square)
    M=sum(beta)%p
    N=sum(n*beta[n] for n in range(m+1))%p
    K=sum(n*(n-1)*beta[n] for n in range(m+1))%p
    F0=sum(alpha)%p
    F1=sum(k*alpha[k] for k in range(2*m+1))%p
    F2=sum(k*(k-1)*alpha[k] for k in range(2*m+1))%p
    assert F0 == M*M%p
    assert F1 == 2*M*N%p
    assert F2 == (2*N*N+2*M*K)%p
    if p%24 in (13,19):
        assert M == 0 and N != 0,(p,M,N)
        assert F0 == F1 == 0 and F2 == 2*N*N%p and F2 != 0
    return (p,m,M,N,F0,F1,F2)

if __name__ == "__main__":
    seen=[check(p) for p in range(7,1001) if p%6==1 and prime(p)]
    target=[x for x in seen if x[0]%24 in (13,19)]
    print("coefficientwise Clausen all p=1 mod6 under 1000:",len(seen))
    print("target CM double roots exact checked:",len(target))
    for x in target:
        if x[0] in (13,19,37,43,61,67,109,373):
            print(x)
    print("ALL EXACT CHECKS PASS")
