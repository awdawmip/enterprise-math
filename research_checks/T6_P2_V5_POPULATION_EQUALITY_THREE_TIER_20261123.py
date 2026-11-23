"""T6 exact v2(d)=5 population rigidity, three-tier exact finite audit.

Uses the seven necessary 64-gap cases from the earlier exhaustive first/two-tier
classification, then fully enumerates possible v2(d)=4 six-moment signatures
under each side's independent mass budget. A v2(d)=3 subgroup obstruction
excludes all seven cases. Standard Python integers; no sampling or floating point.
"""
from functools import lru_cache
from collections import deque
import heapq

K = tuple(range(1, 7))
MOD1 = tuple(1 << k for k in K)
MOD2 = tuple(1 << (2*k) for k in K)
MOD3 = tuple(1 << (3*k) for k in K)
ZERO = (0,) * 6

# (lighter v5 count, heavy nonzero excess parts, light nonzero excess parts,
#  heavy remaining mass, light remaining mass)
CASES = (
    (5, (), (14, 7, 1, 1, 1), 192, 640),
    (6, (), (14, 7, 1, 1, 1), 161, 609),
    (6, (1,), (14, 7, 1, 1, 1, 1), 97, 545),
    (7, (), (14, 7, 1, 1, 1), 130, 578),
    (7, (), (7, 6, 4, 4, 1, 1, 1), 130, 578),
    (8, (), (14, 7, 1, 1, 1), 99, 547),
    (8, (), (7, 6, 4, 4, 1, 1, 1), 99, 547),
)
EXPECTED = (
    (70, 8988, 629160, 147, 0),
    (43, 6886, 296098, 55, 0),
    (14, 3868, 54152, 2, 0),
    (25, 5185, 129625, 12, 0),
    (25, 5185, 129625, 8, 0),
    (14, 3927, 54978, 2, 0),
    (14, 3927, 54978, 3, 0),
)


def odd_profile(n, parts):
    assert len(parts) <= n
    return (1,) * (n-len(parts)) + tuple(2*x+1 for x in parts)


def six_signature(js, moduli):
    return tuple(sum(pow(j, -k, m) for j in js) % m
                 for k,m in zip(K, moduli))


@lru_cache(None)
def v4_options(max_cost):
    """Minimum mass for each complete six-coordinate signature modulo 2^(2k).

    Enumerating all nonnegative multisets by multiplicity recursion. Two such
    multisets with the same signature: keeping the cheaper one loses no
    possibility of extending it with a v3 correction under an upper budget.
    """
    options = {}
    weights = [(16*j-1, six_signature((j,), MOD2))
               for j in range(1, (max_cost+1)//16 + 1, 2)]

    def recurse(i, cost, vec):
        if i == len(weights):
            best = options.get(vec)
            if best is None or cost < best:
                options[vec] = cost
            return
        w,g = weights[i]
        while cost <= max_cost:
            recurse(i+1, cost, vec)
            cost += w
            vec = tuple((x+y)%m for x,y,m in zip(vec,g,MOD2))

    recurse(0, 0, ZERO)
    return options


def v3_group():
    generators = [six_signature((j,), MOD1) for j in range(1, 64, 2)]
    seen = {ZERO}
    queue = deque([ZERO])
    while queue:
        v = queue.popleft()
        for g in generators:
            w = tuple((x+y)%m for x,y,m in zip(v,g,MOD1))
            if w not in seen:
                seen.add(w)
                queue.append(w)
    assert len(seen) == 2048
    return seen


def main():
    G3 = v3_group()
    total_options = 0
    total_second_tier = 0

    for index, ((s, pa, pb, heavy_R, light_R), expected) in enumerate(
            zip(CASES, EXPECTED), start=1):
        a = six_signature(odd_profile(s+64, pa), MOD3)
        b = six_signature(odd_profile(s, pb), MOD3)
        fixed_delta = tuple((x-y)%m for x,y,m in zip(a,b,MOD3))
        heavy_v4 = v4_options(heavy_R)
        light_v4 = v4_options(light_R)
        tested = second_tier = third_tier_members = 0

        for va in heavy_v4:
            for vb in light_v4:
                tested += 1
                # Exact v5+v4 signed sixth moment after multiplying by 2^(5k).
                rem = tuple((d + (1<<k)*((x-y) % (1<<(2*k))))
                            % (1<<(3*k))
                            for d,x,y,k in zip(fixed_delta,va,vb,K))
                if any(r % (1 << (2*k)) for r,k in zip(rem,K)):
                    continue
                second_tier += 1
                # Required v3 signed inverse signature modulo 2^k.
                needed = tuple((- (r >> (2*k)))%(1<<k)
                               for r,k in zip(rem,K))
                if needed in G3:
                    third_tier_members += 1

        row = (len(heavy_v4), len(light_v4), tested,
               second_tier, third_tier_members)
        assert row == expected, (index,row,expected)
        total_options += tested
        total_second_tier += second_tier
        print(f"case={index} light_count={s} v4_heavy={row[0]} "
              f"v4_light={row[1]} examined={tested} "
              f"second_tier={second_tier} third_tier_group={third_tier_members}")

    assert total_options == 1348616
    assert total_second_tier == 229
    print("PASS: all 7 full-budget count-gap-64 cases excluded by third-tier "
          "v3 group; v5 populations must be equal")


if __name__ == "__main__":
    main()
