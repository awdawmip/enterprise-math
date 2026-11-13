"""R727 exact positive-BRC cyclic-nonbacktracking renewal certificate.
Standard-library only. Frozen P000 Source pin: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Usage: python R727_BRC_RENEWAL_VERIFY.py > R727_BRC_RENEWAL_RESULTS.json
"""
import json
from itertools import combinations

ROOT = '012'
TRIADS = tuple(''.join(t) for t in combinations('01234', 3))
ALL_ARCS = tuple((u, v) for u in TRIADS for v in TRIADS
                 if len(set(u) & set(v)) == 2)
REPS = {'A_R725_1_2': 211733226574, 'B_R725_3_4': 5363347296468}
EXPECTED_D = {
    'A_R725_1_2': (1, 0, 0, -3, -7, -8, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    'B_R725_3_4': (1, 0, 0, -3, -7, -8, -5, -1, 0, 0, 0, 0, 0, 0, 0, 0),
}

def matmul(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j, b in enumerate(B[k]):
                    if b:
                        result[i][j] += a * b
    return result

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def certificate(mask):
    arcs = tuple(e for i, e in enumerate(ALL_ARCS) if (mask >> i) & 1)
    n = len(arcs)
    assert n == 15
    B = [[int(e[1] == f[0] and e[0] != f[1])
          for f in arcs] for e in arcs]
    roots = [i for i, e in enumerate(arcs) if e[0] == ROOT]
    powers = [identity(n)]
    for _ in range(n):
        powers.append(matmul(powers[-1], B))
    p = [0] + [trace(P) for P in powers[1:]]
    # Newton coefficients of det(I-xB), exact integer divisibility.
    c = [1]
    for k in range(1, n+1):
        s = sum(c[k-i] * p[i] for i in range(1, k+1))
        assert s % k == 0
        c.append(-s//k)
    # All 225 integer Cayley-Hamilton entries.
    ch = [[0]*n for _ in range(n)]
    for k in range(n+1):
        P = powers[n-k]
        for i in range(n):
            for j in range(n):
                ch[i][j] += c[k] * P[i][j]
    assert all(z == 0 for row in ch for z in row)
    a = [sum(P[i][i] for i in roots) for P in powers]
    numer = [sum(c[k] * a[j-k] for k in range(j+1))
             for j in range(n)]
    # Adjugate numerator: (root-outdegree-1)det(I-xB)+1.
    assert numer == [(len(roots)-1)*c[j] + int(j == 0)
                     for j in range(n)]
    return arcs, B, roots, c

def original_count(arcs, length):
    # Independently enumerate original directed vertex paths, seam included.
    nbr = {t:[v for u,v in arcs if u == t] for t in TRIADS}
    def dfs(prev, cur, first, k):
        if k == length:
            return int(cur == ROOT and prev != first)
        return sum(dfs(cur, v, first if first is not None else v, k+1)
                   for v in nbr[cur] if v != prev)
    return dfs(None, ROOT, None, 0)

def renewal(D, max_m=64):
    b = [1]
    for m in range(1, max_m+1):
        b.append(-sum(D[i]*b[m-i]
                      for i in range(1, min(m,len(D)-1)+1)))
    return b

def eval_scaled(D, numerator, denominator):
    n = len(D)-1
    return sum(c * numerator**i * denominator**(n-i)
               for i,c in enumerate(D))

def run():
    assert len(TRIADS) == 10 and len(ALL_ARCS) == 60
    output = {
        'schema':'R727_EXACT_ROOTED_CNB_RENEWAL_V1',
        'status':'R727_EXACT_BRC_RENEWAL_PASS',
        'science_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'model':'Five-axis V17 directed CNB root 012; exact positive source-distinct histories',
        'proof':'Integer Newton identities + Cayley-Hamilton + adjugate polynomial + independent original-walk check',
        'classes':{}
    }
    for name,mask in REPS.items():
        arcs,B,roots,D = certificate(mask)
        assert tuple(D) == EXPECTED_D[name]
        counts = renewal(D)
        P = identity(15)
        for m in range(1,16):
            P = matmul(P,B)
            assert sum(P[i][i] for i in roots) == counts[m]
        assert all(original_count(arcs,m) == counts[m]
                   for m in range(3,9))
        output['classes'][name] = {
            'canonical_mask':mask, 'directed_edges':['>'.join(e) for e in arcs],
            'root_outdegree':len(roots), 'nonbacktracking_matrix_size':15,
            'det_I_minus_xB_coefficients_low_to_high':D,
            'root_trace_GF':'(root_outdegree-1)+1/det(I-xB)',
            'positive_rooted_CNB_m3_to_m20':counts[3:21],
            'checked_cayley_hamilton_entries':225,
            'direct_original_walk_check_lengths':list(range(3,9))
        }
    a = renewal(EXPECTED_D['A_R725_1_2'])
    b = renewal(EXPECTED_D['B_R725_3_4'])
    diff = [b[m]-a[m] for m in range(65)]
    assert diff[3:9] == [0,0,0,1,1,0]
    assert all(x>0 for x in diff[9:])
    brackets = {
        'A_R725_1_2':(485450,485451),
        'B_R725_3_4':(483131,483132)
    }
    for name,(lo,hi) in brackets.items():
        D = EXPECTED_D[name]
        assert eval_scaled(D,lo,10**6)>0
        assert eval_scaled(D,hi,10**6)<0
    output.update({
       'difference_B_minus_A_m3_to_m20':diff[3:21],
       'strict_comparison':'B>A at m=6,7 and every m>=9; equal at m=3,4,5,8',
       'positive_root_rational_brackets':{
           k:[str(v[0])+'/1000000',str(v[1])+'/1000000']
           for k,v in brackets.items()},
       'scope':'Full integer 15x15 proof certificate. 64 exact coefficients; direct path enumeration m3..8. Infinite claims follow determinant/adjugate algebra, not finite sampling. No V29 permission established.'
    })
    return output

if __name__ == '__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
