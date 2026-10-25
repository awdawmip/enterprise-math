# R1-N14 Stage125 portable mathematical continuation — DUAL ONLY

Mother problem: external ternary iid sequential test with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon 14, all randomized literal ordered-history stopping and decisions. Find V14(alpha)=minimum maximum of P/Q expected stopping time subject to each directional error <= alpha. Not a P000/native-X6 theorem.

Latest author-proved Stage124 endpoint (not independently Driver-accepted):

    alpha124=2573845372952647230925/7411551152237344456704
    V124=377878009388672358128945/29646204608949377826816

Stage124's optimal right-edge randomized state is A=(9,3,0), stop declare P with y=151548960415319/415627392000000; T=(14,7,4) has saturated to declare Q, z=0 (P probability). Relevant immutable proof and verifiers: research_notes/n14_aux_iid_affine_124_20261026/.

Exact new dual candidate (NOT primal theorem): retain A P/continue tie, hold T Q as unique action, move (K,L) by t*(-1,-608000/474363). The first strictly positive gap collision occurs at t=13731333106707/1006541960224, state U=(12,7,5), declare Q / continue. New K=3579845625/4855672, L=416181048/606959. Fresh 680-state Bellman yields exactly A P/continue and U Q/continue ties, 1238 strict gaps and no negative gaps; min strict gap 578968738307/115991671209984.

First unresolved unit: determine all real y,w in [0,1] for A P-stop and U Q-stop using the exact ordered-history first-hit masses P and Q. Confirm A and U cones disjoint: from depth9 A to depth12 U requires (7-3)+(5-0)=9 counted draws in 3 steps, impossible; reverse depth is impossible. Compute M00,dA,dU and the equality relation eP=eQ. Determine which randomization saturates first, whether tP>tQ throughout, the full alpha interval, exact new endpoint and support right-sharpness. Cross-check independent literal integer DFS at all four corners; distinguish count quotient from full ordered policies in the proof. If the presumed P-dominant support fails, state a precise counterexample, not an invented theorem.

Method / constraints: finite positive-rational BRC branch provenance; count state is sufficient only for this iid future four-observer lease. Preserve P000 and active worldview unchanged, fixed GLOBAL_KNOWLEDGE_V1 snapshot main@e8d65b2492cf35be071c32b0c9852487f100be07. This proof is author-level; native owner/CLAIM, Result freeze and independent review remain unavailable/unverified due to CONTROL_QUOTA and STATIC_READONLY_SCOPE_DENIED. Do not overwrite live task owners. Preserve model specificity and transport evidence.
