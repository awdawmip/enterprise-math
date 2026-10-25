# Stage139 exact continuation — DUAL_CANDIDATE_ONLY

**Question.** After the Stage138 exact full-real optimum in the finite ternary iid N=14 mother model, find the next optimal primal affine interval or an exact obstruction, for arbitrary literal ordered-history randomized sequential policies. This remains an **external auxiliary** problem, not native P000/X6 or a three-dimensional Heartbeat slice.

## Verified author frontier inherited (do not rerun as new theorem)

Stage138 proves for every real 0<=delta<=167776984375/25785362496356352:

V14(alpha137+delta)=V137-(7239344/6941)*delta,

with alpha138=4078711246246925855/11735204976119513088 and V138=217809339038053734409/17602807464179269632. The right support is sharp. B=(11,0,1) Q/continue remains randomized with w=38466217568843437/81438720000000000 at the endpoint; H=(11,4,1) has P-stop probability 1.

The supporting dual K138=3709800/6941, L138=3529544/6941 has 680 exact Bellman states, 1,238 positive nonselected gaps (min=4/187407) and only B Q/C and H P/C ties. Original author proof/certificate and runnable full literal-path code are in the sibling Stage138 research directory. Independent Research Driver review remains pending.

## Stage139 exact dual candidate, not yet primal

Continue from K138,L138 on the ray dK=-1, dL=-112/129, preserving the B Q/C equality; the H P/C tie breaks in favor of P. The first of 838 positive directional gap closures is

t=163927584093618/13009554982193,

giving

K139=978154621902/1874305573,
L139=133227391384/267757939.

The newly tied state is C=(6,3,0) (P/continue) alongside B=(11,0,1) (Q/continue). An exact 680-state independent scan finds 1,238 strictly positive gaps, none negative, min=211792744307/7287300067824, and root

H0,139=1792874224751669050640467609/4889306480521221538578432.

These results form a **dual candidate only**; no Stage139 primal interval/right-sharpness is claimed.

## First exact new lemma: disjoint critical cones

C occurs at observation 6 with three symbol-0 events, while B occurs at observation 11 with zero symbol-0 events. C cannot be an ancestor of B because symbol counts cannot decrease; B cannot be an ancestor of C because observation depth cannot decrease. Hence no literal word visits both tied count states, even allowing history-dependent randomization. Their tie-control contributions have no bilinear cross term. This does **not** assert both are reachable under the strict optimal policy: determine reachable first hits separately.

## Next executable unit

1. Compute the first-hit word inventory for B and C under the strict Stage139 Bellman policy using literal prefix identity and exact positive P/Q mass. State which of the “20” nominal depth-6 C words survive earlier unique optimal stops.
2. Set w=Q-stop at B, h=P-stop at C (both [0,1]). Build the four exact M=(eP,eQ,tP,tQ) corners using bottom-up Fraction and a differently structured ordered integer-weight DFS. Verify mixed corner defect zero.
3. Solve eP=eQ. Check the full real feasible interval for w,h, alpha advance, tP>=tQ and equality to H0,139. Match alpha138 and V138 at the left boundary or prove an exact obstruction.
4. If a primal segment is found, establish its right-sharpness using positive action gaps and mass-averaged complementary slackness. Search the next dual break only after the current unit is resolved.
5. Save complete author evidence in the existing research_notes namespace, with source pins, exact acceptance scope, unchanged P000 and explicitly pending native session/owner/CLAIM and independent Driver review.

## Provenance

Global bootstrap pinned main@a197792a7db5d01e0f517fde56d717be4bfb56c5; EM initial research read main@c4095e2200437eb9e0586ead5f40548bdde5e165. BRC used as positive exact labeled ordered history carrier with only a proved finite iid four-observer quotient. Native control list returned CONTROL_QUOTA; native session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The GitHub source files are ordinary unreviewed author artifacts, not canonical Source Result/CLAIM acceptance.
