# PREFIX-427 | Uniform quadratic approach to the final five-Port saturation threshold

Date: 2026-11-02. Scientific input frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation: PREFIX-426, exact global plateau. Evidence status: author-side analytic proof, rational inequalities and independent raw-matrix symbolic check; unreviewed, not admitted. External static coherent complex-source auxiliary model, not a native P000 X6/typed BRC computation.

## Statement

Let beta=10^-6, rho=10^-3, 0<=epsilon<=beta and u,v be complex. Constraints are
  ||u|^2-1|<=epsilon, ||1+u|^2-2|<=epsilon, |v|<=rho,
  ||1+v|^2-1|<=eta, ||z5|^2-709/32|<=eta,
where H=(5+9i)/2+(3+7i)u/2, z4=H+4iv, z5=(22+15i)(1+u)/8+(5+9i)v/4.
Write kappa_*(epsilon,eta)=min ||z4|^2-41| over all these sources.

Put w=sqrt(1+epsilon-epsilon^2), J=41-49epsilon/2+4w,
h=sqrt(J), g=4+59epsilon+368w, T=1226-705epsilon+61w,
eta_sat=709epsilon/64+T/(8000h)-53beta/8,
kappa_sat=(h-4rho)^2-41, D=g/(16000h), M=T/(8000h).
PREFIX-426 proves the unrestricted global optimum and the plateau criterion: eta>=eta_sat iff kappa_*=kappa_sat, and its unique unrestricted optimizer is u*=-epsilon-iw, v*=i rho H(u*)/|H(u*)|.

THEOREM (uniform left approach). For each 0<=epsilon<=10^-6 and each 0<delta<=10^-6, set eta=eta_sat(epsilon)-delta. Then
  2100 delta^2 < kappa_*(epsilon,eta)-kappa_sat(epsilon)
               < C(epsilon)delta^2 <2235 delta^2,
  C(epsilon)=4rho h/D^2=1024000 J^(3/2)/g^2,
  2233<C(epsilon)<2235.
Moreover the quotient of the left-side gap by delta^2 tends to C(epsilon) uniformly as delta approaches 0+. At epsilon=0, C(0)=960000 sqrt(5)/961 = 2233.741163787511... . At epsilon=10^-6, C=2233.736570214725... .

## Exact feasible upper construction

Keep u=u*, and rotate v* using a rational parametrization of the unit circle, without any trigonometric or pi expansion:
  v(t)=v* [(1-t^2)+2 i t]/(1+t^2), t>=0.
This preserves both baseline observations and |v|=rho. For k=|z5|^2-709/32, direct substitution gives
  k(u*,v(t))-k(u*,v*)=(2Dt+2Mt^2)/(1+t^2),
  |z4(u*,v(t))|^2-|z4(u*,v*)|^2=16rho h t^2/(1+t^2).
Define
  t_delta=delta/[D+sqrt(D^2+(2M-delta)delta)].
It is the unique positive root of (2M-delta)t^2+2Dt-delta=0. Thus k(u*,v(t_delta))=-eta. The second joint measurement is bounded by 2rho+beta=0.002001<eta, and the fifth-port upper inequality also holds. This is a complete coherent-source feasible witness for every declared epsilon,delta. Since 2M>delta, 0<t_delta<delta/(2D). Therefore the global gap is strictly below 4rho h delta^2/D^2 = C(epsilon)delta^2.

## Full-source quadratic lower bound

On the negative phase set r=|u|^2, s=|1+u|^2, a=(s-r-1)/2 and b=Im u=-sqrt(r-a^2). Define
  J_u=|H(u)|^2=7-5r+39s/2+4sqrt(r-a^2), h_u=sqrt(J_u).
Its derivatives obey J_{u,r}< -2.9 and J_{u,s}>19 on the entire baseline box. With r*=1+epsilon,s*=2-epsilon and L=(r*-r)+(s-s*), these give
  J_u-J >=2.9L,  |u-u*|<=1.01L.
Here a-a*=L/2 and both square-root denominators are >1.98.

For fixed u, the exact disk minimizer is v0(u)=i rho H(u)/h_u. Set e=v-v0(u). The exact global square identity is
  |z4(u,v)|^2-(h_u-4rho)^2
    =(4h_u/rho)|e|^2+(4h_u/rho-16)(rho^2-|v|^2).
All terms on the right are nonnegative. As h_u>6.7 and
  (h_u-4rho)^2-(h-4rho)^2>=0.99(J_u-J),
the candidate objective gap G=|z4(u,v)|^2-(h-4rho)^2 satisfies
  G>=0.99(J_u-J)+26800|e|^2+26784(rho^2-|v|^2).
Consequently |u-u*|<0.36G. Resolve e into tangential alpha and radial gamma relative to unit n=v0(u)/rho:
  e=gamma n+alpha i n,
  gamma=(|v|^2-rho^2-|e|^2)/(2rho)<=0,
  |gamma|<G/25, G>=26800 alpha^2.

The full fifth-Port observer, without dropping joint source terms, is
  k(u,v)=709(s-2)/64+P Re(v)+Q Im(v)+53|v|^2/8,
  P=[245(1+a)+123b]/16, Q=[-123(1+a)+245b]/16.
We have |(P,Q)|<25, |(P,Q) dot i n|<3.5, and
  |k(u,v0(u))-k(u*,v*)|<5G.
The latter follows from |delta c|<=12L, |delta(P,Q)|<=18|u-u*|, and
  |v0(u)-v*|<1.2rho|u-u*|.
Since |v|^2<=rho^2, the fifth-Port lower boundary implies
  delta <6G+3.5|alpha|.

For the positive phase, the globally optimal absolute deviation differs from kappa_sat by >0.004, using the PREFIX-426 exact phase comparison; the feasible upper witness has gap <2235 delta^2<=2.235e-9, so a full-source optimizer is on the negative phase. At that optimizer, G<2235 delta^2 and delta<=10^-6 give 6G<0.015 delta. Hence
  |alpha|>(197/700)delta,
  G>26800(197/700)^2 delta^2 >2100delta^2.
This lower bound covers every legal continuous source, including ones with displaced u or inward v.

## Uniform sharp leading coefficient

The inequalities just established imply, uniformly in epsilon,
  G=O(delta^2), |u-u*|=O(delta^2),
  rho^2-|v|^2=O(delta^2), |e|=O(delta), gamma=O(delta^2).
The tangent coefficient of k at u* equals
  (PB-QA)/(8h) = D/rho,
because PB-QA=(63r+4a-368b-59)/2=g/2 at u*.
All these rational/radical functions are smooth and their denominators bounded away from 0 on a fixed compact epsilon-box. Thus the fifth-Port condition gives
  delta <=(D/rho)alpha+O(delta^2),
and the exact square identity gives
  G>=(4h/rho)alpha^2+O(delta^3),
with uniform O constants. Therefore liminf G/delta^2>=4rho h/D^2.
The explicit witness has t_delta=delta/(2D)+O(delta^2) uniformly and objective gap Cdelta^2+O(delta^3), proving uniform limsup<=C and the theorem.

This is a sharp asymptotic theorem for the OPTIMAL VALUE. The rotation witness is a feasible source attaining the sharp leading term; exact optimal-source active-set uniqueness for positive delta remains the next independent question.

## Certified arithmetic and independent provenance

At all 0<=epsilon<=beta, 1<=w<=1+beta,
  45-49beta/2<=J<=45+4beta,
  372<=g<=372+427beta.
Using integer isqrt outward root enclosure and Fraction arithmetic gives 0.0034<D<0.0035, 2233<C<2235, M>0 and h>6.7. A standard-library verifier executed 19 exact rational checks PASS, including the lower constant 26800(197/700)^2>2100 and the disk radial bound. The independent SymPy verifier rederived J,A,B,P,Q, their Gram and determinant identities and the rational-circle observation laws from original z4,z5 and returned PASS. A separate high-precision endpoint-only crosscheck passed; it is not used for the universal theorem.

This work composes already published external five-Port results with phase/source/joint-observer fidelity (BRC: COMPOSE_APPLIED at the method level). The typed BRC native kernel was not executed, and no P000 X6 or native three-dimensional slice dynamics are attributed to this static auxiliary computation.

Next PREFIX-428: establish the exact optimizer and active set for small positive delta (whether u remains at u* and |v|=rho), then determine the cubic term or give an exact counterexample. Formal CLAIM, independent Review and Admission remain separate Source operations.
