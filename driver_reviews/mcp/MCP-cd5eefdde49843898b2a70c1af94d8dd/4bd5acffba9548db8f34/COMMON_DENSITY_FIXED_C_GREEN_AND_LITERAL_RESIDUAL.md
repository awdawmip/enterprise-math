# Independent common density, fixed-C Green boundary, and literal residual

Status: ONE BOUNDED LOCAL DENSITY UNIT / FINITE DENSITY AND GREEN LEMMAS
PROVED / ORIGINAL SCALAR COMPARISON OPEN. Prepared 2026-10-12 UTC. This
independent-check directory alone is written. No prime, scalar fit,
old-checker execution, old rational-ansatz search, Source fetch or native
mutation occurs. The fixed F_CM, C, OLD-R and tau remain independent.

## 1. Literal reciprocal endpoint and common moment density

Retain p=6m+1 in the frozen classes, m>=2, N=3m, and precisely
h_0=h_N=g=binom(3m,m), sum h=1. This g is the unit V(1), not the older
p-adic memo's f_p(1/2). For the literal weighted reciprocal kernel,

    eta_N=(1/2)_N(N-1)!/[36(2/3)_N(5/6)_N].

Wilson and 4^N=1 give (1/2)_N=-1/N!. Complementary factorials give

    (2/3)_N(5/6)_N=(5m)!(4m)!/[(2m)!m!]=-g^2.

The last equality uses (5m)!m!=(-1)^(m+1),
(4m)!(2m)!=-1, and (N!)^2=(-1)^(m+1). Every factorial argument is
strictly below p. Therefore the fixed normalization is

    BOX: eta_N=-1/(18g^2), e_(N-1)=-9g^2/20.              (1)

The second value follows from the separately fixed eta_N e_(N-1)=1/40.
Neither endpoint is chosen from F_CM or the target.

Write A(z)=sum_(i=0)^m a_i z^i with the unchanged a_i, and
S_k=sum_(i=0)^k a_i. Set P(z)=sum_(k=0)^(m-1)S_k z^k. The exact finite
coefficient identity, including the top term, is

    (1-z)P(z)=A(z)-z^m/g.                                (2)

Use rho(x)=x(4x-3)^2, 1-rho=(1-x)(1-4x)^2, and y(x)=gA(rho(x)).
The independently fixed unscaled polynomial density is

    D_0(x)=g(1-4x)^2P(rho(x))
            =[y(x)-rho(x)^m]/(1-x), deg D_0<=N-1.         (3)

The division denotes literal polynomial division. Its terminal rho^m
term is not deleted.

Define exactly the previous six moment functional

    Phi(f)=2I_(1/2)(f)+8J_(1/2)(f)-I_1(f)/3+8J_1(f)/3
                                  -7I_(1/4)(f)/3+20J_(1/4)(f)/3.

All I denominators on (3) are <=N and all J denominators are <=p-2.
Linearity and the actual moment definitions U_k,V_k prove

    BOX: g(M_H+M_O)=Phi(D_0),
    M_H+M_O=sum_(k=0)^(m-1)S_k(U_k+V_k).                 (4)

Thus the entire actual H/O prefix pairing uses one fixed polynomial
density, with its original m,N cutoffs and no next beta or J moment.

## 2. Derived inhomogeneous operator and actual density endpoints

Let

    H=2x(x-1)(4x-1)partial_x^2+(20x^2-15x+1)partial_x+(4x-1),
    D_A=z(1-z)partial_z^2+(1/2-3z/2)partial_z-1/18.

The exact coefficient pullback is H=-18(4x-1)Pull_rho(D_A).
It is checked before any field endpoint is evaluated. For the fixed
integer monomial z^m, coefficient reduction m=-1/6 gives
D_A(z^m)=z^(m-1)/9. Since H y=0, (3) gives the actual source equation

    BOX: T D_0=2(4x-1)rho(x)^(m-1),
    T=H composed with multiplication by (1-x),
    T=-2x(1-x)^2(4x-1)partial_x^2
        +(1-x)(36x^2-19x+1)partial_x-2(12x^2-10x+1).     (5)

Only coefficient polynomials are reduced at m=-1/6; the actual finite
degree and exponent m are not replaced by a characteristic-zero fraction.
The terminal rho^m term is exactly what creates the nonzero right side.

The fixed density has the useful literal endpoints

    D_0(0)=g, D_0'(0)=2g, D_0(1)=-1,
    D_0(1/4)=D_0'(1/4)=0,
    D_0(1/2)=-2^(1-m).                                   (6)

At 0 the source vanishes because m>=2, and the actual T row is
D_0'(0)-2D_0(0)=0. At 1 the row is -6D_0(1)=6, with unit 6; no
singular leading coefficient is divided out. The quarter point is a
double zero by (3), and the half point follows from CM0 and rho(1/2)=1/2.

## 3. Genuine Green pairing with the original fixed C carrier

Use the original independently constructed C(w), w(x)=1-rho(x), and
the literal flat-measure carrier

    E(x)=(4x-3)C(w(x))/6.

This E in the x coordinate is distinct from the t-coordinate carrier
and from the coefficient moments E_c(A). For G_N(z)=sum_(j=0)^(N-1)z^j,
direct all-coefficient differentiation gives

    H*E=-rho'(x)G_N(rho(x))/9,
    T*E=(1-x)H*E.                                        (7)

For any L=a partial^2+b partial+c put
K_L(F,Y)=a(FY'-YF')+(b-a')FY. The ordinary Green identity is
K_L'=F LY-Y L*F. The product operator in (5) obeys exactly

    K_T(E,D_0)=K_H(E,(1-x)D_0)
             =K_H(E,y)-K_H(E,rho^m).                    (8)

The first term is the *literal original* composed concomitant:
K_H(E,y)=K_G(C,V)(w(x))=-gJ(rho(x)). Consequently (8) preserves the
earlier cubic Frobenius term; it is not reconstructed from its derivative.
The source derivative is explicitly

    K_T'=rho'(x)[C(w(x))rho(x)^(m-1)
                                 +(y(x)-rho(x)^m)G_N(rho(x))]/9. (9)

At x=1/2 let C_*=C(1/2), C'_w,*=(partial_w C)(1/2), h=2^(-m).
The original and connected C derivatives have opposite signs; this
notation means the derivative in the original w coordinate. There,

    E_*=-C_*/6, E'_* =2C_*/3-C'_w,*/2,
    (rho^m)_*=(rho^m)'_*=h,
    H leading coefficient=-1/2, b_H-a_H'=1/2.

Thus both signs and the actual terminal correction are fixed:

    K_H(E,y)_*=-tau,
    K_H(E,rho^m)_*=h(C_*/3-C'_w,*/4),
    BOX: K_T(E,D_0)_*=-tau-h(C_*/3-C'_w,*/4).            (10)

No C inverse, derivative inverse or boundary fit occurs. This is a
genuine density-to-fixed-C Green boundary; it does not evaluate Phi(D_0).

## 4. Its own explicit fixed-C middle-coefficient Frobenius tail

Set Z(z)=gA(z)-z^m=(1-z)gP(z), and define in the connected coordinate

    G_density(z)=-K_A(Cbar,Z), Cbar(z)=C(1-z).

The literal identity is K_T(E,D_0)(x)=G_density(rho(x)). The Gauss
coordinate polynomial has degree <=4m<p and fixed endpoint G_density(1)=0.
Its source is

    G_density'=[Cbar(z)z^(m-1)+Z(z)G_N(z)]/9.             (11)

If G_density=sum_(s=0)^(4m)sigma_s z^s, its legal coefficient inverse is

    sigma_s=[1_(m<=s<=4m-1)cbar_(s-m)
                 +sum_(i=max(0,s-N))^min(m,s-1)(g a_i-delta_(i,m))]/(9s),
                         1<=s<=4m,
    sigma_0=-sum_(s=1)^(4m)sigma_s.                       (12)

Absent endpoint terms in this formula are omitted, not evaluated at an
exterior coefficient. All denominators are units. It also fixes
sigma_0=gC(1)/2 from the actual lower concomitant.

The cubic composition has degree <=2p-2. Its x^p coefficient uses the
same legal binomial range as the previous dictionary. The terms s>N
vanish by that already proved factorial argument. For 2m+1<=s<=N,
the convolution part of (12) is the full Z(1)=0, so sigma_s=cbar_(s-m)/(9s).
Therefore the actual new derivative-kernel coefficient is

    BOX: k_p^density=(1/9)sum_(s=2m+1)^N cbar_(s-m)
                     binom(2s,p-s)4^(p-s)(-3)^(3s-p)/s. (13)

It uses only the fixed Cbar middle coefficients m+1,...,2m; no e_N or
cbar exterior value occurs. It is not set to zero. Equivalently, the
literal decomposition (8) gives
k_p^density=-g b_p-[x^p]K_H(E,rho^m), with both constituent tails fixed
before comparison.

There is also a direct common-kernel form of this actual density tail.
Let E_(r-1)^adj(z)=sum_(j=0)^(r-1)e_j z^j be the unchanged partial
adjoint polynomial. Using the fixed reflection and (1),
cbar_j=4e_j E_(N-j-1)^adj(1)/(9g^2). In (13) put r=4m-s. This gives

    BOX: k_p^density=4/(81g^2)sum_(r=m)^(2m-1)
                               e_(N-r)E_(r-1)^adj(1)Omega_r,
    Omega_r=binom(8m-2r,2m+r+1)4^(2m+r+1)
                                   *(-3)^(6m-3r-1)/(4m-r). (13a)

The reindexing is literal: j=s-m=N-r, N-j-1=r-1, 2s=8m-2r,
p-s=2m+r+1 and 3s-p=6m-3r-1. Every factorial in this binomial is
below p and the denominator 4m-r is a unit. Omega is a new fixed
coefficient weight, distinct from the old reciprocal triangle W_r.
Equation (13a) uses the very same e_(N-r) kernel as F_CM. Its support
contains the actual OLD-R cutoff point r=m and the strict C-tail part
m<r<=2m-1. Its prefix is evaluated at 1, whereas F_CM's partial Green
prefix is evaluated at 1/2; these values are not equated. The global
remaining C range r>=2m is not removed from F_CM merely because this
particular Frobenius coefficient has smaller support. This exact index
and weight check remains within the present density unit.

If P_density is the coefficientwise primitive of (9) with zero constant
and zero x^p coefficient, the full CM normalization is

    BOX: -tau-h(C_*/3-C'_w,*/4)
            =sigma_0+P_density(1/2)+k_p^density/2.        (14)

All remaining primitive denominators are units; its absent resonant
coefficient is zero because (9) is the derivative of the actual polynomial.
The correction 1/2 is the actual base-field x^p at x=1/2, not an arbitrary
integration constant. The older odd-moment 16^m and finite-log complement
remain separate inherited corrections and are not removed by this lemma.

## 5. Exact density-scope residual against the unchanged F_CM

Consume, without redefining, the previous fixed low/high cutoff source
F_CM with M_R-3tau=eta_N F_CM. Its r<=m and r>m ranges remain explicit
in that source's own constructor. Using only (1),(4), the original scalar
residual is exactly

    BOX: kappa+T_m+2W_m/g-Phi(D_0)+F_CM/(9g^2).           (15)

Thus the precise remaining comparison can be stated as

    Phi(D_0)-F_CM/(9g^2)=kappa+T_m+2W_m/g.                (OPEN) (16)

D_0 has the independent density construction and source (3),(5); F_CM
has its independent reciprocal-D/C construction and original cutoff.
Neither is chosen from (16). The Green boundary (10) and its correction
(14) give exact fixed-C information for this actual density, but they do
not identify the six moment functional Phi with the reciprocal source.
This is the remaining mathematical step, not an assumed closure.

## 6. Independent checking boundary

The new checker passed 40 exact checks: Wilson-normalization algebra,
generic literal prefix/density coefficients, the polynomial T and Gauss
pullback coefficients, monomial source residues, fixed-carrier adjoint
source, literal Green pullback/product identity, density endpoint rows,
CM terminal signs, central C convolution cancellation and normalized
residual sign. The generic arrays have unrelated rational degrees and
instantiate no p=6m+1. No prior checker or old rational ansatz is reused.

The T equation was derived independently in this unit; the parent then
transmitted its fixed-carrier Green formula, whose coefficients and CM
signs were independently checked. The middle-C Frobenius dictionary was
derived independently and shared back. This is directed collaborative
checking, not blind peer review. All literal inputs and old bytes remain
unchanged. Scalar comparison, LIFT, weighted p^3, period normalization
and full native X6 propagation remain OPEN.
