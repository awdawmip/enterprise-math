# Auxiliary iid N=14 sequential testing — Stage 93 exact affine segment

**Date:** 2026-10-25. **Evidence status:** author-level exact rational finite-model proof, not independent Research Driver acceptance, native Task CLAIM, frozen Result, or native BRC/X6/Heartbeat transfer.

## Theorem and inherited input

Take iid observations on {0,1,2} under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), with any randomized, *ordered-history-dependent* stopping rule of horizon T<=14. Define e_P=P(decide Q), e_Q=Q(decide P), t_P=E_P[T], t_Q=E_Q[T], and V14(alpha)=inf_{e_P,e_Q<=alpha} max(t_P,t_Q).

The author-side Stage92 endpoint is

- alpha92 = 5172457130453937143/14900301753911083008;
- V92 = 24277747388885024249/1862537719238885376;
- s92 = 27568725674091547/41779200000000000, the immediate-Q probability at B=(12,0,1).

Freeze the Stage92 tie A92=(12,8,3) to immediate P, Stage91 A91=(6,0,2) to immediate Q and the other inherited endpoint decisions. The action chain is the unchanged source in derive88.py -> ... -> derive92.py; Stage93 imports derive92.py.

**Theorem (every real delta in the specified closed interval):**

\[
0\le\delta\le \eta_{93}:=\frac{546523373675}{1241691812825923584}
\quad\Longrightarrow\quad
\boxed{V_{14}(\alpha_{92}+\delta)=V_{92}-\frac{70065512996148}{21860934947}\delta.}
\]

Thus

\[
\boxed{\alpha_{93}=\frac{5172463688734421243}{14900301753911083008}},\qquad
\boxed{V_{14}(\alpha_{93})=\frac{24275119932147668699}{1862537719238885376}}.
\]

The same fixed Bellman supporting line is unattainable for any alpha>alpha93. No Stage94 primal theorem is asserted.

## 1. Universal Bellman support

Set K=36260219477628/21860934947, lambda_Q=K and lambda_P=72+(8/9)K=33805293518520/21860934947. Their sum is Gamma93=70065512996148/21860934947, both strictly positive.

At count state (n,a,b), where a=#symbol-0 and b=#symbol-1, the exact Q/P likelihood ratio of *every* ordered history reaching the state equals 2^(a+b)/3^a. The P-normalized finite backward Bellman equation, without the third option at n=14, is

\[
D(n,a,b)=\min\{\lambda_Q2^{a+b}/3^a,\ \lambda_P,\ 1+\sum_i P_i D(\operatorname{child}_i(n,a,b))\}.
\]

The terms correspond to decide P, decide Q, continue. Exact rational examination of all binom(17,3)=680 states and 1240 comparisons against nonchosen actions gives 1238 strictly positive gaps, zero negative gaps, and exactly two ties:

- A93=(5,4,0): continue versus decide P;
- B=(12,0,1): continue versus decide Q.

The smallest positive gap is 175345197055/113327086765248. An independently programmed minimum Bellman recursion (as opposed to inherited action evaluation) checks

\[
D(0,0,0)=\frac{5392010828624465307872059490641}{4790213637248826300885368832}
=V_{92}+\Gamma_{93}\alpha_{92}.
\]

Conditionally iid suffix laws and the constant likelihood ratio on each count state make this dual valid for all *ordered-history* policies. For any test with errors <=alpha,

\[
D(0,0,0)\le t_P+\lambda_P e_P+\lambda_Q e_Q
\le \max(t_P,t_Q)+\Gamma_{93}\alpha,
\]

so V14(alpha)>=D(0,0,0)-Gamma93*alpha.

## 2. Exact first-hit branch carrier and disjoint cones

Let A=A93. There are 5 nominal count-compatible ordered prefixes, and all 5 genuinely arrive before earlier stopping. Direct ordered-word enumeration produces first-hit masses

\[
p_A=25/24576,\qquad q_A=25/124416.
\]

The **old continuation** from A has 1827 ordered terminal suffix words (46 terminal decision/state classes). Early stopping there deletes 5*1827=9135 complete ordered terminal histories, counted separately from P/Q weights. Its exact continuation vector (P-error, Q-error, P expected further observations, Q expected further observations) is

\[
R_A=(3621975349/2641807540224,\ 
5106598015/5159780352,\
138353084149/110075314176,\
24822259/15925248).
\]

For B, all 12 nominal first-hit prefixes survive. Its masses and continuation vector are

\[
p_B=48828125/725594112,\quad
q_B=48828125/362797056,\quad
R_B=(63/64,1/144,9/8,13/12).
\]

Its terminal suffix count is 5. A's count a=4 is already positive, while B requires a=0 at depth 12. Because the count of zero symbols never decreases, **no complete history passing A can later pass B**, so the A- and B-randomization cones are disjoint.

The exact branch operator uses the positive rational weighted BRC substrate with ordered provenance and multiplicity kept apart from mere Boolean support or aggregate risk. This is typed **auxiliary** BRC-style reuse; no signed amplitude or native spatial model is being computed.

## 3. Continuous exact primal construction

Let u in [0,1] be the chance of immediate P at A and s in [0,1] that of immediate Q at B. At baseline u=0,s=s92, both error rates equal alpha92. Put

\[
X=p_AR_A^{Perr}=90549383725/64925062108545024,\quad
Y=q_A(1-R_A^{Qerr})=1329558425/641959232274432,
\]
\[
E=p_B(1-R_B^{Perr})=48828125/46438023168,\quad
H=q_BR_B^{Qerr}=48828125/52242776064.
\]

Cone disjointness yields **exact affine identities**, for all real legal u,s:

\[
e_P=\alpha_{92}-Xu+E(s-s_{92}),\qquad
e_Q=\alpha_{92}+Yu-H(s-s_{92}).
\]

Therefore e_P=e_Q is equivalent to

\[
s=s_{92}+h_{93}u,\qquad h_{93}=\frac{X+Y}{E+H}
=\frac{729049707973}{417792000000000}.
\]

Their common error then equals alpha92+eta93*u, where

\[
\eta_{93}=-X+Eh_{93}=Y-Hh_{93}
=\frac{546523373675}{1241691812825923584}>0.
\]

At u=1, s93=27641630644888847/41779200000000000, and 0<s92<s93<1, so every real u in [0,1] produces an admissible test. The P-time decrement per unit u is

\[
p_AR_A^{Ptime}+p_BR_B^{Ptime}h_{93}
=48656606247325/34491439245164544
=\Gamma_{93}\eta_{93}.
\]

Sampling times are affine in u. Exact forward propagation at u=0 and u=1 respectively gives

\[
(t_P-t_Q)_{u=0}=2330264676686154065/3725075438477770752>0
\]

and

\[
(t_P-t_Q)_{u=1}=775708071240140755/1241691812825923584>0.
\]

Thus t_P>t_Q for every real u in [0,1]. Every actually reached action at this policy is a Bellman minimizer, so

\[
t_P+\lambda_Pe_P+\lambda_Qe_Q=D(0,0,0).
\]

Combining primal equality with the universal dual lower bound yields the asserted V14 segment for the entire continuum, not merely a finite sampling grid.

## 4. Right-end sharpness for arbitrary ordered-history randomization

At horizon 14, randomized finite-history policies induce a compact finite occupation-measure polytope; the optimum is attained. Suppose an alpha>alpha93 attained the *same* Bellman line. Both positive multipliers force e_P=e_Q=alpha, and dual equality forces Bellman-minimizing decisions at all reached histories. Strict positivity of all other gaps leaves randomization only at A and B.

Although different ordered words hitting A or B could have different randomization probabilities, **they can be P-weighted aggregated** to common u,s: Q/P is constant on that count state and every possible future suffix has the same conditional law. By proved disjointness, no other cross-term appears; first-hit probabilities are not altered by those actions. Equal errors hence require s=s92+h93*u, and alpha=alpha92+eta93*u<=alpha93, contradicting alpha>alpha93. Therefore the fixed stage93 line is sharp at the right endpoint. This does not prove any next segment.

## 5. Verified Stage94 dual candidate and scope

Freeze A93 to immediate P; the new endpoint action table has all Bellman gaps nonnegative at both K93 and K94=7010064/4231. At K94 the only ties are B (C/Q) and A94=(10,5,1) (C/P), with 1238 strictly positive gaps. At K94-1/10000 the A94 nonselected gap is negative. All these gaps are affine in K, so the frozen-A93 table is optimal for every K in [K94,K93]; **this is a next dual candidate only**.

Two local author-side standard-library Fraction programs passed: one computes action-value Bellman DP and weighted first-hit recurrences; the other enumerates all ordered first-hit/suffix words and independently computes the minimum Bellman root. Both share the earlier deterministic policy table, hence neither is a clean independent Driver review. Source/risk values and executable checks are in certificate93.json, derive93.py and crosscheck93.py. The local research package additionally includes all ancestor code and expanded proof.

**Scientific boundary:** this is an external finite iid auxiliary model. P000 is retained without change; no faithful embedding or three-dimensional-slice third-coordinate semantics, native BRC/X6/Heartbeat preservation, or physics claim is established. No native CLAIM/owner/Result has been confirmed: the control inventory returned CONTROL_QUOTA; the native session start was denied with STATIC_READONLY_SCOPE_DENIED and operation_sent=false.

**Source pins:** GLOBAL_KNOWLEDGE_V1 main@e374f213cc834049f52f37127a035539ae14ff4d, Enterprise Math main@ae0349007a8667277d705a6d9007f65840b3ebac at input read; stage92 source Git blob a18f86e6e327f4004d952ac663ff1a88a49ad6f2; weighted BRC substrate blob f375a059fa4af8c6eefaddb4d4a8689a0c063674. All claims are author-side at these frozen inputs.
