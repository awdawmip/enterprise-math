# R5 — arbitrary source-sensitive activated-L action errors: sharp minimax obstruction

2026-10-31. Portable author proof; **UNREVIEWED / NOT_ADMITTED / no native CLAIM**. This is an auxiliary finite P/Q stopping model, not an established native X6 or physical theorem. It extends the immutable predecessor d88a158ff87e1d6c2c84423c1f93c7654f49b11b, research_notes/brc_r5_activated_L_gate_residual_time_gap_20261031_t0740/RESEARCH.md.

## Fixed sources and role
GLOBAL_KNOWLEDGE_V1 main@476bc97821e1bba3ba6af0604951029c10989c94, and enterprise-math main@29ee73fad57501e0250bdd01bf90bc4d2bd41cd5, both verified during this research turn. Read current global bootstrap/manual, P000 and ACTIVE worldview, task/registration/BRC/math/code policies, and project autonomous/portable protocols. No protected ontology was edited. This automation conversation is an **unregistered local portable research author**, not the owner of a canonical Task: current native status research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED; bounded native task/owner inventory replied CONTROL_QUOTA. No Source activity/session/CLAIM/Result/independent review is asserted.

## Model and exact new family
Retain previous Q hidden-origin masses (A0,A1,B,C0,C1)=(1/8,1/8,1/4,1/4,1/4) and P masses (1/4,1/4,1/4,1/8,1/8). Hidden A origins continue with probabilities x_i. Q conditional next-label kernel K_i over (Y,L,M,H), LR multipliers (1,3/2,2,3), is

K_i=(1/4, ell_i, 1/2-3ell_i/2, 1/4+ell_i/2), 0<ell_i<1/3.

Its conditional P version equals (r_j/2)K_i(j). The Q and P row sums are exactly 1 and all natural masses strictly positive. Other decisions are Y stop u_i, B stop u_B, C continuation z_i. L (LR=3/2) truly STOPs at time 3 or CONTINUEs to time 4; FULL chooses independent source-labelled continuation v_i; seedless LR shares x,u,z,v across the colliding histories. Observer is O=(eP,eQ,TP,TQ).

NEW: choose arbitrary real L STOP error probabilities a_i and L CONTINUE error probabilities b_i independently for each hidden origin i, 0<=a_i,b_i<=1. No other error rates, transitions, natural paths, actions or observer components change. The previous case had a_i=b_i=1/8. The Q and P positive labelled mass reaching L from source i are respectively ell_i*x_i/8 and 3ell_i*x_i/16. Hence, against the old 1/8 baseline,

delta_eQ = (1/8) sum_i ell_i*x_i*((a_i-1/8)+v_i*(b_i-a_i)),
delta_eP = (3/16) sum_i ell_i*x_i*((a_i-1/8)+v_i*(b_i-a_i)).

Stopping times are unchanged. This preserves **origin labels until the actual observer evaluation**; it is not a statement that origin-flow collapse is globally harmless.

## Theorem (all real behavioral policies and error parameters)
Use signed 4-observer direction J=14eP-19eQ+2TP-4TQ and q_+=max(q,0).
Set A_i=2(a_i-1/8), B_i=2(b_i-a_i)-1,
C=sum_i ell_i*A_i, D=sum_i ell_i*B_i, Pplus=sum_i ell_i*(B_i)_+.
Then the exact supports over all real FULL and seedless LR behavioral policies are

sup_FULL J = (-53+1+C+Pplus)/8,
sup_LR J   = (-53+(C+(D)_+)_+)/8.

Their exact gap is

Delta_J = (1+C+Pplus-(C+(D)_+)_+)/8
        >= (1-(ell_0+ell_1)/4)/8 > 5/48 > 0.

**Sharpness:** for each fixed real ell_0,ell_1 in (0,1/3), the **minimum** gap over the entire closed four-parameter error cube [0,1]^4 equals 1/8-(ell_0+ell_1)/32, attained at a_0=a_1=b_0=b_1=0. For all error parameters strictly between 0 and 1, this is the corresponding infimum. Across the admissible open ell-square the uniform 5/48 is an infimum, not an attained minimum.

A deterministic maximizer FULL is: x_0=x_1=u_0=u_1=z_0=z_1=1, u_B=0, v_i=1 if B_i>0 and 0 otherwise. Its observation O* satisfies for **every real** seedless LR observation Y:

||O* - Y||_infinity >= Delta_J/39 > 5/1872,

because the coefficient l1-norm of J is 14+19+2+4=39. Therefore four-dimensional FULL/LR convex hull equality is impossible throughout this entire continuous error family, whether or not ell_0=ell_1. No rank assumption is required for this exclusion.

## Proof
Prior exact observation equations imply 8J_old=-53-u_B+w-E with w=(x_0*u_0+x_1*u_1)/2 and E=sum_i ell_i*x_i*v_i. New source-labelled error corrections contribute 8(J-J_old)=2 sum_i ell_i*x_i*((a_i-1/8)+v_i*(b_i-a_i)); thus

8J=-53-u_B+w+sum_i ell_i*x_i*(A_i+B_i*v_i).   (1)

FULL chooses u_B=0, u_i=1 to maximize the positive w contribution (then w=(x_0+x_1)/2), and chooses v_i=1 for positive B_i, 0 otherwise. Because a_i>=0 gives A_i>=-1/4 and ell_i<1/3, each resulting x_i coefficient 1/2+ell_i*(A_i+(B_i)_+) > 1/2-1/12>0. Therefore x_i=1 gives exactly the FULL support formula and the explicit witness.

Seedless LR has x_0=x_1=x, u_0=u_1=u_B=u, v_0=v_1=v. Here w=x*u and -u_B+w=u*(x-1)<=0, so choose u=0. The remaining variable term is x*(C+v*D), whose real x,v in [0,1] optimum is (C+(D)_+)_+. z does not occur in (1). This gives the LR formula.

Set S=C+(D)_+. If S>=0, then 8Delta=1+Pplus-(D)_+>=1 by positivity of ell_i and the elementary sum-positive-parts inequality Pplus>=(D)_+. If S<0, then 8Delta=1+C+Pplus>=1-(ell_0+ell_1)/4, since A_i>=-1/4 and Pplus>=0. Thus the lower bound holds in both cases. All four errors zero yield A_i=-1/4 and B_i=-1, so S<0 and equality holds in the parameter-specific bound. As ell_0+ell_1<2/3, the strict uniform 5/48 follows. The FULL witness maximizes J; Holder's inequality |J(O*)-J(Y)|<=39||O*-Y||_infinity gives the distance bound. QED.

The policy observer is multi-affine in the local Bernoulli probabilities: in this finite acyclic experiment every information-set decision appears at most once along each realized trajectory. Accordingly each linear support functional has a deterministic maximizer, with the algebraic optimization above covering all real behavioral probabilities. No finite-grid extrapolation is used for the theorem.

## Reproducible exact check and scope
Sibling VERIFY.py is actual executed Python standard-library Fraction code, and EXACT_OUTPUT.txt is its stdout. Seven exact rational model instances each enumerate **512 FULL and 16 LR deterministic policies**: total 3584 FULL plus 112 LR exact observer vectors. It checks all Q/P row normalizations, strict branch positivity, error admissibility, both signed support formulas, sharp lower bounds (including closed-error minimizers), and a legal maximizing FULL witness. Output ends PASS_EXACT_R5_ACTIVATED_L_ALL_ERROR_KERNEL_MINIMAX_NO_GO. The finite regression is distinct from the real-quantified algebraic proof. No Lean proof, independent review or native Source admission occurred.

BRC use: origin-labelled nonnegative P/Q branch flows are REUSE_APPLIED from the previous carrier, with source-specific L-error projection preserving provenance until the declared stop/continue observer. It is not signed-amplitude cancellation. This no-go does **not** exclude source-dependent new natural transitions, altered upstream u_B/w coupling, new interacting LR mergers, altered upstream error rewards, persistent random seeds, other observation targets, or claims of correspondence to X6 natural dynamics.

## Research continuation
Changing only the L-gate STOP/CONTINUE error probabilities cannot cancel the inherited support obstruction, even with source dependence. Next replace a downstream natural transition or add an interacting merger that changes the upstream coupling w-u_B, while retaining strictly positive Q/P rows and likelihood-ratio moment constraints. Derive the full observer map. Check two-time hull equality, then certify **ALL signed 4D hull equality** by exact <=5 LR-vertex rational convex combinations for every FULL deterministic vector or a Farkas separator. Check rank 4; only after equality should one prove actual real LR-image nonmembership by semialgebraic methods. The mother question stays OPEN.

Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.