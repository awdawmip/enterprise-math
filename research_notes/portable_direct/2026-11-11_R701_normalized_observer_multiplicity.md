# R701 — Exact worst-case auxiliary information for normalized BRC E* observers

Date: 2026-11-11 (Asia/Shanghai). Researcher EM-X6-54D0A4; activity RA-26A5311133C612C9AB521167.
Research lineage: frozen static E* R699 output groups; R700 scalar fusion, task RS-X6-TRIADIC-CLOSURE-DYNAMICS. This is an exact finite-model theorem (not native X6/V29/V39 realization).

## Domain and observers

v=(e,t,c,z) is any nonzero integer histogram in the Cartesian box 0<=v<=(24,18,6,12); s=e+t+c+z. Original R699 BRC positive-rational contextual readouts are T3=U/(10s), T8=V/(5s), with U=4e+5t+z and V=2e+2c+z. R700's single fused scalar is P46=(U+46V)/(10s), whose exact value plus known s recovers v.

## Theorem 1: two-probe fibers

Across all 43,224 nonzero states, the normalized rational pair (U/s,V/s) has **36,688 distinct values**, and the maximum number of different histograms with exactly equal output is **30**. The maximum is attained at precisely one rational output pair U/s=3, V/s=1 (T3=3/10, T8=1/5). Consequently a supplementary fixed-width symbol that distinguishes every possible histogram for each observed pair requires at least ceil(log2 30)=5 bits. Five suffice: enumerate each rational-output fiber in lexicographic histogram order and transmit its local index 0..29.

**Explicit thirty-state witness.** U=3s and V=s imply t=e+c, and c=3e-2z, t=4e-2z. Bounded nonnegative solutions occur for e=1..10, with solution counts respectively (2,4,3,4,3,4,3,4,2,1), summing to 30. The exhaustive finite checker certifies that no other rational pair has a larger fiber.

## Theorem 2: single-scalar fibers

Across the same states, P46 has **29,153 distinct rational values**. Its largest fiber contains **44 histograms**, attained at exactly W/s=59 or W/s=62, where W=96e+5t+92c+47z. These classes obey, respectively,

37e-54t+33c-12z=0  (W/s=59),
34e-57t+30c-15z=0  (W/s=62).

A separate bounded Diophantine enumeration verifies that each has exactly 44 states. Thus a worst-case fixed-width auxiliary symbol requires at least ceil(log2 44)=6 bits and six suffice. Natural s takes values 1..60 and fits in six bits; by R700's injective modular decoding, (P46,s) achieves this **optimal six-bit auxiliary bound**.

## Independent necessity of total/provenance count

Both normalized observers are homogeneous of degree zero in the histogram counts. In particular, v=(1,0,0,0), with s=1, and v'=(2,0,0,0), with s=2, yield equal T3, equal T8, and equal P46 despite different source counts. This makes s, or alternative sufficient supplementary information, necessary for exact histogram reconstruction.

## Complete finite certification

R701_NORMALIZED_FIBERS_VERIFY.py iterates all 25*19*7*13 - 1 = 43,224 nonzero bounded histograms and converts each rational U/s, V/s, W/s to numerator/denominator pairs reduced using integer gcd. It explicitly builds and counts all fibers, checks 36,688 and 29,153 image sizes, exact maxima 30 and 44, and the maximizing rational values. Independent bounded Diophantine loops check all 30 witnesses at U/s=3,V/s=1 and both 44-state scalar fiber equations. Full local JSON records size distributions and all maximizing vectors. Expected executed result:

R701_NORMALIZED_FIBER_EXACT_PASS 36688 29153 30 44

This is a finite mathematical classification of R699's already stated static BRC-derived observation map; it does not execute the native BRC kernel or attest a legal X6 Cell/Link/Port, V29 PASS/TRANSFER or V39 flow j. The original 60 labeled path sources stay separate from group counts, and R700+R701 remain author-side pending independent Driver review.

## Next

Build one legal source-labeled native X6 Cell/Link/Port packet that computes T3/T8 while recording V29 PASS/TRANSFER, V39 j, and the source total s. Verify that the packet's event vocabulary admits the two observers and the weighted fusion. If not, find two source histories with identical output but different legal future native observation; use that to refine the information state. P000 triadic closure and rotation covariance remain parent obligations.
