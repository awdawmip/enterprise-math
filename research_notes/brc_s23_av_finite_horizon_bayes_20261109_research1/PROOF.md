# S23/AV: exact finite-horizon Bayes risk from finite symbol history

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE PROVED DERIVATION + EXACT FINITE CERTIFICATE; independent mathematical review pending.

Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: research_notes/brc_s23_av_best_return_risk_cf_20261109_research1/PROOF.md at 3d1e430b8590cbcb08be3dc626ac73940444c33e.
Domain: the external S23/AV 79-symbol auxiliary circle observer, uniform initial phase. Native X6 dynamics, ten-label capacity, Result and Review have separate predicates.

## Mathematical reduction

Retain r=ln(7)/ln(10/7), alpha=(2074774-380295r)/(79r-431), theta=79 alpha-46, with irrational 1/4<theta<1/3. Let x be uniform on [0,1), and C_j(x)=floor(79{x+j alpha}) in {0,...,78}. Set c=floor(79x), u={79x}. The initial symbol c is uniform on 79 labels and independent of uniform u. Exact integer arithmetic gives

C_j(x) = c+46j+floor(u+j theta) (mod 79).

For fixed c, a history (C_0,...,C_{m-1}) is uniquely the arc containing u in the circular partition P_m formed by t_j={-j theta}, j=0,...,m-1. Every floor(u+j theta) jumps once at t_j; for any two u its difference is at most one, so reduction mod 79 cannot identify different atoms. The m boundary points are distinct because theta is irrational. Endpoints have zero measure.

## Theorem 1 — exact future-block Bayes risk for every m,L>=1

Let P_{m+L} refine P_m by inserting t_m,...,t_{m+L-1}. For I an old P_m atom, let J(I) be its refined arcs. Under uniform phase, the smallest probability that a deterministic forecast from the m exact past symbols makes at least one error anywhere in the entire next L-symbol block is

R(m,L) = 1 - sum_{I in P_m} max_{J in J(I)} length(J).      (1)

Proof. Conditional on each initial label and old atom I, phase u is uniform on I. Distinct refined subatoms produce distinct complete observed words of length m+L and therefore distinct future blocks once the history is fixed. The Bayes decision selects the future block of the longest subatom. Its unconditional success contribution is precisely the length of that subatom. Sum over old atoms; the 79 equal initial labels contribute identical copies and cancel. QED.

Formula (1) is an all-index mathematical identity. Sorting the m+L cutpoints and scanning consecutive old atom boundaries takes O((m+L) log(m+L)) comparison operations and O(m+L) storage. Certified evaluation must additionally account for the rational precision, big-integer bit lengths, and source-coordinate construction. For L=1, (1) recovers the previously proved epsilon_m=min_{1<=d<=m} ||d theta||. The repeated one-step predictor also shows R(m,L)<=min(1,L epsilon_m) by the union bound on its first-error event, while formula (1) can give a strict improvement.

## Theorem 2 — exact first deviation in a worked finite family

The predecessor's certified rational-log enclosure is

262204504569236716045286/10^24 < theta < 262204504569236716045287/10^24.     (2)

The accompanying VERIFY_HORIZON.py uses only integer arithmetic to certify the floors of j theta, strict ordering of the relevant phase boundaries, the winning refined subcell in every old atom, and the resulting symbolic affine function a+b theta. No floating-point decision is used.

Put delta=16-61 theta, which is positive. For fixed m=128, the script exhausts each individual integer L=1,...,36 and proves by fully certified affine comparison that

R(128,L) = L(16-61 theta) for every integer 1<=L<=36.    (3)

At L=37, the new boundary t_164 lies in the old arc from t_103 to t_0. The old arc is split into lengths delta and lambda=164 theta-43, with 0<lambda<delta. The first 36 inserted boundaries still each add delta to the Bayes error, while the 37th adds lambda. The same certified full partition scan therefore gives

R(128,37) = 36 delta + lambda = 533-2032 theta.          (4)

Hence the bound L epsilon_128 is exact through horizon 36 and first ceases to be sharp at 37. This is a precise residual-phase trace effect; the 37-step optimal full-block decision is not identical to independently applying 37 one-step majority decisions.

Numerical enclosures below are exact rationals; Q=10^24:

198907965956171564549748/Q < R(128,36) < 198907965956171564551944/Q.
200446715310992995976816/Q < R(128,37) < 200446715310992995978848/Q.

The certificate also checks (m,L)=(61,8),(717,16), and individually every L in (3). Saved file RUN_EVIDENCE.txt contains the actual passing output.

## Next question

Find a proved convergent/three-gap criterion for when R(m,L)=L epsilon_m, and compute its first failure position by exact interval arithmetic. Use the existing finite certificate as a bounded discriminator, not an assertion of universal linearity. In parallel, plateau 413 geometric coverage remains an independent frozen S23/AV question requiring its original critical-cell verifier and coverage witnesses.
