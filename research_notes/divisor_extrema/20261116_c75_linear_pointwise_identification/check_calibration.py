"""Exact finite Newton certificate for discrete total positivity of the outer stock basis."""
from itertools import combinations
from math import prod
from hashlib import sha256
import json

TERMS = ((0, 2), (0, 1), (1, 2), (1, 1), (1, 0), (2, 1), (2, 0))


def determinant(rows):
    m = [row[:] for row in rows]
    det_sign, previous = 1, 1
    for k in range(len(m)-1):
        if not m[k][k]:
            pivot = next((t for t in range(k+1,len(m)) if m[t][k]), None)
            if pivot is None:
                return 0
            m[k], m[pivot] = m[pivot], m[k]
            det_sign *= -1
        current = m[k][k]
        for r in range(k+1, len(m)):
            for s in range(k+1, len(m)):
                value, remainder = divmod(m[r][s]*current - m[r][k]*m[k][s], previous)
                assert remainder == 0
                m[r][s] = value
        previous = current
    return det_sign * m[-1][-1]


def raw_rows(x, length, terms, K=5):
    result = []
    A = B = C = 1
    for step in range(length):
        result.append([A**j*C**i*4**(step*(3-j))*B**(3-i-j) for i,j in terms])
        A *= 4*x+K+4+4*step
        B *= x+K+1+step
        C *= x+4*K+1+step
    return result


def forward_coefficients(layer):
    result = []
    while layer:
        result.append(layer[0])
        layer = [b - a for a, b in zip(layer, layer[1:])]
    return result


def check_all_depths():
    by_size = []
    for size in range(1,len(TERMS)+1):
        degree = 3*size*(size-1)//2
        count = nonzero = total = 0
        digest = sha256()
        for subset in combinations(TERMS,size):
            table = [forward_coefficients([
                determinant(raw_rows(x,size,subset,K)) for x in range(2,3+degree)])
                for K in range(1,2+degree)]
            # First difference in the c coordinate, then in K, based at (2,1).
            coefficients = [forward_coefficients(list(col)) for col in zip(*table)]
            assert coefficients[0][0] > 0
            for i, row in enumerate(coefficients):
                for j, value in enumerate(row):
                    assert value >= 0 and (i+j <= degree or value == 0), (subset,i,j,value)
                    total += 1
                    nonzero += int(value > 0)
                digest.update((','.join(map(str,row))+'\n').encode('ascii'))
            count += 1
        by_size.append(dict(size=size,minors=count,degree_bound=degree,
                            coefficients_checked=total,positive_coefficients=nonzero,
                            sha256_newton=digest.hexdigest()))
    return dict(K_start=1,c_start=2,terms=TERMS,by_size=by_size)

if __name__=='__main__':
    print(json.dumps(check_all_depths(),indent=2))
