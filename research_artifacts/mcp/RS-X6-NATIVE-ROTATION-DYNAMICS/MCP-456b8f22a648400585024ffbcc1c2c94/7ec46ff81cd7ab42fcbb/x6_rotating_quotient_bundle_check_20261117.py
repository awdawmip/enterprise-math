"""Exact moving-kernel X6 signed-frame bundle tests; algebraic, not a native triadic event."""
from itertools import combinations, product
import random
N = 6
I = tuple(range(1, N + 1))

def generator(t):
    i, j, k = t
    g = list(I)
    g[i], g[j], g[k] = j + 1, k + 1, -(i + 1)
    return tuple(g)

def mv(g, x):
    y = [0] * N
    for i, u in enumerate(g):
        y[abs(u) - 1] += x[i] * (1 if u > 0 else -1)
    return tuple(y)

def mul(g, h):
    return tuple((1 if x > 0 else -1) * g[abs(x) - 1] for x in h)

def normalize(v):
    return v if v[-1] == 1 else tuple(-t for t in v)

def chart(v, z, m):
    assert v[-1] == 1 and all(abs(u) == 1 for u in v)
    return tuple(z[i] - v[i] * z[-1] for i in range(N - 1)), z[-1] % m

def section(v, rt):
    r, t = rt
    return tuple(r[i] + v[i] * t for i in range(N - 1)) + (t,)

def act(g, state, m):
    v, rt = state
    w = normalize(mv(g, v))
    return w, chart(w, mv(g, section(v, rt)), m)

def step(letter, state, m):
    v, rt = state
    d = [0] * N
    d[abs(letter) - 1] = 1 if letter > 0 else -1
    z = section(v, rt)
    return v, chart(v, tuple(z[i] + d[i] for i in range(N)), m)

rgen = [generator(t) for t in combinations(range(N), 3)]
rng = random.Random(20261117)
frame_set = {normalize(s) for s in product((-1, 1), repeat=N)}
assert len(frame_set) == 32
checks = 0
for m in (1, 2, 3, 5, 7):
    for v in frame_set:
        for _ in range(12):
            r = tuple(rng.randrange(-8, 9) for _ in range(N - 1))
            t = rng.randrange(m)
            z = section(v, (r, t))
            state = v, chart(v, z, m)
            g, h = rng.choice(rgen), rng.choice(rgen)
            assert act(mul(h, g), state, m) == act(h, act(g, state, m), m)
            k = rng.randint(-100, 100)
            shifted = tuple(z[i] + m * k * v[i] for i in range(N))
            gv = normalize(mv(g, v))
            assert chart(v, z, m) == chart(v, shifted, m)
            assert chart(gv, mv(g, z), m) == chart(gv, mv(g, shifted), m)
            letter = rng.choice(tuple(range(-6, 0)) + tuple(range(1, 7)))
            d = tuple(1 if letter == i + 1 else -1 if letter == -(i + 1) else 0 for i in range(N))
            transformed = mv(g, d)
            mapped = next((i + 1 if u == 1 else -(i + 1)) for i, u in enumerate(transformed) if u)
            assert act(g, step(letter, state, m), m) == step(mapped, act(g, state, m), m)
            checks += 1
assert 23040 // 32 == 720
print({"distinct_line_charts":len(frame_set), "stabilizer":720, "generated_C6":len(rgen), "checked_triplets":checks, "checks":"PASS"})
