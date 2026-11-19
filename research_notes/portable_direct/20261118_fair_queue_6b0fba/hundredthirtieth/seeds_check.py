"""Residue-degree-three seed lines. Python 3.9+, only standard-library arithmetic."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt
import json

ZERO=(0,0)
ONE=(1,0)
OMEGA=(0,1)  # omega=zeta+zeta^2+zeta^4; omega^2+omega+2=0


def add(x,y):
    return x[0]+y[0], x[1]+y[1]


def sub(x,y):
    return x[0]-y[0], x[1]-y[1]


def mul(x,y):
    a,b=x
    c,d=y
    return a*c-2*b*d,a*d+b*c-b*d


def conjugate(x):
    return x[0]-x[1],-x[1]


def norm(x):
    return mul(x,conjugate(x))[0]


def global_point(v):
    pivot=next(x for x in v if x!=ZERO)
    den=norm(pivot)
    nums=[n for x in v for n in mul(x,conjugate(pivot))]
    div=gcd(den,*nums)
    return (den//div,*(n//div for n in nums))


def finite_point(v,p):
    scale=pow(next(n for n in v if n%p),-1,p)
    return tuple(n*scale%p for n in v)


def line_over_D(x,y):
    return global_point([sub(mul(x[(i+1)%3],y[(i+2)%3]),mul(x[(i+2)%3],y[(i+1)%3]))
                         for i in range(3)])


def line_mod_p(x,y,p):
    return finite_point([x[(i+1)%3]*y[(i+2)%3]-x[(i+2)%3]*y[(i+1)%3]
                         for i in range(3)],p)


def three_basis():
    cols=[(ONE,ZERO,ZERO)]
    for _ in range(5):
        a,b,c=cols[-1]
        cols.append((c,add(a,mul((1,1),c)),add(b,mul(OMEGA,c))))
    return cols


BASIS=three_basis()


def coefficients(v):
    return tuple(tuple(sum(v[j]*BASIS[j][i][s] for j in range(6))
                       for s in range(2)) for i in range(3))


def cyc_mul(x,y):
    z=[0]*7
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            z[(i+j)%7]+=a*b
    return [a-z[6] for a in z[:6]]


def integer_ball(max_q):
    def step(k,left,vec):
        if k==0:
            if any(vec) and next(x for x in vec if x)>0:
                yield tuple(vec)
            return
        for a in range(-isqrt(left),isqrt(left)+1):
            yield from step(k-1,left-a*a,vec+[a])
    return step(6,max_q,[])


def floor_cuberoot(n):
    hi=1
    while hi**3<=n:
        hi*=2
    lo=hi//2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**3<=n:
            lo=mid
        else:
            hi=mid
    return lo


def prime(p):
    return p>1 and all(p%i for i in range(2,isqrt(p)+1))


def fixture(p,g,r):
    assert prime(p) and p%7 in (2,4)
    if g is None:
        assert r==0
        w=next(i for i in range(p) if (i*i+i+2)%p==0)
        g=(1,0)
    else:
        assert norm(g)==p
        w=-g[0]*pow(g[1],-1,p)%p
    assert (w*w+w+2)%p==0
    # Columns multiply by g^r on the *original* six integral coefficients.
    a,b=g
    raw_g=[a,b,b,0,b,0]
    power=[1,0,0,0,0,0]
    for _ in range(r):
        power=cyc_mul(power,raw_g)
    columns=[cyc_mul(power,[int(i==j) for j in range(6)]) for i in range(6)]
    # Q(v) <= 7 Q((g/sqrt(p))^r v); all inequalities are strict at the cutoff.
    cap=floor_cuberoot((7**3*p-1)//42**3) if r else floor_cuberoot((p-1)//42**3)
    right=p**(3*r+1)
    directions={}
    primitive=set()
    raw_count=raw_primitive=0
    for v in integer_ball(cap):
        x=[sum(v[i]*columns[i][j] for i in range(6)) for j in range(6)]
        if (42*sum(z*z for z in x))**3>=right:
            continue
        raw_count+=1
        q=coefficients(v)
        key=global_point(q)
        fkey=finite_point([a+w*b for a,b in q],p)
        if key in directions:
            assert fkey==directions[key][1]
        directions[key]=(q,fkey)
        if gcd(*x)==1:
            primitive.add(key)
            raw_primitive+=1
    assert primitive==set(directions)
    atoms=list(directions.values())
    assert len({x[1] for x in atoms})==len(atoms)
    planes={}; reduce_plane={}
    for (i,(x,mx)),(j,(y,my)) in combinations(enumerate(atoms),2):
        h=line_over_D(x,y)
        mh=line_mod_p(mx,my,p)
        if h in reduce_plane:
            assert reduce_plane[h]==mh
        reduce_plane[h]=mh
        planes.setdefault(mh,set()).update((i,j))
    assert len(planes)==len(reduce_plane)
    counts=Counter(map(len,planes.values()))
    L=len(atoms)
    counts[1]=L*(p+1)-sum(k*v for k,v in counts.items())
    counts[0]=p*p+p+1-sum(counts.values())
    assert sum(k*(k-1)*v for k,v in counts.items())==L*(L-1)
    assert sum(k*v for k,v in counts.items())==L*(p+1)
    bad=p*p+p+1-counts[0]
    assert bad==L*(p+1)-sum((k-1)*v for k,v in counts.items() if k>=2)
    if p<=13:
        # Canonical representatives for all dual projective points.
        dual=[(1,a,b) for a in range(p) for b in range(p)]+[(0,1,a) for a in range(p)]+[(0,0,1)]
        direct=Counter(sum(sum(a*b for a,b in zip(t,v))%p==0 for _,v in atoms) for t in dual)
        assert all(counts[k]==direct[k] for k in set(counts)|set(direct))
    counts=+counts
    pairs={k:k*(k-1)*v for k,v in counts.items() if k>=2}
    assert sum(pairs.values())==L*(L-1)
    return dict(p=p,omega_mod_P=w,g=(g if r else None),r=r,exhaustive_Qv_cap=cap,
                raw_antipodal=raw_count,raw_primitive_antipodal=raw_primitive,
                directions=L,bad_seeds=bad,Z_histogram=dict(sorted(counts.items())),
                ordered_direction_pairs_by_plane_size=dict(sorted(pairs.items())))


# Intervals below use only integer or rational arithmetic.
def atan_inverse(d):
    s=Fraction()
    for j in range(24):
        s+=Fraction((-1)**j,d**(2*j+1)*(2*j+1))
    return s,s+Fraction(1,d**49*49)


def real_bounds():
    scale=10**17
    root=isqrt(7*scale*scale)
    r0,r1=Fraction(root,scale),Fraction(root+1,scale)
    a,b=atan_inverse(5);c,d=atan_inverse(239)
    pi0,pi1=16*a-4*d,16*b-4*c
    N=262144; z=N*N*scale
    sumlo=sumhi=0
    # Integrate the positive part over [0,1]; its numerator changes sign once.
    for j in range(N):
        lo2=j*j*scale; hi2=(j+1)**2*scale
        lo1=root*j*N; hi1=(root+1)*(j+1)*N
        p0=max(0,5*z+6*lo1-23*hi2); p1=max(0,5*z+6*hi1-23*lo2)
        q0=7*z+2*lo1-7*hi2; q1=7*z+2*hi1-7*lo2
        u0=7*z-6*hi1+25*lo2; u1=7*z-6*lo1+25*hi2
        assert q0>0 and u0>0
        den0=9*q0*q0*u0*(7*z+lo2); den1=9*q1*q1*u1*(7*z+hi2)
        sumlo+=scale*z*p0**3//den1
        sumhi+=-(-scale*z*p1**3//den0)
    int0,int1=Fraction(sumlo,N*scale),Fraction(sumhi,N*scale)
    ratio0=1+2*r0*int0/pi1
    ratio1=1+2*r1*int1/pi0
    M=10000
    power_sum=sum(scale//j**3 for j in range(1,M+1))
    z30=Fraction(power_sum,scale)+Fraction(1,2*(M+1)**2)
    z31=Fraction(power_sum+M,scale)+Fraction(1,2*M*M)
    cmb0=343*r0/(384*z31);cmb1=343*r1/(384*z30)
    c10,c11=cmb0*ratio0,cmb1*ratio1
    # Elementary Jensen certificate for the unit-index term of C2.
    T=10000
    freq=Counter()
    for y in range(-isqrt(4*T//7),isqrt(4*T//7)+1):
        for x in range(-2*isqrt(T),2*isqrt(T)+1):
            n=norm((x,y))
            if n<=T:
                freq[n]+=1
    count=1; value=0
    for n in range(1,T+1):
        new=count+freq[n]
        value+=-(-scale*(new*new-count*count)//(2*n**3))
        count=new
    Mupper=Fraction(value,scale)+Fraction(96,T)
    disc3lower=z30*32*pi0**3/(343*r1)
    # zeta_D(2)=zeta(2)L(2,chi_-7); bound the character tail absolutely.
    chi=(0,1,1,-1,1,-1,-1)
    l_upper=Fraction(sum(-(-scale*chi[i%7]//(i*i)) for i in range(1,M+1)),scale)+Fraction(1,M)
    disc2upper=pi1*pi1*l_upper/6
    c20=c10*c10*disc3lower**2/(disc2upper*Mupper)
    # If the acute absolute angle of two points of B has cosine >=1/2,
    # one of x+y,x-y lies in B, producing a third direction.
    sqrt3hi=Fraction(isqrt(3*scale*scale)+1,scale)
    angle0=Fraction(2,3)-3*sqrt3hi/(4*pi0)
    c21=c11*c11/2-cmb0*cmb0*angle0/6
    l0,l1=c10/42**3,c11/42**3
    d0,d1=l0-c21/42**6,l1-c20/42**6
    def enclose(lower,upper,places):
        z=10**places
        L=lower*z; H=upper*z
        def fmt(n):
            return f"{n//z}.{n%z:0{places}d}"
        return [fmt(L.numerator//L.denominator),fmt(-(-H.numerator//H.denominator))]
    return dict(integral_mesh=N,ideal_bound_T=T,zeta3_terms=M,
                volume_ratio=enclose(ratio0,ratio1,9),
                C1=enclose(c10,c11,8),C2=enclose(c20,c21,6),
                lambda_at_original_kappa=enclose(l0,l1,14),
                bad_limit_at_original_kappa=enclose(d0,d1,14),
                extra_loglog_exponent=enclose(d0/(3*(1-d0)),d1/(3*(1-d1)),14))


def main():
    cases=[fixture(p,None,0) for p in (2,11,74099,592727,2000387)]
    g=(901,450);p=norm(g)
    for r in (0,1,2,7):
        x=fixture(p,g,r)
        other=fixture(p,conjugate(g),r)
        assert x['Z_histogram']==other['Z_histogram']
        cases.append(x)
        cases.append(other)
    out=dict(finite_cases=cases,certified_real_intervals=real_bounds(),
             scope='j=1 only; preconditioning; Z counts distinct D directions per seed')
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
