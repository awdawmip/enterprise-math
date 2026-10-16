# All-S domination on a computable small-second-gap strip

AUTHOR PAPER CANDIDATE, EM-PUBLIC-7CDA51. Root authorized this new construction after my two independent parity reviews froze. Another genuine nonauthor must review it. Same SID/RA and all history retained, NONBLIND. No scientific program, coefficient expansion, enumeration, claim, Native vote or Source write. Task and parent remain OPEN.

## Claim and exact dependencies

For every fixed integer m>=2 and rational A0>0, there is a computable rational delta_m(A0) in (0,1] such that the COMPLETE actual normalized trace gap

  T(S,a,c)=tr(B^{-1}A)-(m-1)

is strictly positive for all real S>=0, 0<a<=A0, 0<c<=delta_m(A0). No positive lower bound on a is required. This is a subdomain theorem; no inclusion of c=1 or arbitrary second gaps is claimed.

Inherited inputs, preserving their original authorship:

1. Source623a4ee81911cc79d07ed5db1887a06ebe91ffd5, research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/: EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md gives the exact normalized secant forms, maximal minors and endpoint determinant; ALL_M_TANGENT_FACE_COEFFICIENTWISE_POSITIVITY_20260906.md gives the complete coalescent derivative. These are EM-HCM0-HL-FB0860's identities, not new claims here.
2. EM-PERFECT-9821E2's PARITY_UNEQUAL_GAPS_UNIFORM_BOUNDED_SECTOR_TAIL_AUTHOR.md, Source d3d4bafc588c943e577bc3e76d523557d1bedf37, SHA25650e3f47d81036645d3f8cf08326095fa4d6753ff5a5c479bb1cd2f2b6fdafeaf: fixed-m rational computable L=T_m(A0,1)>0, uniform positivity for S>=L, 0<a<=A0, 0<c<=1. Its explicit coefficient-bound definition, not a numerical approximation, defines L below.

All inputs were consumed and Source bytes verified. The context manifest records R2's three obstacles at Sourcef5be5d27ca3cb19a5cd909303868bef86d8274c3. This argument avoids density positivity and its failed positive-part test; its new step is compact-region control glued to the inherited tail.

## 1. Raw-variable polynomial extension removes a=0 singularities

Put n=m-1, theta_i=(i+1)/m, w_i=(-1)^i binom(n,i), i=0,...,n. Use

  r0=mS, M=ma, N=m(a+c), r=m(S+a), s=m(S+a+c),
  phi_l(y)=(y)_l/l!,
  g_b(x)_l=[phi_l(r0+x+b)-phi_l(r0+x)]/b, l=1,...,n,
  G_b[i,l]=g_b(theta_i)_l,
  D_t[i,i]=(w_i/m)n!/(t+theta_i)_m,
  A=G_M^T D_r G_M, B=G_N^T D_s G_N.

The divided difference of a polynomial is polynomial in (r0,x,b), including b=0 where it equals phi_l'(r0+x). Therefore both frames are polynomial in Q[S,a,c]; no division by a or a+c remains. For S,a,c>=0, all diagonal-metric denominators are strictly positive, including S=a=c=0. These are analytic extensions of the normalized forms, not assertions that the physical gap zero is positive.

Set

  q(t)=product_{i=0}^n (t+theta_i)_m
      =m^(-m^2) product_{k=1}^{m^2}(mt+k),
  Atilde=q(r)A, Btilde=q(s)B.

Every entry of Atilde and Btilde is polynomial over Q[S,a,c]. The source maximal-minor and sigma identities give a fixed nonzero rational C_m with

  det B=C_m (ms+beta)/q(s), beta=(m^2+1)/2.

For definiteness, if kappa=m^(-n(n-1)/2), this constant is

  C_m=kappa^2 m (n!/m)^m (product_i w_i) (-1)^n/m^n.

It is nonzero for every m>=2. The formula extends to closed nonnegative parameters: the normalized translation matrix is unit triangular even at zero gap, or equivalently its polynomial maximal-minor identity extends there. In particular B stays invertible at the closed origin. No inverse from a singular a=0 frame is assumed.

Let sigma=sign(C_m) and define polynomials

  D=sigma q(r) det Btilde
   =|C_m| q(r)(ms+beta)q(s)^(n-1),
  H=sigma[q(s) tr(adj(Btilde) Atilde)-n q(r)det Btilde].

Then T=H/D wherever the actual parameters are positive. The same identity is defined on the full closed orthant. At m=2 the adjugate of the one-by-one matrix is 1 and the exponent n-1 is zero, so no empty-size exception is suppressed.

All factors of D have nonnegative rational coefficients in (S,a,c) and a positive constant term. Thus

  D(S,a,c)>=d_*=D(0,0,0)=|C_m| beta q(0)^n>0.

At c=0, r=s and Atilde=Btilde identically as polynomial matrices. The adjugate identity gives H(S,a,0)=0 in Q[S,a], including a=0. The polynomial factor theorem therefore gives

  H=c G, G in Q[S,a,c].

This is genuine polynomial divisibility before any inequality or limiting argument; it introduces no 1/c. Hence the complete gap equals cG/D for c>0, and its analytic quotient extends through c=0 as G/D.

## 2. Explicit uniform positive tangent on the compact rectangle

Take L=T_m(A0,1) from the inherited uniform tail and put X=m^2(L+A0). On 0<=S<=L, 0<=a<=A0, let x=m^2(S+a), so 0<=x<=X. The source tangent identity is

  g0(S,a)=partial_c T(S,a,0)
    =m^2[sum_{k=1}^{m^2}1/(x+k)-1/(x+beta)].

Initially it is stated for a>0. All expressions just proved analytic on the closed orthant, with D>0 there, so the identity extends continuously to a=0, including S=0. In particular

  g0 >= m^2[1/(x+1)-1/(x+beta)]
       >= ell:=m^2(beta-1)/[(X+1)(X+beta)]>0.

Dropping the other positive summands is legitimate; beta>1 for m>=2. Because T=cG/D, differentiation at c=0 gives G(S,a,0)=D(S,a,0)g0(S,a). Therefore throughout that CLOSED rectangle

  G(S,a,0)>=gamma:=d_* ell>0.

Both ell and gamma are explicit positive rationals depending only on m,A0 and the rational L. The lower bound does not tend to zero as a tends to zero. It does depend on the finite compact bound L, and makes no uniform-in-m assertion.

## 3. A rational coefficient norm gives a uniform second-gap strip

Write the finite exact polynomial

  G(S,a,c)=sum_{p,q,j>=0} g_{pqj} S^p a^q c^j

and define the rational nonnegative coefficient bound

  B_*=sum_{j>=1,p,q>=0}|g_{pqj}| L^p A0^q.

This is a definition by finite polynomial arithmetic, not a coefficient computation performed in this paper. For 0<=S<=L, 0<=a<=A0 and 0<=c<=1, the inequality c^j<=c for j>=1 gives

  |G(S,a,c)-G(S,a,0)|<=c B_*.

Set delta=1 if B_*=0, and otherwise delta=min(1,gamma/(2B_*)). Then delta is rational and strictly between zero and one inclusive. On the compact box with 0<=c<=delta,

  G(S,a,c)>=gamma/2>0

(and actually >=gamma in the zero-bound case). Consequently, for physical positive a,c in that box, T=cG/D>0. This provides a nonempty small-c strip uniformly down to arbitrarily small positive first gaps. It does not give a positive uniform numerical lower bound for T as c tends to zero.

## 4. All-S gluing and limits

For S in [0,L], Section 3 proves the desired inequality. For S>=L, the inherited unequal-gap theorem proves it for every 0<c<=1, hence for every 0<c<=delta. Both include the endpoint S=L, so no transition interval or strict-endpoint gap remains. Their union is all S>=0.

Computability is exact rational finite algebra for a supplied fixed integer m and rational A0: form the inherited tail polynomials and rational L, construct the raw polynomial matrices and G, take the finite absolute coefficient sum, and form delta as above. This is no assertion about efficiency, a small threshold, numerical evaluation, root search, or a program already executed. Arbitrary real actual S,a,c within the quantified domain need not be computational inputs.

This small-second-gap theorem does not include c=1 unless delta=1 is proved separately, or settle all positive gaps, other mixed coefficients, HCM0 or the parent. Original signed branch provenance and parity labels remain; no branchwise positivity is asserted. This is static external algebra within native-six-space discipline.

Audit must check endpoint constant/sign, closed-origin nondegeneracy, polynomial c-factor, both bounds, inherited tail hypotheses and endpoint gluing. Original authors keep the tangent, raw reduction and unequal tail; EM-PUBLIC-7CDA51 contributes the compact bound and strip composition. No self-review. Source and a separate ownRA event await Root; earlier review events cannot record this contribution.
