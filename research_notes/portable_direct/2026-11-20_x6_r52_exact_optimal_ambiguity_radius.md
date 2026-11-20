# X6 R52 — An exact globally optimal common-bias ambiguity radius in the four-word BRC observer

Date: 2026-11-20 (Asia/Shanghai). Scope: conditional R44/R47 once-only whole-triad graph; original Researcher EM-X6-214D9C and Activity RA-545183ADD4EF71C3E4698AEE. Status: AUTHOR_PROOF / EXACT_RATIONAL_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## 1. Question and preserved source assumptions

Continue R51 (which corrected R50's noise contrast and disproved its original uniform radius). For an integer Port count p>=1, two positive source weights α,β with S=α+β, P=αβ, 4P<=S², the exact positive BRC root mass in the event-word order (F,FT,FF,FRF) is

    A_p(S,P) = (pS, (p-1)S, 2(p²−1)P, 2pP).

Each four-channel measurement is z=A_p(S,P)+b·(1,1,1,1)+ε, with arbitrary common additive bias b and |ε_i|<=η. A rival may have its own Port count q, weights and bias. What is the **sharp worst-case noise radius** for distinguishing Port count at one fixed true parameter instance, even against unbounded q?

Fix the true instance

    p=4, α=99/100, β=1/100, S=1, P=99/10000, b=0,
    A_4=(4,3,297/1000,99/1250).

Define η_crit as the infimum η>=0 for which some rival positive-weight q≠4 and some observation z are simultaneously η-consistent with the true and rival models, allowing separate arbitrary common biases. Equality is included when the observation sets touch.

## 2. R52 theorem: exact optimal radius over all competing integers

**Theorem.** For the declared fixed instance,

    η_crit = 97079/2000000 = 0.0485395 exactly.

For every η<η_crit, any four-channel observation at that error bound identifies p=4 uniquely among all q>=1 and all strictly positive source weights. At η=η_crit, q=5 has a positive-weight rival realizing the same observation. Thus the bound is both necessary and sufficient for this fixed true parameter instance.

### Proof: universal lower bound for any rival

Set C_q=q²−q−1 and use R51's corrected offset-null contrast

    L_q(z)=(d−h)−C_q[(x−y)−(x−h)/q].

Its coefficient norm is exactly N_1=2 and N_q=2q(q−1)=2(C_q+1) for q>=2. For any exact q-model plus arbitrary bias, L_q is zero. If a common measured z belongs to both radius-η error boxes around the true vector and some q-model (with any bias), the triangle inequality yields

    |L_q(A_4)| <= 2η N_q.

For q>=2, q≠4, the exact contrast identity gives

    |L_q(A_4)| = |4−q|/q · [C_q+(99/5000)(4q+1)]
                >= |4−q| C_q / q.

Therefore every potential rival q>=2 must satisfy

    η >= |4−q| C_q / [4q(C_q+1)].

For q=2 the right side is 1/8. For q=3 it is 5/72. For q>=6 it is

    (1−4/q) · C_q/[4(C_q+1)].

Both factors are positive and strictly increasing for integer q>=6, hence this is at least its q=6 value 29/360. Each of 1/8, 5/72 and 29/360 strictly exceeds 97079/2000000.

For q=1, every exact one-Port model has d−h=−2P_q<0, whereas the true vector has d−h=2C_4P=1089/5000>0. Two radius-η four-channel boxes can overlap only if the true gap 1089/5000 is less than 4η (strict positivity for the q=1 model), requiring η>1089/20000, which also exceeds the proposed η_crit.

The only remaining rival is q=5. Here C_5=19, N_5=40. The exact contrast identity reads

    L_5(A_4) = −97079/25000,

so the sharp necessary lower bound becomes

    η >= |L_5(A_4)|/(2N_5) = 97079/2000000.

Thus no rival can match below η_crit; the proof covers **all** positive integers, without finite cutoff.

### Proof: exact positive-weight witness achieving the bound

Choose a five-Port rival with

    q=5, S_q=402921/500000, P_q=10841/1000000,
    b_q=−126289/1000000.

These parameters admit strictly positive real source weights because

    S_q²−4P_q = 151504332241/250000000000 > 0,

so their two weights are the positive roots of t²−S_q t+P_q.

The rival's unbiased masses are

    A_5=(402921/100000,402921/125000,32523/62500,10841/100000).

Now choose the single common measurement

    z=(7902921/2000000,6097079/2000000,691079/2000000,61321/2000000).

Its four errors relative to the true instance are exactly

    (−η_crit,+η_crit,+η_crit,−η_crit),

while its errors relative to the rival instance **with bias b_q** are exactly

    (+η_crit,−η_crit,−η_crit,+η_crit).

Both satisfy all four simultaneous correlated-error checks from R50.1. This realizes the lower bound and proves global optimality. QED.

## 3. Relation to previous research and BRC meaning

R51's corrected uniform sufficient radius for p=4 here is S/[8(p+1)]=1/40=0.025, whereas this **fixed-instance exact optimum** is 97079/2000000≈0.04854. The distinction is material: R51's radius holds uniformly through a closed-form sufficient inequality; R52 exploits the actual positive source-weight product of one fixed true model and the exact rival constraints to obtain a stronger instance-specific bound. R50's earlier 1/20=0.05 assertion was disproved by R51 and remains superseded.

This is a rooted four-word, positive BRC mass observer over the conditional R44 named-port graph. It uses no phase cancellation and claims no derived law in the native frozen P000 Cell/Link/Port world. Time is event ordering. The third coordinate of a three-dimensional research slice, actual triadic release/reoccupation admission, and provenance-preserving native mapping remain independent open questions.

## 4. Exact verification and durable evidence

Source: research_notes/portable_direct/x6_r52_exact_global_ambiguity_verify.py.
Results: research_notes/portable_direct/x6_r52_exact_global_ambiguity_results.json.

The Python Fraction program executes exact rational vector equality, checks the positive-source-weight discriminant, verifies all eight error coordinates at equality, verifies the exact contrast norm and threshold, and tests 998 distinct competing integers q in 1..1000. The universal q>=6 exclusion is the symbolic monotonicity proof above; finite testing is a corroboration, not a replacement for that proof.

Original frozen P000 science is unchanged. The result is author-proved and checked, not independently reviewed or formally accepted. Next useful direction: an exact general instance-dependent minimax algorithm over (p,S,P), including correlated common-bias projection and nonattained infima; separately test the native TRIADIC_CLOSURE_E admission of R/T candidate operations. Preserve the new R51 erratum and this R52 witness as distinct science units.
