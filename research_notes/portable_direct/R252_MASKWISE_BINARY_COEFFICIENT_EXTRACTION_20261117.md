# R252 — Exact binary coefficient extraction with 63 labeled masks

Date: 2026-11-17 (Asia/Shanghai). Evidence status: **AUTHOR_PROVED / EXACT_FRACTION_TESTED / TWO_PRIME_MODULAR_CROSSCHECK / NOT_REVIEWED**. Frozen science commit: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. R250: acb90adc07ec249069e3662140a8a53e794db615; R251: 3836e783853c34397f87a7a0efe89f94b53c51fd. This auxiliary positive scalar observer does not redefine P000, ACTIVE X6, or native signed provenance.

## Theorem

For the existing 63 masks m=0,...,62, each D_m containing index 0 and the selected indices 1,...,6, let d_m=|D_m| and

\[
h_{m,k}=W_{\operatorname{popcount}(m)}\rho_{D_m}^{\mathsf T}P_{D_m}^{k}{\bf1},
\qquad
\Phi_{k+1}=\sum_{m=0}^{62}h_{m,k}.
\]

The parameters a,b,pi,rho,W are unchanged from frozen R249–R251, and P_D=diag(a_i)+((1-a_i)pi_j)_{i,j in D}. Form the monic characteristic polynomial

\[
c_m(x)=\det(xI-P_{D_m})=x^{d_m}+\sum_{j=0}^{d_m-1}c_{m,j}x^j
\]

and the remainder r_{m,k}(x)=x^k mod c_m(x)=sum_{j=0}^{d_m-1}r_{m,k,j}x^j.

**For every allowed rational parameter s, every mask and every integer k>=0:**

\[
\boxed{h_{m,k}=\sum_{j=0}^{d_m-1}r_{m,k,j}h_{m,j}.}
\]

Binary exponentiation in Q[x]/(c_m) calculates r_{m,k} with O(d_m^2 log(k+2)) field operations using quadratic polynomial multiplication and reduction. Small-block characteristic coefficients and initial d_m moments require O(d_m^2) preprocessing per mask. Across exactly 63 masks,

\[
\sum_m d_m=249,\qquad \sum_m d_m^2=1071,
\]

giving O(1071 log(k+2)) exact rational *field operations* per labeled output at a single event, excluding preprocessing and integer-bit growth. Direct per-event rank-one propagation through event k+1 costs O(249(k+1)) field operations up to constant factors. This comparison is NOT a bit-complexity or wall-time speedup claim.

**Proof.** Cayley–Hamilton gives c_m(P_D)=0. Divide x^k=c_m(x)u(x)+r_{m,k}(x), substitute x=P_D, and multiply by the fixed weighted observer row and initial all-ones column. Hence the identity holds exactly for every k. The rank-one determinant identity supplies the small characteristic polynomial without dense spectral decomposition:

\[
c_m(x)=\prod_{i\in D_m}(x-a_i)-\sum_{i\in D_m}b_i\prod_{j\in D_m\setminus\{i\}}(x-a_j),
\quad b_i=(1-a_i)\pi_i.
\]

The first d_m moments follow from v_i^0=1 and
v_i^{t+1}=a_i v_i^t+(1-a_i)sum_{j in D_m}pi_j v_j^t.
Schoolbook polynomial multiplication and reduction are quadratic in degree d_m<=7. Excluding the all-seven-state mask from the 64 choices yields sums 249 and 1071. QED.

## Actual independent verification

The standalone standard-library program R252_maskwise_binary_recurrence.py reconstructs the 63 blocks independently from frozen source definitions; no SymPy, floating-point comparison, eigenvalue solver, global degree-229 least-common multiple or downloaded certificate is needed.

* **21/21 exact rational tests pass**, comparing the maskwise binary method with independently implemented direct rank-one 63-mask propagation at three parameters s=0.39, 0.40, 0.41, for event indices through n=235. At s=2/5 its first five values match the literal R251 first-five coefficients, beginning with 1406969190/2053.
* **252/252 exact modular per-mask tests pass**: independently implemented dense matrix powering and characteristic-polynomial binary powering agree at n=65536 and n=1000000, s=2/5, for every mask under both primes p=1000000007 and p=1000000009.
* Sum residues at n=65536: 254409637 and 660427110, respectively. At n=1000000: 193543422 and 519693116, respectively.
* Executed full checker duration locally was approximately 5.651 seconds, a test time, not a performance benchmark against R251.

Companion JSON gives all 21 rational-result digests and numerator/denominator bit lengths plus the four modular receipts; local full JSON SHA-256 was 6de66e598d7c26063b8f64016adf75b09babda592a201ff5e2d518c369c3b236. The huge rational answers at n=65536 or n=1000000 were not materialized; modular agreement alone is not a rational equality certificate. The theorem's universal claim follows from the algebraic proof, not the numerical samples.

## Interpretation and next frontier

Unlike R251's single degree-229 aggregate scalar denominator, R252 keeps each of the 63 mask contributions separately, retaining the labeled *positive scalar mask observer* for all future event indices under fixed P_D. It does not encode full branch-event history, signed native X6 ports or native BRC EffectHistogram; an observer-preserving interface for those requires additional structure. An existing 229-degree minimal scalar recurrence is not contradicted by 63 smaller labeled recurrences.

Next: compare complete rational bit complexity, coefficient height, initialization and output conversion against the degree-229 global generating function and direct rank-one propagation; implement a BRC-typed provenance interface if its allowed observer/future operation contracts can be retained; independently resolve continuous-parameter two-mode thresholds 270/403. No formal CLAIM, native Result or mathematical Review is asserted.