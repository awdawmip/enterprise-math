# EC49GCI — Minimal canonical deficit atoms and atom-only dominance

2026-11-28. AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_ALL_BUDGET_REPLAY / NOT_REVIEWED.
Continuation of immutable 0dfad03c5aa13da0ed8acf73a63640bcccbda763:research_notes/portable_direct/EC49GCH_DISJOINT_DEFICIT_NORMALIZATION.md (blob a3dacb29b8cda5b5b673253ace89f270b11b0fc6). The exact generator and reference model are reused from GCH 87d4ce1097a05060ca603c7021d5f2c97288bd2a:research_artifacts/portable_direct/EC49GCH/disjoint_deficit_replay.js. This is an auxiliary strict-Hall combinatorial result; no new native BRC physical arithmetic or frozen archive replay, nor abstract-matroid novelty-priority claim.

## 1. Exact canonical sparse coordinates

Keep GCH's finite nonempty supports, positive integer port capacities, independent prefix S, remaining labeled suffix F, support-union closure W (including empty), n(W)=|F_W| and g(W)=r_(M/S)(F_W). Let D(W)=n(W)-g(W). By GCH D is exactly the disjoint-packing maximum for any intermediate quota a with g<=a<=q_S, using weights n-a. In particular D is nonnegative, monotone under inclusion, and superadditive on disjoint support unions. Define for every nonempty W:
    B_D(W)=max(0, max_{V proper subset W} D(V),
                 max_{V,Z nonempty disjoint; V union Z=W} [D(V)+D(Z)]).
All masks in the maxima are in the closure. Define the canonical atom list
    A(D) = {(W,D(W)): D(W)>B_D(W)}.
Empty maxima are omitted and D(empty)=0. An atom is a *joint support mask*, not an individual label or port.

Theorem: The exact canonical deficit is recovered at every W by the disjoint packing maximum of the atom weights in W. Moreover the atom list is the unique inclusion-minimal exact generator among weighted nonempty support masks using the same disjoint-packing reconstruction (after coalescing duplicates by max and omitting zero/negative weights). Every exact generator must contain every atom at its exact weight.

Proof: For any W the direct recurrence for reconstructing a packing is the GCH recurrence with local weight zero if the mask is not present. Induct on strict inclusion. All proper-subset and disjoint-split terms of the reconstructed value agree with B_D(W) by induction. If W is an atom its retained local weight is D(W); otherwise monotonicity and disjoint superadditivity give D(W)>=B_D(W), and non-atomicity gives equality. This establishes reconstruction, including empty closure. For necessity, any exact generator has local weight at V <= D(V), since the singleton packing is permitted. A packing inside W that does not use W itself either has proper union or splits into two nonempty disjoint subpackings with union W. Its weight is <=B_D(W). If W is an atom this cannot attain D(W), so an exact generator must retain weight D(W) at W. Conversely the atom list suffices; any extra weights are redundant. This is uniqueness only in the declared packing-generator language, not a lower bound on arbitrary encodings.

Construction without extra reconstruction: during GCH normalization compute inherited value B_D(W) before comparing with raw weight d(W)=n(W)-a(W). Then D(W)=max(B_D(W),d(W)); emit atom exactly if d(W)>B_D(W). In a fixed suffix, counts n are common, so the atom list is a canonical signature of the same finite future feasibility observer as GCC. Processed label and objective witness provenance remain outside the signature.

## 2. Atom-only exact dominance

For same suffix F and two prefix states S,T let D_S,D_T be their canonical deficits. Theorem:
    g_S(W)>=g_T(W) for all W iff
    D_T(V)>=w for every (V,w) in A(D_S).
Necessity is immediate. Sufficiency: by monotonicity and disjoint superadditivity of D_T, the value of every disjoint packing of S-atoms within W is <=D_T(W). Maximize and use exact reconstruction. Thus all inequalities follow. Empty atom list requires zero coordinate comparisons and corresponds to full rank on the suffix. Equality iff canonical lists identical. With GCB objective conditions p_S>=p_T,s_S>=s_T this supports all-budget dominance, preserving one original attaining witness. To compare, it suffices to query D_T at S's atom masks. In this replay D_T is available as a dense cache; an atom-only on-demand query engine is not implemented.

## 3. Cover-edge normalization

In GCH and the atom reconstruction, replace all strict inclusion predecessors by maximal proper predecessors (cover edges of the closure poset, excluding empty). Each proper nonempty V inside W is contained in at least one such predecessor; monotonicity proves identical maximum. Keep disjoint split edges unchanged. For u nonempty masks, p all proper containment edges, e cover edges, z disjoint pairs, normalization visits O(u+e+z) terms instead of O(u+p+z); construction costs and mask width are separate. In the replay, covers are built by descending mask order from all containment candidates, rejecting any candidate contained in an already retained maximal predecessor. The temporary full containment lists are retained for counting, not a claimed physical memory reduction. This is exact under the same joint support scope.

## 4. Executed replay and evidence

Executed JS seed 20261128; exact GCH 350-model generator with 2..7 ports and 5..12 labels. Reference enumerates every original labeled subset by strict Hall, obtains ranks by deletion recurrence, independently checks every generated rank and all budget optima and selected witnesses. The solver uses cover normalization, atom list as merge key, atom-only dominance compared with full-coordinate dominance, and dense deficits as an execution cache. Every canonicalization reconstructs from atoms; each emitted atom is individually removed in a check of necessity. No disagreement.

models=350; bruteSubsets=376960; budgets=witnessChecks=5096; rankChecks=46433; decodeChecks=44129; dominanceChecks=1777; fullDominanceCoordinates=8759; atomDominanceCoordinates=1403; stages=2146; generated=7160; states=2986; peak=12; denseEntries=15708; atomEntries=778; initialDense=4744; initialAtoms=181; allContainments=63525; coverEdges=26924; coverConstructionChecks=71682; normalizations=6889; allContainmentVisits=118596; coverVisits=53049; splitVisits=26369; essentialAtomChecks=1437; disagreements=0.
Dominance coordinate totals count candidate coordinates before early exit (not actual short-circuit operation counts). Retained atom entries are logical entries, not measured bytes; each atom also stores a mask index. Full dense deficits were still cached in this implementation. Cover preprocessing adds 71682 containment checks beyond construction of the original candidate lists. No pure timing, peak memory or physical byte benefit claimed. State counts agree exactly with GCH.

Code e9d4264bdf644eb55eef70be39db4b6d93ec32d0:research_artifacts/portable_direct/EC49GCI/atomic_deficit_replay.js (blob b45b40f78672fc5dd311ff5bda14edf35202f914); run node atomic_deficit_replay.js.
Output faf4b8fcd05f63c4efc3589e0d2b6dde75bbb298:research_artifacts/portable_direct/EC49GCI/replay_output.json (blob 9c678235dde4045e3552d58af5d504abee20068b). Both exact readback verified.

## 5. Continuation and authority

Next useful unit: develop atom-only lazy target deficit evaluation and compare its cache cost with dense GCH, implement actual storage without dense per-state duplication, then paired timing and peak memory against GCF/GCG/GCH; look for irreducible joint atom growth families. Recover frozen BRC16943 archive bytes using GCG/GCH historical hashes (witness_records.json c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7; fourth.json 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923). No new archive recovery attempt or native replay in this unit. Inherited historical bounds M14 in [25,27], next root 2046, not new observations. Scope: fixed suffix insertion/skip and all-budget maximum with one witness; not arbitrary future supports, reverse deletion or native cell identity.

Current global main entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613 match immutable 80358801eb2e93b7b5d9bbf38917f22aa1086752. Current global and Source P000 V4/V5, worldview, joint preservation, heartbeat, residual and portable/continuation/method read; current native topic receipt r4-20261128-1133-ec49as-topic-read SUCCEEDED at 2026-11-28T03:34:09.152435+00:00, Source 995ae176f73dbff1924baf61120a751f0dda8c6f, NO_CANONICAL_PUBLICATION_DIRECTORY, native operational owner projection not evaluated. No shared CLAIM or alternate identity. Historical EM-DIRECT-23537B not verified as current own private identity; independent portable informed research. Activity association and canonical integration pending. No P000, frozen science or schedule mutation.
