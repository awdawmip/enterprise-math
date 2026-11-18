"""Signed-secant endpoints and finite exchangeability lengths, with exact rational arithmetic."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial, prod
import json


def determinant(matrix):
    matrix = [list(map(Q, row)) for row in matrix]
    value = Q(1)
    for i in range(len(matrix)):
        pivot = next((h for h in range(i, len(matrix)) if matrix[h][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            matrix[pivot], matrix[i] = matrix[i], matrix[pivot]
            value = -value
        diagonal = matrix[i][i]
        value *= diagonal
        for h in range(i + 1, len(matrix)):
            scale = matrix[h][i] / diagonal
            for j in range(i + 1, len(matrix)):
                matrix[h][j] -= scale * matrix[i][j]
    return value


def cofactor_value(m, t):
    """Original reduced Laplacian at t (independent of the squared-secant construction)."""
    n = m-1
    w = [(-1)**i*comb(n, i) for i in range(m)]
    L = [[Q(0) for _ in range(2*m)] for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            hij = sum(Q(w[s]*t**s, i+1+m*j+m*m*s) for s in range(m))
            edge = w[i]*w[j]*hij
            L[i][i] += edge
            L[m+j][m+j] += edge
            L[i][m+j] = L[m+j][i] = -edge
    return determinant([row[:-1] for row in L[:-1]]) / t**n


def endpoints(m):
    n, b = m-1, m*m
    factor = Q(n**n*m**(n*(n+3)+m)*prod(comb(n,j)**2 for j in range(m))
               *factorial(n)**(2*m), 2*factorial(2*b))
    h0 = factor*(3*b+1)
    ratio = Q((2*n-1)*b+1, (3*b+1)*comb((n+1)*b,2*b))
    return h0, h0*ratio


def endpoint_checks():
    records = []
    for m in range(2, 7):
        d = (m-1)*(2*m-3)
        values = [cofactor_value(m, t) for t in range(1, d+2)]
        constant = sum((-1)**(j+1)*comb(d+1,j)*values[j-1] for j in range(1,d+2))
        leading = sum((-1)**(d-j)*comb(d,j)*values[j] for j in range(d+1))/factorial(d)
        h0, hd = endpoints(m)
        assert constant == h0 and (-1)**d*leading == hd
        records.append({"m":m, "degree":d, "cofactor_values":d+1,
                        "hd_over_h0":str(hd/h0)})
    return records


def direct_secants_m3():
    n, m, b, d = 2, 3, 9, 6
    q = [Q(0)]*(d+1)
    atoms = [(j,s) for j in range(m) for s in range(m)]
    bases = 0
    for I in combinations(atoms,5):
        groups = [[s for j,s in I if j==i] for i in range(m)]
        if not all(groups):
            continue
        rows = []
        for i, group in enumerate(groups):
            z0 = m*i+b*group[0]
            for s in group[1:]:
                z = m*i+b*s
                rows.append((z-z0,z*z-z0*z0))
        delta = rows[0][0]*rows[1][1]-rows[1][0]*rows[0][1]
        if not delta:
            continue
        bases += 1
        weight = Q(delta**2,4)  # (prod_(i=1)^n i!)^2 = 4
        for j,s in I:
            weight *= Q((-1)**(j+s)*comb(n,j)*comb(n,s)*factorial(n),
                        prod(m*j+b*s+r for r in range(1,m+1)))
        q[sum(s for j,s in I)-n] += weight
    for t in range(d+1):
        assert sum(x*(t+1)**a for a,x in enumerate(q)) == cofactor_value(m,t+1)
    return [(-1)**a*x/(comb(d,a)*q[0]) for a,x in enumerate(q)], bases


def functional(h, N, roots, sign=1):
    # Newton expansion P(x)=sum_a (Delta^a P)(0) binom(x,a).
    col = [sign*prod(x-j for j in roots) for x in range(len(roots)+1)]
    result = Q(0)
    for a in range(len(roots)+1):
        result += col[0]*comb(N,a)*h[a]
        col = [y-x for x,y in zip(col,col[1:])]
    return result


def primal(h, N, nodes):
    weights = []
    for j in nodes:
        others = [i for i in nodes if i!=j]
        weights.append(functional(h,N,others)/prod(j-i for i in others))
    for a in range(len(nodes)):
        assert sum(w*comb(j,a) for j,w in zip(nodes,weights)) == comb(N,a)*h[a]
    assert all(w>0 for w in weights)
    return [str(w) for w in weights]


def facets(h, s, N):
    count = negative = 0
    worst = None
    for roots in combinations(range(N+1), s):
        values = [prod(x-j for j in roots) for x in range(N+1)]
        if min(values)<0<max(values):
            continue
        sign = 1 if min(values)>=0 else -1
        value = functional(h,N,roots,sign)
        count += 1
        negative += value<0
        if worst is None or value<worst[0]:
            worst = value, roots, sign
    return {"N":N, "facets":count, "negative":negative, "minimum":str(worst[0]),
            "roots_at_minimum":worst[1],"sign_at_minimum":worst[2]}


def main():
    assert endpoints(2)[1]/endpoints(2)[0] == Q(5,13)
    h, bases = direct_secants_m3()
    runs = []
    for s,N,nodes in [(3,29,[0,6,7,8]), (4,13,[0,1,4,5,13]),
                      (5,12,[0,1,2,3,4,5]), (6,12,[0,1,2,3,4,5,12])]:
        inside, outside = [facets(h,s,v) for v in [N,N+1]]
        assert inside["negative"]==0 and outside["negative"]>0
        runs.append({"truncation":s, "max_extension":N, "support":nodes,
                     "weights":primal(h,N,nodes),"facet_boundary":[inside,outside]})
    value = h[3]-Q(2,5)*h[2]+Q(1,25)*h[1]
    assert value==Q(-71034823,58017960000)
    atom, mass = h[2]/h[1], h[1]**2/h[2]
    assert 0<atom<1 and 0<mass<1 and mass*atom==h[1] and mass*atom**2==h[2]
    print(json.dumps({"endpoint_cofactor_checks":endpoint_checks(),
                      "m3_atom_sets_checked":comb(9,5),"m3_nonzero_bases":bases,
                      "m3_normalized":list(map(str,h)),
                      "ordinary_measure_through_degree_2":{"nonzero_atom":str(atom),
                                                           "its_mass":str(mass)},
                      "ordinary_cubic_test":str(value),"finite_exchangeability":runs},
                     indent=2))


if __name__=="__main__":
    main()
