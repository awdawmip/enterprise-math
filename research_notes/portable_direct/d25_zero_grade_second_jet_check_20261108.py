"""D25 W216 / V2304 zero-valuation grade: p-adic quadratic binomial jets.

Author-side reproducible mathematics; does NOT execute native H0/B0.
Run: python d25_zero_grade_second_jet_check_20261108.py [bound]
"""
from math import isqrt, comb
import sys

PARAMS={"W216": ((1,2),(1,3),(2,3)), "V2304": ((1,4),(1,2),(3,4))}
BASE={"W216":2,"V2304":9}
WEIGHT={"W216":6,"V2304":8}


def primes_upto(x):
    q=bytearray(b'\x01')*(x+1)
    q[:2]=b'\x00\x00'
    for d in range(2,isqrt(x)+1):
        if q[d]:q[d*d::d]=b'\x00'*((x-d*d)//d+1)
    return [p for p in range(5,x+1) if q[p]]


def zero_grade(p,model,independent=True):
    assert p>3
    m=p**3; m2=p**2; inv2=pow(2,-1,m)
    params=[]
    for a,d in PARAMS[model]:
        r=(-a*pow(d,-1,p))%p
        assert (a+d*r)%p==0
        k=(a+d*r)//p
        ell=k*pow(d,-1,m)%m
        params.append((r,ell))
    last=min(r for r,_ in params)
    assert last==((p-1)//3 if model=='W216' else (p-1)//4)
    B=1; D1=0; D2=0
    A=J=K=jet=direct=0
    base_inv=pow(BASE[model],-1,m)
    scalar_inv=1
    fac=[1]*p
    if independent:
        for k in range(1,p): fac[k]=fac[k-1]*k%m
        invfac=[pow(x,-1,m) for x in fac]
        denom_inv=pow(216 if model=='W216' else 2304,-1,m)
        denom_pow=1
    for n in range(last+1):
        v=WEIGHT[model]*n+1
        a=v*B%m
        j=a*D1%m
        k=a*(D1*D1-D2)*inv2%m
        tj=(a-p*j+p*p*k)%m
        A=(A+a)%m;J=(J+j)%m2;K=(K+k)%p
        jet=(jet+tj)%m
        if independent:
            if model=='W216':
                td=v*fac[2*n]*fac[3*n]*pow(invfac[n],5,m)*denom_pow%m
            else:
                td=v*fac[4*n]*pow(invfac[n],4,m)*denom_pow%m
            assert td==tj,(p,model,n,td,tj,params)
            direct=(direct+td)%m
            denom_pow=denom_pow*denom_inv%m
        if n<last:
            q=1
            for r,ell in params:
                x=r-n
                q=q*x%m
                t=pow(x,-1,m)
                D1=(D1+ell*t)%m
                D2=(D2+ell*ell*t*t)%m
            B=B*(-q)*pow(n+1,-3,m)*base_inv%m
    assert (A-p*J+p*p*K)%m==jet
    assert not independent or direct==jet
    return dict(p=p,model=model,cutoff=last,rs=[r for r,_ in params],
                A=A,J=J,K=K,jet=jet,original=direct if independent else None)


def grade_one(p,model):
    mod=p*p
    f=[1]*p
    for i in range(1,p):f[i]=f[i-1]*i%mod
    invf=[pow(x,-1,mod) for x in f]
    omega=((f[p-1]+1)%mod)//p
    h=[0]*p
    for a in range(1,p):h[a]=(h[a-1]+pow(a,-1,p))%p
    if model=='W216':
        left=(p+2)//3; right=(p-1)//2; degree=3; weight=6;denom=216
    else:
        left=(p+3)//4;right=(p-1)//2;degree=4;weight=8;denom=2304
    bp=hp=0
    dp=pow(denom,-left,mod)
    for n in range(left,right+1):
        a=degree*n-p
        b=-(weight*n+1)*f[a]* (f[2*n] if model=='W216' else 1) *pow(invf[n],5 if model=='W216' else 4,mod)*dp%mod
        bp=(bp+b)%mod
        hp=(hp+b*h[a])%p
        dp=dp*pow(denom,-1,mod)%mod
    return dict(B=bp,H=hp,omega=omega,grade1_over_p=(bp+p*(hp-omega*bp))%mod)


def full_orig(p):
    mod=p**3
    invw=pow(216,-1,mod); invv=pow(2304,-1,mod)
    grades=[[0]*3 for _ in range(2)]
    pw=pv=1
    for n in range(p):
        ew=2*n//p+3*n//p
        ev=4*n//p
        if ew<3:grades[0][ew]=(grades[0][ew]+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pw)%mod
        if ev<3:grades[1][ev]=(grades[1][ev]+(8*n+1)*comb(4*n,2*n)*comb(2*n,n)**2*pv)%mod
        pw=pw*invw%mod;pv=pv*invv%mod
    return grades


def signed_tail_from_3f2(p):
    """Previously proved all-prime original W216 grade-two finite-kernel formula."""
    m=(p+4)//6
    h=1; total=0
    for r in range(m):
        total=(total+(6*r+4)*h)%p
        if r+1<m:
            h=h*(r+1)*(6*r+5)*(6*r+7)*pow(9*(2*r+3)**3,-1,p)%p
    leg=pow(6,(p-1)//2,p)
    chi=1 if leg==1 else -1
    assert leg in (1,p-1)
    return chi*pow(9,-1,p)*total%p


def single(p,full=False):
    w=zero_grade(p,'W216');v=zero_grade(p,'V2304')
    g=grade_one(p,'W216');h=grade_one(p,'V2304')
    mod=p**3
    # True all-prime level: W0-V0=DeltaA - p DeltaJ + p² DeltaK.
    dA=(w['A']-v['A'])%mod;dJ=(w['J']-v['J'])%(p*p);dK=(w['K']-v['K'])%p
    B=(g['B']-h['B'])%(p*p);H=(g['H']-h['H'])%p
    assert g['omega']==h['omega']
    lower=(dA+p*(B-dJ)+p*p*(dK+H-g['omega']*B))%mod
    # Combined zero-grade and grade-one original exact certificate from distinct evaluators.
    assert lower==(w['original']-v['original']+p*(g['grade1_over_p']-h['grade1_over_p']))%mod
    tail=signed_tail_from_3f2(p)
    # Genuine independent high-grade bridge: previous all-prime hypergeometric
    # source-port theorem + Guo-Zudilin V2304 aggregate tail-zero theorem.
    whole=(lower+p*p*tail)%mod
    assert whole==0,('allprime W-V conjectural numerical falsifier',p,whole)
    if full:
        grades=full_orig(p)
        assert grades[0][0]==w['original'] and grades[1][0]==v['original']
        assert grades[0][1]//p==g['grade1_over_p'] and grades[1][1]//p==h['grade1_over_p']
        tW=grades[0][2]//(p*p);tV=grades[1][2]//(p*p)
        assert tW==tail and tV==0
        assert (lower+p*p*(tW-tV))%mod==(sum(grades[0])-sum(grades[1]))%mod
        return dict(p=p, W=w, V=v, firstW=g,firstV=h,
                    deltaA=dA,deltaJ=dJ,deltaK=dK,deltaB=B,deltaH=H,
                    lower_residue=lower,tW=tW,tV=tV,full_W=sum(grades[0])%mod,full_V=sum(grades[1])%mod,
                    full_diff=(sum(grades[0])-sum(grades[1]))%mod)
    return dict(p=p,signed_tail=tail,whole_diff=whole,deltaA=dA,deltaJ=dJ,deltaK=dK,deltaB=B,deltaH=H,
                lower=lower, W0=w['jet'],V0=v['jet'])

if __name__=='__main__':
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 2000
    ps=primes_upto(bound)
    for p in ps:
        single(p)
    print('all-prime termwise quadratic zero-grade-jet checks',2*len(ps),'primes',len(ps),'max_p',max(ps))
    for p in (5,11,13,19,37,373):
        if p<=bound:
            d=single(p,full=True)
            print('witness',p,{k:v for k,v in d.items() if k not in ('W','V','firstW','firstV')})
            print('  zero W', {k:v for k,v in d['W'].items() if k in ('cutoff','rs','A','J','K','original')})
            print('  zero V', {k:v for k,v in d['V'].items() if k in ('cutoff','rs','A','J','K','original')})
