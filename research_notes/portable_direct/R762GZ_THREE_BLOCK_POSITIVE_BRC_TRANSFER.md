# R762GZ — Three-block positive-BRC transfer and full X6 Cell/Port returns

Date: 2026-11-20 (Asia/Shanghai). Research Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142. Frozen taskbook: enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8. Frozen P000: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R762GY@3d6e24ff6849cf2d31d270b6ce691e9f09fd2315. Status: AUTHOR-PROVED candidate model and finite exact author checker PASS; independent mathematical review NOT_REVIEWED. Native TRIADIC_CLOSURE_E permission remains open.

## Statement and declared model

R762GY defines four auxiliary K4 STAR labels 0,1,2,3, whose six unordered edges label exactly the six native signed X6 axes. These are auxiliary incidence labels, not four added native dimensions. Current named Port is one edge; chirality is +1 in this calculation. At every event choose one of the two Port endpoints v and an independent sign s in {+1,-1}; add s H_v to the signed X6 *raw chart*, where H_v is the six-axis incidence vector of the three edges incident to v, advance a separately typed event ordinal by one, and update the named Port according to R762GY's parity rule. There are four positive BRC source branches per step, not signed-amplitude recoalescence. This is a declared candidate extension, not a derivation of a physical transition from P000.

Port matching phases are M0=(01,23), M1=(02,13), M2=(03,12). At chirality +1 the next phase is always the following phase modulo 3. The two endpoint choices give both named Ports in that next phase, each exactly once.

The objective is the all-length positive *ordered-source multiplicity* Z_m of histories that return simultaneously to the initial named Port 01 and the complete signed X6 chart Cell displacement. This is an event-count observer, not a final public Cell address or calibrated physical heartbeat.

## Theorem GZ1: an exact two-state BRC operator per three events

Use formal commutative positive source-occurrence markers a,b,c,d for active K4 labels 0,1,2,3; coefficients are nonnegative integer counts of distinct **ordered endpoint choices**. A marker is neither signed force nor amplitude nor a spatial coordinate. In the stated named-Port ordering, the successive positive incidence-histogram transfer matrices are

A = [[a,b],[c,d]], B = [[a,c],[d,b]], C = [[a,d],[b,c]].

One complete three-event block is T=ABC, exactly

T00 = a^3 + abc + abd + b^3,
T01 = a^2 d + a c^2 + b^2 c + b d^2,
T10 = a^2 c + a d^2 + b^2 d + b c^2,
T11 = c^3 + d^3 + a c d + b c d.

For every integer k>=0, the coefficient of a^r b^s c^t d^u in (T^k)00 counts exactly the *ordered* 3k-event endpoint-choice words returning to initial Port 01 with occurrence vector (r,s,t,u). Each such word has 2^(3k) signed refinements before any terminal displacement restriction.

**Proof.** Each directed edge between adjacent matching layers is realized by one and only one current-Port endpoint choice. Assign it the marker of that active endpoint. For a serial pair of positive sources, concatenate words and add their marker exponents, multiplying integer multiplicities. For alternative words with identical endpoint state and exponent vector, retain multiplicity by positive addition. Those are precisely the typed positive BRC serial and recoalescence operations; matrix multiplication on the positive histogram semiring implements them. The three layer operators are A,B,C by their common endpoints; multiplying gives the four entries of T above. Induction by successive three-event blocks proves the all-k claim. No cancellation of negative source weights is used.

At a=b=c=d=1, for k>=1, (T^k)00=2^(3k-1). Including the 2^(3k) independent signed choices gives 4^(3k)/2 signed words returning to the named Port, reproducing GY1.

## Theorem GZ2: full Cell return by a terminal positive BRC sign-refinement observer

For n>=0 set beta(n)=binomial(n,n/2) if n is even, beta(n)=0 otherwise. Define L(a^r b^s c^t d^u)=beta(r)beta(s)beta(t)beta(u) and extend by *nonnegative integer linearity*. Then

Z_(3k) = L((T^k)00) for all k>=0, and Z_m=0 if 3 does not divide m.

In particular Z_m>0 if and only if 6 divides m.

**Proof.** For a fixed endpoint word with n_v active appearances of each vertex v, the signs on those appearances can sum to zero in precisely beta(n_v) ways; sign choices for distinct vertices occupy disjoint positions and multiply. If their four signed net counts are z_v, the six native chart-coordinate increments are y_uv=z_u+z_v. This K4 edge-incidence map from Z^4 to Z^6 is injective: y01=y02=y12=0 forces z0=z1=z2=0, then y03=0 forces z3=0. Thus full six-axis Cell return is exactly the joint condition z_v=0 for all four vertices. Applying L to the positive ordered-endpoint histogram counts every signed return and each provenance word with its correct multiplicity. Named Port return needs m divisible by 3; all four zero signed net counts require m even. Conversely when 6 divides m, repeat an eligible active vertex over a three-edge Port cycle, then assign half its occurrences + and half -; hence at least one return exists for each such length.

This occurrence-histogram quotient is safe only for terminal Cell/Port return and future transitions that depend on named Port and newly independent signs, not prior sign/order. It does NOT preserve the complete ordered history, hidden Link gates, chirality erasure, or phase cancellation. The actual path-level BRC words and their multiplicities remain the underlying source population.

## Theorem GZ3: a two-term all-k formal recurrence

Let U_k=(T^k)00. Then U0=1, U1=a^3+abc+abd+b^3 and

U_(k+2)=S U_(k+1)-D U_k,

where S=a^3+b^3+c^3+d^3+abc+abd+acd+bcd and D=(ab-cd)(ac-bd)(ad-bc).

**Proof.** The two-by-two characteristic identity T^2-(tr T)T+(det T)I=0 follows by direct multiplication. For the three factors A,B,C, determinant multiplicativity yields det(T)=(ab-cd)(ab-cd? No: see correction below).

**Checked factorization:** det(A)=ad-bc; det(B)=ab-cd; det(C)=ac-bd, hence det(T)=(ad-bc)(ab-cd)(ac-bd), which equals D. Multiplication by T^k and taking the (0,0) entry gives the stated recurrence; tr(T) equals S by its displayed entries. The minus sign is *formal polynomial algebra*, NOT a negative weighted BRC branch. For executable counts the companion checker uses only nonnegative occurrence-histogram serial/recoalescence and never evaluates signed-BRC mass.

## Exact results and reproduction

Event m: Z_m, all exact integers:
0: 1
6: 88
12: 61160
18: 96403768
24: 211907632744
30: 544635063751488
36: 1532744178320344712.

The number of equally weighted signed candidate words is 4^m, so the positive-BRC joint-return probability is Z_m/4^m. The values at 6 and 12 independently match R762GY; values at 18,24,30,36 extend the prior frontier.

The companion R762GZ_CHECK.py implements an exact positive BRC incidence-histogram semiring, including explicit typed serial and alternative recoalescence, exact matrix powers to 36 events, terminal independent-sign lift, and an independent direct signed named-Port/net-vertex dynamic-programming comparison through 12 events for both chiralities. Its output is R762GZ_EVIDENCE.json. Author execution PASS; exact integers, no floating point, no pi/trigonometric calculation and no sign/amplitude conflation. Unbounded statements above are proved algebraically, not inferred from those finite checks. Script source and model assumptions are the complete reproducibility specification; no external dependency is needed.

## P000 and BRC boundary; next discrimination

P000 fixes six spatial axes, pairwise native PERP_E, a native 120-degree right angle, and triadic primitive stability. It does not supply the chosen signed composite STAR Port update, four independent branch permissions, physical heartbeat duration or full Link/rotation dynamics. Consequently the three-block return laws are AUTHOR-PROVED_CANDIDATE_MODEL, not a native TRIADIC_CLOSURE_E theorem or Working Truth. The transfer is a problem-specific specialization of the existing positive weighted BRC branch semiring and explicit histogram ideas (source: enterprise-math main, src/enterprise_math/brc_weighted.py and definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json), not a claim to a novel universal BRC tool family. The local checker executes a declared compatible histogram extension, not the repository module.

The next exact test is to identify actual native Cell/Port/Link/time legality on each of the four candidate branches and produce either legal typed witnesses or a minimal rejected event with original state, Link, active endpoint, sign, time, governing rule and source. If any native gate depends on past signed history, extend the BRC carrier with that hidden gate state and labeled provenance rather than applying this unsafe quotient.

Historical contribution: EM-X6-3050F6 (provenance only). Native control read request emr3-20261120-1722-r762gz-current-state-v1 returned SUCCEEDED with 2026-11-20T09:25:58Z snapshot, NEEDS_DISPATCH, no active owner/CLAIM, execution_authorized=false. Prior prepare emr3-20261120-1540-r762gx-own-cont-prepare-v1 ended FAILED with execution_branch_base must be a 40-hex commit SHA; neither failed write nor protected PROGRESS is replayed. GitHub portable science is not formal Result/Review or an authenticated Activity association.
