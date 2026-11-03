# R5 — Complete sixteen-parameter classification of the serial two-law stopping tree

Date: 2026-11-03 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Objective, assumptions and provenance

The four-observer mother problem seeks a finite two-measure stopped experiment with identical convex hulls for FULL-history and seedless likelihood-ratio (LR) observations O=(e_P,e_Q,T_P,T_Q), but different actual real-behavior images. This note proves a complete model-classification theorem for the existing fixed X→J→K1→K2 tree with four source-specific P/Q answer probabilities and four source-specific P/Q terminal-delay probabilities (sixteen real parameters). This classified topology does not realize the mother counterexample; other topologies remain open.

Frozen SCIENTIFIC inputs: global a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current project/global behavior rules were separately read from verified canonical main. P000 and ACTIVE Heartbeat-world axioms were preserved; this is an auxiliary positive-mass BRC probability-flow model, without native X6 calibration.

Load-bearing author-side predecessors (immutable):
- Enterprise Math d5c15d07bf71d7a66d1cc8fd9bb5e12d58e8ffcc, research_notes/brc_r5_ratio_balanced_time_projection_20261103_t0643/RESEARCH.md — complete two-time projection hull classification.
- Enterprise Math 6fd10b22a5e4615545fa39adc89148d77e371510, research_notes/brc_r5_time_face_fiber_obstruction_20261103_t0735/RESEARCH.md — first strict nonuniform order-branch separation.
- Enterprise Math 330562930d1822369f9e6063292cd5521823916b, research_notes/brc_r5_independent_two_law_k2_20261103_t0236/RESEARCH.md — source-uniform-time eight-parameter answer-kernel classification and actual-image aggregation.
- True physical two-measure path realization: Enterprise Math 0592311ad484d47c449563167d2ae6521ccf4234. General signed FULL Bellman oracle: fbeb40d310d5dbdb2766d4e1994293d74bf830c2.

## Model and exact physical observer

Source labels s=(C,I,BJ,IJ). The K1-success coefficients under P are alpha=(1/2,2/3,1/2,3/4), under Q alpha/2; K2 successes under P are c=2/3, under Q c/2. LR collision keys (time,likelihood ratio) at J,K1,K2 are (2,1),(3,1),(4,2). P/Q K2-success terminal Q-answer probabilities are p_s,q_s; P/Q conditional time-6 (rather than time-5) probabilities are a_s,b_s. Every one of these sixteen parameters belongs to the open interval (0,1).

For FULL real history-dependent controls 0<=x,y<=1, 0<=i<=1-x and independent z_s,t_s in [0,1], define

~~~
w=(1/4,(1-x)/4,y/8,i/8),   d=y/16+3*i/32,
Q_s=w_s*alpha_s*z_s,          S_s=c*Q_s*t_s,
e_P=107/128-21*x/128+d/4 - sum_s p_s*S_s,
e_Q=13/64+3*x/64-d/2 + (sum_s q_s*S_s)/4,
T_P=3+sum_s Q_s+sum_s (1+a_s)*S_s,
T_Q=3+(sum_s Q_s)/2+(sum_s (1+b_s)*S_s)/4.   (1)
~~~

Seedless LR requires i=(1-x)y, shared z_s=z and shared t_s=t. All four coordinates are exact physical P/Q terminal error and stopping-time readouts from the cited tree; source identity is retained until observation. Their finite-horizon behavioral maps are multiaffine in local policy probabilities, so all-real support maxima occur at deterministic corners. Write h_K(n)=max{n·O(K)}. Every support gap below quantifies over ALL real FULL and seedless LR behavioral policies, not merely sampled rational controls.

## Theorem A: the other strict nonuniform time-order branch

For arbitrary reals 0<ell<H<=A<1, let a=(A,ell,H,ell), b_s=rho*(1+a_s)-1, with all b_s in (0,1), and allow all eight p_s,q_s to vary independently in (0,1). In particular 1/2<rho<2. Set

~~~
c=2/3, tau=(ell+H)/2, h=-c*(1+tau), f=1,
n3=(h-f)/(1/2-rho/4), n2=1-rho*n3/4,
g=min{c*(H-tau)/16, (25*c/96)*(tau-ell)} > 0.
~~~

For every real 0<delta<g, the physical four-normal n=(delta,0,n2,n3) satisfies

~~~
h_FULL(n)-h_LR(n)=3*delta/16 > 0.              (2)
dist_inf(W,conv O(LR)) >=
    (3*delta/16)/(delta+abs(n2)+abs(n3)),      (3)
~~~

where W is the explicit FULL strategy constructed below. The formula is independent of all p,q.

Proof. At delta=0, the two linear time coefficients obey n2+n3/2=h=-c(1+tau) and n2+rho*n3/4=f=1. Thus each K1 source's optimized score coefficient is A_s=h+c*(1+a_s)f=c*(a_s-tau). Source C and BJ are strictly positive; I and IJ are strictly negative. The LR score is multilinear in its four controls (x,y,z,t). The uniquely maximizing LR binary corner is (1,1,1,1), selecting sources C and BJ. Among the other 15 corners, the minimum positive pure-time score loss is exactly

~~~
g=min{A_BJ/16, (-A_I)/6+3*(-A_IJ)/32}
 =min{c*(H-tau)/16,25*c*(tau-ell)/96}.
~~~

Indeed, z=0 or t=0 eliminates all positive gains; other z=t=1 choices either drop BJ or activate the negative I/IJ pair, with at least the displayed loss. For any physical policy, 0<=e_P<=1; adding delta*e_P changes the relative scores of any two corners by at most delta. If 0<delta<g, the same LR corner is optimal, even among all real policies. Denote its exact physical observation by V.

FULL chooses x=0,y=i=1, continues both serial decisions only on C and BJ (z_C=z_BJ=t_C=t_BJ=1 and z_I=z_IJ=0), leaving their t values irrelevant. The two time coordinates agree with V exactly, while x changes by -1 and d changes by +3/32. Consequently

~~~
W-V=(3/16,-3/32,0,0), n·(W-V)=3*delta/16. (4)
~~~

To prove W really maximizes FULL over all real controls, use the all-signed Bellman identity from the cited exact predecessor. For n=(delta,0,n2,n3), write

~~~
B=107*delta/128+3*(n2+n3), h_x=-21*delta/128,
h_d=delta/4, k_s=1+a_s-delta*p_s,
L_s=max(0,h+c*max(0,k_s)),
h_FULL(n)=B+L_C/8+max(0,(h_d+L_BJ)/16)
            +max(h_x,L_I/6+max(0,3*(h_d+L_IJ)/32)).  (5)
~~~

Because 0<delta<g, k_s>0, L_C,L_BJ>0, L_I=L_IJ=0 for every admissible p_s. Hence (5) is B+L_C/8+(h_d+L_BJ)/16+3h_d/32, attained by W. Subtracting the LR optimum proves (2); the L∞ distance bound (3) is Hölder's inequality. QED.

Exact strictly positive instance: rho=1, a=b=(3/4,1/4,1/2,1/4), p=q=(1/2,1/2,1/2,1/2), tau=3/8, n2=35/12, n3=-23/3, g=1/192 and delta=1/1000. The actual observations are

~~~
LR V=(5/8,15/64,163/48,151/48),
FULL W=(13/16,9/64,163/48,151/48),
support gap=3/16000, L∞ lower bound=9/508048.
~~~

## Theorem B: the C-only nonuniform ridge

Let 0<ell<A<1 and a=(A,ell,ell,ell), with all b_s=rho*(1+a_s)-1 in (0,1) and independent p,q in (0,1)^8. Set tau=(A+ell)/2, use the same n2,n3, and define

~~~
g_ridge=min{c*(A-tau)/8, c*(tau-ell)/16}>0.
~~~

Then for all 0<delta<g_ridge, the physical normal n=(delta,0,n2,n3) has exact all-real gap

~~~
h_FULL(n)-h_LR(n)=13*delta/64 > 0.           (6)
~~~

Proof. At delta=0 only C has positive time coefficient A_C=c*(A-tau); I,BJ,IJ have common negative coefficient -c*(tau-ell). The unique LR maximizing corner (x,y,z,t)=(1,0,1,1) selects only C. Its pure-time strict margin is exactly g_ridge: dropping C loses A_C/8, while the cheapest unwanted BJ contributes -c*(tau-ell)/16. The I alternative costs c*(tau-ell)/6. For delta below this margin, the LR maximizer is unchanged since the e_P tilt is bounded by delta.

FULL instead chooses x=0,y=i=1, only C continues through K2. Its time pair equals V's, and its answer-coordinate fiber changes by

~~~
W-V=(13/64,-1/8,0,0), n·(W-V)=13*delta/64.
~~~

In (5), L_C>0 and L_I=L_BJ=L_IJ=0. Therefore the exact FULL Bellman value is B+L_C/8+h_d/16+3*h_d/32, attained by W, and subtracting the LR vertex proves (6). QED.

Exact example: rho=1, a=b=(3/4,1/4,1/4,1/4), p=q=1/2, delta=1/1000, tau=1/2, n=(delta,0,3,-8), g_ridge=1/96,

~~~
LR V=(121/192,25/96,157/48,595/192),
FULL W=(5/6,13/96,157/48,595/192),
gap=13/64000, L∞ lower bound=13/704064.
~~~

## Theorem C: complete 16-real-parameter classification (relative to cited predecessor proofs)

For every a,b,p,q in (0,1)^4 each, the following are equivalent in the model (1):

~~~
conv O(FULL)=conv O(LR)

iff

a_C=a_I=a_BJ=a_IJ,
b_C=b_I=b_BJ=b_IJ,
p_C=p_I=p_BJ=p_IJ,
q_C=q_I=q_BJ=q_IJ.                                  (7)
~~~

Under these conditions the ACTUAL real-behavior images are equal O(FULL)=O(LR), and the common image has nonempty four-dimensional interior.

Proof. Four-hull equality implies equality of its two-time coordinate projection. The exact predecessor time-projection classification (d5c15d0...) therefore forces common rho_s=(1+b_s)/(1+a_s), a_C>=max(a_I,a_BJ), a_IJ=min(a_I,a_BJ). Every nonuniform a in this ordered class is exactly one of:
(a) a_I>a_BJ=a_IJ, eliminated by the previous source-fiber theorem (6fd10b2...);
(b) a_BJ>a_I=a_IJ, eliminated by Theorem A;
(c) a_I=a_BJ=a_IJ<a_C, eliminated by Theorem B.
The inequalities admit boundary equalities a_C=a_I or a_C=a_BJ as already included. Hence hull equality forces a source-uniform; common rho then forces b source-uniform.

Write these common values as a0,b0. Let R1=sum_s Q_s, R2=sum_s S_s. The timing readout is

~~~
[T_P-3]   [1     1+a0    ] [R1]
[T_Q-3] = [1/2   (1+b0)/4] [R2],
det=(b0-1-2*a0)/4 < 0.                              (8)
~~~

The baseline no-extra-delay time map has matrix [1,1;1/2,1/4] with determinant -1/4. Both maps invertible; the answer coordinates in (1) are unchanged. Thus an invertible affine change of the last two coordinates identifies this common-a,b family with the already-proved eight-answer-kernel family (3305629...). That exact theorem forces p uniform and q uniform separately if four-hull equality holds. Conversely, if all four source-kernel vectors are uniform, the established exact FULL→LR real-policy aggregation matches (x,d,R1,R2), and (8) preserves all true observers. The four-dimensional nonzero internal Jacobian of the uniform baseline is also preserved by the invertible timing map. QED relative to the three cited predecessor author proofs.

This exhausts ONLY the fixed four-source two-serial-key topology with one source-dependent K2 post-success delay/answer mechanism. The parent mother problem remains open for changed stopping-network topology.

## Executed verification

The adjacent self-contained standard-library Fraction verifier VERIFY.py was actually executed on 10 strictly positive rational parameter cases (7 Theorem-A, 3 Theorem-B), including rho=1, 4/5 and 6/5, upper-level ties, near-boundary answer probabilities and independent p,q. It exactly enumerates 20,480 FULL deterministic controls and 160 LR controls, verifies both signed-support maximizers, Bellman values, pure-time corner margins, source-fiber observations and support-gap formulas. Separate nonbinary flow tests check the uniform-a,b invertible clock change. Saved stdout EXACT_OUTPUT.txt: 20,735 exact assertions passed, terminal PASS_EXACT_R5_16_PARAMETER_CLASSIFICATION.

The all-real conclusions arise from the analytic deductions and the named predecessor theorems, not from extrapolation of these ten rational tests. Mathematical admission is pending independent review.

## Authority and next question

GitHub connector identity: awdawmip, repository permissions admin. Site gateway reports static_machine_readonly, research_authority_granted=false. Bounded active-owner read errored CONTROL_QUOTA, so no native owner, CLAIM, Result or independent Driver review is asserted. This is author-side PR branch publication and evidence only. Scientific frozen pins, P000 and ACTIVE worldview are unmodified.

Next, introduce a topological change outside the classified 16-parameter family (e.g., another genuine post-K2 conditional decision with memory or a third source-sensitive merger), compute its exact P/Q stop/answer observer, then demand all-signed four-hull equality via rational FULL-vertex-to-LR convex mixtures or rational Farkas separation before testing real-image nonmembership.
