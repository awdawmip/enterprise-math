"""Finite-field crossing form versus full rational tree cofactors, in the original graph coordinates."""
from fractions import Fraction
from math import comb, factorial, isqrt, lcm
import json


def prime(p):
    return p >= 2 and all(p % j for j in range(2, isqrt(p)+1))


def det(a, p=None):
    a = [row[:] for row in a]
    previous, sign = 1, 1
    for j in range(len(a)-1):
        pivot = next((k for k in range(j,len(a)) if a[k][j] and (p is None or a[k][j]%p)),None)
        if pivot is None:
            return 0
        if pivot != j:
            a[pivot],a[j] = a[j],a[pivot]
            sign *= -1
        for k in range(j+1,len(a)):
            b = a[k][j]
            for i in range(j+1,len(a)):
                u = a[j][j]*a[k][i] - b*a[j][i]
                a[k][i] = u // previous if p is None else u*pow(previous,-1,p)%p
        previous = a[j][j]
    v = sign*a[-1][-1]
    return v if p is None else v % p


def layers(m, scale=None, p=None):
    n, b = m-1, m*m
    depth = n if p is None else 1
    layers = []
    w = [(-1)**i*comb(n,i) for i in range(m)]
    for s in range(depth+1):
        mat = [[0]*(2*m-1) for _ in range(2*m-1)]
        for i in range(m):
            for j in range(m):
                denom = i+1+m*j+b*s
                inv = scale//denom if p is None else pow(denom,-1,p)
                weight = w[i]*w[j]*(-1)**s*comb(n,s)*inv
                mat[i][i] += weight
                if j<n:
                    v = m+j
                    mat[v][v] += weight
                    mat[i][v] -= weight
                    mat[v][i] -= weight
        layers.append(mat)
    return layers


def kernel(mat, p):
    n = len(mat)
    a = [[x%p for x in row] for row in mat]
    pivots = []
    for j in range(n):
        r = len(pivots)
        k = next((i for i in range(r,n) if a[i][j]),None)
        if k is None:
            continue
        a[r],a[k] = a[k],a[r]
        a[r] = [v*pow(a[r][j],-1,p)%p for v in a[r]]
        for i in range(n):
            if i != r:
                c = a[i][j]
                a[i] = [(v-c*u)%p for v,u in zip(a[i],a[r])]
        pivots.append(j)
    basis = []
    for f in set(range(n))-set(pivots):
        z = [0]*n
        z[f] = 1
        for k,j in enumerate(pivots):
            z[j] = -a[k][f]%p
        basis.append(z)
    return basis


def pole_coefficients(m,p):
    n,b = m-1,m*m
    l0,l1 = layers(m,p=p)
    ker = kernel(l0,p)
    assert len(ker)==n
    lv = [[sum(x*y for x,y in zip(row,v))%p for row in l1] for v in ker]
    form = [[sum(x*y for x,y in zip(u,h))%p for h in lv] for u in ker]
    F0 = det(form,p)
    assert F0
    changes = []
    leading = []
    for h in range(1,m**3//p+1):
        s, offset = divmod(h*p-1,b)
        j,i = divmod(offset,m)
        c = [u[i]-(u[m+j] if j<n else 0) for u in ker]
        weight = (-1)**(i+j+s)*comb(n,i)*comb(n,j)*comb(n,s)*pow(h,-1,p)
        changes.append([[weight*x*y%p for y in c] for x in c])
        # Multiaffine polarization gives the mixed principal Gram determinant.
        total = 0
        for mask in range(1<<h):
            selected = [u for k,u in enumerate(changes) if mask>>k & 1]
            changed = [[(v+sum(u[k][l] for u in selected))%p for l,v in enumerate(row)]
                       for k,row in enumerate(form)]
            total += (-1)**(h-len(selected))*det(changed,p)
        leading.append(total*pow(F0,-1,p)%p)
    return leading


def cofactor_polynomial(m):
    n = m-1
    size = 2*m-1
    d = (size-1)*n
    scale = lcm(*range(1,m**3+1))
    full = layers(m,scale=scale)
    def raw(t):
        mat = [[sum(full[s][i][j]*t**s for s in range(m))
                for j in range(size)] for i in range(size)]
        v = det(mat)
        assert v % t**n == 0
        return v//t**n
    vals = [raw(t) for t in range(1,d+2)]
    coef, basis = [0]*(d+1), [1]
    for j in range(d+1):
        lead, rem = divmod(vals[0],factorial(j))
        assert not rem
        for k,v in enumerate(basis):
            coef[k] += lead*v
        basis = [v-(j+1)*u for v,u in zip([0]+basis,basis+[0])]
        vals = [b-a for a,b in zip(vals,vals[1:])]
    assert sum(c*(-2)**j for j,c in enumerate(coef)) == raw(-2)
    return coef


def valuation(x,p):
    assert x
    v = 0
    while x%p==0:
        v += 1
        x //= p
    return v


def one_pole(m,p):
    """Interpolate p*q(t) mod p by suppressing the unique pole in the original graph."""
    n,b = m-1,m*m
    assert 2*p > m**3 and p > 2*n*n+2
    a, off = divmod(p-1,b)
    j0,i0 = divmod(off,m)
    w = [(-1)**j*comb(n,j) for j in range(m)]
    size = 2*m-1
    u = [int(k==i0) - int(j0<n and k==m+j0) for k in range(size)]
    factors = [[[(w[i]*w[j]*w[s]*pow(q,-1,p)%p if q!=p else 0)
                 for s in range(m) for q in [1+i+m*j+s*b]]
                for j in range(m)] for i in range(m)]
    def value(t):
        powers = [pow(t,s,p) for s in range(m)]
        mat = [[0]*size for _ in range(size)]
        for i in range(m):
            for j in range(m):
                weight = sum(v*z for v,z in zip(factors[i][j],powers))%p
                mat[i][i] += weight
                if j<n:
                    mat[m+j][m+j] += weight
                    mat[i][m+j] -= weight
                    mat[m+j][i] -= weight
        change = [[v+u[k]*u[l] for l,v in enumerate(row)] for k,row in enumerate(mat)]
        return ((det(change,p)-det(mat,p))*w[a]*w[i0]*w[j0]*pow(t,a-n,p))%p
    d = 2*n*n
    vals = [value(t) for t in range(1,d+2)]
    coef = [0]*(d+1)
    basis = [1]
    for k in range(d+1):
        lead = vals[0]*pow(factorial(k),-1,p)%p
        for j,v in enumerate(basis):
            coef[j] = (coef[j]+lead*v)%p
        vals = [(y-x)%p for x,y in zip(vals,vals[1:])]
        basis = [(v-(k+1)*u)%p for v,u in zip([0]+basis,basis+[0])]
    assert sum(c*pow(d+2,j,p) for j,c in enumerate(coef))%p == value(d+2)
    l0,l1 = layers(m,p=p)
    # In det(L0+t L1) the t^n coefficient is q(0).
    vals = [det([[x+t*y for x,y in zip(u,v)] for u,v in zip(l0,l1)],p)
            for t in range(size+1)]
    q0, basis = 0, [1]
    for k in range(size+1):
        if k >= n:
            q0 += vals[0]*pow(factorial(k),-1,p)*basis[n]
        vals = [(y-x)%p for x,y in zip(vals,vals[1:])]
        basis = [(v-k*u)%p for v,u in zip([0]+basis,basis+[0])]
    first = next((j for j,c in enumerate(coef) if c),None)
    return dict(m=m,p=p,initial_layer=a,first_pole_coefficient_degree=first,
                leading_residue=coef[first] if first is not None else None,
                q0_mod_p=q0%p,normalized_residue=coef[first]*pow(q0,-1,p)%p if first is not None else None)


def main():
    cases = []
    for m in range(3,10):
        poly = cofactor_polynomial(m) if m<=6 else None
        for p in range(2*m*m+1,m**3+1):
            if not prime(p) or (3*m*m+1)%p==0:
                continue
            a = (p-1)//(m*m)
            leading = pole_coefficients(m,p)
            coeff = leading[0]
            row = dict(m=m,p=p,initial_layer=a,gamma=coeff,successive_mixed_coefficients=leading)
            if poly:
                v0 = valuation(poly[0],p)
                E = 0
                for h,F in enumerate(leading,1):
                    E += (h*p-1)//(m*m)-1
                    actual = Fraction(p**h*poly[E],poly[0])
                    assert actual.numerator*pow(actual.denominator,-1,p)%p == F
                    assert all(valuation(c,p) >= v0-h+1 for c in poly[:E] if c)
                faces = [(Fraction(v0-valuation(c,p),k),k) for k,c in enumerate(poly) if k and c]
                maximum = max(v for v,k in faces)
                count = max(k for v,k in faces if v==maximum)
                assert maximum <= Fraction(1,a-1)
                assert (maximum==Fraction(1,a-1)) == bool(coeff)
                if coeff:
                    assert count == a-1
                    x = Fraction(p*poly[a-1],poly[0])
                    assert x.numerator*pow(x.denominator,-1,p)%p == coeff
                row.update(largest_root_valuation=str(maximum),multiplicity=count)
            cases.append(row)
    print(json.dumps(dict(exact_full_polynomial_cases=sum('multiplicity' in c for c in cases),
                          one_pole_refinements=[one_pole(9,709),one_pole(6,211)],
                          work='original signed Laplacian with the final right vertex grounded',
                          cases=cases),indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
