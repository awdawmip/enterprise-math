# N=14 auxiliary iid sequential testing: exact 56th affine interval

Date: 2026-10-23. **AUTHOR-LEVEL exact finite-model proof; NOT independent Driver review, native CLAIM/Result freeze, Lean formalization, or native BRC/X6/Heartbeat theorem.**

## Model and inherited source

Three-symbol iid laws \(P=(1/8,1/24,5/6)\), \(Q=(1/12,1/12,5/6)\), horizon \(N=14\). Allow all history-adaptive randomized stopping and decisions. Define \(e_P=P(\mathrm{decide}\ Q)\), \(e_Q=Q(\mathrm{decide}\ P)\), and \(t_P,t_Q\) as expected samples. The objective is \(V_{14}(\alpha)=\inf_{e_P,e_Q\le\alpha}\max(t_P,t_Q)\).

The inherited *author-verified, not Driver-accepted* 55th endpoint and randomized stopping-tree are in \`research_notes/2026-10-23_N14_auxiliary_iid_55th_exact_affine_AUTHOR_UNREVIEWED.md\` and its portable checker, initially read at Source main \`6829874ccdd80f8dfc2bcb77dae2612fe346786b\`. At that endpoint:
\[
\alpha_{55}=\frac{1292956447084044215}{3725075438477770752},\quad
V_{55}=\frac{24752806046065630757}{1862537719238885376},\quad
s_{55}=\frac{6623137289528539}{10444800000000000}.
\]
Here \(s\) denotes the probability of immediate Q at \(B=(12,0,1)\). Previously selected deterministic actions are inherited exactly from the 55th portable checker, with \(A_{55}=(12,7,2)\) now fixed at immediate P.

## Exact theorem

Set \(K_{56}=1211436/91\), \(\lambda_Q=K_{56}\), \(\lambda_P=72+(8/9)K_{56}\), \(\Gamma_{56}=\lambda_P+\lambda_Q=2294820/91\) and
\[
\eta_{56}=\frac{7109375}{8420761534464}.
\]
For **every real** \(0\le\delta\le\eta_{56}\),
\[
\boxed{V_{14}(\alpha_{55}+\delta)=V_{55}-\Gamma_{56}\delta.}
\]
The right breakpoint and value are
\[
\boxed{\alpha_{56}=\frac{1292959592044044215}{3725075438477770752}},\qquad
\boxed{V_{56}=\frac{24713151556465630757}{1862537719238885376}}.
\]
This particular supporting affine line is no longer optimal strictly to the right of \(\alpha_{56}\); the value function itself does not end there.

## Dual proof (all policies, including ordered-history-dependent)

For a count-state \(x=(n,a,b)\), the likelihood ratio is \(r(x)=Q(h)/P(h)=2^{a+b}/3^a\). Backwards from \(n=14\), set
\[
D(x)=\min\{\lambda_Qr(x)\;\mathrm{[decide\ P]},\ \lambda_P\;\mathrm{[decide\ Q]},\ 1+\sum_{i=0}^2P_iD(x+i)\;\mathrm{[continue]}\},
\]
omitting continuation at the horizon. Exhaustive exact-rational evaluation of all \(\sum_{n=0}^{14}(n+1)(n+2)/2=680\) states and 1240 comparisons with nonchosen actions gives 1238 strictly positive gaps, no negative gaps and exactly two ties:
\[
(C=Q)\text{ at }A_{56}=(9,0,2),\qquad(C=Q)\text{ at }B=(12,0,1).
\]
The root value equals
\[
D(0,0,0)=\frac{87400215429346773243061}{9970054850043445248}
=V_{55}+\Gamma_{56}\alpha_{55}.
\]
The Bellman lower bound holds separately on every ordered history, hence for arbitrary history-adaptive and randomized policies:
\[
D(0,0,0)\le t_P+\lambda_Pe_P+\lambda_Qe_Q
\le\max(t_P,t_Q)+\Gamma_{56}\alpha
\quad(e_P,e_Q\le\alpha).
\]

## First arrival and explicit primal attainment

Every one of the 36 nominal ordered length-nine histories with zero symbol-0 and two symbol-1 outcomes is a first hit of \(A_{56}\); no earlier stopping intercepts them. Its exact arrival masses are
\[
p_A=\frac{78125}{4478976},\qquad q_A=\frac{78125}{1119744}.
\]
At \(B\), all 12 nominal histories are first hits, with
\[
p_B=\frac{48828125}{725594112},\qquad q_B=\frac{48828125}{362797056}.
\]
Conditional on continuing at each site, the quadruples \((e_P,e_Q,t_P,t_Q)\), measured from the site, are
\[
c_A=(98221/98304,\ 41/248832,\ 15703/12288,\ 24331/20736),
\]
\[
c_B=(63/64,\ 1/144,\ 9/8,\ 13/12).
\]
These conditional values include all inherited deterministic stopping actions and no randomization at the other site. Since \(A_{56}\) has already seen two symbol-1 outcomes while \(B\) has only one, \(B\) cannot descend from \(A_{56}\); the two first-arrival cylinders are disjoint.

At \(A_{56}\), choose immediate Q with probability \(u\in[0,1]\). At \(B\), choose immediate Q with probability \(s\). Define exact response coefficients:
\[
X=p_A(1-c_A.e_P)=6484375/440301256704,\quad
Y=q_Ac_A.e_Q=3203125/278628139008,
\]
\[
E=p_B(1-c_B.e_P)=48828125/46438023168,\quad
H=q_Bc_B.e_Q=48828125/52242776064.
\]
Then
\[
e_P-\alpha_{55}=Xu+E(s-s_{55}),\qquad
e_Q-\alpha_{55}=-Yu-H(s-s_{55}).
\]
Set \(s=s_{55}-h_{56}u\), where
\[
h_{56}=\frac{X+Y}{E+H}=\frac{35913}{2720000}.
\]
Both errors then equal \(\alpha_{55}+\eta_{56}u\), since
\[
\eta_{56}=X-Eh_{56}=Hh_{56}-Y
=\frac{7109375}{8420761534464}>0.
\]
The entire mixing segment is valid: \(0<s_{56}=s_{55}-h_{56}=6485231369528539/10444800000000000<s_{55}<1\).

Exact forward absorption, independently crosschecked by backward risk recursions and four-corner multilinearity, gives
\[
t_P(u)=V_{55}-\Gamma_{56}\eta_{56}u.
\]
The difference \(t_P-t_Q\) is affine and *strictly positive at both endpoints*:
\[
(t_P-t_Q)_{u=0}=\frac{875356767487775843}{1862537719238885376},\quad
(t_P-t_Q)_{u=1}=\frac{984596181247775843}{1862537719238885376}.
\]
Consequently \(t_P=\max(t_P,t_Q)\) throughout the entire real mixing interval. These policies attain the dual lower bound for every real \(\delta=\eta_{56}u\).

## Sharpness of the right endpoint

Finite-horizon randomized policy occupation measures form a compact polytope, so the minimum exists. Were the same supporting line achieved at \(\alpha>\alpha_{56}\), equality in the chain of inequalities above (both positive Lagrange multipliers) would imply \(e_P=e_Q=\alpha\) and actions minimizing Bellman at every positive-mass history. Every action is forced except C/Q at \(A_{56}\) and \(B\). Since no path from \(A_{56}\) can reach \(B\), arbitrary history-specific choices at either tie aggregate exactly into two first-arrival-mass-weighted probabilities \(u,s\in[0,1]\). The two error equations then force \(s=s_{55}-h_{56}u\) and \(\alpha=\alpha_{55}+\eta_{56}u\le\alpha_{56}\), a contradiction. Thus the **supporting line** is sharp.

## Exact verification, limitations, next research unit

The author-side portable checker evaluates 680 states/1240 gaps with \`fractions.Fraction\`, first arrivals and suffix risks, 5 mixtures, root dual equality and next crossing. The second author-side checker enumerates all \(3^9=19683\) nine-step ordered words and \(3^{12}=531441\) twelve-step ordered words, directly minimizes the Bellman recurrence and checks four backward-DP corners plus five mixtures. Both pass. They share the inherited historical stopping action list, so this is not an independent Research Driver review. No Lean checking or bridge to native BRC/X6/Heartbeat has occurred.

**Next exact dual crossing candidate only:** \(K_{57}=6854544972/576215\) with a continuation/immediate-P tie at \(A_{57}=(8,5,0)\) after making \(A_{56}\) immediate Q. Its real first-arrival masses, interference, balance coefficients, next breakpoint and full optimality are unproved.

Snapshot and authority: GLOBAL_KNOWLEDGE_V1 main \`9b91a061c101e778d9b4d0bc99bde7aa5083934a\`; Enterprise Math pre-publication Source main \`6829874ccdd80f8dfc2bcb77dae2612fe346786b\`. Authenticated GitHub login \`awdawmip\`. Native control tasks returned \`CONTROL_QUOTA\`, so active owner/CLAIM not verified. This is source-bound **author research**, not a frozen Result or Driver review.
