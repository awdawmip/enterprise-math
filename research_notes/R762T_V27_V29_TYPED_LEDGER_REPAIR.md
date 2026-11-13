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