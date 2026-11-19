"""Sharp positive degree elevation of the original AP cofactor (python-flint 0.9.0)."""
import json
from math import comb, factorial, isqrt, prod
from pathlib import Path
import sys

from flint import acb, acb_mat, arb, arb_poly, ctx, fmpq, fmpq_mat

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'twentyfirst'))
from physical_flow_check import cofactor

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'sixtyninth'))
from galois_check import residue_polynomial


def original_row(m):
    n = m-1
    b = m*m
    d = n*(2*m-3)
    size = min(3**a*5**j*7**k for a in range(8) for j in range(5) for k in range(4)
               if 3**a*5**j*7**k > d)
    w = [(-1)**i*comb(n,i) for i in range(m)]
    spectra = []
    endpoint = []
    for i in range(m):
        row = []
        end_row = []
        for j in range(m):
            ell = 1+i+m*j
            val = arb(w[i]*w[j])/ell
            coefficients = [acb(val)]
            for h in range(1,n+1):
                val = val*((n-h+1)*b)/(ell+b*h)
                coefficients.append(acb(val))
            row.append(acb.dft(coefficients+[acb(0)]*(size-n-1)))
            end_row.append(fmpq(w[i]*w[j]*factorial(n)*b**n,prod(ell+b*s for s in range(m))))
        spectra.append(row)
        endpoint.append(end_row)
    sample = [None]*size
    for k in range(size//2+1):
        z = (acb(-2*k)/size).exp_pi_i()
        edges = [[entry[k] for entry in row] for row in spectra]
        sample[k] = cofactor(edges, acb_mat)/(z*(1+z))**n
        if k:
            sample[-k] = sample[k].conjugate()
    coeff = acb.dft(sample,inverse=True)
    assert all(x.imag.contains(0) for x in coeff)
    assert all(x.contains(0) for x in coeff[d+1:])
    q0 = fmpq(n**n*m**(n*(n+3)+m)*factorial(n)**(2*m)*(3*b+1)*prod(comb(n,j)**2 for j in range(m)),
              2*factorial(2*b))
    assert coeff[0].real.overlaps(arb(q0))
    assert coeff[d].real.overlaps(arb(cofactor(endpoint,fmpq_mat)))
    return [entry.real/(arb(q0)*comb(d,j)) for j,entry in enumerate(coeff[:d+1])]


def scaled_floor(value, power):
    integer = (value*10**power).floor().unique_fmpz()
    assert integer is not None
    result = int(integer)
    assert arb(fmpq(result,10**power)) < value < arb(fmpq(result+1,10**power))
    return result


def signed(value):
    assert value<0 or value>0
    return 1 if value>0 else -1


def numerator_row(beta, N):
    d = len(beta)-1
    return arb_poly([v*comb(d,i) for i,v in enumerate(beta)])*arb_poly([1,1])**(N-d)


def direct_coefficient(beta, N, k):
    d = len(beta)-1
    value = sum(beta[j]*(comb(d,j)*comb(N-d,k-j))
                for j in range(max(0,k-N+d),min(k,d)+1))
    return value/comb(N,k)


def elevation(beta, N):
    polynomial = numerator_row(beta,N)
    row = [polynomial[k]/comb(N,k) for k in range(N+1)]
    for i,x in enumerate(row):
        if x.contains(0):
            row[i] = direct_coefficient(beta,N,i)
    negative = [i for i,x in enumerate(row) if signed(x)<0]
    least = min(range(len(row)), key=lambda i: float(row[i]))
    assert all(row[least]<x for i,x in enumerate(row) if i!=least)
    assert row[least].overlaps(direct_coefficient(beta,N,least))
    return dict(degree=N,negative_indices=negative,minimum_index=least,
                minimum_floor_times_1e16=scaled_floor(row[least],16))


def derivative(row):
    degree = len(row)-1
    return [degree*(b-a) for a,b in zip(row,row[1:])]


def evaluate(row, t):
    if t==0:
        return row[0]
    if t==1:
        return row[-1]
    degree = len(row)-1
    term = (1-t)**degree
    ratio = t/(1-t)
    result = row[0]*term
    for i in range(1,degree+1):
        term = term*ratio*(degree-i+1)/i
        result += term*row[i]
    return result


def shape(beta):
    first = derivative(beta)
    second = derivative(first)
    signs = [signed(x) for x in first]
    changes = sum(x!=y for x,y in zip(signs,signs[1:]))
    assert signs[0]==signs[-1]==-1 and changes==2
    # The derivative has degree d-1 and only two sign changes in its Bernstein row.
    denominator = 32
    samples = [signed(evaluate(first,arb(k)/denominator)) for k in range(denominator+1)]
    intervals = [k for k in range(denominator) if samples[k]!=samples[k+1]]
    assert len(intervals)==2
    roots = []
    for k in intervals:
        direction = samples[k]
        den = denominator
        for _ in range(43):
            midpoint = 2*k+1
            den *= 2
            k = 2*k + (signed(evaluate(first,arb(midpoint)/den))==direction)
        lo,hi = arb(k)/den,arb(k+1)/den
        # When x ranges in this enclosure, every Bernstein term remains a rigorous interval.
        root = lo.union(hi)
        value = evaluate(beta,root)
        curvature = root*(1-root)*evaluate(second,root)/2
        roots.append((root,value,curvature))
    x,minimum,constant = roots[0]
    assert constant>0 and roots[1][2]<0 and minimum<beta[0] and minimum<beta[-1]
    a = evaluate(second,x)
    b = evaluate(derivative(second),x)
    c = evaluate(derivative(derivative(second)),x)
    w = x*(1-x)
    dC = ((1-2*x)*a + w*b)/2
    R = -constant + w*(1-2*x)*b/3 + w*w*c/8
    return dict(grid_shift_floor_times_1e6=scaled_floor(dC/a,6),
                oscillation_lower_floor_times_1e9=scaled_floor(R-dC*dC/(2*a),9),
                oscillation_width_floor_times_1e9=scaled_floor(a/8,9),
                derivative_sign_changes=changes,critical_brackets_over_32=intervals,
                minimum_argument_floor_times_1e9=scaled_floor(x,9),
                minimum_value_floor_times_1e13=scaled_floor(minimum,13),
                curvature_constant_floor_times_1e10=scaled_floor(constant,10))


def verify():
    ctx.prec=2048
    out=[]
    for m,N,p in [(18,829,5839),(19,1428,6863),(20,2276,8069),(21,3432,9277)]:
        beta=original_row(m)
        d=len(beta)-1
        low,high=elevation(beta,N-1),elevation(beta,N)
        assert len(low['negative_indices'])==1 and not high['negative_indices']
        assert p>m**3 and all(p%i for i in range(2,isqrt(p)+1))
        reduced=residue_polynomial(m,p)
        deriv=reduced.derivative()
        assert reduced.degree()==d and deriv.degree()==d-1
        X=type(reduced)([0,1],p)
        assert deriv.gcd(X.pow_mod(p,deriv)-X).degree()==0
        out.append(dict(m=m,original_degree=d,least_multiplier_exponent=N-d,
                        prime=p,derivative_lead_mod_p=int(deriv[d-1]),linear_factor_count=0,
                        last_failure=low,first_positive=high,shape=shape(beta)))
    return dict(bit_precision=ctx.prec,normalization='q(t)/q(0)',cases=out)


if __name__=='__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
