# An exact finite Lommel bridge and a power-scale actual real-state margin

AUTHOR WORKING / UNREVIEWED. One bounded theorem proposed for eventual
genuine nonauthor whole review. Authors: EM-PUBLIC-7CDA51,
EM-DVR-BFF6DC and EM-DIRECT-88303D, according to the actual constructions
listed in the context. Author crosschecks are not independent votes.
The separate CF1677 complex-disk estimate is not a premise of this theorem.

All calculations below are symbolic hand proofs. No scientific program,
sample, generated coefficient/matrix, test, import/compilation, solver,
consumer or Native operation was used. The old STOP/HOLD and UNKNOWN
formal budgets remain. Source3cc2c193's earlier partial-work HOLD archive
is unchanged; this is a different subsequent proof, not a correction of it.

## 1. The actual state and the bounded conclusion

For an integer m let V be the ORIGINAL positive Student carrier of real
polynomials of degree<=m-2, with weight w_m(v)=(1+4v^2)^(-m), monic
orthogonal polynomials P_k^(m), norms h_k^(m), and e_k=P_k/sqrt(h_k).
Its dimension is m-1. Put D_v=d/dv and let dagger be its actual positive
Hermitian adjoint. We retain the old frame exactly:

 Z_xi=Z0+sum_(k even,2<=k<=n)
        [-2zeta(k)/(2pi)^k] xi^(k-1)D_v^k,
 Z0=vD_v-(m-1/2)I,
 R_xi=Z_xi+Z_xi^dagger, b(xi)=tr(R_xi^2).              (1)

Here n is the largest even integer<=m-2 and t=m-n is2 or3. The original
compressed/rank-one carrier and odd top input are not removed. All norms
below refer to this carrier; it is not enlarged by a degree-m-1 vector.
Define the original positive amplitude

 H_n=n!sqrt(h0^(m)/h_n^(m)),
 A_n(xi)=H_n xi^(n-1)/(2pi)^n, z=pi/xi.               (2)

**Theorem proposed.** For every integer m>=2^1000 and every real

                  m^(-1/100)<=xi<=1,

the SAME actual state satisfies

             b(xi)>=2^(-24) z^(-12) A_n(xi)^2>0.       (3)

Equivalently pi<=z<=pi*m^(1/100). This is an explicit real-state margin.
It is NOT a homogeneous coefficient, L_(d,j)b, the COMMON Psi sign,
full-P1 positivity or a trace/Goal theorem. Those missing arrows are
recorded in section8. No coefficient range is inferred from pointwise
positive Gram values.

The load-bearing old exact input is the full23366-byte bulk primary at
Source cfd876cb9bda189b8978f23d7855a9e66a862a44,
research_notes/owner_goal_20261016/parity_joint_bulk_raw_layer_7cda51_bff6dc/
PARITY_COMMON_LOWER_LAYER_UNIFORM_BULK_RAW_COEFFICIENT_BAND_JOINT_AUTHOR.md,
SHA25658af3cc47f58d63419c7cd23e5853e1add19810ada0548336e7afa0518a212b9,
blobc8f9f6dde9e4e6939d181afdf7f6092a09d12a1c. We use its exact carrier,
Student norms, B8 finite mean and A3 baseline/spectrum facts. Its genuine
old review covered a fixed-xi coefficient theorem, not this enlarged state
domain. All new uniform bounds required for(3) are proved below.

## 2. Exact finite means and the classical parameter certificate

For s=2,3,4,5 with n_s=m-s even>=2, define

 F_m,s(z)=sum_(r=0)^(n_s/2-1)
        (-z^2/4)^r rho_r/[r!(s+1/2)_r],
 rho_r=(n_s-2r)_r,rise/(m-r-1/2)_r,rise.              (4)

Let F_zeta,m,s be this SAME finite sum with the extra original multiplier
zeta(n_s-2r). Every argument is>=2. There is no generic continuation
through a negative-integer hypergeometric denominator. The exact old B8 is

 <(Z_xi-Z0)e_(n_s),e0>/A_(n_s)(xi)
                              =-2F_zeta,m,s(z).      (5)

Set N=n_s-1,nu=s+1/2,M=nu+N=m-1/2. Define scalar Laurent polynomials
L_(0,nu)=1,L_(1,nu)=2nu/z and

 L_(k+1,nu)=2(nu+k)L_(k,nu)/z-L_(k-1,nu).             (6)

Their exact finite certificate is

 L_(N,nu)=sum_(r=0)^floor(N/2) (-1)^r binom(N-r,r)
          Gamma(nu+N-r)/Gamma(nu+r) (2/z)^(N-2r).     (7)

For completeness put C_(N,r)=binom(N-r,r)Gamma(nu+N-r)/Gamma(nu+r),
zero outside the finite support. The coefficient recurrence required by(6)
is C_(N+1,r)=(nu+N)C_(N,r)+C_(N-1,r-1). Pascal's identity reduces it to
-r binom(N-r,r)+(N-2r+1)binom(N-r,r-1)=0. The initial cases agree,
so finite induction proves(7). Multiplying it by(z/2)^N Gamma(nu)/Gamma(M),
and using binom(n_s-1-r,r)=(n_s-2r)_r/r! and
Gamma(M-r)/Gamma(M)=1/(m-r-1/2)_r, proves

 F_m,s=(z/2)^N Gamma(nu)/Gamma(M)L_(N,nu).             (8)

N is odd: floor(N/2)=n_s/2-1 is exactly the original cutoff. The scaled
expression is an even polynomial with constant1; it is removable at0.
These are classical Lommel recurrences composed with the actual parameters,
not a new generic special-function tool or an asymptotic approximation.

The selected classical Bessel recurrence and Wronskian give, for real z>0,

 L_(N,nu)=(pi z/2)[J_M Y_(nu-1)-Y_M J_(nu-1)].        (9)

At N=0 the Wronskian shifted to nu-1 gives+1; the order recurrence then
gives2nu/z and(6). Thus both the sign and normalization are fixed by finite
initial conditions. No separate singular Y value is substituted at z=0.

Define real functions on z>0 by

 a_M=-pi(z/2)^M Y_M/Gamma(M),
 b_M= pi(z/2)^M J_M/Gamma(M),
 Phi_s=Gamma(s+1/2)(z/2)^(1/2-s)J_(s-1/2),
 Xi_s= Gamma(s+1/2)(z/2)^(1/2-s)Y_(s-1/2).

Then(8)-(9) give the EXACT finite identity

                         F_m,s=a_M Phi_s+b_M Xi_s.   (10)

Here a_M,b_M are auxiliary scalar functions, distinct from the actual
matrix amplitude A_n and state polynomial b(xi). The two actual channels
s=t,t+2 have N->N-2,nu->nu+2 but the SAME M. Their prefactors in(8)
are different and both have been retained in deriving(10).

## 3. Exact real phase energy, proved by finite coefficients

Put l=m-1, M=l+1/2. We will prove

 a_M(z)^2+b_M(z)^2
  =sum_(r=0)^l [c_(l,r)/c_(l,l)] z^(2(l-r))>=1,
 c_(l,r)=(l+r)!/(l-r)! *binom(2r,r)/4^r, z>0.         (11)

This is a REAL inequality; it is not complex-disk positivity. Here is a
finite proof. The selected J-series, Y-connection and Gamma reflection
give J_(1/2)=sqrt(2/(pi z))sin z,Y_(1/2)=-sqrt(2/(pi z))cos z,
J_(-1/2)=sqrt(2/(pi z))cos z,Y_(-1/2)=sqrt(2/(pi z))sin z.
For H_v=J_v+iY_v, the order recurrence implies

 H_(k+1/2)=sqrt(2/(pi z))(-i)^(k+1)e^(iz) p_k(i/z),
 p_(-1)=p_0=1, p_(k+1)(w)=(2k+1)w p_k(w)+p_(k-1)(w).

Thus p_k is a real polynomial of degree<=k with constant1. On the real
axis its squared modulus is p_l(i/z)p_l(-i/z), an even Laurent polynomial
of degree<=2l with constant1. Consequently

 h(z):=z(J_M^2+Y_M^2)=2/pi sum_(r=0)^l c_r z^(-2r), c0=1.

Positivity of these coefficients has not been assumed from a square.
The selected Bessel ODE gives u=sqrt(z)J_M,v=sqrt(z)Y_M satisfying
u''+Qu=0,v''+Qv=0,Q=1-l(l+1)/z^2. Differentiation of h=u^2+v^2 gives
h'''+4Qh'+2Q'h=0. Its exact coefficient z^(-2r-1) yields

 c_r=(2r-1)/(2r)[l(l+1)-r(r-1)]c_(r-1)
    =(2r-1)/(2r)(l+r)(l-r+1)c_(r-1).                 (12)

For1<=r<=l all factors are positive, and finite multiplication gives
c_r=c_(l,r) in(11). At r=l+1 the factor vanishes, as required by the
already established finite support. The half-integer Gamma recurrence
and Gamma(1/2)^2=pi give

 c_(l,l)=[(2l)!/(2^l l!)]^2=2^(2l)Gamma(l+1/2)^2/pi.

Substituting into the exact a_M,b_M scale proves(11), whose constant
term is1. For l=0 the identity is the usual sine/cosine energy and the
same empty recurrence applies. This proof uses no large-order asymptotic.

## 4. The actual amplitude-weighted two-channel margin

The exact old norm ratio is

 w=A_(n-2)/A_n
 =z^2/[4sqrt((t^2-1/4)((t+1)^2-1/4))]
     *sqrt((m+t)(m+t+1)/[(m-t)(m-t-1)]).             (13)

For m>=100,t=2,3, the last root is between1 and2: its upper bound
follows from(m+3)(m+4)<4(m-3)(m-4). The other denominator equals
sqrt525 or sqrt2205, strictly between16 and64. Hence for z>=1,

                              1/64<=w<=z^2.         (14)

w is an AMPLITUDE ratio, so its SQUARE weights a squared norm. No old
compact-domain upper64 is asserted on a growing domain.

The exact half-integer formulas are

 Phi2=3(sin z-z cos z)/z^3,
 Phi3=15[(3-z^2)sin z-3z cos z]/z^5,
 Phi4=105[(15-6z^2)sin z+(z^3-15z)cos z]/z^7,
 Phi5=945[(105-45z^2+z^4)sin z+(10z^3-105z)cos z]/z^9.

They follow from the same selected initial half-integer series and
recurrence, and also occur in the unchanged old bulk A3. If
Phi_s=u_s sin z+v_s cos z, the SAME Gamma/power scale gives
Xi_s=-u_s cos z+v_s sin z, by recurrence from the half-integer initial
orders. The2x2 matrices T_t with rows(u_t,v_t),(u_(t+2),v_(t+2)) have

 det T_2=-1575/z^7, det T_3=-99225/z^9.

For z>=1, the four T2 entries after extracting z^-2 are bounded in
magnitude by3,3,2205,1680, each<2^12. Thus ||T2||_F^2<2^26z^-4 and
s_min(T2)^2>2^-6z^-10>=2^-6z^-12, since1575>2^10.
For T3, after extracting z^-3 the bounds are60,45,142695,108675, each
<2^18. Thus ||T3||_F^2<2^38z^-6 and s_min(T3)^2>2^-6z^-12, since
99225>2^16. We used only s_min^2>=det^2/||T||_F^2.

For any common real a,b, the vector(a sin z-b cos z,a cos z+b sin z)
has squared norm a^2+b^2. Applying these matrix bounds to(10), then
the actual diagonal amplitude(1,w), gives

 F_m,t^2+w^2F_m,t+2^2>=2^-18z^-12(a_M^2+b_M^2).       (15)

In particular(11) supplies the weaker energy>=1/4, and hence the finite
pair norm is at least2^-10z^-6. No small-b_M subtraction, arbitrary
channel phase or compactness/no-common-zero argument is being used.

## 5. Uniform scalar-zeta remainder with both actual cutoffs

For any fixed s>=2 and even n_s>=64, we prove

 |F_zeta,m,s-F_m,s|<=2^(-n_s/4), |z|<=n_s/64.         (16)

On the actual support0<=r<=n_s/2-1,0<rho_r<=1 and(s+1/2)_r>=r!.
Thus the absolute finite coefficients are majorized by
|z|^(2r)/(4^r(r!)^2), whose infinite sum is <=cosh|z|<=e^|z|,
because binom(2r,r)<=4^r. For integers k>=3,
zeta(k)-1<=2^-k+integral_2^infinity u^-k du<=2^(1-k);
for k>=2,0<zeta(k)-1<1 by integral comparison with u^-2.

Let S=floor(n_s/4). The actual low indices r<=S have k=n_s-2r>=n_s/2,
so their contribution to the difference is at most
2^(1-n_s/2)e^|z|<=2^(1-15n_s/32)<=2^(-n_s/3).
Here log2>=1/2 and n_s>=64 suffice. For the remaining finite indices,
majorize by a_r=(|z|/2)^(2r)/(r!)^2. At r>=S+1 its consecutive ratio
is <=1/1024. Also r!>=(r/3)^r, so the first term is at most
(3/32)^(2(S+1))<=2^(-6(S+1)). The geometric tail is less than
2^(1-3n_s/2)<=2^(-n_s/3). Adding gives2^(1-n_s/3)<=2^(-n_s/4).
Only majorants were extended to infinity, never the actual zeta cutoff.

For s=t,t+2, n_s>=m-5>=m/2. On1<=z<=pi*m^(1/100),pi<4 and
m^(.99)>=2^990>512 imply z<=m/128<=n_s/64, so(16) applies to both
separate channels. For m>=256, log_2 m<=m/16: it holds at256 and the
difference has derivative1/16-1/(m log2)>=1/16-2/m>=0. At m>=1024,
n_s/4>=m/8>=28+(8/100)log_2 m. Therefore throughout this z-domain

 epsilon_s:=2^(-n_s/4)<=2^-28m^(-8/100)<=2^-12z^-8.   (17)

The error of the amplitude-weighted pair is at most
sqrt(1+w^2)max epsilon_s<2z^2max epsilon_s<=2^-11z^-6.
This is at most half the finite margin following(15). Hence the actual
zeta-restored pair satisfies

 ||(F_zeta,m,t,wF_zeta,m,t+2)||_2^2>=2^-22z^-12,
 ||-2(F_zeta,m,t,wF_zeta,m,t+2)||_2^2>=2^-20z^-12.     (18)

This still precedes restoration of the real baseline Z0.

## 6. The amplitude and the real baseline on the new xi-domain

The exact old Student moments and monic orthogonal minimization give

 h_n^(m)/h0^(m)<=E_m(v^(2n))
 =(2n)!/[16^n n!(t-1/2)_n]<=4^-n,

since(t-1/2)_n>=(1/2)_n=(2n)!/(4^n n!). Thus on the NEW xi-domain,

 A_n>=n!xi^(n-1)/pi^n>=n!m^(-(n-1)/100)/4^n
     >=m^(1/100)[m^(49/100)/8]^n>=4^n>=m^3.          (19)

We used n!>=(n/2)^(n/2), n>=m-3>=m/2. At m>=2^1000,
m^(49/100)/8>=2^487>4. Finally4^n>=2^m>=2^(3m/16)>=m^3 by the
explicit log_2 comparison above. This rechecks the amplitude domain;
the earlier fixed-xi factorial estimate has not been extended by fiat.

The unchanged old bulk A3 gives the actual TWO-ENTRY baseline estimate

 ||( <Z0e_n,e0>, <Z0e_(n-2),e0> )||_2<=2sqrt(2)m.

Only this corner/operator-norm consequence is used, not a false whole-HS
bound<=2m. In units A_n, its error is<=3/m^2. The exact input(5) and
(18) give a normalized nonconstant pair norm>=2^-10z^-6.
The baseline is at most half, because z<4m^.01 implies
2^-11z^-6>=2^-23m^(-6/100), while
3/m^2<=2^-23m^(-6/100) follows from
m^(194/100)>=2^1940>3*2^23. Consequently the actual Z pair obeys

 ||( <Z_xi e_n,e0>, <Z_xi e_(n-2),e0> )||_2
                              >=2^-11z^-6 A_n.       (20)

The HS norm of the ORIGINAL Z is at least this pair norm.

## 7. From actual entries to the actual state, without a functional claim

In the degree-ordered polynomial basis, Z_xi is triangular with real,
xi-independent eigenvalues k-(m-1/2),0<=k<=m-2. The derivative terms
strictly lower degree and vD_v has diagonal k. Thus tr(Z_xi^2)>0.
For real xi, exact adjoint expansion gives

 b(xi)=||Z_xi+Z_xi^dagger||_HS^2
      =2tr(Z_xi^2)+2||Z_xi||_HS^2
      >=2^-21z^-12 A_n^2.

The deliberately weaker bound(3) follows. We have restored Z0, retained
the real spectrum, actual dagger and all original carrier entries.
The proof never asserted that an arbitrary coefficient functional is
positive on squares.

## 8. Reuse classification, selected primary and remaining boundaries

The exact classical ingredients personally selected-read by7CDA are NIST
DLMF10.6.E1a order recurrence,10.5.E2 Wronskian,10.2.E2 J-series,
10.2.E3 Y/J connection,5.5.E3 Gamma reflection, and10.2.E1 Bessel ODE.
Their precise raw TeX bytes, actual HTTP receipts, hashes and each author's
read scope are in the context. These are selected formulas, not whole
chapter or uniform-asymptotic theorem imports. BFF and883's separately
attributed reads are not7CDA's network observations. An initial multipart
E1.tex404 was retained before the actual E1a link was obtained.

This whole result is REUSE/COMPOSE of classical identities and original
finite-mean inputs, with new exact parameter matching and growing-domain
quantification. It is not a claim of a new special-function method family.
Old lexical/index coverage no-hit does not establish novelty or NO_TOOL.

The CF1677 common-large-order COMPLEX-disk component is not used to prove
this REAL theorem, and no contribution or vote is assigned merely because
it belongs to the same research direction. Its actual future use must be
attributed separately. The newly derived full-carrier varying-order Green
representation is likewise not a hidden premise here: its triangular mask,
binomial weights, both parities, coherent pole sum and actual HS control
remain distinct obligations. Fixed-output estimates do not settle them.

In particular(3) does not certify the old strong full-origin-disk E*,
revive the killed uniform-all-subsets small-kappa condition, bound an
exact rising/falling coefficient functional, absorb original C/E/E^2/W+1
or unequal COMMON prefactors, or prove any new homogeneous coefficient
range. All lowerbridge/whole-P1/trace/Goal conclusions remain OPEN.
No scientific execution, Task, Native vote, source-functional extension,
budget reset or theorem promotion is authorized by this paper. Preserve
the earlier3cc HOLD archive and all source/author/reviewer histories.
