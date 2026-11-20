# R284BO — Sharp frozen-diagonal star-Port classification for every positive integer alphabet

Date: 2026-11-20 (Asia/Shanghai). Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.

## Source, scope and theorem

This advances the exact R284BN source at awdawmip/enterprise-math@6c6ea62e1c5906c72281c64a71443222575cbafc:research_notes/portable_direct/R284BN_SHARP_ALL_RADIUS_FROZEN_DIAGONAL_PORT_CLASSIFICATION_20261120.md, which treated only H=2. The present theorem covers all integer H>=2 but fixes n=3 and the same auxiliary directed star-Port observer. This is not a native X6 physical realization, Result freeze, or Foundation admission; P000 is unchanged.

Write the nine entries of C in {1,...,H}^{3x3} as rows (a,b,c),(d,e,f),(g,h,i). Define

\[
F_C(d_0,d_1,d_2,z_1,z_2)=\det(\operatorname{diag}(d_0,d_1,d_2)-C-z_1E_{01}-z_2E_{02}).
\]

Fix j in {0,1,2} and one integer t=d_j. The other four controls are freely and jointly selected in an arbitrarily large prime field F_p. A single residue F_C mod p is read on the circle of circumference p with arbitrary real circular error radius rho>=0; put m=floor(2rho).

For distinct matrices C,C' let Q=F_C-F_C' be a polynomial in the four free controls after d_j=t. Define g_j(H,t) as the minimum |Q| among pairs for which Q is independent of all four controls, with an empty minimum defined to be +infinity.

**BO1 — exact constant-fibre gap.**

\[
g_0(H,t)=\begin{cases}
0&1-H(H-1)\leq t\leq H^2,\\
+\infty&\text{otherwise},
\end{cases}
\]
\[
g_1(H,t)=g_2(H,t)=
\begin{cases}
1-H^2-t&t<1-H^2,\\
0&1-H^2\leq t\leq H^2,\\
t-H+1&t>H^2.
\end{cases}
\]

**BO2 — sharp arbitrary finite circular-noise classification.** There exists a prime and one fixed four-control setting that uniquely decodes all H^9 candidates for every allowed error if and only if

\[
\boxed{\begin{aligned}
j=0:\quad&t\notin[1-H(H-1),H^2]\cap\mathbb Z,\\
j=1,2:\quad&t\notin[1-H^2-m,\max\{H^2,H-1+m\}]\cap\mathbb Z.
\end{aligned}}
\]

For nonnegative t the smallest allowed root setting is H²+1 and each leaf's is max(H²+1,H+m). In particular H=2 recovers R284BN exactly; H=3 gives excluded root [-5,9] and leaf [-8-m,max(9,m+2)].

## Proof of BO1

The exact determinant expansion is

\[
F=(d_0-a)[(d_1-e)(d_2-i)-fh]-(b+z_1)[d(d_2-i)+fg]-(c+z_2)[g(d_1-e)+dh]. \tag{1}
\]

### Frozen root

Set d_0=t, s=t-a, u=di-fg, v=ge-dh. In the order (d_1d_2,d_1,d_2,z_1d_2,z_1,z_2d_1,z_2), the complete nonconstant coefficient signature of (1) is

\[
(s,-si-cg,-se-bd,-d,u,-g,v). \tag{2}
\]

If Q is constant, equality of signatures forces a=a', d=d', g=g', together with
\[
s(i-i')+g(c-c')=0,\quad s(e-e')+d(b-b')=0,
\]
\[
d(i-i')-g(f-f')=0,\quad g(e-e')-d(h-h')=0.
\]
Each entry difference has absolute value at most H-1; if |s|>H(H-1), the first line forces i=i', e=e', c=c', b=b', and the second forces f=f', h=h'. Thus no distinct constant-response pair exists when t<1-H(H-1) or t>H².

Conversely, any t in [1-H(H-1),H²] is uniquely t=a+Hℓ with 1<=a<=H and -(H-1)<=ℓ<=H-1. Choose d=g=H and b=e=h=1 in both matrices. Choose C with i=f=2, C' with i'=f'=1, with c-c'=-ℓ, both c,c' in [1,H]. One may take c=1,c'=1+ℓ for ℓ>=0 and c=1-ℓ,c'=1 otherwise. All other entries agree. In (1), the determinant difference is
\[
F_C-F_{C'}=(-s+H\ell)(d_1+h-e)=0.
\]
The matrices are distinct. Hence root g_0=0 exactly on the stated closed interval and infinity elsewhere.

### Frozen leaf

Freeze d_1=t and put r=t-e. In the order (d_0d_2,d_0,d_2,z_1d_2,z_1,z_2), the nonconstant coefficient signature is
\[
(r,-ri-fh,-ar-bd,-d,di-fg,-(gr+dh)). \tag{3}
\]

For a constant Q, equality implies e=e' and d=d', and
\[
r(a-a')+d(b-b')=0,\qquad r(g-g')+d(h-h')=0,
\]
\[
r(i-i')+(fh-f'h')=0,\qquad d(i-i')-(fg-f'g')=0.
\]
If |r|>H(H-1), the first two equations force a=a',b=b',g=g',h=h'; the third then forces i=i' and f=f' because |h(f-f')|<=H(H-1). The only remaining difference is c-c', and the exact constant response is
\[
Q=-(c-c')[g(t-e)+dh]. \tag{4}
\]

For t<1-H², every e in [1,H] gives |r|>H(H-1) and
\[
g(t-e)+dh\le t-1+H^2<0.
\]
So every constant pair satisfies |Q|>=1-H²-t. Equality occurs with g=1,d=h=H,e=1 and c-c'=1. For t>H², similarly |r|>H(H-1) and
\[
g(t-e)+dh\ge t-H+1>0.
\]
Equality occurs with g=d=h=1,e=H and c-c'=1. These prove both exact tail values.

To obtain zero gaps for the entire middle interval, first change only c by one, take g=1 and let k=dh-e. All integers k in [1-H,H²-1] occur: d=h=1 gives the negative values; d=H, h=1,...,H, e=1,...,H gives consecutive H-long blocks covering k=0,...,H²-1. By (4) the response difference is -(t+k), so zero witnesses cover t in [1-H²,H-1].

For t in [1,H²], uniquely write t=e+Hℓ with 1<=e<=H, 0<=ℓ<=H-1. Choose d=f=H in both matrices and keep g,h,i,e fixed, but take the root rows
\[
(a,b,c)=(2,1,2),\qquad(a',b',c')=(1,1+\ell,1).
\]
All entries remain in the alphabet. Substitution into (1) gives
\[
F_C-F_{C'}=-(r-H\ell)(d_2-i+g)=0.
\]
These two zero-witness intervals overlap or abut for H>=2 and cover [1-H²,H²]. Exchanging the two named leaves and simultaneously their star controls maps j=1 to j=2. This proves BO1.

## Proof of BO2

If g_j(H,t)<=m, some pair has a control-independent integer response difference c satisfying |c|<=m<=2rho. Their closed circular radius-rho error balls intersect on every circle for every control setting, so no decoder can guarantee recovery.

If g_j(H,t)>m, then for each of the N=H^9 matrices, each unordered pair, and every integer c in [-m,m], the polynomial Q(x)-c is nonzero over Z. Choose a prime p larger than all its nonzero integer coefficients in absolute value and greater than both 2m+1 and 8(2m+1)binom(N,2). These polynomials remain nonzero in F_p and have total degree at most two in the four free variables by (1). Independent uniform F_p controls, Schwartz–Zippel and the union bound give failure probability at most
\[
\frac{2(2m+1)\binom{N}{2}}p<1/4.
\]
Consequently a fixed setting exists where no two residues differ circularly by an integer in [-m,m]. Every circular pair distance is then >=m+1>2rho, so all closed noise balls are disjoint and nearest-center lookup succeeds. BO1 gives g_0<=m exactly on the root interval and g_leaf<=m exactly on the stated leaf interval. This proves BO2.

## Validation, interpretation and next problem

An independent Python standard-library checker represents the complete nonconstant coefficient signature, computes each H^9 candidate's constant coefficient, groups by signature, sorts constants in each group and takes the exact minimum of successive differences. It separately crosschecks formula (1) against direct determinant evaluation at signed controls. All **270** frozen-index/t tests passed: H=2 (512 matrices; 35 values of t per index), H=3 (19,683 matrices; 46 values per index), H=4 (262,144 matrices; nine selected t values per index), plus **2,160** coefficient/determinant crosschecks. The infinite-H proof is algebraic, not inferred from the finite tests. The accompanying verification JSON specifies the finite tested ranges and landmarks.

This is an existential result in the exact modular-circular observer; it does not provide a minimal prime, polynomial-time parameter search, inexpensive physical detector or efficient table decoding. Mathematical status AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. The Port observer is signed determinant algebra, not a positive-mass BRC carrier. We reuse BRC's observer-fibre information discipline without claiming a positive-weight reduction.

Next scientific questions: explicit low-prime settings near packing bounds under frozen controls; compact decoding; n>=4 constant-fibre invariants; a lossless named-Port quotient characterization preserving control and observation semantics.

Provenance: historical Researcher EM-DIRECT-E6B1DD and RA-DD7D715E42D8874661313886; neither this note nor the existing RA proves a current CLAIM, execution capability, formal Result, independent review or Working Truth promotion.
