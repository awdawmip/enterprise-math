# R762DN — Exact three-primary BRC endpoint content for C3 and sharp first two plateaux for every C(3^a)

Date: 2026-11-18 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Continuing researcher: `EM-X6-3050F6` (historical SID `MCP-4b2d70a97f594366a7c94a0f8b45df38`). Independent review: `NOT_REVIEWED`.

## Source, premises, and claim scope

Science pins are unchanged: frozen taskbook `research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md@e3f42efac29a2da2d95be391f3231a664e2fade0` and P000 V5 `p000_reality_foundation.json@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Reuse R762DI's 36 named six-step paired-triad Cell-return candidate paths and the R762DJ–DM BRC endpoint group-ring reduction. This is a *candidate* path observer, not an admission of primitive `TRIADIC_CLOSURE_E` Cell/Link/Port events. The ambient six-axis X6 ontology, third-force provenance, and typed observation constraints remain intact.

Let `B` be six *named*, equally weighted integer BRC branches with increments

`(0,0,0), (1,0,0), (0,0,1), (1,1,0), (0,1,1), (1,1,1)`.

Set `P=1+X+Z+XY+YZ+XYZ` in the integral group ring `R_Q=Z[C_Q^3]` for `Q=3^a`, `a>=1`; `C_Q(n;u)` is the coefficient of `u` in `P^n`, and `c_Q(n)=gcd_u C_Q(n;u)` (zero coefficients do not change the gcd). `c_Q(0)=1`. This is exact positive-branch counting with no analytic phase approximation, classical angle, or numerical pi. For k paired-triad *complete* blocks n=2k and physical area modulus q, the relevant normalized modulus is `Q=q/gcd(q,2)`; arbitrary odd n below denotes an algebraic BRC microconvolution, not a claimed complete native block.

## Theorem A — complete exact content for Q=3, including odd exponents

For all integers `n>=0`, `c_3(0)=c_3(1)=c_3(2)=1`. For `n>=3`,

\[
\boxed{v_3(c_3(n))=\begin{cases}
n-1,& n\equiv1\pmod6,\\
n-2,&\text{otherwise},
\end{cases}}
\]

and `c_3(n)` has no prime factors other than 3. Thus for every `n>=3` the exact minimum population of equally likely deterministic initial seeds reproducing *only this endpoint law* is `6^n/c_3(n)`; it is `3*2^n` when `n>=7, n=1 (mod 6)`, and `9*2^n` otherwise. For complete paired-triad k-blocks, `n=2k` gives `9*4^k`, recovering R762DJ. The odd-exponent exceptional class is the new classification.

### Proof (finite algebraic character certificate)

Let `zeta` be a primitive formal cubic root, with `zeta^2+zeta+1=0`. Characters `chi_s(u)=zeta^(s.u)`, for `s,u in C_3^3`, provide the finite group-ring inversion identity

\[
C_3(n;u)=\frac1{27}\sum_{s\in C_3^3}\widehat P(s)^n\,\zeta^{-s\cdot u},\qquad
\widehat P(s)=\sum_{b\in B}\zeta^{s\cdot b}.
\]

Direct exact enumeration of these 27 characters gives the following complete multiplicity table:

| `P-hat(s)/3` | multiplicity |
|---|---:|
| `0` | 12 |
| `2` (trivial character) | 1 |
| `1` | 4 |
| `-zeta` | 4 |
| `-zeta^2` | 4 |
| `zeta` | 1 |
| `zeta^2` | 1 |

In particular all 27 eigenvalues lie in `3 Z[zeta]`. For `n>=3` separate the trivial character and put

\[
C_3(n;u)=3^{n-3}(2^n+t_r(u)),\quad r=n\bmod6,
\quad t_r(u)=\sum_{s\ne0,\widehat P(s)\ne0}(\widehat P(s)/3)^r\zeta^{-s\cdot u}.
\]

The latter sum is an integer (conjugate characters pair) and depends only on `r` because the nonzero nontrivial normalized eigenvalues are sixth roots of unity. Enumerating all 27 possible `u` by multiplication in `Z[zeta]` gives the *complete*, n-independent multiset:

| r parity | `t_r(u)` value : multiplicity |
|---|---|
| even | `-4:8, -1:6, 2:12, 14:1` |
| odd | `-2:21, 7:6` |

The two rows are verified without floating point by the included 27-character checker, which is an exhaustive algebraic certificate for this finite table. For even n, gcd of the differences of the four t-values is 3 and `3 | (2^n+2)`, so `gcd_u(2^n+t_r(u))=3`. For odd n, the difference is 9 and `gcd_u(2^n+t_r(u))=gcd(2^n-2,9)`: it equals 9 exactly when `n=1 mod 6`, otherwise 3. Therefore the gcd of the coefficients is `3^{n-3}*3` or `3^{n-3}*9` as claimed. Direct n=0,1,2 inspection covers the boundary cases. The argument simultaneously establishes purity of the factor 3. QED.

## Theorem B — universal lower bound for Q=3^a

Let `a>=1`, `Q=3^a`, `d=3^(a-1)`. Then for every `n>=0`,

\[
\boxed{v_3(c_Q(n))\ge\max(0,\lfloor n/d\rfloor-2)}.
\]

There are no prime factors other than 3 in `c_Q(n)`.

**Proof.** Write `n=dm+r`, `0<=r<d`. Frobenius reduction modulo 3 gives
`S=P^d = A+3B0` with `A=P(X^d,Y^d,Z^d)` supported on the subgroup `H=(C_3)^3` of `C_Q^3` (and `B0 in R_Q`). By Theorem A, `A^j` is divisible coefficientwise by `3^max(0,j-2)` for every j>=0. Expand `S^m` binomially: every term `(3B0)^i A^(m-i)` has coefficient valuation at least `i+max(0,m-i-2)`, which is at least `max(0,m-2)`. Multiplying by `P^r` preserves this lower bound. Finally `c_Q(n) | P(1,1,1)^n=6^n`. When Q is a power of 3, the group algebra `F_2[C_Q^3]` is reduced (Maschke, or separability of `X^Q-1` in characteristic 2); its nonzero polynomial P (six distinct basis monomials) cannot have a zero power. Thus 2 does not divide the coefficient gcd, and no prime other than 2 or 3 could divide it. QED.

## Theorem C — exact first and second compression plateaux for a>=2

For every `a>=2`, `d=3^(a-1)` and `0<=r<d`,

\[
\boxed{c_{3^a}(3d+r)=3,\qquad c_{3^a}(4d+r)=9.}
\]

**Proof.** Use `S=A+3B0` as above and let `V=A^3/3 mod 3`, `U=A^4/9 mod 3`, regarded as elements of `F_3[H]`. Theorem A and its finite table show that V has coefficient 2 at every element of H, whereas U is *not constant* on H: its coefficients assume `0,1,2` (for example from `C_3(4;u)/9` corresponding to the even t-table). These are algebraic group-ring identities, independent of a.

For m=3, expanding `(A+3B0)^3` modulo 9 gives `S^3/3 = V (mod 3)`. For m=4, expanding modulo 27 gives `S^4/9 = U + V B0 (mod 3)` because the `12 A^3 B0 / 9` term reduces to `4 V B0`, and all other cross terms vanish modulo 3. Both congruences are legitimate since Theorem B establishes the requisite integral divisibilities.

Decompose `C_Q^3` into cosets of H. The element `V=2 sum_{h in H} h` is constant on each H-coset after multiplication by any group-ring element. For `0<=r<d`, the coefficient of `P^r` in the *identity coset* of H is exactly the identity basis element with coefficient 1: every original exponent lies in `[0,r]` and the only triple divisible by d is `(0,0,0)`, attained only from all-constant branches. Consequently the identity-coset part of `(S^3/3)P^r mod 3` is V, hence nonzero, proving exact valuation 1. The identity-coset part of `(S^4/9)P^r mod 3` is U plus some constant-on-H element, which cannot vanish because U is nonconstant; exact valuation 2 follows. Divisibility and absence of other prime factors follow from Theorem B. QED.

## New finite evidence, conjecture and validation limits

For `a>=2`, computations support the stronger formula

\[
\textbf{CONJECTURE:}\quad v_3(c_{3^a}(n))=\max(0,\lfloor n/3^{a-1}\rfloor-2)
\quad\text{for all }n\ge0.
\]

It is proved above as a lower bound and as equality across the first two complete compression plateaux; the universal sharpness for all later plateaux remains open. Author-side exact positive-branch convolution checked Q=3 for n=1..48, Q=9 for n=1..180, and Q=27 for n=1..120; no exception was found. The accompanying independent finite-character certificate checks all 27 Fourier characters, all 27 states for each of six residues, and the stated two t-multisets using integer arithmetic in `Z[zeta]`. It does not use floating point, pi, trigonometric functions or an untyped replacement of BRC dynamics. `R762DN_VERIFY.py` and `R762DN_EVIDENCE.json` provide reproducibility, including sample gcds and the exact assertions tested.

## Next research and operational dependencies

1. Decide or refute the all-a, all-n sharpness conjecture using the 3-adic filtration of the lifted `P^d`, including exact treatment of `B0=(P^d-A)/3` and its interaction with the H-coset socle.
2. Obtain the source-authorized native `TRIADIC_CLOSURE_E` Cell/Link/Port event predicate and V17/V29/V39 transport; only then test whether endpoint-only area observation suffices for legal future events. Signed source provenance and the full X6 ambient model remain in the scientific inputs.
3. Preserve R762CA–DM verified material, owner/claim provenance and author-review separation; the present theorem is author proved and tested, `NOT_REVIEWED`.
