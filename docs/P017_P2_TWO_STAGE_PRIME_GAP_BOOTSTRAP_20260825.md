# P017 — Two-Stage Uniform Prime-Gap Bootstrap for Consecutive-Square P2

Status: `PROVED_WIP CONDITIONAL TRANSFER + EXACT FINITE ENDPOINT CERTIFICATE / NOT CANONICAL / EXTERNAL COMPUTATION DEPENDENCY`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Base owner head before this result: `f9b6cb1b9b7c3d5e5341494792b23f254f3336fe`

Prior-art input: Peter Campbell (2026), *On the Existence of Integers with at Most 3 Prime Factors Between Every Pair of Consecutive Squares*, §2. Campbell records the computational implication that every positive real `x < 6.8*10^19` has a prime in `(x,x+1724]`, and explicitly remarks after Lemma 2.1 that the semiprime construction can be extended beyond `n^2<=10^31` by choosing an appropriate prime `p`.

Historical boundary: this note does not claim the prime-gap computation, semiprime rescaling, or the existence of P2 in sufficiently large short intervals as new mathematics. The result below is an elementary reusable transfer theorem and an optimized application of Campbell's declared finite gap input.

## 1. Abstract uniform-gap hypothesis

Fix real/integer parameters

\[
B>0,\qquad G>0,
\]

and assume the following external certificate:

\[
\boxed{
\forall x\in(0,B),\quad
\exists\text{ prime }q\in(x,x+G].
}
\tag{UG(B,G)}
\]

No distribution theorem beyond this finite uniform-gap certificate is assumed.

## 2. Two-stage bootstrap theorem

Let `K` be a positive integer satisfying

\[
K<B
\]

and

\[
\boxed{
\frac{K^2}{B}+G\le\frac{2K}{G}.
}
\tag{1}
\]

Then the open consecutive-square interval

\[
(K^2,(K+1)^2)
\]

contains a product of two primes.

Equivalently, it contains an integer `a` with

\[
\Omega(a)\le2.
\]

### Proof

Apply `UG(B,G)` first at

\[
x_1=\frac{K^2}{B}.
\]

Because `K<B`, we have `0<x_1<B`. Hence there exists a prime

\[
p\in\left(\frac{K^2}{B},\frac{K^2}{B}+G\right].
\]

By (1),

\[
p\le\frac{2K}{G}.
\tag{2}
\]

Since `p>K^2/B`,

\[
x_2:=\frac{K^2}{p}<B.
\]

Apply `UG(B,G)` a second time at `x_2`. There exists a prime

\[
q\in\left(\frac{K^2}{p},\frac{K^2}{p}+G\right].
\]

By (2),

\[
G\le\frac{2K}{p}.
\]

Therefore

\[
q\le\frac{K^2}{p}+\frac{2K}{p}
=\frac{K^2+2K}{p}.
\]

Multiplying by `p` gives

\[
K^2<pq\le K^2+2K=(K+1)^2-1<(K+1)^2.
\]

Thus `pq` is a semiprime in the open square basin. ∎

## 3. Exact admissible K interval

Condition (1) is equivalent to

\[
G K^2-2BK+BG^2\le0.
\tag{3}
\]

When `B>G^3`, the real roots are

\[
K_\pm
=\frac{B\pm\sqrt{B^2-BG^3}}{G}.
\]

Hence every integer

\[
\boxed{
\lceil K_-\rceil\le K\le\lfloor K_+\rfloor
}
\]

satisfying also `K<B` is covered by the two-stage theorem.

For `B>>G^3`, the upper endpoint is asymptotic to

\[
K_+=\frac{2B}{G}-\frac{G^2}{2}+O\!\left(\frac{G^5}{B}\right).
\]

Thus the finite P2 reach supplied by one uniform gap table is naturally of order `2B/G` in the square-root parameter.

## 4. Campbell 2026 specialization

Campbell records

\[
\boxed{
B=6.8\times10^{19}
=68{,}000{,}000{,}000{,}000{,}000{,}000,
\qquad
G=1724.
}
\]

The exact integer inequality

\[
1724K^2
+68{,}000{,}000{,}000{,}000{,}000{,}000\cdot1724^2
\le
2\cdot68{,}000{,}000{,}000{,}000{,}000{,}000\cdot K
\]

holds exactly for the integer interval

\[
\boxed{
1{,}486{,}089
\le K\le
78{,}886{,}310{,}903{,}386{,}301.
}
\]

The endpoint checker attached to this note verifies:

- the inequality fails at `K=1,486,088` and holds at `1,486,089`;
- it holds at `K=78,886,310,903,386,301` and fails at the next integer;
- the upper endpoint is much smaller than `B`, so the first application condition `K<B` is automatic.

Therefore, conditional only on Campbell's quoted uniform prime-gap computation,

\[
\boxed{
\forall K\in[1{,}486{,}089,
78{,}886{,}310{,}903{,}386{,}301]\cap\mathbb Z,
\quad
(K^2,(K+1)^2)\text{ contains a }P_2.
}
\]

## 5. Continuous finite P2 coverage after adjoining verified Legendre range

Campbell also records the Sorenson–Webster computation that every

\[
K\le7.05\times10^{13}
\]

has an actual prime in `(K^2,(K+1)^2)`.

Since

\[
1{,}486{,}089<7.05\times10^{13},
\]

the two certified ranges overlap enormously. Consequently the two external computational inputs together imply the continuous finite statement

\[
\boxed{
\forall\,1\le K\le
78{,}886{,}310{,}903{,}386{,}301,
\quad
(K^2,(K+1)^2)\text{ contains an integer with }\Omega\le2.
}
\]

The squared upper endpoint is

\[
\boxed{
K_{\max}^2
=6{,}223{,}050{,}047{,}945{,}724{,}396{,}985{,}428{,}834{,}462{,}601
}
\]

or approximately

\[
6.22305\times10^{33}.
\]

Campbell's published Lemma 2.1 stopped at `K^2<=10^31` because that was sufficient to join his explicit P3 argument. The present bootstrap makes his own post-lemma extension remark quantitative using the same gap input twice.

## 6. Relation to P017 cofactor geometry

For the selected first prime `p`, the second application is exactly a prime-in-cofactor-window statement:

\[
q\in
\left(
\frac{K^2}{p},
\frac{K^2+2K}{p}
\right].
\]

The abstract P017 cofactor-window machinery therefore supplies a natural coordinate interpretation, but no new analytic estimate is needed for this finite transfer. The proof uses only the uniform gap certificate twice.

## 7. Optimality relative to the sole UG(B,G) input

To make the second gap call legal one needs

\[
p>\frac{K^2}{B},
\]

while to ensure its guaranteed prime remains inside the cofactor window one needs

\[
p\le\frac{2K}{G}.
\]

With no information other than `UG(B,G)`, choosing the first prime from

\[
\left(\frac{K^2}{B},\frac{K^2}{B}+G\right]
\]

is the natural minimal guaranteed location. Condition (1) is precisely the requirement that this guaranteed interval lie below `2K/G`. Thus the upper scale `K~2B/G` is intrinsic to this two-use uniform-gap mechanism; materially exceeding it requires a larger verified `B`, a smaller verified `G`, or additional prime-distribution information.

## 8. Research consequence

The effective analytic P2 route no longer needs to overlap Campbell's original `X=10^31` boundary. A complete all-K proof could instead join the finite side at approximately

\[
X=K^2\approx6.22\times10^{33}.
\]

This enlarges the permissible explicit analytic threshold by a factor of about `622` in `X` compared with `10^31`.

It does not by itself close the all-K problem: the current Chen/Iwaniec-Laborde effectivity work has not yet produced a rigorous explicit analytic threshold below this new finite endpoint.

## 9. Next

1. audit whether the current explicit/bilinear analytic package can be pushed below `6.22*10^33` rather than `10^31`;
2. search current maximal-prime-gap tables for a stronger rigorously documented `(B,G)` pair and recompute the exact endpoint through this theorem;
3. retain the abstract `UG(B,G)` transfer as a reusable finite bridge for future gap-table updates.
