# R5 — Primitive-eleventh degree-7 recovery and exact sharp cost period at O(N^6)

Date: 2026-11-21. Frozen scalar nonadaptive R5. Status: AUTHOR_EXACT_DERIVATION / EXACT_RATIONAL_CHECKED / NOT_REVIEWED. Independent portable research, not a formal Task CLAIM/RUN, Result or independent review.

## Exact inherited inputs

Continue the immutable [primitive-13 predecessor](https://github.com/awdawmip/enterprise-math/blob/4520f5378832db35aabd0475f247fb24a8395f5c/research_notes/portable_direct/r5_primitive_thirteenth_20261121/RESEARCH.md) and [primitive-11 first-order predecessor](https://github.com/awdawmip/enterprise-math/blob/69664f27d752dcc6e9cabae6355821bfedf0178f/research_notes/portable_direct/r5_eleventh_residue_split_20261121/RESEARCH.md). Frozen 256 labeled hypotheses, 101 prices 214 through 314, and 32,640-pair separating certificate SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b are retained without recertification.

Minimal event sets are S0={214,215,216,217,218}, S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}, S3={223,...,290}, S4={296,...,312}. For fixed m>=1, F_m(N) counts nonnegative vectors of price multiplicities, total price N, for which at least one S_i has multiplicity load < m.

Let z be any primitive 11th root. Previous proof established that the order-nine pole coefficient is H11(z)B_m(z)/P11 and that B_m(z)=0 exactly when m mod 11 is 7,8,9,10,0. We calculate the next Laurent coefficient **only in these five classes**, which determines their previously unresolved degree-seven cost phase.

## Theorem 1 — exact recovery of the primitive-11 degree-seven coefficient

Write M={220,231,242,253,264,275,286,297,308}, P8=231*242*253*264*275*286*297*308, and

\[
H_{\rm tail}(z)=\prod_{\substack{222\le p\le314\\11\nmid p}}(1-z^p)^{-1}.
\]

The S0 finite polynomial is

\[
B_m(x)=\sum_{\substack{a,b,c,d,e\ge0\\a+b+c+d+e<m}}
x^{214a+215b+216c+217d+218e},\qquad D_m(z)=-zB'_m(z).
\]

Let U_s(z) be the coefficient of t^s in U(t)=1/[(1-z^7t)(1-z^8t)(1-z^9t)], and V_w(z) the coefficient of t^w in V(t)=1/[(1-t)(1-zt)(1-z^{-1}t)]. Define T_m(z) as the specialization at x=z of the rationally summed local generating expression

\[
\sum_{\substack{a,b,s,w\ge0\\a+b+s\ge m\\\min(a,b)+s+w<m}}
z^{5a+6b}U_s(z)V_w(z).
\]

Here the unbounded a/b tails are evaluated as rational geometric series before specialization; all their denominators are nonzero at primitive z. Define

\[
C_m(z)=220(1-z)(1-z^{-1})T_m(z)+D_m(z).
\]

For every fixed m with m mod 11 in {7,8,9,10,0}, the primitive-11 contribution is

\[
\boxed{F_m^{(11)}(N)=\frac{N^7}{7!}
\sum_{\operatorname{ord}(z)=11}
\frac{H_{\rm tail}(z)C_m(z)}
{220P_8(1-z)(1-z^{-1})}\,z^{-N}
+O_m(N^6).}\tag{1}
\]

In each of these five classes, C_m(z) is nonzero at *every* primitive 11th root; hence this is a genuine nonzero degree-seven harmonic.

**Proof of the local coefficient.** At a primitive 11th root, all 9 elements of M are pole-producing free factors for the S0 event. S1 and S2 each constrain 220 and leave exactly the other eight free. Any intersection involving S3 or S4 leaves at most seven free members of M and cannot contribute degree seven. The order-eight contributions from events involving S1 or S2 combine by inclusion-exclusion into (E1 OR E2) AND NOT E0. Put a,b for prices 214,215, s for the combined load at 216,217,218, and w for the combined load at 219,220,221. Their three event loads become L0=a+b+s, L1=a+s+w and L2=b+s+w. Therefore (E1 OR E2) AND NOT E0 is exactly a+b+s>=m and min(a,b)+s+w<m, which gives T_m. The local 220 factor is finite; the other eight pole-producing factors yield H_tail*T_m/P8.

For S0, B_m(z)=0 in precisely the five stated threshold classes. Its derivative contributes D_m(z) to the coefficient of (1-x/z)^(-8), while derivative terms multiplying B_m(z) vanish. Its coefficient is H_tail*D_m/[220P8(1-z)(1-z^-1)]. Adding the two contributions proves (1).

## Theorem 2 — explicit all-threshold noncancellation certificate

For r in {7,8,9,10,11}, k>=0, using r=11 as residue zero, the exact Gaussian-cyclotomic vector identity is

\[
\boxed{
C_{r+11k}=
\begin{cases}
C_r+\frac{k}{2}C_{r+11},&k\ \mathrm{even},\\
\frac{k+1}{2}C_{r+11},&k\ \mathrm{odd}.
\end{cases}}\tag{2}
\]

All C values are elements of Z[z]/Phi11(z), with standard basis (1,z,...,z^9). The first basis coordinates of the two base vectors are:

| r | [1]C_r | [1]C_(r+11) |
|---:|---:|---:|
| 7 | 442 | 2204 |
| 8 | 2414 | 4608 |
| 9 | 1533 | 1746 |
| 10 | -897 | -2014 |
| 11 (mod 11 = 0) | -1340 | -1360 |

Both entries of each row are nonzero and have the same sign, so the first coordinate of (2) never vanishes. The full ten-coordinate vectors for all ten bases are in RESULT_ELEVENTH_NEXT.json. Galois conjugation preserves nonzeroness, proving the stated property for each primitive z.

**Proof of the infinite threshold identity (2), rather than interpolation from samples.** Define A=z^5, B=z^6=A^-1, W(t)=tV(t)/(1-t), U0(t)=product_{j=5}^9(1-z^jt)^-1, and

\[
J_c(t)=\frac{t^2V(t^2)/(1-t)-c^2V(ct)/(1-c)-tW(t^2)+cW(ct)}{t-c},
\qquad
E(t)=\frac{tV(t^2)}{1-t}-W(t^2).
\]

Direct geometric summation over the unbounded larger of a,b, partitioned into a>=b and b>a, gives the exact rational identity

\[
\mathcal T(t):=\sum_{m\ge1}T_m(z)t^{m-1}
=\frac{U(t)}{1-t}\bigl(J_A(t)+J_B(t)-E(t)\bigr).\tag{3}
\]

Differentiating the finite S0 threshold generating function gives

\[
\mathcal D(t):=\sum_{m\ge1}D_m(z)t^{m-1}
=-\frac{U_0(t)}{1-t}
\sum_{p=214}^{218}\frac{p z^p t}{1-z^p t}.\tag{4}
\]

Consequently \(\mathcal C(t)=220(1-z)(1-z^{-1})\mathcal T(t)+\mathcal D(t)\) is explicit rational. Every denominator factor of (3)-(4) is among (1-t), (1-t^2), (1-z^j t), (1-z^j t^2) and their powers, with total pole multiplicity at each 22nd root <=3. Thus (1-t^22)^3*C(t) is a polynomial. Further C(t)=O(t^-6) at infinity, giving numerator degree <=60. These are symbolic rational-function statements, independent of sampling.

The attached exact checker calculates precisely the 61 coefficients of that bounded numerator using the formulas (3)-(4), and verifies their 22 residue sums vanish in Z[z]/Phi11(z). Hence the *entire polynomial numerator* is divisible by (1-t^22). Therefore

\[
\boxed{\mathcal C(t)=\frac{G(t)}{(1-t^{22})^2},\quad \deg G\le38.}\tag{5}
\]

It follows that for coefficient indices n>=39, C_(n+1)-2C_(n-21)+C_(n-43)=0, treating missing indices as zero. In particular all sequences at fixed residue modulo 22 are eventually affine; this recurrence already applies at the first required third value in each of the ten exceptional threshold classes. The ten exact initial vectors also satisfy C_(r+22)=C_r+C_(r+11) and C_(r+33)=2C_(r+11). Thus (2) holds for every k>=0. These full-vector checks and numerator-divisibility checks use exact rational arithmetic, not floating fits.

## Corollary — sharp minimum cost period at remainder O_m(N^6)

Previous exact source certificates establish:
- minimum cost modulus 2520 for all fixed m when retaining through degree N^9 with remainder O_m(N^8);
- primitive 11 contributes a degree-eight harmonic for m mod 11=1,...,6, and Theorems 1-2 here supply a degree-seven harmonic for the remaining five classes;
- primitive 13 contributes a nonzero degree-seven harmonic if and only if m mod 13=1,...,8.

All order d>=14 roots have at most seven 214..314 prices divisible by d, so they yield O_m(N^6); at d=12 its degree-seven contributions have order dividing 2520, as do other already included orders. Distinct primitive-root harmonics cannot cancel one another across different orders by Fourier independence. Therefore **for every fixed positive m** the sharp modulus at remainder O_m(N^6) is

\[
\boxed{
M_m=
\begin{cases}
360360=\operatorname{lcm}(2520,11,13),&m\bmod13\in\{1,2,3,4,5,6,7,8\},\\
27720=\operatorname{lcm}(2520,11),&m\bmod13\in\{0,9,10,11,12\}.
\end{cases}}\tag{6}
\]

The modulus describes the coefficient periodicity of the specified quasipolynomial truncation in cost N, not the exact full counting function and not a claim about physical six-dimensional native dynamics.

## Exact computational evidence and scope

Run python3 VERIFY_ELEVENTH_NEXT.py in this directory. It computes rational cyclotomic coefficient vectors, checks the finite polynomial bound through coefficient 60 and zero remainder modulo (1-t^22), tests the implied recurrence through coefficient 89, and independently evaluates the local event inequality by explicit finite/geometric sums and the S0 derivative by 5-variable DP for m=1,..,13 and m=18,..,22. It outputs RESULT_ELEVENTH_NEXT.json. All computations use exact Fraction arithmetic; no standard floating point or Lean checker is used.

This is author-side mathematical derivation with reproducible exact computations. Independent scientific review is NOT_REVIEWED. P000 and the active residual-fidelity worldview remain the premise of Enterprise Math, while the present scalar cyclotomic calculation is a typed cost-observer calculation without an inferred X6/BRC physical transport.

Next scientific question: classify primitive-13 degree-six harmonics in its five leading-order zero classes, and determine when orders 14, 15, 16 first force the cost modulus beyond (6). Preserve the current remainder order and scope when comparing new phases.
