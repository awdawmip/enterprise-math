"""Original V14/V17 carry variables, independently evaluated at finite integers."""
import argparse
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from fractions import Fraction
from math import comb, fsum, isqrt, log, sqrt
from pathlib import Path

GAMMA = 2*log(2)-1


def k2_interval():
    # A = sum_{j>=0} (-1)^j sqrt(2/(j+3)). Bound its Euler transform.
    size = 80
    scale = 10**46
    approx = [isqrt((2*scale*scale)//(j+3)) for j in range(size)]
    lo = hi = Fraction(0)
    for i in range(size):
        total = sum((-1)**j*comb(i,j)*approx[j] for j in range(i+1))
        pos = sum(comb(i,j) for j in range(0,i+1,2))
        unit = scale*(1 << (i+1))
        lo += Fraction(total-((1 << i)-pos),unit)
        hi += Fraction(total+pos,unit)
    two_log = 4*sum(Fraction(1,(2*k+1)*3**(2*k+1)) for k in range(64))
    log_rem = Fraction(36,8*129*3**129)
    return lo-(two_log+log_rem-1), hi+Fraction(1,2**size)-(two_log-1)


def xi_at_endpoints():
    """Bounds for two real Xi values via the theta integral and Simpson."""
    floor=Context(prec=40,rounding=ROUND_FLOOR)
    ceil=Context(prec=40,rounding=ROUND_CEILING)
    def exp_down(x):
        return floor.next_minus(floor.exp(x))
    def exp_up(x):
        return ceil.next_plus(ceil.exp(x))
    def cos_bounds(x):
        # Alternating Taylor polynomial; tail is smaller than 15**106 / 106!.
        x2=floor.multiply(x,x)
        assert x2 == ceil.multiply(x,x)
        lo=hi=term_lo=term_hi=Decimal(1)
        for k in range(1,53):
            den=Decimal((2*k-1)*(2*k))
            term_lo=floor.divide(floor.multiply(term_lo,x2),den)
            term_hi=ceil.divide(ceil.multiply(term_hi,x2),den)
            if k%2:
                lo,hi=floor.subtract(lo,term_hi),ceil.subtract(hi,term_lo)
            else:
                lo,hi=floor.add(lo,term_lo),ceil.add(hi,term_hi)
        return floor.subtract(lo,Decimal('1e-44')),ceil.add(hi,Decimal('1e-44'))
    def atan_inv(q):
        total=Fraction()
        for j in range(36):
            total+=Fraction((-1)**j,(2*j+1)*q**(2*j+1))
        return total,total+Fraction(1,73*q**73)
    a0,a1=atan_inv(5); b0,b1=atan_inv(239)
    pir0=16*a0-4*b1; pir1=16*a1-4*b0
    pi_lo=floor.divide(Decimal(pir0.numerator),Decimal(pir0.denominator))
    pi_hi=ceil.divide(Decimal(pir1.numerator),Decimal(pir1.denominator))
    totals={t:[Decimal(0),Decimal(0)] for t in (Decimal('14.13'),Decimal('14.14'))}
    for i in range(4097):
        u=Decimal(i)/2048
        e0,e1=exp_down(u),exp_up(u)
        v0,v1=floor.multiply(e0,pi_lo),ceil.multiply(e1,pi_hi)
        f0=floor.add(exp_down(v1.copy_negate()),exp_down(floor.multiply(Decimal(-4),v1)))
        f1=ceil.add(exp_up(v0.copy_negate()),exp_up(ceil.multiply(Decimal(-4),v0)))
        f0=floor.multiply(f0,exp_down(u/4))
        f1=ceil.multiply(f1,exp_up(u/4))
        weight=Decimal(1 if i in (0,4096) else (4 if i%2 else 2))
        for t, sums in totals.items():
            c0,c1=cos_bounds(t*u/2)
            q0=floor.multiply(f0 if c0>=0 else f1,c0)
            q1=ceil.multiply(f1 if c1>=0 else f0,c1)
            sums[0]=floor.add(sums[0],floor.multiply(q0,weight))
            sums[1]=ceil.add(sums[1],ceil.multiply(q1,weight))
    out={}
    for t,(lo,hi) in totals.items():
        factor=t*t+Decimal('0.25')
        y0=floor.subtract(Decimal('0.5'),ceil.divide(ceil.multiply(factor,hi),Decimal(6144)))
        y1=ceil.subtract(Decimal('0.5'),floor.divide(floor.multiply(factor,lo),Decimal(6144)))
        # Combined truncation and Simpson remainder, proved in the text.
        y0=floor.subtract(y0,Decimal('1e-7'))
        y1=ceil.add(y1,Decimal('1e-7'))
        assert (y0>0 if t<Decimal('14.14') else y1<0)
        scale=Decimal(10**12)
        out[str(t)]=[int(floor.multiply(y0,scale).to_integral_value(rounding=ROUND_FLOOR)),
                     int(ceil.multiply(y1,scale).to_integral_value(rounding=ROUND_CEILING))]
    return {'Xi_enclosures_denominator':10**12,'endpoint_numerators':out,
            'panels':4096,'included_theta_terms':2,'u_interval':[0,2]}


def first_ordinate_certificate(k_upper):
    # Published zero ordinate in (14.13,14.14); audit all further comparisons.
    t0,t1 = Fraction(1413,100),Fraction(1414,100)
    l0,l1 = Fraction(6931,10000),Fraction(6932,10000)
    pi0,pi1 = Fraction(31415,10000),Fraction(31416,10000)
    delta=max(abs(t0*l0-3*pi1),abs(t1*l1-3*pi0))
    cos_bound=1-delta**2/2
    assert cos_bound > Fraction(92,100)
    a=Fraction(3,5)
    d_sq=(2+a*a+2*Fraction(1414,1000)*a*Fraction(92,100))*(2+2*Fraction(92,100))/(t1*t1*(t1*t1+Fraction(1,4)))
    lower=Fraction(193,10000)
    assert d_sq>lower**2 and lower>Fraction(191,10000)>k_upper*l1/2
    return {'ordinate_input':'14.13 < gamma < 14.14, by the two Xi sign enclosures',
            'absolute_fourier_coefficient_strict_lower':'0.0193',
            'certified_upper_K2_log2_over_2':'0.0191'}


def primes_to(n):
    sieve = bytearray([1])*(n+1)
    sieve[:2] = b'\0\0'
    for k in range(2,isqrt(n)+1):
        if sieve[k]:
            sieve[k*k::k] = bytes((n-k*k)//k+1)
    return [p for p in range(2,n+1) if sieve[p]]


def root_fifth(x):
    lo, hi = 0, 1
    while hi**5 <= x:
        hi *= 2
    while hi-lo>1:
        b=(lo+hi)//2
        if b**5<=x:
            lo=b
        else:
            hi=b
    return lo


def carry_by_residue(n,q):
    return int(2*(n % q)>=q)


def exact_tests():
    ps = primes_to(400)
    pairs = 0
    for n in range(2,193):
        A = sum(carry_by_residue(n,j) for j in range(1,n+1))
        divisors = sum(2*(n//j) for j in range(1,n+1))
        assert A == sum(2*n//j for j in range(1,2*n+1)) - divisors - n
        alpha = Fraction(A,n)
        for y in {2,root_fifth(n**3),n}:
            for p in ps:
                if p>n:
                    break
                powers = []
                q=p
                while q<=n:
                    powers.append(q)
                    q*=p
                cs = [carry_by_residue(n,q) for q in powers]
                count = len(powers)
                # Each component is constant term plus GAMMA times its second entry.
                H = (cs[0],-1) if p>y else (0,0)
                B = (Fraction(p//2,p),-1) if p<=y else (0,0)
                L = (cs[0]-Fraction(p//2,p),0) if p<=y else (0,0)
                A2 = (sum(cs[1:]),1-count)
                D = (-alpha*count,count)
                pieces = (H,B,L,A2,D)
                assert sum(v[0] for v in pieces) == sum(cs)-alpha*count
                assert sum(v[1] for v in pieces) == 0
                # A second acquisition uses valuations of actual integers.
                b = comb(2*n,n)
                nu=0
                while b%p==0:
                    nu+=1
                    b//=p
                assert sum(cs) == nu - int(n < q <= 2*n)
                pairs += 1
    return pairs


def block(N,K):
    size=2*N
    y=root_fifth(N**3)
    ps=primes_to(2*size)
    lam=[0.0]*(2*size+1)
    div=[0]*(2*size+1)
    for d in range(1,2*size+1):
        for m in range(d,2*size+1,d):
            div[m]+=1
    for i in range(1,len(div)):
        div[i]+=div[i-1]
    # A prime p contributes at n=p and at the phase changes k*p, k*p+ceil(p/2).
    diff=[0.0]*(size+1)
    B=0.0
    for p in ps:
        lp=log(p)
        q=p
        while q<=2*size:
            lam[q]=lp
            q*=p
        if p<=y:
            B += (p//2/p-GAMMA)*lp
        elif p<size:
            diff[p] -= GAMMA*lp
            for start in range(p,size,p):
                switch=start+(p+1)//2
                if switch < size:
                    diff[switch]+=lp
                if start+p<size:
                    diff[start+p]-=lp
    for i in range(1,len(lam)):
        lam[i]+=lam[i-1]
    H=0.0
    binlog=0.0
    Jvals=[]; single=[]; double=[]; cross=[]
    max_window=0.0
    for n in range(1,size):
        H+=diff[n]
        binlog+=log(4-2/n)
        if n<N:
            continue
        a=(div[2*n]-2*div[n]-n)/n
        J=binlog-lam[2*n]+(1-a)*lam[n]
        residual=J-H-B
        Jvals.append((J/n)**2)
        single.append((residual/n)**2)
        double.append(((residual-K*sqrt(n))/n)**2)
        cross.append(J/n**1.5)
        if n in (N,(3*N)//2,size-1):
            direct=fsum((carry_by_residue(n,p)-GAMMA)*log(p) for p in ps if y<p<=n)
            max_window=max(max_window,abs(H-direct))
    assert max_window < 2e-7
    return {'N':N, 'y_exact':y,
            'J_norm2':round(fsum(Jvals),12),
            'one_correction_error_norm2':round(fsum(single),12),
            'two_corrections_error_norm2':round(fsum(double),12),
            'cross_sum_J_over_n_to_3_over_2':round(fsum(cross),12),
            'three_native_formula_reads_max_abs_float_error':round(max_window,10)}


def fitted_prefixes():
    ps=primes_to(4096)
    H=first=raw=0.0
    rows=[]
    for n in range(1,4097):
        block_start=1<<(n.bit_length()-1)
        y=root_fifth(block_start**3)
        # The two appearances of gamma recombine for ordinary primes.
        val=fsum(((p//2/p if p<=y else carry_by_residue(n,p))-GAMMA)*log(p)
                 for p in ps if p<=n)
        scaled=val/sqrt(n)
        H+=1/n
        first+=scaled/n
        raw+=scaled**2/n
        if n in (63,128,555,1024,2047,4096):
            b=-first/H
            best=raw-first**2/H
            for step in (-0.25,0.5):
                trial=raw+2*(b+step)*first+(b+step)**2*H
                assert abs(trial-(best+step**2*H))<1e-10
            rows.append({'X':n,'b_hat_approx':round(b,12),
                         'minimum_sum_of_squares_approx':round(best,12)})
    return rows


def run():
    lo,hi=k2_interval()
    d=10**20
    lower=lo.numerator*d//lo.denominator
    upper=-((-hi.numerator*d)//hi.denominator)
    K=float((lo+hi)/2)
    return {'formal_weight_tests_n2_to_192':exact_tests(),
            'K2_certified':{'lower_numerator':lower,'upper_numerator':upper,'denominator':d},
            'K2_squared_log2_approx':round(K*K*log(2),15),
            'oscillation_certificate':first_ordinate_certificate(hi),
            'xi_signs':xi_at_endpoints(),
            'window':'all n on each [N,2N), y=floor(N^(3/5)), log entries floating point',
            'blocks':[block(2**k,K) for k in range(8,17,2)],
            'fitted_all_integer_prefixes':fitted_prefixes()}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    content=json.dumps(run(),indent=2,ensure_ascii=False)+'\n'
    if args.out:
        args.out.write_text(content,encoding='utf-8')
    else:
        print(content,end='')
