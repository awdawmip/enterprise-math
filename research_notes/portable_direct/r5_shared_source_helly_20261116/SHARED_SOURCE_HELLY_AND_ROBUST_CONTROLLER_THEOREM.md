# R5 — Exact common optimal source libraries, Helly-two theorem, and robust Set-control quotient

Date: 2026-11-16 (Asia/Shanghai). Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Scope and inherited exact interface

This is the **auxiliary indexed-center radius-2 one-step repair observer**, not native X6 Cell geometry or an executed BRC physical process. P000, Heartbeat World, and protected source-identity requirements are unchanged. Source labels, suffixes, old cores, and closure names are as in the original graph-incidence theorem:

- research_notes/portable_direct/r5_overlapping_triangle_chain_20261115/OVERLAPPING_TRIANGLE_CHAIN_EXACT_KERNEL.md @ c177b61d1f8fd899038a91f5ecb6e99390890bce
- research_notes/portable_direct/r5_cyclic_bridge_20261115/CYCLIC_BRIDGE_EXACT_RESIDUAL_AND_FUTURE_FIDELITY.md @ b2e4e47c78ff7479474687542107851aa4743e15.

Fix integer k >= 3. The cycle-of-triangles graph has named spine vertices v_i and leaf vertices w_i, i modulo k. Triangle i has edges v_i v_(i+1), v_i w_i, and v_(i+1) w_i. These 3k edges encode always-available two-hot old suffixes and the new target suffixes. Available one-hot helper suffixes are a subset of vertices. All leaf helpers may be taken available; their availability has no effect on the optimum.

Let u in {0,1}^k mark *unavailable* spine helpers, u_i=1 meaning helper v_i is unavailable. Write q(u)=sum_(i mod k) u_i u_(i+1), and A(u)={i:u_i=0}. The inherited source-aware graph theorem gives the exact one-step optima:

  kappa_a(u;2)=5k+q(u),       kappa_ab(u;2)=6k.

For each mask u, a canonical source-labelled optimal a-library uses:
(1) old source (O1,0,y) for every two-hot edge suffix y;
(2) old sources (O0,1,e_i) and (O4,1,e_i) for each available spine helper i in A(u);
(3) old source (O0,1,y) for each edge with both endpoints outside A(u).

Its number of resources is 5k+q(u). Direct radius-2 repair under the original indexed-core metric is valid (rho=|C\O|+[s!=t]+Hamming(x,y)). In particular, this **one optimal library contains the named paired helper sources for every available spine vertex**.

A *common library* for a collection of snapshots means one fixed set of labelled old sources feasible for every snapshot, with no substitutions as helper availability changes; the new target set and edge-source availability stay fixed.

## Theorem 1. Exact common source-optimum for arbitrary finite families

For every nonempty finite family of masks U={u^(1),...,u^(r)}, put u_* = u^(1) OR ... OR u^(r), bitwise OR. Then the minimum source-labelled library valid for every mask in U has exactly

  K_shared(U)=5k+q(u_*)

sources in single-a closure, and 6k in joint-ab closure.

Proof. A fixed feasible library can use only sources available under *every* snapshot. The allowed optional helper set is therefore exactly the intersection of the individual helper sets, equivalent to the unavailable mask u_*. Conversely any library feasible for u_* is feasible for all individual masks. The feasible collections coincide, not just their optimal values. Apply the inherited exact formula, and use the explicit canonical construction at u_* to attain it. QED.

**Two-state compatibility criterion.** For masks u and v, a *single library of individually minimum size for both* exists if and only if

  q(u OR v)=q(u)=q(v).

Necessity and sufficiency follow from Theorem 1 together with monotonicity of q.

## Theorem 2. Pairwise compatibility implies joint compatibility (Helly number 2)

For any finite nonempty collection U of masks, there is a common labelled library which is individually optimal at every member mask if and only if each pair admits such a library (the singleton case is immediate).

Proof. Let F(u) be the set of cyclic spine edges whose two endpoints are unavailable under u. Then |F(u)|=q(u), and F(u) is monotone under OR. Pairwise optimal compatibility means

  F(u OR v)=F(u)=F(v)

for each pair: the set equalities follow from inclusion and equality of finite cardinalities. Consequently all F(u) equal some fixed F. If a cyclic edge belongs to F(u_*), each of its two endpoints is unavailable in at least one member mask. Select one witness mask for each endpoint, say u and v (possibly the same mask). That edge belongs to F(u OR v)=F. Therefore F(u_*)=F, so q(u_*)=q(u) for every u in U. Theorem 1 gives a common individually optimal library. QED.

This is a scope-typed compatibility theorem for the fixed target cycle and helper-source semantics. It is not a generic assertion about arbitrary set-cover problems.

## Theorem 3. Robust fixed library under arbitrary named Set commands

Fix J subset of the k spine indices. Commands Set_i(b), with i in J and b in {0,1}, overwrite the i-th unavailability bit. The empty word is permitted. Let R_J(u) be the set of all reachable masks, and write 1_J for the J-indicator mask.

The minimum one-time stored library remaining feasible for **every** future command word has cardinality

  K_robust(u,J)=5k+q(u OR 1_J)
               =max_{v in R_J(u)} kappa_a(v;2).

The joint-ab robust value is 6k. A constructive witness uses the canonical library for the always-available spine set A_R={i outside J:u_i=0}.

Proof. Every controlled vertex can be made unavailable, while every uncontrolled vertex retains its initial availability. Thus the intersection of available sources across the reachable states has unavailable mask u OR 1_J. Theorem 1 gives the first equality and a feasible fixed witness. Setting every controlled vertex to unavailable reaches exactly that mask; q is coordinatewise monotone, so the attained individual optimum is the maximum over reachable snapshots. QED.

This equality is a minimax *one-time reserve* statement. The same fixed library need not have minimum cardinality under an easier individual snapshot.

## Theorem 4. Exact sufficient residual for the complete source-optimum-family observer

Let Opt(u) be the **entire set** of minimum-cardinality source-labelled feasible old libraries, rather than merely the minimum cardinality or one arbitrary selected witness. Then

  Opt(u)=Opt(v) if and only if u=v.

Proof. An unavailable spine helper e_i cannot appear as a suffix in any feasible old library. When i is available, the canonical optimal library described above includes both (O0,1,e_i) and (O4,1,e_i). Hence from the union of all optimal libraries' labelled sources one can read exactly which spine helpers are available. Equality of Opt families forces equality of u. Equal masks trivially give equal families. QED.

There are exactly 2^k equivalence classes for this full one-step source-optimum-spectrum observer.

For a fixed control set J, let OptRobust_J(u) denote the entire family of minimum-cardinality libraries feasible for *all* reachable masks. Theorem 1 identifies it with Opt(u OR 1_J). Thus this full **robust-reserve source-spectrum** depends exactly on the unavailability mask outside J; varying all initial masks yields precisely 2^(k-|J|) distinct source-spectrum states.

The weaker problem of choosing *one* currently optimal library after each command may admit more compression. These two exact spectra are observer-specific results and do not solve that weaker transducer-minimization problem.

## Theorem 5. Arbitrarily large common-source penalty

For each k>=3, take the k masks u^(i)=e_i, one unavailable spine helper per snapshot. Each has q=0 and individual minimum size 5k. Their bitwise OR is the all-ones mask with q=k. Thus the smallest common source-labelled library needs 6k resources: exactly k additional resources beyond every individual optimum. As 0<=q(u)<=k, this is the maximum possible gap for a family in which each individual optimum is 5k. QED.

## Exact verification and research frontier

The accompanying standard-library checker performs: exhaustive graph-incidence subset minimization on all 504 masks for k=3,...,8; original indexed-core direct repair checks for 56 canonical libraries k=3,...,5; exhaustive 21,824 ordered pairs of masks k=3,...,7; 5,576 distinct-mask triples k=3,...,5; all 21,824 (u,J) configurations k=3,...,7 for robust minimax with full reachable-state maxima; 1,344 direct repair checks of robust libraries k<=5; and exact singleton-gap checks k=3,...,39. Observed result: PASS_R5_SHARED_SOURCE_HELLY_TWO. All computations are exact integer/Boolean, and all universal claims above have independent symbolic arguments. Independent review: NOT_REVIEWED.

The proof reuses the frozen source, retains true helper identity in source-labeled libraries, and changes no P000 or canonical Source state.

**Next question:** construct the *minimal adaptive choose-one* source-aware transducer for a fixed named Set alphabet: after each command, output a feasible currently cardinality-optimal library, allowing a different chosen optimum in the next state. Determine whether its exact equivalence quotient can be smaller than the full Opt spectrum, and test the prior six-cycle pair with unavailable helpers at 3 versus 4 under J={0,1}. Compare with the exact robust-reserve 2^(k-|J|) quotient.

Historical research attribution only: EM-DIRECT-B78E55; RA-33C87C2B703418F0706695E9. These public labels do not authorize a current CLAIM or protected Activity write.
