"""Integral covolumes and direct open-ball counts in the six frozen cyclotomic coordinates."""
from collections import Counter
from itertools import combinations, product
from math import gcd, isqrt
import json


def root_of_unity(a):
    k = a % 7
    return tuple(int(j==k) if k<6 else -1 for j in range(6))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def scale(a,n):
    return tuple(n*x for x in a)


def multiply(a,b):
    c = [0]*7
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            c[(i+j)%7] += u*v
    return tuple(u-c[6] for u in c[:6])


def conjugate(a):
    b = (0,)*6
    for i,v in enumerate(a):
        b = add(b,scale(root_of_unity(-i),v))
    return b


def automorphism(a,k):
    out=(0,)*6
    for j,v in enumerate(a):
        out=add(out,scale(root_of_unity(k*j),v))
    return out


def norm(a):
    value=root_of_unity(0)
    for k in range(1,7):
        value=multiply(value,automorphism(a,k))
    assert not any(value[1:])
    return value[0]


def columns(z):
    s = add(root_of_unity(1),root_of_unity(-1))
    return [z,multiply(z,s),multiply(multiply(z,s),s)]


def gram(basis):
    return [[sum(x*y for x,y in zip(u,v)) for v in basis] for u in basis]


def determinant(g):
    a,b,c = g[0]
    d,e,f = g[1]
    h,i,j = g[2]
    return a*(e*j-f*i)-b*(d*j-f*h)+c*(d*i-e*h)


def cube_floor(x):
    lo,hi = 0,1
    while hi**3<=x:
        hi *= 2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**3<=x:
            lo=mid
        else:
            hi=mid
    return lo


def point_count(z,p,r):
    basis = columns(z)
    g = gram(basis)
    top = cube_floor((p**(2*r+1)-1)//42**3)
    volume = determinant(g)
    bounds=[]
    for i in range(3):
        j,k = [h for h in range(3) if h!=i]
        minor = g[j][j]*g[k][k]-g[j][k]**2
        bounds.append(isqrt(top*minor//volume))
    total = 0
    for t in product(*(range(-b,b+1) for b in bounds)):
        if gcd(*t)!=1 or next(v for v in t if v)<0:
            continue
        v = [sum(t[i]*basis[i][j] for i in range(3)) for j in range(6)]
        q = sum(a*a for a in v)
        if q<=top:
            assert p**(2*r+1)>42**3*q**3 and gcd(*v)==1
            total+=1
    return total


def main():
    one=root_of_unity(0)
    eta = add(add(root_of_unity(1),root_of_unity(2)),root_of_unity(4))
    assert multiply(eta,conjugate(eta))==scale(one,2)
    assert add(eta,conjugate(eta))==scale(one,-1)
    candidates = [one,add(one,scale(root_of_unity(1),-1)),eta,conjugate(eta)]
    names = ('unit','ramified_7','first_prime_over_2','second_prime_over_2')
    lines = [[multiply(z,root_of_unity(j)) for j in range(7)] for z in candidates]
    for a,b in combinations([z for group in lines for z in group],2):
        assert multiply(a,conjugate(b))!=multiply(conjugate(a),b)
    heights = {name:[determinant(gram(columns(z))) for z in group] for name,group in zip(names,lines)}
    hist = Counter(h for row in heights.values() for h in row if h<=32)
    assert hist=={4:6,8:2,16:2,32:6}
    gen29=(-1,-1,1,0,0,0)
    gen43=(-1,-1,-1,1,0,0)
    assert norm(gen29)==29 and norm(gen43)==43
    pi=candidates[1]
    assert multiply(pi,pi)==multiply(root_of_unity(1),add(add(root_of_unity(1),root_of_unity(-1)),scale(one,-2)))
    groups=dict(zip(names,candidates))
    for v,q in ((gen29,29),(gen43,43)):
        for k in range(1,7):
            groups[f"p{q}_conjugate_{k}"]=automorphism(v,k)
    groups["p7_p2_first"]=multiply(pi,eta)
    groups["p7_p2_second"]=multiply(pi,conjugate(eta))
    all_reps=[multiply(z,root_of_unity(j)) for z in groups.values() for j in range(7)]
    for a,b in combinations(all_reps,2):
        assert multiply(a,conjugate(b))!=multiply(conjugate(a),b)
    all_heights={k:[determinant(gram(columns(multiply(v,root_of_unity(j))))) for j in range(7)]
                 for k,v in groups.items()}
    for name,hs in all_heights.items():
        for j,h in enumerate(hs):
            z=multiply(groups[name],root_of_unity(j))
            nn=norm(z)
            # N*z/bar(z) is integral. Multiply the other five conjugates.
            nz_over_zbar=z
            for k in range(1,6):
                nz_over_zbar=multiply(nz_over_zbar,automorphism(z,k))
            trace=sum(automorphism(multiply(root_of_unity(2),nz_over_zbar),k)[0] for k in range(1,7))
            assert h%4==0 and 7*(h//4)==8*nn+trace
    spectrum=Counter(h for hs in all_heights.values() for h in hs if h<=64)
    assert spectrum=={4:6,8:2,16:2,32:6,36:6,48:6,60:6}
    p_types={}
    for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53):
        f=1 if p==7 else next(j for j in range(1,7) if pow(p,j,7)==1)
        p_types[p]=[f,p**f]
    blocks=[]
    for n,levels in ((43,(0,1,7,16)),(85,(0,1,3)),(129,(0,1,3)),(220,(0,1,3))):
        p=n**3-n*n-2*n+1
        assert p%7==6 and all(p%j for j in range(2,isqrt(p)+1))
        for j in (1,2,3):
            g=add(scale(one,n),add(root_of_unity(j),root_of_unity(-j)))
            gpow=one
            for r in range(max(levels)+1):
                if r in levels:
                    counts=[[point_count(multiply(gpow,z),p,r) for z in group] for group in lines]
                    blocks.append(dict(prime=p,depth=r,conjugate=j,counts=counts))
                gpow=multiply(gpow,g)
    print(json.dumps(dict(heights=heights,above_32_and_norms_through_56=all_heights,spectrum_through_64=spectrum,small_spectrum=hist,prime_norms=p_types,blocks=blocks),
                     sort_keys=True,indent=2))


if __name__=='__main__':
    main()
