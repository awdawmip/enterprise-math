"""Bernstein sign certificates for the physical AP interval (python-flint 0.9.0)."""
import argparse
import json
from math import comb, factorial, prod
from flint import acb, acb_mat, arb, ctx, fmpq, fmpq_mat


def cofactor(edges, matrix_type):
    m = len(edges)
    mat = matrix_type(2*m-1, 2*m-1)
    for i, row in enumerate(edges):
        mat[i,i] = sum(row)
        for j in range(m-1):
            mat[i,m+j] = mat[m+j,i] = -row[j]
    for j in range(m-1):
        mat[m+j,m+j] = sum(row[j] for row in edges)
    return mat.det()


def split_half(coefficients):
    """Normalized Bernstein control values on the two closed half intervals."""
    row = coefficients
    left, right = [row[0]], [row[-1]]
    while len(row) > 1:
        row = [(u+v)/2 for u,v in zip(row,row[1:])]
        left.append(row[0])
        right.append(row[-1])
    return left, list(reversed(right))


def lower_power(positive):
    lo = min(value.lower() for value in positive)
    assert lo > 0
    exponent = 0
    while not lo > arb(1)/(1 << exponent):
        exponent += 1
    return exponent


def verify(m):
    n, b = m-1, m*m
    degree = n*(2*m-3)
    # An odd transform length avoids the pole introduced by dividing by (1+z)^n.
    length = min(3**a*5**j*7**k for a in range(8) for j in range(5) for k in range(4)
                 if 3**a*5**j*7**k > degree)
    weights = [(-1)**i*comb(n,i) for i in range(m)]
    spectra = []
    exact_at_one = []
    for i in range(m):
        row, fixed = [], []
        for j in range(m):
            ell = 1+i+m*j
            # Coefficients of the homogenized edge in ordinary powers of z.
            value = arb(weights[i]*weights[j])/ell
            poly = [acb(value)]
            for h in range(1,n+1):
                value = value*((n-h+1)*b)/(ell+b*h)
                poly.append(acb(value))
            row.append(acb.dft(poly + [acb(0)]*(length-len(poly))))
            fixed.append(fmpq(weights[i]*weights[j]*factorial(n)*b**n,
                               prod(ell+b*s for s in range(n+1))))
        spectra.append(row)
        exact_at_one.append(fixed)

    values = [None]*length
    for k in range(length//2+1):
        z = (acb(-2*k)/length).exp_pi_i()
        edges = [[spec[k] for spec in row] for row in spectra]
        value = cofactor(edges,acb_mat) / ((z*(1+z))**n)
        values[k] = value
        if k:
            values[-k] = value.conjugate()
    coefficients = acb.dft(values,inverse=True)
    assert all(x.imag.contains(0) for x in coefficients)
    assert all(x.contains(0) for x in coefficients[degree+1:])
    beta = [x.real/comb(degree,j) for j,x in enumerate(coefficients[:degree+1])]
    q0 = fmpq(n**n * m**(n*(n+3)+m) * factorial(n)**(2*m) *
              prod(comb(n,j)**2 for j in range(m)) * (3*b+1), 2*factorial(2*b))
    q1 = cofactor(exact_at_one,fmpq_mat)
    assert q1 > 0 and beta[0].overlaps(arb(q0)) and beta[-1].overlaps(arb(q1))

    normalized = [v/arb(q0) for v in beta]
    assert all(x>0 or x<0 for x in normalized), "raise bit precision"
    negatives = [j for j,x in enumerate(normalized) if x<0]
    pieces = split_half(normalized) if negatives else [normalized]
    result = {'m':m, 'degree':degree, 'odd_transform_length':length,
              'negative_indices':negatives, 'number_strictly_positive_before_split':len(beta)-len(negatives),
              'whole_or_two_half_lower_dyadic_exponents_for_q_over_q0':[lower_power(piece) for piece in pieces]}
    if negatives:
        j = negatives[0]
        value = normalized[j]
        scaled = (value*10**12).floor().unique_fmpz()
        assert scaled is not None
        low = int(scaled)
        assert value > arb(fmpq(low,10**12)) and value < arb(fmpq(low+1,10**12))
        result['first_negative_ratio_between_consecutive_trillionths'] = [low,low+1]
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--precision',type=int,default=1536)
    parser.add_argument('--moduli',nargs='+',type=int,default=list(range(2,21)))
    args=parser.parse_args()
    ctx.prec=args.precision
    print(json.dumps({'carrier':'AP normalized residual q_m; q0 is its positive constant coefficient',
                      'rows':[verify(m) for m in args.moduli]},indent=2))


if __name__ == '__main__':
    main()
