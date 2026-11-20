# X6 R49 — Exact BRC root tomography under an unknown common additive offset

Date: 2026-11-20. Research mode: independent portable TASK_RESEARCH continuation of R44–R48. Author-reported proof, exact rational checks, NOT_INDEPENDENTLY_REVIEWED.

## Mathematical object and provenance

Use the *conditional* positive-weighted two-source R44/R47 graph, with integer Port count p >= 1 and positive source weights alpha,beta. Its four labelled BRC root masses are

\[
X=pS,\qquad Y=(p-1)S,\qquad D=2(p^2-1)P,\qquad H=2pP,
\]
where \(S=\alpha+\beta>0,\ P=\alpha\beta>0,\ 4P\le S^2\).
These coefficients are established for that declared graph in R47; R48 analyzed independent bounded coordinate errors.

**New observation model.** The same *unknown real additive measurement offset* \(b\) affects all four measured channels, without changing underlying path weights:
\[
(x,y,d,h)=(X+b,Y+b,D+b,H+b).
\]
The offset may be positive, zero or negative. Negative measured values are permitted as offset-corrected readouts; the underlying BRC masses are positive or zero. This is a measurement-level model, not an extra native event.

## R49.1 — Exact joint identifiability despite arbitrary common offset

**Theorem.** For every \(p\in\mathbb Z_{\ge1}\), \(\alpha,\beta>0\), and \(b\in\mathbb R\), the exact four-tuple \((x,y,d,h)\) uniquely determines
(1) p, (2) the unordered pair \(\{\alpha,\beta\}\), and (3) b.
There is no prior bound on p or b.

**Proof.** Take the three offset-invariant differences
\[
s=x-y=S,\qquad k=x-h=p(S-2P),\qquad e=d-h=2(p^2-p-1)P.
\]
Thus s > 0, and the sign of e is negative exactly for p=1 and positive exactly for p >= 2. In particular e is never zero.

For an arbitrary candidate integer q >= 1, the first two differences force
\[
P_q=\frac{qs-k}{2q}=\frac12(s-k/q).
\]
The third difference is then equivalent to
\[
e=f(q),\qquad f(q)=(q^2-q-1)(s-k/q).
\]
If e < 0 only q=1 can be feasible (because \(P_q>0\)); its complete readout can be checked directly.

If e > 0, feasible candidates have q >= 2 and \(s-k/q>0\). On the corresponding connected real domain, f is strictly increasing:
\[
f'(q)=s(2q-1)-k(1+q^{-2}).
\]
For k <= 0, this derivative is positive for q >= 2. For k > 0, feasibility entails k < qs, and hence
\[
f'(q)>s\left(q-1-\frac1q\right)>0\quad(q\ge2).
\]
Therefore at most one feasible integer q >= 2 solves e=f(q). The actual p exists by construction, so it is unique. Because f(q) tends to positive infinity as q grows, the search by increasing integer q starting above max(2,k/s) terminates.

After finding p, recover \(P=(ps-k)/(2p)\), \(b=x-ps\), and \(\alpha,\beta\) as the two positive roots of
\[
t^2-st+P=0,\qquad
\{\alpha,\beta\}=\left\{\frac{s+\sqrt{s^2-4P}}2,\frac{s-\sqrt{s^2-4P}}2\right\}.
\]
Their order is not recoverable because the original graph is symmetric under swapping source names in this coarse readout. QED.

**Exact consistency test for arbitrary four-channel data.** First require s>0 and e != 0. If e<0 test q=1; if e>0 search q>=2 as above. For the unique proposed q, require \(P_q>0,\ 4P_q\le s^2\) and exact regeneration of all four observed readings with b=x-qs. Failure means the observation lies outside the declared common-offset model. This is a terminating decision procedure over exact rationals; the algebraic statement also applies to real inputs with exact comparisons.

## R49.2 — Four measurements resolve an exact three-measurement ambiguity

Dropping D is not generally safe. Consider two different parameter sets:
\[
(p,\alpha,\beta,b)=(3,1,2,0)
\quad\hbox{and}\quad
(2,3/2,3/2,3).
\]
Both produce precisely \((x,y,h)=(9,6,12)\), yet their fourth observations are \(d=32\) and \(d=33/2\), respectively.
Thus the pair is exactly aliased under the declared three-channel observer and distinguished by D. The example does not claim that *every* possible three-channel selection fails, or that four are minimal under additional calibration constraints.

## Verification and scientific boundary

The accompanying standard-library Python 3 Fraction program independently reconstructs all four readings, searches candidates q=1..30, and compares to an exact terminating inverse without a hard Port-count cutoff. It checks all 1,500 combinations
p=1..12; alpha,beta in {1/2,1,3/2,2,3}; b in {-7,-2,0,5/3,11}.
It also verifies the exact three-channel alias. All assertions pass; the general theorem rests on the symbolic argument, not finite sampling. No float approximation, unvalidated empirical inference or formal checker is used.

Frozen scientific substrate: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5), with current ACTIVE joint-observer preservation and X6 six-axis/three-dimensional-slice meanings. The R44 conditional releases/reoccupations R,T and the present additive bias are **not** asserted to be admitted TRIADIC_CLOSURE_E native physical operations. R49 requires neither erasure of Port/source joint relations nor new P000 axioms.

Prior material: R47 paper research_notes/portable_direct/2026-11-20_x6_r47_blind_source_port_weight_tomography.md; R48 paper research_notes/portable_direct/2026-11-20_x6_r48_finite_resolution_blind_brc_inversion.md. R49 adds a common-mode additive drift with no bound or calibration, distinct from R47's common multiplicative gain and R48's independent bounded errors.

## Next discriminating questions

1. With a common unknown offset plus independently bounded rational measurement errors, derive an exact correlated-polytope feasibility certificate for p and positive alpha,beta, retaining the shared offset rather than treating four errors as independent boxes.
2. Determine which smaller sets of BRC root coefficients identify p with only partial calibration, and construct all exact observation aliases.
3. Establish or refute a source/Port/Cell/Link trace-preserving embedding of R44–R49 into genuinely admissible TRIADIC_CLOSURE_E native events. No such embedding is asserted here.

Evidence code: research_notes/portable_direct/x6_r49_common_offset_tomography_verify.py.
Evidence JSON: research_notes/portable_direct/x6_r49_common_offset_tomography_results.json.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_RATIONAL_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
