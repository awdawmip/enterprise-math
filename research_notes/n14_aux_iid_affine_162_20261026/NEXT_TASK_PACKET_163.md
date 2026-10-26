# Stage163 — next portable research unit (DUAL-ONLY)

Model: external N=14 ternary iid, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Policies see full ordered histories; eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau. V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. Not a native P000/X6/BRC theorem.

Verified AUTHOR Stage162 predecessor: alpha162=440625031179621048365/1265046575011281764352, V162=2138966145833987829541/180720939287325966336. Stage162 dual K=1776538556208/5886215131,L=5152927839848/17658645393, ties R=(10,0,1) Q/C and X=(7,3,3) Q/C. At the end X is saturated immediate Q, while R's immediate-Q probability is 1766864861392271/5911808000000000 (interior). The complete proof and exact replay program are beside this packet.

Stage163 DUAL-ONLY candidate: from Stage162 retain R's Q/C tie along dK=-1, dL=-10592/12501. The X state becomes strict Q. First exact gap closure at t=19719048267802073097/3261849711321095041, K163=163900037061/554150611, L163=476600779976/1662451833. New Y=(8,4,1) P/continue tie joins R, with 680 Bellman states, 1238 positive gaps, minimum 1577397669610597/79424873185738752. **No Stage163 primal interval has yet been established.**

First independent task: compute actual ordered first-hit counts/P/Q masses of R and Y under the new strict Bellman policy; show their prefix cones disjoint (Y's four type-0 draws cannot precede R's zero; R depth10 cannot precede Y depth8). Evaluate four deterministic corners by both exact conditional suffix recurrence and literal unmerged ordered history integer-weight DFS. Derive equality-of-errors coin relation, prove legal range and inherited left Stage162 alpha/V, verify tP>=tQ and dual equality at endpoints, and either prove a complete real interval and strict right endpoint or deliver a precise rational obstruction.

Owner control: author artifact is stored on a branch, no formal Task claim. MCP tasks=CONTROL_QUOTA; native session start=STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Independent review and SOURCE acceptance pending. Use actual owner/role service when restored; do not self-assign prior live claims.
