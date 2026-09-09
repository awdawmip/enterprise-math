# RB CM24 source-exposed exact map: eight-gate return draft

Draft boundary: this file is preparation for the specified durable return. It does not create a canonical Result, a terminal disposition, a Driver review, or a publication claim. The frozen full v3 package is awaiting the second bounded source-exposed proof/code review. Its mathematical hard target has not been reduced to a subset.

- Task: `RS-RB-CM24-SOURCE-EXPOSED-EXACT-MAP-CERTIFICATE`.
- Publication: `TP2-554AC43234E8E297A6E9`.
- Researcher: `EM-HODGEH0O-82EF42`.
- Execution: `ER-BDAB13EB167775B80BE7`.
- Claim: `chatgpt-rb-cm24-source-exposed-20260909-e227c807e7ed441c80b53420f8158ff7`.
- Hard target: `RB_CM24_PINNED_SOURCE_EXACT_MAP_CERTIFIED_OR_EXACT_FAILURE`.
- Exposure: `SOURCE_EXPOSED / NONBLIND_DISCLOSED`.
- Suggested harvest scope: one formula's mathematical result and exact certificate, with no new global tool family or advertised API.

The author wrote the earlier blind reduction, participated in source intake and contract preparation, and received explicit Owner field, base-point and geometric suggestions in the shared conversation. This is not an independent rediscovery or blind validation. The old blind raw freeze, INCOMPLETE Result, source-recovery chronology, and historical field error remain unchanged.

## Candidate mathematical conclusion

For the exact pinned formulas and embedding alpha>0, alpha^4=3, beta>0, beta^2=2, i^2=-1, let L=Q(alpha,beta,i), C:t^2=R^3-3R, and let D be the smooth projective normalization of w^2=(R+2)t over C. Keep the frozen k and lambda. Put X=N/D0, W=(2delta N)D0-N(2delta D0), and

    C4=-i*alpha*(9+3beta+2alpha^2+4alpha^2*beta),
    Y=w*W/(2(t+k)D0^2),  delta=t*d/dR.

The displayed map extends to a degree-six morphism from D to the nonsingular projective model of

    Y^2=(C4/4)*X*(X-1)*(X-lambda).

The map X:C->P1 also has degree six. Its common section base divisor in L(7O) is exactly [B0], B0=(-3alpha^2,6i*beta*alpha), with common multiplicity one. The full function-field identity is

    (R+2)t*(delta X)^2=(C4/4)*(t+k)^2*X*(X-1)*(X-lambda),

and the chosen sign satisfies dX/Y=(dR/w)*(1+k/t) globally. The target invariant is exactly j=2417472+1707264beta. No square root of C4/4 is silently introduced.

The four complete special-fiber divisors are given in proof section 5. In the old source order (O,T0,Tplus,Tminus,Pplus,Pminus), the branch assignment is (0,infinity,infinity,0,0,0). Its precise frozen empty-infinity representative is z=lambda*(X-1)/(X-lambda), with vector (1,2,2,1,1,1). For the explicitly chosen half-point Q=(s(beta-1),i*beta*alpha^3*(beta-1)), 2Q=Tminus, the canonical geometric twist triple is (Tplus,T0,Tminus). The certificate retains all three actual nonzero scalar and rational-function representatives over L. Thus the empty-fiber class is nontrivial and lies outside the earlier 180 excluded components.

The normalized pole divisor is 2E_l, where the three-point divisor E_l is cut out by Ql(R)=0 and N-lambda D0=0. Its class S=sum(E_l) satisfies 2S=-B0, hence S is not O. The effective divisor is L-defined without claiming every individual cubic point is L-rational. This supplies the general pole-class parameter and the exact RR dimensions (3,1,2); it is not a substitution of 3O for the true pole class.

## Original eight gates

| Gate | Evidence and exact limit |
| --- | --- |
| 1. Frozen source and coefficient embedding | Original `source_freeze.json` and its seven pins are unchanged. The coefficient degree is proved to be 16; the function-field basis is {1,t}. The missing i in the original source sentence is recorded as an error, not silently repaired in history. |
| 2. Four fibers, parity, constants, half-points, component and descent | Full three additional norm factorizations, nonzero and coprimality witnesses, complete divisors, explicit Q, three cleared L-rational square-class reconstructions, and two exact V4 transports appear in proof sections 5-7 and the certificate. The old corrected RR row is actually matched by exact source pins. No claim of descent to a smaller field or completion of other parameter families is made. |
| 3. All base points and both degrees | Norm(A) exhausts numerator zeros. D0 is nonzero at the other candidate zeros; B0 is the only common point. The complete norm calculation proves D0 has order one there. The pole orders at O are 6 and 7, so O is not a base point. Removing [B0] from L(7O), followed by the function-field tower, proves both degree-six statements. |
| 4. Target and invariant | The actual Y gives the original twisted cubic with constant C4/4. C4, lambda and 1-lambda are nonzero. The exact j cross product is checked. The source's Y and twist are retained; no analytic period is inferred. |
| 5. Full ODE | The entire remainder in L[R,t]/(t^2-R^3+3R) is zero. No substitution t=-k or necessary-only filter is used. The canonical V4-transformed numerator and denominator also pass the complete same-k ODE. |
| 6. Unsquared global differential | The paper derives dX/Y=phi before squaring and checks all possible exceptional points on the normalization. The new tests change the actual Y numerator sign and omit the denominator factor 2; both give nonzero cleared differences. The original sign remains fixed. |
| 7. Exact proof, deterministic checks and limits | Frozen proof, code, 533112-byte certificate, full actual stdout/stderr, runner and receipt are bound below. Thirteen focused tests and the selected two-file static check pass. The proof supplies divisor and field interpretation; software normal forms are not presented as a standalone theorem prover. |
| 8. Gate-by-gate return | This draft enumerates every original gate. The named final durable return and any terminal recommendation must follow the outstanding bounded review. No canonical RR is produced by this draft. |

## Exact v3 evidence

All paths below are relative to `research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/`.

| File | SHA256 |
| --- | --- |
| `check_exact_map.py` | `58c57974e3bf74e17a9a4ff4063d3d6ab676b378521b1dba6dfba26ec38f05b6` |
| `test_exact_map.py` | `41a805d1a57e9422b3a8bfeac8257b8c61231524157514fcf4389a761de712e6` |
| `exact_map_proof.md` | `7c8c480af589fcd875488a8031db4e6adb1cc1a144adee2950a2e16b74866f12` |
| `exact_map_certificate.json` and `runs/placement_v3_final/certificate.json` | `bbb33d3e80274af0eb09aeef6bb6d5009745048849c6e8b93026a6410bac0e5e` |
| `runs/placement_v3_final/receipt.json` | `b02c0cc64126fab7bac3c355d24db2fc816a068e7408ca9c7c28a07744570c26` |
| `checkpoints/placement_source_binding.json` | `722628192d82a4ec5d277c3a07d4f6aea84276edada30e692c88a2853746d3d1` |
| `checkpoints/owner_complete_fibers_placement_v3.md` | `61681db697d06e9d6a9e1ce3fb2725360c6fb048b1ad6fc171d06d2a6525fdf2` |

The actual final execution ran from 2026-09-09T02:14:57.641269+00:00 through 02:15:01.556357+00:00: certificate command 0.797 seconds, thirteen tests 0.880 unittest seconds, and selected static check 0.204 seconds, all exit 0. Full argv, source hashes and raw output hashes are in the receipt. The proof, checker and test bytes were unchanged during those commands. The Owner review is shared-input, source-exposed paper checking, not a new mathematical run or a blind verdict. A second review is not yet claimed in this draft.

The real v3 replay entry is `runs/placement_v3_final/replay.py`, accepting explicit `--root` and `--output-dir`. Use a fresh output directory; it refuses to overwrite execution artifacts. Its new source file is not retrospectively attributed to the v1 run. Old v1/v2 bytes, intermediate actual v3 runs, the peer's original archive-help failure output, and the retrospective v1 provenance note are preserved separately.

## Native arithmetic and scope

This execution extends the existing canonical RB task-local integer polynomial carrier. It preserves integer content and every scalar multiplier in pseudo-remainder identities. Monic algebraic reductions use the proved coefficient and curve relations. Complex function fractions and scalar quotients remain formal; no natural-number division or root value was requested, so actual BRC evaluations are zero. This is the applicable T0 domain boundary, not a substituted positive-count model for complex square classes. T6 observation preservation applies to the declared field, labels, valuation and denominator data. There is no new global family, generic rational wrapper, precision projection, or claim that R,t,w are Spatial6 axes.

Each mathematical child had the recorded 600-second outer timeout and the existing 4096 MiB Windows Job process-memory limit. The memory limit is not a measured peak; source-level checks are not transitive certification of unrelated legacy software. The largest observed coefficient/support figures and actual reused API-call counts remain in the certificate.

## Parent residue

The period integer and homology index, the independently derived normalization of (B1/Omega_P)^2, and exhaustive resolution of all 1980 parameter families remain OPEN. This candidate checks one recovered formula; it does not validate an entire historical theorem package, reverse the old INCOMPLETE result, restore blindness, or close the parent. A formal acceptance recommendation must use the completed review and final return, not this preparation file.
