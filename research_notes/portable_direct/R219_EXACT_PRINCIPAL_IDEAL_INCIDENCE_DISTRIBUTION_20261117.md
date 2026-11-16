# R219 — Exact distribution and incidence moments of principal right ideals

Date: 2026-11-17 (Asia/Shanghai)
Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED
Scope: finite paired-event observer monoid; no physical BRC effect computation or time calibration.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate predecessor: R215_EXACT_PRINCIPAL_IDEAL_AUTOMATA_20261116.md @71e9d86c4fea71a0ff1b2da66fe2b5656998a68b.
Earlier structural dependencies: R209 (Stirling fibres), R213 (Green ideals), R214 (support quotient).

## Definitions

Let m >= 1 be the number of direction symbols, k >= 0 the number of distinguished provenance tags, and L >= 1 the complete paired-event tail depth. The alphabet is A=[m] x ({0} union [k]), of size a=m(k+1); 0 is the neutral tag. Each finite word maps to its final-appearance order of nonneutral tags and its last min(L, word length) complete paired events, yielding the finite monoid J=J_(m,k,L). This observation algebra is separate from the six native spatial axes and the one temporal dimension of P000.

For 0 <= r <= k, define

W_r = r! m^L sum_(j=0)^min(r,L) S(L+1,j+1),

T_r = sum_(j=r)^k binom(k-r,j-r) W_j,

where S(n,j) is a Stirling number of the second kind. R209 counts precisely W_r full-tail elements having any fixed support set of size r; R215 proves that a state with support size r has exactly T_r full-tail elements in its principal right ideal.

For short tails of length 0 <= h < L, define

G_h = sum_(d=0)^(L-h-1) a^d,

C_(h,r) = binom(k,r) m^h sum_(j=0)^r (-1)^j binom(r,j) (r+1-j)^h

for 0 <= r <= min(h,k), and C_(h,r)=0 otherwise. As usual 0^0=1 in the finite-word counting convention (the empty word).

## Theorem A — exact full distribution, not just per-state cardinality

For each integer t >= 0 the number H(t) of elements x of J for which |xJ|=t is

H(t) =
 sum_(r=0)^k binom(k,r) W_r * [t=T_r]
 + sum_(h=0)^(L-1) sum_(r=0)^min(h,k) C_(h,r) * [t=T_r+G_h].

Here [P] is 1 if P holds and 0 otherwise. If numerical cardinalities coincide across categories, their multiplicities are added. Therefore every nonnegative integer power moment is exactly

M_p = sum_(x in J) |xJ|^p
    = sum_r binom(k,r) W_r T_r^p
      + sum_(h<L) sum_(r<=min(h,k)) C_(h,r) (T_r+G_h)^p.

In particular, M_0=|J|, M_1 is the number of ordered pairs (x,y) with y in xJ, the mean right-ideal cardinality is M_1/M_0, and the variance is M_2/M_0-(M_1/M_0)^2.

**Proof.** Fix a support set U of size r. Each length-h word over direction/provenance pairs whose nonneutral tags belong to U has m^h(r+1)^h possibilities. Inclusion-exclusion over the r required nonneutral tags gives m^h sum_j (-1)^j binom(r,j)(r+1-j)^h words using each tag of U at least once. There are binom(k,r) choices of U, proving C_(h,r). A word shorter than L is a unique J-state and all such states are exhausted by (h,r). For full-tail states R209 gives binom(k,r)W_r states of support size r. These are disjoint from short states and exhaust J.

By R215, a full-tail state of support size r has principal right ideal size T_r; a short word of length h and support size r has principal right ideal size T_r+G_h, as its short right multiples are precisely its short literal extensions of lengths h,...,L-1. Grouping the disjoint sectors by their cardinalities proves H(t). Summing t^p over this exact histogram gives M_p. QED.

No enumeration of the |J| states is needed to obtain H, M_1, or M_2: direct integer combinatorics evaluates at most (k+1) full categories and sum_(h<L)(min(h,k)+1) short categories. This is a count of formula categories, not a promise of constant-time bit complexity. All positive observations are retained on the original full state; the histogram is a separate query-specific readout.

## Theorem B — precise threshold for right ideals to be two-sided

For every m>=1, k>=0 and L>=1,

    (for every x in J, xJ=JxJ)
    if and only if
    (a=1 or L<=2).

**Proof.** R213 supplies the principal ideal membership formula. For a full-tail x, xJ=JxJ is the full-tail set of states with supports containing S(x), for every L. For the empty short x, both ideals equal J. When L<=2, each nonempty short x has length 1; it is the only short state in either ideal, and both full-tail sectors coincide, so the ideals agree. If a=1, J is the monogenic truncated-word monoid, hence commutative, so all right ideals are two-sided.

Conversely assume a>=2 and L>=3. Choose two distinct events x,y of A; regard x as a length-1 short state. The length-2 state yx belongs to JxJ, but not to xJ because its short literal word does not have x as prefix. Thus these two principal ideals differ. QED.

For L<=2 the right-ideal cardinality histogram H is also exactly the two-sided ideal cardinality histogram. For L>=3 and a>=2, the latter can depend on short-word self-overlaps as R215 shows.

## Exact X6-compatible observer example: m=12, k=6, L=2

This is the paired-event observation alphabet with 12 signed native directions and six selected provenance tags; it is not a compression of complete physical states. There are |J|=1,407,685 observable states. The exact histogram (right and two-sided ideal cardinality t : multiplicity H(t)) is

518400 : 518400
604800 : 518400
708480 : 259200
833760 : 86400
986400 : 21600
1174176 : 3456
1174177 : 72
1407600 : 144
1407601 : 12
1407685 : 1.

Thus there are exactly ten distinct numerical ideal cardinalities. The aggregate incidence is

M_1=863611486297,
M_2=545292876127030381,

E(|xJ|)=863611486297/1407685,

Var(|xJ|)=21775803066765343105776/1981577059225,

with x chosen uniformly from J. These are exact rational values, with no floating-point approximation. The three short categories consist of the identity (1 state), one neutral-tag event (12 states) and one selected-tag event (72 states).

The pair (x, y) counted by M_1 is an algebraic reachability/ideal-membership pair, not a physical branch interaction, weight or native residual measurement. R214's 8-bit quotient is valid for the declared ideal membership language only; the 21-bit full-action encoding, tagged source relationships and native BRC carrier remain available for richer observations.

## Validation

R219_principal_ideal_incidence_check.py is a standard-library Python exact reference checker. It constructs complete finite monoids by generator BFS with retained word representatives, independently computes all pairwise products and principal right and two-sided ideal sets, then compares the observed right-ideal-size histograms to Theorem A and checks Theorem B model by model. It evaluates the X6 parameters by exact combinatorial formulas, not by enumerating 1.4 million states.

The executed reference test covered 15 finite parameter models, 377 distinct states, 21,737 multiplication-table entries, every principal right ideal and every principal two-sided ideal in those models. All assertions passed. The full model inventory and deterministic outputs are in R219_verification.json. The symbolic proofs above establish general parameters; the finite check is independent corroboration. Independent mathematical review: NOT_REVIEWED.

## Scientific continuation

1. Derive an exact distribution of two-sided ideal sizes for arbitrary L by classifying short patterns through their border autocorrelation signatures, and compare to the R216 border-spectrum frontier without duplicating it.
2. Evaluate the grouped R214 full-state rank extraction and ideal-cardinality readout on the installed native BRC EffectHistogram adapter while retaining typed source, signed/phase, positive rational weight, multiplicity and cross moments. Native execution and benchmark remain NOT_EXECUTED.
3. Continue the depth-2 binary-affine representation gap of R205 (31 to 35 dimensions) as a separate structural unit.

No Task CLAIM, formal Result, independent review or Foundation admission is asserted by this portable publication.
