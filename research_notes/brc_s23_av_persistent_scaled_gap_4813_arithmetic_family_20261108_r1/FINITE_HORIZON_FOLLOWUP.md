# S23/AV follow-up: 2,671 consecutive strict horizon anomalies and exact N(298), N(377), N(456)

Date: 2026-11-08 Asia/Shanghai.
Status: AUTHOR_SIDE_EXACT_FINITE_INTEGER_PROOFS; independent mathematical review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
This proof extends PROOF.md in the same directory at corrected commit a3e9d88c2cd779ee7aa4e7756a0724c961a281f7, and uses its unconditional threshold-gap scaling lemma and 4,813-term finite anomaly family. Scope: two legal S23/AV parameter points with the likelihood-sign future observer.

## Definitions reused

For a prefix with (k,ell)=(#label1,#label4), Lambda(k,ell)=7^(k+ell)/10^k; label3 pads to any length n>=k+ell. For horizon h, T_h={10^i/7^s:0<=i<=s<=h} has M_h=(h+1)(h+2)/2 distinct thresholds and M_h+1 open cells. N(h) is the least prefix length for which all open cells have a padded prefix likelihood ratio witness.

The extreme-left bound is n_tail(h)=min{n>=1:7^(n+h)<10^n}. Previous PROOF.md establishes for every m=0,...,4812 that N(140+79m)>=880+431m, while n_tail(140+79m)=764+431m.

## Theorem 1: exact saturation at three new horizons

N(298)=1742, N(377)=2173, N(456)=2604.

Proof. These h are h_m=140+79m for m=2,3,4. The previous theorem supplies their corresponding lower bounds 880+431m. The independent exact verifier VERIFY_EXACT_N298_377_456.py constructs all T_h thresholds, sorts candidate logarithmic hints, and verifies the ENTIRE sorted order by adjacent strict integer cross-products (10^i*7^s2 < 10^i2*7^s). It then enumerates every pair (n,k), 1<=n<=880+431m, 0<=k<=n, and marks an open cell only when its left and right comparisons to the exact prefix Lambda(n-k,k) are checked with integer powers. This exhaustively witnesses every open cell by the claimed length, giving N(h)<=bound. The exact matching lower bound proves equality.

Finite certificate:
h=298: 44851/44851 cells, n=1742;
h=377: 71632/71632 cells, n=2173;
h=456: 104654/104654 cells, n=2604.

The validator uses floating logarithms solely to propose threshold order and lookup indices: the order of every adjacent pair and every recorded witness interval is checked with exact integer inequalities. It does not infer non-occupancy from an approximate index.

## Theorem 2: a new closer rational resonance and 2,671 consecutive non-tail horizons

The exact rational numbers A*=10^431/7^510 and B*=1 are adjacent thresholds in T_510.

Proof of adjacency. A*<1 is the exact inequality 10^431<7^510. For each s=1,...,510 compute the largest integer i satisfying 10^i<7^s; the exact 510-row integer certificate proves 10^i/7^s <= A*, with equality at (i,s)=(431,510). Thus no T_510 threshold lies strictly between A* and 1. The preceding scaling theorem implies for EVERY t>=0 that the interval

J_t=(10^431/7^(510+t), 7^(-t))

is a single adjacent open cell of T_(510+t).

For a prefix with k label1 and ell label4, Lambda(k,ell) belongs to J_t if and only if

10^431/7^510 < 7^(k+ell+t)/10^k < 1.

Put v=ell+t and K(v)=min{k>=0:7^(k+v)<10^k}. For fixed v, increasing k multiplies 7^(k+v)/10^k by 7/10, so the largest possible value below 1 is R(v)=7^(K(v)+v)/10^K(v). Therefore if R(v)<=A*, NO prefix with this v can enter J_t.

VERIFY_NEAR_RESONANCE.py checks, using only exact integer recurrence for N=7^(K(v)+v), D=10^K(v), that for every v=0,...,20025,

R(v)<=A*.

At each v, the recurrence checks N<D and that the immediately preceding k=K(v)-1 produces a ratio >=1, so it has indeed chosen the smallest legal K(v). It then checks N*7^510<=D*10^431, including the equality-safe boundary. The 20,026 finite rows are a complete exact certificate for that declared range.

If a prefix of padded length n<=20025-t existed in J_t, then ell<=n, hence v=ell+t<=20025, contradicting that finite certificate. Thus for all integers 0<=t<=20025,

N(510+t)>=20026-t.

To compare with n_tail, write h=510+t and n=20025-t. Then n+h=20535, independent of t. The exact integer inequalities

10^17354 <= 7^20535 < 10^17355

imply for each t=0,...,2670, that n>=17355 and therefore 7^(n+h)<10^n. Hence

n_tail(510+t) <= 20025-t < N(510+t) for every integer t=0,...,2670.

This certifies 2,671 CONSECUTIVE distinct horizons h=510,...,3180 with a strict interior threshold obstruction, not merely an arithmetic progression. The theorem describes exact lower bounds, not the unknown exact N(h) at these horizons.

Boundary values from exact integer binary search:
- h=510: N>=20026, n_tail=2783, excess>=17243;
- h=535: N>=20001, n_tail=2919, excess>=17082;
- h=3180: N>=17356, n_tail=17350, excess>=6;
- h=3181: current constructed lower bound N>=17355 equals n_tail=17355, so this family certificate no longer produces strict excess.

## Scope and independent research questions

Both proofs use a two-point S23/AV auxiliary likelihood-sign experiment, not native time evolution or full six-source ten-label mother-model reconstruction. BRC reuse is concrete: the joint (#label1,#label4) count carrier and provenance are retained, and compression to z=1/4 loses the distinctions tested by future likelihood signs. Finite-horizon threshold partition is the certified observer readout under the stated future operations.

VERIFY_EXACT_N298_377_456.py and VERIFY_NEAR_RESONANCE.py were actually executed with Python 3 standard library; their exact stdout is in RUN_EXACT_N298_377_456.txt and RUN_NEAR_RESONANCE.txt. Formal native CLAIM/Owner/Research-Activity remain unconfirmed because the control backend currently returns BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. Theorem admission and independent review are separate steps.

Next: measure or analytically bound the first near-resonance return to J_0 after v=20025; try matching finite upper certificates for h=510 and h=535; extend the continued-fraction mechanism for additional close rational approximants; keep full-lawful delta4 minimax and the ten-label mother-model bridge independent.
