# R179 — 有序来源与独立支路的 X6 单寄存器仿射保真

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_CHECKED / NOT_REVIEWED.

## Scientific provenance and scope

Continues R175–R178, in particular immutable R178 source commit b6b1f661422ade1329a9401797b6d4833c0b8e70, research_notes/portable_direct/R178_LOSSLESS_CHRONOLOGICAL_X6_PATH_AFFINE_LIFT_20261115.md. Scientific input retains the prior lane's frozen pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34, without refreeze. P000 keeps six native spatial axes, twelve signed primitive directions, and separately typed provenance and branch identity. The additional register below is not a spatial axis or a heartbeat time variable.

Actual Source interface inspected: src/enterprise_math/brc_transport.py at blob be1debe367263931bd5e93fd750be3ed54624fe1. Its Affine.then is chronological composition; EffectHistogram.from_terms coalesces equal (positive rational weight, affine effect), adding integer multiplicity. An ordered **spatial** path code alone therefore loses independent branch IDs when source/path/weight coincide.

## Definitions

Let S be the twelve signed X6 directions, I a finite set of distinct atomic branch identifiers, and M a finite set of source/provenance labels. Define a disjoint tagged alphabet

\[
\Sigma=S\sqcup\mathsf I(I)\sqcup\mathsf M(M)\sqcup\{\#\},\qquad K=13+|I|+|M|.
\]

Choose a bijection c: Sigma -> {0,...,K-1}. Encode each atomic branch a=(i,m,P), P a finite signed-native path, as the token word

\[
\tau(a)=\mathsf I(i)\,\mathsf M(m)\,P\,\#.
\]

Concatenation of these words encodes an ordered sequence of atomic branch histories. Distinct token classes and the terminal marker yield a unique parsing back into IDs, sources and ordered primitive steps. Different branches that must remain observable receive distinct IDs.

For arbitrary tagged word w let pi(w) erase metadata and retain its native step sequence P. Put m(w)=|P|, D(w)=the six-axis sum of its steps, and J(w)=the sum of its native-step prefix displacements. Metadata does not count as a native step. Define

\[
h_K(w)=\sum_{r=1}^{|w|} c(w_r)K^{|w|-r},\quad \lambda_K(w)=K^{|w|}.
\]

## R179A — complete affine monoid embedding

On the 13-dimensional rational state (x,j,h) in Q^6 x Q^6 x Q define

\[
T_w(x,j,h)=(x+D(w),\;j+m(w)x+J(w),\;K^{|w|}h+h_K(w)).
\]

**Theorem.** For all finite tagged words u,v,

\[
T_u.\mathrm{then}(T_v)=T_{uv},
\qquad
T_u=T_v\iff u=v.
\]

**Proof.** The erasure pi respects concatenation, hence

\[
m(uv)=m(u)+m(v),\quad D(uv)=D(u)+D(v),
\]
\[
J(uv)=J(u)+J(v)+m(v)D(u).
\]

For the tagged positional register,

\[
\lambda_K(uv)=\lambda_K(u)\lambda_K(v),\quad
h_K(uv)=K^{|v|}h_K(u)+h_K(v).
\]

Substitution into the 13-dimensional affine action yields the first formula. Equality of two actions entails equality of their h-slopes, hence |u|=|v| because K>=2. Equality of h-translations then gives h_K(u)=h_K(v); fixed-length base-K expansions with digits {0,...,K-1}, including leading zeros, are unique. Thus u=v. The converse is immediate. QED.

This stores the **entire typed tagged history** in one extra affine register, even when two histories have the same endpoint, native-step count and all native prefix moments.

## R179B — exact identity-sensitive BRC packet lifting

For each history w, take a positive rational weight q and a positive integer multiplicity n and build one term (q,T_w,n) for EffectHistogram. By R179A,

\[
(q,T_u)=(r,T_v)\iff (q,u)=(r,v).
\]

The histogram's exact coalescence preserves full tagged-history equivalence classes and sums only their true multiplicities. Alternatives correspond to multiset sum. Serial composition has output terms (qr,T_{uv},ns) from each ordered input pair, which is precisely the Cauchy product of weighted history multisets. Source-monoid products, selectors, raw native paths and future observers can be evaluated on the decoded histories.

**Collision witness and repair.** Two branches a,b with different IDs but both source red, weight 1/2, and native path (+E1,-E1) have the same R178 spatial-only effect. A native histogram of two such untagged effects coalesces them into one entry with multiplicity 2, losing the branch-ID selection. Their tagged words differ in the ID token, and R179A produces two different effects and thus two entries of multiplicity 1.

This is exact preservation for the declared typed observation and all future serial/alternative histogram operations, with distinct identifiers supplied for branches that need to remain distinct. No unproved projection discards joint provenance.

## R179C — dimension and information trade-off

The affine dimension is 13, independent of the finite numbers |I| and |M|; the earlier R177–R178 finite provenance-state construction uses a label-dependent auxiliary affine block. The reduced dimension comes with growing integer coefficients. At tagged length L, slope K^L and positional code h_K require O(L log K) bits. The K^L possible words are bijective with the integers 0,...,K^L-1 via h_K; a uniform binary code of fixed word length L needs at least ceil(L log2 K) bits, achieved by the positional integer (apart from customary zero-width conventions). This is a bit-size statement, not a claim that dense matrix computation beats a raw token sequence.

All native spatial quantities remain six-axis and metadata tokens are excluded from the native-step count. Chronological word order is encoded algebraically, without assigning a physical heartbeat interval.

## Reproduction and verification

The attached standalone Python source R179_tagged_x6_affine_check.py uses exact integer and Fraction arithmetic. R179_verification.json contains its output.

For I={a,b,c} and M={red,blue}, K=18 and dimension=13, with deterministic seed 179:

- Full fixed-length positional-code injection over all 6175 tagged raw words of length 0 to 3.
- 90 atomic ID/source/path cases (path length 0 to 3 over two signed native directions), all individually decoded and distinct.
- 8100 ordered atomic pairs with exact statistics/concatenation and unique parsing.
- 500 complete 13 x 13 affine composition checks.
- 50 positive-rational histogram multiplication cases, plus a branch-ID loss/repair witness.

All standalone checks passed. An optional native import-and-composition test is included. In the current local sandbox it returned "No module named 'enterprise_math'"; actual native project-package execution is LOCAL_VALIDATION_PENDING. The mathematical claims have author-side symbolic proofs, independent mathematical review is NOT_REVIEWED.

## Research and control status

Independent portable research output only; no fresh formal Task/CLAIM/Result/Review or owner transition is asserted. The prior source activity is RA-7A118452894D2600AE7DE5A2 (historical researcher EM-DIRECT-BF4AD7, Session MCP-46f202db13e64ad6b4c8860e06908245). The new activity checkpoint and authenticated observation association require their own real authorized write/readback.

Next valuable unit: execute this exact native adapter in an installed Enterprise Math runtime, compare tagged-word bit/operation costs against R177 label-simplex action and explicit token arrays, and develop a self-delimiting finite-alphabet variant for unbounded branch/source IDs.
