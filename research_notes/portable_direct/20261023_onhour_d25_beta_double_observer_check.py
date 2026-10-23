"""Independent p-adic LOW/Beta certificate, based on proven exact Beta shifts.
Finite-test only; not native Enterprise Math benchmark or global proof.
"""
from math import factorial
from fractions import Fraction
from hashlib import sha256

def inv(a,q): return pow(a%q,-1,q)

def beta_moments(m,q):
    # U_s(r)=int_0^1 x^(r-1)(x-1/2)^s dx (mod q), s>=0
    def U(s):
        z=[0]*(3*m+1)
        z[1] = (1+(-1)**s)*inv(pow(2,s+1,q)*(s+1),q)%q
        for r in range(1,3*m):
            # (s+r+1)*U(r+1) - (r/2)*U(r) = 1/2^(s+1)
            z[r+1] = (inv(pow(2,s+1,q),q) + r*inv(2,q)*z[r])*inv(s+r+1,q)%q
        return z
    U_m=U(m); U_prev=U(m-1)
    T=[0]*(3*m+1)
    T[1]=(-1)**m*inv(pow(2,m+1,q)*(m+1),q)%q
    for r in range(1,3*m):
        T[r+1] = T[r]*r*inv(2*(m+r+1),q)%q
    return U_m,U_prev,T

def beta_digits(p):
    assert p>=7 and p%6==1
    m=(p-1)//6;q=p*p
    U,Up,T=beta_moments(m,q)
    # theta = 2^-m(3(-1)^m-2) + I_m + J1_m
    th=(3*(-1)**m-2)*inv(pow(2,m,q),q)%q
    V=J2=0
    H=[0]*(4*m+1);H2=[0]*(4*m+1)
    for k in range(1,4*m+1):
        a=inv(k,p)
        H[k]=(H[k-1]+a)%p
        H2[k]=(H2[k-1]+a*a)%p
    for r in range(1,3*m+1):
        wt=1 if r<=m else inv(3,q)
        th +=wt*(3*m*Up[r]+U[r]+(3*r+inv(2,q)*(p-2))*T[r])
        th%=q
        # V and J2 only need mod p
        w=1 if r<=m else inv(3,p)
        V=(V+w*U[r])%p
        dr = m-r if r<=m else r-m-1
        Jr = (inv(2,p)*(H[r-1]-H[m])+inv(3,p)*2*(H[2*m]-H[dr])+
              inv(3,p)*(H[4*m]-H[3*m-r])+3*inv(2*(3*r-1),p))%p
        J2=(J2+w*((3*r-1)*Jr-inv(2,p))*T[r])%p
    fp=f2=1
    for k in range(1,p):
        fp=fp*k%q
        if k<=2*m: f2=f2*k%q
    A=fp*inv(pow(3,p-1,q)*pow(f2,3,q),q)%q
    assert (A*th-1)%p==0,(p,A*th%p)
    delta=((A*th-1)%q)//p
    # C_m=1/2 alternating harmonic + 2/3[H_2m-H_m] + 1/3[H_4m-H_m]
    alt=sum(((-1)**j*inv(j,p) for j in range(1,m+1)),0)%p
    C=(inv(2,p)*alt+2*inv(3,p)*(H[2*m]-H[m])+inv(3,p)*(H[4*m]-H[m]))%p
    low2=0; a1=b1=c1=a2=b2=c2=0;b=1
    i2=inv(2,p);i3=inv(3,p);i8=inv(8,p);i9=inv(9,p);i18=inv(18,p)
    for n in range(m+1):
        L=(-i2*a1+2*i3*b1+i3*c1)%p
        K=(-i8*a2+4*i9*b2+5*i18*c2)%p
        M=(K+i2*L*L)%p
        low2=(low2+b*(6*n-1)*M)%p
        if n<m:
            aa=inv(m-n,p);bb=inv(2*m-n,p);cc=inv(4*m-n,p)
            a1=(a1+aa)%p; b1=(b1+bb)%p;c1=(c1+cc)%p
            a2=(a2+aa*aa)%p;b2=(b2+bb*bb)%p;c2=(c2+cc*cc)%p
            b=(-b*(m-n)*inv(2*(n+1),p))%p
    ep=(low2+J2-2*V)%p
    rat=pow(4*inv(3,q),p-1,q)
    assert rat%p==1
    chi=(rat-1)//p
    residual=(delta+(A%p)*((inv(pow(2,m,p),p)*C+ep)%p)-chi)%p
    return {"p":p,"beta_residual":residual,"second_moment":ep,"theta_digit":delta,"global_C":C,
            "chi":chi,"M":low2,"J2":J2,"V":V,"A":A%p,
            "second_moment_A":A*ep%p}

def primes_upto(limit):
    marked=bytearray(b"\x01")*(limit+1)
    marked[:2]=b"\x00\x00"
    for k in range(2,int(limit**0.5)+1):
        if marked[k]:
            marked[k*k::k]=b"\x00"*((limit-k*k)//k+1)
    return [p for p in range(7,limit+1) if marked[p] and p%6==1]

def exact_fraction_E(m):
    # Independent polynomial-expansion integrals and harmonic sums.
    from math import comb
    F=Fraction
    def H(k,r=1):
        return sum((F(1,j**r) for j in range(1,k+1)),F(0))
    def moment(r,top):
        return sum((F(comb(m,j)*(-1)**(m-j),2**(m-j))*top**(r+j)/F(r+j)
                    for j in range(m+1)), F(0))
    M=F(0)
    for n in range(m+1):
        A=H(m)-H(m-n); B=H(2*m)-H(2*m-n); C=H(4*m)-H(4*m-n)
        A2=H(m,2)-H(m-n,2); B2=H(2*m,2)-H(2*m-n,2)
        C2=H(4*m,2)-H(4*m-n,2)
        L=-A/2+F(2,3)*B+F(1,3)*C
        K=-A2/8+F(4,9)*B2+F(5,18)*C2
        M+=F((-1)**n*comb(m,n),2**n)*(6*n-1)*(K+L*L/2)
    V=J2=F(0)
    for r in range(1,3*m+1):
        weight=F(1) if r<=m else F(1,3)
        U=moment(r,F(1)); T=moment(r,F(1,2))
        d=m-r if r<=m else r-m-1
        Jr=(H(r-1)-H(m))/2+F(2,3)*(H(2*m)-H(d))+F(1,3)*(H(4*m)-H(3*m-r))+F(3,2*(3*r-1))
        V+=weight*U
        J2+=weight*((3*r-1)*Jr-F(1,2))*T
    return M+J2-2*V

def as_mod(q,p):
    assert q.denominator%p != 0
    return q.numerator*inv(q.denominator,p)%p

if __name__=='__main__':
    for p,want in [(7,Fraction(-649,1296)),
                   (13,Fraction(-262753327,812851200)),
                   (19,Fraction(-1568555346923,14163119308800))]:
        m=(p-1)//6
        exact=exact_fraction_E(m)
        assert exact==want,(p,exact,want)
        assert as_mod(exact,p)==beta_digits(p)['second_moment']
    primes=primes_upto(10000)
    assert len(primes)==611
    assert sum(p%24 in (13,19) for p in primes)==312
    records=[];nonzero=0;fails=[]
    for p in primes:
        d=beta_digits(p)
        if d['beta_residual']: fails.append((p,d))
        nonzero+=bool(d['second_moment'])
        records.append(f"{p},{d['theta_digit']},{d['global_C']},{d['second_moment']},{d['chi']},{d['beta_residual']}\n")
    data=''.join(records).encode('ascii')
    digest=sha256(data).hexdigest()
    assert digest=='700559f007680b9935bd406d8692f941532ed55486fb114f2a9e07f9d272e849',(digest,records[-1])
    assert not fails,fails[:3]
    assert nonzero==611,nonzero
    print('PASS',len(primes),'TARGET_CLASS',312,'BETA_FAILURES',len(fails),
          'NONZERO_QUADRATIC_MOMENT',nonzero,'SHA256',digest)
    print('SAMPLES',records[1].strip(),records[2].strip(),records[-1].strip())
