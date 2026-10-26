# Stage166: exact full-real N14 minimax interval

**AUTHOR_EXACT**, computation-assisted; **NO_NATIVE_CLAIM / NOT_ADMITTED**. 2026-10-26. Source pins: GLOBAL_KNOWLEDGE_V1 main@b496110a673fd7785d200b0d14d6b07611a09f07; Enterprise Math main@611e4903c3a9babc1237b74f0ed3d99df3f33ab0; Stage165 immutable author theorem@3794fcf4c4f3bbc92bc08e6d9ce8bff1ad3cfd13.

**External model only.** N=14 ternary IID P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Full ordered-history randomized stopping/deciding by step 14. eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau); V14(alpha)=min max(tP,tQ) subject to both errors <=alpha. No P000/X6 or native BRC implication.

## Theorem

\[
\alpha_{165}=\frac{881259282664541428015}{2530093150022563528704},\quad
V_{165}=\frac{4277168009143268563157}{361441878574651932672},
\]
\[
K=\frac{310447538892}{1139969309},\quad
L=\frac{912521643352}{3419907927},\quad
\eta=\frac{370490025425}{278890338406367232}.
\]

For **all real** delta in [0,eta] (including irrational values),

\[
\boxed{V_{14}(\alpha_{165}+\delta)
=V_{165}-\frac{1843864260028}{3419907927}\delta .}
\]

New right endpoint:
\[
\boxed{\alpha_{166}=\frac{881262643750052083615}{2530093150022563528704}},\quad
\boxed{V_{166}=\frac{4276909130601160631957}{361441878574651932672}}.
\]

The *same Bellman support line* is unattainable beyond alpha166; V14 itself is not claimed to end.

## Proof I: lower bound

Let s=(n,a,b) denote n observations, a zero outcomes and b one outcomes. The Q/P likelihood ratio is ell(s)=2^(a+b)/3^a. Recursively define

\[
H_s=\min\{K\ell(s),L,1+\sum_i P_i H_{s+e_i}\}
\]

omitting continuation at n=14. The Bellman inequality at every ordered history proves
\(t_P+K e_Q+L e_P\ge H_{\varnothing}\), even for arbitrary history-dependent randomized policies. Hence \(V_{14}(\alpha)\ge H_{\varnothing}-(K+L)\alpha\).

Exact Fraction enumeration over 680 count states gives \(H_{\varnothing}=74798213336514089844785955701/374688677080092029648633856\). Precisely two ties: R=(10,0,1), decide Q/continue; Y=(7,4,1), decide P/continue. Exactly 1238 other action gaps are strictly positive, minimum 8257109179793/957355345452672. The included executable replayer checks the whole finite domain.

## Proof II: full-history constructive upper bound

Choose probability r of decide-Q at R, probability y of decide-P at Y; at other states take unique Bellman minimum. The 10 ordered first-hit histories of R all have zero zero outcomes, whereas the 63 first-hit histories of Y all have four zero outcomes. Hence their future cones cannot contain one another (despite unequal depths). P/Q first-hit masses:

R=(9765625/120932352, 9765625/60466176);
Y=(175/393216, 175/995328).

Evaluate M=(eP,eQ,tP,tQ) at all four deterministic (r,y) corners using (1) exact cached count-state suffix recursion and (2) literal *unmerged* ordered-history DFS using integer P edge weights (3,1,20)/24 and Q weights (1,1,10)/12. Two algorithms agree exactly for all 16 observer values; terminal P and Q masses each equal one. Four DFS counts 408976,387997,408736,387757 sum to 1593466. All four mixed differences vanish. Therefore **for all real r,y**, \(M(r,y)=M_{00}+r d_R+y d_Y\).

The unique equal-error relation is
\[
\boxed{r(y)=\frac{3610801514373861}{11823616000000000}+
\frac{33168957903}{21113600000000}\,y}.
\]
For every real y in [0,1] this is strictly between 0 and 1, and common error
\[
\alpha(y)=\alpha_{165}+\frac{370490025425}{278890338406367232}y.
\]
At y=0, these policies reproduce both Stage165 exact endpoint and R coin. At y=1, alpha and tP give the Stage166 endpoint. Exact P/Q time gaps at the two ends are, respectively, 350688935928809353165/843364383340854509568 and 350562645358878053965/843364383340854509568, both positive; affine dependence makes tP>tQ throughout. Directly at each endpoint \(t_P+K e_Q+L e_P=H_{\varnothing}\); this affine equality holds throughout. So max(tP,tQ)=tP meets the universal lower bound for **every real alpha in the segment**.

## Proof III: strict right-support endpoint

For any alpha>alpha166, if the same line attained equality, compactness of finite-history behavioral policy space gives an optimizing policy. Equality in
\[
\max(t_P,t_Q)\ge t_P\ge H_{\varnothing}-K e_Q-L e_P\ge H_{\varnothing}-(K+L)\alpha
\]
forces eP=eQ=alpha (K,L positive) and only Bellman-minimal actions at all reached histories. Apart from R,Y the actions are unique. For each first-hit cone, the Q/P likelihood ratio is constant on its count-state prefixes; P-mass averaging of any history-dependent tie coin preserves all four P/Q observers. Disjoint cones therefore reduce every equality policy to M(r,y), r,y∈[0,1]. Equal errors force r=r(y), and hence alpha=alpha(y)<=alpha166: contradiction. This proves strict right-support sharpness, not termination.

## Evidence and governance

Replay code VERIFY_STAGE166.py rederives 680 Bellman states, 1238 gaps, four observers by two algorithms, first-hit masses, balanced coin, exact left-right endpoints and the dual equality. Exact rational summary is certificate166.json. The full executed author package (long-form proof, execution logs, full rational certificate and Stage167 scanner) has SHA256 c3a4318beb737626022aac818c15f00f947d7b2a01353d9f5fc0ffd73caff597. No floating-point fit or universal claim from finite samples: the all-real statement follows from affine algebra.

Native em_control_tasks returned CONTROL_QUOTA, session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false; owner/CLAIM unverified. GitHub author branch is **not** native Source Result or independent Driver review. Original positive P/Q ordered branches remain distinguishable; no native X6/BRC readout bridge is claimed. P000 unchanged.

Next: Stage167 **dual-only** first closure at X=(5,1,2) Q/continue with R=(10,0,1) Q/continue; primal interval remains open. See NEXT_TASK_PACKET_167.md.
