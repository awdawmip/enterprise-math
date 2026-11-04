#!/usr/bin/env python3
"""PREFIX-484: exact Smith-with-transform and source order-fiber certificate.
Standard-library integers/Fractions. No external modules, network or randomness beyond seeded Random.
"""
from fractions import Fraction
from random import Random
from math import gcd
from functools import reduce

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def matmul(a, b):
    if not a:
        return []
    if not b:
        return [[] for _ in a]
    assert len(a[0]) == len(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]

def matvec(a, x):
    return [sum(t * u for t, u in zip(row, x)) for row in a]

def rank_q(a, ncols=None):
    if not a:
        return 0
    b = [[Fraction(x) for x in row] for row in a]
    cols = len(b[0]) if ncols is None else ncols
    k = 0
    for j in range(cols):
        piv = next((i for i in range(k, len(b)) if b[i][j]), None)
        if piv is None:
            continue
        b[k], b[piv] = b[piv], b[k]
        val = b[k][j]
        b[k] = [x / val for x in b[k]]
        for i in range(k + 1, len(b)):
            fac = b[i][j]
            if fac:
                b[i] = [v - fac * t for v, t in zip(b[i], b[k])]
        k += 1
        if k == len(b):
            break
    return k

def smith_with_transform(m, ncols=None):
    """Return U,S,V, with U*M*V=S and divisibility-chain SNF.
    Handles rectangular matrices and zero rows/columns. All elementary moves are unimodular.
    """
    rows = len(m)
    cols = len(m[0]) if rows else (ncols if ncols is not None else 0)
    assert all(len(row) == cols for row in m)
    A = [list(row) for row in m]
    U, V = identity(rows), identity(cols)
    def swap_row(i, j):
        A[i], A[j] = A[j], A[i]
        U[i], U[j] = U[j], U[i]
    def swap_col(i, j):
        for arr in (A, V):
            for row in arr:
                row[i], row[j] = row[j], row[i]
    def row_add(i, j, c):
        for arr in (A, U):
            arr[i] = [v + c * t for v, t in zip(arr[i], arr[j])]
    def col_add(i, j, c):
        for arr in (A, V):
            for row in arr:
                row[i] += c * row[j]
    def row_neg(i):
        for arr in (A, U):
            arr[i] = [-x for x in arr[i]]
    k = 0
    while k < min(rows, cols):
        nonzero = [(abs(A[i][j]), i, j) for i in range(k, rows)
                   for j in range(k, cols) if A[i][j]]
        if not nonzero:
            break
        _, i, j = min(nonzero)
        swap_row(k, i)
        swap_col(k, j)
        seen = 0
        while True:
            seen += 1
            if seen > 3000:
                raise RuntimeError('Smith pivot failed to converge')
            changed = False
            for i in range(k+1, rows):
                if A[i][k]:
                    q, rem = divmod(A[i][k], A[k][k])
                    row_add(i, k, -q)
                    if rem:
                        swap_row(i, k)
                    changed = True
                    break
            if changed:
                continue
            for j in range(k+1, cols):
                if A[k][j]:
                    q, rem = divmod(A[k][j], A[k][k])
                    col_add(j, k, -q)
                    if rem:
                        swap_col(j, k)
                    changed = True
                    break
            if changed:
                continue
            pivot = A[k][k]
            bad = next(((i, j) for i in range(k+1, rows)
                        for j in range(k+1, cols) if A[i][j] % pivot), None)
            if bad is not None:
                row_add(k, bad[0], 1)
                continue
            break
        if A[k][k] < 0:
            row_neg(k)
        k += 1
    diag = [A[i][i] for i in range(min(rows, cols)) if A[i][i] != 0]
    assert all(A[i][j] == (A[i][i] if i == j else 0)
               for i in range(rows) for j in range(cols))
    assert all(d > 0 for d in diag)
    assert all(b % a == 0 for a, b in zip(diag, diag[1:]))
    assert matmul(matmul(U, m), V) == A
    return U, A, V

def inverse_unimodular(a):
    n = len(a)
    t = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for k in range(n):
        pos = next(i for i in range(k, n) if t[i][k])
        t[k], t[pos] = t[pos], t[k]
        fac = t[k][k]
        t[k] = [x / fac for x in t[k]]
        for i in range(n):
            if i != k:
                fac = t[i][k]
                t[i] = [x-fac*y for x,y in zip(t[i],t[k])]
    inv = [row[n:] for row in t]
    assert all(x.denominator == 1 for row in inv for x in row)
    return [[int(x) for x in row] for row in inv]

def assert_snf_case(m, h):
    n = len(m[0]) if m else len(h[0])
    U, S, V = smith_with_transform(m, n)
    a = rank_q(m)
    assert a == sum(S[i][i] != 0 for i in range(min(len(m), n)))
    B = [[V[i][j] for j in range(a, n)] for i in range(n)]
    HB = matmul(h, B)
    L, D, R = smith_with_transform(HB, n-a)
    r = rank_q(HB, n-a)
    assert r == rank_q(m+h)-a
    Vin = inverse_unimodular(V)
    Rin = inverse_unimodular(R)
    for p in ([0]*n, [i+1 for i in range(n)], [(-1)**i * (2*i+3) for i in range(n)]):
        c = matvec(Vin, p)
        obs = matvec(m, p)
        uobs = matvec(U, obs)
        ca = [uobs[i] // S[i][i] for i in range(a)]
        assert all(S[i][i] * ca[i] == uobs[i] for i in range(a))
        ck = c[a:]
        t = matvec(Rin, ck)[:r]
        mapped = [D[i][i]*t[i] if i < r else 0 for i in range(len(h))]
        back = matvec(inverse_unimodular(L), mapped)
        v_a = [[V[i][j] for j in range(a)] for i in range(n)]
        rec = [x+y for x,y in zip(matvec(h, matvec(v_a, ca)), back)]
        assert rec == matvec(h, p)
    return a, r, [S[i][i] for i in range(a)], [D[i][i] for i in range(r)]

def kmp(word, gate='aab'):
    q = 0
    for char in word:
        if char == 'x':
            q = 0
            continue
        test = gate[:q] + char
        q = max((j for j in range(len(gate)+1) if test.endswith(gate[:j])), default=0)
    return q

def observe(word):
    axes = 'abcde'
    p, y = [], []
    for c in axes:
        plus, minus = word.count(c), word.count(c.upper())
        p.append(min(plus, minus))
        y.append(plus-minus)
    M = [[1,1,1,1,1],[0,1,0,2,1],[0,0,1,0,1]]
    return (len(word), word.count('x'), tuple(y), tuple(matvec(M, p)), kmp(word))

def weight(word):
    weights = dict(zip('abcde', [6,12,18,24,36]))
    weights.update(dict.fromkeys('ABCDE',1))
    weights['x'] = 1
    w = 1
    for c in word:
        w *= weights[c]
    return w

def first_bc(word):
    state = 0
    for c in word:
        if not state and c in 'bBcC':
            state = 1 if c in 'bB' else 2
    return state

def run():
    M = [[2,0,0,0], [0,6,0,0]]
    H = [[0,0,6,0], [0,0,0,10]]
    stats = assert_snf_case(M, H)
    assert stats == (2,2,[2,6],[2,30]), stats
    M2 = [[2,0,0,0],[0,6,0,0]]
    H2 = [[0,0,4,6],[0,0,8,12]]
    assert assert_snf_case(M2,H2) == (2,1,[2,6],[2])
    rand = Random(484)
    cases = 0
    peak = 0
    for _ in range(360):
        n = rand.randint(1,6)
        m = rand.randint(1,5)
        ell = rand.randint(1,5)
        A = [[rand.randint(-8,8) for j in range(n)] for i in range(m)]
        B = [[rand.randint(-9,9) for j in range(n)] for i in range(ell)]
        a,r,sd,dd = assert_snf_case(A,B)
        assert 0<=r<=min(ell,n-a)
        cases += 1
        peak = max(peak, *(abs(x) for row in A+B for x in row))
    no = 'aA'*3 + 'dD'*2 + 'eE'
    yes = 'bB'*2 + 'aA'*2 + 'dD' + 'eE'
    cfirst = 'cC' + 'bB' + 'aA'*2 + 'dD'*2
    paths = (no, yes, cfirst)
    assert len(set(paths)) == 3
    assert all('aab' not in s for s in paths)
    assert len(set(observe(s) for s in paths)) == 1
    assert observe(no) == (12,0,(0,0,0,0,0),(6,5,1),0)
    assert len(set(weight(s) for s in paths)) == 1
    assert [first_bc(s) for s in paths] == [0,1,2]
    output = lambda s: first_bc(s)==1
    assert [output(s) for s in paths] == [False,True,False]
    assert [output(s+'b') for s in paths] == [True,True,False]
    assert len(set(observe(s+'b') for s in paths)) == 1
    print('SMITH_NONPRIMITIVE_2_30',stats)
    print('SMITH_RANK1_DEFECT',assert_snf_case(M2,H2))
    print('SMITH_RANDOM_EXACT_CASES',cases,'seed=484','max_input_abs',peak)
    print('ORDER_FIBER',observe(no),'common_weight',weight(no))
    print('PATHS',paths)
    print('FIRST_BC_STATES',[first_bc(s) for s in paths])
    print('AFTER_APPEND_B',[output(s+'b') for s in paths])
    print('MIN_FUTURE_SAFE_CARRIER_STATES',3,'fixed_bits',2)
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    run()
