# R5: source-overlap and two interacting nonterminal Bellman decisions

Date: 2026-10-28 Asia/Shanghai. Author-side portable finite two-law research. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Frozen inputs, scope and authority
GLOBAL_KNOWLEDGE_V1 main@398ba80d59d3ea1559e6233eb1823ebdb4df934b: 00_BOOTSTRAP, OPERATING_MANUAL, P000 (verified canonical global blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE worldview and applicable math/code/BRC/EM activity policies. Enterprise Math main@4d32ef6f4fbd8330f762eb7cc9cf8b2a928243c5: AGENTS, p000_reality_foundation, joint relation-observer preservation, HEARTBEAT X6+time, native admissibility, current portable/autonomous protocols, predecessor research_notes/brc_r5_overlap_gluing_20261028_t1948/RESEARCH.md and NEXT_TASK.md.

BRC reuse: exact positive rational two-law branch weights, labeled source history, LR moment transport, retained overlap gamma and ordered stop/continue. The observer (e_P,e_Q,T_P,T_Q) is an N2 auxiliary statistical readout. No native X6 dynamics, ontological inference or future-operation-preserving X6 embedding is claimed. GitHub authenticated identity awdawmip has push permission. The native Sites gateway reports research_authority_granted=false and a static read-only scope; em_control_tasks returned CONTROL_QUOTA, so Source owner and native CLAIM were not verified. This author-side note is not native Result/review/admission.

## Model and observer
At time 1: hidden histories A,B,O have Q masses (1/4,1/4,1/2), P masses (3/8,3/8,1/4) and LR (3/2,3/2,1/2). O is terminal. A and B can stop or continue, full-history separately; LR-only behavior must share one first-stage continue probability x at (time 1, LR 3/2).

Fix 0<g<4/25. At time 2 following A or B, child LR signatures are s=(1/2,1,2,3), with conditional Q distributions

    c=(3g/2, 1/5-5g/4, 1/5-5g/4, g)
    a=(9/25,0,0,6/25); b=(0,3/10,3/10,0)
    q_A=c+a; q_B=c+b.

The conditional P distribution has entries s_i q_h(i)/(3/2). At the fourth child (LR 3), a second nonterminal collision, A/B may stop or continue to time 3. Its four successor LR signatures t=(1,2,4,5) have conditional Q kernels

    z_A=(3/8,1/8,1/8,3/8); z_B=(1/8,3/8,3/8,1/8)

and conditional P entries t_j z_h(j)/3. Other time-2 children and all time-3 children are terminal. Full policies observe hidden source A/B; LR-only unseeded policies share a second continuation probability y at (time 2, LR 3). All local behavior randomization ranges over real [0,1]; there is no persistent randomized seed. Stopping actions declare P or Q.

Define e_P=P(declare Q), e_Q=Q(declare P), T_P=E_P stopping time, T_Q=E_Q stopping time. Minimize L=e_P+2 e_Q+(1/4)T_Q, signed direction lambda=(1,2,0,1/4).

## Local invariants, exact all-real support theorem
For every 0<g<4/25 the kernels are strictly positive (rational when g is rational). Summing Q mass and s-weighted mass verifies normalized P and Q kernels: E_q s=3/2; E_z t=3. Differences are

    q_A-q_B=(9/25,-3/10,-3/10,6/25)
    z_A-z_B=(1/4,-1/4,-1/4,1/4).

Consequently the first local (TV_Q,TV_P)=(3/5,3/5) and the second=(1/2,1/2), CONSTANT over this family. Yet the source-tagged common Q arrival mass at the second collision is min(Q(A,s4),Q(B,s4))=g/4. The predecessor triple-polytope theorem gives the sharp first-stage constraint g<=4/25 for this fixed TV pair; the family realizes each strictly positive interior g.

Terminal optimal declaration at LR r has error cost min(r,2) per unit incoming Q mass. Continuing costs an additional (1/4) per unit Q mass for each extra step. At the second collision the terminal error cost is 2. Direct exact summation gives E_zA[min(t,2)]=13/8 and E_zB[min(t,2)]=15/8, so the per-unit-Q second-stage continue-minus-stop values are

    d_A2=1/4+13/8-2=-1/8,
    d_B2=1/4+15/8-2=+1/8.

Write A fourth-child Q probability a4=g+6/25 and B fourth-child probability b4=g. Since E_qh[min(s,2)]=3/2-q_h(s4), their first-stage fully informed continue-minus-stop values after optimal second-stage decisions are

    d_A1=1/4-a4-a4/8=-1/50-9g/8<0,
    d_B1=1/4-b4=1/4-g>0.

If everyone stops at time 1 and declares Q, L0=5/4. Full-history backward induction therefore chooses A to continue at both nonterminal stages and stops B,O at time 1. The exact ALL-REAL optimum is

    V_full(g)=5/4+(1/4)d_A1=249/200-9g/32.

An unseeded LR-only policy must use x at time 1 for both A,B and y at their common time-2 LR=3 child. By linearity in each local behavioral decision and summation of source-tagged Q masses, its exact objective at every real x,y in [0,1] is

    L_LR(g;x,y)=5/4+(x/4)[13/50-2g-(3/100)y].

Nonoptimal terminal declaration mixtures can only increase L. For x>=0, y=1 minimizes the bracket; minimization over x in [0,1] therefore yields

    V_LR(g)=5/4+(1/4) min(0,23/100-2g).

The exact signed support gap is thus

    Delta(g)=V_LR(g)-V_full(g)
      =1/200+9g/32  for 0<g<=23/200,
      =1/16-7g/32   for 23/200<=g<4/25.

This is strictly positive throughout the entire strict-positivity interval; it increases with g up to 23/200 and decreases thereafter, so its UNIQUE maximum IN THIS ONE-PARAMETER FAMILY is Delta_max=239/6400 at g=23/200. The two-level predictive collision changes the loss by a genuine extra term: freezing second-collision continuation at g=23/200 gives gap 21/800; allowing it yields 239/6400, an increase of 71/6400. Fixed local TV pairs therefore do not determine the global signed-support gap; the retained source-overlap/occupation coordinate matters.

These claims hold for all real local randomization probabilities. Full-history optimality is backward-induction linearity at each decision history. LR objective is explicitly bi-affine in x,y and its minimum is attained at one of its four corners. Finite rational tests are corroborative, not the proof of the real continuum claim.

## Exact four-dimensional witness and exclusion
At g=23/200:

    q_A=(213/400,9/160,9/160,71/200)
    q_B=(69/400,57/160,57/160,23/200).

Continue A at both nonterminal levels, stop B/O at time 1, and declare Q at LR=2 ties. The complete actual observation vector is

    O*=(5051/6400,71/1600,1313/800,1071/800).

Indeed P mass declaring P is 19*a4/32, Q mass declaring P is a4/8; T_P=1+3/8+3*a4/4 and T_Q=1+1/4+a4/4, where a4=71/200. Hence

    L(O*)=7761/6400;   inf_{O in O_LR} L(O)=5/4=8000/6400.

Since the L1 norm of lambda is 13/4, EVERY real LR reachable O obeys

    ||O-O*||_infty >= (239/6400)/(13/4)=239/20800.

The full and LR TRUE images differ; their convex hulls differ as well because this signed support function differs. Thus this model is decisively EXCLUDED from the mother target requiring equality of all four-dimensional signed support functions but inequality of actual behavioral images.

## Reproducibility, prior art, and open problem
VERIFY.py uses Python Fraction only, checks strict positivity, exact mass/moment constraints, both local TV pairs, and computes O via exact terminal-path summation. It checks all 16 full deterministic source action tuples, all 4 LR deterministic action pairs, seven explicit rational g values and 159 further exact g=i/1000 cases. EXACT_OUTPUT.txt is the actual execution output of the corresponding verification program. Exact proof covers all real x,y; no floating point, symbolic proof assistant, independent review or X6 physical simulation is claimed.

Prior-art background: M. Ali Khan, H. Yu, Z. Zhang, 'A simple proof of Blackwell's theorem on the comparison of experiments for a general state space', Economics Letters 247 (2025), DOI 10.1016/j.econlet.2024.112146. This is comparison-of-experiments context, NOT verification of this particular dynamic calculation or a claim of novelty.

Next mathematical unit: find/characterize a two-nonterminal-collision family where every globally active signed Bellman face has source-sign coherence. Either prove strict support separation and reject a candidate, or prove all-direction convex-hull equality before testing true-image semialgebraic nonattainment. Preserve source occupation g; keep P000, native X6 bridge and independent Source review as separate obligations.
