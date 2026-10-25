# Stage118 portable research task after Stage117 X saturation

## Mother question
Find the exact next affine piece (or a certified obstruction) for `V14(alpha)=inf max(E_P tau,E_Q tau)` over all full ordered-history randomized stopping and decisions up to N=14, subject to `P(decide Q),Q(decide P)<=alpha`, under external auxiliary iid laws `P=(1/8,1/24,5/6)`, `Q=(1/12,1/12,5/6)`. No native P000/X6/Heartbeat transfer is assumed.

## Frozen source/frontier
Stage117 author-checked finite proof (not independently Driver reviewed) is in `research_notes/n14_aux_iid_affine_117_20261026/`. Endpoint:
[
 alpha_{117}=900390161470101555373/2592933255351443128320,qquad
 V_{117}=132635001628579939136609/10371733021405772513280.
]
At this endpoint `X=(7,5,1)` now chooses P with probability 1, `D=(9,1,2)` still decides Q with probability `376073711298041/1042086080000000`, and terminal T chooses P uniquely. Stage117 was dual-`K=7703713039590/8727240137`, `L=7249159245096/8727240137` with exactly two ties (X and D).

## First concrete next question
Keep D tied, make X uniquely stop P, and continue the decreasing `K+L` dual ray. An exact affine-action sweep located a candidate next wall at
[
 K_{118}=rac{254421}{296},quad L_{118}=rac{90232}{111},quad
 G=(13,6,4).
]
At G the **Q-stop / continue** actions tie. The ray step after Stage117 is
[
 x=rac{59905896822963}{2583263080552},quad
 K_{118}=K_{117}-x,quad
 L_{118}=L_{117}-rac{164096}{214569}x.
]
An author-side independent 680-state Bellman recurrence found only D and G tied at the candidate dual and a minimum positive gap `837575281/15909322752`. These numbers are a **candidate dual boundary, not a Stage118 affine interval proof**.

## Required mathematics and evidence
Compute ordered FIRST arrival counts and exact positive rational P/Q mass at G under the unique policies (except the D tie). Analyze its path cones against D and saturated X; check whether G can follow the D mixture and whether the new error/time observer is bilinear. Construct the complete feasible randomization family `eP=eQ`, verify `tP` versus `tQ` and any saturation before claiming a continuous real alpha segment. Produce a global Bellman dual lower bound, primal equality for every real parameter, and sharp right endpoint or an explicit obstruction.

For every new claimed interval provide a completely enumerated horizon-14 rational Bellman certificate, full ordered-history integer-DFS cross-check (not only sorted counts), a proof of averaging history-dependent policies for the declared four observers, and actual executed source output. If any supporting lemma remains unresolved, label the result conditional or exploratory.

## BRC and source limits
Use the exact positive-rational ordered-history carrier and BRC weighted substrate as in Stage117; retain branch provenance, first-hit path multiplicity, and the four error/time moments. Count compression is valid only for the declared iid conditional observers and horizon; it does not establish a general native branch quotient. The protected P000 worldview and its six-axis/three-dimensional-slice constraints remain untouched.

## Governance and actual authority
The previous research is author-side provenance, not a native formal task or result. Current native task-list request returned `CONTROL_QUOTA`; own native session creation was refused with `STATIC_READONLY_SCOPE_DENIED, operation_sent=false`. Re-read current canonical dispatch/owner before any formal claim or overwrite. Persist any completed independent Stage118 science under a new `research_notes/` artifact and verify an immutable GitHub readback. Keep formal Result and Driver acceptance separate.
