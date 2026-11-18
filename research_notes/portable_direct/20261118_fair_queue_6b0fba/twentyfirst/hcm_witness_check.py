"""One Bernstein coefficient by exact rational interpolation of the physical AP cofactor."""
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial, prod
from multiprocessing import Pool
import argparse
import json

from flint import fmpq, fmpz, fmpz_mat, fmpz_poly


@lru_cache(None)
def prepare(m):
    """A fixed positive denominator for each row of the unnormalised Laplacian."""
    n = m-1
    w = [(-1)**i * comb(n,i) for i in range(m)]
    local = []
    for i in range(m):
        row = []
        for j in range(m):
            den = [i+1+m*j+m*m*s for s in range(m)]
            z = fmpz(1)
            for a in den:
                z = z.lcm(a)
            row.append((z,[w[i]*w[j]*w[s]*(z//a) for s,a in enumerate(den)]))
        local.append(row)
    row_den = [fmpz(1) for _ in range(2*m-1)]
    for i in range(m):
        for j,(z,_) in enumerate(local[i]):
            row_den[i] = row_den[i].lcm(z)
            if j<n:
                row_den[m+j] = row_den[m+j].lcm(z)
    scales = [[(row_den[i]//z, row_den[m+j]//z if j<n else 0)
               for j,(z,_) in enumerate(local[i])] for i in range(m)]
    return [[coeff for _,coeff in row] for row in local], scales, prod(row_den)


def q_at(data):
    m,j,d = data
    n = m-1
    if j == 0:
        b = m*m
        q0 = fmpq(n**n * m**(n*(n+3)+m) * prod(comb(n,k)**2 for k in range(m))
                   * factorial(n)**(2*m)*(3*b+1), 2*factorial(2*b))
        return q0
    local,scales,row_den = prepare(m)
    powers = [fmpz(j)**s*d**(n-s) for s in range(m)]
    size = 2*m-1
    lap = [[fmpz(0) for _ in range(size)] for _ in range(size)]
    for i in range(m):
        for k in range(m):
            edge = sum(x*y for x,y in zip(local[i][k],powers))
            left, right = scales[i][k]
            lep = left*edge
            lap[i][i] += lep
            if k < n:
                rep = right*edge
                lap[m+k][m+k] += rep
                lap[i][m+k], lap[m+k][i] = -lep, -rep
    numerator = fmpz_mat(lap).det()
    denominator = row_den * fmpz(d)**(n*(size-1)) * fmpz(j)**n
    return fmpq(numerator,denominator)


def weights(d, k):
    factors = [fmpz_poly([-r,d-r]) for r in range(d+1)]
    product = prod(factors,start=fmpz_poly([1]))
    primary = []
    for j,factor in enumerate(factors):
        quotient,rem = divmod(product,factor)
        assert not rem
        primary.append(fmpq(quotient[k],(-1)**(d-j)*factorial(j)*factorial(d-j)))
    # Exact reproduction on the full polynomial basis t^a:
    # [z^k] (1+z)^d (z/(1+z))^a = binom(d-a,k-a).
    # k is close to the middle; the next independent tests exercise both sides.
    for a in sorted({0,1,k-1,k,k+1,d} & set(range(d+1))):
        target = comb(d-a,k-a) if a<=k else 0
        assert sum(c*fmpz(j)**a for j,c in enumerate(primary)) == target*fmpz(d)**a
    return primary


def serializable(sample):
    return str(sample)


def worker(data):
    return serializable(q_at(data))


def exact_summary(x):
    def data(a):
        return {"bits":a.bit_length(),"sha256_of_signed_decimal":sha256(str(a).encode()).hexdigest()}
    return {"sign":int(x>0)-int(x<0),"numerator":data(x.numerator),"denominator":data(x.denominator)}


def full_row(samples):
    """A/(L*d!) assembled by a product tree of homogeneous Lagrange basis rows."""
    d = len(samples)-1
    lcm = fmpz(1)
    for x in samples:
        lcm = lcm.lcm(x.denominator)
    def join(a,b):
        if b==a+1:
            weight = (-1)**(d-a)*comb(d,a)*(lcm//samples[a].denominator)*samples[a].numerator
            return fmpz_poly([-a,d-a]),fmpz_poly([weight])
        mid=(a+b)//2
        pl,al=join(a,mid)
        pr,ar=join(mid,b)
        return pl*pr,al*pr+ar*pl
    _,row=join(0,d+1)
    return row,lcm*factorial(d)


def dyadic_certificate(row,d):
    """Test the homogeneous numerator after a dyadic subdivision of the physical t."""
    shift=fmpz_poly([1,2])
    leaves=[]
    def reverse(f):
        return fmpz_poly([f[d-i] for i in range(d+1)])
    def visit(poly,j,n):
        smallest=min(poly[i] for i in range(d+1))
        if smallest>0:
            leaves.append({"left_numerator":j,"right_numerator":j+1,"denominator":n,
                           "positive_coefficients":d+1,
                           "smallest_integer_coefficient_bits":smallest.bit_length()})
            return
        if n>=256:
            raise AssertionError("positive subdivision not obtained")
        left=reverse(reverse(poly)(shift))
        right=poly(shift)
        visit(left,2*j,2*n)
        visit(right,2*j+1,2*n)
    visit(row,0,1)
    return leaves


def run(m,k,workers):
    d=(m-1)*(2*m-3)
    coeff=weights(d,k)
    points=[(m,j,d) for j in range(d+1)]
    if workers==1:
        samples=[q_at(point) for point in points]
    else:
        with Pool(workers) as pool:
            samples=[fmpq(x) for x in pool.imap(worker,points,chunksize=2)]
    weighted=sum(a*b for a,b in zip(coeff,samples))
    normalized=weighted/(comb(d,k)*samples[0])
    sign_count=[sum(int(t<0) if s<0 else int(t>0) if s>0 else int(t==0) for t in samples)
                for s in [-1,0,1]]
    # Record an exact short dyadic bracket for the normalized coefficient.
    a,b=abs(normalized.numerator),normalized.denominator
    exponent=int(a.bit_length()-b.bit_length())
    pow2=fmpq(2)**exponent
    if abs(normalized)<pow2:
        exponent-=1
        pow2/=2
    assert pow2<=abs(normalized)<2*pow2
    mantissa=(normalized/pow2*10**8).floor()
    if m==18 and k==279:
        assert weighted < 0
    row, row_den = full_row(samples)
    assert fmpq(row[k],row_den)==weighted
    assert fmpq(row[0],row_den)==samples[0] and fmpq(row[d],row_den)==samples[-1]
    subdivision=dyadic_certificate(row,d)
    return {"m":m,"d":d,"bernstein_index":k,
            "exact_negative_indices":[i for i in range(d+1) if row[i]<0],
            "exact_zero_indices":[i for i in range(d+1) if row[i]==0],
            "certified_positive_subintervals":subdivision,"rational_nodes":d+1,
            "negative_zero_positive_samples":sign_count,
            "ordinary_coefficient_of_transformed_polynomial":exact_summary(weighted),
            "normalized_by_binomial_times_q0":exact_summary(normalized),
            "normalized_dyadic_bracket":{"power_of_two":exponent,"denominator":10**8,
                "lower_numerator":int(mantissa),"upper_numerator":int(mantissa+1)}}


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--workers",type=int,default=2)
    args=parser.parse_args()
    print(json.dumps(run(18,279,args.workers),indent=2))
