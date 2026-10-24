"""Independent no-SymPy rational/DP check for R261 x=2 Hankel witness."""
from collections import defaultdict
from fractions import Fraction as F
import json

states = ((0, 0), (0, 2), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
edge = {
    0: ((2, -1, -1), (2, +1, -1)),
    1: ((0, -1, -1), (0, +1, -1)),
    2: ((1, +1, +1), (2, +1, -1))
}

def monitor(r, a):
    return ((1, 2, 2) if a == 0 else (0, 0, 2))[r]

def qpow(k):
    return F(2**k) if k >= 0 else F(1, 2**(-k))

def det_fraction(mat):
    work = [[F(v) for v in row] for row in mat]
    result = F(1)
    for j in range(len(work)):
        pivot = next((i for i in range(j, len(work)) if work[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            work[pivot], work[j] = work[j], work[pivot]
            result = -result
        diag = work[j][j]
        result *= diag
        for i in range(j + 1, len(work)):
            if work[i][j]:
                ratio = work[i][j] / diag
                for k in range(j+1, len(work)):
                    work[i][k] -= ratio * work[j][k]
                work[i][j] = F(0)
    return result

def main():
    # Method A: direct positive-integer histogram propagation, not an affine matrix implementation.
    counts = {(0, 0, +1, 0): 1}
    source_values = []
    forget_values = []
    for n in range(25):
        source_values.append(sum((qpow(k) * c for (q,r,eps,k), c in counts.items()
                                  if q == 0 and r == 2 and eps == 1), F(0)))
        forget_values.append(sum(c for (q,r,eps,k),c in counts.items()
                                 if q == 0 and r == 2 and eps == 1))
        assert sum(counts.values()) == (1 << n)
        nxt = defaultdict(int)
        for (q,r,eps,k),c in counts.items():
            for a in (0,1):
                q1,eta,b = edge[q][a]
                nxt[(q1,monitor(r,a),eta*eps,eta*k+b)] += c
        counts = dict(nxt)
    # Method B: independent linear Fourier/channel propagation at x=2.
    idx = {state:i for i,state in enumerate(states)}
    vector = [F(0)] * 14
    vector[0] = F(1)
    lifted_values = []
    for n in range(25):
        lifted_values.append(vector[2*idx[(0,2)]])
        nxt = [F(0)] * 14
        for src,(q,r) in enumerate(states):
            for a in (0,1):
                q1,eta,b = edge[q][a]
                dest = idx[(q1,monitor(r,a))]
                if eta == 1:
                    nxt[2*dest] += qpow(b) * vector[2*src]
                    nxt[2*dest+1] += qpow(-b) * vector[2*src+1]
                else:
                    nxt[2*dest] += qpow(b) * vector[2*src+1]
                    nxt[2*dest+1] += qpow(-b) * vector[2*src]
        vector = nxt
    assert source_values == lifted_values
    H = [[source_values[i+j] for j in range(13)] for i in range(13)]
    det = det_fraction(H)
    assert det == F(163341851565859597265625,1099511627776)
    H11 = [[F(forget_values[i+j]) for j in range(11)] for i in range(11)]
    assert det_fraction(H11) == F(151782400)
    print(json.dumps({
       'status':'PASS','method':'integer histogram vs independent Fraction channel transfer',
       'depths_compared':'0..24','specialization':'x=2',
       'hankel_det':f'{det.numerator}/{det.denominator}',
       'hankel_order':13,'forget_translation_x1_order':11,
       'forget_translation_x1_hankel_11_det':'151782400','terms':'q=0, r=2, parity=+, each raw word has weight 1'
    },indent=2))

if __name__=='__main__':
    main()
