# Perfect Prime AP HCM0 — m=6 all-parameter normalized trace certificate

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260906T2125`  
Date: 2026-09-06  
Status: **EXACT ALL-PARAMETER m=6 THEOREM — ALL-m M6 / HCM0 REMAIN OPEN**

## 1. Statement

Set `m=6`, `n=5`. Let the initial actual layer be `S=s0>=0`, and let the two consecutive block lengths satisfy `a>0`, `c>0`. Put

\[
r_0=6S,\qquad r=6(S+a),\qquad s=6(S+a+c).
\]

Normalize the synchronized quotient forms by the strictly positive trivial gap squares:

\[
\mathcal H_a=(6a)^{-2}Q_{r_0,r},
\qquad
\mathcal H_{a+c}=(6(a+c))^{-2}Q_{r_0,s}.
\]

Then for every real `S>=0`, `a>0`, `c>0`,

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)>5.
}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}(Q_{r_0,s}^{-1}Q_{r_0,r})
>5\left(\frac{a}{a+c}\right)^2>0.
}
\tag{1.2}
\]

Thus the first dangerous extreme genuine three-support mixed coefficient has the required strict sign for every `m=6` actual three-layer base slice.

## 2. Exact reduced data

For `m=6`,

\[
F(x)=\mu_x^{-1}=\frac1{120}\prod_{k=1}^{6}(6x+k),
\]

and direct finite differencing gives

\[
\boxed{\Delta^5F(x)=23328(12x+37).}
\tag{2.1}
\]

At the middle terminal level `r=6(S+a)`, the six blocks `r,r+1,...,r+5` partition one contiguous block of `36=m^2` linear factors. Hence

\[
L_r=\prod_{k=1}^{36}\bigl(36(S+a)+k\bigr)>0.
\tag{2.2}
\]

For the later endpoint `s=6(S+a+c)`, the Sherman-Morrison scalar used by the frozen rank-one inverse is

\[
S_s=(-1)^5\Delta^5F(s)
=-23328\,[72(S+a+c)+37]<0.
\tag{2.3}
\]

The checker constructs the normalized translation transition

\[
V=\overline T_{6a}\overline T_{6(a+c)}^{-1},
\]

in exact polynomial arithmetic, reconstructs the common-denominator numerator of `H_r`, inserts the previously proved rank-one numerator for `H_s^{-1}`, and forms

\[
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)-5.
\]

No floating-point arithmetic is used.

## 3. Positive polynomial certificate

After exact cancellation of the factor `c`, clearing rational coefficient content, and orienting by the known sign in (2.3), one obtains

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)-5
=
\frac{\frac{2229025112064}{5}\,c\,P_6(a,c,S)}
{[72(S+a+c)+37]\,L_r}.
}
\tag{3.1}
\]

The primitive integer polynomial `P_6` has:

- total degree `36=6^2`;
- exactly `6214` nonzero monomials;
- all `6214` coefficients strictly positive;
- minimum coefficient
  `4579782756145393414891192920000000`;
- maximum coefficient
  `6306341609694513654383029565571237172427478203022182449152000`.

Order monomials by SymPy canonical `Poly(a,c,S).terms()` order and serialize each row as

`deg_a,deg_c,deg_S|coefficient`.

The primitive coefficient table has digest

`sha256:7e1b1042aba54c874bae3b57fbff13cd6d3c22fafc455331390c2fa24918f13a`.

The exact rational polynomial before primitive normalization has coefficient content

\[
\frac{51998697814228992}{5},
\]

and division by the positive factor `23328` in `Delta^5 F` gives exactly

\[
\frac{51998697814228992/5}{23328}
=\frac{2229025112064}{5},
\]

which is the prefactor in (3.1).

Since every displayed denominator factor is strictly positive on `S>=0`, `a>0`, `c>0`, (1.1) follows.

## 4. BRC observer/provenance audit

The current global BRC policy is applied explicitly.

This target is a signed determinant/mixed-discriminant cancellation problem. Positive Weighted-BRC total mass is therefore **not** a sound replacement for the signed coefficient, by the Foundation `SIGNED_BOUNDARY` rule.

The normalization above is nevertheless BRC-safe for this observer because it removes only the strictly positive scalar `(6b)^2` and retains the exact labels

\[
(S,a,c),\qquad r_0=6S,\ r=6(S+a),\ s=6(S+a+c).
\]

Thus no layer provenance or sign-carrying branch datum needed by the mixed coefficient is discarded. The all-positive polynomial `P_6` is obtained only **after** the signed algebra has been resolved exactly; it is not inferred from positive branch mass.

## 5. Pattern through m=3,4,5,6

Full-parameter certificates now exist consecutively for

\[
m=3,4,5,6.
\]

Their positive primitive numerator degrees are

\[
9,16,25,36=m^2.
\]

The common structural source is the contiguous denominator identity

\[
\prod_{j=0}^{m-1}\prod_{k=1}^{m}(m(r+j)+k)
=\prod_{k=1}^{m^2}(mr+k),
\]

which at an actual middle level `r=m(S+a)` becomes

\[
\prod_{k=1}^{m^2}(m^2(S+a)+k).
\]

This repeated `m^2`-degree positive numerator pattern is now an exact four-dimensional discovery frontier. It strongly motivates a dimension-free branch/complement-factor formula, but it is not itself promoted to an all-`m` theorem.

## 6. Boundary and next target

Proved here:

- exact all-parameter `m=6` normalized trace inequality;
- a `6214`-term positive primitive polynomial certificate;
- strict sign of the extreme three-support mixed coefficient at `m=6`;
- explicit BRC observer/provenance audit for this reduction.

Still open:

- `M6_ACTUAL_TWO_BLOCK_NEWTON_TRACE_POSITIVITY` for arbitrary `m`;
- all remaining genuine three-support coefficients;
- all-support layer sign regularity;
- HCM0 and parent determinant nonvanishing.

The next proof target is not another brute-force dimension. It is to derive the positive `m^2`-block numerator as a sign-resolved sum over labeled complement-factor branches, using the exact contiguous denominator block and the rank-one inverse formula while preserving signed provenance.