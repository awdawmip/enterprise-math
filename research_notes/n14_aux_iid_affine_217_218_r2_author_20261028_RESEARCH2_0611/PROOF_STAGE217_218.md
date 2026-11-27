# Stages 217–218: two exact full-real optimal intervals (external ternary IID N14)

**Classification:** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. This is a scientific author deliverable, not a native Source Result, formal CLA﻿IM, independent Driver acceptance, P000/X6 dynamics proof or theorem promotion.

## Exact finite model and predecessor

The observations are IID under P=(3,1,20)/24 and Q=(2,2,20)/24. A randomized policy can use *every complete ordered observation history*, stops no later than N=14, and announces P or Q. Define eP=P(announce Q), eQ=Q(announce P), tP=E_P(stop time), tQ=E_Q(stop time), and

V14(alpha)=inf{max(tP,tQ): eP<=alpha and eQ<=alpha}.

The inherited exact Stage216 right endpoint (author-level proof in immutable commit 4b2ff184d394740b795b30efefb169ee293f1e2c) is

alpha216 = 7504698785088745369/21035720123168587776,
V216 = 4095371032631387677/438244169232678912.

## New Stage217 theorem

Set K217=157464/1631 and H217=13979469720797262916799/178694060004624826368.

For **every real** delta in

0 <= delta <= 106015/5258930030792146944,

the exact value function satisfies

V14(alpha216+delta) = V216 - (314928/1631)delta.

Its right endpoint is

alpha217 = 7504698785089169429/21035720123168587776,
V217 = 4095371032629681817/438244169232678912.

The only Bellman ties are T217=(13,8,4), declare P / continue, and Z=(14,0,0), declare P / declare Q. With u the chance of declaring P at T217 and z the chance of declaring P at Z, the error-balancing coin is exactly

z217(u) = 661397004428488601/1638400000000000000 - (191789/81920000000000000)u.

Both endpoint z probabilities lie strictly between zero and one. As u increases from 0 to 1, the common error increases strictly from alpha216 to alpha217. At these endpoints tP-tQ is respectively 134153754144544607/146081389744226304 and 402461262432992921/438244169232678912, both strictly positive.

## New Stage218 theorem

Set K218=590392/6235 and H218=157610795201533453269439/2049339296374314762240.

For **every real** delta in

0 <= delta <= 136390625/7925422620672,

the exact value function satisfies

V14(alpha217+delta) = V217 - (1180784/6235)delta.

Its right endpoint is

alpha218 = 7505060794177169429/21035720123168587776,
V218 = 4093942756303281817/438244169232678912.

The only Bellman ties are T218=(8,3,1), declare P / continue, and Z=(14,0,0), declare P / declare Q. The exact balancing coin is

z218(u) = 661397004424652821/1638400000000000000 - (17366643/16000000000)u.

Both endpoint probabilities belong to (0,1). As u increases from 0 to 1, equal errors grow strictly from alpha217 to alpha218. The tP-tQ endpoint differences are 402461262432992921/438244169232678912 and 401994805549792921/438244169232678912, both strictly positive.

## Universal lower bound and complete proof

At a complete ordered history h containing n letters, a zeros and b ones, the ratio Q(h)/P(h) equals rho(n,a,b)=2^(a+b)/3^a. Define B_K recursively by

B_K(n,a,b)=min{K*rho(n,a,b) [declare P], K [declare Q], 1 + sum_{j=0}^2 P_j B_K(next_j) [continue if n<14]}.

The recurrence is justified by induction on remaining horizon over *the full ordered tree*. Under P normalization, the two terminal costs are K Q(h)/P(h) and K; the continuation cost adds exactly one P-time unit. Thus for every history-dependent randomized strategy, not merely count-dependent policies,

tP + K(eP+eQ) >= B_K(0,0,0)=H.

Consequently V14(alpha)>=H-2K alpha for all alpha. The count quotient is valid for this IID Bellman recursion only because the likelihood ratio and every suffix transition law depend exclusively on (n,a,b). It is independently checked below without collapsing ordered path provenance.

For K217 and K218 the exact rational backward recursion exhausts sum_{n=0}^{14}(n+1)(n+2)/2 = 680 count states. In each stage it has exactly 1,238 strictly positive alternative-action gaps and *only* the two ties stated above. Their respective minimum positive gaps are 294667/12682656 and 2357336/122723505. An explicit positive-rational full ordered-tree enumeration agrees, for each of four deterministic tie policy corners, with an independently implemented bottom-up Bellman evaluator; the corner vectors (eP,eQ,tP,tQ), P/Q path masses, tree counts and all exact differences are stored in certificate217.json and certificate218.json.

The two tied decisions cannot occur on the same ordered observation path. T217 has b=4 and T218 has b=1, whereas Z has b=0; b never decreases. Z is terminal and cannot precede either T. Thus the observation vector is *exactly affine*, without a u*z term:

O(u,z) = O00 + u (O10-O00) + z (O01-O00).

In both cases the four-component mixed coefficient O11-O10-O01+O00 equals precisely zero. Solving eP=eQ yields the two explicit z(u) curves. The exact endpoint sign checks above establish 0<z(u)<1, strictly increasing common error and tP>tQ *for every real u in [0,1]* by affine interpolation, not a finite grid argument. Every action taken at these states is a Bellman minimizer, so for every such u,

tP+K(eP+eQ)=H, hence max(tP,tQ)=tP=H-2K alpha.

The inherited left endpoints are verified by exact equality with the previous stage. Matching the universal bound yields the asserted V14 equalities over the complete real intervals, including irrational parameters.

## Exact computation and BRC scope

Two distinct executed programs perform (i) top-down Fraction Bellman/suffix DP plus full unmerged, positive-integer P/Q branch-mass DFS with four corners, and (ii) a separate iterative bottom-up Bellman and explicit full *ordered-word* stack enumerator which checks the saved exact certificates. The primary computations visit 73,672 ordered-tree nodes for Stage217 and 66,796 for Stage218, a total of 140,468; the independent reference reaches identical counts, corners, action ties, strict gaps, mixed terms, legal coin endpoints, and exact (alpha,V) endpoints. Exact run outputs: STAGE217_AUTHOR_EXACT_FULL_REAL_PASS 73672; STAGE218_AUTHOR_EXACT_FULL_REAL_PASS 66796; STAGE217_INDEPENDENT_EXACT_PASS 73672; STAGE218_INDEPENDENT_EXACT_PASS 66796. These are author-side checks, not independent project mathematical admission.

This reuses BRC's typed nonnegative branch masses (separate P and Q), path multiplicity and ordered provenance for the declared observation/timing functional. The 680-state compression is only an IID suffix value-function quotient; it is not a generic proof that any X6 joint relation or future observer survives compression. The locked Heartbeat World P000 (six discrete native spatial dimensions and separately typed time) remains the research basis; this auxiliary IID result has *no demonstrated native X6 embedding, observer-preserving readout or physical time calibration*. P000 is not modified.

## Strict-right separation and Stage219 dual candidate only

The exact first-switch downward-K scan from the Stage218 right corner gives

K219=314587800/3377071,
H219=28050139715601809024924983/369995418708693051506688,

with only Bellman ties (9,4,3) declare Q / continue and (14,0,0) declare P / declare Q. This is a **dual candidate only**. Its contact identity at alpha218 is

H219 = H218 + 2*alpha218*(K219-K218).

Since K219<K218, the Stage219 dual lower bound exceeds the *fixed Stage218 supporting line* by exactly 2*(K218-K219)*(alpha-alpha218) for every alpha>alpha218. This proves strict-right nonoptimality of that fixed line, NOT the unproved Stage219 primal interval. The exact first-switch scanner inspected 680 states and 1,238 positive gaps; its minimum positive gap is 7442425/1641256506.

## Evidence, permissions and next question

Files: REPRO_STAGE217_218.py (actually locally executed), certificate217.json, certificate218.json, certificate219_dual.json, RUN_OBSERVATIONS.md (real observed logs), and NEXT_TASK_PACKET_219.md. All arithmetic is exact Fraction/integer without floating point.

Scientific control pins read for this turn: GLOBAL_KNOWLEDGE_V1 main@d9859d053564a0c5b87ad606d6a885f85780880d; Enterprise Math main@d69d13f84e26004821ff24936d750088065c4975; original project P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Original author-facing predecessor: 4b2ff184d394740b795b30efefb169ee293f1e2c. Native service v0.6.11 reported research_authority_granted=false; em_control_tasks returned CONTROL_QUOTA. The active owner cannot be confirmed through this native read; this work is portable local-author research with formal registration/CLAIM/Result/Driver review outstanding.

**Next scientific unit:** compute Stage219 four full ordered-history corners and legal real balanced-coin segment, inspect mixed ancestry and time dominance, then prove full-real optimality or provide a precise rational obstruction. No Stage219 original/primal proof is claimed here.
