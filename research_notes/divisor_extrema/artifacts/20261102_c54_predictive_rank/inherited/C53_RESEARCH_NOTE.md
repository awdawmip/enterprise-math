# C53：同残差历史检验、一位准备记忆与八读数反推

Progress-Event-ID: prime-c53-history-memory-20261102-a1  
Date: 2026-11-02 Asia/Taipei  
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING  
Research-Activity-ID: NONE_ALLOCATED; no session-start action exposed in this turn's gateway tool surface.  
Global-read: 7b489d7f01de86318487817e4a98129dadf0d83c  
EM-read: d6ba8dee453e3faf5303bc308c6bdc9ae17e31f1

## 1. Parent question, inherited result and declared scope

The parent objective is to identify laws of prime/composite joint paths, including how whole-path conditions distinguish local histories. C52 recovered fixed Plackett–Luce preparation rates and a quadratic terminal weight from seven complete words of 1260. Its fixed-rate assumption is now tested rather than silently enlarged.

Inherited exact source: awdawmip/enterprise-math@7b20a913a725b5c51f77e39c475452954f1307aa, research_notes/divisor_extrema/20261102_c52_nonuniform_preparation_self_calibration.md, blob 708229febaa06a4f485dd8fa19e945a96fbc9433, and the mounted C52 reproduction archive. This turn uses finite positive rational calculations; no local-limit theorem is required.

Population: all 180 different words with counts (2,2,1,1) for primes (2,3,5,7). Let X_pq count ordered occurrence pairs p before q. Keep

A = 2(X23-X25+X27+X35-X37)-4,
B = 2X57-1,
D = A+gamma B.

The joint score (A,B) and complete path provenance remain separate from positive probability. rho_1 and common endpoint terms are retained symbolically; they cancel only in declared differences/normalizations. The inherited bridge treats words, scores and memory as internal records over a retained Heartbeat X6 Cell. Word order and mathematical rates are not new spatial coordinates. P000 and its protected axioms remain unchanged.

The first diagnostic permits **any positive terminal weight W(A,B)** shared by all paths with that score. The explicit inverse later specializes to a declared history-dependent preparation and q^(D²), 0<q<1. These are different scopes and are not exchanged in the proof.

## 2. A four-word diagnostic that eliminates the entire terminal weight

Set h+=2332 and h-=3223. Both have used counts (2,2,0,0), partial X23=2, partial A increment 4 and partial B increment 0. Their integer endpoint is 36. The two possible complete suffixes are 57 and 75.

The four words have final scores

| word | A | B |
|---|---:|---:|
|233257|0|1|
|233275|0|-1|
|322357|0|1|
|322375|0|-1|

Let P be any strictly positive reference law on complete words and Q(w)=P(w)W(A(w),B(w))/Z. Define

C = Q(233257) Q(322375) / [Q(233275) Q(322357)].

Then exactly

C = [P(57|2332)/P(75|2332)] / [P(57|3223)/P(75|3223)].

Proof: the two prefix masses cancel, each column has the same final score in both rows, the two terminal weights cancel, and Z cancels. No evenness, monotonicity, quadratic weight, q calibration, or gamma calibration is used here.

Consequently C=1 under every reference preparation whose continuation depends only on the common current count/score state. This includes rates that vary arbitrarily with remaining counts or with the current score: constant rates are not needed for this null. C != 1 certifies that the common count/score state is insufficient for this declared continuation observation, subject to the shared terminal-weight premise.

### General rectangle law

Take histories h_i with the same compressed state and continuations c_j for which terminal score is T_j, independent of i. Write R_ij=P(c_j|h_i). The unnormalized selected table is diag(prefix masses) R diag(W(T_j)). Every positive 2x2 cross ratio is unchanged. Since both diagonal matrices are invertible, rank is unchanged. All cross ratios equal one iff all normalized reference continuation rows coincide, provided all admissible continuations are included. This is an exact future-equivalence criterion for the specified target and observation, not a claim that four entries test every possible continuation.

Within a positive 2x2 rectangle with arbitrary row and column nuisance scalings, four entries are necessary for a nontrivial multiplicative invariant: three arbitrary positive entries a,b,c always admit the rank-one completion d=bc/a. This limited minimality statement is not a lower bound for all possible experimental designs.

The generic odds-ratio invariance is classical. This turn constructs a terminal-score-matched arithmetic rectangle and uses it to test the sufficiency of the retained state.

## 3. A constructive repair: remember the most recent 2 or 3

Introduce a state ell taking values 0,+1,-1. Before either visible type has occurred ell=0; after a 2 set ell=+1; after a 3 set ell=-1; occurrences of 5 or 7 leave ell unchanged.

Fix positive parameters x,y,z,theta, with the baseline rate of 7 normalized to 1. At a prefix with remaining counts b_p, use rates

lambda2=x, lambda3=y, lambda5=z theta^ell, lambda7=1,

and choose p with probability lambda_p b_p / sum_j lambda_j b_j. Before the first visible occurrence the 5 rate is z; this initial-state convention is part of the model. After at least one visible occurrence, ell is a single binary record. theta=1 recovers C52.

Keep Q(w) proportional to P_(x,y,z,theta)(w) q^[(A+gamma B)^2]. For the four diagnostic words, even terminal weighting gives

a := Q(233257)/Q(233275) = z theta,
b := Q(322357)/Q(322375) = z/theta,
C = a/b = theta².

Thus z=sqrt(ab) and theta=sqrt(a/b), with unique positive roots. The cross ratio alone continues to recover theta² for arbitrary W(A,B); recovering z from the two individual ratios uses W(0,1)=W(0,-1), as supplied by the even terminal law.

### Exact witness

Let (x,y,z,theta)=(1,2,3,2), q=gamma=1/2. Then

a=6, b=3/2, C=4.

Conditioning the selected population on the two prefixes gives

Q(next=5|2332)=6/7,
Q(next=5|3223)=3/5.

Both histories are at 36 and have the same current signed score. Even terminal weighting is identical on their two remaining paths, so these conditionals directly display the different preparation states.

A safe DP state for this model is (used counts, partial A, partial B, ell). From it all reference transitions, score increments and terminal observations can be computed. Induction on remaining length proves future sufficiency. The two histories above prove that ell cannot be discarded at this state when theta != 1. This gives a one-bit necessity-and-sufficiency result for the declared model once a visible type has appeared; it is not a universal one-bit representation of history.

## 4. Eight-word global inverse for six parameters

Six neutral words are

w0=233257, w7=233275, w2=233572,
w30=322357, w37=322375, w3=322573.

All have A=0 and B=+/-1. In addition to a,b define

R2=Q(w0)/Q(w2), R3=Q(w30)/Q(w3).

Direct cancellation of common prefixes gives

R2 = x(x+1) a/[b(a+1)],
R3 = y(y+1) b/[a(b+1)].

The unique positive inverse is

x = [sqrt(1+4 R2 b(a+1)/a)-1]/2,
y = [sqrt(1+4 R3 a(b+1)/b)-1]/2,
z=sqrt(ab), theta=sqrt(a/b).

These six-word preparation formulas hold for every strictly positive even terminal weight W(D), including the rational nonquadratic examples tested below.

Add w+=232357 and w-=323257, with scores (2,1) and (-2,1). The reference preparation correction factors are

f+ = P(w0)/P(w+) = a(b+1)(a+y+1)/[b(a+1)(x+b+1)],
f- = P(w0)/P(w-) = (2x+y+b+1)(x+y+a+1)/[(x+y+b+1)(x+2y+a+1)].

Define u=Q(w+)/Q(w0)*f+ and v=Q(w-)/Q(w0)*f-. Then

u=q^(4+4gamma), v=q^(4-4gamma),
q=(uv)^(1/8), gamma=(log u-log v)/(log u+log v).

The domain u,v>0, uv<1 yields a unique 0<q<1 and real gamma. Together with the positive preparation inverse, the eight specified word probabilities determine all six parameters globally within the model family.

All remaining words are predicted by

Q(w) proportional to P_(x,y,z,theta)(w) u^[k(k+B)/2] v^[k(k-B)/2], A=2k.

The exponents are nonnegative integers. The same formula also checks the normalized calibration probabilities; arbitrary positive input frequencies need not belong to this family. Eight reads are a proved sufficient design, not a claim of globally minimum cardinality.

### Numerical display of the exact rational example

For x=1,y=2,z=3,theta=2,q=gamma=1/2:

| word | Q(word), decimal display |
|---|---:|
|233257|0.020519313947293418|
|233275|0.0034198856578822366|
|233572|0.017954399703881744|
|322357|0.005671748829533925|
|322375|0.003781165886355950|
|322573|0.009452914715889875|
|232357|0.00008727833189386958|
|323257|0.005208748925082176|

The preparation ratios are a=6,b=3/2,R2=8/7,R3=3/5. The corrected residual ratios are u=1/64,v=1/4. Full rational numerators and denominators are in results/exact_checks.json.

## 5. Error bounds, a counterexample to score-only aggregation, and weight testing

If each of four measured positive probabilities brackets its true value within a relative epsilon, then the true cross ratio is enclosed by

C_obs ((1-epsilon)/(1+epsilon))² <= C_true <= C_obs ((1+epsilon)/(1-epsilon))².

For C_obs=4 and epsilon=1%, this is approximately [3.8431526321,4.1632486481], strictly separated from 1. In the declared memory model theta lies in [1.9603960396,2.0404040405] after outward rounding. Thus the history contrast can be identified before selecting a quadratic terminal law.

Full eight-input interval inversion uses monotone roots, inherited rigorous log tails and 100-bit outward dyadic arithmetic. With all eight example probabilities allowed ±1% relative error, outward decimal enclosures are

x in [0.97178,1.02894],
y in [1.94316,2.05839],
z in [2.94059,3.06061],
theta in [1.96039,2.04041],
q in [0.48573,0.51469],
gamma in [0.43985,0.56538].

At 0.1%, q is in [0.49855,0.50145] and gamma in [0.49376,0.50630]. The exact endpoints are rational intervals in the result file. These are deterministic input-containment guarantees, not sample confidence intervals. The bounds deliberately retain dependency overestimation rather than claiming optimal intervals.

Within the four neutral paths one can redistribute mass between the two histories separately in each B column, keeping all 18 (A,B) aggregate probabilities unchanged. Equalizing the two row masses in each column changes C=4 to C=1, while preserving positivity, normalization and every score-fiber mass. Thus the coarse terminal score histogram alone does not retain this particular history diagnostic for arbitrary reference preparations. It does not establish nonidentifiability within every restricted parametric model.

For an additional shape check, replace the terminal law by 2^(-D^4) with gamma=0. The six neutral reads still recover preparation. The two residual calibration ratios are both 2^-16, which a quadratic candidate interprets as q_hat=1/16, gamma_hat=0. A held-out A=4,B=1 word has corrected ratio 2^-256, whereas the quadratic candidate predicts 2^-64. This exact discrepancy survives the history-dependent reference preparation.

## 6. 1260 and 2520 as smallest carriers of two declared history tests

For binary visible words with fewer than four occurrences, at least one symbol occurs at most once; its position is uniquely determined by the visible inversion count. There are no distinct same-count, same-inversion histories. At counts (2,2), the first collision is 2332 versus 3223. Adding two distinct hidden primes once each produces the four-cell continuation design. Its smallest integer is

2²3²5·7 = 1260.

This minimum is within the declared design: two visible prime types, matching count and inversion score, and two different hidden types each appearing once. No claim is made about all possible memory experiments.

At four visible occurrences the equal-score collision ends in different visible types. To test a last-visible memory repair, require the two histories to have the same last type as well. The first binary example has counts (3,2):

h1=23322, h2=32232.

They both reach 72, both have X23=2, and both end in 2. Add the two suffixes 57 and 75; the complete target is

2³3²5·7 = 2520.

This is the smallest integer in the analogous same-last-visible design. The argument for minimality is the preceding length-four classification and the order of the four smallest distinct primes. A bounded enumeration is a check of this proof, not its infinite justification.

Every last-visible preparation of Section 3 predicts the 2520 rectangle cross ratio to be exactly 1, regardless of positive parameters and of a common terminal W(A,B). Thus this is a new held-out test of the proposed one-bit state, without fitting its parameters again.

## 7. A second mechanism: a fixed hidden preparation regime

To determine what the history contrast actually identifies, keep a different candidate model: once per complete path, choose one of two fixed PL rate sets with probability 1/2,

lambda^(1)=(1,2,3,1),
lambda^(2)=(3,1,1,2).

Within either regime there is no history-dependent rate. But the regime is unobserved, so an observed prefix updates its posterior probability. Retain the same quadratic terminal score weighting for comparison.

Exact full-word calculations give

C_1260=13529/12374 approximately 1.0933408760,
C_2520=5617/5358 approximately 1.0483389324.

The first rectangle detects history information in this mixture, too. The second one distinguishes it from the last-visible candidate, which predicts C_2520=1. At epsilon=1% relative budget on each of the four probabilities, both exact contrasts still have lower bounds above 1.

At prefixes 23322 and 32232, the reference posterior chance of regime 1 is respectively

7/22 and 364/1255.

This is the retained extra record required by this particular alternative. A sufficient reference state is (remaining counts, posterior regime odds). For a next symbol p, posterior odds update by multiplication with K1(p|counts)/K2(p|counts). Adding the partial scores gives sufficient state for later terminal selection. The reference transition is the posterior-weighted mixture of the two regime transitions. Exact Bayes updates and reference conditionals were checked for all 1189 nonterminal prefixes of the 1260 and 2520 populations.

Thus a non-unit rectangle identifies missing predictive information in the current coarse state. The subsequent 2520 experiment discriminates two explicit mechanisms for storing it. This is a constructive distinction, not an inference of a unique physical cause from four probabilities.

## 8. Mathematical and computational evidence

General author proofs: rectangle invariance and future-equivalence criterion; one-bit model state sufficiency; six neutral and eight complete-word inverse; strict input envelopes; the two minimal-design arguments; posterior-regime repair. These arguments are finite algebra/probability identities and do not depend on asymptotic normality.

Executed main checks:

- 6 full symbolic product identities;
- 32 history-preparation DP/full-word comparisons, 5760 reference word evaluations;
- 320 complete six-parameter recoveries, 55,040 held-out word probabilities;
- 96 even nonquadratic preparation recoveries;
- 96 arbitrary score-weight cross ratios and 24 count-dependent nulls;
- all 343 nonterminal prefix h-transform predictions in the exact example;
- two input budgets and 12 parameter-containment checks;
- 36 additional count populations (523 word evaluations), 5 initial 1-to-5 checks;
- 20 binary collision populations.

Executed diagnostics:

- 3 last-visible predictions rejected by the 2520 mixture witness;
- 1189 mixture posterior conditional checks and 1187 one-step posterior updates;
- 63 general rectangle/rank-one-completion checks;
- 3 additional even-weight checks, one quartic holdout and one equal-score-mass information-loss witness;
- 90 bounded four-prime configurations checking the smallest carrier.

All declared assertions passed. Counts overlap where a common finite object is tested in several ways; they are not presented as independent statistical samples. No Monte Carlo is used.

The inherited BRC source is unchanged: 8138 bytes, Git blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1, matched to current EM metadata. The inherited loader is also unchanged and retains its existing one unused relative-import omission in the in-memory AST. Positive serial/recoalescence operations were actually executed 11,520 times for selected full-word weights. New DP aggregation occurs only after equality of future transition and terminal-observer laws has been proved for (counts, A, B, ell). Signed scores label the observer and do not cancel positive branch mass.

## 9. Prior work and source status

The general cross-ratio invariance is established contingency-table mathematics; Stanley Luck (2019), *Factoring a 2 x 2 contingency table*, PLOS ONE 14(10):e0224460, explicitly discusses invariance under row/column scaling. The author HTML article was read, including Introduction lines 151–156.

The PL product formula is existing work. Turner, van Etten, Firth and Kosmidis, *Introduction to PlackettLuce*, author documentation §1, was read. This turn's contribution is the arithmetic score-matched design, explicit memory-rate inverse, discriminating 2520 construction and scoped state repair. A comprehensive novelty review and independent proof review remain separate work.

References:
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0224460
- https://hturner.github.io/PlackettLuce/articles/Overview.html

The requested task remains this user-directed continuation; no unrelated dispatch was requested. On 2026-11-02 the exposed Enterprise Math gateway contained 14 read-oriented actions and did not expose em_session_start. An actual em_status call returned a read-only-named authenticated client, registered_session_count=0 and research_authority_granted=false. It also advertised backend session-registration capability; that service advertisement is not a callable session-start action or a registration receipt. No session, activity or CLAIM was created, and no alternative mutation path was used to bypass the gateway scope.

This turn's current GitHub connector exposes 48 read operations and no file-create/update or commit writer. Plugin discovery confirms the installed GitHub connector but supplies no callable write action; no GitHub CLI is installed in this runtime. The EM note and global journal were therefore not published, and no remote commit or write receipt is claimed. PUBLICATION.json records each pending destination. Local full proof, three new Python files and exact results are delivered in the C53 reproduction package. Native activity registration and mathematical admission remain distinct.

## 10. Continuation point

The 1260 fixed-last-visible model is now exactly identifiable and testable with eight complete-word reads. The 2520 experiment distinguishes it from an explicit mixture of fixed reference regimes. Next, study which finite set of score-matched continuation rectangles determines a minimal predictive record across a family of composite endpoints, retaining the unnormalized positive source weights and actual terminal-observer scope.
