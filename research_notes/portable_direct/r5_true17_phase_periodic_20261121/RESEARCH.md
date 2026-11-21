# R5 — Genuine-incidence primitive-17 leading phase and next-order lift

Scientific date: 2026-11-21. Status: AUTHOR_EXACT_PROOF / EXACT_INTEGER_CHECK / NOT_REVIEWED. Scientific predecessor: enterprise-math@7adeeb905714c34c42279ed26dec993ba4afe7c6; earlier corrected 16-root incidence: @5aefe382332056f38cf942775097bf09afbcbb58. These fixed scientific sources are not rebased by the present control read. No formal CLAIM/RUN, review or theorem admission is claimed.

## Statement and domain

Keep exactly the original frozen scalar R5 model: 256 named hypotheses, the 101 integer prices 214,...,314, and the five **separate** failure events
E_i = {sum_{p in S_i} a_p < m}, a_p in Z_{\ge0}, with
S0={214,...,218}, S1={214,216,217,218,219,220,221},
S2={215,...,221}, S3={223,...,290}, S4={296,...,312}.
The cost generating function for the union E0∪...∪E4 is F_m(q)=C(q)R_m(q), where
C(q)=prod_{p=214}^{314}(1-q^p)^{-1}, R_m(q) the genuine inclusion-exclusion finite-numerator factor.
Take a primitive 17th root z. D=q d/dq.

**Theorem A (all positive thresholds, exact leading-phase classification).**
At z, R_m(z) depends *only* on m mod 17. Exactly
- R_m(z) != 0 if m mod 17 in {1,...,12};
- R_m(z) = 0 if m mod 17 in {13,14,15,16,0}.

Consequently F_m has an exact order-six pole at each primitive 17th root for all m in the first 12 classes. The primitive-17 contribution to the coefficient f_m(N) has a nonzero N^5 Fourier component, and the minimal coefficient-quasipolynomial period modulo O_m(N^4) is divisible by 17 for these classes. No assertion is made that this identifies the full minimum period.

**Theorem B (exact S4 derivative for *every* m>=1).**
For the single S4-event numerator R4(q),
R4(z)=0 and
D R4(z) = -5202 ceil(m/17).
Writing RA for the union E0∪E1∪E2, one has at z
R_m(z)=R_A(z)=R_0(z),
D R_m(z)= D R_A(z) - 5202 ceil(m/17)[1-R_0(z)].
Here R_0 denotes *single* E0, not the entire union. These equations preserve true joint incidence; the D R_A term cannot be replaced by a union-cardinality cutoff.

**Proposition C (finite exact further lift).**
For all ten m in {13,14,15,16,17,30,31,32,33,34}, R_m(z)=0 while D R_m(z)!=0. Therefore F_m has an exact fifth-order pole, yielding a nonzero N^4 primitive-17 Fourier term and a necessary period factor 17 modulo O_m(N^3). This extends the predecessor's five finite thresholds by a second block m=30,...,34; it is *not* yet an all-m next-order nonvanishing theorem.

## Proof of Theorems A and B

All three blocks A, S3, S4 are disjoint **variable groups** (A uses 214..221, S3 223..290, S4 296..312). Hence with R3 and R4 their single-event factors:
 R_m(q)=1-(1-RA(q))(1-R3(q))(1-R4(q)).

S3 contains four distinct prices divisible by 17: 238,255,272,289. Its bounded event polynomial is finite for every fixed m, so R3(q) vanishes to order at least four at z.

S4 comprises 17 consecutive prices, one in each residue class mod17, with unique multiple p=306. The complete homogeneous sum of all S4 price variables in the **number of selected copies** has series
 sum_{k>=0} h_k(z^{296},...,z^{312}) t^k
 =prod_{p=296}^{312}(1-z^p t)^{-1}=1/(1-t^{17}).
Thus the event cutoff at total copies <m gives
 P4(z)=sum_{k=0}^{m-1}h_k = ceil(m/17).
The 306 factor gives a simple zero in W4(q)=prod_{p=296}^{312}(1-q^p) and all other factors are nonzero. Product of their root values is prod_{r=1}^{16}(1-z^r)=17. Accordingly D W4(z)= -306*17=-5202, proving R4(z)=0 and D R4(z)=-5202 ceil(m/17).

Every nonempty intersection involving E1 or E2 contains the price p221 divisible by17. Every such finite numerator factor therefore vanishes at z. The *only* surviving RA value is the single E0 factor R0(z). Since R3 and its first derivative vanish, differentiating the displayed disjoint-block identity yields the two R_m formulas.

For E0 alone put W0(z)=prod_{p=214}^{218}(1-z^p) !=0 and P0(z,m)=sum_{k=0}^{m-1}h_k(z^{214},...,z^{218}).
The five residues are 10,11,12,13,14 mod17. Therefore its threshold generating series is
 sum_{m>=1} R0(z,m)t^{m-1}
 = W0(z)/[(1-t)prod_{r=10}^{14}(1-z^r t)]
 = W0(z) Q(t)/(1-t^{17}),
 Q(t)=prod_{r in {1,...,16}\setminus{10,...,14}}(1-z^r t).
The polynomial Q has degree exactly 11. It follows algebraically that R0(z,m+17)=R0(z,m) for every m>=1 and R0(z,m)=0 in the classes 13..17. For m=1..12, an exact polynomial multiplication/reduction in Z[z]/Phi17(z) produces **12 nonzero vectors** (stored in RESULT.json as 16-coordinate field vectors). This is a finite exhaustive certificate for the only remaining 12 classes, not an extrapolation from samples. All Galois conjugates at primitive roots have the same zero/nonzero status. This proves Theorem A.

Finally C(q) has exactly six pole factors at any primitive 17th root (the multiples 221,238,255,272,289,306). If R_m(z)!=0, its sixth-order pole survives; if R_m(z)=0 but D R_m(z)!=0, the zero is simple and the pole has exact order five. A primitive Fourier component of order N^d cannot be represented to O(N^{d-1}) accuracy using a quasi-polynomial period not divisible by 17.

## Exact finite certificate for Proposition C

The attached VERIFY.py works over integer vectors mod z^17-1 and finally reduces by Phi17(z)=1+z+...+z^16. It uses distinct load constraints L0=a+b+u, L1=a+u+v, L2=b+u+v, for
a=a214, b=a215, u=a216+a217+a218, v=a219+a220+a221.
The internal h_u and h_v are *complete homogeneous symmetric sums*, not a single reweighted union load. Each of the seven inclusion-exclusion masks retains its original individual inequalities. Derivatives for E0 and the p221-factor are performed with D=q d/dq before reduction. The independent direct E0 generating-polynomial certificate is also evaluated. The earlier known m=13 derivative vector is asserted in full, rather than simply accepting the new routine's output.

Exact DR_m(z) first two coordinates in Z[z]/Phi17(z), basis (1,z,...,z^15):

|m|coordinate 0|coordinate 1|leading R_m(z)|DR_m(z)|
|--:|--:|--:|:--:|:--:|
|13|-13328|-8840|0|nonzero|
|14|-6681|6171|0|nonzero|
|15|-7565|1105|0|nonzero|
|16|-12631|-8602|0|nonzero|
|17|-4046|9724|0|nonzero|
|30|-29087|-22542|0|nonzero|
|31|-10268|18751|0|nonzero|
|32|-17782|-3757|0|nonzero|
|33|-25262|-14994|0|nonzero|
|34|-6545|22542|0|nonzero|

RESULT.json stores all 16 field coordinates for each row, including the 17 leading-phase vectors, and the precise status/verification scope. No floating point arithmetic is involved. Reproduction: \`python3 VERIFY.py 13 14 15 16 17 30 31 32 33 34\`. The 13..17 output recovers the predecessor exact vectors. This is an author-calculated exact finite certificate, not independently reviewed.

## Reusable residual carrier and remaining problem

The 17-phase of the leading coefficient is now globally classified. The next derivative retains a multi-event joint-load residual; treating E0∩E1∩E2 as a single bound on the union would again be invalid. The closed S4 derivative isolates one factor of the next-order fluctuation exactly, permitting smaller future computations.

A concrete next question is to derive a rational threshold generating function for D RA(z,m) (including its genuine multi-load intersections), then classify whether the fifth-order 17th-root term is nonzero for *every* m congruent to 13..17 mod17. The finite evidence at k=0,1 does not prove that universal conclusion. After that, re-evaluate the eleven- and thirteen-root next-order coefficients under the corrected event incidence before asserting any full strict minimum-period formula. No P000, BRC positive-mass interpretation, native Heartbeat X6 evolution, or original frozen scientific input is changed.
