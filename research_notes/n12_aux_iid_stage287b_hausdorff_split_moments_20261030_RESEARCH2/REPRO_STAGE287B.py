#!/usr/bin/env python3
"""Stage287-B: exact ordered-path checks, Hausdorff moment examples.

Requires Python standard library only. All arithmetic is fractions.Fraction;
finite checks are NOT a proof of the all-real moment-cone theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations

P = {(0, 0): F(1, 16), (0, 1): F(3, 16),
     (1, 0): F(9, 16), (1, 1): F(3, 16)}
Q = {(0, 0): F(1, 9), (0, 1): F(2, 9),
     (1, 0): F(4, 9), (1, 1): F(2, 9)}
SOURCES = {'P': P, 'Q': Q}


def moment(atoms, n):
    """Unnormalized moments of a finite rational measure."""
    return [sum((w * y**j for w, y in atoms), F(0)) for j in range(n + 1)]


def determinant(mat):
    """Exact Fraction determinant by Gaussian elimination."""
    n = len(mat)
    if n == 0:
        return F(1)
    a = [row[:] for row in mat]
    sign = 1
    out = F(1)
    for k in range(n):
        piv = next((i for i in range(k, n) if a[i][k]), None)
        if piv is None:
            return F(0)
        if piv != k:
            a[k], a[piv] = a[piv], a[k]
            sign *= -1
        val = a[k][k]
        out *= val
        for i in range(k + 1, n):
            factor = a[i][k] / val
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
            a[i][k] = F(0)
    return sign * out


def is_psd(mat):
    """Small symmetric rational matrix: every principal minor >= 0."""
    if not mat:
        return True
    assert all(mat[i][j] == mat[j][i]
               for i in range(len(mat)) for j in range(len(mat)))
    return all(determinant([[mat[i][j] for j in subset] for i in subset]) >= 0
               for size in range(1, len(mat) + 1)
               for subset in combinations(range(len(mat)), size))


def hausdorff_matrices(m):
    n = len(m) - 1
    if n % 2 == 0:
        k = n // 2
        return (
            [[m[i + j] for j in range(k + 1)] for i in range(k + 1)],
            [[m[i + j + 1] - m[i + j + 2] for j in range(k)]
             for i in range(k)]
        )
    k = (n - 1) // 2
    return (
        [[m[i + j + 1] for j in range(k + 1)] for i in range(k + 1)],
        [[m[i + j] - m[i + j + 1] for j in range(k + 1)]
         for i in range(k + 1)]
    )


def solve_invertible(A, v):
    """Exact linear solve on examples with nonsingular principal blocks."""
    n = len(v)
    if not n:
        return []
    a = [list(A[i]) + [v[i]] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col]), None)
        assert piv is not None, 'Use PSD pseudoinverse/range form for singular blocks'
        a[col], a[piv] = a[piv], a[col]
        div = a[col][col]
        a[col] = [t / div for t in a[col]]
        for r in range(n):
            if r != col:
                coeff = a[r][col]
                a[r] = [x - coeff * y for x, y in zip(a[r], a[col])]
    return [a[i][-1] for i in range(n)]


def extension_interval(lower):
    """For present strictly nonsingular examples, determine next moment interval."""
    n = len(lower)  # extend s0...s_(n-1) by s_n
    if n % 2 == 0:  # n=2k
        k = n // 2
        A = [[lower[i + j] for j in range(k)] for i in range(k)]
        v = [lower[i + k] for i in range(k)]
        B = [[lower[i + j + 1] - lower[i + j + 2]
              for j in range(k - 1)] for i in range(k - 1)]
        w = [lower[i + k] - lower[i + k + 1] for i in range(k - 1)]
        d = lower[2 * k - 1]
    else:             # n=2k+1
        k = (n - 1) // 2
        A = [[lower[i + j + 1] for j in range(k)] for i in range(k)]
        v = [lower[i + k + 1] for i in range(k)]
        B = [[lower[i + j] - lower[i + j + 1]
              for j in range(k)] for i in range(k)]
        w = [lower[i + k] - lower[i + k + 1] for i in range(k)]
        d = lower[2 * k]
    L = sum((v[i] * solve_invertible(A, v)[i] for i in range(len(v))), F(0))
    U = d - sum((w[i] * solve_invertible(B, w)[i] for i in range(len(w))), F(0))
    assert L <= U
    return L, U


def word_probability(j, n, y):
    return y**j * (1 - y) if j < n else y**n


def leaf_dist(src, n, settings, adaptive=None):
    """Ordered leaves: keys (U,R,S,T,word,terminal). settings=(w,x,y).

    Adaptive test uses only x=0 and selects path-dependent y_(R,S).
    """
    out = defaultdict(F)
    for rs, src_mass in SOURCES[src].items():
        r, s = rs
        for w, x, y0 in settings:
            for u, uprob in ((0, 1-x), (1, x)):
                if uprob == 0:
                    continue
                y = adaptive[rs] if adaptive is not None else y0
                assert 0 <= y <= 1
                t = r ^ u
                for j in range(n+1):
                    word = (1,) * j + ((0,) if j < n else ())
                    term = 'STOP' if j < n else 'SURVIVE'
                    out[(u, r, s, t, word, term)] += src_mass*w*uprob*word_probability(j, n, y)
    assert sum(out.values(), F(0)) == 1
    assert all(w >= 0 for w in out.values())
    return dict(out)


def total_variation(a, b):
    return sum((abs(a.get(k,F(0))-b.get(k,F(0)))
                for k in set(a)|set(b)), F(0)) / 2


def project(d, erase_u=False, erase_t=False, erase_rs=False):
    out = defaultdict(F)
    for (u,r,s,t,word,term), w in d.items():
        key = ((None if erase_u else u),
               (None if erase_rs else r),
               (None if erase_rs else s),
               (None if erase_t else t),word,term)
        out[key] += w
    return dict(out)


def ordered_terminal_moments(d, n):
    # Full-ordered leaf mass conditional on one upstream U and all RS combined.
    ret={}
    for u in (0,1):
        categories=[]
        for j in range(n+1):
            word=(1,)*j + ((0,) if j<n else ())
            categories.append(sum((w for (uu,r,s,t,ww,term),w in d.items()
                                  if uu==u and ww==word),F(0)))
        ret[u]=categories
    return ret


def main():
    assert sum(P.values(),F(0)) == sum(Q.values(),F(0)) == 1
    # n=4 exact endpoint measures; first three moments identical.
    mu_L = [(F(1,2), F(1,4)), (F(1,2), F(3,4))]
    mu_H = [(F(1,8), F(0)), (F(3,4), F(1,2)), (F(1,8), F(1))]
    mL = moment(mu_L, 4)
    mH = moment(mu_H, 4)
    assert mL[:4] == mH[:4] == [F(1),F(1,2),F(5,16),F(7,32)]
    assert mL[4]==F(41,256) and mH[4]==F(11,64)
    L4,H4=extension_interval(mL[:4])
    assert (L4,H4)==(mL[4],mH[4])
    assert all(is_psd(M) for m in [mL,mH] for M in hausdorff_matrices(m))
    print('N4_INTERVAL',str(L4),str(H4),'WIDTH',str(H4-L4))

    # n=5 strictly interior lower moments, interval from rational Schur complements.
    mu_mid = [(F(1,4), F(1,4)), (F(1,4), F(3,4)),
              (F(1,16), F(0)), (F(3,8), F(1,2)), (F(1,16), F(1))]
    mm=moment(mu_mid,5)
    assert mm[:5]==[F(1),F(1,2),F(5,16),F(7,32),F(85,512)]
    assert mm[5]==F(137,1024)
    L5,H5=extension_interval(mm[:5])
    assert (L5,H5)==(F(271,2048),F(277,2048))
    assert L5 < mm[5] < H5
    assert all(is_psd(M) for M in hausdorff_matrices(mm))
    assert all(is_psd(M) for M in hausdorff_matrices(mm[:5]+[L5]))
    assert all(is_psd(M) for M in hausdorff_matrices(mm[:5]+[H5]))
    print('N5_INTERVAL',str(L5),str(H5),'WIDTH',str(H5-L5))

    # Rational degree-four data with ONLY irrational possible support:
    # roots of q(t)=t^2-t+1/8 are (1/2 +/- sqrt(2)/4).
    algmom=[F(1),F(1,2)]
    while len(algmom)<7:
        algmom.append(algmom[-1]-F(1,8)*algmom[-2])
    assert algmom[:5]==[F(1),F(1,2),F(3,8),F(5,16),F(17,64)]
    expectation_q_square = (algmom[4]-2*algmom[3]
        +F(5,4)*algmom[2]-F(1,4)*algmom[1]+F(1,64)*algmom[0])
    assert expectation_q_square==0
    assert all(is_psd(M) for M in hausdorff_matrices(algmom[:5]))
    print('N4_IRRATIONAL_ATOM_OBSTRUCTION', 'E[q(Y)^2]=0',
          'q=y^2-y+1/8', 'moments', ','.join(map(str,algmom[:5])))

    # Exact complete ordered path replay of n=4 endpoint strategies.
    # x=0 makes each m_j its own U=0 block, TV = |Delta m4|.
    sett_L = [(w,F(0),y) for w,y in mu_L]
    sett_H = [(w,F(0),y) for w,y in mu_H]
    for src in SOURCES:
        a=leaf_dist(src,4,sett_L)
        b=leaf_dist(src,4,sett_H)
        assert total_variation(a,b)==F(3,256)
        ca=ordered_terminal_moments(a,4)
        cb=ordered_terminal_moments(b,4)
        assert ca[0]==[mL[j]-mL[j+1] for j in range(4)]+[mL[4]]
        assert cb[0]==[mH[j]-mH[j+1] for j in range(4)]+[mH[4]]
        assert ca[1]==cb[1]==[F(0)]*5
        print(src,'N4_FULL_LEAF_TV',str(total_variation(a,b)),
              'positive_leaves',sum(w>0 for w in a.values()),sum(w>0 for w in b.values()))

    # Swapping X-dependent conditional Y distributions preserves the pooled
    # (R,S,word) but not (R,S,T,word). Dropping U *alone* keeps T=R xor U.
    swap_A = [(w/F(2),F(0),y) for w,y in mu_L] + \
             [(w/F(2),F(1),y) for w,y in mu_H]
    swap_B = [(w/F(2),F(0),y) for w,y in mu_H] + \
             [(w/F(2),F(1),y) for w,y in mu_L]
    for src in SOURCES:
        a=leaf_dist(src,4,swap_A)
        b=leaf_dist(src,4,swap_B)
        assert total_variation(a,b)==F(3,256)
        assert total_variation(project(a,erase_u=True),project(b,erase_u=True))==F(3,256)
        assert total_variation(project(a,erase_u=True,erase_t=True),
                               project(b,erase_u=True,erase_t=True))==0
        print(src,'U_ERASURE_T_RETAINED_TV',str(F(3,256)),
              'U_T_ERASED_TV',0)

    # Path-adaptive port parameter: source-blind rule but y chosen after RS.
    adapt_A = {(0,0):F(1,2),(0,1):F(1),(1,0):F(1,2),(1,1):F(0)}
    adapt_B = {(0,0):F(1,2),(0,1):F(0),(1,0):F(1,2),(1,1):F(1)}
    for src in SOURCES:
        for j in range(6):
            ma=sum((SOURCES[src][rs]*y**j for rs,y in adapt_A.items()),F(0))
            mb=sum((SOURCES[src][rs]*y**j for rs,y in adapt_B.items()),F(0))
            assert ma==mb
        a=leaf_dist(src,5,[(F(1),F(0),F(0))],adaptive=adapt_A)
        b=leaf_dist(src,5,[(F(1),F(0),F(0))],adaptive=adapt_B)
        expected=F(3,8) if src=='P' else F(4,9)
        assert total_variation(a,b)==expected
        # Final-all-success at the exact RS=(0,1) is a discriminating event.
        event=(0,0,1,0,(1,)*5,'SURVIVE')
        assert a.get(event,F(0))-b.get(event,F(0))==SOURCES[src][(0,1)]
        print(src,'ADAPTIVE_SAME_ALL_POOLED_MOMENTS_TV',str(expected),
              'RS01_EVENT_GAP',str(SOURCES[src][(0,1)]))

    print('STAGE287B_HAUSDORFF_SPLIT_MOMENT_EXACT_PASS')


if __name__=='__main__':
    main()
