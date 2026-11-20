# D25/LIFT — Joint p³ Cauchy carry support of two ordered coefficient sources

2026-10-27. AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Same previous D25 author context; not an independent reviewer and not a Source checkpoint. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7.

## Exact signed observer

For all primes p>=5 and nonnegative n,
\[
u_n=\binom{2n}{n}/8^n,\quad
c_n=\binom{3n}{n}\binom{2n}{n}^{2}/216^n \in\mathbf Z_{(p)}.
\]
Preserve the original ordered triangular Cauchy observer
\[
S_N=\sum_{j+k<N}(3(j+k)-1)u_jc_k.
\]
Population: ordered pairs (j,k). Future operations in scope: finite signed p-integral weighted sums. Precision: p³. Boolean support, exact valuation, nonzero units, and signed sum are distinct readouts.

## New u-index all-prime carry distribution

Read base-p digits d_i of n from least to most significant. Define alpha_0=0 and alpha_(i+1)=floor((2*d_i+alpha_i)/p) in {0,1}. Kummer (or Legendre) plus p not dividing 8 gives exactly
\[
v_p(u_n)=\sum_i\alpha_{i+1}.
\]
A trailing higher zero digit clears any final carry with zero additional cost. Put A=(p+1)/2, B=(p-1)/2. From prior carry 0/1 the next-carry digit counts are (A,B)/(B,A). Therefore the complete valuation-distribution polynomial over 0<=n<p^e satisfies
\[
F_{p,e}(z)=\sum_{0\le n<p^e}z^{v_p(u_n)}
=(1,0)\begin{pmatrix}A&Bz\\B&Az\end{pmatrix}^e(1,1)^T.
\]
The matrix determinant is (A²-B²)z=pz. Cayley-Hamilton gives the exact all-prime recurrence and generating series
\[
F_0=1,\quad F_1=A+Bz,\quad
F_e=A(1+z)F_{e-1}-pzF_{e-2},\qquad
\sum_{e\ge0}F_e(z)t^e=\frac{1-zt}{1-A(1+z)t+pzt^2}.
\]
Negative terms in this algebraic recurrence are not negative BRC mass. Extracting z^0,z^1,z^2, equivalently counting at most two positive carry events (including adjacent events), gives the closed coefficient-support count
\[
U_{p,0}=1,\quad U_{p,1}=p,\quad
U_{p,e}=A^e+2BA^{e-1}+(2e-3)B^2A^{e-2}
+\mathbf1_{e\ge3}(e-2)B^3A^{e-3}
+\mathbf1_{e\ge4}\binom{e-2}{2}B^4A^{e-4}\ (e\ge2).
\]
This is a proof for every p>=5 and every e>=0, not a numerical interpolation.

## Joint valuation mask and proof

Reuse without re-crediting the preceding D25 exact two-channel c_k valuation: for digits f_i of k,
\[
\beta_{i+1}=\lfloor(2f_i+\beta_i)/p\rfloor,\quad
\gamma_{i+1}=\lfloor(3f_i+\gamma_i)/p\rfloor,\quad
v_p(c_k)=\sum_i(\beta_{i+1}+\gamma_{i+1}).
\]
Define the ordered precision-safe support
\[
\mathcal K_{p,N}=\{(j,k):j,k\ge0,\ j+k<N,\ v_p(u_j)+v_p(c_k)<3\}.
\]
Then for EVERY p>=5, N>=0,
\[
\boxed{S_N\equiv\sum_{(j,k)\in\mathcal K_{p,N}}
(3(j+k)-1)u_jc_k\pmod{p^3}.}
\]
Proof: any excluded source pair satisfies u_j c_k in p³ Z_(p), hence multiplication by any p-integral weight remains zero mod p³. The original signed coefficient and j+k<N boundary have not changed. Conversely, for a pair whose combined valuation is below 3, weight 1 makes its product nonzero modulo p³. Thus this is the smallest source-wise mask uniformly safe for ALL p-integral weights. For the particular weight 3(j+k)-1 additional p-factors or cancellation may allow further reduction, which is NOT claimed here. Combining valuations gives a strictly sharper safe mask than independently testing v_p(u_j)<3 and v_p(c_k)<3.

## Exact digit-DP for the triangular source count

For N with e base-p digits, scan low to high. The finite state comprises: u carry (0/1), two c carry channels (0,0)/(0,1)/(1,1) while the running valuation stays below 3, the total valuation (0/1/2), the addition carry of j+k (0/1), and the comparison (<,=,>) of the already formed sum digits with the corresponding N digits. At each digit (j_i,k_i) update all carries and reject total valuation >=3. Compare the new sum digit with the new higher N digit, overwriting the lower-digit comparison only if the new digits differ. Accept at the end iff the addition carry is 0 and comparison is <. Every accepted digit path is uniquely an ordered pair in K_(p,N), and conversely. A fixed-state direct implementation performs O(p² log_p(N+1)) integer-arithmetic transition updates, not an asymptotic bit cost. This counts retained pairs only; it does NOT evaluate signed coefficients.

## Executed author-side evidence; exact limitations

The companion standard-library checker uses an independent factorial-Legendre valuation oracle, tests the formula against exact enumeration, compares digit DP with direct triangle masks, and performs the full signed modular sum before/after compression. Examples: at p=19,N=41 the full triangle has 861 ordered pairs and the mask keeps 636; S_N=3372 mod 19³. For p=373,N=p³=51,895,117 the DP returns 168,999,151,344,875 retained ordered pairs, a count ONLY, not a S_N sum or an H0/B0 native run. The stored author-check JSON is an actually executed expanded regression; the short reproducer was also executed separately.

BRC: REUSE_APPLIED / COMPOSE_APPLIED. Both source labels, individual carry channels, and valuations are retained until the stated p³ observation; the support quotient loses nonzero unit residues, p^4 data and possible unmodeled future operations. These are external arithmetic source indices, NOT a proved P000/X6 three-dimensional-slice observer or native dynamics.

The exact winning Source CLAIM/OPEN/checkpoint, original p=373 native H0/B0 experiment (existing Issue #1559), and the legitimate UR V2 four-file original (94,687 bytes, SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) remain unverified. Do not treat this GitHub Draft as a Source predecessor completed unit when CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS. Next scientific proof obligation: a source-faithful H0/B0 integral-coefficient and Frobenius/Delta-R transport to this carrier, or a rigorous obstruction to that transport. This mask alone does NOT prove LIFT/JT2.