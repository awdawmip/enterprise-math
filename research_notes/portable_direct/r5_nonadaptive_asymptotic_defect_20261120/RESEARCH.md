# R5 — First two rare-failure corrections in the complete nonadaptive cost spectrum

Date: 2026-11-20. Scientific status: AUTHOR_SYMBOLIC_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Frozen scope and provenance

The frozen scalar R5 input is awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, EXACT_R5_ALL_101_BUDGETS.json, SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. It contains 256 labelled hypotheses and the 101 fixed integer-priced query labels 214,...,314. A fixed unordered query multiset, with repetitions, corrects at most f unflagged adversarial errors and e flagged erasures exactly when each of the following five minimal separating sets is hit at least m=2f+e+1 times:

- S0 = {214,215,216,217,218}, size 5.
- S1 = {214,216,217,218,219,220,221}, size 7.
- S2 = {215,216,217,218,219,220,221}, size 7.
- S3 = {223,...,290}, size 68.
- S4 = {296,...,312}, size 17.

These are taken from the original exact 32,640-pair frozen enumeration, not freshly inferred from approximate data. The predecessor's all-cost rational generating function is [GLOBAL_RATIONAL.md](../r5_nonadaptive_low_excess_425_20261120/GLOBAL_RATIONAL.md) at commit 15fcf2a6a659ba0c06287b3dd27a5b0e67b78475.

Let N=735m+D, D≥0. Let a_m(D) count query multisets of exact cost N that satisfy all five conditions, and let U(N) count *all* 101-price multisets of exact cost N:

\[
U(N)=[q^N]\prod_{k=214}^{314}(1-q^k)^{-1}.
\]

## New theorem — the first missing-design terms

For every **fixed** integer m≥1, as D→∞, define

\[
P'=\prod_{k=219}^{314}k,\quad B_m=\binom{m+4}{5},\quad C_m=\binom{m+4}{6}.
\]

Then the failure count has the exact two-leading-order expansion

\[
\boxed{
U(N)-a_m(D)=
\frac{B_m}{95!P'}N^{95}+
\frac{12792B_m-1080C_m}{94!P'}N^{94}
+O_m(N^{93}).
}
\]

For m=1: (B,C)=(1,0). For m=2: (6,1), with the N^94 bracket equal to 75,672. For m=3: (21,7), with bracket 261,072.

Let \(P=\prod_{k=214}^{314}k\). The **relative defect law** is

\[
\boxed{\lim_{D\to\infty}
N^5\left(1-\frac{a_m(D)}{U(N)}\right)
=\binom{m+4}{5}\frac{100!}{95!}\prod_{k=214}^{218}k.}
\]

Thus the smallest five-query witness determines the first non-universal term. The other four witnesses can first affect the exact polynomial asymptotic at order N^93. The statement is for fixed m; no uniform-m theorem is claimed.

## Proof

**1. Codimension.** Failure of a witness S of r distinct prices means the sum of its r nonnegative multiplicities is at most m−1. For fixed m, this admits finitely many multiplicity vectors, leaving 101−r free positive-price variables. The corresponding weighted-partition count is O_m(N^(100−r)). For S0 this is O_m(N^95); S1 and S2 are O_m(N^93); S3 and S4 are smaller. All intersections are subsets of single failures. Therefore the number of invalid multisets differs from the number failing only S0 by O_m(N^93). No independence assumption on the overlapping witness sets is needed.

**2. Exact smallest-witness series.** Let v=(v_214,...,v_218) range over nonnegative integer 5-tuples with |v|<m, and put c(v)=Σ_{k=214}^{218}k v_k. Define

\[
p'(x)=[q^x]\prod_{k=219}^{314}(1-q^k)^{-1}
\]

(with p'(x)=0 for negative integer x). The exact count of S0-failing designs is

\[
F_{0,m}(N)=\sum_{|v|<m}p'(N-c(v)).
\]

The 96 consecutive remaining prices 219,...,314 have gcd 1. Their unrestricted generating function has a pole of order 96 at q=1; every other root-of-unity pole has order at most 48. The first two residue-polynomial terms therefore give, uniformly for the finite set of c(v),

\[
p'(N-c)=\frac{(N-c)^{95}}{95!P'}+
\frac{25584}{2}\frac{(N-c)^{94}}{94!P'}+O_m(N^{93}).
\]

**3. Exact simplex moments.** Stars and bars plus the hockey-stick identity imply

\[
\sum_{|v|<m}1=\binom{m+4}{5}=B_m,\qquad
\sum_{|v|<m}v_k=\binom{m+4}{6}=C_m
\]

for every one of the five prices k∈S0. Because their sum is 214+215+216+217+218=1080,

\[
\sum_{|v|<m}c(v)=1080C_m.
\]

Expand the two displayed powers of N−c(v), then sum. The N^95 coefficient is B_m/(95!P'), and the N^94 coefficient is (25584B_m/2−1080C_m)/(94!P'). Combining with step 1 proves the main result.

**4. Relative defect.** The consecutive 101 unrestricted prices give U(N)=N^100/(100!P)+O(N^99), since every nontrivial root-of-unity pole has order at most 51. Divide step 3 by this positive asymptotic and simplify P/P'=∏_{214}^{218}k. QED.

## Sharper universal expansion through the same degree

For completeness set T=N+13332 and S_j=Σ_{k=214}^{314}k^j. Exact sums are

\[
S_2=7125146,\quad S_4=526642516946,\quad S_6=40586436142782386.
\]

Residue extraction after q=e^(−x) gives

\[
U(N)_{\rm polynomial}
=\frac1P[x^{100}]\,e^{Tx}
\prod_{k=214}^{314}\frac{kx/2}{\sinh(kx/2)}.
\]

Using log((y/2)/sinh(y/2))=−y²/24+y⁴/2880−y⁶/181440+O(y⁸), we obtain

\[
\begin{aligned}
U(N)=\frac1P\Big[&
\frac{T^{100}}{100!}-\frac{S_2T^{98}}{24\cdot98!}
+\frac{(5S_2^2+2S_4)T^{96}}{5760\cdot96!}\\
&-\big(\frac{S_6}{181440}
+\frac{S_2S_4}{69120}+\frac{S_2^3}{82944}\big)
\frac{T^{94}}{94!}\Big]+O(N^{92}).
\end{aligned}
\]

The other singularities contribute O(N^50). To obtain a fully explicit a_m(D) expansion with remainder O_m(N^93), subtract the two invalid-count terms in the boxed theorem from this U(N) expression. The first new witness-dependent correction appears at power N^95, before the N^94 term.

## Exact validation

An **independent five-bit coverage-mask integer DP** was run for m=1, each exact cost N=0,...,1800; it does not use the predecessor's rational factorization. The unique feasible design at cost 735 was recovered. Selected exact counts (unrestricted / valid / invalid / S0-only invalid):

| N | U(N) | a_1(N−735) | U−a_1 | F_0,1 |
|---:|---:|---:|---:|---:|
| 735 | 768 | 1 | 767 | 547 |
| 1160 | 38442 | 0 | 38442 | 16694 |
| 1162 | 40676 | 1 | 40675 | 17378 |
| 1165 | 44361 | 18 | 44343 | 18606 |
| 1500 | 4953405 | 724532 | 4228873 | 2771965 |
| 1800 | 109153327 | 20205401 | 88947926 | 67485223 |

The original frozen input SHA-256, the five saved witness sets and all six prior m=1 coefficients for D=425,...,430 were also checked against the preserved evidence ZIP. The degree-2,4,6 Laurent coefficients were independently reconstructed by exact rational polynomial multiplication of all 101 single-price factors. Every assertion passed. The proof, rather than extrapolation from these finite values, establishes the asymptotic for all fixed m.

Companion reproducibility materials: VERIFY.py, RESULT.json. The checker's optional --archive input is the preserved predecessor ZIP; without it, the mask DP and rational identities are still independently executable.

## Next unresolved scientific units

1. Compute the N^93 coefficient with proper inclusion-exclusion for the two overlapping seven-price witnesses, separating their intersections with S0; determine whether the first nontrivial multi-witness correction can be expressed in a compact closed form.
2. Establish a uniform asymptotic for m increasing with N and identify its transition regime.
3. The separate adaptive 256-hypothesis eight-error minimax problem retains its historical 8335≤C8*≤8343 bounds; a new strategy certificate or stronger lower-bound witness is needed to improve them.

Source status: portable author-side research only; previous contributor EM-DIRECT-4C3E47 / Activity RA-F2257922D00B2FE4C4818DBD cited for provenance, **not** as a fresh authenticated claim, execution capability, independent review, or accepted foundation. P000 / ACTIVE world-view unchanged; this scalar observer-quotient theorem has not been transferred to native BRC/X6 path dynamics.
