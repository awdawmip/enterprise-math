# P017 — Iwaniec–Laborde `a=5` interior effective-parameter packet

Status: `PROVED_WIP PARAMETER COMPATIBILITY + NUMERICAL MAIN-TERM CROSS-CHECK / NOT CANONICAL / NO FINITE THRESHOLD CLAIM`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Purpose: replace the invalid boundary packet `theta=1/2, a=6` by a strict interior packet inside the exact 1981 hypothesis `3/7 < theta < 1/2`, while keeping a large positive main-term margin and fixed exponent room for later explicitification.

## 1. Packet

Take

\[
\boxed{
\theta=\frac{49}{100},\qquad
 a=5,\qquad
 d=\frac35,\qquad
 D=x^d,
}
\]

and

\[
\boxed{
 b=3,\qquad c=\frac{13}{3}.
}
\]

Then

\[
\frac37<\frac{49}{100}<\frac12,
\]

so the short-interval exponent lies strictly inside the range assumed in §3 of Iwaniec–Laborde 1981.

The weight relation is exact:

\[
b+c+1=3+\frac{13}{3}+1=\frac{25}{3}=\frac{a}{d}.
\]

Equivalently this is the condition of Lemma 1,

\[
b+c+1=a\frac{\log x}{\log D}.
\]

## 2. Weight-window inequalities

The small and high weight breakpoints have exact x-exponents

\[
D^{b/a}=x^{db/a}=x^{9/25},
\]

and

\[
D^{c/a}=x^{dc/a}=x^{13/25}.
\]

Hence

\[
\boxed{
D^{b/a}<y=x^{49/100}<D^{c/a}
}
\]

because

\[
\frac9{25}=0.36<0.49<0.52=\frac{13}{25}.
\]

Also

\[
1\le b<c\le a.
\]

## 3. Lemma-4 bilinear level with fixed epsilon room

Lemma 4 allows, up to its epsilon losses,

\[
M\le yx^{-\varepsilon},\qquad
N\le yx^{-5/14-\varepsilon}.
\]

Therefore

\[
MN\le x^{2\theta-5/14-2\varepsilon}.
\]

Choose the concrete bookkeeping value

\[
\varepsilon=\frac1{100}.
\]

Then

\[
2\theta-\frac5{14}-2\varepsilon
=\frac{211}{350}
=0.602857\ldots
\]

while

\[
d=\frac35=\frac{210}{350}.
\]

Thus the packet has the fixed exponent slack

\[
\boxed{
\left(2\theta-\frac5{14}-2\varepsilon\right)-d
=\frac1{350}>0.
}
\]

A compatible block choice is, at the exponent level,

\[
M\asymp x^{0.48},\qquad N\asymp x^{0.12},
\]

which lies strictly inside the two Lemma-4 bounds and has product `x^0.60`.

This paragraph is parameter bookkeeping, not a new proof of Lemma 4; the analytic theorem remains the 1981 input.

## 4. Lemma-6 high-prime tail

Since

\[
z=D^{1/a}=x^{3/25},
\]

we have

\[
z^2=x^{6/25}=x^{0.24}.
\]

For `theta=49/100`, the base exponent in

\[
D_1=(y^3/x)^{1/2}x^{-2\varepsilon}
\]

is

\[
\frac{3\theta-1}{2}=\frac{47}{200}=0.235.
\]

With `epsilon=1/100`,

\[
D_1=x^{43/200}=x^{0.215},
\]

so

\[
\boxed{D_1<z^2}.
\]

The remaining Lemma-6 order conditions are also strict:

\[
z^2=x^{6/25}<y=x^{49/100}<w=D^{c/a}=x^{13/25}<y^{3/2}=x^{147/200}.
\]

Thus the entire Selberg-tail parameter chain has fixed exponent room.

## 5. General main-term formula and cross-check

The first inequality on p.53 of Iwaniec–Laborde gives the general `a,b,c` lower integral for `W_1`; the later use of Laborde's constants `B_1,B_2` is only a specialization to `a=6`, `b>=3` and is not needed for the present packet.

We numerically reconstructed the standard Jurkat–Richert functions `F,f` from

\[
F(s)=\frac{2e^\gamma}{s}\quad(s\le3),
\]

\[
f(s)=0\quad(s\le2),
\]

and the usual delay differential system

\[
(sF(s))'=f(s-1),\qquad (sf(s))'=F(s-1).
\]

As a transcription check, substituting the printed 1981 optimum

\[
a=6,\quad \theta=0.45,\quad b=4.8698,\quad c=5.1828
\]

into the general p.53 integral plus Lemma-6 tail gives the normalized net

\[
0.00356168\ldots,
\]

which equals `2G` to the precision of the paper's printed `G=0.00177...`. This independently checks the transcription and normalization.

For the present exact packet

\[
a=5,\quad \theta=49/100,\quad d=3/5,\quad b=3,\quad c=13/3,
\]

the same numerical evaluation gives

\[
\mathcal B_{W_1}\approx0.9357197184,
\]

and the Lemma-6 tail ratio is exactly

\[
R=
\frac{4(dc/a-\theta)}{3\theta-1}
=
\frac{12}{47}.
\]

Hence the normalized net quantity

\[
S=e^{-\gamma}\mathcal B_{W_1}-R^2
\]

is approximately

\[
\boxed{S\approx0.4601808421>0.}
\]

This positivity is currently classified as a **high-margin numerical analytic diagnostic**, not a machine-certified interval-arithmetic theorem. The margin is large enough that rigorous enclosure is a tractable next engineering step.

## 6. Consecutive-square embedding

For a square basin

\[
I_K=\{K^2+1,\ldots,K^2+2K\},
\]

put

\[
x_K=K^2+2K=(K+1)^2-1.
\]

For all sufficiently large `K` (indeed the exponent comparison is elementary),

\[
x_K^{49/100}<2K.
\]

Therefore the terminal short interval

\[
(x_K-x_K^{49/100},x_K]
\]

lies inside the open consecutive-square basin. Thus an effective version of the 1981 method for this fixed packet would immediately give an effective P2-in-every-square-basin theorem beyond its explicit threshold.

This does not create a new asymptotic theorem: Iwaniec–Laborde already prove a stronger asymptotic result with exponent `0.45`. The value of this packet is the much larger main-term and exponent slack available for **explicitification**.

## 7. P017 remainder interface

For the full square basin,

\[
O_m(K)=H_m(K)-H_{2m}(K),
\]

and

\[
O_m(K)-\frac Km=r_K(m)-r_K(2m),
\qquad
r_K(m)=H_m(K)-\frac{2K}{m}.
\]

Thus every classical bilinear floor-remainder estimate has an exact odd-parity P017 transfer. The remaining project-specific opportunity is to exploit the low-height square-endpoint coupling to reduce effective constants; the carry representation by itself is not an independent parity-breaking theorem.

## 8. Current next target

The frontier is now an explicit-constant audit, not a parameter-search problem:

1. replace every `O`, `<<`, and `x sufficiently large` in Lemmas 2, 4 and 6 by auditable constants for this fixed packet;
2. rigorously enclose the p.53 main integral (easy in principle because the numerical margin is about `0.46`);
3. combine with an explicit finite square-basin verification range and determine whether the thresholds overlap;
4. only if the generic explicit threshold remains too high, return to P017's special square-endpoint coupling for an improvement.
