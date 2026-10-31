# Stage216 — full-real primal interval in the external N14 ternary-IID model

**Status (2026-10-28):** PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. This is an external statistical auxiliary problem, not native P000 six-dimensional Cell dynamics, a formal Source Result, a CLAIM, an independent Driver review or a theorem about physical time.

## Definition and exact statement

At each of at most 14 IID observations, P=(3,1,20)/24 and Q=(2,2,20)/24 on symbols 0,1,2. Policies may randomize their stop/decision using the entire ordered observation history. Let eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf_{eP,eQ<=alpha} max(tP,tQ).

The inherited Stage215 author endpoint is alpha215=3747711513430661245/10517860061584293888, V215=2066603386919928833/219122084616339456 (source PR #1571, immutable Stage215 commit 2ecb7fb85b835f70ce502a3cf1f71ed839e1d332).

**Theorem.** For **every real** 0<=delta<=9275758227422879/21035720123168587776, including irrational delta,

V14(alpha215+delta) = V215 - (1816115578006559472/9275758227422879)*delta.

The new endpoint is alpha216=7504698785088745369/21035720123168587776 and V216=4095371032631387677/438244169232678912.

## Universal bound on all ordered-history policies

For history count state s=(n,a,b), Q(h)/P(h)=rho(s)=2^(a+b)/3^a, with positive P mass at every history. Define K=908057789003279736/9275758227422879 and the finite exact backward recursion B_K(s)=min{K*rho(s) (declare P), K (declare Q), 1+sum_j P_j*B_K(next(s,j)) (continue)}; forbid continue when n=14. Backward induction **on each original ordered history** proves tP+K(eP+eQ)>=B_K(0,0,0), even for randomized full-history policies. The count quotient is sufficient only for this IID Bellman suffix observer, not for the native X6 state.

Exact rational evaluation over sum_{n=0}^{14} (n+1)(n+2)/2=680 count states yields H=B_K(root)=10060422269700525971327026167740407/127032717449378935977323595300864. It exhibits 1,238 strictly positive alternative-action gaps with minimum 3387232024158932057/432769775858641842624, and exactly two tied states: T=(1,0,1), with Q vs continue; Z=(14,0,0), with terminal P vs Q. Thus V14(alpha)>=H-2*K*alpha for every feasible full-history policy.

## Exact randomized witness and tightness for all real alpha

At T choose Q with probability u (otherwise continue); at Z choose P with probability z (otherwise Q). T has b=1 and Z has b=0; observation counts never decrease, so T cannot precede Z. Z is terminal and cannot precede T. No ordered history uses both tie decisions. Consequently the four-observation vector O=(eP,eQ,tP,tQ) has exactly the affine form O(u,z)=O(0,0)+u*DT+z*DZ, with zero mixed uz coefficient, not merely a numerical approximation. The four exact rational corner vectors are preserved in certificate216.json.

The equal-error condition eP=eQ gives the affine coin
z(u)=305483250299541629/819200000000000000 + (50430503829405343/1638400000000000000)*u.
At the endpoints z(0)=305483250299541629/819200000000000000 and z(1)=661397004428488601/1638400000000000000, both in (0,1). Hence the coin is valid for every real u in [0,1]. Its shared error increases strictly from alpha215 to alpha216.

At u=0 and u=1 the exact tP-tQ differences are, respectively, 190531627781481473/219122084616339456 and 134153754144544607/146081389744226304, both positive, hence tP>tQ throughout. All actions in this witness are Bellman minima, so tP+K(eP+eQ)=H and therefore max(tP,tQ)=tP=H-2*K*alpha. This attains the universal lower bound at every real alpha in the stated interval. Both endpoints join the inherited Stage215 certificate exactly.

The exact Fraction IID suffix dynamic program agrees on all four deterministic tie-policy corners with a separately traversed **unmerged ordered-history DFS** using positive *integer* P/Q branch masses and exact denominator 24^14. The four ordered visit counts are 24,958 / 24,958 / 18,457 / 18,457, total **86,830**, with every corner and its cross term checked exactly. The source scripts and observed logs are included; no remote computation or independent mathematical review is implied by source storage.

## First strict-right separator and next frontier

A complete exact rational first-switch scan finds Stage217 **dual-only** K217=157464/1631, H217=13979469720797262916799/178694060004624826368, ties at (13,8,4) between P and continue and terminal (14,0,0) between P and Q. The contact identity H217=H216+2*alpha216*(K217-K216) is exact and K217<K216. Thus the new dual lower bound strictly exceeds Stage216's **fixed supporting line** at every alpha>alpha216; Stage217 primal optimality remains unproved.

## Types and authority

BRC reuse: separate positive-rational P and Q branch transport, multiplicity and ordered provenance are retained in the unmerged DFS; exact IID suffix factorization justifies the restricted count-state Bellman compression. No signed/phase cancellation, infinite-scale theorem, native three-dimensional slice embedding, X6 observer/readout preservation or physical calibration is asserted. Inputs pinned to GLOBAL_KNOWLEDGE_V1 main@1253d79ae5047ccf148f5a33bc2cc68e9a6b4caf, Enterprise Math main@e52306357a448bf8880b4ef6424bb2e5e54a6166 and P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Owner lookup via the native adapter returned CONTROL_QUOTA; no active owner, CLAIM or Source Result is inferred.
