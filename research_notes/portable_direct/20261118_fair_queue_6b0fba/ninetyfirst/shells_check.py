"""Finite signed cubic-lattice seeds. Exact ball polynomials and shortest-word EGFs."""
import argparse
from collections import Counter, deque
from fractions import Fraction
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json


def axis_step(x, i, sign):
    return x[:i] + (x[i] + sign,) + x[i + 1:]


def combine(p, q):
    out = Counter()
    for (j, a), w in p.items():
        for (k, b), v in q.items():
            out[j + k, a + b] += w * v
    return {key: v for key, v in out.items() if v}


def one_axis(a, outward, delta, last=0):
    # The keys (j,k) encode t^k e^(jt). delta is the signed clamped displacement.
    h = int(last != 0)
    p = Counter()
    if a >= h and (not last or last * delta > 0):
        p[0, a-h] += Fraction(1, factorial(a-h))
    rays = len(outward) if not last else int(last in outward)
    p[1, 0] += rays
    for k in range(a+1-h):
        p[0, k] -= Fraction(rays, factorial(k))
    return {key: v for key, v in p.items() if v}


def coefficient(p, r):
    value = sum(v * comb(r, k) * factorial(k) * j**(r-k)
                for (j, k), v in p.items() if k <= r)
    assert int(value) == value
    return int(value)


def distances(seed, y):
    return [sum(abs(a-b) for a, b in zip(y, s)) for s in seed]


def native_bfs(seed, radius):
    d = len(seed[0])
    distance = dict.fromkeys(seed, 0)
    words = dict.fromkeys(seed, 1)
    queue = deque(seed)
    shell = [0]*(radius+1)
    total = [0]*(radius+1)
    order = [(i, j) for i in range(d) for j in (-1, 1)]
    edges = [[0]*(2*d) for _ in shell]
    last = [[0]*(2*d) for _ in shell]
    flat = [[0]*d for _ in shell]
    while queue:
        x = queue.popleft()
        r = distance[x]
        if r > radius:
            continue
        shell[r] += 1
        total[r] += words[x]
        for k, (i, sign) in enumerate(order):
            y = axis_step(x, i, sign)
            if y not in distance:
                distance[y] = r+1
                words[y] = 0
                queue.append(y)
            if distance[y] == r+1:
                edges[r][k] += 1
                last[r][k] += words[x]
                words[y] += words[x]
            if distance[y] == r and sign == 1:
                flat[r][i] += 1
    return shell, total, edges, last, flat


def full_formula(seed, radius, directional):
    d = len(seed[0])
    low, high = tuple(map(min, zip(*seed))), tuple(map(max, zip(*seed)))
    box = list(product(*(range(a,b+1) for a,b in zip(low,high))))
    metrics = {y: distances(seed,y) for y in box}
    nearest = {y: min(row) for y,row in metrics.items()}
    cover = max(nearest.values())
    balls = [0]*(radius+1)
    edges = [[0]*(2*d) for _ in balls]
    flat = [[0]*d for _ in balls]
    expansion = Counter()
    finals = [Counter() for _ in range(2*d)]
    for y in box:
        rays = [tuple(j for j,c in ((-1,low[i]),(1,high[i])) if y[i]==c)
                for i in range(d)]
        q = nearest[y]
        # Each chosen nonempty ray has positive radial displacement. The count
        # for the ball, with l chosen axes, is binom(r-q,l).
        def choose_rays(excluded=-1):
            coeffs = [1]
            for i, signs in enumerate(rays):
                if i != excluded:
                    coeffs = [a+b for a,b in zip(coeffs+[0],[0]+[len(signs)*v for v in coeffs])]
            return coeffs
        c = choose_rays()
        for r in range(q,radius+1):
            balls[r] += sum(v*comb(r-q,l) for l,v in enumerate(c))
        for j,s in enumerate(seed):
            if metrics[y][j] != q:
                continue
            shifts = tuple(y[i]-s[i] for i in range(d))
            factors = [one_axis(abs(a), rays[i], a) for i,a in enumerate(shifts)]
            all_axes = {(0,0):1}
            for f in factors:
                all_axes = combine(all_axes, f)
            expansion.update(all_axes)
            if directional:
                for i,a in enumerate(shifts):
                    others = {(0,0):1}
                    for h,f in enumerate(factors):
                        if h!=i:
                            others = combine(others, f)
                    for b,sign in enumerate((-1,1)):
                        factor = one_axis(abs(a),rays[i],a,sign)
                        finals[2*i+b].update(combine(others,factor))
        if directional:
            for i in range(d):
                c = choose_rays(i)
                for r in range(q,radius+1):
                    lft = r-q
                    # Holding y_i fixed gives a sphere in the other fibres.
                    sphere = int(lft==0)
                    if lft:
                        sphere += sum(v*comb(lft-1,l-1) for l,v in enumerate(c) if l)
                    for b,sign in enumerate((-1,1)):
                        if sign in rays[i]:
                            # A half-infinite outward edge family beginning at this face.
                            edges[r][2*i+b] += sum(v*comb(lft,l) for l,v in enumerate(c))
                        else:
                            diff = nearest[axis_step(y,i,sign)]-q
                            if diff==1:
                                edges[r][2*i+b] += sphere
                            if diff==0 and sign==1:
                                flat[r][i] += sphere
    expansion = {k:v for k,v in expansion.items() if v}
    signs = list(product((-1,1),repeat=d))
    faces = [[sum(i*j for i,j in zip(e,s)) for s in seed] for e in signs]
    top = sum(row.count(max(row)) for row in faces)
    assert expansion[d,0] == top
    width = max(b-a for a,b in zip(low,high))
    assert max((a for j,a in expansion if j==d-1), default=0)<=max(0,width-1)
    total = [coefficient(expansion,r) for r in range(radius+1)]
    shell = [b-a for a,b in zip([0]+balls, balls)]
    last = [[coefficient(p,r) for p in finals] for r in range(radius+1)] if directional else []
    return (shell,total,edges,last,flat), expansion, top, cover, sum(map(max,faces))


def inspect(seed, radius, directional=True):
    seed = sorted(set(seed))
    if not seed or not seed[0] or radius < 0 or len({len(s) for s in seed}) != 1:
        raise ValueError("a finite nonempty seed of consistent positive dimension and a nonnegative radius are required")
    d = len(seed[0])
    expected = native_bfs(seed,radius)
    formula, expansion, top, cover, support_sum = full_formula(seed,radius,directional)
    assert expected[:2]==formula[:2]
    if directional:
        assert expected[2:]==formula[2:]
        for r in range(radius):
            assert sum(formula[3][r])==formula[1][r+1]
    balls = []
    for a in formula[0]:
        balls.append(a + (balls[-1] if balls else 0))
    # Two finite differences at radii >= the covering radius of the box.
    if radius>=cover+d:
        line=balls[cover:]
        for _ in range(d-1):
            line=[b-a for a,b in zip(line,line[1:])]
        for i,value in enumerate(line):
            assert value==2**d*(cover+i)+2**(d-1)*d+support_sum
    return {"d":d,"seed":seed,"radius":radius,"volume":balls,"shell":formula[0],
            "words":formula[1],"word_expansion":[[j,a,str(v)] for (j,a),v in sorted(expansion.items())],
            "support_sum":support_sum,"word_leading":top,"box_covering_radius":cover,
            "positive_negative_order":"axis index, sign minus then plus",
            "outgoing_edges":formula[2],"last_direction_words":formula[3],"flat_edges":formula[4]}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    tests=0
    grid=list(product(range(3),repeat=2))
    for mask in range(1,1<<len(grid)):
        seed=[s for j,s in enumerate(grid) if mask>>j&1]
        inspect(seed,5,False)
        tests+=1
    examples={"degenerate_line":([(0,),(4,),(7,)],12),
              "two_diagonal_ends":([(0,0),(2,-2)],8),
              "diagonal_with_midpoint":([(0,0),(1,-1),(2,-2)],8),
              "sharp_w4":([(0,0,0),(4,2,0)],9),
              "skew_three_d":([(-1,0,0),(1,0,1),(0,2,-1),(0,-1,2)],7),
              "legacy_pair_6":([(0,)*6,(1,0,0,0,0,0)],4),
              "legacy_elbow_6":([(0,)*6,(1,0,0,0,0,0),(1,1,0,0,0,0)],4)}
    rows={name:inspect(seed,radius) for name,(seed,radius) in examples.items()}
    assert rows["legacy_pair_6"]["shell"]==[2,22,122,462,1362]
    assert rows["legacy_elbow_6"]["words"]==[3,32,314,2846,23990]
    assert rows["legacy_elbow_6"]["last_direction_words"][-1]==[15119,12496,12496,15119]+[16819]*8
    assert rows["two_diagonal_ends"]["volume"][2:]==rows["diagonal_with_midpoint"]["volume"][2:]
    assert [2,3,"2/3"] in rows["sharp_w4"]["word_expansion"]
    result={"all_nonempty_seeds_of_3x3_grid":tests,"grid_radius":5,
            "cross_checks":"independent signed native BFS for shell and words, all edge and last-direction counts in named examples",
            "examples":rows}
    content=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.out is None: print(content,end="")
    else: args.out.write_text(content)


if __name__=="__main__":
    main()
