"""D25 W216 two-digit p-adic first jet, signed row factor, finite Dwork checks.
Standalone Python 3 standard library. AUTHOR_SIDE / UNREVIEWED / NOT_NATIVE.
"""

def primes_upto(n):
    ans=[]
    for q in range(2,n+1):
        if all(q%d for d in range(2,int(q**.5)+1)):
            ans.append(q)
    return ans

def original_vu(p, count, M):
    """Strip p from the actual W216 ratio; yield valuation and unit."""
    v,u=0,1
    inv36=pow(36,-1,M)
    for k in range(count):
        yield v,u
        if k+1==count:
            return
        numerator=[3*k+1,3*k+2,2*k+1]
        denominator=k+1
        shift=0
        num_unit=1
        for n in numerator:
            while n%p==0:
                n//=p
                shift+=1
            num_unit=num_unit*n%M
        while denominator%p==0:
            denominator//=p
            shift-=3
        v+=shift
        u=u*num_unit*pow(denominator,-3,M)*inv36%M

def factorial_firstjet(p):
    M=p*p
    h=[0]*p; fac=[1]*p
    for n in range(1,p):
        h[n]=(h[n-1]+pow(n,-1,M))%M
        fac[n]=fac[n-1]*n%M
    unit=[1]*(3*p+1); valuation=[0]*(3*p+1)
    for n in range(1,3*p+1):
        t=n;v=0
        while t%p==0:
            t//=p
            v+=1
        unit[n]=unit[n-1]*t%M
        valuation[n]=valuation[n-1]+v
    return h,fac,unit,valuation

def predicted_vu(p,a,b,pre):
    M=p*p
    h,fac,unit,valuation=pre
    c2,b2=divmod(2*b,p)
    c3,b3=divmod(3*b,p)
    alpha2,alpha3=2*a+c2,3*a+c3
    val=c2+c3+valuation[alpha2]+valuation[alpha3]
    U=(pow(216,-(a*p+b),M)
       *pow(fac[p-1],c2+c3,M)
       *unit[alpha2]*unit[alpha3]*fac[b2]*fac[b3]
       *pow(fac[a],-5,M)*pow(fac[b],-5,M))%M
    U=U*(1+p*(alpha2*h[b2]+alpha3*h[b3]-5*a*h[b]))%M
    return val,U

def check(p):
    M=p*p
    pre=factorial_firstjet(p)
    rows=[0]*p
    first=[]
    for k,(v,u) in enumerate(original_vu(p,p*p,M)):
        a,b=divmod(k,p)
        predicted=predicted_vu(p,a,b,pre)
        assert (v,u)==predicted,(p,k,(v,u),predicted)
        term=u*pow(p,v,M)%M
        rows[a]=(rows[a]+(6*k+1)*term)%M
        if k<p:
            first.append((v,u))
    result={"p":p,"pairs_checked":p*p}
    if p%6!=1:
        return result
    m=(p-1)//6
    def A(k):
        v,u=first[k]
        return u*pow(p,v,M)%M
    h=pre[0]
    q=((pow(216,p-1,M)-1)//p)%p
    L0=sum((6*b+1)*A(b) for b in range(2*m+1))%M
    L1=sum((6+(6*b+1)*(2*h[2*b]+3*h[3*b]-5*h[b]-q))*A(b)
           for b in range(2*m+1))%p
    L2=sum((6*b+1)*first[b][1]
           for b in range(2*m+1,3*m+1))%p
    F0=sum(A(a) for a in range(2*m+1))%M
    F1=sum(a*A(a) for a in range(2*m+1))%p
    expect=[A(a)*(L0+p*a*L1+p*(3*a+1)*L2)%M
            if a<=2*m else 0 for a in range(p)]
    assert rows==expect,("row",p,[(a,x,y) for a,(x,y)
                                  in enumerate(zip(rows,expect)) if x!=y][:4])
    total=(F0*L0+p*F1*L1+p*(F0+3*F1)*L2)%M
    assert sum(rows)%M==total
    result.update({"row_factor":"PASS","L0":L0,"L1":L1,"L2":L2,
                   "F0_mod_p":F0%p,"F1_mod_p":F1,
                   "W_p2_mod_p2":total})
    return result

def high_precision_finite_only(p):
    assert p in (13,19)
    M=p**7
    W1=W2=0
    for k,(v,u) in enumerate(original_vu(p,p*p,M)):
        term=(6*k+1)*u*pow(p,v,M)
        if k<p:
            W1=(W1+term)%M
        W2=(W2+term)%M
    defect=(W2-p*W1)%M
    c=((W1-p)%M)//p**3%p
    assert defect%p**6==0
    assert defect//p**6==c
    return {"p":p,"W_p_mod_p7":W1,"W_p2_mod_p7":W2,
            "defect_div_p6":defect//p**6,"base_c_p":c,"status":"FINITE_PASS"}

if __name__=="__main__":
    tests=[p for p in primes_upto(59) if p>3]+[61,67,73,109,373]
    for p in tests:
        print(check(p),flush=True)
    for p in (13,19):
        print(high_precision_finite_only(p),flush=True)
    print("ALL EXACT CHECKS PASS")
