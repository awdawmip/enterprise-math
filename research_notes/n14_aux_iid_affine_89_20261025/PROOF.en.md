# N=14 auxiliary iid sequential testing — Stage 89 exact affine support

Date: 2026-10-25. Classification: AUTHOR-SIDE EXACT FINITE-MODEL PROOF, with locally executed exact rational programs. This is not a native Enterprise Math Result, independent Driver review, formal CLAIM, native BRC/X6/Heartbeat transfer, or P000 verification. Both author checkers inherit the previous verified deterministic stopping-action map.

## 1. Model and exact theorem

Under the hypotheses \(P=(1/8,1/24,5/6)\), \(Q=(1/12,1/12,5/6)\), consider all randomized, ordered-history stopping and terminal-decision rules of horizon \(N=14\). Write \(e_P=P(\mathrm{decide}\ Q)\), \(e_Q=Q(\mathrm{decide}\ P)\), and \(t_P=E_PT,t_Q=E_QT\). Let
\[
V_{14}(\alpha)=\inf\{\max(t_P,t_Q):e_P\le\alpha,\ e_Q\le\alpha\}.
\]
Stage 88 supplies the exact primal boundary
\[
\alpha_{88}=\frac{5172392070782909543}{14900301753911083008},
\quad
V_{88}=\frac{24307502422996613729}{1862537719238885376},
\quad
s_{88}=\frac{29743974300660427}{41779200000000000}.
\]
Here \(s_{88}\) is the probability of immediately deciding Q at balancing count state \(B=(12,0,1)\). Stage 88 fixes deterministic P at its previous tie \(A_{88}=(6,4,0)\). All other previously selected stopping actions are inherited as a fixed finite table from the immutable source \`a08b0e41d583dabefe00b8116c89d97b4d0bdf65\`; the executable map and the new proof are provided beside this file.

**Theorem (entire real segment).** For every real \(0\le\delta\le\eta_{89}\), where
\[
\eta_{89}=\frac{623875}{12934289716936704},
\]
one has
\[
\boxed{V_{14}(\alpha_{88}+\delta)=V_{88}-\frac{808776}{217}\delta}.
\]
In particular
\[
\alpha_{89}=\frac{5172392071501613543}{14900301753911083008},
\qquad
V_{14}(\alpha_{89})=
\frac{24307502088163349729}{1862537719238885376}.
\]
The affine support line is right-sharp: for every feasible \(\alpha>\alpha_{89}\), it lies strictly below \(V_{14}(\alpha)\).

## 2. Global Bellman dual lower bound (all history policies)

Let \(a\) and \(b\) be counts of symbols 0 and 1 in a prefix of length \(n\). The likelihood ratio is \(Q/P=2^{a+b}/3^a\). At \(K=\lambda_Q=419904/217\) fix
\[
\lambda_P=72+\frac89K=\frac{388872}{217},
\qquad \Gamma=\lambda_P+\lambda_Q=\frac{808776}{217}>0.
\]
For each count state \(h=(n,a,b)\) and \(n\le14\) set the exact P-normalized terminal costs \(D_P(h)=\lambda_Q 2^{a+b}/3^a\), \(D_Q(h)=\lambda_P\). If \(n<14\), set \(D_C(h)=1+\sum_{i=0}^2 P_i D(h+i)\), with \(h+i\) the count update. Then recursively set \(D(h)=\min(D_P,D_Q,D_C)\), omitting continue at \(n=14\).

An exact rational backward pass over all \(\sum_{n=0}^{14}(n+1)(n+2)/2=680\) states shows:
- Of 1240 comparisons between the inherited selected action and an unselected action, 1238 gaps are strictly positive, zero negative, exactly two gaps zero.
- The *only* ties are continue versus immediate Q at \(A=(11,5,4)\) and \(B=(12,0,1)\). The smallest positive gap is \(819780607/41469345792\).
- The independently minimized root agrees with the selected recursion:
\[
D_0=\frac{3883735655924485817999}{2971843272609103872}
=V_{88}+\Gamma\alpha_{88}.
\]

Conditionally at each ordered prefix, the future suffix probability law and \(\ell=Q/P\) depend only on \(h\); thus this count-state Bellman dual lower bound is valid for every history-dependent randomized policy, even if its action differs across distinct prefixes with the same count triple:
\[
D_0\le t_P+\lambda_P e_P+\lambda_Q e_Q
\le\max(t_P,t_Q)+\Gamma\alpha.
\]
Consequently \(V_{14}(\alpha)\ge D_0-\Gamma\alpha\) globally.

## 3. Independent ordered-word audit and disjoint cones

There are \(\binom{11}{5,4,2}=6930\) nominal length-11 words with state \(A\). After respecting every inherited earlier terminal decision, only **2760** are actual first-hit prefixes. Their separate positive measures are
\[
p_A=\frac{2875}{16307453952},\qquad
q_A=\frac{2875}{7739670528}.
\]
Under the inherited continuation suffix policy the conditional (P error, Q error, P remaining time, Q remaining time) vector is
\[
R_A=(511/512,\;1/1728,\;73/64,\;157/144).
\]
There are precisely seven terminal ordered suffix words/classes from A. Immediate stopping at A truncates **19320** formerly complete histories (2760 times 7).

For B, all twelve nominal prefixes are first-hit, with
\[
p_B=\frac{48828125}{725594112},\qquad
q_B=\frac{48828125}{362797056},\qquad
R_B=(63/64,\;1/144,\;9/8,\;13/12).
\]
There are five terminal suffix words, accounting for 60 full histories. Counts and P/Q masses are separate data, not interchangeable. The independent DFS verifier explicitly enumerates each terminal suffix and records first-hit paths, rather than using only nominal multinomial counts.

A has five observed zeros at depth 11, whereas B has zero zeros at depth 12. Monotonicity of counts precludes a path reaching A before B; B cannot reach the shallower A. Thus their *ordered decision cones* are disjoint. Mixed \(us\) perturbation terms vanish exactly.

## 4. Continuum primal certificate

Let \(u\in[0,1]\) be the probability of immediate Q at A and \(s\in[0,1]\) that of immediate Q at B. With the stage88 baseline \((u,s)=(0,s_{88})\), define the exact positive coefficients
\[
X=p_A(1-R_A^{P,\mathrm{err}})=\frac{2875}{8349416423424},\qquad
Y=q_AR_A^{Q,\mathrm{err}}=\frac{2875}{13374150672384},
\]
\[
E=p_B(1-R_B^{P,\mathrm{err}})=\frac{48828125}{46438023168},\qquad
H=q_BR_B^{Q,\mathrm{err}}=\frac{48828125}{52242776064}.
\]
Because of the disjoint cones, these are *identities for real probabilities*, not endpoint interpolations:
\[
e_P-\alpha_{88}=Xu+E(s-s_{88}),\qquad
e_Q-\alpha_{88}=-Yu-H(s-s_{88}).
\]
Enforcing equal errors gives
\[
s=s_{88}+h_{89}u,\qquad
h_{89}=-\frac{X+Y}{E+H}=-\frac{245111}{870400000000},
\]
and
\[
e_P=e_Q=\alpha_{88}+\eta_{89}u,\qquad
\eta_{89}=X+Eh_{89}=-Y-Hh_{89}
=\frac{623875}{12934289716936704}.
\]
At the right endpoint
\[
s_{89}=s_{88}+h_{89}=\frac{29743962535332427}{41779200000000000};
\]
hence \(0<s_{89}<s_{88}<1\), proving probability feasibility for every real \(u\in[0,1]\).

The exact difference \(t_P-t_Q\) is affine (again by disjoint cones). At \(u=0,1\) its values are respectively
\[
\frac{2166716868242604305}{3725075438477770752}>0,\qquad
\frac{2166717554273724305}{3725075438477770752}>0.
\]
It follows \(t_P>t_Q\) everywhere on the entire segment. Every selected action on a positive-mass path is a minimizer of the fixed dual Bellman recursion (including the two permitted ties); therefore
\[
t_P+\lambda_Pe_P+\lambda_Qe_Q=D_0.
\]
Since \(e_P=e_Q=\alpha_{88}+\eta_{89}u\), this yields
\[
\max(t_P,t_Q)=t_P=D_0-\Gamma(\alpha_{88}+\eta_{89}u).
\]
Combined with the global lower bound, this proves optimality at *every real* \(\delta=\eta_{89}u\), and substitution \(u=1\) gives the exact stage89 endpoint and value.

## 5. Right-endpoint sharpness

Assume some \(\alpha>\alpha_{89}\) attained the same affine support lower bound. The finite-horizon randomized ordered-history strategy set is a compact finite-dimensional polytope (occupation-measure or behavioral-strategy formulation); its optimum is attained. Both dual multipliers are strictly positive, so equality forces \(e_P=e_Q=\alpha\) and every reached action to be dual-Bellman minimizing. The exact strictly positive-gap certificate leaves randomization only at A and B. Across different prefixes with the same count triple, likelihood ratios agree, and the frozen continuation suffix statistics agree, so averaging their stopping probabilities with the common proportional P/Q reach weights preserves all aggregate risks. Thus every equality-attaining policy admits an equivalent aggregate pair \((u,s)\in[0,1]^2\). The exact errors above force \(s=s_{88}+h_{89}u\) and therefore \(\alpha=\alpha_{88}+\eta_{89}u\le\alpha_{89}\), a contradiction. The affine support is right-sharp.

## 6. Reproducibility, scope and next frontier

Run \`python derive89.py\` and \`python crosscheck89.py\` in the same directory, using Python standard-library \`fractions.Fraction\` only. The second checker independently enumerates ordered first-hit and terminal suffix words and recomputes true Bellman minima. It nevertheless shares the predecessor frozen action table, so it does **not** constitute a clean independent Research Driver review. A local expanded proof, detailed outputs and complete SHA-256 source inventory are in the user-delivered zip (SHA256 \`f069340502216ed233cf9845ffd8edac3bb24345071163730be0b67e9902a3c2\`). The two published Python programs are byte-identical to locally executed code (expected Git blobs \`7bf9ea6232ec15330593cfa9ef424a3f43b8ffe1\` and \`15f179646539bd026f36e08e5dbf06cb2f3fa6a4\`).

This is an **auxiliary iid** statistical decision model, not an established conservative native X6/P000 or Heartbeat map; preserving ordered histories and separate positive measures is essential. No formal Research Driver, Source-issued CLAIM, native Result or acceptance is asserted. Real owner identity remains unverified because native \`em_control_tasks\` responded \`CONTROL_QUOTA\` and \`em_session_start\` responded \`STATIC_READONLY_SCOPE_DENIED\`, with \`operation_sent=false\`. Current work is a source-provenanced author-side study and lightweight local research activity only.

**Next unproved directional candidate:** \(K_{90}=3166224876/1665893\) and \(A_{90}=(7,2,3)\), continue versus immediate Q. Neither the stage90 segment nor its right-sharpness has been proved. See \`NEXT_TASK_PACKET_90.md\`.

Read pins: GLOBAL_KNOWLEDGE_V1 \`awdawmip/chatgpt-global-knowledge@3281f16647ce1fd82b58cad5939d6a0c165aa771\`, EM project read \`awdawmip/enterprise-math@8bbf3f61e50802adf85299f7ddd9e666a1c12a6e\` before this stage registration; immutable mathematical predecessor source \`a08b0e41d583dabefe00b8116c89d97b4d0bdf65\`.
