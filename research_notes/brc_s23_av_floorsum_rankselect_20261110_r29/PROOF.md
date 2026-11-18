# R29: floor-sum rank/select and signed Farey batch certificates (2026-11-10)

Researcher-ID: EM-DIRECT-FEEA1D; Research-Activity-ID: RA-6490893BE980ADAE97B2BCC1. Auxiliary irrational-circle S23/AV observer, historical m=128, frozen scientific source pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessors: R27 commit 6cfd0bf078b3bd05fbd4c51508a868a4706a5823 and R28 commit 5ce03c532c07418f18088d9509eb8097184e82d3. Author-side result only; independent mathematical review and formal CLAIM are not asserted.

## Lemma 1 — exact Euclidean source counting

Let theta be irrational with 0<theta<1; historical cuts P_m are phases {s theta} for 0<=s<m. A historical arc runs counterclockwise from historical source a to its successor b. Define w=1 if its endpoints wrap through zero, otherwise w=0. For any future source t>=m, its exact arc-membership indicator is

I_{a,b}(t) = floor((t-a)theta)-floor((t-b)theta)+floor(a theta)-floor(b theta)+w. (1)

For theta=T/D, summing (1) on an integer source interval [L,U) yields

C_{a,b}(L,U) = S(L,U,a)-S(L,U,b)
    +(U-L)*(floor(a*T/D)-floor(b*T/D)+w),

where S(L,U,s)=sum_{t=L}^{U-1} floor((t-s)*T/D). Each S equals the standard Euclidean floor_sum(U-L,D,T,(L-s)T), computable in O(log D) integer arithmetic operations (bit operations and source-index sizes must be counted separately). This holds for wrapping arcs as well as ordinary arcs, and retains each historical arc's source identity.

## Theorem 2 — shortest terminal suffix via rank/select

Take a Farey regime with positive smaller denominator q, larger denominator j, and long-gap source window [j+1-q,j) (as in R27). A terminal suffix [j-H,j), m<=H<=q-1, is sufficient exactly when C_arc(j-H,j)>0 for every historical arc. This property is monotone in H. Let h_arc be the smallest positive integer h such that C_arc(j-h,j)>0. Then H_min=max_arc h_arc is the shortest possible sufficient suffix, provided H_min<=q-1. The last surviving long-gap source in arc is t_arc=j-h_arc, and its R27 event position is n=q+t_arc+1. The algorithm uses binary searches on count expressions, not enumeration of q source phases. Cost: O(m(log q+log H_min) log D + m log m) arithmetic operations, with explicit B-bit arithmetic/serialization costs for integer size B=O(log D+log(j+Kq)).

## Lemma 3 — uniform theta-enclosure stability with TWO floor sums

Let theta_-<theta<theta_+ and A<=B positive integers. Since d>0, floor(d theta_+) >= floor(d theta_-). Therefore the equality

sum_{d=A}^B floor(d theta_-)=sum_{d=A}^B floor(d theta_+)       (2)

proves that floor(d theta) is invariant for EVERY integer d in [A,B] throughout the open enclosure. Both endpoint sums are Euclidean floor sums. With sources t in [L,U) and old cuts s in [0,m), use A=L-(m-1), B=U-1. Thus equality (2) certifies every source-to-historical-cut cyclic-order comparison at once, even if U-L is millions. Separately check historical d=1,...,m-1. This is a full finite exact certificate, not a sampled comparison.

## Theorem 4 — signed semiconvergent batch

Let p/q and c/j be neighboring reduced rationals straddling theta, with q<j and determinant absolute value 1. Put e=|q theta-p|>0. The opposite neighbor in batch k is (c+kp)/(j+kq), with its positive error v_k=v_0-k e. For upper p/q>theta, source phases t+kq move by -k e; for lower p/q<theta they move by +k e. Define d_t as the directional circular clearance from source t in a sufficient terminal suffix to its next historical arc boundary in that direction. The same historical owner is preserved over k=0,...,K if K e<min_t d_t, and the Farey neighbor persists if v_K>0. Hence the maximal safe integer K is the smaller of min_t(ceil(d_t/e)-1) and ceil(v_0/e)-1, evaluated rigorously over the exact theta enclosure. All positions translate as n_arc(k)=q+t_arc+1+kq and have amplitude min(e,v_k). The minimum of the two affine positive errors must be checked over the enclosure; a switch is a legitimate finite event.

## Exact S23 certificate, comparison scope

Theta is the original irrational parameter strictly between

262204504569236716045286 / 10^24 < theta <
262204504569236716045287 / 10^24.

Both endpoints are comparison witnesses. Using m=128 and the exact rank/select calculation:

| q | p | j | c | p/q relative theta | shortest H | batch K | neighbor K bound | owner K bound |
|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 14298 | 3749 | 25339 | 6644 | lower | 164 | 9 | 9 | 252 |
| 154021 | 40385 | 168319 | 44134 | upper | 164 | 2 | 2 | 2291 |
| 6318118 | 1656639 | 10899111 | 2857796 | upper | 164 | 5 | 5 | 171406 |

Each candidate's entire long-gap source window has stable historical owner assignments by exact endpoint floor-sum equality. At H=163 precisely historical arc rank 127 (old cut source 61) is unvisited; H=128 leaves 36 historical arcs unvisited; H=164 covers all 128. The 128 final source indices form exactly the two consecutive blocks

t-j in [-164,-98] (67 sources) union [-61,-1] (61 sources).

Hence event positions for batch member k are exactly

n-(j+kq) in [q-163,q-97] (67) union [q-60,q] (61),

with 36 zero increments between blocks and q-164 zeros between adjacent batches. The respective event increments across k are

* q=14298: -3749+14298 theta for k=0..8, and 40385-154021 theta at k=9;
* q=154021: 40385-154021 theta for k=0,1, and -124904+476361 theta at k=2;
* q=6318118: 1656639-6318118 theta for k=0..4, and -11140991+42489701 theta at k=5.

The independently generated R27 exact EVENT table was used as an OPTIONAL cross-check: 1280+384+768=2432 predicted source-labeled risk events agree, each at the stated integer position and integer-affine increment. The local full verifier uses Python integers/Fraction only. The smaller standalone verifier included with this source publication reconstructs the window and batch certificate without requiring that R27 input. The algorithms preserve the index provenance of all historical arcs. They establish no native six-axis X6 dynamics, no general novelty over the classical Euclidean floor-sum literature, no independent review and no Task Result acceptance.

## Evidence and next research unit

Files: VERIFY_R29.py, CERTIFICATE_R29.md, RUN_EVIDENCE.txt. The full local run in the research environment also produced a 128-source-per-family JSON certificate. The top-level finite checks all passed, with no q-sized phase array. The next mathematical question is a near-return rigidity theorem explaining why three nonconsecutive Farey families share H_min=164 and identical two blocks; then build a direct affine-run merger outputting the 298 established R27 maximal runs without first materializing 9697 individual events. Count conversion, precision, source labels, output bytes and validation in the complexity comparison.