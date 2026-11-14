# R762AE — Chronological source-blind V29 TRANSFER fibers and an exact permanent theorem

**Status:** author-side conditional theorem, constructive proof and exact finite cross-check; NOT_REVIEWED / NOT_NATIVE_ADMITTED. Date: 2026-11-14. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Original contributor EM-X6-3050F6, Activity RA-6068F717D991DF54FBBDDEED. Previously observed CLAIM MCP-e4b33a56e2686c66e7cd5ca2 and RUN-53ab7d7bffccaaf2c0af47a4 do **not** supply current execution authorization. Frozen P000 scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389. Reuses R762AC (ff7f13951e13d2b50134e6139e9493c2659a22f2) and R762AD (240b9624100f01dfb3a034d226ee26cd2245fb8c), without changing them.

## Precise model and observer

Retain R762AC/AD's *conditional* capacity-two hub and m fully occupied, unit-capacity named outer Cell ports, each initially carrying an identifiable source token i. A native move in the star is only the signed-axis spoke step I_i: i -> hub or O_j: hub -> j. Consider a shortest full moved-support execution of exactly 2m steps: each of the m sources ingresses once, egresses once, and ends at a different port. The hub is empty at both macro boundaries. Each outer port issues I_i once and receives O_i once.

A **chronological source-blind TRANSFER transcript** tau records *all* I_i/O_j labels and their temporal order, but does not report which hidden source token was picked for O_j. This is **strictly richer** than V29's terminal aggregate counter ledger. The hidden final source map is the permutation sigma(i)=j. No internal PASS, V17 frame change or V39 holonomy is assumed in this boundary-only lift.

A syntactically feasible transcript contains each I_i/O_i exactly once, has I_i earlier than O_i (the port must become vacant), and has prefix hub occupancy #I-#O in [0,2]. Such a transcript need not have a physical source realization.

## Theorem AE1 — the source fiber is an exact 0/1 permanent

Let t(I_i),t(O_j) be positions in a feasible transcript tau, and let

M_tau(i,j) = 1 if i != j and t(I_i) < t(O_j); otherwise 0.

For every m >= 2, the number A(tau) of *labeled physical shortest traces* yielding the same complete source-blind chronological observation is

**A(tau) = per(M_tau) = sum_(sigma in S_m) prod_i M_tau(i,sigma(i)).**

**Proof.** A realized trace defines a bijection sigma between ingress sources and distinct destination ports. Every source that exits must already be in the hub, and no source returns to its original port, so the selected entries of M_tau equal one. Conversely, any permutation selecting only one entries uniquely prescribes which source leaves at each O_j. Its source's ingress precedes that egress; bijectivity prevents it from having departed earlier. The target port is empty because I_j occurs earlier than O_j, and it receives exactly one outgoing token. Hub occupancy is completely determined by the transcript's prefix #I-#O, independent of token choices, so it never exceeds two. Thus this assignment is a fully legal unique replay. The constructions are mutually inverse. QED.

For A(tau)>=1 and a future query able to distinguish every final source map, the precise *fixed-length worst-case, conditioned-on-tau* minimum repair is ceil(log2 A(tau)) bits. Zero bits suffice iff A(tau)=1. This statement is **not** an entropy estimate or global observer equivalence for operations that observe more than the final map.

Exact BRC fiber computation requires no floating point: with rows i and bitmask S of already chosen destinations, let D(0,empty)=1 and propagate D(i+1,S union {j}) += D(i,S) when M_tau(i,j)=1 and j not in S. Then D(m,all)=A(tau), by integer subset DP O(m^2 2^m) time and O(2^m) memory.

## Theorem AE2 — a Fibonacci chronology fiber with exact repair lower bounds

Fix the feasible chronological port log

tau_m = I0, I1, O0, I2, O1, I3, O2, ... , I_(m-1), O_(m-2), O_(m-1).

For all m>=2,

**A(tau_m) = F_(m-1)**, F_0=0, F_1=1, F_(k+1)=F_k+F_(k-1).

**Proof.** In this tau_m, t(I_i)<t(O_j) iff j>=i-1 (for i=0 the same inequality is automatic on j>=0). Therefore its allowable permutations are exactly derangements satisfying sigma(i)>=i-1.

These derangements biject with compositions of the ordered interval [0,m-1] into contiguous blocks of length at least two. Each block [a,b] maps a to b and every i=a+1,...,b to i-1. Conversely, take least remaining a and let b=sigma(a)>a. To occupy destination a, source a+1 is forced: sigma(a+1)=a, because sources with index >a+1 cannot reach a, and source a itself cannot return to a. If b>a+1, destination a+1 similarly forces sigma(a+2)=a+1; continue until sigma(b)=b-1. Thus the initial block [a,b] is forced and the suffix is independent. This is a bijection. Writing c_m for compositions into parts >=2 gives c_0=1,c_1=0,c_m=sum_(ell=2)^m c_(m-ell). Its generating function is (1-z)/(1-z-z^2), whose coefficients satisfy c_m=F_(m-1) for m>=2. QED.

A concrete collision already occurs at m=4:

tau_4 = I0,I1,O0,I2,O1,I3,O2,O3.

The **same full chronological port log** admits both source-to-port maps (1,0,3,2) (two transpositions) and (3,0,1,2) (one four-cycle). The future question "where did source 0 end?" distinguishes them. Exactly one repair bit is needed for this observed transcript. At m=6 the canonical transcript admits five source maps and needs three fixed-length bits. This is *real source/path residual*, not noise, not an extra spatial dimension, and not V17 holonomy.

The formula is valid as abstract star combinatorics for all m, but only m<=6 can use **distinct underlying X6 native axes** within the simple six-spoke embedding. In particular m>3 is a **nonprimitive** multiple-force configuration and cannot itself be promoted to primitive P000 triadic balance.

## Independent exact verification and range

The companion executable independently enumerates labeled legal physical traces using explicit token positions and evaluates the 0/1 permanent via a separate subset DP for each source-blind transcript. All results agree for every realized transcript m=2,...,6. The R762AD total C_m=m! 2^(m-1) F_(m-1) is independently matched.

| m | Number of distinct chronological transcripts | Fiber histogram (fiber size: count) | Total labeled shortest traces | Largest observed fiber |
|---:|---:|---|---:|---:|
| 2 | 4 | 1:4 | 4 | 1 |
| 3 | 24 | 1:24 | 24 | 1 |
| 4 | 288 | 1:192, 2:96 | 384 | 2 |
| 5 | 3840 | 1:2400, 2:960, 3:480 | 5760 | 3 |
| 6 | 63360 | 1:31680, 2:20160, 3:5760, 4:2880, 5:2880 | 115200 | 5 |

Canonical Fibonacci values are additionally checked exactly for m=2,...,15. The two general theorems rest on their proofs; finite tests provide independent cross-checks. The finite worst-case transcript-conditioned repair requirements are 0,0,1,2,3 bits for m=2,...,6. By contrast, the coarser **terminal V29-only** source fiber has derangement size !m (R762AD), requiring 0,1,4,6,9 bits respectively for m=2,...,6. The difference is a scope-typed information comparison, not a permission to delete identity if source-sensitive future operations remain.

**Not yet proved:** the tempting universal assertion max_tau A(tau)=F_(m-1) for every m. It holds in the full m<=6 census and the canonical family supplies a lower bound for every m, but no general upper-bound proof is asserted. Also the native TRIADIC_CLOSURE_E event predicate, Cell/channel occupancy, any mandatory internal PASS, actual V17 state update and V39 frame transport are still open; this conditional theorem does not admit the candidate model as native physics.

**Next science:** restrict the permanent's allowed source/port edges to the *actually admitted*, source-typed TRIADIC_CLOSURE_E macro alphabet and coupled PASS/TRANSFER laws. Determine the minimal observer repair over *multiple* genuine triadic macros, and prove the necessary future-operation descent/retained branch identity under P000 and the joint-observer preservation constraint.

Artifacts: R762AE_TRANSFER_PERMANENT_VERIFY.py and R762AE_TRANSFER_PERMANENT_EVIDENCE.json in this research_notes directory. No native Source PROGRESS/Result, independent Driver review or P000/worldview changes are claimed here.
