"""Exact finite checks and log-domain asymptotic diagnostics, Python standard library."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from math import ceil, cos, exp, isqrt, log, pi, sqrt, tan
from pathlib import Path

source = Path(__file__).resolve().parents[1] / "ninetyeighth" / "collisions_check.py"
assert sha256(source.read_bytes()).hexdigest() == "6f678e9da4558badd2d0d4a5fe137f3c9a045fecbea2b13c40a09cb8512d72a2"
spec = spec_from_file_location("elastic", source)
elastic = module_from_spec(spec)
spec.loader.exec_module(elastic)


def axes(masses, length):
    m1, m2, m3 = masses
    c = Fraction(2*m1, m1+m2)
    d = Fraction(2*m3, m2+m3)
    x, y = 1, 1
    for _ in range(length):
        x, y = x*(c*x/y).denominator, y*(d*y/x).denominator
    if length:
        assert x*y == c.denominator*d.denominator*(c*d).denominator**(length-1)
    return x, y


def check_lattices():
    calls = Counter()
    counts = [0, 0, 0]
    for masses in product(range(1, 8), repeat=3):
        for length in range(1, 11):
            x, y = axes(masses, length)
            counts[0] += 1
            if length <= 4 and max(x,y) <= 12:
                for i,j in product(range(x+1),range(y+1)):
                    measured = elastic.all_words_safe((i+j,j,0), masses, length, calls)
                    assert measured == (i % x == 0 and j % y == 0)
                    counts[1] += 1
                counts[2] += 1
    return {"index_cases": counts[0], "direct_starting_pairs": counts[1],
            "direct_mass_depth_cases": counts[2], "direct_gate_calls": dict(calls)}


def exponent(u, v, sign):
    # Divide by 1+sign*sqrt(-2) using its conjugate.
    k = 0
    while (u+2*sign*v) % 3 == 0 and (v-sign*u) % 3 == 0:
        u, v = (u+2*sign*v)//3, (v-sign*u)//3
        k += 1
    return k


@lru_cache(None)
def states(n):
    if n < 1:
        return ()
    return tuple((u,v) for v in range(-isqrt(n//2), isqrt(n//2)+1)
                 for u in range(-isqrt(n-2*v*v), isqrt(n-2*v*v)+1) if u or v)


def word_range(word):
    pos = bottom = top = 0
    for gate in word:
        pos += 1 if pos % 2 == gate else -1
        top, bottom = max(top,pos), min(bottom,pos)
    return top//2, -(bottom//2)


def direct_word(u, v, word):
    speeds = (v+u, v-u, -v)
    for gate in word:
        speeds = elastic.contact(speeds, (1,1,2), gate, integer=True)
        if speeds is None:
            return False
    return True


@lru_cache(None)
def path_counts(e, t):
    counts = [1]*(2*e+2)
    for _ in range(t):
        counts = [a+b for a,b in zip([0]+counts, counts[1:]+[0])]
    return counts


def spectral(e, t):
    h = 2*e+3
    return 2/(h*(h-1))*sum(cos(pi*r/h)**t / tan(pi*r/(2*h))**2
                              for r in range(1,h,2))


def check_walk():
    limit = 140
    starts = states(limit)
    by_shell, by_time = Counter(), Counter()
    for u,v in starts:
        i, j = exponent(u,v,1), exponent(u,v,-1)
        by_shell[(u*u+2*v*v, i,j)] += 1
    for t in range(8):
        for word in product(range(2), repeat=t):
            a,b = word_range(word)
            eligible = 0
            for u,v in starts:
                actual = direct_word(u,v,word)
                assert actual == (exponent(u,v,1) >= a and exponent(u,v,-1) >= b)
                eligible += actual
            assert eligible == len(states(limit//3**(a+b)))
            by_time[t] += eligible
        predicted = sum(c*path_counts(i+j,t)[2*j] for (_,i,j),c in by_shell.items())
        assert predicted == by_time[t]
    layer_windows = 0
    for bound in range(1,limit+1):
        direct = Counter(exponent(u,v,1)+exponent(u,v,-1) for u,v in states(bound))
        for e in range(max(direct)+1):
            reduced_bound = bound//(3**e)
            no_three = (len(states(reduced_bound))-2*len(states(reduced_bound//3))
                        +len(states(reduced_bound//9)))
            assert direct[e] == (e+1)*no_three
            layer_windows += 1
    counts_by_norm = Counter(u*u+2*v*v for u,v in starts)
    for n in range(1,limit+1):
        assert elastic.norm_representations(n) == counts_by_norm[n]
    for e,t in product(range(12), range(40)):
        h = 2*e+3
        exact = sum(path_counts(e,t))/((h-1)*2**t)
        assert abs(spectral(e,t)-exact) < 1e-13
        assert sum(x*(h-x) for x in range(1,h,2))*6 == ((h-1)//2)*h*(h+1)
    return {"energy_bound":limit, "named_states":len(starts),
            "direct_state_word_checks": len(starts)*255, "joint_survivor_counts":dict(by_time),
            "exact_walk_vs_sine_cases":480, "exact_finite_disk_layer_sizes":layer_windows,
            "dirichlet_norm_coefficients":limit}


def mixture_log(t):
    # At large t, paired modes other than r=1 are exponentially small near the saddle.
    # Keep all signed modes using principal-eigenvalue rescaling.
    a = log(3)
    saddle = (pi*pi*t/(4*a))**(1/3)
    logs = []
    for e in range(ceil(4*saddle)+20):
        h = 2*e+3
        leading = cos(pi/h)
        scaled = sum((cos(pi*r/h)/leading)**t/tan(pi*r/(2*h))**2
                     for r in range(1,h,2))
        logs.append(log(4*(e+1)/9) - a*e + log(2*scaled/(h*(h-1))) + t*log(leading))
    m = max(logs)
    return m + log(sum(exp(y-m) for y in logs))


@lru_cache(None)
def disk_size(bound):
    side = isqrt(bound//2)
    return sum(2*isqrt(bound-2*v*v)+1 for v in range(-side,side+1))-1


def oscillation():
    # At theta=log_3 h (h=1 or 2), kappa=2. B(Y)<=N(Y)<=7Y for Y>=1.
    def prime_free(bound):
        return disk_size(bound)-2*disk_size(bound//3)+disk_size(bound//9)

    endpoints = {}
    depth = 18
    for h in (1,2):
        low = sum(Fraction(prime_free(h*3**j), h*h*9**j) for j in range(depth+1))
        high = low+Fraction(7,2*h*3**depth)
        endpoints[h] = [str(low), str(high)]
    jumps = [prime_free(2*3**j)-prime_free(2*3**j-1) for j in range(depth+1)]
    assert jumps == [2]+[0]*depth
    return {"phases_log3_h":endpoints, "depth":depth, "jump_at_log3_2":"1/2"}


def main():
    samples = []
    for t in (1000, 10000, 100000, 1000000):
        a = log(3)
        kappa = 1.5*(pi*pi*a*a/4)**(1/3)
        predicted = log(16*sqrt(2*pi)/(3*pi*a)) + log(t)/2 - kappa*t**(1/3)
        samples.append([t,round(exp(mixture_log(t)-predicted),7)])
    return {"supercritical_F2_exact_bounds": oscillation(), "finite_lattices": check_lattices(), "exit_walk":check_walk(),
            "infinite_disk_survival_over_asymptotic_numerical": samples}


if __name__ == "__main__":
    print(json.dumps(main(),sort_keys=True,indent=2))
