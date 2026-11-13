# R701 — Exact V29 counterflow fibers and circulation/observer repair

Date: 2026-11-11, Asia/Shanghai. Mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142. Frozen science pins preserved. Author-side mathematical derivation, UNREVIEWED, no native CLAIM/Result/Working Truth/Foundation admission. Derived after R700/R700b, Draft PR #2015.

## Source and typed BRC carrier

V29: research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md (Git blob 6849ebd3fc776fb7da3b46627376490aba3dad99). V39: research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md (blob 8151d0b6a4b65225b93d858bbc8a5d7037bf9cef). R699 science input pin: commit 55743642c88a24377ad4797cc2c6359c98b20553. The E* BRC carrier has 60 labeled positive tokens, four class capacities (24,18,6,12). All assertions below concern its declared count-level candidate encoding into V29 PASS events; raw labels, order, triadic frame and V39 based-loop transport remain separately typed.

Fix n>=3 typed ring ports indexed modulo n at one Cell. The only allowed local PASS arcs in the count model are adjacent forward and backward ring arcs. Define v_i=M[i,i+1] and w_i=M[i+1,i], and set other M entries to zero. For n=4, v equals R700's four BRC source-bin counts in the forward-only submodel, where 0<=v<=(24,18,6,12) and all w=0. Nonnegative integers M are the primitive V29 ledger; signs below enter only derived observers.

Set omega_i=v_i-w_i, Omega=M-M^T (hence Omega[i,i+1]=omega_i), u_int=(M-M^T)1, P=sum_i(v_i+w_i), H_i=v_i+w_i. Matched TRANSFER changes only Rin/Rout, so u_int=u_observed-Rin+Rout, and leaves Omega and P unchanged.

## Theorem R701.1 — forward-only native Omega suffices

In the forward-only R700 ring, Omega[i,i+1]=v_i exactly. Therefore the existing full V29 Omega observer already recovers all four BRC bin counts even without P. R700's contrast-only seven-state fiber and three-bit worst-case additional memory apply only to the deliberately coarser u-only quotient. Proof: opposite PASS arc counts w_i vanish, so each displayed Omega entry equals its forward count; TRANSFER leaves M unchanged. QED.

## Theorem R701.2 — exact two-direction fiber, all n>=3

Suppose omega and P are observed from this ring grammar, with no per-arc capacities. Put A=sum_i |omega_i|. A pair (omega,P) is realizable if and only if P>=A and P-A is an even integer. For realizable data let Q=(P-A)/2. Then all admissible nonnegative ledgers are in exact bijection with weak n-part compositions q of Q:

v_i=max(omega_i,0)+q_i; w_i=max(-omega_i,0)+q_i;
q_i>=0, sum_i q_i=Q.

Consequently each (Omega,P) fiber has precisely F(n,Q)=binomial(Q+n-1,n-1) distinct directed count ledgers, with exact worst-case fixed-length repair cost ceil(log2 F(n,Q)) binary bits, zero if F=1.

Proof. Any two nonnegative counts with difference omega_i decompose uniquely into the positive/negative parts of omega_i plus q_i=min(v_i,w_i). Their sum equals |omega_i|+2q_i, yielding the necessity of P=A+2Q. Conversely each weak composition constructs a unique admissible ledger and the asserted observation. Stars and bars counts such compositions. Distinguishing F finite possibilities needs at least ceil(log2 F) bits and an enumeration index attains the bound. QED.

This measures lost symmetric counterflow multiplicity, not external physical X6 flow or V39 frame holonomy.

## Theorem R701.3 — minimum of three direct edge-total probes

For n=4, given Omega, P and the direct edge-total readings H_i for any three edges, compute the fourth H from P minus their sum. Then v_i=(H_i+omega_i)/2, w_i=(H_i-omega_i)/2, recovering the full directed ledger.

For each possible choice of just two distinct H_i and every Q>=1, a collision exists even with Omega=0, P=2Q: place all Q opposite-PASS pairs on one or the other of the two unmeasured edges. Both choices yield exactly the same two H readings and (Omega,P) while having different ledgers. Thus three readings are necessary and sufficient **within the menu of individual direct H_i channels**. Arbitrary encodings of the finite q-composition index may use a different number of scalar channels.

## Theorem R701.4 — two independent information-loss kernels

For this ring, u_int,i=omega_i-omega_(i-1) (indices modulo n). Thus u_int alone determines omega up to a common integer circulation k(1,...,1). One signed edge omega_0 in addition to u_int reconstructs the other signed omega components by recursion and an exact closure consistency check.

For any connected oriented graph with m undirected edges and n vertices, the integer edge-to-divergence incidence map has rank n-1 and kernel rank m-n+1 (a graph cycle-space coordinate lattice). On the ring this rank is one. Hence u discards signed circulation, while (Omega,P) additionally discards the distribution q of symmetric opposite PASS pairs; these are distinct mechanisms. Full native Omega already retains the first.

## Executed exact verification

The attached self-contained Python standard-library verifier enumerates all omega in {-1,0,1}^4 and all nonnegative q-compositions for Q=0..6, covering 17,010 directed M ledgers. It checks full M-derived Omega,u,P, the exact fiber formula and inversion from three H_i. It independently enumerates the full 43,224 nonempty forward-only R700 capacity-box histograms and verifies Omega directly recovers v. It generates exact collision witnesses for all six two-H observation menus.

Executed output: R701_EXACT_COUNTERFLOW_FIBERS_PASS. The universal theorem is proved algebraically; bounded enumeration is regression evidence, not the proof of the universal quantifier.

## Next question

Construct an actually legal signed X6 Link/Port, triadic active-frame and V39 based-loop event packet realizing one declared pair of opposite PASS arcs, then test whether a permitted continuation distinguishes a counterflow q difference despite matching (j,h). Preserve BRC token identities and V29 event order. The present event grammar alone does not license physical X6 realization, but its count-level information bound is exact.