# PREFIX-825 — Exact minimal nonnegative integer Q-only BRC carriers at capacities 3 and 4

**Research status:** AUTHOR_PROVED / EXACT_SYMBOLIC_CERTIFICATE / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.  
**Date:** 2026-11-16. **Task scope:** independent portable auxiliary research; no shared TASK CLAIM acquired.  
**Scientific freeze:** \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; continue PREFIX-823 and PREFIX-824 without changing P000, source semantics or native event permissions.

## 1. Model and statement

Let \`q\` be the capacity, \`q=3\` or \`4\`. There are at least \`q+1\` named unmarked sources with pairwise distinct positive integer removal weights \`beta_i\`. A single distinguished marked source has removal weight \`b>0\` and insertion weight \`a>0\`. A named state is \`(m,S)\`, \`m∈{0,1}\`, \`|S|+m≤q\`. Removal of \`i∈S\` has weight \`beta_i\`, removal of a present mark has weight \`b\`, and insertion of an absent mark has weight \`a\` provided capacity allows. \`Q=R+A\` is their unnormalized nonnegative integer transition operator. The declared observer \`C_l\` is total mass in states with \`l\` present sources, for \`0≤l≤q\`. The future language consists of \`Q^j\`, every integer \`j≥0\`, not independently addressable \`R,A\`.

Let \`U[k,h]\` (mark absent) and \`V[k,h]\` (mark present) be conditional elementary-symmetric moments of degree \`h\` of the unmarked removal weights in each named subset with initial mass. Empty/out-of-range entries are zero. Exact named-source branch counting yields
\[
(QU)_{k,h}=(h+1)U_{k+1,h+1}+bV_{k,h},\qquad
(QV)_{k,h}=(h+1)V_{k+1,h+1}+aU_{k,h},
\]
with capacity boundary truncation, and \`C_l=U[l,0]+V[l-1,0]\`. These are formulas for the declared positive-count BRC source model, not native X6 physical evolution.

**Theorem 825.1.** At \`q=3\`, there is a 14-dimensional exact carrier with nonnegative integer coordinates, nonnegative integer update matrix and nonnegative integer output matrix, preserving \`CQ^j\` for every \`j≥0\`. Its dimension equals the minimal rational-linear future-observable dimension.

**Theorem 825.2.** At \`q=4\`, the corresponding exact minimal positive integer carrier dimension is 23. This completes the \`b>0\` positive-carrier realization for capacities 1–4 (capacities 1–2 are PREFIX-824). The arbitrary-\`q\` extension remains open.

## 2. Constructive 14-dimensional carrier for q=3

Use zero-based coordinate indices. Define \`x=(x0,...,x13)\` as

| Index | Coordinate | Index | Coordinate |
|---|---|---|---|
| 0 | U[0,0] | 7 | U[3,1]+b V[2,0] |
| 1 | U[2,0] | 8 | U[1,0]+V[0,0] |
| 2 | U[2,1] | 9 | U[1,1]+b V[0,0] |
| 3 | U[2,2] | 10 | 2U[3,2]+b V[2,1] |
| 4 | V[1,0] | 11 | 3U[3,3]+b V[2,2] |
| 5 | V[1,1] | 12 | V[2,1]+a U[1,0] |
| 6 | U[3,0]+V[2,0] | 13 | 2V[2,2]+a U[1,1] |

The complete output is \`(x0,x8,x1+x4,x6)\`. Each update is exact:
\[
\begin{aligned}
x'_0&=x_9,&x'_1&=x_7,&x'_2&=x_{10},&x'_3&=x_{11},\\
x'_4&=x_{12},&x'_5&=x_{13},&x'_6&=a x_1,&x'_7&=ab x_1,\\
x'_8&=x_2+bx_4+x_5+ax_0,&
x'_9&=2x_3+2bx_5+abx_0,\\
x'_{10}&=abx_2,&x'_{11}&=abx_3,&
x'_{12}&=2ax_2+abx_4,&x'_{13}&=4ax_3+abx_5.
\end{aligned}
\]
All coefficients and coordinates are nonnegative integers.

## 3. Constructive 23-dimensional carrier for q=4

Retain the following fifteen unmodified moments as \`x0,...,x14\`, in this exact order:
\[
U[0,0],U[1,0],U[1,1],U[2,2],U[3,0],U[3,1],U[3,2],U[3,3],
U[4,4],V[0,0],V[1,1],V[2,0],V[2,1],V[2,2],V[3,3].
\]
Add eight nonnegative integer mixed moments
\[
\begin{aligned}
x_{15}&=U[4,0]+V[3,0],&
x_{16}&=U[4,1]+bV[3,0],\\
x_{17}&=U[2,0]+V[1,0],&
x_{18}&=U[2,1]+bV[1,0],\\
x_{19}&=2U[4,2]+bV[3,1],&
x_{20}&=3U[4,3]+bV[3,2],\\
x_{21}&=V[3,1]+aU[2,0],&
x_{22}&=2V[3,2]+aU[2,1].
\end{aligned}
\]
The output is \`(x0,x1+x9,x17,x4+x11,x15)\`. The complete positive update is
\[
\begin{array}{llll}
x'_0=x_2+bx_9,&x'_1=x_{18},&x'_2=2x_3+bx_{10},&x'_3=3x_7+bx_{13},\\
x'_4=x_{16},&x'_5=x_{19},&x'_6=x_{20},&x'_7=4x_8+bx_{14},\\
x'_8=0,&x'_9=ax_0+x_{10},&x'_{10}=ax_2+2x_{13},&x'_{11}=x_{21},\\
x'_{12}=x_{22},&x'_{13}=ax_3+3x_{14},&x'_{14}=ax_7,&x'_{15}=ax_4,\\
x'_{16}=abx_4,&x'_{17}=ax_1+x_5+bx_{11}+x_{12},&
x'_{18}=abx_1+2x_6+2bx_{12},\\
x'_{19}=abx_5,&x'_{20}=abx_6,&x'_{21}=2ax_5+abx_{11},&
x'_{22}=4ax_6+abx_{12}.
\end{array}
\]

## 4. Proof of future exactness, positivity and minimality

Let \`v\` be the full conditional moment vector of dimension \`(q+1)^2\`, \`L\` its \`Q\` update matrix and \`C\` its cardinality output. The displayed coordinate definitions specify an integer matrix \`T_q\` and the displayed updates specify \`M_q\`; the outputs define \`W_q\`. Direct substitution into the two elementary-symmetric moment recurrences proves the exact polynomial matrix identities
\[
T_qL=M_qT_q,\qquad C=W_qT_q
\]
over \`\mathbb Z[a,b]\`, for \`q=3,4\`. Hence \`C L^j=W_qM_q^jT_q\` for every \`j≥0\`; nonnegative integer coordinates and updates follow immediately.

Minimality is a separate rank certificate. Form the observability matrix \`O_q=[C;CL;...;CL^9]\`, with rows grouped by power, then cardinality. For \`q=3\`, use zero-based row and column indices
\`R3=K3=[0,1,2,3,4,5,6,7,8,9,10,11,12,14]\`. The exact integer-polynomial determinant of this 14×14 minor is \`96*a^5*b\`.

For \`q=4\`, use
\`R4=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,25,30]\` and
\`K4=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,24]\`.
The 23×23 determinant is \`21233664*a^11*b^7\`.
Both are strictly positive for \`a,b>0\`. Because the complete observer factors through the \`14/23\` retained coordinates, its rank is at most \`14/23\`; these explicit nonzero minors force equality. The accompanying symbolic certificate computes both determinant polynomials over the rationals (no floating point).

Finally, on actual *named* states, choose any \`k+1\` distinct unmarked weights for each subset cardinality \`0≤k≤q\`; the \`k+1\` elementary-symmetric coordinate columns from \`k\`-subsets of those \`k+1\` indices are independent. Indeed, for polynomials \`P_j(t)=∏_{i≠j}(1+beta_i t)\`, evaluation at \`t=-1/beta_j\` annihilates all other \`P_i\` and leaves \`P_j≠0\`. This works separately in the marked-present and marked-absent blocks, hence the map from legal named states onto all conditional moment coordinates has full rational row rank. Therefore the observer rank on the named domain is exactly 14 or 23. Any exact rational-linear carrier preserving all future \`Q\`-only histograms has dimension at least that rank; the displayed positive integer carriers attain it. QED.

The minimality comparison is within finite-dimensional rational-linear carriers. It does not assert minimality among arbitrary nonlinear encodings or for independently selectable \`R,A\`.

## 5. Independent exact checks and reproducibility

- Standard-library \`PREFIX825_R6_Q3_Q4_POSITIVE_MINIMAL_CHECK.py\` directly enumerates all legal marked/unmarked named subsets, branches using their exact integer weights, checks every carrier one-step intertwining and compares full cardinality histograms through step 9. The code additionally evaluates abstract moment-space intertwining, rational row ranks and integer determinant certificates.
- Optional SymPy \`PREFIX825_R6_Q3_Q4_SYMBOLIC_CERT.py\` verifies the polynomial identities and computes the two explicit 14×14 and 23×23 minors **symbolically**.
- \`PREFIX825_R6_Q3_Q4_POSITIVE_MINIMAL_RESULTS.json\`: q=3 beta sets (1,2,3,4), (1,2,3,5,8), (1,2,3,4,7,11); q=4 beta sets (1,2,3,4,5), (1,2,4,7,9,11); \`a,b∈{1,2,3}\`, 45 configurations. Exact regression: 882 abstract-coordinate one-step assertions, 5 rational-rank/minor checks, 5 named-moment-rank checks, 2,592 named basis checks and 25,920 future histogram checks. \`ALL_EXACT_ASSERTIONS_PASSED\`.
- Original named states, branch weights and histograms are independently generated; exact Python integers/Fractions are used throughout. Symbolic certificate run separately returned \`ALL_SYMBOLIC_CERTIFICATES_PASSED\`.

## 6. Frontier and scoped interpretation

This proves positive rational-rank-minimal BRC source-count realizations for \`q=3,4\`, closing two low-capacity cases of PREFIX-824's open \`b>0\` problem. Next: attempt \`q≥5\`, where the hidden observer kernel has dimension \`ceil(q/2)\`; determine whether a positive integer quotient at the same minimal rank exists, or find a precise obstruction. Benchmark total preprocessing/update/output cost if making algorithmic performance claims.

P000 remains unchanged: six native X6 axes, three-dimensional native slice, independent ordered time, full source/provenance and signed/phase-sensitive residuals when required. The present positive-count model declares \`Q\` and cardinality histograms only. No physical elapsed time, native Cell/Link/Port admission, amplitude cancellation or signed phase interference is inferred.

**Source references:** PREFIX-823, PREFIX-824; \`awdawmip/enterprise-math:docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context\`, \`docs/PORTABLE_RESEARCH_PROTOCOL.md\`, \`research_priorities/research_method.json\`, \`p000_reality_foundation.json\`, \`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json\`; global canonical \`main@28899b00f1cc1a29b092d80672bcf9b6cc39c4d8\` at initial read. This auxiliary discovery does not supersede or CLAIM \`RS-X6-NATIVE-TIME-DYNAMICS\`.
