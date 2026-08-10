# P022 — Support-Localized Franel Defect Incidence

Status: `ACTIVE RESEARCH NOTE / EXACT DECOMPOSITION + NEGATIVE BOUNDARY`  
Owner: `program/p022-geometry-v2`  
Consumes: central-binomial A-elimination, integer midpoint companion, Franel zero alphabet

## 1. Exact valuation decomposition

Let `p` be any forced-midpoint prime `p=5 or 7 (mod 8)` such that `p-2` is composite, and let

\[
m=(p-1)/2.
\]

Write the canonical A-elimination as

\[
A_m=\prod_{j<m}A_j^{\alpha_j},
\]

and the corresponding pure Franel defect as

\[
D_m=F_m\Big/\prod_{j<m}F_j^{\alpha_j}.
\]

Then for every prime `p`, exactly

\[
\boxed{
v_p(D_m)=v_p(F_m)-\sum_{j<m}\alpha_jv_p(F_j).}
\]

No independence assumption is used here.

## 2. P022-LI37 — support-localized zero signature

Inside the forced-midpoint window the integer companion gives

\[
p\mid F_j
\iff
p\mid H_{m-j}.
\]

Therefore all *possible* correction locations are the exact incidence set

\[
\boxed{
I_p=\{(j,m-j,\alpha_j):\alpha_j\ne0,\ p\mid H_{m-j}\}.}
\]

For the yes/no support-avoidance question, the whole Franel zero alphabet may be replaced by its intersection with the finite canonical A-support.

For the exact defect valuation one further needs the local values `v_p(F_j)` on those hits.  Zero-set cardinality, first-zero rank, or global p-Lucas basin density are not sufficient substitutes.

## 3. P022-LI38 — exact cancellation at p=157

The prime `157` is a forced-midpoint prime and `157-2=155` is composite.  Here

\[
m=78.
\]

The canonical A-support includes

\[
\alpha_{16}=+1,
\]

and the integer companion detects

\[
157\mid H_{62}
\iff
157\mid F_{16}.
\]

Direct valuations are

\[
v_{157}(F_{78})=1,
\qquad
v_{157}(F_{16})=1.
\]

No other support term has positive `157`-valuation, hence

\[
\boxed{v_{157}(D_{78})=1-1=0.}
\]

This is the canonical negative boundary showing that forced midpoint alone does not guarantee a usable defect witness.

## 4. P022-LI39 — zero-alphabet cardinality is insufficient

Two primes can have the same Franel zero-alphabet cardinality and opposite half-defect behavior.

For `p=157`,

\[
Z_{157}=\{16,75,78,81,140\},
\qquad |Z_{157}|=5,
\]

and the support hits `16`, giving `v_157(D_78)=0`.

For `p=389`,

\[
Z_{389}=\{25,176,194,212,363\},
\qquad |Z_{389}|=5,
\]

but its canonical A-support is disjoint from this alphabet below the midpoint.  Moreover

\[
v_{389}(F_{194})=1,
\]

so

\[
\boxed{v_{389}(D_{194})=1.}
\]

Thus

\[
\boxed{|Z_p|\not\Rightarrow\text{half-defect survival}.}
\]

The location of the hidden zero information relative to the declared elimination support is essential.

## 5. Precision interpretation

This is a concrete P022 specialization of the P023 rule that the legal quotient depends on the declared future computation.

- For p-Lucas basin-size questions, `z_p=|Z_p|` may be sufficient.
- For half-defect support avoidance, retain only `Z_p intersect supp(alpha)`.
- For exact defect valuation, retain the support-localized weighted valuation signature
  \[
  \{(j,\alpha_j,v_p(F_j)):v_p(F_j)>0\}.
  \]

A globally richer-looking scalar statistic can therefore be strictly less useful than a smaller relation-conditioned positional signature.

## 6. Executable assets

- `src/enterprise_math/p022_barlow_half_defect_incidence.py`
- `tests/test_p022_barlow_half_defect_incidence.py`

The test suite contains both the `p=157` cancellation and the `p=173` early-zero/non-support boundary, plus target-family no-hit regressions.
