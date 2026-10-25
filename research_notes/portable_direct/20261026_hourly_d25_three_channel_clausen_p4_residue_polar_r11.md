# D25/LIFT — Three-channel corrected-Clausen p^4 residues and full polar rank moments

2026-10-26. TASK_RESEARCH parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

**Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** External finite hypergeometric model, not original-class native CM experiment, Source research checkpoint, formal review or LIFT/JT2 proof.

## Inputs (consumed, not re-credited)

- Corrected Clausen parameter operator and exact rank/Hasse recurrence: research_notes/portable_direct/20261025_hourly_d25_clausen_operator_rank_boundary.md.
- Existing p^4 ordered signed low/high cutoff in corrected Hasse jets: research_notes/portable_direct/20261026_hourly_d25_corrected_clausen_jet_reflection_p4_bridge.md.
- Single-channel Toeplitz 0/1/infinity residue identity: research_notes/portable_direct/20261026_hourly_d25_toeplitz_infinity_compensation_r11.md.
- Middle-band unimodular high-polar inverse: research_notes/portable_direct/20261026_hourly_d25_unimodular_polar_rank_reconstruction_r11.md at 61883bacbd78cb9d0f5633958dfea3f33fc78898.

The new issue is to transport the *complete* p^4 corrected Hasse reflection, with three distinct jet channels, into rational endpoint/infinity observables, then distinguish the scalar observer from the quadratic rank operator's stronger source requirements.

## Exact source and carriers

For p=6m+1>=7 prime set

\[
u_{a,n}=[t^a]\frac{(-m-t)_n(-2m-2t)_n}{(1-p/2-3t)_n n!}
\]

in the p-local ring, reduced modulo p^2; all n<p denominators are p-units. For (a,b) in {(0,2),(1,2),(0,3)} set

\[
F_a(z)=\sum_{j=1}^{2m}2^{-j}u_{a,j}z^{-j},\quad
G_b(z)=\sum_{\ell=1}^{2m}2^\ell u_{b,p-\ell}z^\ell,\quad
H_{ab}=F_aG_b=\sum_{n=1-2m}^{2m-1}c_n^{ab}z^n.
\]

n=ell-j is *oriented*: the original signed cutoff retains n<=0. Define

\[
A_{ab}=H_{ab}(1),\quad B_{ab}=H'_{ab}(1),\quad
I^0_{ab}=\sum_{n>0}c_n^{ab},\quad
I^1_{ab}=\sum_{n>0}(6n-1)c_n^{ab},
\]

and U_ab=A_ab-I^0_ab, T_ab=A_ab-6B_ab+I^1_ab.

## Theorem A — two-kernel residue transfer (exact)

For any finite Laurent polynomial H over characteristic zero (and coefficientwise over the present p-local ring), with K0=1/(1-z), K1=(1+5z)/(1-z)^2,

\[
\boxed{\operatorname{Res}_0\frac{K_0(z)H(z)}z dz
=H(1)-\sum_{n>0}[z^n]H
=\sum_{n\le0}[z^n]H,}\tag{A0}
\]

\[
\boxed{\operatorname{Res}_0\frac{K_1(z)H(z)}z dz
=H(1)-6H'(1)+\sum_{n>0}(6n-1)[z^n]H
=\sum_{n\le0}(1-6n)[z^n]H.}\tag{A1}
\]

**Proof.** At zero the kernels are respectively sum z^r and sum (6r+1)z^r, r>=0. At z=1 the residues of K0 H/z and K1 H/z are -H(1) and 6H'(1)-H(1). At infinity K0=-sum_{r>=1}z^{-r}, K1=sum_{r>=1}(6r-1)z^{-r}; their infinity residues are +sum_{n>0}c_n and -sum_{n>0}(6n-1)c_n. Rational residue conservation yields (A0),(A1), keeping both independent infinity ports. This is also a purely formal Laurent-coefficient proof over the p-local ring. QED.

## Theorem B — full corrected p^4 three-channel reflection

With r_n=(1/6)_n(1/3)_n/[2^n(n!)^2] and the original **ordered** Q_p=sum_{0<=a,b<p;a+b>=p}(6(a+b)+1)r_ar_b, one has Q_p in p^2 Z_(p) and

\[
\boxed{\frac{Q_p}{p^2}\equiv\frac{2^{-p}}{18}
\left[T_{02}+p\left(6U_{02}-\frac{T_{12}+T_{03}}6\right)\right]\pmod{p^2}.}\tag{B1}
\]

Equivalently

\[
\boxed{\frac{Q_p}{p^2}\equiv\frac{2^{-p}}{18}\left[
A_{02}-6B_{02}+I^1_{02}
+p\left(6(A_{02}-I^0_{02})
-\frac{A_{12}-6B_{12}+I^1_{12}+A_{03}-6B_{03}+I^1_{03}}6\right)
\right]\pmod{p^2}.}\tag{B2}
\]

**Proof.** The already-established corrected-jet reflection is the sum over 1<=j<=2m,1<=ell<=j of 2^{-(j+p-ell)}/18 times

\[
(6(j-\ell)+1)u_{0,j}u_{2,p-\ell}
+p\left[6u_{0,j}u_{2,p-\ell}
-\frac{6(j-\ell)+1}{6}
(u_{1,j}u_{2,p-\ell}+u_{0,j}u_{3,p-\ell})\right].
\]

Putting n=ell-j, the scalar multiplier becomes 2^{-p}2^n and the affine signed weight becomes 1-6n. Group by n<=0 and apply (A0),(A1) to exactly the three independent Hasse channels. This is (B1), then (B2). In particular **no quadratic labelled-rank moment is needed for the isolated scalar p^4 reflection**. QED.

The upper ports are computable in O(m) ring operations per channel using prefix sums P_ell=sum_{j<ell}2^{-j}u_{a,j} and J_ell=sum_{j<ell}j 2^{-j}u_{a,j}, followed by

\[
I^0_{ab}=\sum_\ell 2^\ell u_{b,p-\ell}P_\ell,\quad
I^1_{ab}=\sum_\ell 2^\ell u_{b,p-\ell}[(6\ell-1)P_\ell-6J_\ell].\tag{B3}
\]

This operation count excludes the cost of generating u and arithmetic bit length.

## Theorem C — new full-support N=4m-1 unimodular high-polar inverse

The previous high-polar inverse covered only j=m+1,...,2m. Here j=1,...,2m is required. Let N=4m-1, n_r=1-2m+r for 0<=r<N and, for s=0,1,2, set

\[
X_r^{ab,s}=\sum_{\ell-j=n_r}j^s u_{a,j}u_{b,p-\ell},\qquad
\mathcal P_{ab,s}(z)=\frac{z^{4m}}{(1-2z)^{4m}}[(-\theta)^sF_a(z)]G_b(z),\quad \theta=z\,d/dz.
\]

With t=1-2z,

\[
\boxed{2^{4m}t^{4m}\mathcal P_{ab,s}(z(t))
=\sum_{r=0}^{N-1}X_r^{ab,s}(1-t)^{2m+1+r}.}\tag{C1}
\]

Its **N high poles** t^{-4m},...,t^{-2}, after multiplying coefficients by 2^{4m}, obey

\[
\boxed{\beta_k=(-1)^k\sum_{r=0}^{N-1}\binom{2m+1+r}{k}X_r\quad(0\le k<N).}\tag{C2}
\]

The integer inverse is

\[
\boxed{d_k=\sum_{h=0}^k\binom{2m+h}{h}\beta_{k-h},
\qquad X_r=(-1)^r\sum_{k=r}^{N-1}\binom{k}{r}d_k.}\tag{C3}
\]

The transform determinant is (-1)^{N(N-1)/2}, hence unit over every ring. **Proof:** a cell contributes j^s 2^{ell-j}z^{4m+ell-j}; z=(1-t)/2 cancels the 2-factor and produces 2^{-4m}(1-t)^{4m+ell-j}. The exponents are precisely 2m+1,...,6m-1. Coefficient extraction gives (C2). Consecutive binomial evaluations have Vandermonde determinant 1 before row signs. Divide the generating polynomial by (1-t)^{2m+1}, recover its degree-<N coefficients with (1-t)^{-2m-1}=sum_h binom(2m+h,h)t^h, then substitute t=1-y to obtain (C3). QED.

For s=0 this recovers the complete three Hasse channel diagonal mass arrays and thus (B1); s=1,2 supply source rank information needed for polynomial operator transport, without a prime-dependent linear-system solver.

## Theorem D — quadratic corrected operator needs second labelled-rank moment (sharp boundary)

The corrected rank/Hasse operator includes (r-1-m)(r-1-2m)=r²-(3m+2)r+(m+1)(2m+1). On a general labelled signed-cell carrier, mass and first-rank moments do not determine its action. For m>=3 use valid equal-difference cells (j,ell)=(m+1,1),(m+2,2),(m+3,3) with signed perturbations delta=(1,-2,1). Their n=ell-j=-m is identical and

\[
\boxed{\sum\delta=0,\quad \sum\delta j=0,\quad
\sum\delta(j+\ell)=0,\quad
\sum\delta j^2=\sum\delta(j-1-m)(j-1-2m)=2\ne0.}\tag{D1}
\]

Thus full rankwise quadratic operator preservation requires a degree-two observer on unrestricted labelled carriers, and (C3) with s=2 provides it. This witness **does not** assert that constrained one-parameter hypergeometric source families admit the synthetic cell perturbation. Nor does it create a false obstruction for the scalar reflection (B1), which needs s=0 only. Single quadratic action is covered; compositions may require higher moments. QED.

## Exact author checks and discriminatory example

The companion stdlib checker independently evaluates the original ordered Q_p mod p^4 from the unaltered r_n recurrence, corrected denominator/Hasse jets mod p^2, direct lower-triangle sums, three-channel residues, two independent infinity computations (direct and O(m) prefix), and full polar inverse including source moments s=0,1,2.

- 80 primes p=6m+1, 7<=p<=997: B1/B2, A0/A1, prefix infinity and original Q/p² all PASS.
- 22 primes p=6m+1, 7<=p<=211: all three channels times s=0,1,2 full-support polar inverses PASS.
- m=3 integer observer-fiber witness (D1) PASS.

At p=13: Q_13/169=104 mod169; residue bracket=26; prefactor 2^{-13}/18=121. Infinity ports (I^0_02,I^1_02,I^1_12,I^1_03)=(71,140,96,66) mod169. Deleting all upper ports gives the **wrong** 129 mod169 rather than 104. These are author exact checks, not independent review or native CM evidence.

## BRC, authority, next unresolved unit

**BRC COMPOSE_APPLIED:** population ordered pairs with rank, corrected parameter/Hasse channel, signed coefficients and p-adic precision; operations cutoff, shifted quadratic operator, convolution, infinity residue and polar inversion; observer compression to channel masses is proved safe only for the stated scalar, not quadratic future operations. Complex z is external algebra, not a native P000 plane; no invented six-dimensional interpretation.

**Next exact science action:** transport the *shifted* corrected rank/Hasse recurrence through s=2 full polar moments, retaining source rank endpoint and both orientations; seek a genuine coupled WZ/adjoint cancellation that improves on the residue re-expression. Original-class CM H0/B0, divided-power [X]U mod p², native Frobenius direction/eta, kappa and Delta_p-R_p are still missing; independent review remains pending. D25/LIFT/JT2 remains OPEN.

Current ordinary Research-lane logical conversation: chatgpt-research-hourly-enterprise-math-20260923 (distinct from maintenance lane). The fresh 2026-10-26 recovery/continuation read reports own prior service session but no authorized run, and a preserved native checkpoint. The current Source task still has latest historic claim MCP-d0d70cd041b01e5db192870a versus checkpoint expected predecessor MCP-87631b892b41fa18d799f2d8; control support #1558. This portable note makes no native CLAIM/OPEN/checkpoint or mathematical admission claim.