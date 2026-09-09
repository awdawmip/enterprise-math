# JT2 next observer and retained-state contract

Status: **DRIVER RESEARCH ORGANIZATION / NEW QTF3 PAPER CANDIDATE PENDING REVIEW / NO NEW TOOL**.

This packet continues the existing UR/Sun and QTF3 tasks. It changes no Task, CLAIM, Result or audit gate. The reviewed p² bridge is a declared input; the new fixed-point p³ argument is [qtf3_reflection_degree_candidate.md](qtf3_reflection_degree_candidate.md) and has distinct authorship/review status.

## Source-qualified names and addresses

Use explicit names before any normalization or projection:

| Typed object | Meaning and retained precision |
| --- | --- |
| F_quad(z), L_legendre(u) | The two exact p-1 truncations in candidate9e3a41dc; coefficient labels and p-unit denominators retained. |
| B_Sun(x) | L_legendre((1-x)/2); distinct from the coefficient B_k below. |
| A_Sun(x), C_Sun(x) | Generalized-Legendre parameters 2/3 and -4/3; C_Sun is not C_tail,r. |
| g_raw | F_quad(1/2), required modulo p³ before dividing by p. The 20260827 reflected-product return called this G_p. |
| h_weighted | (F_quad+12z F_quad')(1/2), required modulo p². The 20260827 return called this H_p. |
| G_div | g_raw/p modulo p² after CM0. The 20260828 terminating-jet return called this G_p. The two historical G_p symbols cannot be identified without this division. |
| R_tail | The exact reflected scalar below, observed modulo p. |
| E_QTF3, r_QTF3 | (L_legendre-F_quad∘φ)/p² and E_QTF3/u^p; preserve the defining sign, exact zero prefix and finite degrees. |

The fixed point u=1/2 has φ(u)=1. The CM ports u_-=(1-t)/2 and u_+=(1+t)/2 have φ(u_±)=1/2 in R[t]/(2t²-1). Retain the two ports and their involution. A formal t is a basis/relationship carrier, not a numerically extracted root. Frobenius statements belong to their specified residue precision.

## Recovered reflected scalar; no tail replay

The prior source chain now supplies an explicit definition, not only a symbol:

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2\,2^k},\qquad
C_{\mathrm{tail},r}=\frac{2^{r-1}(r-1)!^2}{18(5/6)_r(2/3)_r},
\]
\[
R_{\mathrm{tail}}\equiv
2\sum_{i=1}^{m}B_i\sum_{r=1}^{i}(1+6(i-r))C_{\mathrm{tail},r}
\pmod p.
\]

The exact source is the 20260827 REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN, §2, at commit6058e8fa, blob3fedf7bef09b426037840721855f9a9d05558a0b. The preceding FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN at the same commit, blobc8c2423e8569a3da27b41bb7f602b4b781bb2a79, gives the exact finite identity S_p=g_raw h_weighted-T_p and the inherited plus-class reduction T_p≡p²R_tail modp³. These are consumed source interfaces; their valuation-block proof and old experiments are not rerun.

Thus the old LIFT still asks for the weighted S_p≡p modp³ at address1/2. The unweighted fixed-point QTF3 candidate does not silently supply that implication.

For the R_tail sum, a finite positive-rational BRC population is explicitly
\[
\{(i,r):1\le r\le i\le m\},\qquad
w_{i,r}=2B_i(1+6(i-r))C_{\mathrm{tail},r}.
\]
Serial composition multiplies these displayed positive factors; alternative composition sums the labeled weights. For this fixed sum alone, exact total mass followed by a valid p-unit residue observer suffices. A future index-dependent reweighting or changed cutoff needs the original labels or a factorization proof; a Boolean support flag or unlabelled total is not that proof.

All denominators above are p-units on p=6m+1: the first p-zero factor indices of (5/6)_r and (2/3)_r are 5m and 4m, whereas r<=m uses only indices through m-1. B_i for i<=m stops before its first p-zero index m. Factorial indices are below p, 18 is a unit, and 1<=1+6(i-r)<=p-6. Preserve these factor ranges as unit witnesses. The signed QTF3/Sun differences are separate algebraic carriers, not negative native BRC branch masses.

## LIFT's explicit digit and carry observer

Retain G_div modulo p², h_weighted modulo p², R_tail modulo p, and the source witness CM0 before division. With chosen integer residue lifts a_0,b_0 and next digits a_1,b_1, write symbolically
\[
G_{\rm div}\equiv a_0+p a_1,\qquad h_{\rm weighted}\equiv b_0+p b_1\pmod{p^2}.
\]
Under the declared UR input, a_0b_0≡1 modp. Retain its carry
\[
\kappa=\frac{a_0b_0-1}{p},\qquad
\Delta_p\equiv\kappa+a_0b_1+b_0a_1\pmod p.
\]
Then LIFT is the exact equality Δ_p=R_tail in F_p. The displayed divisions are symbolic and justified by their valuation witnesses; a future evaluator must produce the real BRC quotient/remainder reconstruction.

This exposes precisely why UR's Boolean truth, G_div modulo p alone, or a dropped multiplication carry cannot determine the next observation. The old Phi_xx contribution must remain in G_div modulo p², equivalently g_raw modulo p³. No new digit value is fabricated here.

## Sun output3 and conditional output6

The current task's proof request remains a derivation, even though the scalar target has qualified p² support from another route. Retain at each labeled port A_Sun,B_Sun,C_Sun modulo p³, their needed first jets modulo p², the p² reflection defects alpha,beta,gamma, CM0/SIMPLE witnesses and the frozen barycentric lift.

The exact next certificate must eliminate adjacent values using the differentiated recurrence while retaining every defect. It must state the coefficient ring and every extra ordinary/generalized-Legendre identity used. Reusing the already-proved scalar target as an assumption inside this elimination would not supply the requested derivation.

If claiming an obstruction instead, freeze the precise relation system, all retained frozen inputs and the target observer. Any separating assignments must satisfy that declared system; a relaxed model that drops the barycentric lift, degree constraints, endpoint normalization or polynomial realizability is only a result about that relaxed model. It is not automatically the task's minimal obstruction. No such obstruction is certified by this packet.

## Existing reuse and the next release boundary

Apply the existing T6 fiber-constancy rule: an observer survives a quotient only if it is constant on every admitted fiber for the declared future operations. The new QTF3 candidate illustrates why the exact finite-prefix and reflection-degree data cannot be erased before the higher-precision observation. Its proof supplies the needed algebra; metadata matches alone do not.

The selected weighted-BRC commitments are pinned at e9f7310b:definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json, blobf375a059fa4af8c6eefaddb4d4a8689a0c063674. The earlier T0/T6 interface packet remains the implementation boundary: paper reuse is applied, no native API call or migration certification is claimed. T5's floor quotient is not silently relabeled as a residue projection.

There is no confirmed tool expression/composition failure. The remaining obligations are mathematical review of the new fixed-point argument, Sun's specified elimination or genuine exact obstruction, and an actual weighted/address-preserving p³ link to old LIFT. A new generic tool would require a concrete failed input/output contract and validated gap first.

The temporary reference worker has ended. Owner reserved current slots for R005/RB; route a new bounded reviewer/worker only when one becomes available and obtain the existing task's current runtime authority before formal execution. The new proof's author is EM-DVR-57CCCE, so its decisive non-author check remains external. Both parent objectives remain separate; no duplicate task or claim is created.

Driver-ID: EM-DVR-57CCCE / CONTROL_PLANE

Global-Knowledge-Sync: main@5f14819 / GLOBAL_KNOWLEDGE_V1
