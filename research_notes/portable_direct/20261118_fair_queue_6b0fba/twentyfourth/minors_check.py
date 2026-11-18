"""Half-Pascal AP pencil. Exact arithmetic, Python standard library, JSON on stdout."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, lcm, prod
import json


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse(a):
    m = len(a)
    aug = [row[:] + [F(i == j) for j in range(m)] for i, row in enumerate(a)]
    for j in range(m):
        k = next(i for i in range(j, m) if aug[i][j])
        aug[k], aug[j] = aug[j], aug[k]
        lead = aug[j][j]
        aug[j] = [x/lead for x in aug[j]]
        for i in range(m):
            if i != j and aug[i][j]:
                lead = aug[i][j]
                aug[i] = [x-lead*y for x, y in zip(aug[i], aug[j])]
    return [row[m:] for row in aug]


def row_scale(a):
    den = [lcm(*(x.denominator for x in row)) for row in a]
    return [[int(x*d) for x in row] for row, d in zip(a, den)], den


def bareiss(a):
    mat = [r[:] for r in a]
    n, previous, orientation = len(a), 1, 1
    if not n:
        return 1
    for k in range(n-1):
        if not mat[k][k]:
            other = next((i for i in range(k+1, n) if mat[i][k]), None)
            if other is None:
                return 0
            mat[k], mat[other] = mat[other], mat[k]
            orientation *= -1
        pivot = mat[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                value, rem = divmod(pivot*mat[i][j] - mat[i][k]*mat[k][j], previous)
                assert rem == 0
                mat[i][j] = value
        previous = pivot
    return orientation * mat[-1][-1]


def det(a):
    ia, den = row_scale(a)
    return F(bareiss(ia), prod(den))


def make(m, t=F(1,2)):
    n = m-1
    w = [(-1)**i*comb(n, i) for i in range(m)]
    stepsize = m*m
    h = [[F(factorial(n)*stepsize**n, prod(1+i+m*j+s*stepsize for s in range(m)))
          for j in range(m)] for i in range(m)]
    assert all(h[i][j] == sum(F((-1)**r*comb(n,r), 1+i+m*j+r*stepsize) for r in range(m))
               for i in range(m) for j in range(m))
    def normalized(gram):
        mass = [sum(w[j]*row[j] for j in range(m)) for row in gram]
        assert min(mass) > 0
        return [[x*w[j]/s for j, x in enumerate(row)] for row, s in zip(gram, mass)], mass
    a, e = normalized(h)
    b, d = normalized(list(zip(*h)))
    def pascal(t):
        return [[comb(i,j)*t**(i-j) if j <= i else F(0) for j in range(m)] for i in range(m)]
    s, sinv = pascal(F(1, 2)), pascal(F(-1, 2))
    def star(half):
        value = multiply(multiply(sinv, half), s)
        return [[(-1)**j*x for j, x in enumerate(row)] for row in value]
    astar, bstar = star(a), star(b)
    cstar = [[(-1)**(i+j)*x for j, x in enumerate(row)] for i, row in enumerate(inverse(bstar))]
    defect = [[x-y for x, y in zip(row, other)] for row, other in zip(cstar, astar)]
    ba = multiply(b, a)
    assert all(sum(row)==1 for row in ba)
    # Basis 1,e_1,...,e_n; the lower-right block has entries BA_ij-BA_0j.
    fixed_quotient = det([[F(i==j)-ba[i][j]+ba[0][j] for j in range(1,m)] for i in range(1,m)])
    scalar = det(cstar)*fixed_quotient / sum(wj*dj for wj, dj in zip(w,d))
    # Integrate t^i(1-t/2)^(n-i) against (1-t^m)^n(1-t^(m*m))^n.
    def moment(i):
        return sum(F((-1)**(j+k)*comb(n,j)*comb(n,k), 1+i+m*j+m*m*k)
                   for j in range(m) for k in range(m))
    assert e == [moment(i) for i in range(m)]
    spine = [comb(n,i)*sum(F((-1)**r*comb(n-i,r), 2**r)*moment(i+r)
                           for r in range(n-i+1)) for i in range(m)]
    assert scalar > 0 and min(spine) > 0
    if t != F(1,2):
        shift = t-F(1,2)
        defect = multiply(multiply(pascal(-shift), defect), pascal(shift))
        spine = [comb(n,i)*sum((-t)**r*comb(n-i,r)*moment(i+r)
                               for r in range(n-i+1)) for i in range(m)]
    return defect, scalar, spine


def moving_center_certificate(defect):
    """Bernstein sign certificates on full subintervals, after exact Newton interpolation."""
    m = len(defect)
    def pascal(t):
        return [[comb(i,j)*t**(i-j) if i>=j else F(0) for j in range(m)] for i in range(m)]
    def two_minors(t):
        h = t-F(1,2)
        matrix = multiply(multiply(pascal(-h), defect), pascal(h))
        return [det([row[c:c+5] for row in matrix[2:7]]) for c in (0,1)]
    values = [two_minors(F(j)) for j in range(21)]
    def power_coeffs(col, degree):
        differences = [q[col] for q in values[:degree+1]]
        a, newton = [F(0)]*(degree+1), [F(1)]
        for j in range(degree+1):
            for i, x in enumerate(newton):
                a[i] += x*differences[0]
            newton = [(v-j*u)/(j+1) for v,u in zip([F(0)]+newton, newton+[F(0)])]
            differences = [v-u for u,v in zip(differences,differences[1:])]
        assert a[-1] != 0
        return a
    powers = [power_coeffs(0,20), power_coeffs(1,15)]
    cert = []
    for lo,hi,col in [(F(0),F(1,8),1), (F(1,8),F(1,4),1),
                      (F(1,4),F(1,2),0), (F(1,2),F(1),0)]:
        a = powers[col]
        d = len(a)-1
        shifted = [(hi-lo)**j*sum(a[k]*comb(k,j)*lo**(k-j) for k in range(j,d+1))
                   for j in range(d+1)]
        coefficients = [sum(F(comb(i,j),comb(d,j))*shifted[j] for j in range(i+1))
                        for i in range(d+1)]
        assert max(coefficients) < 0
        smallest_abs = -max(coefficients)
        b = max(0, smallest_abs.denominator.bit_length()-smallest_abs.numerator.bit_length()+1)
        assert max(coefficients) <= -F(1,2**b)
        assert sum(coefficients[j]*comb(d,j) for j in range(d+1))/2**d == two_minors((lo+hi)/2)[col]
        cert.append({'interval':[str(lo),str(hi)], 'column_start':col, 'degree':d,
                     'negative_coefficients':d+1,'each_coefficient_at_most_minus_two_to_minus':b})
    q0,q1 = two_minors(F(33,256))
    assert q0>0 and q1<0
    return cert


def enumerate_minors(m):
    defect, scalar, spine = make(m)
    integral, den = row_scale(defect)
    # Laplace expansion by the last selected row, with one dictionary per order.
    # Positive row denominators need only be restored for the numerical comparisons.
    prev = {((), ()): 1}
    statistics, negatives = [], []
    for k in range(1,m+1):
        subsets = list(combinations(range(m),k))
        reducers = {j: [(column, j[:t]+j[t+1:], (-1)**(k-1+t)) for t, column in enumerate(j)]
                    for j in subsets}
        current, counts = {}, [0, 0, 0]
        for i in subsets:
            row = integral[i[-1]]
            for j in subsets:
                val = sum(s*row[c]*prev[i[:-1], rest] for c, rest, s in reducers[j])
                current[i,j] = val
                counts[(val>0)-(val<0)+1] += 1
                if m==7 and val<0:
                    negatives.append([list(i),list(j)])
                if k==m-1:
                    out_i = next(h for h in range(m) if h not in i)
                    out_j = next(h for h in range(m) if h not in j)
                    exact = F(val, prod(den[h] for h in i))
                    assert exact == scalar * spine[out_i] / 2**out_j
        assert sum(counts)==comb(m,k)**2
        statistics.append(counts)
        prev = current
    assert counts==[0,1,0]
    result = {'counts_by_order_negative_zero_positive': statistics, 'maximal_minors_formula_checks': m*m}
    if m in (3,7):
        other_checks = 0
        for t in (F(1,7), F(1)):
            shifted, scale, masses = make(m,t)
            for i in range(m):
                for j in range(m):
                    a = [[v for col,v in enumerate(row) if col!=j]
                         for r,row in enumerate(shifted) if r!=i]
                    assert det(a) == scale*masses[i]*t**j
                    other_checks += 1
        result['extra_maximal_minor_checks_at_1_over_7_and_1'] = other_checks
    if m==7:
        def minor(i,j,k):
            return det([row[j:j+k] for row in defect[i:i+k]])
        q = minor(2,0,5)
        p = minor(2,1,4)*minor(3,0,4)/(minor(2,0,4)*minor(3,1,4))
        assert q*minor(3,1,3) == minor(2,0,4)*minor(3,1,4)*(1-p)
        assert F(1109618870,10**9)<p<F(1109618871,10**9)
        assert [minor(i,j,5)>0 for i in (0,2) for j in (0,2)]==[True,True,False,True]
        result.update({'center_interval_certificates': moving_center_certificate(defect),
                       'negative_indices_zero_based': negatives, 'negative_contiguous_five': str(q),
                       'desnanot_cross_ratio_integer_bracket': [1109618870,1109618871,10**9]})
    return result


if __name__=='__main__':
    data = {m: enumerate_minors(m) for m in range(2,9)}
    assert data[7]['counts_by_order_negative_zero_positive'][4] == [21,0,420]
    assert data[8]['counts_by_order_negative_zero_positive'][5] == [305,0,479]
    print(json.dumps(data, indent=2))
