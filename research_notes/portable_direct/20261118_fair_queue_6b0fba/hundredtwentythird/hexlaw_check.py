"""Integer certificates for the four original hexagonal ports and the scale decoder."""
import argparse
import json
import math
import runpy
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path


W103_SHA = "d5cb3dbbaa32935da8e0a5e805ad9f1434e5ef25f40bd88865ed6a6cdddfad10"
NATIVE_BLOB = "026b13094e8cf8d5656d45cd7b69e0d1ff9cf895"
CUTS = (Q(683,1000), Q(710,1000), Q(734,1000))


def primes_to(n):
    keep = bytearray(b'\1')*(n+1)
    keep[:2] = b'\0\0'
    for p in range(2, math.isqrt(n)+1):
        if keep[p]:
            keep[p*p:n+1:p] = bytes((n-p*p)//p+1)
    return [p for p in range(2, n+1) if keep[p]]


def factors(n):
    fs = []
    q = 2
    while q*q <= n:
        if n % q == 0:
            fs.append(q)
            while n % q == 0:
                n //= q
        q = 3 if q == 2 else q+2
    if n>1:
        fs.append(n)
    return fs


def order(p):
    d = p-1
    for q in factors(d):
        while d % q == 0 and pow(4, d//q, p) == 1:
            d //= q
    return d


def rho(p):
    return Q(p*(p-2),(p-1)**2)


def decode_ratio(z):
    found = []
    while z != 1:
        p = max(factors(z.numerator))
        assert p>=3 and p not in found
        found.append(p)
        z /= rho(p)
    return math.lcm(*(order(p) for p in found)), sorted(found)


def band(x):
    for i,cut in enumerate(CUTS):
        if x < cut:
            return (6,2,3)[i]
    return 1


def conditional_certificate(y):
    primes = primes_to(y)[1:]
    orders = [(p,order(p)) for p in primes]
    brackets = {}
    for g,low,high in [(6,659,680),(2,687,704),(3,714,730),(1,738,751)]:
        lo = Q(y-1,y)*math.prod(rho(p) for p,d in orders if g % math.gcd(d,6)==0)
        hi = math.prod(rho(p) for p,d in orders if g%d == 0)
        assert Q(low,1000)<lo<=hi<Q(high,1000)
        assert band(lo-Q(2,1000))==band(hi+Q(2,1000))==g
        text = str(lo)
        brackets[g] = {'outward_thousandths':[low,high], 'upper_exact':str(hi),
                       'lower_fraction_sha256':sha256(text.encode()).hexdigest(),
                       'lower_floor_millionths':int(lo*1000000)}
    return brackets


def original_ratio(hist):
    n = sum(hist.values())
    left = sum(v for k,v in hist.items() if k[1]=='1')
    right = sum(v for k,v in hist.items() if k[2]=='1')
    joint = sum(v for k,v in hist.items() if k[1:]=='11')
    return Q(joint*n,left*right)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--native', type=Path, help='frozen nollm_strict_hex_expansion_20260916/verify.py')
    args=parser.parse_args()
    old = Path(__file__).resolve().parents[1]/'hundredthird'/'hxpi_check.py'
    assert sha256(old.read_bytes()).hexdigest()==W103_SHA
    helper=runpy.run_path(str(old))
    source=None
    if args.native:
        from hashlib import sha1
        b=args.native.read_bytes()
        assert sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==NATIVE_BLOB
        source=runpy.run_path(str(args.native))
    # 7^omega(s) <= C sqrt(s), using every odd prime < 49 only once.
    primes=primes_to(48)[1:]
    c2=Q(7**(2*len(primes)),math.prod(primes))
    assert c2 < 1224**2
    assert (48*1224*1000)**2 < 4**26-1
    brackets=conditional_certificate(3000)
    records=[]
    geometric=[]
    failed=[]
    for t in range(1,37):
        data=helper['arithmetic_table'](t)
        z=original_ratio(data['histogram'])
        if t<=8:
            direct=helper['direct'](t,source)
            assert direct['histogram']==data['histogram']
            geometric.append([t,direct['old_ids'],direct['named_gcd_rows_sha256']])
        if band(z)!=math.gcd(t,6):
            failed.append(t)
        if t>=5:
            assert band(z-Q(1,1000))==band(z+Q(1,1000))==math.gcd(t,6)
        model=Q(data['correlation_model'])
        recovered=None
        if t%3==0:
            assert z==model
            recovered,support=decode_ratio(z)
            assert recovered==t and support==data['primes']
        records.append({'t':t,'observed':str(z),'model':str(model),'class':band(z),
                        'exact_inverse_on_full_periods':recovered})
    assert failed==[2,4]
    print(json.dumps({'order_product_cut':3000,'conditional_brackets':brackets,
               'finite_scale_ratios':records,'geometric_ids':geometric,
               'geometric_total':sum(row[1] for row in geometric),
               'small_class_exceptions_without_noise':failed,
               'roundoff_allowance':'1/1000','analytic_threshold_checked_from':26},
               sort_keys=True,indent=2))


if __name__=='__main__':
    main()
