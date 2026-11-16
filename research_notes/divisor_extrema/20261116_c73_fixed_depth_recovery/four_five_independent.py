"""Independent one-readout Jacobian checks by p-adic finite differences."""
from verify_fixed_h import derivatives
from math import prod

P = 1_000_000_007
M = P * P
profiles = {
    4: [[20, 8, 8, 8], [1, 15, 9, 3]],
    5: [[26, 8, 8, 8, 8], [1, 21, 15, 9, 3]]
}


def evaluate(xs):
    r = len(xs)-1
    real, center, dr, dc = 0, 0, 1, 1
    for i in range(r, 0, -1):
        inventory = 2*(r-i+1)+1
        rate = 4*pow(xs[i]*pow(xs[i-1],-1,M),3*inventory,M)%M
        scale = pow(16,-1,M)*7*pow(rate,5,M)%M
        a = rate*pow(scale,-1,M)%M
        real_den = 1+scale*real
        center_den = 1+a*center
        dr = dr*scale*(1-rate)*pow(real_den,-2,M)%M
        dc = -dc*a*pow(center_den,-2,M)%M
        real = (rate+scale*real)*pow(real_den,-1,M)%M
        center = pow(center_den,-1,M)
    observable = [dr*pow(real,-1,M)*pow(xs[-1],-3,M)%M,
                  dc*pow(center,-1,M)*pow(xs[-1],-12,M)%M]
    for row in profiles[r]:
        observable.append(prod(pow(x,4*e,M) for x,e in zip(xs[1:],row))%M)
    if r == 5:
        lands = [pow(x,4,M) for x in xs]+[0]
        observable.extend([(a-b)%M for a,b in zip(lands,lands[1:])])
    return observable


def rank_cert(r):
    import sympy
    xs = [1]+[(13-i)*pow(13+i,-1,M)%M for i in range(1,r+1)]
    base = evaluate(xs)
    columns = []
    for j in range(1,r+1):
        shifted = xs[:]
        shifted[j] += P
        lifted = evaluate(shifted)
        differences = [(b-a)%M for a,b in zip(base,lifted)]
        assert all(d%P == 0 for d in differences)
        columns.append([d//P for d in differences])
    rows = list(zip(*columns))
    if r == 4:
        return [int(sympy.Matrix(rows).det())%P]
    return [int(sympy.Matrix(rows[:4]+[row]).det())%P for row in rows[4:]]


if __name__=='__main__':
    for r in profiles:
        ds=rank_cert(r)
        assert all(ds)
        print(f'r={r}: {ds}')
    gs=(2,3,5,7,11,13)
    coeffs=derivatives(gs)
    coeff_mod=[t.numerator*pow(t.denominator,-1,P)%P for t in coeffs]
    assert all(coeff_mod)
    print(f'c={2+sum(gs)}, gaps={gs}, oriented log-center coefficient residues={coeff_mod}')
