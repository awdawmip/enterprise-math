# R137B — Exact Farey-gap integer criterion and all-coefficient word certificates

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE MATHEMATICS / NOT_REVIEWED.
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Previous sources: R134 hybrid all-K at cf0054d39919605bc026175c9438ff7f6495f600; R135 midpoint lifting at 195734abcd97356feb3bc26f9c4a3e0ea5924921; R136 at 73438a02082bf7ee60ccd656f66ac87d753d5a11; R137 divisor-collision note in this directory.
Scope: exact external S23 tied one-parameter observer, not a native X6 update theorem.

## Exact statement

Let integers K>=2, m>=1 and L=K-1. For 0<theta<1 and i=0,...,m-1, define

\[
 S_i^{(K)}(\theta)=\lfloor(L+i+1)\theta\rfloor-\lfloor(L+i)\theta\rfloor.
\]

Fix any neighboring Farey fractions r=a/b < s=c/d of order m, including the outer endpoints 0/1 and 1/1. For alpha in the open interval I=(r,s), form intercept cuts:

- zero lower cut (p,j)=(0,0), value 0;
- j=1,...,m: (p_j,j) where p_j=ceil(j alpha), value B_j(alpha)=p_j-j alpha;
- synthetic upper cut (q,k)=(1,0), value 1.

The p_j are constant throughout I; the m+2 cuts are strictly ordered on I. Every pair of adjacent cuts has lower G_l(alpha)=p-j alpha and upper G_u(alpha)=q-k alpha. All (alpha,rho) with alpha in I and G_l(alpha)<rho<G_u(alpha) produce one fixed mechanical word W, determined by their gap (the ordinary floor coding).

**Theorem (exact tied-phase feasibility).** That gap word W is attainable at some tied parameter theta=alpha in I with rho={L alpha} *strictly within this gap* if and only if there exists an integer N satisfying

\[
 \boxed{(L+k)r-q < N < (L+j)s-p.} \tag{B1}
\]

In particular, compute

\[
 N_*=\left\lfloor (L+k)r-q\right\rfloor+1.
\]

The gap is feasible exactly when N_*<(L+j)s-p. When feasible, define

\[
 \ell=\max\left(r,\frac{N_*+p}{L+j}\right),\qquad
 h=\min\left(s,\frac{N_*+q}{L+k}\right).
\]
Then ell<h, and theta=(ell+h)/2 is an exact rational certificate with

\[
 r<\theta<s,\quad G_l(\theta)<\{L\theta\}<G_u(\theta).
\]

This is a necessary *and* sufficient exact integer criterion per Farey slope/intercept gap, with no scan over the input coefficient K.

## Proof

For each alpha in I, set

\[
 f(\alpha)=(L+k)\alpha-q,\qquad
 g(\alpha)=(L+j)\alpha-p.
\]

The cut-order hypothesis implies f(alpha)<g(alpha), since g-f=G_u-G_l>0. Both functions are continuous and strictly increasing (L>=1 and j,k>=0). The condition that L alpha-N lies in (G_l(alpha),G_u(alpha)) is precisely

\[
 f(\alpha)<N<g(\alpha). \tag{B2}
\]

Consider the union over alpha in I of real intervals (f(alpha),g(alpha)). The set of pairs
{(alpha,y):alpha in I, f(alpha)<y<g(alpha)}
is the continuous image of the connected rectangle I x (0,1) under
(alpha,t) -> (alpha,(1-t)f(alpha)+t g(alpha)).
Its projection to the y-axis is thus an interval; openness follows from the strict inequalities, and its infimum/supremum are f(r) and g(s), respectively, because f,g are strictly increasing. Hence

\[
 \bigcup_{\alpha\in I}(f(\alpha),g(\alpha))=(f(r),g(s)).
\]

An integer N occurs in this union exactly when it satisfies (B1); the smallest integer strictly greater than f(r) is N_*. For such N_*, inequality (B2) is equivalent to theta> (N_*+p)/(L+j) and theta<(N_*+q)/(L+k). Intersecting with I gives (ell,h), which is nonempty by the union equality. Its rational midpoint satisfies B2. Since G_l,G_u lie strictly between 0 and 1 inside their gap, 0<L theta-N_*<1; therefore L theta-N_*={L theta}, as required. QED.

## Complete all-K algorithm and bit complexity

Enumerate all neighboring order-m Farey intervals (Theta(m^2)). In each, sort the m+2 affine intercept cuts at the midpoint alpha_0=(r+s)/2. Their order is constant because two distinct j-cuts can collide only when (j-j')alpha is integral, at rational denominator <=m, absent from I; no cut crosses 0 or 1 in I. For each of the m+1 adjacent gaps, apply (B1) and, if feasible, build theta and evaluate all m floor differences, retaining one witness for each distinct word.

Every S-word at a rational Farey endpoint also occurs immediately to its right: each floor(n theta) is right-continuous and has only finitely many cuts. Likewise, a tied intercept exactly on a cut produces one of the neighboring words for a sufficiently small positive theta displacement. Consequently the open-interval/open-gap enumeration captures the *entire* V(K,m), including rational endpoint outputs.

For K=1, the same right-continuity argument gives a simpler complete branch: sample one midpoint theta in every Farey interval and evaluate the word. Here floor terms range from n=0 to m and therefore have all jumps at Farey points of denominator <=m.

The algorithm uses Theta(m^3) exact gap-integer comparisons and at most O(m^4) rational arithmetic/floor operations for constructing and checking m-bit certificates, plus sorting. All intermediate integers and witness denominators have O(log(K+m)+log m) bits up to fixed polynomial products. Thus the bit complexity is polynomial in m and log(K+1) for *every* K>=1, including K with arbitrarily many binary digits. This improves the straightforward R134 hybrid O(m^5) arithmetic bound to O(m^4) while retaining exact witnesses and strict endpoints; it matches the order of R135's O(m^4) lifting algorithm in the saturated range, now for all K.

This is a coefficient-sensitive computational method for the auxiliary S23 family. It is not a generic native six-dimensional BRC algorithm.

## Exact tests and observations

Companion check_r137b.py independently constructs the chronological set of fractions a/n (n from K-1 to K+m-1), uses one exact rational midpoint per chronological atom, and compares the resulting full word set with the Farey integer criterion for m=1,...,10 and K=2,...,39: 380 pairs, exact match. It separately checks every returned witness by the original strict fractional-parts inequality, not only floor differences.

For K=10^80+137, m=1,...,20, the criterion recovers the classical full Sturmian word count F_m; at m=20 it returns 944 distinct words. Largest generated witness denominator in that particular run has 533 bits. This large-input check is finite and does not itself prove the all-K result.

The computed script marker is R137B_FAREY_INTEGER_CRITERION_PASS.

## Next frontier

The exact inequality (B1) exposes the missing-word mechanism through integer gaps between two rational endpoints. Analyze its extreme values over Farey cells to obtain stronger, non-enumerative first-saturation and eventual-saturation constants, and classify return/disappearance intervals of each word as K changes. Preserve each word's potentially multiple Farey-gap representations instead of treating the first as unique.
