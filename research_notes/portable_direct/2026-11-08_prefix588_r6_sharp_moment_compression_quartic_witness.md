# PREFIX-588-R6 — Sharp third-order native BRC compression and positive quartic witness

2026-11-08, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_NATIVE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Implementation reused: PREFIX565_positive_marginal_certificate.py, verified source Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41, 96 native ports and six original labeled BRC actions. This is independent TASK_RESEARCH, not a formal Source CLAIM; native control backend could not authenticate this session.

## Model and observation

Choose a native initial port I in {0,...,95} according to any probability vector π. Make two independent, conditionally uniform choices from the original six labeled actions; use ZERO_ROOT. Retain the native path source.

Let the seven accumulated original BRC rewards be (R1,...,R6,K). Set:
P0=R1+R2, P1=R3+R4, P2=R5+R6=2-P0-P1;
Y=K-(5R1-R2+5R3-R4-4R5-4R6)/192; T=192Y.

The declared observer is **all raw mixed moments of (Y,P0,P1,P2) of total degree ≤3**, hence all its joint third cumulants. No future native transition beyond the two-step horizon is included in the compression claim.

## Theorem 1 — Exact minimal linear observer: eight variable moments

For every initial native port i, enumerate its 36 labeled two-step paths. Form the integer matrix M of shape 96×20 whose columns are the sums of T^a P0^b P1^c, a+b+c≤3, over those 36 paths. Then:

**rank_Q(M)=9.** There are **23 distinct per-port moment profiles**, with the exact class-size histogram:
size 1: 1 group; size 2: 3; size 3: 1; size 4: 14; size 6: 1; size 8: 3.

For every normalized start-port probability law π, all 20 third-order-and-below pooled moments are exactly determined by **eight variable rational coordinates**:

E[P1], E[P0], E[T], E[T P1], E[T P0], E[T²], E[T² P1], E[T³],

together with the constant E[1]=1. Within the class of linear summaries of π that must preserve all those pooled moments for **every** π, eight variable coordinates are minimal.

### Exact rank proof

The 3456 native paths admit precisely ten triple outputs (T,P0,P1), in lexicographic order:
(-10,1,1),(-4,1,1),(-1,0,1),(-1,1,0),(2,1,1),
(5,0,1),(5,1,0),(182,1,1),(188,1,1),(191,1,0).

The signed vector (155,-330,0,0,176,0,0,-11,10,0) annihilates every monomial T^a P0^b P1^c with a+b+c≤3 on this ten-point support. Thus the pathwise degree≤3 evaluation has rank at most 9, as does the conditional moment matrix M.

For the reverse bound, take M's row indices (0,2,7,8,16,18,24,32,34) and column indices (0,1,2,3,7,8,9,17,19), with columns enumerated by total degree then ascending T and P0 exponents. The 9×9 integer minor has determinant **8903588102459890348326912 ≠ 0**. Hence rank_Q(M)=9. Its first independent column is constant 36 per port, giving an exact eight-dimensional affine image of normalized π. This proves linear minimality. The 23 classes arise by exact equality of complete 20-column conditional rows; they are a sufficient deterministic merge for this observer and horizon.

## Theorem 2 — A native positive start-law counterexample at fourth order

Consider two distinct positive native starting-port distributions:

π+ = (116 δ38 + 248 δ24 + 60 δ34)/424,

π− = (160 δ0 + 165 δ2 + 11 δ7 + 88 δ32)/424.

Continue with the **same original independent uniform six-action BRC kernel** from either start law. For every a+b+c≤3, exactly:

E_{π+}[T^a P0^b P1^c] = E_{π−}[T^a P0^b P1^c].

But:

E_{π+}[T^4] − E_{π−}[T^4] = 8838720/53 > 0,

κ4^{π+}(Y) − κ4^{π−}(Y) = **1705/13893632 > 0**.

Proof: Both integer port-weight lists sum to 424. Their signed weighted difference annihilates all 20 conditional moment columns, checked as exact integers. The unnormalized difference of 36-path T^4 sums is 2545551360; division by 424·36 yields 8838720/53. Since the first three Y raw moments are identical, the difference of fourth cumulants equals the difference of fourth raw moments, rescaled by 192^4. This gives 1705/13893632.

Thus a third-order observer can be **exact and linearly minimal** but still miss a genuine, positively realizable fourth-order native gate-residual difference. One fourth-order repair coordinate distinguishes this pair. This is a sharply scoped finite-depth BRC information-preservation witness, not a replacement dynamics.

The independent signed path-support annihilator above has nonzero fourth T-moment 424258560, confirming the order distinction.

## Executed certificate and continuation

Execute PREFIX588_R6_third_order_observer_compression_certificate.py beside the original PREFIX565_positive_marginal_certificate.py. It uses exact Fraction/integer arithmetic and enumerates all original 96×6×6 paths. Local result: ALL_CHECKS_PASS; its JSON result is published with this proof. The native backend identity check returned BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false; no current owner or Source-native claim was obtained.

Next: (a) test if these eight coordinates evolve under a third native step; (b) classify the 23 signature classes under *actual* native action automorphisms; (c) repeat the construction for the eight other frozen allowed roots.
