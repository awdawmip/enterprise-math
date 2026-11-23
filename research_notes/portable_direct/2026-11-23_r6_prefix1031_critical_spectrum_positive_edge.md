# PREFIX-1031 — Critical-spectrum classification and an unconditional positive-edge wedge for the signed X6 port-contrast observer

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1030. Status: AUTHOR_ANALYTIC_PROOF / LOCAL_SIGN_PROVED / NOT_REVIEWED.

## Scope and frozen provenance

Frozen scientific input is enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5). The Stage46 signed BRC candidate W=J12-6I12, incoming -e1, the forbidden bidirectional Link {0,e1}, exactly one negative outgoing step, and the original joint Cell/terminal-port/grade coherent square-mass observer are unchanged. This is a theorem **about the already derived Laurent spectral observer**, not a claim that a phase torus is native physical space or that its scalar spectrum preserves the full signed BRC state. No new native propagation or classical reference computation is performed.

Reuse the verified PREFIX-1026 exact functional (written here with x as a scalar spectral variable):

5 nu[f] = -4 mu[H f'] - 2 mu[P f] + 12 integral_(t in [0,36]) (6-t) (integral_0^t (11+x) f(x) dx) mu(dt),

where H(x)=x^2(36-x)^2, P(x)=x(x-36)(17x-91), and mu is the normalized Haar pushforward of L=|z1+...+z6|^2. The contrast moments are nu[x^m]=a_m for integer m>=1, with the algebraic extension a_0=2412. The predecessor's local formula, when mu has a smooth density rho, is

5 g(x)=4(H(x)rho(x))' - 2P(x)rho(x) + 12(11+x) F(x),
F(x)=integral_[x,36] (6-t) mu(dt).

All names and coefficients in the functional are fixed inherited BRC-observer identities; the present work checks their **new geometric and sign consequences** symbolically.

## Theorem 1: exact critical levels and all nonzero-level Hessians

Use only the rotational invariance of the auxiliary Laurent spectrum to fix z6=1 and write z_j=exp(i theta_j) for j=1,...,5; these angles are an auxiliary parametrization of a five-dimensional compact phase torus, not X6 native spatial angles. The critical values of the real analytic function L on this torus are **exactly**:

{0,4,16,36}.

At a critical point where L>0 every z_j equals +1 or -1 in this gauge. The numbers of such critical points are 15 at L=4, six at L=16, and one at L=36. All 22 points are nondegenerate. Their Morse indices (number of negative Hessian eigenvalues) are 3, 4, and 5, respectively. The level L=0 is a separate critical set, and includes ten collinear zero-sum sign configurations.

**Proof.** Write S=sum_j z_j. The full six-phase first derivatives are -2 Im(z_j conjugate(S)). The sum of these six derivatives is zero, so vanishing of the five gauge derivatives implies vanishing of the sixth. When S!=0, every z_j is parallel or antiparallel to S. Since z6=1, S is real and all z_j belong to {+1,-1}. Thus S is one of +-2, +-4, +-6 (or 0), giving L=S^2 in {0,4,16,36}; all those values are realized.

For a nonzero collinear S=s=sum_{j=1}^6 a_j, with a6=1 and a_j in {+-1}, the exact second-order expansion is

L(theta)=s^2 + theta^T M theta + O(||theta||^3),
M=aa^T-s diag(a), a=(a1,...,a5)^T.

The determinant lemma gives det(M)= -s^4 product_{j=1}^5 a_j, which is nonzero when s!=0. At a configuration with p positive and q=6-p negative signs, the relative rotation between the two sign blocks has positive quadratic coefficient, directions internal to the larger block are negative, and directions internal to the smaller block are positive. Hence the Morse index is max(p,q)-1. This is 3 for |s|=2, 4 for |s|=4 and 5 for |s|=6. There are 2^5=32 collinear sign configurations in the z6=1 gauge; by elementary binomial counting, 15 have |s|=2, 6 have |s|=4, 1 has |s|=6, and the remaining 10 have s=0. Every configuration with S=0 is critical because L=|S|^2. QED.

**Regularity consequence.** At every value in the open bands (0,4), (4,16), and (16,36), L is a submersion on its compact level set. Local smooth coordinates and a partition of unity therefore give a C-infinity density rho for mu on each of these three bands. Moreover mu has no point masses: the critical set is contained in the zero set of the nonconstant real analytic function |S|^2 together with finitely many isolated sign configurations, all of Haar measure zero; on the complementary regular set the coarea formula gives absolute continuity. At L=4 and L=16 the isolated nondegenerate critical points can be analyzed via the five-variable Morse normal form. The results above make the C1/local-singularity analysis there a finite, explicit task, rather than an unclassified spectral obstruction.

## Theorem 2: strict positive density at the spectral ceiling

There are constants c>0 and epsilon>0 such that on the already established smooth upper band, with u=36-y -> 0+,

rho(36-u) = c u^(3/2) + O(u^(5/2)),
d rho(y)/dy at y=36-u = -(3/2)c u^(1/2) + O(u^(3/2)),

and

**g(36-u)=2520 c u^(5/2) + O(u^(7/2))**.

Consequently **g(y)>0 for every y in (36-epsilon,36)**. This is an unconditional local-sign statement *within the frozen Laurent observer*, independent of the still-open global sign problem on the other bands.

**Proof of rho expansion.** The sole maximizer of L is z1=...=z6=1, hence theta=0 after gauge. At that point the quadratic expansion is

36-L(theta)=theta^T(6I5-11^T)theta+O(||theta||^3).

The symmetric matrix 6I5-11^T has eigenvalues 1 (once) and 6 (four times), so the maximum is strictly nondegenerate. The smooth Morse change of variables gives exactly 36-L=||v||^2 near the maximizer with a smooth, strictly positive transformed Haar density A(v). Integrating over the radius ||v||=sqrt(u), its spherical average is A(0)+O(u): odd first-order terms vanish after spherical averaging. The radial Jacobian in five variables is proportional to u^(5/2-1)=u^(3/2). Hence rho(36-u)=c u^(3/2)(1+O(u)), where c>0, and differentiating the smooth radial-average expansion yields the stated derivative. All Haar normalization constants are absorbed into c; no numerical phase/trigonometric or pi calculation is needed.

**Proof of g expansion.** Substitute y=36-u into the inherited exact spectral polynomials. First,

H(y)rho(y)=1296 c u^(7/2)+O(u^(9/2)),

so 4(H rho)'=-18144 c u^(5/2)+O(u^(7/2)). Next,

P(36-u)= -18756 u+O(u^2),

so -2P rho=37512 c u^(5/2)+O(u^(7/2)). Finally,

F(36-u)=integral_0^u (-30+v) rho(36-v) dv
         = -12 c u^(5/2)+O(u^(7/2)),

so 12(11+y)F(y)=-6768 c u^(5/2)+O(u^(7/2)). Sum and divide by five:

(-18144+37512-6768)c/5 = 2520 c.

The leading coefficient is strictly positive. QED.

## Corollary 3: a proved two-parameter Hausdorff-positive wedge

Set E_(m,k)=nu[y^m(36-y)^k] and n=m+k. There exists t0<1 such that, for every fixed t in (t0,1) and every sequence of nonnegative integers (m,k) with n->infinity and m/n->t,

**E_(m,k)>0 eventually**.

More strongly, for every compact K contained in (t0,1), there is N(K) such that E_(m,k)>0 whenever n>=N(K) and m/n belongs to K.

**Proof.** Choose t0 so that 36t0>36-epsilon. By Theorem 2, the signed functional nu has smooth, strictly positive density g near each y=36t for t in (t0,1). PREFIX-1030's exact normalized Bernstein localization then gives

D_(m,k) = (n+1) binom(n,m) E_(m,k) / 36^(n+1)
        -> g(36t)>0.

The contribution of the remaining compactly supported finite-order distribution is exponentially suppressed away from the Beta concentration point, including any spectral critical levels. On compact K the concentration and the positive minimum of g are uniform. Since the normalizing factor is positive, the claims follow. QED.

This proves **simultaneous growth m,k->infinity with a positive limiting ratio k/m sufficiently small**, which the fixed-index corner results PREFIX-1027 did not cover. No computable value of t0 or N(K) is claimed; finding explicit interval bounds remains research work.

## Reproducibility and independent checks

This is a pure symbolic proof, with no new scientific numerical experiment and no claimed runnable-code certificate. Its independently checkable inputs are:
1. The frozen Laurent moment representation and exact polynomial spectral functional in PREFIX-1026 and PREFIX-1030;
2. The five-variable derivative and quadratic Hessian computation in Theorem 1;
3. The nondegenerate maximum and five-dimensional radial Jacobian;
4. The three rational-polynomial leading coefficients -18144, +37512, -6768, summing to +12600 before division by 5;
5. The inherited positive-kernel localization from PREFIX-1030.

The new local asymptotic exponent 5/2 for g is consistent with the previously derived moment exponent 7/2 for the contrast a_m (PREFIX-1025), furnishing an analytic crosscheck. This is author reasoning, not an independent referee or formal proof-checker acceptance.

## Open questions and next discriminating work

1. Establish a rigorous signed-density representation across the two interior critical levels y=4,16, including the correct local Morse contributions and any boundary term at y=0. In particular, determine whether nu has a globally L1 density without distributional singular parts.
2. Produce explicit interval arithmetic or source-typed BRC-observer bounds on g(y) over (16,36), then (4,16) and (0,4), respecting the frozen signed observer and avoiding non-BRC native reference computations. A verified negative point would produce a genuine high-order counterexample; all-positive bounds would advance the global Hausdorff problem.
3. Obtain an effective t0 or certified N(K), beyond the existential wedge proved here.

Original parent objective B_fix,odd(32) in {19,20} stays open. Preserve previous scientific publications PREFIX-1026..1030, historical contributor identifiers EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056, and original SID MCP-45ad6d29cd534c1aad25595a72e3c532 as provenance only. This independent portable proof does not assert a formal CLAIM, PROGRESS, Result/Review, activity linkage or P000 change.
