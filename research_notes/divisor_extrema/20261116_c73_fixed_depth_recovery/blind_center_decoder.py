"""Decode rational dyadic centers solely from H readings and the public inventory.

Test-word generation and expected-center checking use the hidden schedule. blind()
and recover() receive only the measurements, a public height bound and its public
precision. The flag --full additionally tests a nine-gap, eight-block stock.
"""
from fractions import Fraction as Q
from math import prod, gcd
import argparse
import hashlib
import json

def rising(n,k):
    return prod(range(n,n+k))

def odds_at_tail(w):
    y = Q(prod(4*i+1 for i in range(3,w+1)),4**(w-2)*rising(4,w-2))
    x = Q(840,(w+2)*(w+3)*(w+4))
    return [y*(x*a+b)/(1+x*y*a) for a,b in
            [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]

def endpoint_odds(gaps):
    """Compute all three exact endpoint odds by the original (rho,tau) blocks."""
    r=len(gaps)-1
    n=sum(gaps)+2
    edges=[]
    for i,m in enumerate(gaps[:-1]):
        k=2*(r-i)+1
        v=n-m
        odd=prod(k+4*j for j in range(v,n+1))
        rho=Q(odd,4**m*rising(v+k,m+1))
        tau=Q(28*(k-1+4*v)*odd,
              4**m*(k-1+v)*rising(v+4*k,m+1))
        edges.append((rho,tau)); n=v
    z=odds_at_tail(n)
    for rho,tau in reversed(edges):
        z=[(rho+tau*x)/(1+tau*x) for x in z]
    return z

def simulate(gaps):
    z = endpoint_odds(gaps)
    lo,hi=min(z),max(z)
    return hi/lo,(1+hi)/(1+lo)

def public_height(r,c):
    """Uniform upper bound on both raw integer columns at this public stock."""
    height=1680+10*(c+2)*(c+3)*(c+4)
    for remaining in range(1,r+1):
        k=2*remaining+1
        top=(c+k-1)*rising(c+k+1,3*k)
        bottom=28*(4*c+k-1)*rising(c+k,3*k)
        height*=top+bottom
    return height

def truth(gaps):
    r=len(gaps)-1
    n=sum(gaps)+2
    edges=[]
    for i,m in enumerate(gaps[:-1]):
        k=2*(r-i)+1; v=n-m
        edges.append(((v+k-1)*rising(n+k+1,3*k),
                      28*(4*v+k-1)*rising(v+k,3*k)))
        n=v
    W=(n+2)*(n+3)*(n+4)
    result=[]
    for marker in (1,10):
        a,b=1680,1680+marker*W
        for top,bottom in reversed(edges):
            a,b=bottom*b,bottom*b+top*a
        result.append(Q(a,b))
    return sorted(result)

def recover(observed,bound):
    """Reconstruct a small rational from the public dyadic window."""
    assert observed>0
    den=observed.denominator
    shift=(den & -den).bit_length()-1
    bits=(2*bound*bound).bit_length()
    modulus=1<<bits
    odd_denominator=den>>shift
    residue=observed.numerator*pow(odd_denominator,-1,modulus)%modulus
    hi,lo=modulus,residue
    hi_coeff,lo_coeff=0,1
    while lo>bound:
        quotient,rem=divmod(hi,lo)
        hi,lo=lo,rem
        hi_coeff,lo_coeff=lo_coeff,hi_coeff-quotient*lo_coeff
    if not (lo and 0<abs(lo_coeff)<=bound and lo_coeff%2 and gcd(lo,lo_coeff)==1):
        raise ValueError('observations outside public reconstruction window')
    if (lo-residue*lo_coeff)%modulus: raise ValueError('noncongruent fraction')
    result=Q(lo,lo_coeff*(1<<shift))
    if not (0<result and max(result.numerator,result.denominator)<=bound):
        raise ValueError('outside normalized rational height')
    return result,bits

def blind(r,c,g,h=None):
    B=public_height(r,c)
    if h is None:
        ratio,bits=recover(g,B*B)
        return max(ratio,1/ratio),bits
    z_low=(h-1)/(g-h)
    z_high=g*z_low
    center1,bits=recover(1/z_low,B)
    center2,_=recover(1/z_high,B)
    return sorted((center1,center2)),bits

def fingerprint(x):
    num=x.numerator.to_bytes((x.numerator.bit_length()+7)//8,'big')
    den=x.denominator.to_bytes((x.denominator.bit_length()+7)//8,'big')
    return hashlib.sha256(len(num).to_bytes(4,'big')+num+den).hexdigest()

def test(r,lowest):
    gaps=[lowest+(37*i+7*i*i)%(max(10,lowest//6)) for i in range(r+1)]
    c=sum(gaps)+2
    expected=truth(gaps)
    g,h=simulate(gaps)
    got,bits=blind(r,c,g,h)
    ratio,single_bits=blind(r,c,g)
    assert got==expected and ratio==expected[1]/expected[0]
    return dict(r=r,c=c,gaps=gaps,two_center_bits=bits,one_ratio_bits=single_bits,
                center_sha256=[fingerprint(x) for x in got],
                ratio_sha256=fingerprint(ratio),endpoint_pair_distinct=got[0]!=got[1])

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true')
    args=parser.parse_args()
    jobs=[(1,500),(2,1250),(3,2500)]
    if args.full:jobs.append((8,9000))
    print(json.dumps([test(*values) for values in jobs],indent=2))
