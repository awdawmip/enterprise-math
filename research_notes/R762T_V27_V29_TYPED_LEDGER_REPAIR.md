# R762T — V27/V29 typed triadic ledger repair and minimum boundary mass

**Status:** Author-side exact mathematics; finite exact verification; NOT_REVIEWED/NOT_ADMITTED. Date: 2026-11-14 Asia/Shanghai. Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5). No CLAIM/Result or physical event admission is asserted. Four local *internal passage ports* are not native X6 spatial axes.

## Exact definition and local realization theorem

V29's nonnegative state at a Cell consists of M in N_0^(d×d), Rin,Rout in N_0^d, and derived counts I=M1+Rin, O=M^T1+Rout, Omega=M-M^T, u=Omega 1+Rin-Rout.

For fixed M and integer target u, set w=u-(M-M^T)1.

**T1 (complete sharp fiber):** Every nonnegative realization is uniquely parameterized by t in N_0^d:

    Rin_i=max(w_i,0)+t_i,    Rout_i=max(-w_i,0)+t_i.

The minimum total boundary count is ||w||_1, uniquely at t=0; all other realizations cost ||w||_1+2 sum_i t_i.

**Proof.** Componentwise Rin_i-Rout_i=w_i has precisely the displayed nonnegative solutions. Their pairwise sum is |w_i|+2t_i; add over all ports.

## Precise V27 to V29 reconciliation

V27's directed triadic internal passage 0→1→2→0 has:

    M=[[0,1,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,0]]
    M1=M^T1=(1,1,1,0)
    u=(-2,-4,-3,10).

V27 displays I=(0,0,0,10) and O=(2,4,3,0), with I-O=u. However, when interpreted literally as V29 *derived total* counts simultaneously with the specified M, this I violates the necessary inequality I>=M1 at ports 0,1,2. There is then no nonnegative V29 Rin.

**T2 (exact repair):** Retype that displayed pair as V29 *boundary counts*. The resulting exact compatible ledger is

    Rin=(0,0,0,10), Rout=(2,4,3,0)
    Inew=(1,1,1,10), Onew=(3,5,4,0).

It is nonnegative, Inew-Onew=u, and its Omega=M-M^T is unchanged. By T1 the unique minimum boundary cost is 10+9=19. The V27 scoring inputs (u,Omega) remain algebraically identical. The V27 20-triad scorer is not rerun here.

**Proof.** A directed three-cycle has equal row and column sums (1,1,1,0), so Omega1=0. Apply T1 with w=u. Reconstruct Inew and Onew from V29's definition.

## Closed two-Cell conservative network witness

**T3:** Choose an abstract two-Cell network A (target), B (companion) with directed connectors B:0→A:3, A:0→B:1, A:1→B:1 and A:2→B:1. Initially all counts vanish. Issue 10, 2, 4, 3 matched TRANSFER events on these four connectors respectively, and three A-internal PASS events 0→1, 1→2, 2→0.

The resulting A ledger is T2's, with u_A=(-2,-4,-3,10) and scalar sum +1; B has total scalar u_B sum -1. The network charge Q= sum of all Cell u components equals 0 after **each** primitive event. When M_A is fixed, self-transfers are excluded and every A boundary occurrence touches B, 19 matched transfers are necessary and sufficient.

**Proof.** Each transfer supplies one unit of A's Rin or Rout. T1 requires at least 19 such units; the specified 19 events meet the bound. PASS and matched TRANSFER individually conserve Q by V29, and direct computation gives Q=0.

The second Cell compensates the target's nonzero scalar local contrast in a zero-initial-charge network. This is an exact V29 count-network witness with explicitly *declared* connectors, not an assertion of a P000-native physical admission predicate.

## BRC observer fiber

**T4:** At fixed M and u, T1's t-family gives infinitely many nonnegative boundary ledgers with the same (u,Omega). Taking t=(1,0,0,0) increases both absolute I[0] and O[0] by one and leaves the V27 score inputs exactly unchanged. An observer that may query I[0] distinguishes these states. Hence (u,Omega) is sufficient for the declared score-only future, but not for the expanded V29 future language containing absolute counts.

## Reproducible checks and scientific frontier

The accompanying standard-library Python checker performs an exact 19-TRANSFER/3-PASS two-Cell replay and verifies Q after every event, enumerates all 8 directed 3-cycles on four internal labels, checks scalar minimizers for all w from -10 to 10 by exhaustive nonnegative pairs bounded at 20, and tests 81 common-mode t-vectors. The T1 proof is algebraic for all d,M,u; its generality is not inferred from finite verification. JSON output is R762T_V27_V29_TYPED_RECONCILIATION_EVIDENCE.json.

Next: determine actual P000-native triadic Cell/Link/Port legality of the corrected boundary coupling, then derive the genuine V17 frame connection and V39 pair (j,h), preserving individual source identity and real event order. A valid V29 count grammar alone does not specify TRIADIC_CLOSURE_E physical admission or V39 h.

**Sources:** P000 V5 frozen a72226e2430ffa4786321ac86e7f0c599d5f0389; V27/V29/V39 research_notes at current Source main 06cc34a52d0cce82fc700a40410e1ad829f78561; preceding R762S PR #2337 commit eae85017c5effa339e0ee6406d5917a0aa5855f2. No P000 or ACTIVE worldview changes.

## T5 — Exact global minimum for a prescribed V29 contrast signature

The preceding repair is an instance of a general **sharp primitive-event complexity theorem**. Fix any finite d-port Cell A and any antisymmetric integer matrix Ω (Ω^T=-Ω), together with an integer desired local contrast u. Begin with zero counts, permit internal completed PASS and matched boundary TRANSFER to a companion Cell B, do not allow self-TRANSFERS, and permit sufficient directed A↔B connectors for each of A's ports. The minimum number of primitive events incident on or internal to A needed to realize **exactly** (Ω,u) is

    N_min(Ω,u)= sum_{0<=i<j<d}|Ω_ij| + sum_i |u_i-(Ω1)_i|.

The first term counts PASS events; the second counts matched TRANSFER events. Both minima can be attained simultaneously, with no negative counts. All Cell network scalar charge remains zero if the companion receives the opposite boundary increments.

**Proof.** For every unordered pair i<j, nonnegative M_ij,M_ji with M_ij-M_ji=Ω_ij require at least |Ω_ij| PASS increments; diagonal M_ii contributes nothing to Ω. Equality is attained by M_ij=max(Ω_ij,0), M_ji=max(-Ω_ij,0), M_ii=0. With that Ω, the boundary contrast is w=u-Ω1; T1 independently forces and attains the lower bound sum_i|w_i| matched TRANSFER occurrences. Put all these transactions between A and B using declared connectors, and the two parts construct the specified signature with total charge zero. Each primitive event supplies exactly one corresponding count increment. QED.

For V27's Ω the PASS lower bound is 3 and Ω1=0; for u=(-2,-4,-3,10) the boundary lower bound is 19. Therefore **22 primitive V29 occurrences** are necessary and sufficient to realize the precise V27 pair (Ω,u) within this declared two-Cell network grammar, even if the nonnegative passage matrix M is not fixed in advance. Extra symmetric PASS pairs or extra common-mode boundary counts do not reduce the bound. This is a typed ledger operation count, not a physical force-event duration or native TRIADIC_CLOSURE_E action count.

An additional exact construction checker covers 729 (Ω,u) cases: every skew Ω on three active labels with each independent entry in {-1,0,1}, and each target u component in {-1,0,1}, embedded into four ports. The universal formula is proved above and does not depend on this finite range.
