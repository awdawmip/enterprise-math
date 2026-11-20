# R5 | Primitive cubic-root cost residual (2026-11-21)

Status: AUTHOR_EXACT_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED. Frozen 256-hypothesis, 101-price scalar nonadaptive R5 model (prices P={214,...,314}); primitive cube root is a cost-generating-function phase, not X6 native time.

Scientific pin: EXACT_R5_ALL_101_BUDGETS.json, SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. Two preexisting local ZIP copies match this digest. Reuse the predecessor's exhaustive 32,640-pair separation certificate. The five minimal separating sets are:
S0=[214,218], S1={214,216,...,221}, S2=[215,221], S3=[223,290], S4=[296,312].
For fixed integer m>=1, F_m(N) counts nonnegative query multiplicities of total price N when at least one S_j has fewer than m queries. Let omega^3=1, omega!=1, omega^2+omega+1=0. Write F_m^(3)(N) for only the two primitive cube-root partial-fraction contributions, *not the entire count*. Put
P3=product_{j=0}^{31}(219+3j), A3=1/(3^32 P3)>0.

## New theorem A: entire class m=3k+1

For every fixed k>=0,
\[
\boxed{F_{3k+1}^{(3)}(N)=\frac{(k+1)A_3}{31!}N^{31}\,(2,-1,-1)_{N\bmod3}+O_k(N^{30}).}
\]
The two primitive cubic poles are of genuine order 32. In particular a period-two or nonperiodic observer cannot retain the N^31 cubic residue.

**Proof.** For a nonempty I subset {0,1,2,3,4}, the inclusion-exclusion term is
\[
H_{I,m}(q)\prod_{p\in P\setminus\bigcup_{j\in I}S_j}(1-q^p)^{-1},
\]
where H is a finite polynomial because each constrained price multiplicity is less than m. At omega, the pole order is bounded by the number of free prices divisible by three. Exact enumeration of all 31 nonempty subsets yields unique maximum 32 for I={0}; all other subsets at most 31. For E0={219,...,314}, each residue mod3 occurs exactly 32 times. Taking s=1-q/omega,
\[
\prod_{p\in E0}(1-q^p)^{-1}=A_3s^{-32}(1+O(s)),
\]
because (1-omega)(1-omega^2)=3 and each divisible price p contributes (ps)^-1.

The finite local threshold polynomial H0,m obeys
\[
\sum_{m\ge1}H_{0,m}(\omega)z^m
=\frac{z}{1-z}\prod_{p=214}^{218}(1-z\omega^p)^{-1}
=\frac{z}{(1-z^3)^2}.
\]
Indeed residues 214..218 are (1,2,0,1,2) modulo3. Consequently H0,3k+1(omega)=k+1, with zero coefficients at m congruent 0 or 2. Conjugate partial fractions give
2(k+1)A3 Re(omega^-N) binom(N+31,31)+O_k(N^30),
proving the claim.

## New theorem B: m=2 and m=3

\[
\boxed{\begin{aligned}
F_2^{(3)}(N)&=\frac{A_3}{30!}N^{30}(432,-213,-219)_{N\bmod3}+O(N^{29}),\\
F_3^{(3)}(N)&=\frac{A_3}{30!}N^{30}(432,-219,-213)_{N\bmod3}+O(N^{29}).
\end{aligned}}
\]
These thresholds have zero order-32 coefficient but genuinely nonzero order-31 coefficients.

**Proof.** Let U={214,...,221}, a_j(n)=1{sum_{p in Sj}n_p<m}, and h(n)=max(a0+a1+a2-1,0). Define finite polynomials H1,m, H2,m, Hh,m by their q-weighted short-event or overlap sums. Write H01(m) for coefficient of s in H0,m(omega(1-s)). The respective order-31 free-factor ratios to A3 are
R1=657/(1-omega^2)=219(1-omega),
R2=657/(1-omega)=219(2+omega), Rh=657.
The full order-31 pole coefficient is A3 Qm, where
\[
Q_m=H_{01}(m)+R_1H_{1,m}(\omega)+R_2H_{2,m}(\omega)-657H_{h,m}(\omega).
\]

The exact finite calculations in Z[omega] are:

| m | H01 | H1(omega) | H2(omega) | Hh(omega) | Qm |
|---:|---|---|---|---|---|
|2|217+2omega|1+omega|-omega|1|217+2omega|
|3|215-2omega|0|0|0|215-2omega|

The overlap evaluations enumerate every vector in {0,...,m-1}^8 on U and retain the signed inclusion-exclusion multiplicity before taking root phases. Particularly Hh,2(omega)=1 (not merely the empty-vector weight). Both Qm are nonzero. For a+b omega, conjugate extraction yields
\[
2\Re((a+b\omega)\omega^{-N})=(2a-b,\ 2b-a,\ -a-b)_{N\bmod3}.
\]
This gives both displayed vectors. Pole orders at all other primitive d>=4 roots are at most 25 because P contains at most 25 multiples of any d>=4.

## Exact checks, residual interpretation and open questions

VERIFY_CUBE.py checks the original SHA-256, all 31 inclusion-exclusion subsets, the local Z[omega] dynamic program for m=1..120, independent direct compositions for m=1..4, and complete m=2,3 overlap domains of sizes 2^8 and 3^8. Exact integer cyclotomic arithmetic, no floats; RESULT_CUBE.json records the outcomes. PASS locally. No independent review or formalization.

The earlier q=-1 theorem establishes nonzero period-two content at N^47 for every m; the above establishes independent period-three content at N^31 for m=3k+1 and at N^30 for m=2,3. Hence the full quasi-polynomial, if represented through those orders, requires N mod 6 as its joint periodic label. This is a proven observer-fidelity requirement *inside the scalar R5 model* and no claim of BRC physical equivalence or algorithmic speedup.

Next: derive an m-generating function for Q_m on both missing residue classes and classify zeros; study primitive fifth roots and the minimal joint residual carrier for cost N and threshold m. Historical adaptive-eight-error bounds 8335 <= C8* <= 8343 unchanged.

Frozen predecessor: https://github.com/awdawmip/enterprise-math/blob/00fc3f2d975c2ab02bf90cc27f015500d47b1b13/research_notes/portable_direct/r5_rare_failure_n78_20261120/HIGH_DEGREE_48_THEOREM.md
Fourth-root predecessor: https://github.com/awdawmip/enterprise-math/blob/7cfbb6d24fdba1bb69daa9922d175221686a75b7/research_notes/portable_direct/r5_even_n20_period8_exact_20261121/RESEARCH.md
