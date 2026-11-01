"""Original hypergeometric companion p³ jet and actual cutoff tail (not native H0/B0)."""

def primes_under(n):
    return [p for p in range(5,n) if all(p%d for d in range(2,int(p**.5)+1))]

def certificate(p):
    m=p**3
    h1=next(i for i in range(p) if (8*i+1)%p==0)
    h3=next(i for i in range(p) if (8*i+3)%p==0)
    r=min(h1,h3);b=max(h1,h3)
    lam=1 if p%8 in (1,3) else 5
    delta=lam*p*pow(8,-1,m)%m
    beta=1;f=1;g=j=0
    L=(4*r+1)*pow(2,-1,m)%m
    z=1; iz=pow(9,-1,m); i64=pow(64,-1,m)
    sums={'full':0,'cut':0,'tail':0,'F':0,'G':0,'J':0,'Gtail':0,'Jtail':0,'theta_tail':0}
    for n in range(p):
        assert beta==(f+delta*g+delta*delta*j)%m,(p,n)
        value=beta*z%m
        sums['full']=(sums['full']+value)%m
        if n<=b:sums['cut']=(sums['cut']+value)%m
        else:
            sums['tail']=(sums['tail']+value)%m
            sums['Gtail']=(sums['Gtail']+delta*g*z)%m
            sums['Jtail']=(sums['Jtail']+delta*delta*j*z)%m
            sums['theta_tail']=(sums['theta_tail']+n*value)%m
            assert beta%(p*p)==0
            if p>=11:assert beta%m!=0
        sums['F']=(sums['F']+f*z)%m
        sums['G']=(sums['G']+delta*g*z)%m
        sums['J']=(sums['J']+delta*delta*j*z)%m
        if n==p-1:break
        inv=pow((n+1)**2,-1,m)
        beta=beta*(8*n+1)*(8*n+3)*i64*inv%m
        a=(n-r)*(n+r+pow(2,-1,m))%m
        f,g,j=a*f*inv%m,(a*g+L*f)*inv%m,(a*j+L*g-f)*inv%m
        z=z*iz%m
    assert sums['full']==(sums['cut']+sums['tail'])%m
    assert sums['full']==(sums['F']+sums['G']+sums['J'])%m
    assert sums['tail']==(sums['Gtail']+sums['Jtail'])%m
    return (p,r,b,sums)

def independent_tail(p):
    from math import factorial
    h1=next(i for i in range(p) if (8*i+1)%p==0)
    h3=next(i for i in range(p) if (8*i+3)%p==0)
    b=max(h1,h3)
    q1=(8*h1+1)//p;q3=(8*h3+3)//p
    tot=0
    for n in range(b+1,p):
        nu=q1*q3
        for i in range(n):
            if i!=h1:nu=nu*(8*i+1)%p
            if i!=h3:nu=nu*(8*i+3)%p
        den=pow(576,n,p)*pow(factorial(n),2,p)%p
        tot=(tot+nu*pow(den,-1,p))%p
    return tot

if __name__=='__main__':
    ps=primes_under(300)
    for p in ps:certificate(p)
    print('PASS_D25_ORIGINAL_K_P3_SECOND_JET_AND_TAIL',len(ps),'primes under 300')
    for p in (13,23,37,61,373):
        d=certificate(p)
        assert d[3]['tail']//(p*p)==independent_tail(p)
        print('INDEPENDENT_TAIL',p,independent_tail(p))
    print('P373',certificate(373))
