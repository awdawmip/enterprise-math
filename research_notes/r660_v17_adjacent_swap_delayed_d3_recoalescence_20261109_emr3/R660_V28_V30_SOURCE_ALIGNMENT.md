# R660｜V28/V29/V30 Source 语义核验与群生成接口

Date: 2026-11-09 Asia/Shanghai. Status: author-side source alignment, verified after the R660 base proof. Original R660 proof/finite experiment remain unchanged. No independent Driver acceptance.

## Exact native historical source bytes checked

- \`research_notes/X6_PASSAGE_CONTINUITY_AND_NETWORK_BIAS_V28_20260906.md\`, Git blob \`8d4e93bcec148eba1624df8fb8bd0b022655c2bd\`: I=M1+R_in, O=M^T1+R_out, u=Ω1+R_in−R_out; matched transfers conserve network scalar count.
- \`research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md\`, Git blob \`6849ebd3fc776fb7da3b46627376490aba3dad99\`: PASS increments M[a,b], TRANSFER increments Rout_x[a] and Rin_y[b] simultaneously; all native ledger counters remain nonnegative; Q=Σ_cell Σ_port u conserved. An edge/port transfer must be **allowed by the declared network port relation**; historical V29 does not publish the complete H set for R660.
- \`research_notes/X6_EVENT_ORDER_RELATIVE_HOLONOMY_OBSTRUCTION_V30_20260906.md\`, Git blob \`3707518fa40644fd3bb45a8733923305b3b992ed\`: explicitly declares the same event-after-count, strict V27 maximizer, V17 shared-slot transport transducer as R660; demonstrates a two-PASS-event order witness. It does not supply a universal automatic event scheduler.
- R660 original frozen scientific pin remains R462@18783e01e3646c72b7aab3b16d3f565e83e6446f, V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d. This addendum supplies source-interpretation evidence, not a scientific re-pin.

## Conserved scalar on the three-TRANSFER witness

R660: x internal PASS seed (2,0,0,0), y seed (3,3,3,3); exactly the three TRANSFER port pair occurrences (2,2),(3,3),(0,0), in either order.

After all three, the local signed contrasts are exactly:

\[
u_x=(1,-2,-1,-1),\qquad u_y=(-2,-3,7,1).
\]

Hence \(\sum_a u_{x,a}=-3\), \(\sum_b u_{y,b}=+3\), and \(Q=0\). These are derived signed differences from nonnegative M,Rin,Rout; no negative native event was used. This confirms R660's static endpoint matches V28/V29 continuity and scalar conservation.

The V30 declared transducer's count→strict-score→slot ordering matches the R660 chosen update ordering. The remaining native-network requirement is to instantiate an approved **port-to-port transfer relation H** containing (2,2),(3,3),(0,0) on a chosen neighboring X6 Cell pair, and any additional event-window/clock semantics needed by an autonomous network law. This is a concrete interface gap, not an ambiguity about the stated auxiliary transducer.

## Combined event-order defects and S3 port

The exact V30 two-PASS witness records sorted-target slots σ_AB=(2,0,1), σ_BA=(0,2,1). Under R659/R660 composition convention, their relative permutation is

\[
\tau_*=\sigma_{BA}\sigma_{AB}^{-1}=(2,1,0),
\]

an odd transposition.

R660's three-TRANSFER witness gives \(\rho_*=(1,2,0)\), an even order-three cycle. As permutations,

\[
\rho_*^3=e,\quad \tau_*^2=e,\quad
\tau_*\rho_*\tau_*=\rho_*^{-1},\quad
\langle \rho_*,\tau_*\rangle=S_3
\]

(the six distinct words are \(e,\rho_*,\rho_*^2,\tau_*,\rho_*\tau_*,\rho_*^2\tau_*\)). Thus a **common group-valued interface** meant to distinguish the observed relative defects under arbitrary composition must retain the six-element S3 structure if it uses a group-homomorphic quotient. Any nontrivial normal kernel in S3 contains A3 and would erase the observed three-cycle.

This is an algebraic interface conclusion from two exactly specified, separately realized historical witness contexts. It does not assert that both witnesses are executable consecutively at one identical native Cell state or that every S3 element is reached by a single fixed input. Testing such common-context reachability is the next open dynamical problem.

## Next precise research unit

Specify the native X6 adjacency/port relation H and an event-time selector with full current Source permissions; test the R660 e2/e3 swap and its convergence under that selector. Then ask whether a multi-Cell common S3 port can be locally updated, source-pairing safe, and rotation covariant without storing the entire past event word.