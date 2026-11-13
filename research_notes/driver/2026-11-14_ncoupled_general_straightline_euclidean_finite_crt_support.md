# N-coupled: every fixed straight-line Euclidean integer circuit has finite CRT-rank support

Date: 2026-11-14  
Status: **Driver auxiliary exact mathematical theorem, with a finite reproducible regression; no new frozen Result, native review, CLAIM, Task completion or parent closure.**  
Source lineage: original `G_poly-loc` mathematics by `EM-NCAS1-5F7A3C`, immutable integrity re-freeze by `EM-NCASR2-C9BCF9` (`RR-13ED25CE1AA8899BCFEC`). This additional theorem was derived in the ongoing shared `EM-DVR-DEBB5E` Driver context, not a blind independent verification.

## 1. Complete statement

Fix any **finite straight-line integer circuit** `G` in one nonnegative public integer input `N`. Its initial registers consist only of `N` and finitely many fixed integer constants; each additional register is computed by one of

`x+y, x-y, xy, floor(x/y), rem(x,y)=x-y floor(x/y)`,

where **`y` may be the value of any earlier register**, not necessarily a constant, affine function, or polynomial in `N`. Assume every executed quotient/remainder divisor is a strictly positive integer for all sufficiently large positive `N`. All programs and register dimensions are fixed independently of `N`. Negative dividends are allowed (floor-based Euclidean convention). A finite list of fixed-dimensional integer output matrices may be populated by registers of such circuits. An otherwise arbitrary selector may choose a single whole matrix leaf from this fixed finite list for each public `N`, without injecting fresh numerical data.

**Theorem.** There exists an effectively computable finite list `C_G` of positive integers, independent of `N` and of hidden factors, such that for every `N=pq`, where `p` and `q` are distinct odd primes and all circuit operations are defined,

`rank_Fp(M_{sigma(N)}(N)) != rank_Fq(M_{sigma(N)}(N))`

implies that some `c in C_G` gives a proper ordinary factor

`1 < gcd(N,c) < N.`

There also exists a finite prime set `S_G`, determined solely by `G`, for which every leaf and output matrix has equal hidden-channel ranks whenever both `p` and `q` lie outside `S_G`. Thus **arbitrary computed numerical Euclidean divisors** inside a *fixed finite* circuit do not by themselves escape static CRT determinantal support.

The theorem is an exact mathematical classification of this circuit class, not an efficiency statement about computing the finite list. It leaves circuits with an input-dependent number of operations, unbounded state, non-arithmetic primitives, factor-bearing external inputs, and hidden-CRT-local leaf selection outside this class.

## 2. Closure of eventual rational quasipolynomials under arbitrary computed divisors

Call an integer-valued function `f(n)` *eventually rational quasipolynomial* (EQP) if some positive integer `M`, threshold `n_0`, and rational polynomials `P_0,...,P_{M-1}` satisfy

`f(n)=P_r(n)` for all `n>=n_0` with `n == r mod M`.

**Lemma.** If `f` and `g` are EQP and `g(n)>0` for every sufficiently large integer `n`, then `floor(f(n)/g(n))` and its Euclidean remainder `f(n)-g(n)floor(f(n)/g(n))` are also EQP.

**Proof.** Refine to a common period `M` and threshold. For a fixed residue `r`, write `f(n)=P_r(n)` and `g(n)=Q_r(n)` with `P_r,Q_r in Q[X]`. Because `g(n)>0` eventually, `Q_r` is not identically zero and is eventually positive on its progression. Polynomial division over `Q[X]` provides

`P_r(X) = H_r(X)Q_r(X) + R_r(X),`

with `H_r,R_r in Q[X]` and either `R_r=0` or `deg R_r < deg Q_r`. (When `Q_r` is a nonzero constant, take `R_r=0`.) Thus

`P_r(n)/Q_r(n)=H_r(n)+epsilon_r(n),    epsilon_r(n)=R_r(n)/Q_r(n) -> 0`

along that progression; the sign of nonzero `epsilon_r(n)` also stabilizes because `R_r` and `Q_r` are fixed polynomials.

Choose a positive integer `L` clearing all coefficients' denominators of the finitely many quotient polynomials `H_r`. Refining the period to `M L` makes the fractional part `theta_s={H_r(n)}` constant on each finer residue `s`: for `n==s mod M L`, every `(n^j-s^j)` is divisible by `M L`, so `H_r(n)-H_r(s)` is an integer.

There are finitely many constants `theta_s in [0,1)`. After one global threshold, `epsilon_r(n)` has stable sign and sufficiently small magnitude that:

* when `0<theta_s<1`, `floor(H_r(n)+epsilon_r(n))=H_r(n)-theta_s`;
* when `theta_s=0`, `floor(H_r(n)+epsilon_r(n))=H_r(n)-1` if `epsilon_r` is eventually negative, and `=H_r(n)` otherwise.

Thus on each refined progression the Euclidean quotient agrees **exactly** with a rational polynomial in `n` for every sufficiently large `n`. The remainder `f-g floor(f/g)` is then EQP by arithmetic closure. The claim remains true if `f` is negative. This establishes the lemma.

Initial constants and the input `n` are polynomials; EQP functions are closed under `+,-,*` by common period/threshold. Applying the lemma at each of the finitely many Euclidean-division gates proves inductively that **every register and output entry of `G` is EQP**. No particular bound on the polynomial degree or number of nested divisions is needed beyond the finite circuit assumption.

## 3. Finite list of proper-gcd certificates

Take one common eventual period `M` and threshold `n_0` for all entries of all output matrices at all leaves. For leaf `l` and residue `r`, let `P_{l,r}(X)` be the matrix of the rational-polynomial entry formulas on that class. Pick one fixed positive integer `L` clearing all their coefficient denominators and set

`B_{l,r}(X)=L P_{l,r}(X) in Mat(Z[X]),`
`A_{l,r}=B_{l,r}(0) in Mat(Z).`

For `N=pq>=n_0` in the residue class `r`, `B_{l,r}(N)-A_{l,r}` has every entry divisible by `N`. If neither prime divides `L`, multiplication by `L` preserves rank in both hidden prime fields, so the output's channel ranks equal the ranks of the two reductions of the **fixed integer matrix `A_{l,r}`**.

For every matrix `A` with rational rank `k>0`, and every `1<=t<=k`, let

`Delta_t(A)=gcd{ |det A[I,J]| : I,J index t-by-t minors } > 0.`

If the channel ranks are `u<v`, choose `t=v`. The elementary minor criterion gives `p | Delta_v(A)` for the lower-rank prime, and `q` does not divide that divisor. Therefore `gcd(pq,Delta_v(A))` equals the lower-rank prime and is proper.

Build `C_G` as the union of (i) all these positive divisors for every `l,r,t`; (ii) the prime divisors of `L`, which handle noninvertible clearing multipliers; and (iii) the primes dividing any of the **finitely many semiprimes `N<n_0`** on which the circuit is defined. These are finite, effectively obtainable from the finite circuit and the EQP construction. The third component handles small exceptional inputs directly without pretending the eventual polynomial formula holds there.

Let `S_G` be the finite set of primes dividing `C_G`. If `p,q notin S_G`, then at every `A_{l,r}` the top nonzero determinantal divisor is invertible modulo each prime, so the reduction has rational generic rank over both fields; rank 0 matrices remain rank 0. Every leaf consequently has matching CRT ranks, uniformly for any global leaf-selection rule. This proves both assertions.

## 4. Exact computed-divisor example

Use a **quadratic, computed** divisor `d(N)=N^2+N+1` and set

`u(N)=floor((N^3+7)/d(N)),`
`f(N)=floor(u(N)/4)+2,`
`g(N)=rem(N^3+7,d(N)),`
`D(N)=diag(f(N),g(N)).`

The algebraic identity `(N-1)(N^2+N+1)=N^3-1` shows `N^3+7=(N-1)d(N)+8`. Since `0<=8<d(N)` for `N>=3`, this is an **exact Euclidean division**: `u(N)=N-1` and `g(N)=8` throughout all distinct odd-semiprime inputs.

For `r=N mod 4` and `s=(r-1) mod 4` we have

`4D(N)=diag(N+(7-s),32)`,

so the fixed integral specialization is `A_r=diag(7-s,32)`. For `N=35=5*7`, `r=3,s=2`, `D(35)=diag(10,8)`. Its rank is 1 over `F_5` and 2 over `F_7`; `gcd(35,5)=5` is the pre-fixed support certificate.

The divisor `d(N)` is quadratic, computed from earlier numeric registers, and not an affine/fixed divisor. Nevertheless the finite circuit's CRT-rank asymmetry is explained by static support.

## 5. Reproducible finite regression

The exact Python 3 regression below covers all pairs of the 16 odd primes `3<=p<60`: **120 semiprimes, 17 unequal-rank pairs, and 17 fixed-witness cases**. It checks both the exact computed-division identity and every detected rank asymmetry; the universal theorem is proven in ``2–3.

```python
from itertools import combinations
from math import gcd

primes = [
    p for p in range(3, 60, 2)
    if all(p % d for d in range(3, int(p**0.5) + 1, 2))
]

checked = unequal = witnessed = 0
for p, q in combinations(primes, 2):
    n = p * q
    denominator = n*n + n + 1
    u = (n**3 + 7) // denominator
    f = u // 4 + 2
    g = (n**3 + 7) % denominator
    residue = n % 4
    a, b = 7 - ((residue - 1) % 4), 32
    assert u == n - 1 and g == 8
    assert (4*f - a) % n == 0 and (4*g - b) % n == 0
    rank_p = (f % p != 0) + (g % p != 0)
    rank_q = (f % q != 0) + (g % q != 0)
    checked += 1
    if rank_p != rank_q:
        unequal += 1
        support = (2, gcd(abs(a), abs(b)), abs(a*b))
        assert any(1 < gcd(n, c) < n for c in support)
        witnessed += 1

print(len(primes), checked, unequal, witnessed)
```

Executed integer output: `16 120 17 17`; no mismatches.

## 6. Scientific scope and relation to current frontier

This theorem includes as strict special cases the previously saved fixed-divisor theorem and its affine-divisor extension. It is stronger because **every positive Euclidean divisor can itself be a computed earlier register**, subject only to the fixed finite circuit. It also allows any fixed depth of such nesting and finitely many globally selected pre-fixed matrix outputs.

It does not treat unbounded loops, inputs encoding hidden factors, variable-length computation, arbitrary algorithms factoring `N`, input-dependent output-expression injection, or hidden-CRT-local independent branch choices. More informative experiments can target a growing-time process or a genuinely non-Euclidean operation with provenance-preserving state. Nothing in this auxiliary deduction reassigns the original Result, grants independent reviewer status, changes a protected worldview premise, or closes the mother objective.
