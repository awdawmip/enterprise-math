# R5 — Strong second-gate activation still separates the complete four-observer convex hull

Date: 2026-11-05. Mode: TASK_RESEARCH author-side portable derivation. Status: AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. The parent R5 target (equal convex hulls but unequal real behavior images) remains OPEN.

Frozen scientific source pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Behavioral normative context was separately read from current main; this does not change the frozen scientific inputs.

## 1. Exact question and model

The preceding author-side study proved a first-gate Jensen separation for a source-dependent first probability kernel, using a signed time normal that suppresses the second gate only for 0<epsilon<=5/8. The unresolved local question was whether **strong terminal information at the second gate** could compensate for the first-kernel difference. Here the second gate is deliberately activated and a new normal shows that the **same entire positive one-parameter family 0<epsilon<=1** still has STRICT convex-hull separation.

At time 1, hidden source h is A or B, with P and Q source weights w_A=w_B=1/2 and common likelihood ratio 1. On continuation the time-2 likelihood-ratio keys are R=(1/2,1,3/2). Source Q kernels are

- K_A=(1/4,1/2,1/4);
- K_B=(3/8,1/4,3/8).

All have positive entries, sum to 1, and their R-moment is 1. Their induced P probabilities are r_j K_h(j).

At time 2, STOP and declare P/Q or CONTINUE are allowed. A continuation from r_j reaches a terminal likelihood-ratio key in S=(1/4,1/2,1,3/2,7/4). Write the positive source-INDEPENDENT Q kernel M_j(epsilon)=(1-epsilon) delta_{r_j}+epsilon V_j, where

- V_low=(11,1,1,1,1)/15;
- V_mid=(1,1,1,1,1)/5;
- V_high=(1,1,1,1,11)/15.

Their S-moments are 1/2,1,3/2, respectively; induced conditional P probabilities are s M_j(s)/r_j. Every Q and P transition on the full listed terminal support is strictly positive for any REAL 0<epsilon<=1. At times 1 and 2 both decisions and unrestricted P/Q declarations are legal; at the time-3 terminal any P/Q declaration is legal. FULL may condition on hidden source, whereas seedless LR sees only (time, likelihood ratio). Policies may use arbitrary real action probabilities.

The exact observer is O4=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P), T_P=E_P[stopping time], T_Q=E_Q[stopping time]. Time values are 1,2,3.

## 2. General all-real Bellman–Jensen identity

Fix a REAL k>0 and REAL u,v; use the unrestricted signed direction n=(-1,-k,-u,-v), so c(r)=u*r+v is the local Q-scaled cost PER time unit. The optimal scalarized free declaration at likelihood ratio r is C_k(r)=-min(r,k). Put

A_h(k)=sum_j K_h(j) C_k(r_j)-C_k(1);
B_j(k)=sum_s M_j(s) C_k(s)-C_k(r_j).

The time-2 STOP value is C_k(r_j)-2c(r_j); CONTINUE value is C_k(r_j)+B_j(k)-3c(r_j). Thus optimal stage-2 value is

V_j=C_k(r_j)-2c(r_j)+(B_j(k)-c(r_j))_+.

Define the exact first-gate continuation advantage

G_h=A_h(k)-c(1)+sum_j K_h(j) (B_j(k)-c(r_j))_+.

Because the second-stage kernel is independent of hidden source, every time-2 and terminal choice for any direction can be optimized as a function of observed keys alone. FULL can optimize time-1 STOP/CONTINUE for each source; seedless LR must pool the source advantage at time 1. Consequently for the entire real-policy class,

h_FULL(n)=C_k(1)-c(1)+sum_h w_h (G_h)_+;

h_LR(n)=C_k(1)-c(1)+(sum_h w_h G_h)_+;

Delta(n)=sum_h w_h (G_h)_+-(sum_h w_h G_h)_+ >=0.

This is an exact, source-dependent first-kernel formula, INCLUDING arbitrarily strong second-gate continuation. It is not restricted to nonnegative u,v, because support normals of the full four-dimensional observable set have arbitrary signed time coefficients.

Proof: Bellman optimization at time 2 yields V_j as above. For each source, the time-1 STOP scalar value is C_k(1)-c(1), and CONTINUE scalar value is C_k(1)-c(1)+G_h (since sum_j K_h(j)r_j=1 and sum_j K_h(j)=1). FULL separately takes positive parts and averages; seedless LR optimizes the pooled source advantage. Terminal labels and time-2 actions selected in the Bellman recursion depend only on current likelihood ratio, as M_j is source-independent. Finite behavioral randomization cannot improve a linear directional payoff over deterministic local actions. QED.

## 3. Weak second gate (old normal, expanded scope stated exactly)

For n0=(-1,-1,-5/32,0), k=1, c(r)=5r/32, the exact quantities are A_A=1/8, A_B=3/16, and B=(epsilon/12,epsilon/4,epsilon/12). Every time-2 gate is optimally STOP for 0<epsilon<=5/8 because B_j<=c(r_j). Hence G_A=-1/32, G_B=1/32 and

h_FULL(n0)=-73/64; h_LR(n0)=-37/32; Delta(n0)=1/64.

This portion is the already published result reused at its exact scope; its new role here is to cover the first interval of the combined parameter classification.

## 4. Strong-gate normal and exact full-interval theorem

Use the NEW normal n1=(-1,-1/2,-3/4,+5/8); equivalently k=1/2, u=3/4, v=-5/8. Then c(1/2)=-1/4, c(1)=1/8, c(3/2)=1/2. The exact terminal Bayes gains are

B=(11epsilon/60,epsilon/20,epsilon/60).

For ALL real 0<epsilon<=1, the low-ratio second gate strictly CONTINUES because B_low-c(1/2)>0, whereas the middle and high gates STOP because B_mid<1/8 and B_high<1/2. The second-gate action has therefore NOT been suppressed. Since C_{1/2}(r)=-1/2 on all r in R, A_A=A_B=0. The exact source continuation advantages reduce to

G_A=-1/16+11epsilon/240 < 0 for 0<epsilon<=1;

G_B=-1/32+11epsilon/160, which is >0 iff epsilon>5/11.

Their mean switches sign at epsilon=9/11. Thus for 5/11<epsilon<=1,

Delta(n1)=
  -1/64+11epsilon/320                 if 5/11<epsilon<=9/11;
   1/32-11epsilon/480                if 9/11<=epsilon<=1.

The formulas agree at 9/11, where Delta=1/80. On the range 5/8<epsilon<=1, the strong-gate gap is at least 3/512>0. Together with n0 on 0<epsilon<=5/8, this proves

**THEOREM (entire positive epsilon family). For every real epsilon in (0,1], the strictly positive two-source, two-gate model above has conv O4(FULL) != conv O4(seedless LR).**

This is a fully specified continuum result, not a finite grid statement. The separating normal may depend on the interval, but has only the two explicit values n0 and n1. The proof uses only rational symbolic identities and positivity.

## 5. Exact witness and distance, including maximal strong experiment

For every epsilon>5/11, an n1-maximizing FULL policy is: source A STOP/P at time 1; source B CONTINUE at time 1; at time 2 continue at r=1/2 and STOP/P at r=1 and 3/2; at time 3 declare Q at s=1/4 and P at all other s. Its actual observation is

W_epsilon=(11epsilon/320, 1-11epsilon/80, 51/32, 27/16).

The corresponding scalar value is h_FULL(n1). With ||n1||_1=23/8, duality gives the exact lower bound

dist_infinity(W_epsilon,conv O4(LR)) >= (8/23)*Delta(n1).

At epsilon=1, all terminal kernels are strictly positive and maximally mixed by V_j, and explicitly

W_1=(11/320,69/80,51/32,27/16);
h_FULL(n1)=-97/160;
h_LR(n1)=-59/96;
Delta(n1)=1/120;
dist_infinity >=1/345.

The weak-gate earlier witness covers 0<epsilon<=5/8 with Delta=1/64 and distance >=1/138. Hence the whole epsilon family has a strictly positive separating certificate, and a conservative interval-uniform distance lower bound 3/1472 by choosing the relevant witness.

## 6. Exact verification and source discipline

VERIFY.py uses only Python Fraction and itertools. It checks strict positive Q/P kernels, normalization, their likelihood-ratio first moments, the analytic advantages and hinge formulas, the explicit strong-gate witnesses, and independently enumerates 2,592 deterministic seedless LR policies for each of 6 rational parameter/normal checks. Actual output is in EXACT_OUTPUT.txt and ends PASS_EXACT_R5_STRONG_GATE_FULL_EPSILON_OBSTRUCTION. Finite enumeration corroborates individual rational models; it is NOT the basis of the continuum proof.

BRC semantics used: hidden-source identity and positive path mass; likelihood-ratio change of measure P=rQ; STOP/CONTINUE branch identity and observable (t,r); quotient information loss measured by the exact Jensen positive-part gap. This scoped statistical model neither revises P000/X6 native ontology nor claims a physical realization.

Earlier scientific context: the source-dependent-first-kernel predecessor at 90d8896c72f9dc67f065d6fa07eba24607510331. General prior-art reference points: D. Blackwell, "Equivalent Comparisons of Experiments", Ann. Math. Stat. 24(2) (1953), DOI 10.1214/aoms/1177729032; R. Laroche and R. Tachet Des Combes, "On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs", PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html. The exact model and formula above are an author-side derivation, not a claim of novelty for the general Blackwell/occupancy framework.

## 7. Next discriminating unit

This complete epsilon-interval exclusion closes only the current *specific family*, not R5. The next search should vary the source-dependent terminal kernels M_{h,j} or add a coupling/merger topology in which the Bellman stage-2 advantage itself remains history-specific, because the source-independent M_j assumption made exact first-gate Jensen pooling possible. Establish exact four-dimensional hull equality (vertex/dual rational certificates) before testing real-policy nonmembership. Verify current Owner/claim authority before any formal R5 control update. No theorem admission or independent review is asserted.
