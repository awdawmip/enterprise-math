# D25/LIFT GH-29/GH-30 — square-fiber G-port obstruction and two-moment repair

2026-10-28. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is original-author *portable* mathematics, not a native Source checkpoint, formal Result, independent review, admission, or original Hasse W/S theorem.

Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; Objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Logical Research conversation chatgpt-research-hourly-enterprise-math-20260923 stays distinct from maintenance chatgpt-hourly-enterprise-math-20260921.

Immutable author inputs: GH-22 (two character source identities), GH-26 (original signed quadratic fibers), GH-27/GH-28 (F-channel conic–Legendre conversion). Paths are in the same research_notes/portable_direct directory. Their author-derived scope does not acquire formal admission through this extension.

## Setup

Let p=8m+3 be prime, m>=2 (p>=19), k=F_p, and chi be the quadratic character, chi(0)=0. Set

\[
D_m=\binom{3m+1}{m},\quad F_m(z)={}_2F_1(-m,-m;2m+2;z),\quad G_m(z)=(16z\partial_z+5)F_m(z).
\]

Retain both GH-22 original labeled populations, not just their F scalar:

\[
h_F(x)=\chi(x)[x(1+x)]^{3m+1}(1+9x)^m,\quad
h_G(x)=\chi(x)[x(1+x)]^{3m+1}(1+9x)^{m-1}(5-9x).
\]

Their exact finite-field sums satisfy

\[
D_mF_m(9)=-S_F,\quad D_mG_m(9)=-S_G,\qquad S_{F/G}=\sum_{x\in k}h_{F/G}(x).
\tag{1}
\]

Put U=k minus {0,-1,-1/9}; v=(1+9x)/(9x(1+x)), t=1+x. The true fiber consists of the **distinct rational roots** of

\[
9vt^2-9(v+1)t+8=0,\quad \Delta(v)=9v^2-14v+9,
\tag{2}
\]

counting a repeated root once. Denote this set by T(v), and let Sigma(v)=sum_{t in T(v)} chi(t) and M_j=sum_{v nonzero} v^j Sigma(v), j>=1. GH-26 proved h_F(x)=9^m v^m chi(t) for each original x in U. Because m>=2, BOTH original source weights vanish at all three excluded x (including x=-1/9); none is silently deleted.

## GH-29: square-fiber G-port obstruction (general theorem)

**Theorem.** For all such primes:

On an occupied nonsquare fiber v, the two distinct t,t' have the **same** quadratic character; on a ramified nonsquare fiber there is only one actual root. In either case,

\[
\sum_{t\in T(v)} 9^m v^m\chi(t)\frac{14-9t}{9t-8}
=9^m v^m\Sigma(v)\frac{13v-27}{8v}.
\tag{3}
\]

On an occupied square fiber v, the discriminant is nonzero and square, there are exactly two roots with **opposite** quadratic characters. Its F sum is zero, but its G sum is the root-orientation-independent signed quantity

\[
B(v)=\frac{27}{4}9^m v^m\chi(t)(t-t')
=\frac{9^{m+1}}4v^{m-1}\chi(t)\delta_v,\qquad
\delta_v^2=\Delta(v),\quad t=\frac{3(v+1)+\delta_v}{6v}.
\tag{4}
\]

Define B_p=sum of B(v) over all occupied square fibers. Then the **complete** G source is

\[
\boxed{S_G=\frac{9^m}{8}(13M_m-27M_{m-1})+B_p.}\tag{5}
\]

**Proof.** Vieta gives t+t'=(v+1)/v and tt'=8/(9v). Since chi(8)=-1 for p=3 mod8, chi(tt')=-chi(v). Therefore distinct nonsquare-fiber roots have equal characters, while distinct square-fiber roots have opposite characters. A square ramification would force chi(tt')=+1, so it is impossible. Write R(t)=(14-9t)/(9t-8)=6/(9t-8)-1. The exact symmetric identities

\[
(9t-8)(9t'-8)=-8,\quad
\frac{R(t)+R(t')}{2}=\frac{13v-27}{8v},\quad
R(t)-R(t')=\frac{27}{4}(t-t')
\tag{6}
\]

give (3) and (4). For ramification, R(t) equals the displayed symmetric mean but the actual root is counted only once. Interchanging delta_v changes both chi(t) and delta_v signs, making their product invariant. Summing source contributions proves (5). QED.

**Explicit observer-loss witness:** p=19,m=2 has D_mF_m(9)=0 but B_19=8 and D_mG_m(9)=10. F-zero alone does **not** certify G-zero or preservation of every future signed observer. This does not prove B_p nonzero for every prime.

## GH-30: full F/G Laurent repair (general theorem)

Define integer Laurent moments

\[
c_n=\operatorname{CT}_s(s-8-2s^{-1})^n,\quad
c_0=1,\ c_1=-8,\quad
(n+1)c_{n+1}=-8(2n+1)c_n-72nc_{n-1}.
\tag{7}
\]

**Theorem.** For 1<=j<=m,

\[
\boxed{M_j=-72^{-j}c_{2j}\pmod p.}\tag{8}
\]

The distinct, ORIGINAL F and G source sums hence obey

\[
\boxed{D_mF_m(9)=2^{-3m}c_{2m}\pmod p,}\tag{9}
\]

\[
\boxed{D_mG_m(9)=2^{-3m-3}(13c_{2m}-1944c_{2m-2})-B_p\pmod p.}\tag{10}
\]

**Proof.** Apply the exact GH-27 identity for each positive j:

\[
M_j=2^{-j}\chi(3)\sum_{u\in k}u^{2j}\chi(3u^2+8u+6)
=18^{-j}\sum_{w\in k}(w-4)^{2j}\chi(w^2+2).
\]

In the second equality w=3u+4 and 3(3u^2+8u+6)=w^2+2. The conic y^2=w^2+2 has the **exact bijection** s=y+w nonzero, w=(s-2s^{-1})/2. Since 0<2j<p-1, the unweighted power sum over w is zero. All Laurent exponents in (s-8-2/s)^{2j} lie strictly inside +/- (p-1), so complete-field orthogonality gives

\[
\sum_w(w-4)^{2j}\chi(w^2+2)
=2^{-2j}\sum_{s\ne0}(s-8-2s^{-1})^{2j}=-2^{-2j}c_{2j}.
\]

This proves (8). Now S_F=9^m M_m, and (5) supplies S_G. Using D_mF_m=-S_F, D_mG_m=-S_G and 27*72=1944 proves (9),(10). QED.

The restriction m>=2 is necessary for the stated no-boundary-correction formula: for p=11,m=1, h_G(-1/9)=3 mod11 and M_0 cannot be replaced by (8). No unconditional k=0 extrapolation.

## Checked evidence / meaning / continuation

The companion Python standard-library checker enumerates **all** 75 primes 19<=p<2001, p=3 mod8. For every prime it checks original finite-field F and G sources against GH-19 integer binomial/derivative coefficients, every occupied x-fiber and ramification, (3)-(6), the independent discriminant-square-root branch certificate, and integer Laurent moments (8)-(10). All 75 pass. B_p was nonzero in all 75 finite cases, **only finite observation**. Four exact tuples (p,D F,D G,non-square predicted D G,B_p): (19,0,10,18,8), (43,0,21,15,37), (67,0,3,50,47), (83,73,0,5,5).

BRC application: COMPOSE_APPLIED to GH-22, GH-26 and GH-27/GH-28. Population: labeled finite x-sources. Branches: distinct t,t', chi(t), discriminant and F/G port. Future operation: the G weighting R(t). F's scalar quotient loses the square-fiber antisymmetric branch, explicitly repaired by B_p. This does **not** identify these scalar auxiliaries with the original full six-dimensional X6 law, the six Hasse sources, or the native physical observer. No new axioms or time/spatial coordinate changes.

The class-19 all-prime F_m(9) / special Legendre zero is NOT proved. The G non-square Laurent part alone is NOT the G port; B_p is indispensable. GH-15 Laurent first-order compensation, GH-20/21 p-adic jets, original W/S, H0/B0, [X]U mod p^2, Frobenius eta/kappa, original p=373 experiment and independent Driver review remain OPEN.

Next exact research: seek a structural evaluation or higher-cover identity for B_p while continuing the independent proof/counterexample search for the class-19 F zero. Preserve the adjacent Laurent moment and the square-fiber signed residual as separate observer coordinates.

Control read in this run: connected Site gateway 0.6.11 reports research_authority_granted=false and write_relay_enabled=false. No fresh native winning CLAIM, authorized OPEN or Source publish_checkpoint was obtained. The current connector does not expose recovery_status. Historical session/staging/request/real contributions remain untouched; control support awdawmip/enterprise-math#1558 retains the predecessor/session transition recovery. Neither publication on GitHub nor this author check grants formal Research-Activity admission or review. The existing hourly schedule/phase/enablement/notification setup was not modified.
