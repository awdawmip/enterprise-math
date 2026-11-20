# X6 signed-word orbit count — Driver mathematical recheck (shared context)

Date: 2026-11-21 (+08:00). Driver: EM-DVR-DEBB5E, original SID MCP-9b4714dc46b948afa4875a86c89c713c.
Task: RS-X6-NATIVE-ROTATION-DYNAMICS, publication TP2-6A1F9D8C2047E3B51C01.
Original author source: awdawmip/enterprise-math@9d09f6bc13b36a8d47d11b524fae4dd5254ac333:research_artifacts/mcp/RS-X6-NATIVE-ROTATION-DYNAMICS/MCP-c618a61189764f23846a391a08518a1a/0f0e002ae5e625394259/X6_SIGNED_WORD_ORBIT_SPLITTING_AND_CONCATENATION_20261116.md (Git blob 21eade70b2ea882ca50c283684079bc415e9cc5).
Original provenance: EM-EMF6D046-5A2844 and EM-X6-DFD1FD as carried by the exact task continuation; their scientific credit is preserved.

## Exact proposition and independent arithmetic check

Let B6=(C2)^6 ⋊ S6 and H=(C2)^6 ⋊ A6 act diagonally on ordered words W_N={±e1,...,±e6}^N. S(N,k) denotes the Stirling number of the second kind. Then for N≥1:

|W_N/B6| = sum_{k=1}^{min(6,N)} S(N,k) * 2^(N-k)

|W_N/H| = sum_{k=1}^{min(6,N)} (1 + [k>=5]) * S(N,k) * 2^(N-k).

Both quotients have one orbit for N=0.

Independent reasoning: a B6 orbit determines a set partition of the N positions by unsigned axis and a sign vector in each block modulo whole-block negation, giving S(N,k)*2^(N-k). For a representative using k axes, an odd underlying permutation stabilizing it exists exactly when the unused axes number 6-k is at least 2: swap two unused axes. Since H has index two in B6, the B6 orbit splits into two H orbits exactly for k>=5. This proves the formulas for every N, without using finite computation to extrapolate.

I wrote and ran a fresh in-session exact-integer enumeration of all 360 even permutations of six axes and 64 independent sign choices (23,040 H elements). For every group element, fixed signed letters = twice the number of axis fixed points with positive sign; Burnside sum fixed_letters^N / 23040 was computed for N=0,...,8. Independently, Stirling recurrence S(n,k)=k*S(n-1,k)+S(n-1,k-1) reproduced the orbit formula. All nine rows matched exactly:

| N | H Burnside | H formula | B6 formula |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 |
| 2 | 3 | 3 | 3 |
| 3 | 11 | 11 | 11 |
| 4 | 49 | 49 | 49 |
| 5 | 258 | 258 | 257 |
| 6 | 1570 | 1570 | 1539 |
| 7 | 10900 | 10900 | 10298 |
| 8 | 85312 | 85312 | 75848 |

## Composition caveat checked directly

One-letter words e1 and e2 lie in the same H orbit; however e1e1 and e1e2 have different unsigned-axis equality partitions and are in distinct H orbits. The independent word-orbit compression is therefore not a concatenation congruence. A future composition protocol needs shared-frame or relative-axis context (and, for native X6 transfer, the relevant branch/Port/time/triadic-event observations).

## Review classification and follow-through

This is a **mathematical scoped recheck**, not a new Native immutable Driver Review or a new Result. The Driver had previously worked on signed-frame X6 models: SHARED_CONTROL_CONTEXT_DISCLOSED; clean-blind independence is not claimed. The count is proved for the stated static signed-permutation action; native P000 Cell/Port/three-force/time rotation admissibility remains open. The original author's work remains the source of this theorem and the adjacent historical work remains credited.

Recommended next scientific unit: test a typed native path/event transition with fixed common frame and actual future readout, then determine whether its equivalence is a right-congruence on composable histories. No new Task or owner CLAIM requested by this note.
