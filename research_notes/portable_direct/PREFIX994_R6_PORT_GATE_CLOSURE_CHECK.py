"""PREFIX-994 exact rational reproducer.

Scope: PREFIX-993's six-port positive Schur kernel coupled to native positive
X6 Cell-axis steps. cap2 / no-repeat are explicitly auxiliary gates; neither
is asserted as an actual native Link/Port occupancy axiom.

Run: python PREFIX994_R6_PORT_GATE_CLOSURE_CHECK.py
Uses only Python standard library (Fraction, Counter, json).
"""
from fractions import Fraction as Q
from collections import Counter
from pathlib import Path
import json

m = 6
kappa = (0, 0, 1, 1, 0, 1)
rho = (1, 2, 1, 2, 3, 3)
X = ((1, 2, 1, 3, 2, 4), (2, 1, 3, 1, 4, 2))
F = tuple(tuple(Q(v, 5000) for v in row) for row in X)
R = tuple(tuple(Q(rho[h]) if kappa[h] == c else Q(0)
                for c in range(2)) for h in range(m))
W = tuple(tuple(Q(rho[h])*F[kappa[h]][j] for j in range(m))
          for h in range(m))
zero = (0,)*m

def identity(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))

def product(A, B):
    return tuple(tuple(sum((A[i][t]*B[t][j] for t in range(len(B))), Q())
                       for j in range(len(B[0]))) for i in range(len(A)))

def inverse(M):
    n = len(M)
    E = identity(n)
    a = [list(M[i])+list(E[i]) for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        v = a[j][j]
        a[j] = [x/v for x in a[j]]
        for i in range(n):
            if i != j:
                v = a[i][j]
                a[i] = [a[i][k]-v*a[j][k] for k in range(2*n)]
    return tuple(tuple(row[n:]) for row in a)

def minus_from_identity(M):
    E = identity(len(M))
    return tuple(tuple(E[i][j]-M[i][j] for j in range(len(M)))
                 for i in range(len(M)))

def partition(M):
    result = []
    for h in range(len(M)):
        for block in result:
            k = block[0]
            if all(M[h][a]*M[k][b] == M[h][b]*M[k][a]
                   for a in range(len(M[0])) for b in range(len(M[0]))):
                block.append(h)
                break
        else:
            result.append([h])
    return result

S = product(F, R)
small_inverse = inverse(minus_from_identity(S))
Wp = product(product(R, small_inverse), F)
I = identity(m)
Ws = tuple(tuple(I[i][j]+Wp[i][j] for j in range(m)) for i in range(m))
assert Ws == inverse(minus_from_identity(W))
assert Wp == product(W, inverse(minus_from_identity(W)))
assert S == ((Q(11,5000), Q(19,5000)), (Q(2,625), Q(11,5000)))
assert max(map(sum, W)) == Q(39,5000)
assert max(map(sum, Wp)) < 1
assert Wp[0] == tuple(Q(a,24889817) for a in
                      (5027,9997,5046,14986,10054,19994))
assert partition(W) == [[0,1,4],[2,3,5]]
assert partition(Wp) == [[0,1,4],[2,3,5]]
assert partition(Ws) == [[h] for h in range(m)]

# Counterexample: the auxiliary restriction prohibits the immediately
# repeated incoming port. The exact outgoing supports distinguish all six.
G = tuple(tuple(Q() if h == j else W[h][j] for j in range(m))
          for h in range(m))
assert partition(G) == [[h] for h in range(m)]
assert W[0][0] == Q(1,5000)
assert G[0][0] == 0 and G[1][0] == Q(2,5000)

# Exact native X6 positive-coordinate path stress test with another auxiliary
# rule: no positive coordinate may be incremented more than twice.
def gate(z, j): return z[j] < 2
def step(z, j): return z[:j]+(z[j]+1,)+z[j+1:]

def direct(h, n):
    d = Counter({(zero,h,Q(1)):1})
    for _ in range(n):
        nxt = Counter()
        for (z,last,wt),cnt in d.items():
            for j in range(m):
                if gate(z,j):
                    nxt[(step(z,j),j,wt*W[last][j])] += cnt
        d = nxt
    return d

def class_transfer(h, n):
    if n == 0:
        return Counter({(zero,h,Q(1)):1})
    d = Counter({(zero,kappa[h],Q(1)):1})
    for _ in range(n-1):
        nxt = Counter()
        for (z,c,wt),cnt in d.items():
            for j in range(m):
                if gate(z,j):
                    nxt[(step(z,j),kappa[j],wt*rho[j]*F[c][j])] += cnt
        d = nxt
    out = Counter()
    for (z,c,wt),cnt in d.items():
        for j in range(m):
            if gate(z,j):
                out[(step(z,j),j,wt*rho[h]*F[c][j])] += cnt
    return out

def statistics(d):
    return dict(
        path_count=sum(d.values()),
        exact_mass=str(sum((wt*cnt for (_z,_j,wt),cnt in d.items()), Q())),
        distinct_endpoint_terminal_weight=len(d),
        distinct_weights=len({wt for (_z,_j,wt) in d})
    )

samples = {}
for h in range(m):
    for n in range(8):
        d = direct(h,n)
        assert d == class_transfer(h,n), (h,n)
        assert all(sum(z) == n for z,_j,_wt in d)
        if n == 7:
            assert sum(d.values()) == 128520
    if h in (0,1,2):
        samples[str(h)] = {str(n): statistics(direct(h,n)) for n in (5,7)}

# Histogram-semiring multiplication: a coefficient is a Counter of exact
# positive rational monomials with natural-number path multiplicities.
one = Counter({Q(1):1})
def hmul(a,b):
    out = Counter()
    for x,n in a.items():
        for y,k in b.items():
            out[x*y] += n*k
    return out

def hmatrix(A,B):
    return [[sum((hmul(A[i][t],B[t][j]) for t in range(len(B))),
                 Counter()) for j in range(len(B[0]))]
            for i in range(len(A))]

H = [[Counter({W[i][j]:1}) for j in range(m)] for i in range(m)]
RH = [[Counter({Q(rho[h]):1}) if kappa[h] == c else Counter()
       for c in range(2)] for h in range(m)]
FH = [[Counter({F[c][j]:1}) for j in range(m)] for c in range(2)]
SH = hmatrix(FH, RH)
large = [[one.copy() if i == j else Counter() for j in range(m)]
         for i in range(m)]
small = [[one.copy() if i == j else Counter() for j in range(2)]
         for i in range(2)]
path_counts = {}
for n in range(1,7):
    large = hmatrix(large,H)
    assert large == hmatrix(hmatrix(RH,small),FH), n
    path_counts[str(n)] = sum(sum(x.values()) for x in large[0])
    small = hmatrix(small,SH)
assert path_counts['6'] == m**6

certificate = {
    'schema': 'PREFIX994_R6_GATE_CLOSURE_EXACT_V1',
    'proof_status': 'AUTHOR_ANALYTIC_PROOF_EXACT_FRACTION_CHECKED_NOT_REVIEWED',
    'source_prior': 'PREFIX993 at 45b71416907502e0f12a29b3d2ed30705fe45fc1',
    'frozen_P000_V5': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
    'native_scope': 'positive native X6 Cell steps, WBRC Schur port weights; cap2/no-repeat are synthetic auxiliary gates',
    'port_count':m, 'class_count':2, 'kappa':kappa, 'rho':rho,
    'FR': [[str(x) for x in row] for row in S],
    'inverse_I_minus_FR': [[str(x) for x in row] for row in small_inverse],
    'max_row_sum_W':str(max(map(sum,W))),
    'original_partition':partition(W),
    'positive_closure_partition':partition(Wp),
    'kleene_star_partition':partition(Ws),
    'Wplus_first_row':[str(x) for x in Wp[0]],
    'no_repeat_partition':partition(G),
    'no_repeat_one_step_contrast':{
        'h0_j0':str(G[0][0]), 'h1_j0':str(G[1][0]),
        'original_h0_j0':str(W[0][0])
    },
    'histogram_matrix_identity_checked_lengths':[1,6],
    'histogram_matrix_path_counts_from_h0':path_counts,
    'cap2_full_endpoint_terminal_exact_weight_histogram_checked_lengths':[0,7],
    'cap2_checked_initial_histories':list(range(m)),
    'cap2_samples':samples,
    'mathematical_admission':'NOT_REVIEWED',
    'remaining':'Obtain and type the actual native X6 Link/Port occupancy relation; test availability fibers.'
}
if __name__ == '__main__':
    output = Path(__file__).with_name('PREFIX994_R6_EXACT_RESULTS.json')
    output.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',
                      encoding='utf-8')
    print('PASS: six-port positive closure, star/synthetic gate split')
    print('PASS: six histories n=0..7 full gated X6 endpoint/terminal/weight histograms')
    print('PASS: exact histogram-semiring matrix factorization n=1..6')
    print(json.dumps({'FR':certificate['FR'],'samples':samples},ensure_ascii=False))
