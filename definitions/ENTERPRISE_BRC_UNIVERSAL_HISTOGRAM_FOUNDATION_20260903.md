# Enterprise Math — Universal Positive-Rational Histogram BRC Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION ADDENDUM / MAIN-BACKED / FINITE-EXPLICIT-POSITIVE-RATIONAL`
Effective: `2026-09-03`
Parent: `ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md`
Theorem ledger: `ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_THEOREM_LEDGER_20260903.json`

## 1. Purpose

This addendum freezes the main-backed branch-moment, length-aware port, universal exact-weight histogram and dominant-degeneracy results from PRs #1155–#1157.

Power sums, Newton identities, transfer/generating matrices, group semirings, Laurent polynomial/group algebras, weighted rational series and tropical leading multiplicity are classical/general mathematics. Enterprise Math claims the typed BRC synthesis and exact reusable interfaces, not ownership of those generic facts.

## 2. Explicit branch moment characters

For a finite explicit positive-rational branch family `Q={q_e}`, define

\[
P_m(Q)=\sum_e q_e^m,
\qquad m=0,1,2,\ldots.
\]

For alternative branch union and serial Cartesian composition,

\[
P_m(Q\sqcup R)=P_m(Q)+P_m(R),
\]

\[
P_m(Q\times R)=P_m(Q)P_m(R).
\]

Thus every integer `m>=0` is an exact sum-product semiring character.

For an explicit weighted multigraph define

\[
W^{(m)}_{ij}=\sum_{e:i\to j}q_e^m.
\]

Then

\[
\boxed{(W^{(m)n})_{ij}=\sum_{\substack{p:i\to j\\|p|=n}}w(p)^m}.
\]

At fixed length this unifies the previous CWM boundary:

- `m=0` gives supported path count;
- `m=1` gives total positive mass;
- `m->infinity` through the `1/m` root gives dominant path mass.

Canonical ID: `WBRC-T33`.

## 3. Finite moment completeness on primitive branch cells

For `r` positive rational parallel branch weights, the data

\[
P_0=r,\ P_1,\ldots,P_r
\]

recovers the elementary symmetric coefficients by Newton identities and therefore the monic root polynomial

\[
\prod_{i=1}^r(t-q_i).
\]

Hence it determines the unordered exact weight multiset. If the graph has maximum primitive parallel multiplicity `R`, the finite matrix family

\[
\boxed{W^{(0)},W^{(1)},\ldots,W^{(R)}}
\]

is complete for every primitive source-target branch-weight multiset up to parallel-label permutation. Higher moments obey the induced finite linear recurrence.

Canonical ID: `WBRC-T34`.

## 4. Length-aware fixed-m port transfer

For fixed `m`, partition

\[
W^{(m)}=\begin{pmatrix}A_m&X_m\\Y_m&B_m\end{pmatrix}.
\]

Introduce a formal length marker `z` and define

\[
\boxed{E_m(z)=zB_m+z^2Y_m(I-zA_m)^{-1}X_m}.
\]

Then over formal power series / rational functions,

\[
\boxed{(I-zW^{(m)})^{-1}[B,B]=(I-E_m(z))^{-1}}.
\]

The coefficient of `z^n` is exactly the `m`-th power-sum of original length-`n` port paths. This preserves count at `m=0` even when the all-depth count diverges at `z=1`.

At `m=1,z=1`, when the ordinary hidden total-mass block is stable,

\[
E_1(1)=W_{\rm eff},
\]

recovering `WBRC-T30`.

Positive rational gauge acts at moment order `m` by the diagonal gauge `h_i^m`; `m=0` is gauge blind. Fixed-m port contexts and stable sequential elimination commute with this transfer.

Canonical ID: `WBRC-T35`.

## 5. Universal exact-weight histogram carrier

Let

\[
G=\mathbb Q_{>0}^{\times}.
\]

The universal positive finite branch carrier is

\[
\boxed{\mathcal H=\mathbb N[G]}.
\]

Write

\[
H=\sum_q c_q[q],
\]

where `c_q` is the number of alternatives having exact weight `q`.

Recoalescence adds coefficients at equal weights; serial composition convolves weights:

\[
[q]\otimes[r]=[qr].
\]

The old quantities are projections:

\[
C(H)=\sum_qc_q,
\]

\[
W(H)=\sum_qc_qq,
\]

\[
M(H)=\max\{q:c_q>0\},
\]

\[
P_m(H)=\sum_qc_qq^m.
\]

Thus CWM and every integer moment are typed readouts of one exact carrier.

Canonical ID: `WBRC-T36`.

## 6. Prime-valuation universal transfer

Unique factorization gives

\[
G\cong\bigoplus_p\mathbb Z.
\]

A basis element becomes a finite Laurent monomial

\[
[q]\longleftrightarrow X^{v(q)}=\prod_px_p^{v_p(q)}.
\]

A finite graph therefore uses only finitely many prime variables.

Moment specialization is

\[
\boxed{x_p\mapsto p^m}.
\]

In particular:

- `m=0`: `x_p->1` gives branch count;
- `m=1`: `x_p->p` gives total mass.

For the histogram transition matrix `mathcal W`, every coefficient of

\[
\mathcal W^n
\]

is the exact path-weight histogram at length `n`. The formal series

\[
\mathcal G(z)=\sum_{n\ge0}z^n\mathcal W^n
\]

therefore simultaneously preserves length, exact rational path weight and equal-weight multiplicity.

For port blocks define formally

\[
\boxed{\mathcal E(z)=z\mathcal B+z^2\mathcal Y(I-z\mathcal A)^{-1}\mathcal X}.
\]

Then

\[
(I-z\mathcal W)^{-1}[B,B]=(I-\mathcal E(z))^{-1},
\]

and every fixed moment transfer is recovered by specialization:

\[
\boxed{\Phi_m(\mathcal E(z))=E_m(z)}.
\]

When a finite adjugate/determinant compression is used, alternating signs live only in the algebraic completion; they are not signed/amplitude path mass.

Canonical ID: `WBRC-T37`.

## 7. Dominant-degeneracy quotient

For nonzero histogram `H`, define

\[
M(H)=\max\{q:c_q>0\},
\qquad
\boxed{d(H)=c_{M(H)}}.
\]

Set `Lead(0)=(0,0)` and

\[
\operatorname{Lead}(H)=(M,d).
\]

This is an exact semiring quotient:

- recoalescence keeps the larger `M`, or adds `d` when maxima tie;
- serial multiplication sends
  \[
  (M_1,d_1)(M_2,d_2)=(M_1M_2,d_1d_2).
  \]

Pure max-times is the further quotient `(M,d)->M`.

For finite nonzero `H`, if `r<1` is the largest subdominant ratio and `C_< = C-d`,

\[
0\le\frac{P_m(H)}{M^m}-d\le C_<r^m.
\]

Hence

\[
\frac{P_m(H)}{M^m}\to d,
\]

and derived log readout gives

\[
\ln P_m(H)=m\ln M+\ln d+o(1).
\]

Thus the old equal-`k` branch `ln k` is the special case of the general dominant-degeneracy term `ln d`.

Canonical ID: `WBRC-T38`.

## 8. Hard boundaries

Freeze:

```text
TOTAL_MASS_W1 != MOMENT_OR_HISTOGRAM_COMPLETENESS
CONSTANT_W_EFF != LENGTH_SAFE_PORT_SIGNATURE
PRIMITIVE_MOMENT_CUTOFF != AUTOMATIC_PORT_MOMENT_CUTOFF
WEIGHT_HISTOGRAM != LABELED_SEMANTIC_PROVENANCE
FORMAL_RATIONAL_TRANSFER != CONVERGENT_POSITIVE_MASS_OUTSIDE_STABILITY
ALGEBRAIC_DETERMINANT_SIGNS != SIGNED_AMPLITUDE_BRC
FINITE_SYMBOLIC_REPRESENTATION != RUNTIME_COMPLEXITY_SPEEDUP
```

Canonical negative IDs: `WBRC-N14..N18`.

## 9. Tool routing

Reusable T0 subtools:

- `t0.weighted_brc_histogram` -> `src/enterprise_math/brc_histogram.py`;
- `t0.weighted_brc_moment_transfer` -> `src/enterprise_math/brc_moment_transfer.py`.

These extend the existing `T0_BRC` weighted family. They do not create a new top-level tool family and do not mutate Boolean R023 support semantics.
