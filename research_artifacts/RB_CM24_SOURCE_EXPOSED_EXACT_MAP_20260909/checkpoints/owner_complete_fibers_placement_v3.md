# Owner paper review of the complete v3 fiber and placement argument

Status: PAPER_REVIEW_PASS_AT_STATED_SCOPE; not a formal Driver verdict or task PASS.

Reviewed source: `research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/exact_map_proof.md`, SHA256 `7c8c480af589fcd875488a8031db4e6adb1cc1a144adee2950a2e16b74866f12`, 23,768 bytes, local candidate. Root actually read the complete proof, the new fiber/placement polynomial routines, and their source/classification binding code. The proof file hash was independently read by Root. The source is disclosed; Root previously supplied field, divisor and normalization suggestions. This is shared Owner paper checking, not a blind derivation, an independent computational replay, a canonical Result, or a formal review-record write.

## Scope and findings

The v1/v2 exact identity and base-point checks already have immutable EM checkpoints. This review examines the additional mathematical deductions in sections 5–7, with the full exact polynomial identities as their explicitly required computational premises. The current author reports the actual reconstruction run at 2026-09-09T02:04:40.863745Z–02:04:41.784582Z, certificate `03ac63220eccee49fbb879cb27d0af76f11470d4c56e30233b78397d7408ab23`. Root read that run receipt; this note does not claim to have rerun it or to have completed the final publication readback.

1. The three complete norm factorizations, squarefreeness, avoidance of the branch R-values and coprimality with the t coefficients support the asserted reduced divisors E_inf, E_1 and E_l. A root of a residual polynomial selects one ordinary t-sheet. The other sheet is nonzero, so order two of the norm gives order two on C. No split roots need be chosen over L; the full divisors are L-defined.

2. The simple R+3s factor in all three norms, combined with their verified vanishing at B0, gives individual order one for D0, A1 and Al. This is stronger than the v2 common-minimum-order statement. Thus the cancellation leaves X(B0) finite and outside 0,1,lambda. The denominator of the displayed derivative-ratio value is nonzero. It is not an omitted point of a special fiber.

3. The listed fibers all have degree six. Cross-overlap of their residual divisors would force N=D0=0 because lambda and 1-lambda are nonzero, and the only common point B0 has already been excluded from those residual factors. The branch labels follow from the full local divisors, not merely from the count 4+2.

4. Both target transformations preserve the fixed lambda, twist C=C4/4 and unsquared differential:
   x'=(X-lambda)/(X-1), Y'=(lambda-1)Y/(X-1)^2;
   z=lambda/x', Yz=-lambda Y'/x'^2.
   The composition has Yz=lambda(1-lambda)Y/(X-lambda)^2. Neither transformation flips the source t or changes fixed k. The derivative multiplier lambda(1-lambda) is correct.

5. The tangent norm, its nonzero tQ and the distinct third intersection Tminus imply div(ell)=2[Q]+[Tminus]-3[O], hence 2Q=Tminus and div(t/ell)=[T0]+[Tplus]-2[Q]. These fix the base half-point convention explicitly.

6. The norm identity for h gives (h+H)^2=h(Tr(h)+2H). From M U=removed Q3 B, 256 V=c removed Q3^3 and K B=J S^2 one gets h=(c M K/256)(Q3(h+H)/S)^2/J. For h0, J=R(R+s)=t^2/(R-s), yielding the stated alpha0 and u0. For h1, J=R, yielding the stated alpha1 and u1. All scalar factors stay visible; no constant square root is assumed.

7. G0 G1 Gl=(R+2)t and the full ODE give h0 h1 hl=Hprod^2/C4. Since R(R-s)(R+s)=t^2, the proposed alphal and ul supply the third class. The code also reconstructs that third class by a complete cleared identity. The labels (Tplus,T0,Tminus) therefore have more evidence than divisor parity alone. In particular the nonzero two-torsion class of R-s is not geometrically square: its half-divisor [Tplus]-[O] is nonprincipal on the elliptic curve.

8. The second V4 transport and the displayed canonical v0,v1,vl produce the scalar triples written in section 7. Root checked both identities gm/gp=R(t/(R gp))^2 and R/gp=gm(t/(gp gm))^2. The original assignment (0,3,3,0,0,0) and canonical empty-infinity assignment (1,2,2,1,1,1) are distinguished; x' is not mislabeled as the canonical stored row.

9. For z, the half pole divisor is the actual E_l. The full Al divisor gives 2 sum(E_l)=-B0, so its Picard parameter is nonzero; it cannot be silently replaced by 3O. With base divisors (0,3[O]-[Q],[Q]) and B'_a=B_a+[O]-[T_a], direct divisor comparison yields div(v_a)=E_a-E_l+B'_a. The positive degrees and genus-one RR dimensions are (3,1,2).

10. The unsquared RR scalar has the correct sign. The displayed v-product gives t v0 v1 vl=Hprod alpha0^2/x'^2, while 2 delta(z)/(t+k)=-lambda Hprod/x'^2. Therefore eta=-lambda/alpha0^2, eta^2=C4 a0 a1 al, with no square-root choice.

## Boundaries

These deductions exhibit this one map in a surviving 4+2 component, with its actual half-point, constants and nonzero pole class. Descent is to the declared L=Q(alpha,beta,i); no minimal field or smaller real-field descent is proved. They do not settle the other parameter families, a period or homology index, historical blindness, Working Truth, or Foundation status.

The arithmetic implementation is a task-local extension of the existing exact integer-polynomial API. The proof uses the T6 observation-preservation contract by retaining the labels, units, scalars and differential direction needed by later operations. This review does not identify a new mathematical tool family or assert BRC execution.

The final candidate still needs its source-bound full run and actual negative checks, an additional reviewer of the complete disclosed proof/program, immutable publication/full readback, and the unchanged eight-gate durable return. This paper review does not replace those obligations.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@177139a / GLOBAL_KNOWLEDGE_V1
