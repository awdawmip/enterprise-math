"""Check exact carry inversions and rational wave covariances; run with Python 3.11+."""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial, isqrt
from pathlib import Path
import json
import runpy
import sys


NATIVE_FILE = "brc_count_centered_carry.py"
NATIVE_SHA = "1b849203290b376105c559974c23dca4ff06b2485b6a0e6455983e3d30a3165f"


def carry_bit(n, p):
    return (2*n)//p - 2*(n//p)


def primes_to(n):
    values = bytearray([1]) * (n+1)
    values[:2] = bytes(2)
    for p in range(2, isqrt(n)+1):
        if values[p]:
            values[p*p::p] = bytes(1+(n-p*p)//p)
    return [i for i, value in enumerate(values) if value]


def bernoulli_numbers(limit):
    values = [Q(1)]
    for n in range(1, limit+1):
        values.append(-sum(comb(n+1,k)*values[k] for k in range(n))/(n+1))
    return values


def bernoulli(n, x, numbers):
    return sum(comb(n,k)*numbers[k]*x**(n-k) for k in range(n+1))


def local_wave(j, at, delta, numbers):
    # Coefficients in u of V_j(at+u-delta), up to the next half-period cut.
    n = j+1
    x = (at-delta) % 1
    y = (x+Q(1,2)) % 1
    return [Q(comb(n,i),factorial(n)) *
            (bernoulli(n-i,x,numbers)-bernoulli(n-i,y,numbers)) for i in range(n+1)]


def polynomial_covariance(j, delta, numbers):
    cuts = sorted({Q(0), Q(1,2), Q(1), delta%1, (delta+Q(1,2))%1})
    value = Q(0)
    for left,right in zip(cuts,cuts[1:]):
        a = local_wave(j,left,0,numbers)
        b = local_wave(j,left,delta,numbers)
        value += sum(ai*bk*(right-left)**(i+k+1)/(i+k+1)
                     for i,ai in enumerate(a) for k,bk in enumerate(b))
    return value


def wave_certificates():
    numbers = bernoulli_numbers(18)
    result=[]
    for j in range(1,9):
        n=j+1
        cov={}
        for delta in map(Q,("0","1/7","1/4","1/3","1/2","6/7")):
            direct=polynomial_covariance(j,delta,numbers)
            fourier=Q(2*(-1)**n,factorial(2*n))*(
                bernoulli(2*n,(delta+Q(1,2))%1,numbers)-bernoulli(2*n,delta,numbers))
            assert direct==fourier
            cov[str(delta)]=direct
        assert cov["1/2"]==-cov["0"] and cov["1/7"]==cov["6/7"] and cov["1/4"]==0
        energy=cov["0"]*factorial(j)**2*(1-Q(1,2)**(2*j+1))/(2*j+1)
        result.append(dict(j=j,critical_exponent=str(Q(2*j+1,2*j+2)),energy=str(energy),
                           phase_variance=str(cov["0"]),phase_covariance_at_one_seventh=str(cov["1/7"])))
    assert [r["energy"] for r in result[:3]]==["7/4608","31/307200","2159/128450560"]
    return result


def recover_short_intervals(bit, sieve):
    y,n0=2048,32768
    all_primes=sieve(2*y)
    intervals=0
    cohorts=[0,0]
    reads=[0,0]
    examples=[]
    for x in range(y,2*y,31):
        z=min(2*y,x+y*y//(16*n0))
        primes=[p for p in all_primes if x<p<=z]
        first={}
        for n in range(n0,2*n0):
            phase=8*(n%x)
            if x<=phase<=3*x:
                sign=0
            elif 5*x<=phase<=7*x:
                sign=1
            else:
                continue
            # Monotonicity between the endpoints checks the entire real interval.
            assert (2*n)//z==(2*n)//x and (2*n//z)%2==sign
            cohorts[sign]+=1
            reads[sign]+=len(primes)
            for p in primes:
                assert bit(n,p)==sign
            first.setdefault(sign,n)
        assert set(first)=={0,1}
        # In the formal basis (1, log p), recover every coefficient.
        constant=-(z-x)
        for p in primes:
            center=Q(p//2,p)
            diff=(bit(first[1],p)-center)-(bit(first[0],p)-center)
            assert diff==1
        if len(examples)<4 and primes:
            examples.append(dict(x=x,z=z,cohort_representatives=[first[0],first[1]],
                                 rational_constant=constant,primes_with_log_coefficient_one=primes))
        intervals+=1
    return dict(N=n0,Y=y,intervals=intervals,cohort_sizes=cohorts,integer_prime_carry_reads=reads,examples=examples)


def integer_root(n,k):
    lo,hi=0,1
    while hi**k<=n:
        hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**k<=n:
            lo=mid
        else:
            hi=mid
    return lo


def second_boundary_block(n0,bit,sieve):
    # Floating logs only in this illustration (fixed Decimal precision).
    y=integer_root(n0**5,6)
    primes=sieve(y)
    with localcontext() as ctx:
        ctx.prec=36
        weights={p:Decimal(p).ln() for p in primes}
        jumps=[Decimal(0)]*n0
        def from_floors(n):
            return sum(weights[p]*(bit(n,p)-Decimal(p//2)/p) for p in primes)
        current=from_floors(n0)
        for p in primes:
            for residue,value in ((0,-weights[p]),((p+1)//2,weights[p])):
                first=n0+1+(residue-n0-1)%p
                for n in range(first,2*n0,p):
                    jumps[n-n0]+=value
        observed=pure=error=Decimal(0)
        probes={n0,n0+1,n0+n0//5,n0+n0//2,2*n0-1}
        for idx,jump in enumerate(jumps):
            n=n0+idx
            current+=jump
            if n in probes:
                assert abs(current-from_floors(n))<Decimal("1e-25")
            t=Decimal(n%y)/y
            v1=Decimal(1)/8-min(t,1-t)/2
            s=t if t<Decimal("0.5") else t-Decimal("0.5")
            v2=(s/8-s*s/4)*(1 if t<Decimal("0.5") else -1)
            residual=current+v1*y*y/n
            predicted=-2*v2*y**3/n**2
            observed+=(residual/n)**2
            pure+=(predicted/n)**2
            error+=((residual-predicted)/n)**2
        def rounded(x):
            return str(x.quantize(Decimal("1e-12")))
        return dict(N=n0,y=y,primes=len(primes),direct_address_checks=len(probes)*len(primes),
                    second_residual_energy=rounded(observed),second_wave_energy=rounded(pure),
                    squared_difference_with_second_wave=rounded(error))


def schedule_cutoff(n):
    # Decimal.ln is correctly rounded. Enclose its value by adjacent decimals,
    # then certify each integer floor with exact rational comparisons.
    with localcontext() as ctx:
        ctx.prec=len(str(n))+24
        center=Decimal(n).ln()
        low=Q(center.next_minus())
        high=Q(center.next_plus())
    a=n//(high**7)
    b=n//(low**7)
    assert a==b
    return a


def sparse_schedule_examples():
    rows=[]
    index=10**32+7
    for degree in (1,2,3,4,8):
        n=index**degree
        x=schedule_cutoff(n)
        step=x*x//(128*n)
        lo,hi=0,1
        while schedule_cutoff((index+hi)**degree)-x<=step:
            lo,hi=hi,2*hi
        while hi-lo>1:
            mid=(lo+hi)//2
            if schedule_cutoff((index+mid)**degree)-x<=step:
                lo=mid
            else:
                hi=mid
        end=(index+lo)**degree
        z=schedule_cutoff(end)
        assert step//2<=z-x<=step and end<n*2
        assert schedule_cutoff((index+lo+1)**degree)-x>step
        n_pair=[(end//x+1)*x+x*k//4 for k in (1,3)]
        for sign,position in enumerate(n_pair):
            assert end<=position<2*n
            assert 2*position//x==2*position//z and (2*position//x)%2==sign
        rows.append(dict(degree=degree,greedy_index_step=str(lo),
                         cutoff_digits=len(str(x)),cutoff_step_digits=len(str(z-x))))
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--native-dir",type=Path,help="directory with the pinned count-centered carry source")
    args=parser.parse_args()
    bit,sieve=carry_bit,primes_to
    if args.native_dir:
        path=args.native_dir / NATIVE_FILE
        assert sha256(path.read_bytes()).hexdigest()==NATIVE_SHA
        native=runpy.run_path(str(path))
        bit,sieve=native["carry_bit"],native["primes_up_to"]
        print("Pinned original carry_bit and primes_up_to loaded.",file=sys.stderr)
    results=dict(reference_sha256=NATIVE_SHA,exact_waves=wave_certificates(),
                 sparse_schedule_examples=sparse_schedule_examples(),
                 exact_short_intervals=recover_short_intervals(bit,sieve),
                 second_boundary_decimal=[second_boundary_block(n,bit,sieve) for n in (4096,16384,65536)])
    print(json.dumps(results,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
