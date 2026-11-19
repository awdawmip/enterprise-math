# R284BH — Frozen-diagonal Port gauge and the cubic raw-output obstruction

Date: 2026-11-20 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED. Source lineage: R284BG; independent portable continuation, no formal CLAIM, Result or Review claimed.

## Observer and question

For n>=2 and strictly positive rational n-by-n matrix C, define
\[
Y_C(D,z)=\det\left(D-C-\sum_{i=1}^{n-1}z_iE_{0i}\right),\qquad D=\mathrm{diag}(d_0,\ldots,d_{n-1}).
\]
The labeled star edits act in row 0. Is full identification possible if one diagonal control d_j is kept fixed, while all other diagonal controls and all star edits remain arbitrary?

## BH1: Every diagonal controller is individually necessary

For every n>=2, any index j, any fixed rational value h, and every strictly positive rational matrix C, infinitely many distinct strictly positive rational matrices C' arbitrarily close to C satisfy
\[
Y_{C'}(D,z)=Y_C(D,z)\quad\text{for every }D,z\text{ with }d_j=h.
\]
This holds for full polynomial observations and arbitrarily many adaptive scalar reads.

**Proof for j>=1.** Let T=I+t E_{0j}, where t is rational. Since det T=1, T E_{0i}=E_{0i} for all i>=1 and T D=D+t h E_{0j} for d_j=h, setting
\[
C'=TC-t h E_{0j}
\]
gives
\[
D-C'-\sum_i z_iE_{0i}
 =T\left(D-C-\sum_i z_iE_{0i}\right).
\]
So the determinants are identical. For any column l different from j the row-0 entry changes by t C_{jl}, which is nonzero for t!=0. For sufficiently small nonzero rational t, every entry stays positive.

**Proof for j=0.** Fix any k>=1 and set V=I+t E_{0k}. Now det V=1, E_{0i}V=E_{0i} for i>=1, and D V=D+t h E_{0k} when d_0=h. Setting
\[
C'=CV-t h E_{0k}
\]
gives
\[
D-C'-\sum_i z_iE_{0i}
 =\left(D-C-\sum_i z_iE_{0i}\right)V.
\]
For any row r>=1, the column-k entry changes by t C_{r0}, so C' differs and remains positive for sufficiently small rational t. This proves both cases.

Since equality holds at every permitted instrument setting, adaptive choices also receive identical transcripts; no assumption about finite precision is required.

## BH2: Binary positive obstruction when the fixed setting is zero

For every n>=2 and every j, when d_j=0 there is an exact collision among matrices in {1,2}^{n by n}. Let C be all ones and t=1. If j>=1, C' doubles row 0; if j=0, C' doubles column 1. Both have identical observations at every permitted setting. For n=3, explicit witnesses are

\[
C=\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix},\quad
C'_0=\begin{pmatrix}1&2&1\\1&2&1\\1&2&1\end{pmatrix},\quad
C'_1=\begin{pmatrix}2&2&2\\1&1&1\\1&1&1\end{pmatrix}.
\]

## BH3: Cubic raw output exponent is tight inside the R284BG guard

The exact BG construction has Sidon offsets a_i>=0, A=max a_i, Q=4A+2, e_i=Q+a_i, d_i=b^{e_i}, R=A+1, z_i=b^{R+2a_i}, and S=sum_i e_i. The distinct positive differences among n offsets imply A>=n(n-1)/2 and therefore
\[
S\ge n(4A+2)\ge 2n^2(n-1)+2n=\Omega(n^3).
\]
The monomial at exponent S in the resulting determinant has coefficient exactly 1 and every other term has a smaller exponent. The BG digit-coefficient bound is L=n n! (1+H)^n. For b>2L, all lower digits together have absolute magnitude at most
\[
L(b^S-1)/(b-1)<b^S/2.
\]
Consequently |Y_C|>=b^S/2 for every admissible BG matrix C, and the noiseless raw output needs Omega(n^3 log_2 b) bits. The existing BG upper bound O(n^3 log b) makes this Theta(n^3 log b) within that precise encoding. Its maximum individual actuator exponent remains Theta(n^2).

BH1 explains why simply freezing a diagonal controller is not an injectivity-preserving way to reduce the product exponent. BH3 is specific to the BG positive-power guarded code; no unrestricted one-read complexity lower bound is claimed.

## Reproducibility and provenance

Companion standard-library checker: research_notes/portable_direct/R284BH_frozen_diagonal_gauge_checker.py. Exact Fraction-based determinant observations: 4,320 rational cases, n=2..7, every frozen coordinate. Binary n=3 enumeration over all 512 candidate matrices with fixed-zero t=1 admissibility and a 3^5 controller grid: 24 witness pairs, 5,832 exact determinant comparisons. PASS. Verification JSON: research_notes/portable_direct/R284BH_frozen_diagonal_gauge_verification.json. These are author-side finite tests; the general theorem is the displayed determinant identity.

Parent scientific input: R284BG_INTERLEAVED_SIDON_QUADRATIC_ACTUATOR_ONE_SCALAR_PORT_DECODER_20261120.md on Enterprise Math main, as previously frozen; compare with R284BF for architecture-specific guards. This is exact finite Port/observer algebra, compatible with P000, ACTIVE Heartbeat X6 and joint-observation preservation. It makes no new ontological or Foundation claims. Port labels and permitted future operations are explicitly retained.

Next research: seek an alternative coefficient-address/readout construction achieving O(n^2) or near-quadratic raw measured output bits while preserving full diagonal control and deterministic polynomial-time decoding. Account for any extra normalization, instrument-side subtraction or communication needed to suppress known high digits.