from math import factorial, comb, isqrt

def prime_list(limit):
    return [p for p in range(7, limit+1, 6) if all(p%d for d in range(2, isqrt(p)+1))]

def check(p):
    m=(p-1)//6
    P=p*p
    inv=lambda x,M:pow(x%M,-1,M)
    f=[1]*p
    for i in range(1,p):f[i]=(f[i-1]*i)%p
    B=f[2*m-1]*f[2*m]*inv(f[4*m],p)%p

    # Low first-order Jacobian expansion, using full mod p² for the base.
    low_base=0;low_jet=0; eps=0
    termwise=[]
    for n in range(m+1):
        k0=((1-3*n)*(6*n+3)*inv((3*n+2)*(3*n+1),P))%P
        bn=(-1)**n*comb(m,n)*pow(inv(2,P),n,P)%P
        E=(eps + 2*inv(1-3*n,p) + 2*inv(6*n+3,p)
             - inv(3*n+2,p)-2*inv(3*n+1,p))%p
        base=bn*k0%P
        low_base=(low_base+base)%P
        low_jet=(low_jet+base*E)%p
        termwise.append(base*(1+p*E)%P)
        if n<m:
            eps=(eps+3*inv(6*n+1,p)-inv(3*n+2,p)-2*inv(3*n+1,p))%p

    # High exact p-unit transport from normalized 2m seam in two sectors.
    h1=0;h2=0
    for s in range(1,m):
        am=pow(2,m-s,p)*f[2*m]*f[s-1]*inv(f[m+s]*f[m-1],p)%p
        ka=4*(1-2*s)*(3*s+1)*inv((2*s+1)*(6*s+1),p)%p
        h1=(h1+am*ka)%p
    for s in range(1,2*m):
        bm=inv(24,p)*pow(inv(2,p),s-1,p)*f[2*m+1]*f[m+s-1]*inv(f[m]*f[2*m+s],p)%p
        kb=(2-3*s)*(6*s+1)*inv(3*s*(3*s+1),p)%p
        h2=(h2-bm*kb)%p
    high=B*(h1+h2)%p

    H=sum(inv(i,p) for i in range(1,2*m+1))%p
    q=(pow(6,p-1,P)-1)//p
    fac=lambda n:factorial(n)
    G=(((-1)**m*fac(2*m)**3)*inv(fac(3*m)**2,P))%P
    Bfull=(fac(2*m-1)*fac(2*m)*inv(fac(4*m),P))%P
    seam_correction=B*(28-6*H-12*q)*inv(9,p)%p
    assert (low_base-G+Bfull)%p==0
    divided=((low_base-G+Bfull)%P)//p
    defect=(divided+low_jet+high+seam_correction)%p

    # Completely independent original hypergeometric recurrence, n=0..4m.
    v=0;u=1;low_actual=0;hi_actual=0; T2=None
    for n in range(4*m):
        if n==2*m:T2=u%P; assert v==1
        if n!=2*m:
            kden=(3*n+p+2)*(3*n+2*p+1)
            k=(2*p+1-3*n)*(6*n+2*p+3)*inv(kden,P)%P
            x=k*u*pow(p,v,P)%P
            if n<=m:
                assert x==termwise[n],(p,n,x,termwise[n])
                low_actual=(low_actual+x)%P
            else: hi_actual=(hi_actual+x)%P
        a=(4*m+1+2*n)*(3*n+1)*(3*n+2)
        b=36*(n+1)*(2*m+n+1)*(4*m+n+1)
        while a%p==0:a//=p;v+=1
        while b%p==0:b//=p;v-=1
        u=u*a*inv(b,P)%P
    assert low_actual==(low_base+p*low_jet)%P,(p,low_actual,low_base,low_jet)
    assert hi_actual%P==(p*high)%P,(p,hi_actual,high)
    assert T2%p==B,(p,T2,B)
    assert defect==0,(p,defect)
    return p,divided,low_jet,high,seam_correction,defect

if __name__=='__main__':
    rows=[check(p) for p in prime_list(1000)]
    print('p=1 mod6 primes',len(rows),'joint-author-check PASS')
    for row in rows:
        if row[0] in (13,19,31,37,61):print('joint',row)
