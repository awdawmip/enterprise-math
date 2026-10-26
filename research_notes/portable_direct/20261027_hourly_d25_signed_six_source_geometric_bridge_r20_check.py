ORDER=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))

def series_coeffs(p, mod):
    m=(p-1)//6
    deg=4
    f=[1]+[0]*deg
    out=[f]
    for k in range(0,p-1):
        # f[k+1]/f[k]=((k-m)-t)((k-2m)-2t)/((k+1)*((k+1-p/2)-3t))
        N=[(k-m)*(k-2*m), -(3*k-4*m), 2]
        D0=(k+1)*(2*(k+1)-p)
        D1=-6*(k+1)
        inv0=pow(D0,-1,mod)
        q=[0]*(deg+1)
        for i in range(deg+1):
            a=sum(f[i-j]*N[j] for j in range(min(i,2)+1))
            q[i]= ((2*a - (D1*q[i-1] if i else 0))*inv0)%mod
        f=q
        out.append(f)
    return out

def add(a,b,mod):
    d=a.copy()
    for k,v in b.items():
        d[k]=(d.get(k,0)+v)%mod
    return {k:v for k,v in d.items() if v}

def smul(a,v,mod):
    return {k:(w*v)%mod for k,w in a.items() if w*v%mod}

def mul(a,b,mod):
    c={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            if i+j+k+l>2:continue
            t=(i+k,j+l)
            c[t]=(c.get(t,0)+v*w)%mod
    return {k:v for k,v in c.items() if v}

def T(c):return {(i,0):v for i,v in enumerate(c) if v}
def S(c):return {(0,i):v for i,v in enumerate(c) if v}

def op_Q(n,m,mod):
    t=T([0,4*m]);s=S([0,14*m-3*n]);ts=add(t,s,mod)
    ts=add(ts,T([0,0,2]),mod);ts=add(ts,S([0,0,-2]),mod)
    return add({(0,0):-18*m*m+9*m*n-n*n},ts,mod)

def compute_lift(p):
    m=(p-1)//6
    mod=p**3
    high_mod=p**5
    fs=series_coeffs(p,mod)
    f=[1]
    for k in range(0,p-1):
        nxt=f[-1]*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,high_mod)%high_mod
        f.append(nxt)
    betas={r:(f[r]//(p*p))%mod for r in range(2*m+1,p)}
    for r in betas: assert f[r]%(p*p)==0
    theta=-p*pow(6,-1,mod)%mod
    L,N=1-2*m,2*m-1
    def q(r):return S(fs[r][2:5])
    def low(r):return T(fs[r][:3])
    def eval_dpoly(a):return sum(v*pow(theta,i+j,mod) for (i,j),v in a.items())%mod
    direct_plus=direct_minus=lifted_plus=lifted_minus=0
    for n in range(L,N+1):
        if n>=0:
            F=add(mul(T([2*m*m,4*m,2]),q(p-n-1),mod),smul(mul(S([6*m*m,-8*m,2]),mul(low(2*m-n),q(4*m),mod),mod),-1,mod),mod)
            e=(2*(m+theta)**2*betas[p-n-1]-(6*m*m-8*m*theta+2*theta*theta)*f[2*m-n]*betas[4*m])%mod
        else:
            F=add(mul(S([20*m*m,-14*m,2]),mul(low(-n),q(p-1),mod),mod),mul(T([0,2*m,-2]),mul(low(2*m),q(p-(2*m+n+1)),mod),mod),mod)
            e=((20*m*m-14*m*theta+2*theta*theta)*f[-n]*betas[p-1]+(2*m*theta-2*theta*theta)*f[2*m]*betas[p-(2*m+n+1)])%mod
        direct=(e*pow(2,n,mod))%mod
        lifted=(eval_dpoly(F)*pow(36,-1,mod)*pow(2,n,mod))%mod
        assert direct==lifted,(p,n,direct,lifted)
        if n<0:
            direct_minus=(direct_minus+direct)%mod
            lifted_minus=(lifted_minus+lifted)%mod
        else:
            direct_plus=(direct_plus+direct)%mod
            lifted_plus=(lifted_plus+lifted)%mod
    assert (direct_plus,direct_minus)==(lifted_plus,lifted_minus)
    return {"status":"PASS","Gminus_p3":direct_minus,"Gplus_p3":direct_plus,"Gtotal_p3":(direct_plus+direct_minus)%mod}

def compute(p,precision=1):
    mod=p**precision
    m=(p-1)//6
    assert p>3 and p%6==1
    fs=series_coeffs(p,mod)
    for r in range(2*m+1,p): assert fs[r][0]==fs[r][1]==0,(p,r,fs[r])
    F={};U={};V={}
    L=1-2*m;N=2*m-1
    for n in range(L,N+1):
        V[n]={};U[n]={}
        for j in range(1,2*m+1):
            ell=j+n
            if ell<1 or ell>2*m:continue
            part=mul(T(fs[j][:3]),S(fs[p-ell][2:5]),mod)
            V[n]=add(V[n],part,mod)
            U[n]=add(U[n],smul(part,j,mod),mod)
        if n>=0:
            p1=mul(T([2*m*m,4*m,2]),S(fs[p-n-1][2:5]),mod)
            p2=mul(S([6*m*m,-8*m,2]),mul(T(fs[2*m-n][:3]),S(fs[4*m][2:5]),mod),mod)
            F[n]=add(p1,smul(p2,-1,mod),mod)
        else:
            p1=mul(S([20*m*m,-14*m,2]),mul(T(fs[-n][:3]),S(fs[p-1][2:5]),mod),mod)
            p2=mul(T([0,2*m,-2]),mul(T(fs[2*m][:3]),S(fs[p-(2*m+n+1)][2:5]),mod),mod)
            F[n]=add(p1,p2,mod)
    def pu(n):return add(add({(0,0):p-2*n},T([0,-3]),mod),S([0,-3]),mod)
    def pv(n):return add({(0,0):-(p-n)*(p-2*n)*pow(2,-1,mod)%mod},S([0,3*(p-n)]),mod)
    def qu(n):return add(add({(0,0):6*m-2*n},T([0,-3]),mod),S([0,-3]),mod)
    for n in range(L,N+1):
        lhs=add(mul(pu(n),U[n],mod),mul(pv(n),V[n],mod),mod)
        un=U.get(n+1,{});vn=V.get(n+1,{})
        rhs=add(mul(qu(n),un,mod),mul(op_Q(n,m,mod),vn,mod),mod)
        assert add(lhs,smul(rhs,-1,mod),mod)==F[n], (p,n,'rank',lhs,rhs,F[n])
    z=2
    def zpow(n): return pow(z,n,mod)
    def sum_face(pred):
        out={}
        for n in range(L,N+1):
            if pred(n): out=add(out,smul(F[n],zpow(n),mod),mod)
        return out
    neg=sum_face(lambda n:n<0);pos=sum_face(lambda n:n>=0)
    tot=add(neg,pos,mod)
    transported={}
    for n in range(L,N+1):
        a=add(mul(pu(n),U[n],mod),mul(pv(n),V[n],mod),mod)
        transported=add(transported,smul(a,zpow(n),mod),mod)
        b=add(mul(qu(n-1),U[n],mod),mul(op_Q(n-1,m,mod),V[n],mod),mod)
        transported=add(transported,smul(b,-zpow(n-1),mod),mod)
    bl=add(mul(qu(L-1),U[L],mod),mul(op_Q(L-1,m,mod),V[L],mod),mod)
    transported=add(transported,smul(bl,zpow(L-1),mod),mod)
    assert transported==tot,(p,'geo transport',transported,tot)
    def jet(v):
        a,b,c,d,e,f=(v.get(k,0) for k in ORDER)
        return ((a%mod,(b+c)%mod,(d+e+f)%mod),((b-c)%mod,2*(d-f)%mod),(2*(d-e+f)%mod,))
    orig=None
    if precision==1:
        lift=compute_lift(p)
        assert lift["status"]=="PASS"
        orig=lift
    return {"p":p,"m":m,"negative":jet(neg),"positive":jet(pos),"total":jet(tot),"raw_total":tuple(tot.get(k,0) for k in ORDER),"endpoint":tuple(bl.get(k,0) for k in ORDER),"Fsample":{n:tuple(F[n].get(k,0) for k in ORDER) for n in (L,0,1) if n<=N}, "lift":orig}

if __name__ == "__main__":
    from fractions import Fraction
    from math import isqrt

    def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
    ps=[p for p in range(7,998) if p%6==1 and prime(p)]
    zeros=[]
    for p in ps:
        result=compute(p)
        if result['lift']['Gtotal_p3']==0:zeros.append(p)
        assert result['lift']['Gtotal_p3']%p == result['total'][0][0]*pow(36,-1,p)%p
        if p in (7,13,19,37,733):
            print(f'{p}: finite-origin six-channel (S,A,B)={result["total"]}; negative={result["negative"]}; positive={result["positive"]}; original G modulo p^3={result["lift"]["Gtotal_p3"]}')
    assert len(ps)==80,(len(ps),ps)
    assert compute(19)['total'][0][1]==0 and compute(19)['total'][1][0]==7
    assert compute(733)['total'][0][0]==49 and compute(733)['lift']['Gtotal_p3']%733==714
    assert 7 in zeros
    print('PASS: prime_count=',len(ps),'p^3-vanishing_finite_sources=',zeros)

    for p in [7,13,19]:
        m=(p-1)//6;theta=Fraction(-p,6)
        f=[Fraction(1)]
        for k in range(p-1):
            f.append(f[-1]*Fraction((6*k+1)*(3*k+1),18*(k+1)**2))
        beta={r:f[r]/p**2 for r in range(2*m+1,p)}
        G=Fraction(0)
        for n in range(1-2*m,2*m):
            if n>=0:
                E=2*(m+theta)**2*beta[p-n-1]-(6*m*m-8*m*theta+2*theta*theta)*f[2*m-n]*beta[4*m]
            else:
                E=(20*m*m-14*m*theta+2*theta*theta)*f[-n]*beta[p-1]+(2*m*theta-2*theta*theta)*f[2*m]*beta[p-(2*m+n+1)]
            G+=Fraction(2**n) *E if n>=0 else Fraction(1,2**(-n))*E
        modulus=p**3
        exact_mod=G.numerator*pow(G.denominator,-1,modulus)%modulus
        assert exact_mod==compute(p)['lift']['Gtotal_p3'],(p,exact_mod)
        print(f'Fraction-independent-source p={p}: PASS, v_p(G)=',end='')
        if G==0:print('infty')
        else:
            num=abs(G.numerator);den=G.denominator;v=0
            while num%p==0:v+=1;num//=p
            while den%p==0:v-=1;den//=p
            print(v)
