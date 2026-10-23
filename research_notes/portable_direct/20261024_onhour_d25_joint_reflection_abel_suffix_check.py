"""D25 joint LOW/HIGH reflection and Abel-suffix certificate.
Author integer modular checks only; NOT a native benchmark or admitted Result.
"""
from math import comb, factorial, isqrt

def primes_1mod6(limit):
    return [p for p in range(7, limit + 1, 6)
            if all(p % d for d in range(2, isqrt(p) + 1))]

def verify(p):
    m=(p-1)//6
    p2=p*p
    inv=lambda a,mod=p:pow(a%mod,-1,mod)
    power=lambda a,b:pow(a%p,b,p)
    f=[1]*(p+1)
    for t in range(1,p+1): f[t]=f[t-1]*t%p
    B=f[2*m-1]*f[2*m]*inv(f[4*m])%p
    C=m*comb(2*m,m)*pow(2,m,p)%p
    gamma=((-1)**m)*B*C%p

    # Original TWO distinct high sectors, independently of the reflection.
    h1=h2=0
    for s in range(1,m):
        a=power(2,m-s)*f[2*m]*f[s-1]*inv(f[m+s]*f[m-1])%p
        ka=4*(1-2*s)*(3*s+1)*inv((2*s+1)*(6*s+1))%p
        h1=(h1+a*ka)%p
    for s in range(1,2*m):
        c=power(2,1-s)*f[2*m+1]*f[m+s-1]*inv(f[m]*f[2*m+s])%p
        kb=(2-3*s)*(6*s+1)*inv(3*s*(3*s+1))%p
        h2=(h2-c*kb*inv(24))%p
    high_orig=B*(h1+h2)%p

    I=[(r,1 if r<m else inv(3)) for r in range(1,3*m) if r!=m]
    def F(n):
        return sum(w*power(2,-r)*inv(r+n) for r,w in I)%p
    F6=sum(w*power(2,-r)*inv(6*r+1) for r,w in I)%p
    F2=sum(w*power(2,-r)*inv(2*r+1) for r,w in I)%p

    def k(j):
        return (1-3*j)*(6*j+3)*inv((3*j+2)*(3*j+1))%p
    def kappa_ref(n):
        return (-2+4*inv(1-6*n)+2*inv(1-2*n))%p
    def Q(n):
        return (inv(2*(n+1)) - power(2,-m)*inv(n+m)
                + power(2,-m-1)*inv(3)*inv(n+m+1)
                - power(2,-3*m)*inv(3)*inv(n+3*m))%p

    for n in range(m+1):
        assert (F(n)-F(n+1)*inv(2)-Q(n))%p==0,(p,n,'boundary')
        assert (k(m-n)-kappa_ref(n))%p==0,(p,n,'reflection')

    rising6=rising2=1
    for i in range(m+1):
        rising6=rising6*(6*i-1)*inv(6)%p
        rising2=rising2*(2*i-1)*inv(2)%p
    P=(4*f[m]*inv(rising6)*F6 +2*f[m]*inv(rising2)*F2)%p
    assert (C*(2*f[m]*inv(rising2))+m*power(2,3*m+2))%p==0,(p,'rank2')

    low_jet=low_base=reflected_low_sum=raw_mr_sum=local_sum=e=0
    tlist=[]
    for j in range(m+1):
        bn=(-1)**j*comb(m,j)*power(2,-j)%p
        kj=k(j)
        d=(2*inv(1-3*j)+2*inv(6*j+3)-inv(3*j+2)-2*inv(3*j+1))%p
        D=(e+d)%p
        t=bn*kj%p
        tlist.append(t)
        local_sum=(local_sum+t*d)%p
        low_jet=(low_jet+t*D)%p
        reflected_low_sum=(reflected_low_sum+t*(D+gamma*power(2,j)*F(m-j)))%p
        raw_mr_sum=(raw_mr_sum+(-1)**j*comb(m,j)*kappa_ref(j)*F(j))%p
        if j<m:
            e=(e+3*inv(6*j+1)-inv(3*j+2)-2*inv(3*j+1))%p
        b_full=(-1)**j*comb(m,j)*pow(inv(2,p2),j,p2)%p2
        k_full=(1-3*j)*(6*j+3)*inv((3*j+2)*(3*j+1),p2)%p2
        low_base=(low_base+b_full*k_full)%p2
    A=sum(tlist)%p
    suffix=abel_suffix=0
    for j in range(m-1,-1,-1):
        suffix=(suffix+tlist[j+1])%p
        eps=(3*inv(6*j+1)-inv(3*j+2)-2*inv(3*j+1))%p
        forcing=(eps+gamma*power(2,j+1)*Q(m-j-1))%p
        abel_suffix=(abel_suffix+forcing*suffix)%p
    abel_joint=(local_sum+gamma*F(m)*A+abel_suffix+B*C*P)%p
    high_mr=B*C*(raw_mr_sum+P)%p
    high_joint=(reflected_low_sum-low_jet+B*C*P)%p
    assert high_orig==high_mr==high_joint,(p,high_orig,high_mr,high_joint)
    assert abel_joint==(low_jet+high_orig)%p,(p,abel_joint,low_jet,high_orig)

    # Independently preserve original first-digit and seam terms.
    G=(-1)**m*factorial(2*m)**3*inv(factorial(3*m)**2,p2)%p2
    Bfull=factorial(2*m-1)*factorial(2*m)*inv(factorial(4*m),p2)%p2
    assert (low_base-G+Bfull)%p==0,(p,'first-digit')
    low_div=((low_base-G+Bfull)%p2)//p
    H=sum(inv(i) for i in range(1,2*m+1))%p
    q=(pow(6,p-1,p2)-1)//p
    seam=B*(28-6*H-12*q)*inv(9)%p
    joint=(low_div+reflected_low_sum+B*C*P+seam)%p
    abel_defect=(low_div+abel_joint+seam)%p
    orig=(low_div+low_jet+high_orig+seam)%p
    assert orig==joint==abel_defect==0,(p,joint,orig,abel_defect)
    return p,m,high_orig,low_div,low_jet,high_mr,B*C*P%p,seam,joint,local_sum,gamma*F(m)*A%p,abel_suffix

if __name__=='__main__':
    pp=primes_1mod6(1000)
    rows=[verify(p) for p in pp]
    print('PASS:',len(rows),'p=6m+1 primes <=1000; original high, reflected rank-two and Abel agree')
    print('p mod24 in (13,19):',sum(p%24 in (13,19) for p in pp))
    for row in rows:
        if row[0] in (7,13,19,31,37,61):print(row)
