"""Integer shears, endpoint moments and explicit equal-marginal mixtures."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json


def step(v, c):
    x, y = v
    return (x+y, y) if c == 'A' else (x, x+y)


def evaluate(word, v=(1, 1)):
    for c in word:
        v = step(v, c)
    return v


def decode(v):
    x, y = v
    suffix = []
    while x != y:
        if x > y:
            x -= y
            suffix.append('A')
        else:
            y -= x
            suffix.append('B')
    assert x == 1
    return ''.join(reversed(suffix))


def moments(v):
    x, y = v
    return (1, x, y, x*x, x*y, y*y)


def push(v, c):
    m, x, y, xx, xy, yy = v
    if c == 'A':
        return m, x+y, y, xx+2*xy+yy, xy+yy, yy
    return m, x, x+y, xx, xy+xx, yy+2*xy+xx


def addto(target, key, row, weight):
    v = target[key]
    for i, value in enumerate(row):
        v[i] += weight*value


def base_table():
    return defaultdict(lambda: [0]*6)


def transfers(weights):
    table = {0: list(moments((1, 1)))}
    for wa, wb in weights:
        new = base_table()
        for a, v in table.items():
            addto(new, a+1, push(v, 'A'), wa)
            addto(new, a, push(v, 'B'), wb)
        table = new
    return table


def exhaustive(weights):
    table = base_table()
    for letters in product('AB', repeat=len(weights)):
        w = ''.join(letters)
        v = evaluate(w)
        assert decode(v) == w
        weight = 1
        for c, pair in zip(w, weights):
            weight *= pair[int(c == 'B')]
        addto(table, w.count('A'), moments(v), weight)
    return table


def subseqs(w, k):
    coeff = {'': 1}
    for c in w:
        for s, n in list(coeff.items()):
            if len(s) < k:
                coeff[s+c] = coeff.get(s+c, 0)+n
    return coeff


def solve(columns, rhs):
    n = len(columns)
    a = [list(map(Fraction, row)) + [Fraction(y)] for row,y in zip(zip(*columns),rhs)]
    det = 1
    for i in range(n):
        j = next(j for j in range(i,n) if a[j][i])
        if j != i:
            a[i], a[j] = a[j], a[i]
            det = -det
        e = a[i][i]
        det *= e
        a[i] = [x/e for x in a[i]]
        for j in range(n):
            if i != j:
                e = a[j][i]
                a[j] = [x-e*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a], int(det)


def mixture_paths():
    words = ['AAABBB','AABABB','AABBAB','AABBBA','ABAABB','ABABAB']
    rows = [moments(evaluate(w)) for w in words]
    _, det = solve(rows, (1,0,0,0,0,0))
    # Four short histories and their A/B reflections. The opposite endpoint
    # cancels the global moments because the moment differences are symmetric.
    changes = {}
    for w, k in zip(('ABABB','ABBBA','BAABB','BABBA'),(-1,1,1,-1)):
        changes[w] = k
        changes[w.translate(str.maketrans('AB','BA'))] = -k
    endpoint = base_table()
    for w,k in changes.items():
        addto(endpoint, w.count('A'), moments(evaluate(w)), k)
    assert endpoint[2] == [0,-2,-2,-40,-30,-40]
    assert endpoint[3] == [-v for v in endpoint[2]]
    return {'rank_basis':words, 'moment_determinant':det, 'signed_changes':changes,
            'endpoint_moment_changes':dict(endpoint)}


def main():
    for n in range(12):
        weights = [(2+i%5, 1+(i*i)%7) for i in range(n)]
        assert transfers(weights)==exhaustive(weights)
    a,b = 'A','B'
    obstruction=[]
    for k in range(1,8):
        a,b = a+b,b+a
        assert subseqs(a,k)==subseqs(b,k) and evaluate(a)!=evaluate(b)
        obstruction.append({'order':k, 'length':len(a),'point':evaluate(a)})
    d0,d1=0,2
    for m in range(1,21):
        x,y=evaluate('ABBA'*m)
        assert x-y == d1
        d0,d1=d1,6*d1-d0
    print(json.dumps({'exhaustive_depths':list(range(12)),'ordered_subsequence_examples':obstruction,
                      'balanced_degree_two_example':mixture_paths(),
                      'exact_two_letter_outputs':{w:evaluate(w) for w in ['AB','BA','ABBA','BAAB']}},indent=2))


if __name__ == '__main__':
    main()
