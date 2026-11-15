"""Exact R004 p-adic named-future profile collision certificate: integer only."""
from itertools import product


def span(rows, modulus=4):
    out = {(0, 0)}
    for row in rows:
        out = {((a[0]+t*row[0])%modulus, (a[1]+t*row[1])%modulus)
               for a in out for t in range(modulus)}
    return out


def profile(A, B):
    U, V = span(A), span(A + B)
    sizes = []
    for power in (1, 2, 4):
        powerV = {((power*x[0])%4, (power*x[1])%4) for x in V}
        sub = {((u[0]+v[0])%4, (u[1]+v[1])%4)
               for u in U for v in powerV}
        assert len(sub) % len(U) == 0
        sizes.append(len(sub)//len(U))
    assert sizes[-1] == 1
    def log2_exact(n):
        assert n > 0 and (n & (n-1)) == 0
        return n.bit_length()-1
    return tuple(log2_exact(sizes[i]//sizes[i+1]) for i in (0,1))


def main():
    B = [(1,0),(0,1)]
    a1 = [(1,0)]
    a2 = [(0,1)]
    before1, before2 = profile(a1, B), profile(a2, B)
    after1, after2 = profile(a1+[(1,0)], B), profile(a2+[(1,0)], B)
    assert before1 == before2 == (1,1)
    assert after1 == (1,1) and after2 == (0,0)
    assert (1,0) in span(a1) and (1,0) not in span(a2)
    print("R004_P2_NAMED_FUTURE_PROFILE_COLLISION_PASS",
          before1, before2, after1, after2)


if __name__ == "__main__":
    main()
