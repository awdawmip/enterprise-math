# R5: Exact signed cone cover for one LR collision; different eight-leaf strict exclusion

2026-10-28 / AUTHOR_PROVED, EXACT_FINITE_CHECKED, UNREVIEWED, NOT_ADMITTED. Local research provenance: EM-R5-LOCAL-20261028-CONE11. This is an external rational two-measure sequential-decision model, not a canonical Task/CLAIM/Result, independent review, P000 physics or native BRC residual attribution.

Frozen authority: GLOBAL_KNOWLEDGE_V1 main@a7e3676a22ef00eeadac53398be856fd804d1006; Enterprise Math main@281ecd321ac38064822ec4b7d28ded183373923c. Read global normative entry, P000, ACTIVE worldview and portable research. Source predecessor: research_notes/brc_r5_unrestricted_8leaf_support_20261028/PROOF.md and NEXT_TASK.md. Mother target remains strictly positive rational models with conv(O_LR)=O_full yet O_LR != O_full under unrestricted seedless decisions.

## A. All-signed exact convex-hull gate

Let h be a full observation history of a finite positive dual-measure tree, R(h)=P(h)/Q(h). A full behavioral policy may choose any local stop/continue and terminal declarations based on h. A compressed policy uses only (time,R) without persistent shared random seed. Its four outputs are O=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P), T_H=E_H τ. For every signed λ∈R⁴, V_S(λ)=inf{λ·O(π):π in S}. Let F and L be the finite deterministic full-history and LR-policy output tables.

**Theorem A.** O_full=conv(F) exactly, even without an external persistent random seed; conv(O_LR)=conv(L). Consequently (i) V_full(λ)=V_LR(λ) for every signed λ, (ii) conv(F)=conv(L), and (iii) each f∈F has an exact convex representation by at most five l∈L, are equivalent. With rational input, successful five-point coefficients may be rational; failure admits an exact rational separating λ.

**Proof.** For either policy class the finite trajectory law is multi-affine in its independent local action probabilities, thus each output is a convex combination of deterministic outputs. The stronger unseeded full-history convexity follows by occupancy-flow averaging: for full policies π1,π2 and θ∈[0,1], write q_i(h) for still-sampling arrival mass under Q. Define at histories with positive q_θ(h)=θq_1(h)+(1−θ)q_2(h),
π_θ(d|h)=[θq_1(h)π_1(d|h)+(1−θ)q_2(h)π_2(d|h)]/q_θ(h);
at zero-reach histories choose arbitrary actions. Induction yields Q flows that mix exactly, and P flows also mix since p_i(h)=R(h)q_i(h), where R(h) is policy-independent. All four outputs mix, without a common seed. Such conditioning depends on hidden full history and need not respect LR compression. Thus O_full is convex and equals conv(F). Equality of all linear minima is equality of compact convex hulls. In R⁴ Carathéodory reduces membership to ≤5 points. Rational finite polytope linear systems admit rational basic representations, and strict rational hyperplane separators when not included. QED.

This is a finite, *complete* all-signed certificate, not a finite direction grid. Enumeration of f∈F and exact rational LP membership in conv(L) either gives ≤5-point rational coefficients for each f or a rational strict supporting direction.

## B. One-collision piecewise-rational cone-cover theorem

Suppose two independent distinguishable first-stage groups A,B feed **exactly one** shared compressed (time,LR) decision signature at stage 2, with common action D={P,Q,C}: stop-and-declare P or Q, or continue. Root early stops, other stage-2 actions and terminal declarations remain free. For each group g and shared action d let V_{g,d} be its finite attainable deterministic root-subtree four-vectors (including strategies that stopped before d would be reached). Set f_{g,d}(λ)=min_{z∈V_{g,d}} λ·z. Then
V_full(λ)=Σ_g min_d f_{g,d}(λ),
V_LR(λ)=min_d Σ_g f_{g,d}(λ).
Equality holds precisely when argmin_d f_{A,d}(λ) intersects argmin_d f_{B,d}(λ), including ties and early-stop masking.

**Proof.** Fixing d removes the only coupling. The two group subtree optimizations then separate. For any two finite arrays (x_d),(y_d), min_d(x_d+y_d)=min_d x_d+min_d y_d iff a common d attains both minima. For each selection σ of active minimizer z_{g,d}∈V_{g,d}, define the rational closed cone Cσ by λ·(z_{g,d}−z)≤0 for all z∈V_{g,d}, all g,d. These finitely many cones cover R⁴. Inside Cσ every f_{g,d} is linear, equal to λ·z_{g,d}. Let G_{σ,d} be its subcone where λ·(z_{g,d}−z_{g,e})≤0 for all g and e∈D. The support functions coincide on all signed directions iff Cσ is covered by union_d G_{σ,d} for every σ.

To detect a violation, select for **every** shared action d some group g_d and alternative e_d, and solve a rational linear system containing Cσ inequalities and λ·(z_{g_d,d}−z_{g_d,e_d})≥1. This captures the complement of the union: at each shared action some group strictly prefers another. Because all forms are homogeneous, any finite collection of strict positive violations can be scaled so its minimum margin reaches 1. Rational feasibility has a rational witness; if every such finite system is infeasible, the signed cones cover all R⁴. Thus exact rational LP is a complete decision method for this topology, without floating-point searching and with signed time penalties allowed. QED.

This one-collision factorization does not claim to handle several interacting collisions; Theorem A remains valid for general finite trees.

## C. New positive rational eight-leaf candidate: exact rejection

At t=1, Q(A)=Q(B)=1/2 and P(A)=1/4,P(B)=3/4. At t=2, conditional Q branch mass is (U,V)=(1/4,3/4) for either history. The unconditional (Q,P,R=P/Q) values are:
AU=(1/8,1/8,1), AV=(3/8,1/8,1/3), BU=(1/8,1/8,1), BV=(3/8,5/8,5/3). Thus distinct ordered histories AU and BU have an actual LR collision R=1.
At t=3 each history gives two equal-Q-conditional-mass leaves, with P/Q conditional multipliers AU=(1/3,5/3), AV=(1/2,3/2), BU=(2/3,4/3), BV=(3/5,7/5). All means are 1, all eight terminal P,Q masses are positive, each measure sums to one, and the terminal ratios (1/3,5/3,1/6,1/2,2/3,4/3,1,7/3) are all distinct.

Choose signed λ=(-18,-10,-2,3). At t=2 AU: costs (stop P,stop Q,continue)=(-1,-2,-17/8); BU=(-1,-2,-15/8). The independently optimized V arms are W_AV=-2, W_BV=-93/8 and t=1 early-stop minima are L_A=-4,L_B=-27/2. With shared action d=P,Q,C the two root cost profiles are f_A=(-4,-4,-33/8), f_B=(-27/2,-109/8,-27/2). Hence V_full=-71/4 and V_LR=-141/8, strictly Δ=1/8.

A concrete full-history optimal policy continues at both roots; at AU continues and declares P at AU0,Q at AU1; AV stops and declares P; BU stops and declares Q; BV continues and declares Q at both terminal leaves. It realizes O*=(41/48,7/16,11/4,5/2). Every **real-valued** seedless LR local-randomized policy obeys
18e_P +10e_Q +2T_P −3T_Q ≤ 141/8,
but O* has LHS 71/4=142/8. Therefore O* lies strictly outside conv(O_LR): THIS MODEL IS EXCLUDED and DOES NOT solve the equal-hull mother question.

Signed-direction robustness: since every output coordinate is between 0 and 3, the gap changes by at most 6||λ−λ0||₁. It remains >0 if ||λ−λ0||₁<1/48. The result includes a negative time coefficient and unrestricted t1/t2 stopping/declaring.

## Exact validation and scope

The separately preserved original Python standard-library Fraction verifier exhaustively enumerates reachability-reduced deterministic policies: 38²=1444 full, 18·8²=1152 LR; exactly 1132 distinct full outputs and 724 distinct LR outputs. It checks positivity, P/Q normalization, only AU/BU shared signature, terminal distinctness, inclusion L⊆F, exact costs and witness, plus exact Bellman/exhaustive agreement at 144 extra signed directions. Actual stdout ends ALL EXACT CHECKS PASSED. These 144 finite directions are CROSS-CHECKS, NOT proof of all-signed claims; those come from the symbolic theorems above. A full LP cone enumeration and an equal-hull counterexample remain OPEN.

Native interpretation only: six-axis X6 Cell chart, first A/B via E1/E2, U/V via E3/E4, last outcome via E5/E6 with **ordered path** retained and separately typed stage time. This is an observer-encoding illustration, neither a native plane nor established native propagation law; P000 untouched. Positive P/Q mass must not be treated as a signed BRC amplitude.

Source control status at read: gateway CODE_REVIEW_REQUIRED and CONTROL_QUOTA on inventory; current native owner not verifiable, no Source-issued CLAIM/Result/independent Driver review. Author artifact UNREVIEWED / NOT_ADMITTED, not canonical Task. Recover by checking Source when available, without impersonation or takeover. Next: run exact rational five-point inclusion or signed LP separator on a genuinely different model; ONLY AFTER equality of convex hulls, attempt all-real polynomial/nonmembership proof.

Evidence ZIP contents: full 16KB PROOF.md, exact tested VERIFY.py, actual EXACT_OUTPUT.txt, NEXT_TASK.md. Local complete ZIP SHA256: f6a77061cfacb4b703b1017f30c59ae772471f5dad2458bfbe92d935edb15949; Git object SHA1 expected for raw ZIP bytes: 98aa2f21ff5cbefd637ceadeddc021a5715d1b74.