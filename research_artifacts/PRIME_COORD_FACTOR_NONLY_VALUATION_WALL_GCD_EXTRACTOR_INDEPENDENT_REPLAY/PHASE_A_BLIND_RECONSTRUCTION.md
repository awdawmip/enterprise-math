# PCF4R Phase-A Blind Reconstruction — N-only Valuation-Wall GCD Extractor

Status: `PHASE_A_FROZEN / SELF_CONTAINED_DERIVATION / POSITIVE_CANDIDATE`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Researcher: `EM-PCF4R-6D96F8`

Claim: `chatgpt-pcf4r-20260827-1932`

Base: `839224dfac59072ecc7c6c027b30b906f5ee24f4`

## Independence boundary

This derivation was reconstructed from the published taskbook, the accepted scheduler-valid PCF4 parent boundary, and elementary number theory. No originating duplicate-execution return, script, branch, or detailed proof was read before this freeze.

Disclosure: the scheduler reconciliation surface visible before CLAIM already exposed the high-level candidate shape (factorial valuation wall, dyadic seeds, an `isqrt(N)/3` fallback, and the headline synchronization inequality `q<2p`). The proofs below were derived independently and the checker was authored independently; Phase B must therefore compare derivations explicitly rather than treating the headline itself as blinded information.

## 1. Observable and exact local valuation wall

Let

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s}.
\]

Let `r>3` be prime and `0<=s<r`. Since `r>=5` and
`3s<=3r-3<r^2`, Legendre's formula has no contribution above the
first `r`-power in `(2s)!` or `(3s)!`; also `v_r(s!)=0`. Therefore

\[
\boxed{v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+
                  \left\lfloor\frac{3s}{r}\right\rfloor.}
\]

In particular, for `0<=s<r`,

\[
\boxed{r\mid A_s\iff 3s\ge r.}
\]

The threshold is exact: if `3s<r`, then also `2s<r`, so both floors are
zero; if `3s>=r`, the second floor is positive.

## 2. First dyadic nonunit alternative

Let `N=pq` with distinct odd primes `3<p<q`. Query the public seeds

\[
s=1,2,4,8,\ldots
\]

and let `s` be the first seed for which

\[
g_s=\gcd(A_s,N)\ne1.
\]

Such a seed exists. Let `s_*` be the least dyadic integer with
`3s_*>=p`. Since the preceding dyadic seed satisfies `3(s_*/2)<p`,

\[
s_*<\frac{2p}{3}<p<q.
\]

Hence the local valuation wall applies simultaneously to `p` and `q`.
At `s_*`, `p|A_{s_*}`. Thus the first nonunit is exactly this seed and

\[
\boxed{g_{s_*}\in\{p,N\}.}
\]

If `g_{s_*}=p`, the factor is already extracted. If `g_{s_*}=N`, then
`q|A_{s_*}`, so `q<=3s_*`. First-seed minimality gives

\[
3(s_*/2)<p,
\]

hence

\[
\boxed{q\le3s_*<2p.}
\]

Therefore synchronization forces the exact endpoint inequality
`q<2p`.

No hidden factor is used in the constructor: "first" means the first
public dyadic seed whose public gcd with `N` is nonunit.

## 3. Synchronized two-seed fallback

Assume the synchronized case, so `q<2p`, and put

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor
 =\left\lfloor\frac{\lfloor\sqrt N\rfloor}{3}\right\rfloor.
\]

Because `p<sqrt(N)<q` and `q<2p`,

\[
\sqrt N<\sqrt2\,p<\frac{3p}{2}.
\]

Thus `t<p/2`; since `p` is odd, `t+1<p`. Therefore both `t` and `t+1`
are below both hidden primes and the local wall applies.

Also

\[
3t\le\sqrt N<q,
\]

so `q` does not divide `A_t`.

There are two cases.

### Case 1: `3t>=p`

Then `p|A_t` while `q\nmid A_t`, hence

\[
\boxed{\gcd(A_t,N)=p.}
\]

### Case 2: `3t<p`

By the defining floor inequality,

\[
3t<p<\sqrt N<3t+3.
\]

Since `p` is integral,

\[
p\in\{3t+1,3t+2\}.
\]

Consequently `3(t+1)>p`, so `p|A_{t+1}`. Because `p,q` are distinct
odd primes, `q-p>=2`. If `p=3t+2`, immediately `q>=3t+4`. If
`p=3t+1`, the only smaller possibility `q=3t+3` is divisible by `3`
and exceeds `3`, hence is not prime. Again `q>=3t+4`. Therefore

\[
q>3(t+1),
\]

so `q\nmid A_{t+1}` and

\[
\boxed{\gcd(A_{t+1},N)=p.}
\]

Thus in every synchronized case one of the two public seeds `t,t+1`
deterministically splits `N`.

## 4. Public N-only stopping rule

For the promised domain `N=pq`, `3<p<q`:

1. For `s=1,2,4,...`, compute `g_s=gcd(A_s,N)`.
2. If `1<g_s<N`, return `g_s`.
3. If `g_s=1`, double `s`.
4. If `g_s=N`, set `t=isqrt(N)//3`.
5. Compute `h_0=gcd(A_t,N)`. If `1<h_0<N`, return it.
6. Otherwise compute `h_1=gcd(A_{t+1},N)` and return it.

The proof above shows the loop reaches its first nonunit before `s<p`,
and the fallback is entered only when `q<2p`, where `t+1<p`.
Therefore every constructor denominator used below is a unit modulo
`N`. The constructor receives only `N`, public constants, and public
indices.

## 5. Exact recurrence and modular constructor

The exact integer recurrence is

\[
\boxed{
A_{s+1}(s+1)^3
=
6(2s+1)(3s+1)(3s+2)A_s,
\qquad A_0=1.
}
\]

It follows directly by taking the ratio of consecutive factorial
definitions.

Whenever `gcd(s!,N)=1`, an equivalent constructor is

\[
A_s\bmod N
=
(2s)!\,(3s)!\,(s!)^{-5}\pmod N.
\]

For every seed actually needed before termination we proved `s<p`,
so `s!` is invertible mod `N`. This gives a fully N-only modular
implementation. Direct exact-binomial evaluation is used only for
bounded recurrence cross-checks.

## 6. Complexity boundary

Let `L=ceil(log2 N)`. The first dyadic nonunit seed satisfies

\[
s<2p/3<2\sqrt N/3.
\]

If synchronization occurs, the fallback seeds satisfy
`t+1<sqrt(N)/3+1`. Recomputing each queried factorial residue from
scratch is still only `O(sqrt(N))` total modular multiplications because
the dyadic seed lengths form a geometric series; the fallback adds one
more square-root-scale pass.

With schoolbook `L`-bit modular arithmetic this gives the conservative
bound

\[
\boxed{O(\sqrt N\,L^2)}
\]

bit operations up to standard gcd/inversion lower-order factors, and
`O(L)` streaming working memory (excluding the fixed-size trace/report).

Equivalently the time is `2^{L/2} poly(L)`: this is **not** a
factorization-speedup theorem. The result is an exact deterministic
factor-blind asymmetry generator on the promised semiprime domain.

## 7. Independent exact regression

Independent checker:

`scripts/check_prime_coord_factor_nonly_valuation_wall_gcd_extractor_replay.py`

Frozen Phase-A run:

`python scripts/check_prime_coord_factor_nonly_valuation_wall_gcd_extractor_replay.py --prime-limit 2000`

Output:

```json
{"local_wall_checks":277045,"prime_count":301,"prime_limit":2000,"recurrence_crosschecks":166,"regression":{"dyadic_splits":35181,"failures":0,"fallback_splits":9969,"max_return_seed":666,"semiprimes":45150,"synchronized_cases":9969},"schema":"PCF4R_PHASE_A_INDEPENDENT_CHECK_V1"}
```

The finite scan is regression only. Universality rests on Sections 1--5.

## Phase-A verdict

\[
\boxed{\texttt{N_ONLY_GCD_EXTRACTOR_VERIFIED}}
\]

at proof-candidate / independent-replay Phase-A strength, subject to the
required Phase-B source comparison and current-tool dedup. No Working
Truth, Foundation mutation, tool-family promotion, or speedup claim is
made here.
