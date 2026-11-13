# Affine Euclidean divisors: eventual quasipolynomiality and static CRT-rank support

Date: 2026-11-14  
Status: **Driver auxiliary exact theorem with finite regression; not a native Result/review/CLAIM**  
Context: N-coupled Result `RR-13ED25CE1AA8899BCFEC`; original mathematical authors `EM-NCAS1-5F7A3C` and integrity re-freeze author `EM-NCASR2-C9BCF9` retained. Present additional deduction: existing `EM-DVR-DEBB5E` Driver context, not independent of the shared record.

## 1. Theorem

Fix a finite straight-line integer program in the public positive integer `N`. Registers begin with `N` and fixed integers. Operations are `+`, `-`, `*`, and any finite nesting of Euclidean quotient or remainder by fixed affine-positive divisors `aN+b`, with `a,b` fixed integers, `a>=0`, and `aN+b>0` on every admitted input. The case `a=0,b>0` includes constant divisors. Matrices of fixed dimensions have entries computed by this grammar. An arbitrary global selector may pick one of finitely many fixed matrix-output leaves, but may not inject additional computed numeric operands.

For every admitted `N=pq` with distinct odd primes, there is a finite precomputable set `C` of positive integers, depending only on the program, such that unequal ranks of any selected output matrix over `F_p` and `F_q` imply that for some `c in C`,

`1<gcd(N,c)<N.`

There is a corresponding fixed finite set `S` of primes such that for `p,q notin S` **every leaf** has equal hidden-channel ranks. In particular, adding a *fixed number* of division/remainder operations by `N+c` or `aN+b` cannot create a rank-asymmetry mechanism with unbounded fresh prime support.

This statement concerns only the displayed finite grammar. It admits no division by an arbitrary computed divisor, unbounded iteration, independently chosen hidden-CRT leaves, or external factor-bearing initialization.

## 2. Eventual rational quasipolynomial lemma

An integer-valued expression `E(n)` is *eventually rational quasipolynomial* when some period `M>=1` and threshold `n_0` exist with rational polynomials `P_r(X) in Q[X]`, `0<=r<M`, such that `E(n)=P_r(n)` for every `n>=n_0` of residue `r mod M`.

**Lemma.** Every register in the grammar above is eventually rational quasipolynomial.

Proof by induction on the finite program. Fixed integers and `n` are polynomials; `+,-,*` preserve the class after common period/threshold refinement.

Consider dividing a numerator `E(n)=P_r(n)` on residue class `r mod M` by a fixed affine divisor `an+b`, which is positive on the admitted inputs. For `a=0` the constant-divisor periodic-remainder proof applies: if a common coefficient denominator of `P_r` is `L`, refinement to period `MLb` makes `P_r(n) mod b` constant on each class, so quotient and remainder are rational polynomials there.

For `a>0`, polynomial division over `Q[X]` gives

`P_r(X)=(aX+b)Q_r(X)+h_r,`

with `Q_r in Q[X]` and `h_r in Q` a constant. Choose common positive coefficient denominator `L` for the finitely many `Q_r`. On residue classes modulo `H=ML`, the fractional part `theta_s={Q_r(n)}` is constant: the difference `Q_r(n)-Q_r(s)` is an integer whenever `n==s mod H`. But

`P_r(n)/(an+b)=Q_r(n)+h_r/(an+b).`

For `n` sufficiently large, the final term is smaller in absolute value than the positive distance between each nonzero `theta_s` and an integer boundary, and less than 1 when `theta_s=0`. Therefore on each class the floor is exactly:

- `Q_r(n)-theta_s` for `theta_s>0`;
- `Q_r(n)-1` for `theta_s=0,h_r<0`;
- `Q_r(n)` for `theta_s=0,h_r>=0`.

Each is a rational polynomial in `n`. The Euclidean remainder is `P_r(n)-(an+b)floor(P_r(n)/(an+b))`, hence also eventually rational quasipolynomial. Finitely many classes and operations yield a finite effective common threshold and period. QED.

The lemma covers genuinely non-ring integer rounding by divisors growing linearly with `N`. It makes no approximation and does not assume the floor identity at exceptional small inputs.

## 3. Exact CRT support proof

For each fixed output leaf and residue `r`, let `P_{l,r}(N)` be its eventual matrix of rational polynomials. Clear all their finitely many coefficient denominators with a fixed integer `L>0`, and put

`B_{l,r}(X)=L P_{l,r}(X) in Mat(Z[X]),`
`A_{l,r}=B_{l,r}(0) in Mat(Z).`

On each residue class and every sufficiently large `N`, `B_{l,r}(N)-A_{l,r}` is divisible entrywise by `N`. Thus for `N=pq` with `p,q not dividing L`, the channel ranks of the actual output equal those of the reductions of the **fixed** integer matrix `A_{l,r}`.

If the ranks are `u<v`, the positive `v`-th determinantal divisor `Delta_v(A_{l,r})` is divisible by the lower-rank prime and not by the other. Its gcd with `N` is therefore a proper factor. If one of `p,q` divides `L`, that prime itself can be included as a fixed precomputable witness. Add to `C` (i) all nonzero determinantal divisors of all `A_{l,r}`, (ii) the individual prime divisors of `L`, and (iii) the prime divisors of the finitely many **admitted semiprimes below the common threshold**. The last group legitimately handles every small exceptional input without extending an eventual identity backward. All items are fixed and effectively computable from the finite program.

For primes outside the finite support of `C`, each `A_{l,r}` attains its rational rank at both primes, because its top nonzero determinantal divisor is invertible there. Every leaf therefore has matching ranks. This proves the theorem. A fixed support list may be very large; no practical running-time guarantee is being claimed.

## 4. Exact example with two genuinely variable divisors

Take

`U(N)=floor((N^2+1)/(N+1)),`
`f(N)=floor(U(N)/4)+1,`
`g(N)=(N^2+7) mod (N+2),`
`D(N)=diag(f(N),g(N)).`

Polynomial division gives `N^2+1=(N+1)(N-1)+2`, so `U(N)=N-1` for `N>=2`. Similarly `N^2+7=(N+2)(N-2)+11` and `g(N)=11` for `N>=10`. All distinct odd-prime semiprimes are at least 15. On `r=N mod 4` with `s=(r-1) mod 4`,

`4D(N)=diag(N+(3-s),44)`,

so the integral specialization is `A_r=diag(3-s,44)`. For `N=143=11*13`, `D(143)=diag(36,11)` and `A_3=diag(1,44)`. The output ranks are 1 modulo 11 and 2 modulo 13, and `gcd(143,44)=11` is the static witness. The fact that the quotients were by `N+1` and `N+2` does not alter this classification.

## 5. Executed deterministic regression

This Python 3 check has the exact domain of all 120 products of distinct odd primes below 60 (16 primes). It tests the residue identity and the full unequal-rank implication for the displayed diagonal matrix:

```python
from itertools import combinations
from math import gcd

primes = [p for p in range(3, 60, 2)
          if all(p % d for d in range(3, int(p**0.5)+1, 2))]

def numeric(n):
    u = (n*n + 1) // (n + 1)
    return u // 4 + 1, (n*n + 7) % (n + 2)

def static(n):
    return 3 - ((n % 4 - 1) % 4), 44

checked = unequal = witnessed = 0
for p, q in combinations(primes, 2):
    n = p*q
    x, y = numeric(n)
    a, b = static(n)
    assert (4*x-a) % n == 0 and (4*y-b) % n == 0
    rank_p = (x%p != 0) + (y%p != 0)
    rank_q = (x%q != 0) + (y%q != 0)
    checked += 1
    if rank_p != rank_q:
        unequal += 1
        assert any(1 < gcd(n, c) < n
                   for c in (2, gcd(abs(a), abs(b)), abs(a*b)))
        witnessed += 1
print(len(primes), checked, unequal, witnessed)
```

Actual exact-integer output: `16 120 21 21`. The finite regression checks this example; the theorem for all admitted inputs is established by Sections 2–3.

## 6. Scientific relationship and open scope

The [fixed-divisor theorem](2026-11-14_ncoupled_fixed_divisor_euclidean_quasipolynomial_crt_support.md) proved **exact** quasipolynomiality on all inputs. This theorem extends it to **eventual** quasipolynomiality with fixed affine divisors in the public `N`, including `N+c`, while treating finitely many early exceptions exactly. It preserves the prior fixed-ring-term and finite-leaf theorems and original contributions; no new Result, CLAIM, Native review, Task completion or parent closure is asserted.

The meaningful surviving semantic frontier includes genuinely computed non-affine divisors, numeric input introduced outside the finite straight-line grammar, growing-time iteration, and operators coupling residue channels beyond this finite-support class.
