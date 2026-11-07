# EC49BQ — Exponential BRC memory-rank jump under compositional end filters

**2026-10-30 | AUTHOR_ANALYTIC_PROOF / EXACT_NATIVE_BRC_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**

## Object and question

Use all 12 original signed X6 directions D={±E_i,1≤i≤6}. The finite word universe U_n is **all ordered length-n zero-displacement words**, n even. Fix strictly positive rational weights w_i^+,w_i^- and the single-word BRC weight χ(t)=product of signed-step weights. For arbitrary selected path multiplicities μ:U_n→Q_nonnegative, a future filter F returns the sum of μ(t)χ(t) over paths satisfying F. This is a clearly declared mathematical selected-ensemble/filter extension. The pinned native signed_brc.py endpoint_weight function computes the unfiltered μ≡1 sum but does not implement selection.

For 1≤r with even n≥4r, let P_r(t) and S_r(t) be the first and last r **ordered, signed** steps, and N=12^r. Compare (A) one-shot observations P_r=p OR S_r=s, one filter per future observation, with (B) sequentially composable filters, including P_r=p AND S_r=s. Both include unfiltered weight. Optionally the exact original path count is additionally observable. Axis labels and the weight instrument stay fixed; word inversion exchanges sign-reversed prefix and suffix and preserves χ for closed paths. General axis-group actions/interior surgery are not assumed.

**Theorem.** For every even n≥4r≥4 and every strictly positive rational direction-weight table, the exact minimum number of rational-linear additive coordinates sufficient for all weighted observations is

    one-shot: 2N−1 ; sequentially composed: N².

When original path count is also observed, let q_i=w_i^+ w_i^-. If all q_i are equal, both ranks stay unchanged. If any q_i differ, the ranks are exactly 2N and N²+1, respectively. The minimality claim ranges over all nonnegative rational selected ensembles and all rational-linear additive statistics; it is NOT an arbitrary bit-encoding lower bound.

## Proof

**Every end-pair exists.** Given any signed length-r words p,s, concatenate

    p | inverse(p) | (+E_1,−E_1)^((n−4r)/2) | inverse(s) | s.

Inverse means reverse order and flip each sign. This has length n, zero displacement, and the prescribed prefix p and suffix s. Thus all N² end-pair cells are nonempty.

**One-shot span.** The 2N row functions are f_p(t)=χ(t)1[P_r(t)=p] and g_s(t)=χ(t)1[S_r(t)=s]. A relation sum_p a_p f_p + sum_s b_s g_s=0 evaluated on any nonempty end pair (p,s) gives χ(t)(a_p+b_s)=0, and χ(t)>0. Thus all a_p=c and all b_s=−c. There is precisely one independent relation. The unfiltered row is sum_p f_p, so the rank is 2N−1.

**Composition span.** A sequential prefix-plus-suffix filter produces h_(p,s)(t)=χ(t)1[P_r=p,S_r=s]. All N² such rows have pairwise disjoint, nonempty supports, hence are independent. Every allowed end-filter composition is a union of such cells, so the span has rank N².

**Independent count criterion.** Closed words have equal plus and minus occurrences k_i on each axis and sum_i k_i=n/2, so χ(t)=product_i q_i^(k_i). If q_i=q for all i, χ=q^(n/2) everywhere, and count is q^(−n/2) times unfiltered weight. If q_i≠q_j, choose ends p=(+E_i)^r and s=(−E_i)^r. Complete the middle length n−2r using either repeated i-axis roundtrips or repeated j-axis roundtrips. They share the same (p,s) cell but their weights differ by (q_i/q_j)^((n−2r)/2)≠1. Every function in the composed weighted row span is proportional to χ *within* each cell, whereas count is 1 on both witnesses. Thus count is independent of the larger composed span, and also of the one-shot subspan, adding exactly one coordinate.

**Exact minimality.** Reuse the proved EC49BP finite-U row-span principle. For any purported sufficient rational-linear additive statistic S, take z in its rational kernel and a rational nonnegative baseline a large enough that a+z is also nonnegative. Identical S on a and a+z forces every legal output row to annihilate z. Hence the row span of S contains the entire observer row span; its rank cannot be lower. The displayed row bases attain the lower bounds. QED.

## Strict same-marginal, different-composition witness

Take n=4,r=1, positive weights w+=(2,3,3,2,1,1), w−=(1,1,1,1,1,1). Define t(a,b)=(+E_a,−E_a,−E_b,+E_b). Compare the two rational ensembles with unit multiplicities:

    A={t(1,2),t(4,3)}
    B={t(1,3),t(4,2)}.

All four single-path weights are exactly 6. Both have count 2 and total weight 12; **every individual signed prefix and suffix weighted filter agrees** on A,B. But the sequential filter first P_1=+E_1 and then S_1=+E_2 returns A→6 and B→0. The state sufficient for one-shot observations is not sufficient after composition. Here q=(2,3,3,2,1,1), so exact ranks with path count are **24 versus 145**; without count 23 versus 144. At r=2, n≥8, the analytic formula gives 288 versus 20737 with count. No exhaustive n=8 enumeration was performed.

## Native BRC correspondence and executed exact audit

For any ends p,s, write L=n−2r. Every path in their joint cell uniquely has middle m of length L and displacement −Δ(p)−Δ(s), preserving the native signed-axis identities. Thus the exact all-path weight in that cell equals

    χ(p) * endpoint_weight(L,−Δ(p)−Δ(s),w+,w−) * χ(s).

Replace endpoint_weight with endpoint_multiplicity for the count. This is a typed factorization into the original BRC source, not a generic numeric model renamed BRC.

The actually executed release program VERIFY_EC49BQ.py imports the project kernel at experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py and checks its exact Git Blob 300a96e3dc24bf6fff73743037a0347a8bc83176 before use. With Python Fraction and SymPy: fully enumerated all **396** length-4 closed signed X6 paths; native unfiltered endpoint weight **1560**; audited all **144** nonempty prefix–suffix fibres against native BRC counts and weights (12 fibres of size 1, 120 of size 2, 12 of size 12); directly checked rational one-shot matrix ranks **23** and **24**; and verified the 6/0 two-ensemble witness. For n=6, 144 native middle-kernel evaluations give exactly **19920** closed words and native total weight **152640**. Two executions produced byte-identical exact JSON. General n,r claims rest on the analytic proof above, not finite sampling.

## Scope and next

This is an author-side, unreviewed theorem about the finite static X6 **ordered non-shortest walk universe**, positive exact BRC weights and a declared auxiliary selected-ensemble filter interface. The native endpoint API still only aggregates the full compatible path set. It does not claim physical heartbeat time, complex amplitude evolution, native filter implementation or project mathematical admission. P000 and ACTIVE worldview remain unchanged. The general future-observer row-space idea is related to established Myhill–Nerode/weighted-automata Hankel theory; only the project-specific theorem, bounds, witness and BRC certificate are claimed as this unit's incremental work.

**Next EC49BR:** analyze nontrivial H≤S6 fixed/covariant weight-instrument actions on the joint-filter orbit row span and construct an exact native-BRC bridge to any real selection interface before claiming software support.
