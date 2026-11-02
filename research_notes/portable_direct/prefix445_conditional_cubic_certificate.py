"""PREFIX-445: exact two-sector conditional cubic BRC closure certificate.

Scientific axes: native signed X6 first-axis restricted source words.
Positive rational branch weights; no floating-point arithmetic.
The pinned original signed_brc.py is injected beside this script from the
verified, byte-exact source artifact (blob 300a96e3dc24bf6fff73743037a0347a8bc83176).
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import hashlib
import importlib.util

THIS = Path(__file__).resolve()
CANDIDATES = (
    THIS.parents[2] / 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py',
    THIS.with_name('pinned_signed_brc.py'),
)
SOURCE = next((p for p in CANDIDATES if p.is_file()), None)
if SOURCE is None:
    raise FileNotFoundError('frozen signed_brc.py missing: use pinned checkout or evidence pack')
RAW = SOURCE.read_bytes()
SOURCE_BLOB = hashlib.sha1(b'blob ' + str(len(RAW)).encode() + b'\0' + RAW).hexdigest()
assert SOURCE_BLOB == '300a96e3dc24bf6fff73743037a0347a8bc83176', SOURCE_BLOB
spec = importlib.util.spec_from_file_location('pinned_signed_brc', SOURCE)
pinned = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pinned)
endpoint_multiplicity = pinned.endpoint_multiplicity

Witness = tuple[int, ...]
A7: Witness = (0, 3, 3, 3, 4, 4, 4, 7)
B7: Witness = (1, 2, 2, 2, 5, 5, 5, 6)


def bag(ks: Witness) -> dict[int, F]:
    out = defaultdict(F)
    for k in ks:
        out[k] += F(1)
    return dict(out)


def moments(n: int, bag_counts: dict[int, F]):
    t = [[F(0) for _ in range(4)] for _ in range(2)]
    for k, c in bag_counts.items():
        assert c > 0 and 0 <= k <= n
        x = n - 2 * k
        for j in range(4):
            t[k % 2][j] += c * x**j
    return t


def J(n: int, c: dict[int, F]):
    t = moments(n, c)
    return tuple(t[r][j] for r in range(2) for j in range(3)) + (t[0][3]+t[1][3],)


def Jplus(n: int, c: dict[int, F]):
    t = moments(n, c)
    return tuple(t[r][j] for r in range(2) for j in range(4))


def kernel(n: int, c: dict[int, F], a: tuple[F, F], b: tuple[F, F]):
    """One step: (+) k->k, (-) k->k+1, weights depend on incoming k mod 2."""
    out = defaultdict(F)
    for k, w in c.items():
        r = k % 2
        out[k] += a[r]*w
        out[k+1] += b[r]*w
    return dict(out)


def expected_Jplus(n: int, c: dict[int, F], a, b):
    t = moments(n, c)
    z = [[F(0)]*4 for _ in range(2)]
    binom = ((1,), (1, 1), (1, 2, 1), (1, 3, 3, 1))
    for s in (0, 1):
        for j in range(4):
            z[s][j] = sum(F(binom[j][q]) * (a[s]*t[s][q] + (-1)**(j-q)*b[1-s]*t[1-s][q]) for q in range(j+1))
    return tuple(z[r][j] for r in range(2) for j in range(4))


def expected_J_under_equal_mass(n: int, c: dict[int, F], a, b):
    m0, m1 = a[0]+b[0], a[1]+b[1]
    assert m0 == m1
    p = expected_Jplus(n, c, a, b)
    return p[:3] + p[4:7] + (p[3]+p[7],)


def validate_word_capacity(n: int, ks: Witness):
    from collections import Counter
    for k, count in Counter(ks).items():
        z = (n-2*k, 0, 0, 0, 0, 0)
        capacity = endpoint_multiplicity(n, z)
        assert count <= capacity, (n,k,count,capacity)
        assert capacity >= comb(n,k)


def check():
    a_bad = (F(2,3), F(1,2))
    b_bad = (F(3,5), F(1,3))
    m0, m1 = a_bad[0]+b_bad[0], a_bad[1]+b_bad[1]
    assert (m0, m1, m0-m1) == (F(19,15),F(5,6),F(13,30))
    a_good = (F(2,3), F(1,2))
    b_good = (F(3,5), F(23,30))
    assert a_good[0]+b_good[0] == a_good[1]+b_good[1]
    checks=0
    for n in range(7, 27):
        validate_word_capacity(n, A7)
        validate_word_capacity(n, B7)
        ac,bc=bag(A7),bag(B7)
        assert J(n,ac) == J(n,bc)
        va,vb=moments(n,ac),moments(n,bc)
        assert va[0][3]-vb[0][3] == 384
        assert va[1][3]-vb[1][3] == -384
        ao,bo=kernel(n,ac,a_bad,b_bad),kernel(n,bc,a_bad,b_bad)
        assert J(n+1,ao)[-1]-J(n+1,bo)[-1] == 384*(m0-m1) == F(832,5)
        ag,bg=kernel(n,ac,a_good,b_good),kernel(n,bc,a_good,b_good)
        assert J(n+1,ag) == J(n+1,bg)
        assert J(n+1,ag) == expected_J_under_equal_mass(n,ac,a_good,b_good)
        for c in (ac,bc):
            for aa,bb in ((a_bad,b_bad),(a_good,b_good)):
                assert Jplus(n+1,kernel(n,c,aa,bb)) == expected_Jplus(n,c,aa,bb)
                checks += 1
    weights=(F(1,7),F(2,3),F(4,5))
    # 3^4 positive kernels and 6 nonuniform finite bags; exact two-step composition.
    for a0,a1,b0,b1 in product(weights,repeat=4):
        aa=(a0,a1);bb=(b0,b1)
        for n,ks in ((7,A7),(7,B7),(9,(0,3,3,6,6,9)),(9,(1,2,2,7,7,8)),(14,(0,6,8,14)),(14,(2,2,12,12))):
            c=bag(ks)
            nxt=kernel(n,c,aa,bb)
            assert Jplus(n+1,nxt)==expected_Jplus(n,c,aa,bb)
            nxt2=kernel(n+1,nxt,bb,aa)
            assert Jplus(n+2,nxt2)==expected_Jplus(n+1,nxt,bb,aa)
            checks += 2
    print('PREFIX445 EXACT PASS')
    print('pinned_signed_brc source blob='+SOURCE_BLOB)
    print('witness_n=7..26 (20 lengths), branch_capacity=PASS')
    print('J(A)=J(B)=TRUE; delta_sector_cubics=(384,-384)')
    print('conditional mass=(19/15,5/6); delta_m=13/30; delta_U3_after=832/5')
    print('equal-mass conditional update conserves J for the two witnesses')
    print('exact Jplus step checks='+str(checks)+' (20*2*2 + 3^4*6*2)')
    print('all arithmetic Python int/Fraction; no float')

if __name__ == '__main__':
    check()
