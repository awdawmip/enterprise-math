# R116 — Exact online universe refinement and Top-k capacity transfer

Date: 2026-11-13. Enterprise Math Research1. Author-side **finite ranked Boolean auxiliary model** continuing R115-SIG, exact predecessor commit 70bdc1abf3ce2ffa8d9ba7501181bcfb53846d77 at research_notes/brc_s23_av_r115_signature_rank_20261113/PROOF.md. Earlier bounded-future R115 at 5086853083aa88d3cf8d25a1fc54f6435d7b4d2f is preserved separately. Frozen scientific source pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This work is an auxiliary Boolean observer theorem, not an assertion about native Cell/Link/Port admission or an alteration of P000.

## 1. Exact domain

Let I=[a,b] be a nonempty closed rational parameter interval, and let U0 be a finite strictly ranked set of complete source identities (t,branch). Different branches at time t share the same Boolean eligibility predicate M_t(theta). Each predicate has a finite, exactly constructible rational-cut atomization, constant on every singleton cut atom and every open-gap atom. Let F,G be arbitrary subsets of U0 and C=F∩G, D=F△G.

Top_k(F,theta) is the descending list of the first k eligible complete identities, truncated after its final available identity. If an eligible D identity exists, let d(theta) be its **highest-ranked** member and set

    h(F,G;theta) = #{v in C : v > d(theta) and M_time(v)(theta)=1}.

Otherwise h=+infinity. Set K(F,G;I)=min_{theta in I} h(F,G;theta). The minimum is attained on a rational singleton/open-gap representative in the finite atomization. By the first-difference lemma from R112/R115-SIG,

    Top_k(F,theta)=Top_k(G,theta) iff k <= h(F,G;theta),

for every positive integer k. Thus equality throughout I holds exactly for k <= K(F,G;I).

Now adjoin a new potential time s absent from U0, with a nonempty finite family Vs of complete identities at s. Write U1=U0 union Vs. The newly supplied predicate M_s has the same exact finite-cut property. First enlarge only the potential universe, keeping F,G subsets of U0. Subsequently add a single u in Vs to one or both histories.

## 2. R116.1 — Exact future-signature refinement

Let T0 be the time set of U0. Define sigma0(theta)=(M_t(theta))_(t in T0) and sigma1(theta)=(sigma0(theta),M_s(theta)). Let S0 and S1 be their respective **sets of attained signatures**, d0=|S0|, d1=|S1|. For each z in S0 let P_z={theta in I:sigma0(theta)=z}; P_z need not be connected. Define e_z=1 exactly when P_z intersects both {M_s=0} and {M_s=1}, otherwise e_z=0.

**Theorem A (abstract-state count).**

    d1 = d0 + sum_(z in S0) e_z, so d0 <= d1 <= 2*d0.

Proof. Forgetting the final bit projects S1 surjectively onto S0. The fiber of an old z contains one or two distinct children, with two precisely if e_z=1. Count all fibers. QED.

Let J0,...,J_(q-1) be the ordered exact rational atom grid obtained by refining all old and new cuts, including singleton endpoints, and rho_i their rational representatives. Put a_i=sigma0(rho_i), b_i=M_s(rho_i). Write N_conn(sigma) for the number of maximal consecutive runs of equal signatures.

**Theorem B (connected-state count).**

    N_conn(sigma1)-N_conn(sigma0)
      = sum_(i=0)^(q-2) 1[a_i=a_(i+1) and b_i != b_(i+1)].

Proof. Every old signature boundary survives adjoining a bit. A formerly absent boundary becomes present exactly when the new bit flips. Count boundaries plus one. This handles discontinuities and half-open endpoint membership because every endpoint is a separate exact atom. QED.

**Minimal-observer consequence.** For all possible future F',G' subsets of U1 and every positive k, equal sigma1 signatures imply equal truth values of Top_k(F',theta)=Top_k(G',theta). If two signatures differ at time t, the histories F'={(t,b)}, G'=empty and k=1 distinguish them, using any identity (t,b) in U1. Therefore sigma1 is the coarsest abstract state retaining *all* such future equality predicates, while Theorem B gives the coarsest connected representation of that observation.

The abstract and connected counts can diverge. With U0 containing only an always-ineligible time and a new s eligible on the five intervals [1/10,2/10), [3/10,4/10), [5/10,6/10), [7/10,8/10), [9/10,1), the distinct-signature count is 1 -> 2, while the connected-run count is 1 -> 11. An explicit connected output therefore requires Ω(N_conn) cells even when the abstract signature count is two.

## 3. R116.2 — Exact zero-rank-work inheritance

**Theorem C (potential-universe extension).** Before any membership edit, for each attained child (z,b) in S1,

    h_new(z,b) = h_old(z).

Indeed every currently present identity belongs to U0. Its eligibility and strict ranking depend only on sigma0, hence every Top-k list and capacity is exactly unchanged by making a new but absent identity *potentially* available. With a persistent rank tree keyed by currently present complete identities, every child may reference the unchanged old rank root by pointer; only its signature-map entry is new. This preserves the identity, branch, history and rank information. QED.

At the first actual membership insertion, a dynamically keyed balanced rank map can insert the new identity with O(log(n+1)) path nodes for n existing keys. This structural bound assumes the keyed balanced map. It excludes rational cut construction, arbitrary-precision bit operations, signature-map materialization and source-set membership costs.

## 4. R116.3 — First insertion transfer formulas

Fix one new identity u=(s,b) absent from F and G. Define its old higher-ranked eligible common prefix

    c_u(theta) = #{v in F∩G : v>u and M_time(v)(theta)=1}.

**Theorem D (one-sided insertion).** After adding u to exactly one of F or G,

    h'(theta) = h(theta)                       if M_s(theta)=0,
    h'(theta) = min(h(theta),c_u(theta))       if M_s(theta)=1.

In particular, interpreting min(empty)=+infinity,

    K' = min(K, min_{theta in I : M_s(theta)=1} c_u(theta)).

Proof. When u is ineligible there is no change. Otherwise, if the old highest eligible difference d outranks u, the first difference remains d, and every eligible common source outranking d also outranks u, hence c_u>=h. If u outranks d, it becomes the new highest difference, whose common prefix is precisely c_u<=h. If there was no old eligible difference then h=+infinity and u becomes the first difference. In all cases the local minimum formula holds, and minimizing over the refined finite rational atomization gives the global formula. QED.

**Lazy corollary.** To obtain the new whole-interval all-k capacity after the first one-sided insertion, it suffices to intersect the old signature fibers with the active region of M_s, calculate c_u on the intersecting old signatures, and take the minimum with the old K. One need not construct every new rank-tree root for this single capacity answer. Exactly discovering intersections and evaluating rank prefixes still incur real work.

**Theorem E (joint insertion).** If u is inserted into *both* F and G, D stays fixed. Where an eligible old highest difference d exists,

    h'(theta) = h(theta) + 1[M_s(theta)=1 and u>d(theta)].

Where no eligible old difference exists, h'=h=+infinity. Proof. A newly eligible common identity adds one element above the unchanged highest difference precisely in the indicated case. Consequently one-sided insertion makes K nonincreasing; common insertion makes K nondecreasing. QED.

A finite K' yields an exact rational witness: a representative theta attaining h'=K' makes Top_(K'+1) disagree. Directed example: F=G={(1,0)}, M_1=[1/2,1), add u=(0,0) to F only, M_0=[1/3,2/3). At theta=2/5 the new capacity is zero and Top-1 differs; at theta=3/5 the capacity is one and Top-1 agrees.

## 5. Verifier, cost scope and actual results

The attached Python 3 checker uses fractions.Fraction for every rational endpoint and atom representative; all eligibility and rank predicates are exact. It enumerates old and new singleton/open-gap atoms, constructs full source lists independently, and compares Top-k directly for k=1,...,23. It checks Theorems A-E and an immutable old-rank-root object-reference inheritance model, not a deployed persistent balanced-tree implementation or runtime benchmark.

Run (after decoding the attached gzip+base64 source):

    python check_r116.py

Observed deterministic output, seed 1162026:

    R116_PASS 360 17732 815672 34382 17732 741 631

There are 360 randomized history instances, 17,732 exact rational atoms, 815,672 direct Top-k comparisons, 34,382 difference-witness checks, 17,732 common-insertion checks, 741 total abstract-signature splits and 631 newly introduced connected boundaries. The code also checks 5,656 inherited old root references and 2,492 active-new-time signature rows. Directed assertions cover +infinity -> 3, 3 -> 0, 2 -> 2, and the rational 2/5 vs 3/5 witness. Raw metrics and samples are retained in verification_r116.json.

An online outer signature map can clone old references during expansion; after it has materialized d1 distinct signatures, the first actual new membership insertion only changes the d_s rows for which M_s=1. A dynamically keyed persistent rank map and outer balanced map can update their paths using O(d_s(log(n+1)+log(d1+1))) nodes, **conditional on preprocessing and accurate active-fiber intersection**. The present checker is an independent exact formula verifier, not that full data-structure implementation. Real costs of constructing phase cuts, rational sort and bit lengths, source membership, materializing connected intervals, and historical memory remain to be benchmarked.

## 6. Unfinished R117 frontier and provenance

The next unit is to implement a genuinely persistent keyed rank tree together with an online rational-cut tree, verify split/merge/reintroduction over multiple newly introduced times, quantify live and retained history memory and rational bit operations, and compare with full rebuilding under adversarial oscillatory predicates. A separate S23 question is whether its six affine-phase predicates support active-fiber intersection without enumerating all algebraic cuts.

Read provenance: current canonical global knowledge 7bbbdf8c5b5cc5b92f7c82ad093d1b8626eef1a8, current Source control fcc83f5469de9cdccdee30d6b856d745a838de31, frozen science 43ec6098b1330ae86d0a7863be336c5d97f6ef34. On 2026-11-13 the native exact S23 task request returned NO_CANONICAL_PUBLICATION_DIRECTORY, with native operational owner not evaluated. This is **independent author-side research**, not a formal TASK CLAIM or independent acceptance.
