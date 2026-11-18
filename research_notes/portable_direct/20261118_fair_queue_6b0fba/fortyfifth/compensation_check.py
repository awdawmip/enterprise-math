"""Exact finite prime-ideal and local-factor checks for the compensation calculation."""
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial, isqrt, exp
import hashlib
import json

SOURCE_SHA256 = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
ONE = (F(1), F(0))
ZERO = (F(0), F(0))


def add(u, v):
    return u[0] + v[0], u[1] + v[1]


def scale(c, u):
    return c * u[0], c * u[1]


def sub(u, v):
    return add(u, scale(-1, v))


def mul(u, v):
    a, b = u
    c, d = v
    return a*c - b*d, a*d + b*c - b*d


def conj(u):
    return u[0] - u[1], -u[1]


def div(u, v):
    norm = mul(v, conj(v))
    assert norm[1] == 0 and norm[0]
    return scale(1 / F(norm[0]), mul(u, conj(v)))


def power(u, n):
    out = ONE
    for _ in range(n):
        out = mul(out, u)
    return out


def is_prime(n):
    return n >= 2 and all(n % k for k in range(2, isqrt(n) + 1))


def ideals(P, modulus):
    # Primary and congruent to 1 mod modulus. Norm >= 3*max(a*a,b*b)/4.
    bound = 2 * isqrt(2 * P) + 2
    idx = lambda r: range(-bound + (bound+r) % modulus, bound+1, modulus)
    out = []
    for a, b in product(idx(1), idx(0)):
        Q = a*a - a*b + b*b
        if P < Q < 2*P and (is_prime(Q) or (b == 0 and is_prime(abs(a)) and abs(a)%3 == 2)):
            out.append((a, b, Q))
    return sorted(out, key=lambda r: (r[2], r[0], r[1]))


def partitions(sequence):
    if not sequence:
        yield ()
        return
    i, *rest = sequence
    for parts in partitions(rest):
        yield ((i,),) + parts
        for j, block in enumerate(parts):
            yield parts[:j] + ((i,)+block,) + parts[j+1:]


def injective_mobius(rows):
    n = len(rows[0])
    ans = ZERO
    for parts in partitions(list(range(len(rows)))):
        term = ONE
        for block in parts:
            total = ZERO
            for p in range(n):
                v = ONE
                for i in block:
                    v = mul(v, rows[i][p])
                total = add(total, v)
            coeff = (-1)**(len(block)-1) * factorial(len(block)-1)
            term = mul(term, scale(coeff, total))
        ans = add(ans, term)
    return ans


def injective_direct(rows):
    total = ZERO
    for assignment in permutations(range(len(rows[0])), len(rows)):
        v = ONE
        for i, p in enumerate(assignment):
            v = mul(v, rows[i][p])
        total = add(total, v)
    return total


def local_factor(prime, sigma, eta):
    a, b, Q = prime
    d = F(eta, Q**sigma)
    h = F(1, Q)
    R = scale(F(1, Q**(6*sigma)), power(conj((a,b)),6))  # eta is real quadratic or trivial.
    # Uncontracted j=0 row from the source, including all marked/rescaled signs.
    raw_star = add(scale(1/(1-h), sub(scale(1-h, R), scale(d*(Q-1)*h*h, ONE))),
                   add(scale(-d,ONE), scale(h,R)))
    raw_star = div(raw_star, sub(ONE,R))
    raw = add(scale((1+h)/(1-h),ONE), raw_star)
    raw_B = sub(scale(1/d, div(raw_star,raw)), scale(h, ONE))
    H = scale((1-h)**2/(1-d),raw)
    G = scale(1/(1-d),sub(scale((1/d-h)*(1-h)**2,raw_star),scale(h*(1-h*h),ONE)))
    assert G == mul(H,raw_B)
    J = sub(scale(1-(1-h)*d,ONE), scale(h,R))
    delta = div(scale(1-h,add(scale((1-h)*d,ONE),scale(h-1/d,R))),J)
    assert delta == sub(scale(-1,raw_B),ONE)
    return add(ONE,delta)


def draw_prob(weights):
    total = sum(weights)
    return [F(w,total) for w in weights]


def no_collision(prob, K):
    # Ordered, identically distributed draws. Newton-free elementary symmetric DP.
    e = [F(1)] + [F(0)]*K
    for w in prob:
        for k in range(K,0,-1):
            e[k] += w*e[k-1]
    return factorial(K)*e[K]


def wire(u):
    return [str(x) for x in u]


def main():
    P = 3500
    sites = ideals(P,36)
    assert len(sites)==5 and len(set(q for _,_,q in sites))==3
    rows = []
    profiles = (lambda y: F(1), lambda y: y, lambda y: 2-y, lambda y: 1+y)
    for profile in profiles:
        weights = [profile(F(q,P)) for _,_,q in sites]
        rows.append(draw_prob(weights))
    data, contracted = [], 0
    for sigma, twist in product([1,2],["principal","Legendre5_norm"]):
        factors = [local_factor(p,sigma,1 if twist=="principal" or p[2]%5 in (1,4) else -1) for p in sites]
        assert all(p[2]%5 for p in sites)
        # Each local Gaussian norm factor is verified against G/H in Q(omega).
        for k in range(1,5):
            clean = [[scale(w, ONE) for w in row] for row in rows[:k]]
            full = [[scale(w, t) for w,t in zip(row,factors)] for row in rows[:k]]
            assert injective_direct(clean) == injective_mobius(clean)
            actual = injective_direct(full)
            assert actual == injective_mobius(full)
            contracted += 1
        norm_counts = {}
        for site,w in zip(sites,rows[0]):
            norm_counts[site[2]] = norm_counts.get(site[2],0) + w
        clean4 = injective_direct(clean)
        assert clean4[0]>0 and no_collision(list(norm_counts.values()),4)==0
        assert actual[1]==0
        data.append(dict(sigma=sigma,eta=twist,distinct_vs_independent_weight=wire(clean4),
                         inserted_divided_by_distinct=wire(div(actual,clean4))))
    w = draw_prob([p[2] for p in sites])
    lam = sum(x*x for x in w)
    assert no_collision(w,2)==1-lam
    enlarged=[]
    for p0 in [3500,10000,50000,200000]:
        ps=ideals(p0,36)
        mu=draw_prob([p[2] for p in ps])
        v2=sum(x*x for x in mu)
        K=max(2,isqrt(int(1/v2)))
        exact=no_collision(mu,K)
        lam2=K*(K-1)*v2/2
        enlarged.append(dict(P=p0,prime_ideals=len(ps),rational_norms=len({q for _,_,q in ps}),
                             K=K,birthday_lambda=str(lam2),no_collision_decimal=float(exact),
                             poisson_decimal=exp(-float(lam2)),
                             exact_fraction_sha256=hashlib.sha256(str(exact).encode()).hexdigest()))
    print(json.dumps(dict(frozen_external_paper_sha256=SOURCE_SHA256,
                          full_ray_modulus=36,ray_class_number=108,annulus=[P,2*P],
                          ideals=sites,primewise_local_checks=4*len(sites),
                          direct_vs_partition_comparisons=2*contracted,
                          ray_sample=data,identical_windows=enlarged),indent=2,sort_keys=True))


if __name__=="__main__":
    main()
