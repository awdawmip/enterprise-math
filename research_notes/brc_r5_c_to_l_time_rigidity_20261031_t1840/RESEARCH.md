# R5 18:40 — source-independent natural C→L detour: all-real time-hull rigidity

Date: 2026-10-31 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is an auxiliary finite two-law stochastic stopping process, not an accepted native X6 theorem.

## Frozen source inputs and authority
GLOBAL_KNOWLEDGE_V1 canonical main `e848bbb6de55e7e9c21057a9ce92f7a66f70d503` (both entries, P000 full/projection, ACTIVE worldview, mathematical/BRC/activity procedures); Enterprise Math canonical main `6c20d83d79d260c09b24824cadbf65dedeaf8e5e` (AGENTS, autonomous research and portable protocol). P000 original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches same-snapshot projection. Immediate predecessor: `f434bcc901de69cbe7d9e142cd287a03fe4a7d07:research_notes/brc_r5_error_invariant_time_separator_20261031_t1740/README.md`; base two-merger model: `e7916482f44a925e11ece98e406309f4655fb1f1:research_notes/brc_r5_positive_two_merger_rigidity_20261031_t1340/README.md`. These are unreviewed author-side mathematical inputs; the construction/proof below is self-contained. Current gateway directed-research context reports `authority_granted=false`; owner inventory query returned `CONTROL_QUOTA`. No certified current Source Owner/CLAIM/Result/independent review.

## Full source/path-labelled positive-weight BRC model
Two hidden origins i=0,1 carry Q=P prior mass 1/2 and initial likelihood ratio LR=1. Let real `0<alpha_i<1/2`, `0<kappa<1`. At stage 1 key A=(time1,LR1), choose STOP time1 or CONTINUE. Upon continue, nature selects stage2 D,C,Y at conditional Q probabilities `(alpha_i,1−2alpha_i,alpha_i)` and conditional P probabilities `(alpha_i/2,1−2alpha_i,3alpha_i/2)`, with node likelihood ratios `(1/2,1,3/2)`.

At D=(time2,LR1/2), STOP time2 or CONTINUE; continuation Q routes are 2/3 to terminal (time3,LR1/4) and 1/3 to shared L=(time3,LR1), with P conditional routes 1/3 and 2/3. At Y=(time2,LR3/2), STOP time2 or CONTINUE; continuation Q routes are 1/2 to terminal (time3,LR2) and 1/2 to the same L, with P conditional routes 2/3 and 1/3. L STOP ends at time3; L CONTINUE ends at time4, always LR1.

**New strictly positive nature detour:** C=(time2,LR1) has *no agent action*; nature independently absorbs at time2 with Q=P conditional probability 1−kappa, or passes to **the same shared L** at time3 with probability kappa. All positive natural routing masses are preserved for the open parameter domain. Every terminal Q-cylinder mass q of LR lambda has P mass lambda*q; total P and Q terminal mass is 1 for any strategy by the per-node LR moment identity. FULL behaviour can depend on origin/path (including L-entry C/D/Y). Seedless LR behaviour can use only the common (time,LR) keys A,D,Y,L and shares each action probability across all histories at that key. No persistent random seed.

Observer: `O=(error_P,error_Q,T_P,T_Q)`. Terminal errors may be any admissible history/source/path-dependent action response, common to both strategy classes. Signed directions below use only time coordinates and are independent of such responses.

## Universal theorem and quantitative certificate
Set `s=(alpha_0+alpha_1)/2`, `Abar=1+kappa`, `u=2*(Abar−s*(2*kappa−1))`, `v=−(u+s)`, and `H=u*T_P+v*T_Q`. For **all real** alpha_0,alpha_1 in (0,1/2), kappa in (0,1) and all admissible terminal-error kernels,
```
sup_FULL H       = −s + (1+kappa)*abs(alpha_0−alpha_1)/4
sup_seedless_LR H = −s
Delta_H          = (1+kappa)*abs(alpha_0−alpha_1)/4.
```
Thus the **two-dimensional stopping-time convex hulls are equal iff alpha_0=alpha_1**. When equal, their **actual two-time real behavioural observation sets** coincide and equal a compact convex flow polytope. When different, their **full four-observer convex hulls differ** under every terminal-error kernel since the time projection already separates. A FULL maximizer has distance from the entire LR time convex hull (hence entire LR four-hull, by the time coordinates) in L∞ at least `Delta_H/(abs(u)+abs(v))=Delta_H/(2*u+s)`.

## All-real analytic proof
Per Q mass at terminal LR lambda and time t, the H payoff is `w_lambda*t` with `w_lambda=u*lambda+v`. From the definition of u,v and s, on the full open domain:
```
w_1       = −s < 0,
w_(1/2)   = −u/2−s < 0,
w_(3/2)   =  u/2−s = 1+kappa−2*kappa*s > 0.
```
Hence L optimally STOPs at time3 instead of time4 (negative w_1); D optimally STOPs at time2 instead of time3 (negative w_(1/2), and continuation conserves conditional mean LR 1/2); and Y optimally CONTINUEs to time3 instead of time2 (positive w_(3/2), conserved mean LR 3/2). These are strict, history-independent Bellman choices, so shared D,Y,L actions cause no conflict for this direction. C's forced nature split has conditional value `(2+kappa)*w_1=−(2+kappa)*s`.

A STOP at time1 has payoff `−s`. Given origin i, A CONTINUE followed by optimal lower controls has
```
V_i = alpha_i*(2*w_(1/2))
    + (1−2*alpha_i)*((2+kappa)*w_1)
    + alpha_i*(3*w_(3/2))
    = −(2+kappa)*s +(1+kappa)*alpha_i,
V_i−(−s)=(1+kappa)*(alpha_i−s).
```
FULL may independently choose the better A action in each origin; seedless LR must use a single A action. Since average alpha is s, LR's maximized A value is −s. Exactly one origin is above s and the other below unless equal; averaging the two positive parts gives the FULL bonus `(1+kappa)*abs(alpha_0−alpha_1)/4`. Every path visits a given policy decision only once, so the expected reward is multi-affine in local real behavioural probabilities and its maxima occur at deterministic policies. This proves both support claims, with all-real quantifiers.

If alpha_0=alpha_1, Q natural transition pushforwards depend only on observed (time,LR) key, also at C and L. For any FULL policy, aggregate exact Q node-action occupancy at each A,D,Y,L, and take the observed-key action probability equal to aggregate Q STOP flow divided by total Q occupancy (arbitrary when zero). P mass at each key equals LR times Q mass, including paths that arrive at L from C,D,Y, so this single seedless LR Markovization reproduces *both* P and Q time/action flows inductively, including C's forced branch. The converse inclusion is immediate. All admissible key occupancy flows are characterized by finite linear conservation equations and nonnegativity and can be realized by this Markovization; their two-time linear readout image is a compact convex polytope. Under path-dependent terminal errors, this only proves the **time projection**, not equality of the four-error observation images.

Finally for a FULL maximizer x and any LR hull point y, `H(x)−H(y)>=Delta_H`; dual Hölder gives `||x−y||_infinity>=Delta_H/(|u|+|v|)`. QED.

## Explicit strict-positive rational witness
Choose `alpha_0=1/4,alpha_1=1/8,kappa=1/4`. Then `s=3/16`, `(u,v)=(43/16,−46/16)`; integer direction `J=43*T_P−46*T_Q`. FULL CONTINUEs at A only for origin0, D STOPs, Y CONTINUEs and all L STOP. Its exact time pair is `(T_P,T_Q)=(7/4,27/16)`. Exact maxima are `sup_FULL J=−19/8`, `sup_LR J=−3`, gap `5/8`; its time/four-observer L∞ distance from the entire LR convex hull is at least `(5/8)/(43+46)=5/712`. The terminal errors may be any admissible responses; H ignores them.

## Exact computation and scientific scope
Standalone standard-library `VERIFY.py` enumerates **4096 FULL plus 16 LR deterministic policies** per each of nine rational parameter triples, checks exact two-law normalization, Bellman maxima, the symbolic gap formula, and exact rational 2D-hull membership of all 4096 FULL time points in each of two equal-origin rational instances. The script also checks the explicit witness and bound. `EXACT_OUTPUT.txt` records the actual execution, ending `PASS_EXACT_R5_C_TO_L_DETOUR_TIME_HULL_RIGIDITY`. All-real conclusions rest on the analytic proof, not finite sampling.

BRC reuse is the exact origin/route/port-labelled positive Q path mass, transported as P=lambda*Q before the **signed observer**. The source residual alpha_0−alpha_1 survives the added C→L collision in the support gap. This is an auxiliary finite external stopping model, not a native X6/heartbeat physical model. Its mother target (equal four-hulls but unequal actual real four-images) remains open; source Owner/review/admission are pending.
