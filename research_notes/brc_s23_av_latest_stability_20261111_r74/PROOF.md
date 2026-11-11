# R74 / S23-AV: Complete latest-source-time stability by two exact affine-arc tests

**Status:** Author-side mathematical result for the frozen S23/AV auxiliary rational-circle model. Frozen scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged). Predecessors: R72 at 917f62a46d986a757476e0e4bc35ad603eba4fb9, R73 (first-entry exact theorem) at 7230816201f56d70526568a69bb87211adc0602b. This is not a native BRC/X6 theorem, canonical Result, CLAIM, Review or accepted working truth.

## 1. Precise question

The fixed finite population is independently keyed (t,branch) source events with integer time t. Observer has integer time j and rational phase x. Real theta ranges over a rational closed interval I=[L,U]. The original labelled target arc has affine endpoints A(theta)={a theta}, B(theta)={b theta}, with constant boundary floors and 0<=A(theta)<B(theta)<1 throughout I.

A source with time t qualifies at theta precisely when {x+(t-j)theta} belongs to [A(theta),B(theta)). Let T(theta) be the maximum qualifying source time t, or NONE when no event qualifies. Branch labels remain independently stored; the present auxiliary phase depends only on t, not branch. Question: decide exactly whether T(theta) is constant over **all real theta in I**, and construct two rational witnesses if it changes.

## 2. The complement unwrapping lemma

For any phase alpha and 0<=A<B<1, the complement of [A,B) on the circle is [B,1) union [0,A). It is exactly the unwrapped half-open interval [B,A+1) considered modulo integer translations. Formally:

    {alpha} not in [A,B)
    <=> exists integer k: B+k <= alpha < A+1+k.

This retains the original convention: A is included in the target and excluded from the complement; B is excluded from the target and included in the complement. Complement width 1-(B-A) is strictly positive, even when A=0 at an endpoint.

For general affine lower/upper functions C(theta)<D(theta), alpha(theta)=x+(t-j)theta, define u=alpha-C, v=alpha-D. Existence of a translated half-open interval member is equivalent to v(theta)<k<=u(theta) for some integer k. R73's exact first-entry theorem only requires D-C>0; it does not require C,D themselves to lie in [0,1). Hence its three tests apply to the target (C=A,D=B) and the complement (C=B,D=A+1) without splitting into possibly degenerate subarcs.

## 3. Complete per-source classifier

For a fixed source time, run the R73 O(1)-rational-operation exact oracle twice:

- E_in = there exists some theta in I inside the target [A,B), with rational witness theta_yes.
- E_out = there exists some theta in I inside the complement [B,A+1) modulo integers, with rational witness theta_no.

The arcs form a disjoint partition at each real parameter, so E_in and E_out cannot both be false. Classify:

- ALL_OUT when E_in=false.
- ALL_IN when E_out=false.
- MIXED when both are true. Preserve the two witnesses.

This is an exact interval-universal classification. Each oracle has a proof and witness construction; finite point sampling is not the basis of completeness.

## 4. Latest-time stability theorem

Group the retained event identities by exact integer time t. Inspect distinct times in strictly descending order, skipping all ALL_OUT time classes. If every time is ALL_OUT, T(theta)=NONE identically.

Otherwise let t* be the **first** non-ALL_OUT time. If t* is ALL_IN, then for every theta, t* qualifies and every greater time is absent, so T(theta)=t*. If t* is MIXED, then T(theta_yes)=t* because all higher times are absent, whereas at theta_no t* is absent and every higher time is absent, so T(theta_no)<t* or NONE. Thus T cannot be constant. Conversely a constant time T=t* necessarily is ALL_IN while all higher times are ALL_OUT, so the classifier is necessary and sufficient.

With an existing immutable ordered-time index this scans at most the n distinct times and uses O(n) rational operations. Unsorted input also requires sorting O(n log n) integer comparisons. Exact bit arithmetic for each visited time and returned rational witness is polynomial in the supplied integer/rational input bit lengths. This solves **uniform latest-time constancy**, not a unique branch-specific selection when branches may have different future semantics. An explicitly declared lexicographic tie rule could be applied to same-time branches in this auxiliary model without discarding their distinct identities.

## 5. Independent computational test

The executable Python Fraction checker performs 2416 valid random interval-model tests with deterministic seed 741126. It independently enumerates all rational roots at which a source's affine lift relative to target A/B reaches an integer, checks each root and every adjacent rational midpoint, then directly computes the latest qualifying time. The partition is exhaustive for the tested finite models because source membership can change only at one of these roots.

All checks passed: CHANGES 1380; STABLE 720; STABLE_NONE 316. The largest finite partition inspected contained 61 rational points. The checker verifies two exact rational witnesses for each CHANGES result yield different latest time. Cases include negative source times, signed labels, singleton parameter intervals and two independently keyed source branches sharing a time. A separate t of order 10^30 test returned a change witness without enumerating its enormous critical-point set. See check_r74.py and verification.json. The proof, not the finite tests, supplies the full-real-interval conclusion.

## 6. BRC/research scope and R75

The existing (t,branch) collection, time ordering, original labels and historical provenance are fully retained; this only changes a query algorithm. It is an auxiliary circle source model without a proved typed native X6/BRC interpretation. The next discriminating unit R75 is to integrate the two R73 oracles into R72's persistent phase-group index and compare **identical complete interval-latest-time queries**, counting preprocessing, immutable updates, rational bit operations, memory, tree access and witness recovery. Extend to branch-specific phase semantics and a clear tie policy; separately handle arcs that cross zero by exact parameter partition.
