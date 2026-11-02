# C53：同残差历史检验、一位准备记忆与八读数反推（补存）

Progress-Event-ID: prime-c53-history-memory-20261102-recovered-c54
Date: 2026-11-02 Asia/Taipei
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED_IN_C53 / INDEPENDENT_REVIEW_PENDING
Original event: prime-c53-history-memory-20261102-a1
Recovery source: mounted prime_quantum_history_memory_c53.zip, RESEARCH_NOTE.md, history_memory.py, diagnostics.py and results. This record preserves the prior C53 result; its historical test counts are not new C54 executions.
Research-Activity-ID: NONE_ALLOCATED. C53 had no exposed session_start action; C54 attempted its own session_start and received STATIC_READONLY_SCOPE_DENIED, operation_sent=false.
Global read for recovery: 9bd2cd7d8a993944ac80e66182eb4ec8ecb53293
EM read for recovery: 530d31584aad57453eb8c935d0339b76c8869a94

## 1. Model and parent objective

Continue the user-directed study of prime/composite joint paths and whole-path conditions. C52 source is awdawmip/enterprise-math@7b20a913a725b5c51f77e39c475452954f1307aa:research_notes/divisor_extrema/20261102_c52_nonuniform_preparation_self_calibration.md, blob 708229febaa06a4f485dd8fa19e945a96fbc9433.

The population is all 180 different words with counts (2,2,1,1) for (2,3,5,7). Xpq counts p-before-q occurrence pairs. A=2(X23-X25+X27+X35-X37)-4, B=2X57-1, D=A+gamma B. Complete paths, positive probabilities, signed scores and rho_1 retain their types. Arithmetic words are internal joint records over a retained Heartbeat X6 Cell; no physical coordinates or time law are inferred.

## 2. Exact four-word history diagnostic

Histories h+=2332 and h-=3223 both reach36, have counts(2,2,0,0) and X23=2. Appending57 yields final(A,B)=(0,1); appending75 yields(0,-1). For any strictly positive reference P and any common strictly positive terminal weight W(A,B), set Q(w)=P(w)W(A,B)/Z. Then

C=Q(233257)Q(322375)/[Q(233275)Q(322357)]
 =[P(57|2332)/P(75|2332)]/[P(57|3223)/P(75|3223)].

Prefix masses, column terminal weights and Z cancel. Evenness and a quadratic terminal weight are not required. Every count-and-score-only continuation law gives C=1, including count-dependent rates. C!=1 certifies missing predictive information for this continuation and shared-terminal-weight scope.

More generally, matched histories hi and continuations cj with terminal score Tj independent of i give a positive table diag(prefix masses) R diag(W(Tj))/Z. Rank and all cross ratios are preserved. All cross ratios equal1 iff normalized continuation rows coincide when all admissible continuations are included. Within a positive2x2 table under arbitrary row/column scalings, three entries admit a rank-one completion; four are needed for a nontrivial multiplicative invariant. This is scoped minimality, not a universal measurement bound.

## 3. One-bit preparation repair and explicit inverse

Memory ell is0 before any visible occurrence, +1 after2, -1 after3;5 and7 preserve it. Reference rates are(x,y,z theta^ell,1), all positive, and next-symbol probability is rate times remaining count divided by the total. theta=1 recovers C52. After a visible occurrence this is a one-bit record.

For six neutral words w0=233257,w7=233275,w2=233572,w30=322357,w37=322375,w3=322573, all A=0 and B=+-1. Under any positive even terminal weight:
a=Q(w0)/Q(w7)=z theta;
b=Q(w30)/Q(w37)=z/theta;
R2=Q(w0)/Q(w2)=x(x+1)a/[b(a+1)];
R3=Q(w30)/Q(w3)=y(y+1)b/[a(b+1)].
Thus z=sqrt(ab),theta=sqrt(a/b),
x=[sqrt(1+4R2 b(a+1)/a)-1]/2,
y=[sqrt(1+4R3 a(b+1)/b)-1]/2.
The positive roots are unique for every positive rate. The cross ratio alone gives theta^2 even for arbitrary W(A,B); recovering z from a,b uses evenness.

Add w+=232357,w-=323257, with(A,B)=(2,1),(-2,1). For the quadratic terminal law, set
f+=a(b+1)(a+y+1)/[b(a+1)(x+b+1)],
f-=(2x+y+b+1)(x+y+a+1)/[(x+y+b+1)(x+2y+a+1)],
u=Q(w+)/Q(w0)*f+,v=Q(w-)/Q(w0)*f-.
Then u=q^(4+4gamma),v=q^(4-4gamma),
q=(uv)^(1/8), gamma=(logu-logv)/(logu+logv).
The domain u,v>0,uv<1 yields the unique q in(0,1) and real gamma. Eight reads are sufficient for all six parameters; no global minimum-cardinality claim is made. With A=2k, every other path is predicted by P(w)u^[k(k+B)/2]v^[k(k-B)/2] and normalization. The two exponents are nonnegative integers. Normalized calibration probabilities must also match; arbitrary data need not belong to the model.

For(x,y,z,theta,q,gamma)=(1,2,3,2,1/2,1/2), a=6,b=3/2,C=4,R2=8/7,R3=3/5,u=1/64,v=1/4. The next5 probabilities at2332 and3223 are6/7 and3/5. Counts, partial A/B and ell are a sufficient future state by induction; these histories show ell cannot be dropped at that state for theta!=1.

## 4. Error and alternative-law tests

For four probability centers each with relative epsilon, C lies in Cobs times[((1-eps)/(1+eps))^2,((1+eps)/(1-eps))^2]. For Cobs4,eps1%, this is approximately[3.8431526321,4.1632486481]. The theta interval is contained in[1.96039,2.04041].

Eight-input rigorous inversion at1% relative budgets gives outward intervals x[.97178,1.02894],y[1.94316,2.05839],z[2.94059,3.06061],theta[1.96039,2.04041],q[.48573,.51469],gamma[.43985,.56538]. At0.1% q[.49855,.50145],gamma[.49376,.50630]. These are deterministic input enclosures, not sampling confidence intervals.

Redistributing positive masses within each(A,B)fiber can preserve all18 score probabilities yet change C4 to1. Thus the coarse score histogram does not preserve this diagnostic for arbitrary reference laws. A quartic terminal2^(-D^4),gamma0 still allows neutral preparation recovery; two residual calibration odds would suggest quadratic qhat1/16, but a held-out A4/B1 corrected ratio is2^-256 rather than2^-64.

## 5. 1260 and2520 matched-history designs

With fewer than4 binary visible occurrences one type occurs at most once, so counts and inversion number determine the word. The first collision2332/3223 has counts2,2. Adding two different hidden primes once gives smallest carrier1260 in this declared two-visible/two-hidden design.

Requiring equal last visible type as well first permits23322 and32232: both reach72, have X23=2 and end in2. Adding57/75 gives2520, the minimum in that stricter design. Every last-visible preparation above predicts C2520=1 for arbitrary positive parameters and common terminal W.

A distinct alternative chooses once per complete path, with equal prior weights, fixed PL rates(1,2,3,1) or(3,1,1,2). It gives C1260=13529/12374 and C2520=5617/5358. Both have lower bounds above1 under1% relative error per entry. At prefixes23322 and32232 the reference posterior probability of the first regime is7/22 and364/1255. Remaining counts plus regime posterior odds form sufficient reference state; update odds by multiplying regime next-symbol likelihood ratios. Add scores for terminal selection. Nonunit cross ratio identifies missing information, not a unique physical mechanism.

## 6. Prior execution and provenance

C53 recorded:6 symbolic identities;32 reference DP/direct-word comparisons;320 six-parameter recoveries with55040 held-out probabilities;96 even nonquadratic recoveries;96 arbitrary-score-weight ratios and24 count-dependent nulls;343 h-transform prefixes;two error budgets;36 additional populations;20 collision populations. Diagnostics include1189 mixture conditionals,1187 posterior updates,63 general rectangle tests and90 bounded prime-role configurations. All claimed C53 assertions passed. They are reused evidence, not rerun here.

BRC source blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1 was reused unchanged in C53;11520 positive serial/recoalescence operations recorded. Generic odds-ratio invariance and PL ranking methods retain existing attribution: Luck2019 PLOS ONE e0224460; Turner et al., Introduction to PlackettLuce. Full C53 proof/code/exact results remain in the original conversation archive, now supplemented by this recoverable Source checkpoint. Independent review and formalization remain separate.

Next: extend matched continuation tables to obtain lower bounds on predictive response state or latent regime count, and determine the smallest composite carriers within an explicitly stated design.
