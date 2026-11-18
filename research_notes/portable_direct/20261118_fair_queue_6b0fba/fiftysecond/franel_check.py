"""Exact arithmetic for two-digit Franel congruences and the unit/valuation laws."""
from collections import Counter
from itertools import product
from math import comb, gcd, isqrt
import json


def digit_table(p,power=3):
    H=[0]
    for j in range(1,p):
        H.append((H[-1]+pow(j,-1,p))%p)
    F,L=[],[]
    for b in range(p):
        coeff=[comb(b,j)**power for j in range(b+1)]
        F.append(sum(coeff)%(p*p))
        L.append(power*sum(v*(H[b]-H[j]) for j,v in enumerate(coeff))%p)
    return F,L


def recurrence(N):
    f=[1,2]
    for n in range(1,N):
        q,r=divmod((7*n*n+7*n+2)*f[-1]+8*n*n*f[-2],(n+1)**2)
        assert r==0
        f.append(q)
    return f


def subgroup_order(values,modulus,phi):
    factors = []
    n=phi
    for r in range(2,isqrt(n)+1):
        if n%r==0:
            factors.append(r)
            while n%r==0:
                n//=r
    if n>1:
        factors.append(n)
    # Unit groups here are cyclic. The least common multiple of element orders suffices.
    result=1
    for v in set(values):
        order=phi
        for r in factors:
            while order%r==0 and pow(v,order//r,modulus)==1:
                order//=r
        result=result//gcd(result,order)*order
    return result


def digits_formula(n,p,F,L):
    v=w=1
    while n:
        n,b=divmod(n,p)
        v=v*(F[b]+p*(n%p)*L[b])%(p*p)
        w=w*F[b]%(p*p)
    return v,w


def class_counts(p,m,F,L):
    good=[b for b,f in enumerate(F) if f%p]
    bad=[b for b,f in enumerate(F) if f%p==0]
    g=len(good)
    top=sum((F[b]//p)%p!=0 for b in bad)
    mid=sum((F[b]//p+a*L[b])%p!=0 for b,a in product(bad,good))
    one=top*g**(m-1)
    if m>=2:
        one+=(m-1)*g**(m-2)*mid
    return [g**m,one,p**m-g**m-one]


def by_digits(p,m,F,L):
    states=Counter({(0,1):1})
    for _ in range(m):
        nxt=Counter()
        for (a,r),number in states.items():
            for b in range(p):
                key=(b,r*(F[b]+p*a*L[b])%(p*p))
                nxt[key]+=number
        states=nxt
    bins=Counter()
    for (_,r),v in states.items():
        bins[r]+=v
    return bins


def val_one_formula(p,m,F,L):
    good=[b for b,f in enumerate(F) if f%p]
    bad=[b for b,f in enumerate(F) if f%p==0]
    mu=Counter(F[b]%p for b in good)
    def mul(x,y):
        out=Counter()
        for a,na in x.items():
            for b,nb in y.items():
                out[a*b%p]+=na*nb
        return out
    powers=[Counter({1:1})]
    for _ in range(m-1):
        powers.append(mul(powers[-1],mu))
    top=Counter(F[b]//p%p for b in bad if F[b]//p%p)
    ans=mul(top,powers[m-1])
    if m>1:
        mid=Counter(F[a]*(F[b]//p+a*L[b])%p for a,b in product(good,bad)
                    if (F[b]//p+a*L[b])%p)
        for r,n in mul(mid,powers[m-2]).items():
            ans[r]+=(m-1)*n
    return ans


def cyclic_support(p,F,L):
    good=[b for b,f in enumerate(F) if f%p]
    ell={b:L[b]*pow(F[b],-1,p)%p for b in good}
    K=subgroup_order([F[b] for b in good],p*p,p*(p-1))
    H=subgroup_order([F[b]%p for b in good],p,p-1)
    states=Counter({(0,1,0):1})
    T=4
    for _ in range(T):
        before=states
        states=Counter()
        for (a,d,e),count in before.items():
            for b in good:
                states[b,d*F[b]%(p*p),(e+a*ell[b])%p]+=count
    out=Counter()
    for (_,d,e),v in states.items():
        out[d,e]+=v
    assert sum(out.values())==len(good)**T
    complete=Counter()
    for ds in product(good,repeat=T):
        n=0
        for b in ds:n=p*n+b
        f,d=digits_formula(n,p,F,L)
        e=(f*pow(d,-1,p*p)%(p*p)-1)//p
        complete[d,e]+=1
    assert out==complete
    E=Counter()
    for (_,e),v in out.items(): E[e]+=v
    return dict(K_size=K,H_size=H,joint_limit_size=K*(p if p>=5 else 1),
                m=T,unit_words=len(good)**T,naive_exact_good_words=E[0],
                actual_joint_support=len(out))


def main():
    exact=recurrence(4100)
    for n in range(151):
        assert exact[n]==sum(comb(n,j)**3 for j in range(n+1))
    ps=[p for p in range(3,998,2) if all(p%q for q in range(2,isqrt(p)+1))]
    samples={}
    for p in ps:
        if p>41:break
        F,L=digit_table(p)
        good=[b for b,f in enumerate(F) if f%p]
        bad=[b for b,f in enumerate(F) if not f%p]
        for n,v in enumerate(exact):
            fitted,_=digits_formula(n,p,F,L)
            assert fitted==v%(p*p)
        for b in range(p):
            assert (L[b]==0)==all((exact[a*p+b]-exact[a]*F[b])%(p*p)==0 for a in range(p))
        rows=[]
        for m in (1,2,3,5,8):
            hist=by_digits(p,m,F,L)
            vals=[sum(v for r,v in hist.items() if r%p),
                  sum(v for r,v in hist.items() if r%p==0 and r),hist[0]]
            assert vals==class_counts(p,m,F,L)
            assert {r//p:c for r,c in hist.items() if r%p==0 and r}==val_one_formula(p,m,F,L)
            if p**m<=len(exact):
                assert hist==Counter(v%(p*p) for v in exact[:p**m])
            rows.append(dict(m=m,v0_v1_vge2=vals))
        samples[p]={'good_digit_count':len(good),'bad_digit_rows':[
            {'b':b,'e':F[b]//p,'L':L[b],'annihilating_good_neighbors':[
                a for a in good if (F[b]//p+a*L[b])%p==0]} for b in bad],
            'all_prefix_Lucas_digits':[b for b in range(p) if L[b]==0],
            'counts':rows}
        if p<=29 and p in (3,5,7,11,29):
            samples[p]['joint_distribution']=cyclic_support(p,F,L)
    orders=Counter()
    for p in ps:
        f=[1,2]
        for n in range(1,p-1):
            f.append(((7*n*n+7*n+2)*f[-1]+8*n*n*f[-2])*pow((n+1)**2,-1,p)%p)
        v=subgroup_order([x for x in f if x],p,p-1)
        orders[(p-1)//v]+=1
    w=[]
    for n in (335,418,505):
        q=exact[n];v=0
        while q%29==0:
            q//=29;v+=1
        w.append(dict(n=n,digits_base29_high_first=list(divmod(n,29)),valuation=v,F_mod_29cubed=exact[n]%29**3))
    family_checks=0
    for p in (3,5,7,11):
        for power in range(2,8):
            F,L=digit_table(p,power)
            for n in range(p*p):
                expected=sum(comb(n,j)**power for j in range(n+1))%(p*p)
                assert digits_formula(n,p,F,L)[0]==expected
                family_checks+=1
            if power%p==0:assert all(x==0 for x in L)
    print(json.dumps(dict(direct_binomial_max_n=150,independent_integer_recurrence_max_n=4100,
                         other_power_direct_cases=family_checks,primes_through_997=len(ps),index_histogram_for_mod_p_digit_subgroup=orders,
                         exact_digit_samples=samples,p29_witnesses=w),indent=2))
if __name__=='__main__':
    main()
