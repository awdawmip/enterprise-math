# N=14 auxiliary iid sequential test: exact 52nd affine interval

**Author-side exact finite-model proof, 2026-10-23; NOT independently Driver-reviewed, Lean-formalized, or a theorem about native BRC/X6/Heartbeat.** There is no formal CLAIM or Result freeze.

## Model and inherited 51st endpoint

The symbols 0,1,2 are iid under P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), with horizon N=14. An arbitrary ordered-history-dependent randomized stopping policy has errors eP=P(decide Q), eQ=Q(decide P), and expected sample counts tP,tQ. Define V14(alpha)=inf max(tP,tQ), subject to eP,eQ<=alpha.

We inherit the author-checked 51st right endpoint

$$
\alpha_{51}=5171825736480880397/14900301753911083008,\quad
V_{51}=12376505799748489069/931268859619442688,\quad
s_{51}=26493368445399769/41779200000000000.
$$

Here s51 is the probability of immediately deciding Q at B=(12,0,1). The fixed stop actions are completely specified by the SP/SQ and threshold rules in the attached standalone checker, inherited from the preceding 51st proof (source: awdawmip/enterprise-math@7af2e720b372b6aa2b0b79f99489546c3fe00179, research_notes/2026-10-23_N14_auxiliary_iid_51st_exact_affine_AUTHOR_UNREVIEWED.md). The 51st right-endpoint policy has already switched A51=(10,4,4) to unconditional immediate Q.

## Theorem

Let

$$
K_{52}=280418092213968/16640988557,\quad
\Gamma_{52}=530876769802488/16640988557,\quad
\eta_{52}=16640988557/4966767251303694336.
$$

For **every real** 0<=delta<=eta52, the unrestricted global finite-model value obeys

$$
\boxed{V_{14}(\alpha_{51}+\delta)=V_{51}-\Gamma_{52}\delta}.
$$

The new exact breakpoint and value are

$$
\boxed{\alpha_{52}=1292956446600961517/3725075438477770752},\quad
\boxed{V_{52}=24752812520708302205/1862537719238885376}.
$$

The same Bellman supporting line **cannot** remain equal to V14(alpha) at any alpha>alpha52. No claim is made that V14 itself terminates.

## Global Bellman certificate

For state x=(n,a,b), with counts a of symbol 0 and b of symbol 1 among n observations, Q(history)/P(history)=r(x)=2^(a+b)/3^a. Put lambdaQ=K52 and lambdaP=72+8*K52/9=250458677588520/16640988557, so lambdaP+lambdaQ=Gamma52. On each of 680 finite count states recursively compute using exact rational arithmetic

$$
D(x)=\min\{\lambda_Q r(x)\ (\mathrm{decide\ P}),\ \lambda_P\ (\mathrm{decide\ Q}),\
1+\sum_{i=0}^2 P_i D(x+i)\ (\mathrm{continue})\},
$$

omitting continue at n=14. Every prescribed action is optimal. Among 1240 comparisons against other actions, 1238 have strictly positive slack and exactly two have zero slack: continue/Q at A52=(3,0,3) and continue/Q at B=(12,0,1). There are no negative slacks. The root identity is exact:

$$
D(0,0,0)=20212481306077731227154928958549/1823204051343245311261802496
         =V_{51}+\Gamma_{52}\alpha_{51}.
$$

Conditional minimization over successive observations holds for **every** ordered-history randomized policy (not only Markov/count policies):

$$
D(root)\leq t_P+\lambda_P e_P+\lambda_Q e_Q
          \leq\max(t_P,t_Q)+\Gamma_{52}\alpha.
$$

Thus V14(alpha)>=V51+Gamma52*(alpha51-alpha) globally.

## First-stop reach and nested old state

A52=(3,0,3) has precisely one surviving ordered prefix, the word 111 (three symbol-1 outcomes). Its unconditional first-hit masses are pA=1/13824 and qA=1/1728. B has 12 first-hit words, with pB=48828125/725594112 and qB=48828125/362797056.

Conditional on continuing, using the fixed 51st right-endpoint stop tree, the quadruples (eP,eQ,tP,tQ) are

$$
c_A=(695505717377/695784701952,\ 24976691/743008370688,\
392193889717/260919263232,\ 79410763063/61917364224),
$$

$$
c_B=(63/64,\ 1/144,\ 9/8,\ 13/12).
$$

**Nested-state nuance:** A52 is earlier than A51. Of 3150 nominal histories leading to A51, 1565 are genuine first-hit histories in the 51st tree, and **16 of those pass through A52 first**. Switching at A52 preempts these descendants. We recompute cA under the *already deterministic-Q* action at A51. It would be incorrect to treat A51 as a third independent randomization cylinder or reuse its unadjusted reach. In contrast, A52 and B are disjoint cylinders: the former contains 3 ones, the latter only 1, and counts cannot decrease.

## Primal construction and attainment

At A52 stop and decide Q with probability u in [0,1], and at B stop and decide Q with probability s; retain all other actions. Because A52 and B cylinders are disjoint, no interaction term appears. Define the exact positive increments

$$
X=p_A(1-c_A.eP)=278984575/9618527719784448,\quad
Y=q_A c_A.eQ=24976691/1283918464548864,
$$

$$
E=p_B(1-c_B.eP)=48828125/46438023168,\quad
H=q_B c_B.eQ=48828125/52242776064.
$$

Relative to the 51st endpoint (u=0,s=s51),

$$
e_P-\alpha_{51}=Xu+E(s-s_{51}),\qquad
e_Q-\alpha_{51}=-Yu-H(s-s_{51}).
$$

Choose

$$
s=s_{51}-h_{52}u,\qquad
h_{52}=(X+Y)/(E+H)=1019357370869/41779200000000000.
$$

Then eP=eQ=alpha51+eta52*u with

$$
\eta_{52}=X-Eh_{52}=Hh_{52}-Y=16640988557/4966767251303694336>0.
$$

This is feasible throughout: 0<s51-h52<=s<=s51<1. In particular, s52=264923490880289/417792000000000. Independent exact forward and absorbing-backward computations agree that

$$
t_P(u)=V_{51}-\Gamma_{52}\eta_{52}u.
$$

Both sampling means are affine in u; their difference is positive at both endpoints:

$$
(t_P-t_Q)_{u=0}=1748365495275977401/3725075438477770752>0,
$$

$$
(t_P-t_Q)_{u=1}=291786475196600941/620845906412961792>0.
$$

Thus tP>tQ for all u. The constructed policy saturates the global Bellman bound throughout the **entire continuum**, proving the stated exact affine interval. The continuum argument rests on the disjoint-cylinder algebra, not interpolation from numerical samples.

## Sharpness

If this same supporting line attained the optimum at alpha>alpha52, positive lambdaP/lambdaQ would force eP=eQ=alpha and the Bellman slack equality would prohibit any nonoptimal action. Only A52 and B can randomize. Even for history-specific randomization, conditional risks and likelihood ratios coincide within each count state, so averaging yields effective u,s in [0,1]. The two exact error identities force s=s51-h52*u and alpha=alpha51+eta52*u<=alpha52, contradiction. The finite randomized-policy space is compact, so the infimum is attained; the line cannot stay optimal beyond alpha52.

## Verification and next scientific unit

The primary portable Python checker declares the complete finite stop sets and checks Bellman actions, reach, conditional suffixes, five rational randomized policies, endpoint identities and next candidate, using fractions.Fraction throughout. The second author-side checker separately minimizes Bellman, enumerates ordered first-hit words (including the **16** A51 descendants), evaluates four absorbing-backward corners and checks exact affine interpolation. It shares the declared historical stop sets, so it is **not** an external independent mathematical review. Neither tool performs native BRC/X6/Heartbeat arithmetic or a physical transfer claim.

After fixing A52 to immediate Q, the **53rd dual candidate only** is K53=297764424/19019, A53=(10,8,2), with continue/immediate-P tie. First-hit reach under the 52nd stop tree, two-error compensation, complete right-interval attainment and sharpness are not yet established. No native CLAIM, Driver review, proof assistant certificate or physical/native correspondence is claimed.

Pinned global knowledge: awdawmip/chatgpt-global-knowledge@674c44f8c3c194a82c63f0bba6da995d1d307ad3; pinned pre-publication Enterprise Math Source: awdawmip/enterprise-math@4fe67f915d52a563825757c8d6e9e199f2eb4b64. P000 and ACTIVE worldview have not been changed.
