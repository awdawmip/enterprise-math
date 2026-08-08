# Legendre Pressure Test: Square Basins, Carries, and Möbius Cancellation

Status: `ACTIVE RESEARCH NOTE`  
Discipline: this note **does not prove Legendre's conjecture**. It records only ordinary-mathematical proofs, finite computational counterexamples, and the resulting open obstruction.

## 1. Why Legendre's conjecture

Legendre's conjecture asks that for every integer `k>=1`, the open interval

\[
(k^2,(k+1)^2)
\]

contain a prime.

This is exactly aligned with the square-collapse basin of Enterprise Math: the basin of `C_2(n)=k^2` is

\[
[k^2,(k+1)^2-1].
\]

Thus the public problem can be used as an external pressure test without changing the object: every square-collapse basin should contain a prime among its interior states.

External benchmark: at the time of this note the conjecture remains open. Campbell (2026) proves that every consecutive-square interval contains an integer with at most three prime factors; Sorenson–Webster computationally verified Oppermann/Legendre up to `k<=7.05*10^13`. See `SRC-CAMPBELL-2026-SQUARES` and `SRC-SORENSON-WEBSTER-2025`.

## 2. Notation

Define the interior of the square basin by

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\qquad |I_k|=2k.
\]

For a positive integer `d`, define

\[
H_d(k)
=
\#\{n\in I_k:d\mid n\}
=
\left\lfloor\frac{k^2+2k}{d}\right\rfloor
-
\left\lfloor\frac{k^2}{d}\right\rfloor.
\]

More generally, for `p>=1`, define

\[
H_{p,d}(k)
=
\left\lfloor\frac{(k+1)^p-1}{d}\right\rfloor
-
\left\lfloor\frac{k^p}{d}\right\rfloor,
\]

and

\[
W_p(k)=(k+1)^p-k^p.
\]

## 3. Theorem L001 — Root-factor horizon

Status: `PROVED`

If `n>1` has at least `m` prime factors counted with multiplicity, then at least one prime factor satisfies

\[
p\le R_m(n).
\]

Proof. If all `m` selected prime factors exceeded `R_m(n)`, each would be at least `R_m(n)+1`, hence

\[
n\ge(R_m(n)+1)^m>n,
\]

a contradiction.

Therefore for `n\in I_k`, where `R_2(n)=k`,

\[
n\text{ is composite}
\iff
\exists\text{ prime }p\le k\text{ with }p\mid n.
\]

This gives the exact finite sieve cutoff for Legendre's problem.

## 4. Theorem L002 — Euclidean basin descent

Status: `PROVED`

Write

\[
k=qd+t,
\qquad 0\le t<d.
\]

For every `p>=1`,

\[
\boxed{
H_{p,d}(k)
=
\frac{W_p(k)-W_p(t)}{d}
+
H_{p,d}(t)
}.
\]

Proof. Since `k` is congruent to `t` modulo `d`, both `k^p-t^p` and `(k+1)^p-(t+1)^p` are divisible by `d`. Subtracting the corresponding local endpoints before taking integer quotients extracts the divisible part and leaves exactly `H_{p,d}(t)`.

For squares this simplifies to

\[
\boxed{H_d(k)=2q+H_d(t)}.
\]

Thus a global hit count splits into a deterministic coarse term and a strictly smaller local basin.

## 5. Definition L003 — Square carry

Define

\[
\kappa_d(k)=H_d(k\bmod d).
\]

Then L002 gives

\[
\boxed{H_d(k)=2\left\lfloor\frac{k}{d}\right\rfloor+\kappa_d(k)}.
\]

For `t=k mod d`,

\[
\kappa_d(k)
=
\left\lfloor
\frac{(t^2\bmod d)+2t}{d}
\right\rfloor.
\]

Since `0<=t<d`,

\[
0\le (t^2\bmod d)+2t<3d,
\]

so the square case has the special ternary compression

\[
\boxed{\kappa_d(k)\in\{0,1,2\}}.
\]

For higher powers the local basin width is not bounded by a fixed multiple of `d`, so this ternary behavior is special to the square layer.

## 6. Theorem L004 — Möbius carry identity

Status: `PROVED`

Let

\[
P_k=\prod_{p\le k}p
\]

and let `mu` be the classical Möbius function. Möbius inversion is established mathematics adopted here without a novelty claim; see `SRC-ROTA-1964-MOBIUS`.

By L001, the states in `I_k` coprime to `P_k` are exactly the primes. Hence, writing

\[
\Pi(k)=\#\{p:k^2<p<(k+1)^2,\ p\text{ prime}\},
\]

we have

\[
\Pi(k)=\sum_{d\mid P_k}\mu(d)H_d(k).
\]

Substituting L003 gives

\[
\Pi(k)
=
2\sum_{d\mid P_k}\mu(d)\left\lfloor\frac{k}{d}\right\rfloor
+
\sum_{d\mid P_k}\mu(d)\kappa_d(k).
\]

The first sum counts the integers in `1..k` coprime to `P_k`, of which only `1` exists. Therefore

\[
\boxed{
\Pi(k)
=
2+
\sum_{d\mid P_k}\mu(d)\kappa_d(k)
}.
\]

Thus Legendre's conjecture is exactly equivalent to

\[
\boxed{
\sum_{d\mid P_k}\mu(d)\kappa_d(k)\ge-1
}.
\]

This is not a proof; it converts the problem into a signed local-carry balance.

## 7. Theorem L005 — Binary parity compression

Status: `PROVED`

For odd `d`, define

\[
\delta_d(k)=\kappa_d(k)-\kappa_{2d}(k).
\]

Let

\[
q=\left\lfloor\frac{k}{d}\right\rfloor.
\]

Then

\[
\boxed{
\delta_d(k)\in\{0,(-1)^q\}
}.
\]

Hence there is a binary variable

\[
\varepsilon_d(k)\in\{0,1\}
\]

with

\[
\delta_d(k)=(-1)^q\varepsilon_d(k).
\]

Proof idea. `H_d(k)` corresponds to a consecutive block of integer quotients, while `H_{2d}(k)` counts the even quotients in that block. Any even-length block has exact odd/even balance; only the at-most-two boundary quotients supplied by the square carry can create imbalance. For even `q` the difference is `0` or `+1`; for odd `q` it is `0` or `-1`.

Pairing the Möbius terms `d <-> 2d` in L004 yields

\[
\boxed{
\Pi(k)
=
2+
\sum_{\substack{d\mid P_k\\d\text{ odd}}}
\mu(d)
(-1)^{\lfloor k/d\rfloor}
\varepsilon_d(k)
}.
\]

The ternary carry has therefore been compressed to a **binary boundary event plus a quotient-layer parity sign**.

## 8. Center anchor and Theorem L006 — Anchor-face cancellation

Rewrite the square interval around

\[
M=k(k+1).
\]

Then

\[
I_k=M+\{1-k,\ldots,k\}.
\]

If `p|M`, then

\[
p\mid(M+s)\iff p\mid s.
\]

Thus all prime factors of `k(k+1)` align with the zero residue in centered coordinates.

Let

\[
A_k=\prod_{\substack{p\le k\\p\mid k(k+1)}}p.
\]

For every `d|A_k`, let `t=k mod d`. Since

\[
t(t+1)\equiv0\pmod d,
\]

we have:

- if `d|k`, then `t=0` and `kappa_d(k)=0`;
- otherwise `0<t<d`, `t^2 congruent -t (mod d)`, hence `t^2 mod d=d-t` and `kappa_d(k)=1`.

Therefore

\[
\boxed{
\sum_{d\mid A_k}\mu(d)\kappa_d(k)=0
\qquad(k\ge2)
}.
\]

Equivalently, split the coprime prime factors of `k` and `k+1`: terms supported only on the `k` side have zero carry; once a `k+1`-side factor is present the carry is one, while the Möbius sum over all `k`-side subsets is zero.

Meaning: **the entire Boolean face supported only on center-anchor primes cancels. Every genuinely difficult Möbius term must contain at least one prime that does not divide `k(k+1)`.**

## 9. Anchor Möbius transfer

Split the small primes into

\[
A_k=\prod_{p\mid k(k+1)}p,
\qquad
B_k=\prod_{\substack{p\le k\\p\nmid k(k+1)}}p.
\]

For `b|B_k`, define

\[
\Lambda_b(k)
=
\sum_{a\mid A_k}\mu(a)\kappa_{ab}(k).
\]

Then L004 becomes

\[
\Pi(k)=2+
\sum_{b\mid B_k}\mu(b)\Lambda_b(k),
\]

and L006 gives

\[
\Lambda_1(k)=0.
\]

Hence

\[
\boxed{
\Pi(k)=2+
\sum_{\substack{b\mid B_k\\b>1}}
\mu(b)\Lambda_b(k)
}.
\]

This moves the support of the unresolved part from all small primes to interactions involving transverse primes.

A tempting stronger conjecture was

\[
|\Lambda_b(k)|\le\omega(A_k).
\]

Finite search disproves it:

\[
k=456,
\quad A_k=2\cdot3\cdot19,
\quad b=5,
\quad \Lambda_5(456)=-4,
\]

while `omega(A_k)=3`. This route is therefore not retained as a candidate theorem.

## 10. Failed route: square residues/common root alone are insufficient

Another candidate was that all forbidden residue classes arising from one square root might already prevent complete coverage of length `2k`.

This is false.

Take

\[
y=73,
\]

and

\[
x=33641709557196602631265058865.
\]

Let

\[
P_{73}=\prod_{p\le73}p
=40729680599249024150621323470.
\]

Direct integer verification gives

\[
\gcd(x^2+r,P_{73})>1
\qquad(1\le r\le146).
\]

Thus every state from `x^2+1` through `x^2+146` is covered by primes at most `73`. The local square roots do not merely exist independently; they come from one common integer `x`.

The crucial failure is

\[
x\gg73.
\]

Therefore the uneliminated Legendre constraint is not merely “common square root,” but the stronger self-consistency

\[
\boxed{x=y=k}.
\]

The project calls this still-open structural feature **Bounded Common-Root Coherence**, more precisely **Root–Cutoff Coupling**.

This is adjacent to classical Jacobsthal/covering problems, so the terminology is currently `NOVELTY_UNVERIFIED`; a new name is not evidence of historical novelty.

## 11. The actual remaining obstruction

L004–L006 do not evade the classical sieve parity barrier. Campbell's 2026 result also explains that the weighted-sieve framework meets natural limitations when one tries to push the bound `Omega<=3` further (`SRC-CAMPBELL-2026-SQUARES`).

The pressure test now locates the needed tool more narrowly:

1. controlling total removal is insufficient;
2. square-residue structure alone is insufficient;
3. a common root alone is insufficient;
4. the self-consistency `root = cutoff = k` must be used;
5. signed cancellation between Möbius parity layers must be controlled, not only nonnegative preimage counts.

A concrete next attack is to seek a sign-reversing pairing, quotient-layer recursion, or transverse-prime stratification for

\[
\mu(d)(-1)^{\lfloor k/d\rfloor}\varepsilon_d(k)
\]

that pairs most terms and leaves boundary terms whose total is at least `-1`.

## 12. Feedback into P008

This pressure test shows that the P008 “minimal algebraic structure” problem should compare at least:

- commutative idempotent collapse/semilattice structures;
- the Boolean divisor lattice;
- incidence algebras;
- Möbius inversion;
- signed boundary/carry observables;
- multiscale Euclidean descent.

The existing monotone preimage counts provide nonnegative information only, whereas a public prime problem immediately requires signed cancellation. P008 should therefore ask not only how to represent collapse, but also how overlap depth and signed inversion live on the collapse lattice.

## 13. Current status

- `L001` root-factor horizon: `PROVED`
- `L002` Euclidean basin descent: `PROVED`
- `L003` ternary square carry: `PROVED`
- `L004` Möbius carry identity: `PROVED`
- `L005` binary parity compression: `PROVED`
- `L006` anchor-face cancellation: `PROVED`
- `|Lambda_b|<=omega(A_k)`: `DISPROVED_BY_COUNTEREXAMPLE`
- “an arbitrary common square root prevents full coverage”: `DISPROVED_BY_EXPLICIT_WITNESS`
- “bounded common-root coherence implies Legendre”: `OPEN`
- Legendre's conjecture: `OPEN / NOT PROVED HERE`

Executable verification is in `src/enterprise_math/legendre.py` and `tests/test_legendre_pressure.py`.
