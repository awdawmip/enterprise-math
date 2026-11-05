# C58: returning residuals, factorial memory contraction and retained path identity

Progress-Event-ID: prime-c58-interleaved-return-20261105-a1
Date: 2026-11-05 Asia/Taipei
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING
Researcher-ID: EM-DIRECT-C2CF7D / TASK_RESEARCH
Research-Activity-ID: RA-C7875C6BD7A68740A6454BF2
Global-read: f4502d8cb3b3f6ab05c68c871f79a78cb462b71f
EM-read: 818a9bf6da1e0ee0dad578df0924a926b52443fa

## 1. Inherited model and present question

Continue C57 at EM@5fd53df906cd2fb4033cc00849214567eb54db02:research_notes/divisor_extrema/20261104_c57_residual_dependent_updates.md, blob7decda7883a50004b3322ef4b4c8442f759ecca7, and its mounted exact reproduction archive. The question is whether interleaved 2/3 inputs returning the local residual to zero restore old predictive distinctions.

Keep all positive complete factor words, signed score labels, rho_1 and the retained Heartbeat X6 internal-record bridge. At visible counts(a,b), xi=2X23-ab. State ell is0,1,2:2 increments capped at2; the first two3s reset for preparation; later3s retain the old state with probability e(xi)=1/(4+xi^2), otherwise reset0;5/7 preserve state. Symbol rates(1,1,z_ell,1), z=(1/4,1,4), multiply remaining counts and normalize. Same final score uses the same strictly positive W(A,B). A,B retain C57 definitions; no quadratic/even W is needed below.

Actual prefixes h0=32223,h1=23232 reach72, have X23=3 and xi0, and prepare pure states0 and1. Complete tails557/575/755 have the calibrated matrix T with rows(1/15,4/15,2/3),(1/3,1/3,1/3),(32/45,8/45,1/9). The initial1..5 conventions are unchanged.

## 2. Exact classification of zero-return words

Appending2 changes xi by-b; appending3 changes xi by+a. A word u with r2 and s3 changes xi by as-br+2X23(u)-rs. From a=b+1 and xi0, a balanced r/r word returns to0 iff X23(u)=r(r-1)/2.

Among these words, exactly one avoids22: (32)^r. Proof: a balanced word with no22 can be alternating32, alternating23, or start/end2 with precisely one doubled3 gap. The first returns; the second adds2r to xi; the third, whose doubled gap follows j twos, adds2j>0. Starting/ending3 needs too many3s. These cases exhaust all possibilities.

Every known common word containing22 synchronizes the old latent state: after its second2 all inputs are at state2. Positive symbol likelihoods only change row masses; with the same initial counts/scores the entire remaining conditional law agrees. Raw path identity is retained. For r3 the return words are233322,323232,332223. The first ends in state2, the last in(39/40,0,1/40), independently of the old state; the alternating word retains a nonzero contrast.

## 3. Zero residual at every update, but factorial contraction

For (32)^k, every3 is entered at xi0, so e=e(0)=1/4 remains constant. Target N_k=12600*6^k. All returning visible words followed by the three tails have score columns(-1,2),(-1,0),(-1,-2), independent of prefix and returning-word identity.

With n remaining2s and n remaining3s, put a_s=n/(2n+2z_s+1), b_s=n/(2n+2z_s). The exact observed32 kernel is
K_n=[[0,a0*b0,0],[0,a1*(1-e)*b0,a1*e*b1],[0,a2*(1-e)*b0,a2*e*b2]].
The common-block kernel is K_k K_(k-1)...K_1, followed by row normalization. It retains the state-dependent likelihood of every observed symbol.

After the first block, support is{1,2}. The positive2x2 subkernel M_n has det=a1*a2*e*(1-e)*b0*(b2-b1)<0 for0<e<1. Hence old-state contrasts alternate sign at each later block and remain nonzero at every finite k. The two-history three-tail table has rank2 for every k.

Its projective cross ratio is(n+z1)/(n+z2). The image diameter is Delta_n=log((n+z2)/(n+z1)); its log-odds contraction is theta_n=(sqrt(n+z2)-sqrt(n+z1))/(sqrt(n+z2)+sqrt(n+z1)). This follows directly by maximizing t(ad-bc)/[(a+ct)(b+dt)] for a positive2x2 matrix. At z1=1,z2=4, Delta_n<=3/(n+1), theta_n<=3/[4(n+1)]. After two blocks all rows are positive. Therefore for k>=2,
d_H<=Delta_(k-1)*product_(n=1)^(k-2)theta_n<=3*(3/4)^(k-2)/k!.
Using TV<=tanh(d_H/4)<=d_H/4 gives
TV<= (3/4)^(k-1)/k!.
The same bound holds for any initial states, the calibrated positive tail, and any common positive terminal W, because stochastic readout cannot increase d_H and column weights preserve it. TV uses half-l1. The bound holds for any fixed e(0) in(0,1); nonzero-residual feedback values are not sampled by this particular word.

## 4. A nondegenerate common limit and exact calibration

Let F_n(p) be the normalized state2 probability after M_n from input(1-p,p). It is a strictly decreasing positive fractional-linear map. Define s0=0 and s_k=F1 o F2 o ... o Fk(0). Prefix h1 gives s_k, while h0 gives s_(k-1). Also s_(k+2) lies strictly between s_k and s_(k+1). The factorial bound shrinks these nested intervals to a unique s_* in(0,1); every initial state converges to(0,1-s_*,s_*).

For e1/4, F_n(0)=(4n+1)/(16n+13), F_n(1)=(4n+1)/(16n+49). Exact s29/s30 bracket gives
s_* in[.164070699386373361519175997040106856161808249,.164070699386373361519175997040106856161808250].
This is a limit of the declared conditional finite-target preparations. The selected tail limit is obtained from this state by the same W.

Unweighted tail TV between h0/h1 at k1,2,3,5,10,20 is approximately .06513409962,.003335458871,.0001937711781,5.518785394e-7,7.340724287e-14,1.972620296e-29. All are stored as exact positive Fractions. Tail odds cross ratios for k1/2/3 are104/77,48125/48854,42828047/42790625, alternating above/below1.

One block also calibrates e: the state2 mass after h1 is5e/(8-3e); h0 ends in state1. Four557/755 reads give C=(24+8e)/(24-19e), e=24(C-1)/(19C+8). At C104/77 and1% relative error per read, exact containment is[63771/291484,918681/3274324], outward decimals[.2187804,.2805712].

## 5. How common are the exceptional returning words?

R_r=[x^(r(r-1)/2)]F_rr(x), with F_ab=F_(a-1,b)+x^a F_(a,b-1), boundary1. For r1..10, R_r=1,1,3,7,18,51,155,486,1555,5095. Concatenations of the three r3 return words give R_r>=3^floor(r/3), after filling the remainder with32 blocks.

For the actual nonuniform preparation, all balanced visible words have the same numerator r!^2. With n visible symbols left their denominator lies between n+3/2 and n+9. Positive latent branch summation preserves these bounds. For the common terminal weight, max_s(TW)_s/min_s(TW)_s<=32/3. Thus any two returning words' total weights differ by at most
L_r=(32/3)*product_(n=1)^(2r)(n+9)/(n+3/2).
Consequently, conditional on a returning visible word followed by a complete tail,
Pr((32)^r)<=L_r/(L_r+R_r-1).
This is uniform in common positive W and initial state. L_r<= (32/3)*product_(j=2)^9(2r+j)/9!=O(r^8), so the bound tends to0. Exact count/bound at r20/30/40/60 gives approximately .07186984,2.4801392e-6,3.0537378e-11,1.0931492e-21. The event concerns an actually recorded word avoiding22, not automatic equality after forgetting which returning word occurred.

## 6. Forgetting word identity: exact counterexample

Keep only the two reset words233322 and332223. Each separately gives identical conditional tails from h0 and h1 and cross ratio1 under every common positive W. Forget which of them occurred, summing their complete positive word masses. The resulting cross ratio is
43128030242589/55721931509536 approximately .7739866346020016.
At W1 the tail TV is1799128752421/43686880968330 approximately .04118235755318044.
The two histories weight the two returning blocks differently, while the blocks have different final states. Keeping the block label, or its conditional mixture probability, repairs this specific coarsened observation. A known reset and an unobserved mixture of reset words are distinct readouts.

## 7. Executed evidence and attribution

All assertions passed:36 generic/specialized kernels,72 actual full-word conditional rows,36 terminal-weight cancellations,297 factorial bounds,19 inverses; all66196 balanced binary words for r1..9;225 exact-reset and18 exceptional-state checks; rolling return counts throughr60 and135 actual weighted exception bounds;28 nested intervals;7 symbolic identities. A separate independent complete enumeration of75600 used12600 words, all-pairs scoring, and matched60 DP terminal fibers with exact total1. These checks overlap and are not statistical samples. No Monte Carlo.

The unchanged BRC source is8138 bytes/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1, checked against current EM metadata.64 native positive serial/recoalescence operations were executed on proved terminal-equivalent fibers; raw words, block labels and signed scores remain recoverable. All finite results use exact Fraction arithmetic; decimal limit endpoints are outward rational rounding.

Generic positive-matrix projective contraction and synchronizing words are established theory. Actually read: Carroll2004, Birkhoff's contraction coefficient, author institution abstract, DOI10.1016/j.laa.2004.02.039; Volkov2022 original-journal search abstract for synchronization definitions. MathNet full opening timed out. The needed2x2 contraction formula is proved directly here. Present results remain author-derived with independent review pending; no comprehensive novelty review or physical experiment is claimed.

Native registration succeeded at507eb8bedb48b8222f3ff09060a9b5213ccab8b5 with the above own researcher/activity and declared previous contribution. It grants no formal Task claim or mathematical acceptance. Checkpoint publication is recorded separately.

Full Chinese proof, interleaved_return.py, run_checks.py, full_population_check.py, symbolic_checks.py, exact JSON and logs plus minimal inherited code are preserved in prime_quantum_interleaved_return_c58.zip. This Source file is a standalone scientific checkpoint.

Next: retain block-posterior information when complete return words are hidden, and derive one cross-target effective update instead of merging all zero-residual histories by their final scalar.
