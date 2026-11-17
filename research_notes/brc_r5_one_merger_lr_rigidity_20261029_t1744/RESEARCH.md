# Enterprise Math R5 — One-merger exact-LR rigidity and finite rational certificate

2026-10-29; AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an exact finite external two-measure stopping model, not a native Heartbeat-X6 physical claim. It does not solve the two-interacting-merger mother question.

## Source pins, BRC carrier and provenance

GLOBAL_KNOWLEDGE_V1 canonical main@2bf1702d3a5b60d026c482a41b87a9f8c4a6784f: 00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE worldview, Enterprise Math TASK route and P000. Enterprise Math main@35458bfe0ecaf9e6ec5e1d5914e5736025797629: AGENTS.md, p000_reality_foundation.json, joint-relation preservation and docs/PORTABLE_RESEARCH_PROTOCOL.md. Predecessor: PR #1663 immutable 1ad57fc5a25823fb42476306228fb842cb001914, research_notes/brc_r5_quantized_lr_phase_diagram_20261029_t1643/RESEARCH.md. This proof uses **exact** LR, not quantized LR.

BRC REUSE_APPLIED: the carrier is the separate positive source/path-labelled P and Q masses and conditional distributions. The observer retains exact likelihood-ratio collisions, terminal declaration and four expected observables. Information is quotiented only after a scoped fiber-preservation proof; there is no native geometric embedding or new BRC implementation.

## Model and scope

At fixed decision time t>=1, a single (t,r) seedless exact-LR key receives finitely many FULL-distinguishable source histories i. Each has Q mass rho_i>0 and P mass r*rho_i, r>0. Histories outside this key, if any, contribute policy-independent observations. One initial choice is stop+declare P, stop+declare Q, or continue. Continuation produces a terminal signal y at t+1, with strictly positive conditional Q kernel q_i(y), P kernel p_i(y), both normalized; declaration P or Q is mandatory. FULL observes source and terminal signal, while genuine seedless LR behavior uses only (t,r) and (t+1,r*p_i(y)/q_i(y)). Behavioral action randomness is local, with no persistent shared seed. Let O=(e_P,e_Q,T_P,T_Q), e_P=P[declare Q], e_Q=Q[declare P].

Define lambda_i(y)=p_i(y)/q_i(y), and the terminal Q-weighted LR measure
nu_i(lambda)=sum_{y:lambda_i(y)=lambda}q_i(y).
For arbitrary real a,b let m(a,b)=min(a*r,b), g_i(a,b)=sum_y min(a*r*p_i(y),b*q_i(y)), I_i(a,b)=m(a,b)-g_i(a,b). Let W=sum_i rho_i.

## Theorem 1 — complete one-merger rigidity

Within exactly the model above, the following are equivalent:
(1) convex hulls of the FULL and seedless exact-LR four-observer behavioral images are equal, equivalently **all** real signed support directions coincide;
(2) nu_i=nu_j for every pair of source histories;
(3) the ACTUAL real behavioral four-observer images coincide.

Source raw terminal signal alphabets and raw conditional probabilities may differ; equality is required only of Q-weighted terminal exact-LR pushforwards. This theorem does not assert equality for arbitrary later interactions or native X6.

**Necessity and gap formula.** For signed w=(a,b,c,d), put tau=c*r+d. Per unit Q source mass, the optimal stop cost is S=m(a,b)+t*tau. The optimal continuation cost is C_i=g_i(a,b)+(t+1)*tau. Terminal minimization depends only on terminal LR, so both strategy classes can achieve each optimal terminal declaration at every terminal collision, for signed a,b as well as positive ones. At the first collision FULL chooses separately by source, LR must share an action. Hence with common policy-independent cost K:

V_FULL=K+W*S+sum_i rho_i*min(0,tau-I_i);
V_LR  =K+W*S+min(0,sum_i rho_i*(tau-I_i)).

These are the true minima over **all real randomized** behavioral policies because the local random actions enter expectations affinely. For each a,b let Ibar=sum_i rho_i*I_i/W and freely choose tau=Ibar, e.g. c=0,d=Ibar. Then

V_LR-V_FULL = sum_i rho_i*max(I_i-Ibar,0)
            = (1/2)*sum_i rho_i*abs(I_i-Ibar).

Thus all-signed hull equality forces all I_i(a,b), hence all g_i(a,b), to agree for every real pair a,b.

Take a=1,b=x>=0. The function g_i(1,x)=sum_y q_i(y)*min(r*lambda_i(y),x) is continuous piecewise affine, and its right derivative away from knots equals sum_{lambda:x<r*lambda}nu_i(lambda). Equality of g_i for every x implies equal jumps at all positive LR atoms, hence nu_i=nu_j. No LR tolerance is involved.

**Sufficiency including zero-flow boundaries.** Suppose all nu_i equal nu. Given any FULL policy let its initial action probabilities be s_i^P,s_i^Q,u_i summing to one. Define shared LR first-stage action probabilities s^A=sum_i rho_i*s_i^A/W for each A in {P,Q,continue}. Let U=sum_i rho_i*u_i. If alpha_{i,y} is the FULL terminal probability of declaring P, define at each terminal LR multiplier lambda with nu(lambda)>0:

alpha(lambda)=
  [sum_i rho_i*u_i*sum_{y:lambda_i(y)=lambda}q_i(y)*alpha_{i,y}]
  /[U*nu(lambda)]   if U>0,
and choose arbitrary alpha(lambda) in [0,1] when U=0.

This is a lawful seedless LR behavior. The continued terminal Q mass at multiplier lambda is U*nu(lambda) for both policies; its P mass is r*lambda*U*nu(lambda). The construction matches terminal P-declaration Q flow, and therefore terminal P-declaration P flow, both errors and both time coordinates. First-stage stop flows match by Q-mass averaging and equal source LR r. Zero-flow keys are immaterial. Every FULL four-observer vector is reproduced by LR, whose class is a subset of FULL. Thus (2)=>(3)=>(1). QED.

## Theorem 2 — finite rational test, no signed direction sweep needed

If r,rho_i,p_i,q_i are rational, set K={0} union {r*p_i(y)/q_i(y)}. The three preceding conditions hold **iff** g_i(1,x) is independent of i at every finite rational x in K. Differences are piecewise affine with all knots in K; they vanish at 0 and for x above the largest knot, where each g_i(1,x)=r. Knot equality implies everywhere equality and the likelihood-ratio pushforward criterion.

If some knot x has sourcewise information values I_i=min(r,x)-g_i(1,x) not all equal, put Ibar=sum rho_i*I_i/W and choose signed direction w=(1,x,0,Ibar). Its **exact rational all-real support gap** is Delta(x)=1/2*sum_i rho_i*abs(I_i-Ibar)>0. For two sources, Delta=(rho_1*rho_2/W)*abs(I_1-I_2). This is a finite proof-producing primal/no-go decision rule, not sampling of directions.

## Strict positive Fraction examples actually executed

Both examples: t=1, r=1, rho_A=rho_B=1/2. Source A (Q,P) conditional pairs:
(1/4,1/8),(1/2,1/2),(1/4,3/8), hence nu_A={1/2:1/4,1:1/2,3/2:1/4}.

SAFE raw-distinct source B:
(1/4,1/8),(1/6,1/6),(1/3,1/3),(1/4,3/8).
It has four raw terminal labels but nu_B=nu_A. The explicit matching map was run on all 1152 source/terminal FULL deterministic assignments and 300 rational randomized policies, obtaining identical genuine seedless-LR four-vectors in every case.

DISTINCT source B:
(1/3,1/6),(1/3,1/3),(1/3,1/2).
At finite knot x=1, g_A=7/8, g_B=5/6, I_A=1/8, I_B=1/6, Ibar=7/48 and Delta=1/96. Therefore for **every real seedless LR policy**

96*e_P+96*e_Q+7*T_P+7*T_Q >= 110.

The FULL policy stop A at t=1 and declare P; continue B, declaring Q only when terminal LR=1/2, P otherwise, yields O*=(1/12,5/6,3/2,3/2) and the left side equals 109. Therefore distance in L-infinity to every seedless LR four-observer vector is at least 1/206. Entire deterministic sets checked: 576 FULL vectors and 24 LR vectors; min integer direction 109 vs 110. Additionally all 625 signed directions with coordinates in {-2,-1,0,1,2} were checked against the exact Bellman formula.

The all-real quantifiers follow the constructive proof, not finite testing. The standard-library Fraction verifier was executed and printed PASS_EXACT_R5_ONE_MERGER_LR_RIGIDITY; EXACT_OUTPUT.txt contains actual stdout. No formal Lean checker or independent mathematical review is claimed.

## Prior art, native authority, next scientific obligation

Related background (not a priority-novelty claim): Laroche and Tachet Des Combes, On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs, ICML 2023, Proceedings of Machine Learning Research 202:18548-18562, https://proceedings.mlr.press/v202/laroche23a.html . That work has a different model and does not verify the present dual-measure calculation.

Native status at this run: research_authority_granted=false; Source gate UPSTREAM_CODE_REVIEW_REQUIRED; 5/5 native jobs active. Bounded active-owner check via em_control_tasks returned CONTROL_QUOTA. Therefore owner, live CLAIM, Research Activity source registration, Result and independent Driver review are not certified; REGISTER_PENDING. GitHub preservation is author-side and not Source admission.

Next: seek a **genuinely coupled two-merger** strictly positive rational experiment on exact collision algebraic constraints. Preserve source/path BRC masses and time; first exclude a strict early opposite-sign Bellman gap, then certify all-signed convex hull equality by an exact primal convex combination of <=5 LR vertices per FULL vertex or an exact Farkas separator. Only for a complete hull PASS test actual real-image nonmembership via certified semialgebraic methods, including zero-flow boundaries. The mother problem remains open.
