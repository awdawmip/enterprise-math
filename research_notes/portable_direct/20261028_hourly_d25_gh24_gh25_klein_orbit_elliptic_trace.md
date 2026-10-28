# D25/LIFT GH-24 / GH-25 — weighted Klein-four source transport and the non-CM elliptic orbit carrier

2026-10-28. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. These are author-side auxiliary finite-field results, not native Source checkpoint/CLAIM, independently reviewed Results, or original W/S/Hasse claims. Predecessors: GH-17–19 and GH-22/23. TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN. Scientific frozen source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## GH-24 (theorem): exact weighted Klein-four transport

Let p=8m+3>=11 be prime, k=2m+1=(p+1)/4, and chi the quadratic character of F_p. Define the source population U=F_p\{0,-1,-1/9}, with labeled weight
\[
h(x)=\chi(x)[x(1+x)]^{3m+1}(1+9x)^m,\quad
\phi(x)=\frac{1+9x}{9x(1+x)}.
\]
GH-22 establishes D_m F_m(9)=-sum_{x in F_p} h(x) with D_m=binom(3m+1,m), a p-unit. Since m>=1, h is zero at all three excluded affine points.

The nonidentity elements of the actual V4 stabilizer of the four marked points {0,-1,-1/9,infinity} are
\[
A(x)=-\frac{1+x}{1+9x},\quad B(x)=\frac1{9x},\quad
C(x)=-\frac{1+9x}{9(1+x)}=A(B(x)).
\]
They preserve U, commute, square to identity, and satisfy phi(Ax)=phi(x), phi(Bx)=phi(x)^{-1}. The exact pointwise laws on U are
\[
\boxed{h(Ax)=-\chi(\phi(x))h(x),\quad
h(Bx)=\phi(x)^k h(x),\quad
h(Cx)=-\phi(x)^{-2m}h(x)
=-\chi(\phi(x))\phi(x)^k h(x).}
\tag{GH-24a}
\]
Consequently the exact signed finite moment has a *source-aware group projector*
\[
\boxed{\sum_{x\in F_p}h(x)=\frac14\sum_{x\in U}
h(x)(1-\chi(\phi(x)))(1+\phi(x)^k).}\tag{GH-24b}
\]
On a free orbit O={x,Ax,Bx,Cx}, its signed contribution is precisely
\[
\boxed{\sum_{y\in O}h(y)=h(x)(1-\chi(\phi(x)))(1+\phi(x)^k).}\tag{GH-24c}
\]
All chi(phi)=+1 free orbits therefore cancel; chi(phi)=-1 free orbits retain the nontrivial coefficient 2 h(x)(1+phi(x)^k). **The surviving orbits need not separately sum to zero.**

Proof. Direct algebra verifies the V4 relations, quotient laws, and preservation of U. Substitute A and B into h. The identities 4m+1=(p-1)/2, 8m+2=p-1, Euler's criterion chi(2)=-1 for p=3(mod 8), and x^(p-1)=1 on U yield the A and B multipliers. The C multiplier is their product since chi(phi(Bx))=chi(phi(x)), and phi^(4m+1)=chi(phi), phi^(8m+2)=1. Sum h under each of the four permutations of U, divide by 4, and factor the result as (1-chi(phi))(1+phi^k). This group averaging is valid also at fixed points; the free-orbit expression applies only where the orbit is truly free. QED.

**Port/boundary caveat (GH-22 G channel).** h_G(x)=chi(x)[x(1+x)]^(3m+1)(1+9x)^(m-1)(5-9x). For m>=2 the three excluded points also contribute zero. At the edge p=11,m=1, x=-1/9=6 has h_G(6)=3(mod11); hence sum_Fp h_G=sum_U h_G+3. A U-only G orbit argument would be false at this edge.

## GH-25 (theorem): exact elliptic orbit count and no direct CM

Define E/Q: y^2=x(x+1)(9x+1), nonsingular with good reduction for p>3. Its finite-field trace is
\[
\tau_p=p+1-\#E(F_p)=-\sum_{x\in F_p}\chi(x(x+1)(9x+1)).
\]
E has three distinct rational order-two points (0,0), (-1,0), (-1/9,0). The rational point P=(1/3,4/3) doubles to (0,0): substituting its tangent y=4x gives
\[
(4x)^2-x(x+1)(9x+1)=-x(3x-1)^2.
\]
Together P and (-1,0) generate a subgroup of order eight. Therefore for every p>3,
\[
\boxed{8\mid\#E(F_p),\qquad \tau_p\equiv p+1\pmod8.}\tag{GH-25a}
\]

For p=8m+3>=11, A has two fixed points from 9x^2+2x+1=0 (discriminant -32, chi(-2)=1); B has two fixed points x=+/-1/3; and C has none (discriminant 288, chi(2)=-1). Consequently there are precisely two orbits of size two, one A-fixed/B-transposed and one B-fixed/A-transposed, and 2m-1 free orbits. The A-fixed pair has chi(phi)=-1. On the B-fixed pair phi=1, so its total signed F-source contribution is zero. The sign chi(phi) is constant along all orbits and
\[
\chi(\phi(x))=\chi(x(x+1)(9x+1)),
\]
because their ratio is the square [3x(x+1)]^(-2). Hence the nonsquare fiber contains (p-3+tau_p)/2 members, two A-fixed. The exact number of **free nonsquare fibers/orbits** is
\[
\boxed{N_p=(p-7+\tau_p)/8.}\tag{GH-25b}
\]
This is an integer, consistently with tau_p=4(mod8). It counts candidate surviving orbits, not guaranteed nonzero group-summed residues.

Finally, over Qbar, E is Legendre with lambda=1/9; its characteristic-zero j-invariant is exactly
\[
\boxed{j(E)=256\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}
=\frac{4\cdot73^3}{81}=\frac{1556068}{81}\notin\mathbb Z.}\tag{GH-25c}
\]
A characteristic-zero CM elliptic j is an algebraic integer, while a rational algebraic integer must be an integer. Therefore this exact E/Q, and every characteristic-zero elliptic curve isogenous to it over Qbar, is **non-CM**. This excludes only a direct CM-isogeny interpretation of this *specific* carrier. It does not exclude characteristic-p Frobenius coincidences, a different curve on a higher cover, or prime-dependent WZ certificates. Classical background: G. Megyesi, The j-invariant of an elliptic curve (https://personalpages.manchester.ac.uk/staff/gabor.megyesi/teaching/math32062/j-inv.pdf); CM singular-modulus integrality (https://www.math.columbia.edu/~calebji/CM-Final.pdf). No novelty is claimed for the classical torsion/group/CM principles themselves.

## Explicit p=19 counterexample to orbitwise cancellation

For p=19, m=2, tau=4, N_19=2. The A-fixed size-two orbit {7,16} has sum 12 (mod19). The two active free orbits {3,8,12,14} and {4,5,9,11} have sums 17 and 9. The B-fixed orbit {6,13} and the chi(phi)=+1 free orbit have sum zero. Hence the *global* F source sum is 12+17+9=38=0 (mod19) even though all three surviving orbit sums are individually nonzero. A proof of the global F-branch vanishing cannot silently upgrade the V4 projector to orbitwise zero.

## Evidence and BRC/continuation

The companion pure Python standard-library checker exhaustively verifies all group transformations for all points, enumerates orbit weights and counts, computes the full E(F_p) point counts, and cross-checks the independent GH-19 integer binomial coefficient expressions for both GH-22 F/G moments, including the p=11 boundary. It passed for all 76 p<2000 with p=3(mod8). This finite validation does not prove the universal statement; the above algebra does.

Typed BRC: REUSE_APPLIED exact GH-22 finite character carrier, COMPOSE_APPLIED the quotient/fiber/elliptic trace observer. Retain the signed, labeled x-source, p,m, phi, chi(phi), F/G port, all V4 orbit identities and the three genuine omitted boundary points. This is signed modular cancellation, NOT positive branch mass; no claim about complete native X6 or original six Hasse W/S source identities.

**Next exact unit:** derive a weighted quotient sum on phi with its two genuine A-fixed branch points; prove or refute the *remaining* free-orbit sum for all p=19(mod24), not by assuming E has CM or using GH-23's excluded order-3 base symmetry. Re-enter GH-15 Laurent B_0 correction and GH-20/21 next-digit source moments only after honest F-branch progress. Original H0/B0, [X]U mod p^2, Frobenius eta/kappa, R23/R36 finite Green, native p=373 and independent Driver remain OPEN.

Control: gateway v0.6.11 local Site read at 2026-10-28 08:18+08 shows research_authority_granted=false and write_relay_enabled=false. One typed read-only continuation request returned INVALID_ARGUMENT / CONTROL_QUOTA. No native winning claim, open, formal checkpoint or independent mathematical admission is claimed. Existing support tracker enterprise-math#1558; preserve old sessions/staging and frozen source. The connected GitHub file, if published, is portable author evidence only. Existing hourly task schedule and notifications unchanged.