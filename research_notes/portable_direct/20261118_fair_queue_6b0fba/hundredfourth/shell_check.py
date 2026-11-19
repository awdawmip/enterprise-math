"""Independent check of the radial action on named residue coordinates."""
import argparse
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import runpy


GROUP = tuple(permutations(range(4)))
ID = GROUP[0]
SIGNS = {g: (-1)**sum(g[i] > g[j] for i in range(4) for j in range(i+1, 4)) for g in GROUP}
PIN = "28f3000ea052b78b7b7ec3ba34c3d880ed98666b61eef2888d1890cd11e61b04"


def rad(x):
    return max(map(abs, x))


def own_move(n, depth, g, x):
    if rad(x) < n-depth+1:
        return x
    return tuple(SIGNS[g]*x[g.index(i)] for i in range(4))


def balls(n):
    return [v+(-sum(v),) for v in product(range(-n, n+1), repeat=3) if abs(sum(v)) <= n]


def obs(x, q):
    return tuple(v % q for v in x)


def theorem(n, t, q, g):
    return g == ID or q == 1 or t in (1, n+1) or q >= n+t


def all_gates(move):
    results = []
    for n in range(1, 6):
        points = balls(n)
        count = descends = single = 0
        for q in range(1, 2*n+3):
            read = [obs(x, q) for x in points]
            for t in range(1, n+2):
                for g in GROUP:
                    fibers = {}
                    scalars = [{} for _ in range(4)]
                    scalar_ok = [True]*4
                    ok = True
                    changed = False
                    for x, z in zip(points, read):
                        y = obs(move(n, n-t+1, g, x), q)
                        if fibers.setdefault(z, y) != y:
                            ok = False
                        changed |= y != z
                        for i in range(4):
                            scalar_ok[i] &= scalars[i].setdefault(z[i], y[i]) == y[i]
                    assert ok == theorem(n, t, q, g)
                    if t <= n:
                        assert changed == (q > 1 and g != ID)
                    for i in range(4):
                        predicted = q == 1 or t > n or (g[i] == i and (SIGNS[g] == 1 or q == 2 or t == 1))
                        assert scalar_ok[i] == predicted
                        single += 1
                    count += 1
                    descends += ok
        results.append([n, len(points), count, descends, single])
    return results


def fixed(z, q):
    return len(set(z)) == 1 and 2*z[0] % q == 0


def has_lift(z, q, r):
    for i in range(4):
        low = sum(-r+(x+r)%q for j, x in enumerate(z) if j != i)
        high = sum(r-(r-x)%q for j, x in enumerate(z) if j != i)
        for v in {-r, r}:
            if (v-z[i]) % q == 0 and low <= -v <= high and all(
                    -r+(x+r)%q <= r for j, x in enumerate(z) if j != i):
                return True
    return False


def shell_formula(q, r):
    d = len({r%q, -r%q})
    tuples_in = 1 if d == 1 else 6 + 2*int(4*r % q == 0)
    return 4*d*q*q - 6*d*d*q + 4*d**3 - tuples_in


def shells():
    summary = []
    for q in range(1, 15):
        residues = [z+(-sum(z)%q,) for z in product(range(q), repeat=3)]
        points = balls(q+2)
        actual = [set() for _ in range(q+3)]
        for x in points:
            actual[rad(x)].add(obs(x, q))
        failures = []
        increments = []
        for r, current in enumerate(actual):
            possible = [z for z in residues if any((v-r)%q == 0 or (v+r)%q == 0 for v in z)]
            assert len(possible) == shell_formula(q, r)
            by_lift = {z for z in possible if has_lift(z, q, r)}
            assert by_lift == current
            if len(current) != len(possible):
                failures.append(r)
            increments.append(len(current) - sum(fixed(z, q) for z in current))
        start = 0 if q==1 else (2 if q==4 else q-1)
        assert 1+max(failures, default=-1) == start
        per_period = sum(shell_formula(q, r) - int(2*r % q == 0) for r in range(q))
        summary.append(dict(q=q, first_stable_radius=start, bad_radii=failures,
                            increments= increments, stable_nonfixed_per_q_radii=per_period))
    return summary


def future_classes(move):
    swaps = ((1,0,2,3), (0,2,1,3), (0,1,3,2))
    records=[]
    for n in range(1, 6):
        points=balls(n)
        for q in range(1, 2*n+2):
            by_future, by_code = {}, {}
            erased = set()
            for x in points:
                z=obs(x, q)
                radius=rad(x)
                signature=(z,) + tuple(obs(move(n, d, g, x), q)
                                      for d in range(1, n+1) for g in swaps)
                code=(z, None if fixed(z, q) else radius)
                assert by_future.setdefault(signature, code) == code
                assert by_code.setdefault(code, signature) == signature
                erased.add((z, radius))
            records.append([n, q, len(by_code), len(erased)])
    return records


def scale_square(move):
    g=(0,2,1,3)
    cases=[]
    for n in range(1,5):
        b=balls(n)
        for d in range(1,n+1):
            for q in range(1,2*n+2):
                # Compare actual point images for a full shell to establish faithfulness.
                for r in range(1,n+1):
                    band=[x for x in b if rad(x)==r]
                    functions={tuple(obs(move(n,n,perm,x),q) for x in band) for perm in GROUP}
                    assert len(functions)==(1 if q==1 else 24)
                for gn in (ID, g):
                    for gp in (ID, g):
                        equal=all(obs(move(n+1,d,gp,x),q)==obs(move(n,d,gn,x),q) for x in b)
                        assert equal == (q==1 or (gn==ID and (d==1 or gp==ID)))
                cases.append([n,d,q])
    x=(2,-2,0,0)
    y=(-3,3,0,0)
    def pictures(m):
        return [obs(move(m,2,g,p),5) for p in (x,y)]
    low,upper=pictures(3),pictures(4)
    assert low[0]==low[1] and upper[0]!=upper[1]
    return dict(configurations=len(cases), joint_examples=4*len(cases),
                n3_depth2_q5={"input":[x,y],"lower":low,"upper":upper})


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo",type=Path,help="also use pinned original prefix_move for every case")
    args=ap.parse_args()
    move=own_move
    if args.repo:
        path=args.repo/"scripts/check_a3_recursive_shell_alignment_tomography.py"
        assert sha256(path.read_bytes()).hexdigest()==PIN
        move=runpy.run_path(str(path))["prefix_move"]
    print(json.dumps(dict(source_sha256=PIN,
                          gate_columns=["n","points","cases","descending","one_coordinate_cases"],gates=all_gates(move),
                          future_columns=["n","q","rotations_only","with_erasure"],
                          futures=future_classes(move),shells=shells(),square=scale_square(move)),
                     indent=2,sort_keys=True))


if __name__=="__main__":
    main()
