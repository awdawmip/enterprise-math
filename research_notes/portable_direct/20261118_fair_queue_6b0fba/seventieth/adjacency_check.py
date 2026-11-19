"""Ordinary numeric Omega shells, rational obstructions and fixed CRT design."""
import argparse
import hashlib
import json
from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path


def sieve(limit):
    least=list(range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if least[p]!=p:
            continue
        for n in range(p*p,limit+1,p):
            if least[n]==n:
                least[n]=p
    omega=bytearray(limit+1)
    for n in range(2,limit+1):
        omega[n]=omega[n//least[n]]+1
    return least,omega


def divisors(d):
    return [n for n in range(1,d+1) if d%n==0]


def shapes(family, offsets):
    return sorted({Fraction(a,d) for d in family for a in range(d*offsets[0],d*offsets[-1]+1)
                   if Fraction(a,d) not in offsets})


def sha(obj):
    return hashlib.sha256(json.dumps(obj,separators=(',',':')).encode()).hexdigest()


def crt_design(least,omega):
    family,offsets=[1,2,3,6],[0,2,6]
    obstruction=shapes(family,offsets)
    n,M=0,1
    data=[]
    prime=max(family)*(offsets[-1]-offsets[0])+1
    for r in obstruction:
        a,b=r.numerator,r.denominator
        while least[prime]!=prime:
            prime+=1
        exponent=omega[b]+2
        power=prime**exponent
        wanted=-a*pow(b,-1,power)%power
        n+=M*((wanted-n)*pow(M,-1,power)%power)
        M*=power
        data.append([a,b,prime,exponent])
        prime+=1
    for a,b,prime,exponent in data:
        assert (b*n+a)%prime**exponent==0
        assert all((n+h)%prime for h in offsets)
    assert all(gcd(n+h,M)==1 for h in offsets)
    denom=sorted({b for d in family for b in divisors(d)})
    phi=lambda b:sum(gcd(a,b)==1 for a in range(1,b+1))
    expect=(offsets[-1]-offsets[0])*sum(phi(b) for b in denom)+1-len(offsets)
    assert expect==len(data)
    return dict(family=family,offsets=offsets,directional_prime_powers=data,n=n,M=M,
                ray_count=len(data),naive_blockers=sum((d-0)*(offsets[-1]-offsets[0])+1-len(offsets) for d in family))


def consecutive(D,pr,omega):
    level=omega[D]+1
    return all(omega.count(level,D*p+1,D*q)==0 for p,q in zip(pr,pr[1:]))


def obstruction(b,pr,omega):
    for p,q in zip(pr,pr[1:]):
        for c in range(b*p+1,b*q):
            if gcd(b,c)==1 and omega[c]==omega[b]+1:
                return [c,p,q]
    return None


def multiplier_table(pr,cap,omega):
    bad={b for b in range(1,cap+1) if obstruction(b,pr,omega)}
    blocked=bytearray(cap+1)
    minimal=[]
    for d in sorted(bad):
        if blocked[d]:
            continue
        minimal.append(d)
        for k in range(d,cap+1,d):
            blocked[k]=1
    good=[d for d in range(1,cap+1) if not blocked[d]]
    assert good==[d for d in range(1,cap+1) if consecutive(d,pr,omega)]
    return dict(primes=pr,cap=cap,good_count=len(good),good=good,
                minimal_bad_count=len(minimal),minimal_bad_first=minimal[:18],
                minimal_bad_all_sha256=sha(minimal))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    least,omega=sieve(600000)
    def factors(n):
        ans=[]
        while n>1:
            p=least[n];ans.append(p);n//=p
        return ans
    def interval(pr,D):
        a,b=D*pr[0],D*pr[-1]
        selected=[n for n in range(a,b+1) if omega[n]==omega[D]+1]
        assert selected==[D*p for p in pr]
        return dict(multiplier=D,closed_range=[a,b],shell=omega[D]+1,
                    terms=selected,omega_in_order=list(omega[a:b+1]),
                    between_factors=[factors(n) for n in range(a,b+1) if n not in selected])
    runs=[]
    for pr,Ds in [([55813,55817,55819],[1,2,3]),([55807,55813,55817,55819,55823],[1,2])]:
        assert all(least[p]==p for p in pr)
        assert all(gcd(p,q)==1 for p,q in zip(pr,pr[1:]))
        runs.append(dict(primes=pr,shell_intervals=[interval(pr,d) for d in Ds]))
    tables=[multiplier_table(pr,512,omega) for pr in ([2,3],[3,5],[5,7],[11,13],[17,19])]
    assert tables[0]['good']==[d for d in range(1,513) if (d//(d&-d)) in (1,3)]
    assert all(d%2 for d in tables[1]['good'])
    examples=[[r,next(n for n in range(2*r+1,3*r) if omega[n]==2)] for r in (5,7,11,13,17,19,23)]
    audit=dict(finite_sieve_limit=len(omega)-1,simultaneous_runs=runs,
               fixed_multiplier_tables=tables,crt_design=crt_design(least,omega),
               small_prime_obstructions_for_2_3=examples,obstruction_9=[9,20,factors(20)],
               obstruction_2_for_3_5=[2,9,factors(9)])
    doc=json.dumps(audit,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(doc)
    else:
        print(doc,end='')


if __name__=='__main__':
    main()
