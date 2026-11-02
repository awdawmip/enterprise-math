# PREFIX-438 — X6 signed-path moment fibers and minimal diagnostic Port repair

Date: 2026-11-02 (Asia/Shanghai). Author-side portable TASK_RESEARCH; UNREVIEWED / NOT_ADMITTED.

## Source and selected question

Continue PREFIX-437's exact 64-state X6 even-flux auxiliary controller toward typed BRC/Port observation. P000 spatial carrier is the native affine Z^6 torsor, with twelve signed unit steps. The controller's five position parity bits p=(x1,...,x5) mod 2 and phase sign bit t follow, for step sigma*e_j:

p_i' = p_i + [i=j] mod 2, for i<=5;
t' = t + sum_(i<j) p_i mod 2.

Frozen scientific input is enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d, kept separate from the current source snapshot. Current project source read: main@7d5cf2250c5a333307999efbca6d245aba43b724; current account rules: chatgpt-global-knowledge main@cfbfe77d05ceab2961ac0b5c3bab5f7b8b26abbe. Relevant original interfaces: src/enterprise_math/brc_control_port.py (ControlPacket), brc_transport.py (Affine, EffectHistogram, MomentState), and original signed_brc.py blob 300a96e3dc24bf6fff73743037a0347a8bc83176.

The new selected *diagnostic* Port is r1(w) = number of negative e1 steps in a signed path word, modulo 2. This is a declared path-history observer, not an asserted physical Port actuator. Its deterministic update is r1' = r1 + [j=1 and sigma=-1] mod 2.

## Theorem A — exact two-step fiber witness; minimal 128-state repair

The legal native length-two return paths w=(+e1,-e1) and w'=(+e2,-e2) from the same chosen X6 Cell have equal endpoints, durations and terminal (p,t) values; both return those six controller bits to their initial values. Yet r1(w)=1 and r1(w')=0. This is an exact witness that the terminal 64-state sign controller plus exact endpoint and duration does not determine this proposed history Port.

Add the bit r1. The 128 states C=(p,t,r1) admit the exact one-step update above and spatial affine effects x->x+sigma*e_j. Serial composition updates C; BRC alternatives retain positive path multiplicities until the observer is applied.

Minimality applies to a controller with no independent parity oracle, observing terminal (t,r1) and supporting every future signed single-axis update. Different t or r1 states differ at horizon zero. When t,r1 agree but p differs, let k be the first differing parity index among 1,...,5 and append +e_(k+1). Its t update sees the differing prefix, so horizon-one observations differ. All 128 states are accessible when chart starts range over X6 Cells and loops are allowed: a +e1,-e1 return toggles r1 and leaves t fixed; a two-axis plaquette toggles t, with r1 adjustable by an additional return. The construction and pairwise separation prove the exact minimum 128 for this observation language.

The repair bit is non-spatial path memory: even a two-step spatial return can change it.

## Theorem B — all-scale same-duration X6 BRC moment-fiber family

For every integer n>=1 take the 2^n positive unit-weight signed native paths of length n using only +e1 and -e1. Let E_n contain words with an even number k of negative steps and O_n the odd-k words. Their endpoints are (n-2k)e1 with exact multiplicities C(n,k). Both populations have 2^(n-1) paths. Define M_d(E_n)=sum_(k even) C(n,k)(n-2k)^d, and similarly M_d(O_n).

For every d=0,...,n-1, M_d(E_n)=M_d(O_n), but

M_n(E_n)-M_n(O_n)=2^n*n! > 0.

Proof: the difference D_d=sum_(k=0)^n (-1)^k C(n,k)(n-2k)^d is the n-th finite difference of a polynomial of degree d in k. It vanishes for d<n. For d=n the polynomial has leading coefficient (-2)^n, and sum (-1)^k C(n,k) k^n=(-1)^n n!, yielding D_n=2^n n!. The proof covers every n. Any shared subsequent affine map preserves equality for polynomial observers of degree <n by substitution.

For n=4, E_4 has endpoint histogram x1=(-4,0,4) with weights (1,6,1); O_4 has x1=(-2,2) with weights (4,4). Both have moments (M0,M1,M2,M3)=(8,0,32,0), while M4 values are 512 and 128. The exact endpoint-selective Port count[x1=0] is 6 versus 0. All other native coordinates remain zero. Every word in these two families yields the same 64-state terminal (p,t), because j=1 never increments t and after n steps p1=n mod2.

Consequently, the typed quadratic MomentState alone merges these two exact BRC sources if their path-family label is removed, whereas an EffectHistogram retaining affine endpoint translations distinguishes them on evaluate. The moment subfamily uses only legal signed-X6 steps; it is a *selected* BRC branch population, not the full twelve-direction endpoint_multiplicity count. For each fixed finite moment order D, n=D+1 supplies an explicit endpoint-resolved fiber witness.

## Actual checks and next scientific unit

Executed in the working container: exact original signed_brc.py imported from the immutable prior bundle with Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176; an independent exact integer translation-only kernel implementing the documented ControlPacket deterministic, alternatives, then and evaluate laws; all twelve signed transitions for every 64- and 128-state candidate; the two-step witness; all n=1..12 path endpoints/counts and lower moments; 2016 and 8128 complete state-pair separations. Separately, the companion standard-library certificate executed n=1..20 moment identities and all 8128 pair separations. All reported checks passed. These finite runs supplement the analytic all-n proof.

The actual upstream ControlPacket class was read from GitHub, but the local run exercised a source-interface-compatible independent translation/unit-weight implementation rather than importing the full upstream module. The proposed r1 Port is an auxiliary diagnostic interface. Native Sites reported research_authority_granted=false, and canonical owner listing failed CONTROL_QUOTA, so this author-side artifact has no formal CLAIM/Result/Review/Admission.

Next PREFIX-439: execute these packet constructions against the exact imported upstream ControlPacket/EffectHistogram/MomentState classes; compare terminal effect histograms, quadratic moment channels and a declared history Port, then seek a permitted S6-symmetric Port implementation with explicit state cost. Preserve the original X6/typed-BRC native observation-and-dynamics mother objective.