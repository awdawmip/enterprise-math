# N=14 auxiliary iid sequential testing — stage92 exact affine interval

**2026-10-25; author-side rational finite-model proof.** This is not independent Research Driver review, a native Enterprise Math CLAIM/Result, a theorem about P000/X6/Heartbeat or native BRC admission.

## Statement

Observations are iid in {0,1,2} under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). Tests may be randomized and depend on the complete ordered history, but stop at T<=14. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(T), tQ=E_Q(T), and V14(alpha)=inf max(tP,tQ) over tests with both errors <=alpha.

Use the verified **author-side** stage91 endpoint:
\[
\alpha_{91}=\frac{5172457130438856743}{14900301753911083008},\quad
V_{91}=\frac{24277747395672814529}{1862537719238885376},\quad
s_{91}=\frac{27568725422700427}{41779200000000000}.
\]
Here s denotes immediate decision Q probability at B=(12,0,1), otherwise continue. Freeze A91=(6,0,2) to immediate Q, with earlier decisions inherited from exact stage88->89->90->91 action code (stage91 source Git blob 44a5f59e16ab379a0ff29fdfd225a8f6fa592367, source commit 966d52251166b4d17ea861ea4374639669abbee9).

**Theorem.** Define
\[
\eta_{92}=\frac{104725}{103474317735493632},\qquad
\Gamma_{92}=\frac{1062252}{295}.
\]
For **every real** \(0\le\delta\le\eta_{92}\),
\[
\boxed{V_{14}(\alpha_{91}+\delta)=V_{91}-\Gamma_{92}\delta}.
\]
The new endpoint is
\[
\boxed{\alpha_{92}=\frac{5172457130453937143}{14900301753911083008}},\qquad
\boxed{V_{14}(\alpha_{92})=\frac{24277747388885024249}{1862537719238885376}}.
\]
For alpha>alpha92 the same fixed Bellman dual support line cannot be attained (right-end sharpness of this support).

## Global Bellman dual

Set lambdaQ=K92=551124/295, lambdaP=72+(8/9)K92=511128/295. Their sum is Gamma92. For count state z=(n,a,b) with a=#symbol0, b=#symbol1, the exact likelihood ratio Q/P=2^(a+b)/3^a. Under P-normalization the Bellman recursion over n<=14 is
\[
D(z)=\min\left\{\lambda_Q\frac{2^{a+b}}{3^a},\ \lambda_P,\ 1+\sum_{i=0}^2 P_i D(z+e_i)\right\},
\]
omitting continuation at n=14. The three choices are immediate P, immediate Q, continue. Exhaustive Fraction backward evaluation of **all 680** count states compares the fixed stage91 endpoint action with 1240 alternatives: 1238 strict positive gaps, zero negative gaps, and exactly two zero ties
\[
A_{92}=(12,8,3):C\sim P,\qquad B=(12,0,1):C\sim Q.
\]
The minimum strict positive gap is 125158067/6263930880. A separate minimizing recursive Bellman implementation gives
\[
D(0,0,0)=\frac{81643359052598886694907}{64641014961820139520}
=V_{91}+\Gamma_{92}\alpha_{91}.
\]
Because iid conditional suffix probabilities and Q/P depend only on count state, this Bellman minimum bounds **all** ordered-history and randomized tests, not merely count-based tests:
\[
D(0,0,0)\le t_P+\lambda_P e_P+\lambda_Q e_Q
\le \max(t_P,t_Q)+\Gamma_{92}\alpha .
\]
Thus V14(alpha)>=D(0,0,0)-Gamma92*alpha.

## Exact positive ordered branch accounting

At the new tied state A=(12,8,3), 1980 ordered symbol words have the desired counts, but **only 852 genuinely survive all earlier decisions**. Enumerating their independent P and Q path weights yields
\[
p_A=\frac{355}{115964116992},\qquad
q_A=\frac{355}{371504185344}.
\]
Under baseline continuation at A, there are exactly five ordered terminal suffixes with conditional vector (P-error, Q-error, extra P samples, extra Q samples)
\[
R_A=(1/576,\ 143/144,\ 25/24,\ 13/12).
\]
Immediate stopping at A therefore truncates 852*5=**4260** former full terminal ordered words; this count is not a probability.

At B=(12,0,1), 12 of 12 ordered words survive; the separate first-hit masses and continuation vector are
\[
p_B=\frac{48828125}{725594112},\quad
q_B=\frac{48828125}{362797056},\quad
R_B=(63/64,\ 1/144,\ 9/8,\ 13/12).
\]
B also has five terminal suffix words. A and B are **distinct states at the same depth 12**, hence their entire decision subtrees/cones are disjoint. Thus no cross term arises when randomizing them; ordered provenance and two rational probability measures are retained rather than collapsed to a single total.

## Entire real interval: primal witness

Let u in [0,1] denote immediate P probability at A and s denote immediate Q probability at B; all other actions are fixed. Define
\[
X=p_A R_A^{Perr}=\frac{355}{66795331387392},\quad
Y=q_A(1-R_A^{Qerr})=\frac{355}{53496602689536},
\]
\[
E=p_B(1-R_B^{Perr})=\frac{48828125}{46438023168},\quad
H=q_B R_B^{Qerr}=\frac{48828125}{52242776064}.
\]
Exact disjoint-cone identities for any real u,s are
\[
e_P=\alpha_{91}-Xu+E(s-s_{91}),\quad
e_Q=\alpha_{91}+Yu-H(s-s_{91}).
\]
Thus eP=eQ uniquely iff
\[
\boxed{s=s_{91}+h_{92}u},\qquad
h_{92}=\frac{X+Y}{E+H}=\frac{1047463}{174080000000000}.
\]
Substitution gives
\[
e_P=e_Q=\alpha_{91}+\eta_{92}u,\quad
\eta_{92}=-X+Eh_{92}=Y-Hh_{92}>0.
\]
At u=1,
\[
s_{92}=\frac{27568725674091547}{41779200000000000},
\]
so 0<s91<s92<1 and every real u in [0,1] is admissible. Both sampling expectations are affine in u due to disjointness. Their exact difference at the endpoints is
\[
(t_P-t_Q)_{u=0}=\frac{2330264683137429905}{3725075438477770752}>0,\quad
(t_P-t_Q)_{u=1}=\frac{2330264676686154065}{3725075438477770752}>0.
\]
Consequently max(tP,tQ)=tP on the **whole real** parameter interval. Every reached action is Bellman-minimizing, so
\[
t_P+\lambda_Pe_P+\lambda_Qe_Q=D(0,0,0).
\]
The primal witness therefore attains the dual bound at all real alpha=alpha91+eta92*u and proves the theorem without extrapolating from a finite parameter grid.

## Right-end sharpness

Randomized finite-horizon decision rules define a compact finite-dimensional occupation-measure polytope, so the infimum is attained. Equality on the same dual line for some alpha>alpha92 would force, since both multipliers are positive, eP=eQ=alpha and every reached action to minimize this exact Bellman recursion. Strict positive gaps exclude all deviations except at A and B. At each count state, Q/P is constant across its ordered prefixes and future iid laws are identical; history-dependent randomization can therefore be aggregated to effective u,s in [0,1] preserving both errors and expectations. Error equality forces s=s91+h92*u, whence alpha=alpha91+eta92*u<=alpha92, a contradiction.

## Methods, provenance and next candidate

The package contains exact Python standard-library Fraction scripts for (i) full 680-state rational Bellman and forward path calculation and (ii) ordered-prefix/terminal-suffix DFS plus a separately implemented minimizing recursion. Both inherit the same stage88->91 deterministic policy; they constitute **author-side reproducibility**, not clean independent mathematical review. This is an **external finite iid auxiliary model**. A faithful native BRC/X6, three-dimensional slice and Heartbeat transfer is not proved. Positive rational path weights and ordered multiplicity instantiate a typed BRC-style positive-weighted carrier; no signed cancellation is claimed.

The **next unproved candidate** is K93=36260219477628/21860934947 with possible C-versus-P tie at A93=(5,4,0). Its first-hit geometry, error compensation and feasibility require fresh proof.

Input pins: GLOBAL_KNOWLEDGE_V1 main@50e22254dac1b15435eed58a6ad87a3e9b8627f0; EM source read main@0c20646ad4d9fa5345dcdbc28c35fdf52a2bc5d7; verified stage91 source 966d52251166b4d17ea861ea4374639669abbee9. Native control: CONTROL_QUOTA; native session start: STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No live owner, CLAIM, native Result or Driver acceptance was verified.
