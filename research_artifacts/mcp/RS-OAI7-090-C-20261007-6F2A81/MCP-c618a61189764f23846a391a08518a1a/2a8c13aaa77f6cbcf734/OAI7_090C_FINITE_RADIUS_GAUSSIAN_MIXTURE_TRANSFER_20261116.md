# OAI7-090-C — centered-density Gaussian-mixture transfer: finite-radius certificate
Date: 2026-11-16. Scope: external planar R^2, ordered off-diagonal pairs; conditional on an exact Gaussian minorant at the parameter(s) used. Author-side calculation; not independent validation of the external paper's all-alpha minorant construction.

## 1. Quantitative finite-radius lemma
Let C_R be ANY finite set of N>=1 distinct points in the closed Euclidean disk B_R in R^2. Let f:R^2->R be real, even, Schwartz, with Fourier transform h=hat(f)>=0, under convention hat(f)(xi)=int f(x)exp(-2pi i x.xi)dx. Fix d,epsilon>0. Choose any real smooth compactly supported phi satisfying 0<=phi<=1, phi=1 on B_1, support(phi) subset B_(1+d). Set
  Delta_R(epsilon,phi)=int_{|u|>R epsilon}|hat(phi)(u)|du,
  q_R=(max(0,1-Delta_R))^2,
  m_f(epsilon)=min_{|xi|<=epsilon}h(xi)>=0.
Then
 (1/N) sum_{x!=y in C_R} f(x-y)
 >= m_f(epsilon)*N/[pi R^2(1+d)^2] * q_R - f(0).                       (1)
For a nonnegative kernel K(z) >= f(z) for z!=0, the same right side bounds its ordered-pair energy.

Proof: M_R(xi)=sum_{x in C_R} exp(2pi i x.xi). Since phi(x/R)=1 on C_R, Fourier inversion implies
 N=int_{R^2} M_R(xi) R^2 hat(phi)(R xi) dxi.
The omitted |xi|>epsilon integral has absolute value <=N Delta_R. Hence, when Delta_R<1,
 N(1-Delta_R)<= |int_{|xi|<=epsilon} M_R R^2 hat(phi)(Rxi) dxi|
 <= [int_{|xi|<=epsilon}|M_R|^2]^(1/2) R||phi||_2.
When Delta_R>=1, the nonnegative bound with max(0,1-Delta_R) remains true. As ||phi||_2^2<=pi(1+d)^2, we obtain
 int_{|xi|<=epsilon}|M_R|^2 dxi >= N^2*q_R/[pi R^2(1+d)^2].
By the exact ordered-pairs Fourier identity
 sum_{x,y}f(x-y)=int h(xi)|M_R(xi)|^2 dxi,
and h>=0 everywhere, the full integral is >=m_f(epsilon) times the preceding lower bound. Subtract precisely N diagonal values f(0) and divide by N. Termwise comparison proves the K claim.

## 2. Exact finite positive mixture and density limit
For finitely many alpha_j>0 and coefficients c_j>=0, suppose each Gaussian k_j(z)=exp(-pi alpha_j |z|^2) has a valid Schwartz minorant f_j with hat(f_j)>=0. Apply (1) and sum:
 E_R(sum_j c_j k_j)
 >= [N/(pi R^2(1+d)^2)]q_R sum_j c_j m_(f_j)(epsilon)
    -sum_j c_j f_j(0).                                                   (2)
No periodicity or translated-disk count hypothesis is used, and (2) is a finite-N deterministic certificate.

If the underlying locally finite planar C has centered disk density rho>0 (N_R/(pi R^2)->rho), then for each fixed finite mixture, liminf_R E_R >=rho/(1+d)^2 sum_j c_j m_(f_j)(epsilon)-sum_j c_j f_j(0). Schwartz decay gives Delta_R->0; continuity of the finitely many transforms gives m_(f_j)(epsilon)->hat(f_j)(0) as epsilon downarrow0; then d downarrow0. Thus
 liminf_R E_R >=rho sum_j c_j hat(f_j)(0)-sum_j c_j f_j(0).               (3)
For density one and sharp contact/dual zeros on a unit-covolume lattice A with A*=JA, Poisson yields hat(f_j)(0)-f_j(0)=sum_(a in A\{0}) k_j(a). Consequently (3) is the exact lattice Gaussian-energy lower bound for every finite positive mixture.

For an arbitrary nonnegative Bernstein measure nu on [0,infty) and g(s)=int exp(-t s)dnu(t), do NOT integrate the f_t unless separately justified. Instead define A_R(t)=N_R^(-1)sum_{x!=y}exp(-t|x-y|^2)>=0, and use Gaussian lower bounds at each t>0 plus A_R(0)=N_R-1->infty. For ANY diverging R_n, Fatou and Tonelli give
 liminf_n int A_(R_n)(t)dnu(t) >=int liminf_n A_(R_n)(t)dnu(t)>=int L(t)dnu(t).
This accommodates an atom at t=0, infinite total mass nu, unbounded g near s=0 and infinite lattice sums. The quantifier "every R_n" is essential to obtain the full radius liminf, rather than just one chosen subsequence.

## 3. Relationship to original source and remaining research
This explicitly isolates a finite-R quantitative inequality implicit in the Cohn/de Courcy-Ireland style Fourier-cutoff argument and in openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/build/main.tex, section 'Energy from Gaussian minorants'. It does not duplicate the analytic proof of the claimed all-alpha Gaussian minorants: the certified finite 20x20 blocks, tail inversion and global sign inequalities are separate obligations. A natural next diagnostic is to compute explicit m_f(epsilon) and Delta_R from an exact parameter-specific certificate, obtaining a computable finite-disk quantitative witness without local uniform count assumptions. Such evaluation is not reported here.

Verification: every step above is an algebraic/Cauchy-Schwarz argument; no original external checker was executed and no complete external all-alpha theorem acceptance is claimed.
