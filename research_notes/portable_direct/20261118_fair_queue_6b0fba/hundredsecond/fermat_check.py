"""Replay additions and individual squarings for the indicated pairs of residues."""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm, prod
from pathlib import Path
from runpy import run_path
import json


def factors(n):
    result={}
    p=2
    while p*p<=n:
        while n%p==0:
            result[p]=result.get(p,0)+1
            n//=p
        p=3 if p==2 else p+2
    if n>1:
        result[n]=1
    return result


def output(value, modulus, depth, shifts):
    ans=[]
    for h in shifts:
        v=(value+h)%modulus
        for _ in range(depth):
            v=v*v%modulus
        ans.append(v)
    return tuple(ans)


def collide(modulus, depth, shifts, x=Fraction(3), y=Fraction(-3,2)):
    def residue(z):
        return z.numerator*pow(z.denominator,-1,modulus)%modulus
    u,v=map(residue,(x,y))
    return u!=v and output(u,modulus,depth,shifts)==output(v,modulus,depth,shifts)


def divisors(n):
    data=[1]
    for p,e in factors(n).items():
        data=[d*p**i for d in data for i in range(e+1)]
    return data


def exact_layers():
    report=[]
    shifts=(0,1,3,6)
    earlier=Path(__file__).resolve().parents[1]/'ninetyfourth'/'translates_check.py'
    direct_pairs=run_path(str(earlier))['direct_pairs']
    for r in range(1,12):
        n=2**r
        diffs=[(6+2*h)**n-(2*h-3)**n for h in shifts]
        base=3*(2**n-1)
        assert gcd(*diffs[:2])==gcd(*diffs[:3])==gcd(*diffs)==base
        assert gcd(base,10**n-1)==3*gcd(2**n-1,5**n-1)
        for m in range(3,2002,2):
            wanted=base%m==0 and 9%m!=0
            for labels in (shifts[:2],shifts[:3],shifts):
                assert collide(m,r,labels)==wanted
        if r<=6:
            valid=[m for m in divisors(base) if 9%m]
            assert all(collide(m,r,shifts) for m in valid)
            expected=3*(prod(len(divisors(2**(2**j)+1)) for j in range(1,r))-1)
            assert len(valid)==expected
            report.append([r, len(valid)])
    prior=[(5,2),(17,3),(257,4),(641,6)]
    for p,r in prior:
        assert direct_pairs(p,2**r,shifts[:3])>=2
        assert collide(p,r,shifts) and not collide(p,r-1,shifts)
    return dict(moduli_per_depth=1000,depths=11,menus_checked=3,
                word_count_and_divisor_counts=report,prior_full_readout=prior)


def fermat_layers():
    rows=[]
    for j in range(1,6):
        f=2**(2**j)+1
        fs=factors(f)
        row=[]
        for p,e in fs.items():
            assert p%(2**(j+1))==1
            for k in range(1,e+2):
                for r in range(1,j+4):
                    assert collide(p**k,r,(0,1,3,6))==(k<=e and r>=j+1)
            v=pow(10,2**(j+1),p)
            row.append([p,e,v])
        if j>=2: assert any(v!=1 and e%2 for _,e,v in row)
        rows.append([j,f,row])
    return rows


def signed_power_two(z):
    if not z: return False
    n=abs(z.numerator);d=z.denominator
    return n&(n-1)==0 and d&(d-1)==0


def conic_examples():
    report=[]
    for u in map(Fraction,(-2,2,-3,Fraction(3,2),Fraction(-3,2),Fraction(5,3))):
        beta=[1/(u**e-1) for e in (1,2,3)]
        lam=(beta[2]-beta[0])/(beta[1]-beta[0])
        assert lam==(u+1)**2/(u*u+u+1)
        assert lam*(4-3*lam)==((u*u-1)/(u*u+u+1))**2
        # Clear all denominators and translate the first shift to zero.
        d=lcm(*(b.denominator for b in beta))
        y=d*beta[0];x=y+d
        shifts=tuple(int(d*b-y) for b in beta)
        assert all(Fraction(x+h,y+h)==u**e for e,h in enumerate(shifts,1))
        seen=Counter()
        for j in range(1,5):
            n=2**j
            for p in factors(abs(u.numerator)**n+u.denominator**n):
                if p==2 or d%p==0 or any((y+h)%p==0 for h in shifts):continue
                assert collide(p,j+1,shifts,x,y)
                seen[j]+=1
        report.append(dict(base=str(u),ratio=str(lam),shifts=shifts,verified=sum(seen.values())))
    return report


def all_fifth_shifts():
    original = (0, 1, 3, 6)
    examples = {}
    tests = 0
    for h in range(-9, 12):
        ratio = Fraction(2*h + 6, 2*h - 3)
        rows = []
        for j in range(1, 9):
            depth = j + 1
            n = 2**depth
            f = 2**(2**j) + 1
            # Compute original labelled reads independently of the reduced ratio.
            u = 3
            v = -3*pow(2, -1, f) % f
            delta = output(u, f, depth, (h,))[0] - output(v, f, depth, (h,))[0]
            kept = gcd(f, delta)
            assert kept == gcd(f, pow(ratio.numerator, n, f) - pow(ratio.denominator, n, f))
            if h in original:
                assert kept == f
            if h == -3:
                assert kept == 1
            if j <= 5:
                for modulus in divisors(f):
                    if modulus > 1:
                        assert collide(modulus, depth, (*original, h)) == (kept % modulus == 0)
                        tests += 1
            rows.append(kept)
        if h in (-5, -3, 2, 4, 5, 8):
            examples[str(h)] = rows
    return {"j_range": [1, 8], "shift_range": [-9, 11],
            "original_read_vs_primitive_gcd": 21*8, "exact_divisor_checks": tests,
            "largest_retained_factors_by_shift": examples}


if __name__=='__main__':
    completion=[h for h in range(-5000,5001) if signed_power_two(Fraction(2*h+6,2*h-3))]
    assert completion==[0,1,3,6]
    print(json.dumps(dict(exact_layers=exact_layers(),fermat_numbers=fermat_layers(),
                          integer_shift_sample=completion,conic=conic_examples(),
                          fixed_pair_fifth_shift=all_fifth_shifts()),
                     sort_keys=True,indent=2))
