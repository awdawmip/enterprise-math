# PREFIX-428 | Exact global optimizer and uniform cubic gap below saturation

Date 2026-11-02. Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Antecedents: PREFIX-426 (exact plateau) and PREFIX-427 (uniform quadratic bound), both author-side and unreviewed. This result is author-proved and rational/symbolic checked, not formally reviewed/admitted. Scope: the external static five-Port coherent complex-source auxiliary model; native typed BRC and P000 X6 dynamics have not been executed.

## Fully quantified statement

Set beta=10^-6, rho=10^-3, 0<=epsilon<=beta and 0<delta<=beta. Let eta=eta_sat(epsilon)-delta. Minimize kappa=abs(|z4|^2-41) over complex u,v subject to
abs(|u|^2-1)<=epsilon, abs(|1+u|^2-2)<=epsilon, |v|<=rho,
abs(|1+v|^2-1)<=eta and abs(|z5|^2-709/32)<=eta, with
H=(5+9i)/2+(3+7i)u/2, z4=H+4iv, z5=(22+15i)(1+u)/8+(5+9i)v/4.

Define w=sqrt(1+epsilon-epsilon^2), u0=-epsilon-iw,
J=|H(u0)|^2=41-49epsilon/2+4w, h=sqrt(J),
g=4+59epsilon+368w, T=1226-705epsilon+61w,
D=g/(16000h), M=T/(8000h),
eta_sat=709epsilon/64+M-53beta/8,
kappa_sat=(h-4rho)^2-41.

THEOREM: The unique global optimizer is
u_delta=u0,
n=iH(u0)/h,
t_delta=delta/(D+sqrt(D^2+(2M-delta)delta)),
v_delta=rho*n*(1-t_delta^2+2it_delta)/(1+t_delta^2).

The active set consists of |u|^2=1+epsilon, |1+u|^2=2-epsilon (when epsilon=0 these are equalities), |v|=rho, and |z5|^2=709/32-eta. The |1+v|^2 observation is strict. All optimal sources are on the negative-Im(u) phase, |z4|^2>41.

With G=kappa_*(epsilon,eta)-kappa_sat,
G=16rho*h*t_delta^2/(1+t_delta^2)
 =8rho*h*delta^2/[D^2+Mdelta+D sqrt(D^2+2Mdelta-delta^2)].
Setting C=4rho*h/D^2, K=-C*M/D^2, one has for the entire parameter rectangle
0 < G-Cdelta^2-Kdelta^3 < 14,000,000,000 delta^4.
Thus G=Cdelta^2+Kdelta^3+O(delta^4), uniformly in epsilon.
K(0)=-4459454.630701413395... and K(10^-6)=-4459436.182031726908... .
The quartic Taylor coefficient is rho*h*(D^2+5M^2)/D^6.

## Proof: exact observer algebra and feasibility

For the negative branch write r=|u|^2, s=|1+u|^2, a=(s-r-1)/2, b=Im(u)=-sqrt(r-a^2), H=A+iB, v=x+iy. Raw z4/z5 expansion gives
F=|z4|^2=J_u+16(x^2+y^2)+8Bx-8Ay,
J_u=7-5r+39s/2-4b,
k=|z5|^2-709/32=709(s-2)/64+Px+Qy+53(x^2+y^2)/8,
P=[245(1+a)+123b]/16, Q=[-123(1+a)+245b]/16.

At u0, p_k=(P,Q), n=iH/h, and i*n its complex tangent:
p_k dot n=-M/rho, p_k dot (i*n)=D/rho.
Indeed PB-QA=T/8 and -PA-QB=g/16 using w^2=1+epsilon-epsilon^2 (independent symbolic check supplied). The rational unit-circle path v(t)=rho*n*(1-t^2+2it)/(1+t^2) has the exact increments
k(u0,v(t))-k(u0,v(0))=(2Dt+2Mt^2)/(1+t^2);
F(u0,v(t))-F(u0,v(0))=16rho*h*t^2/(1+t^2).
By PREFIX-426, k(u0,v(0))=-eta_sat. The positive root of
(2M-delta)t^2+2Dt-delta=0
is precisely t_delta; hence k(u0,v_delta)=-eta. Its |1+v|^2 observer obeys
abs(2Re(v)+rho^2)<=2rho+rho^2=0.002001<eta
(the last inequality follows from M>0.023 and delta<=beta). Feasibility and the exact objective value follow.

## Proof: full-source dual support and unique optimality

Put c=(1-t_delta^2)/(1+t_delta^2), z=2t_delta/(1+t_delta^2) and
lambda=8h*rho*z/(D*c+M*z)
=16h*rho*t_delta/[D(1-t_delta^2)+2Mt_delta].
Exact bounds establish 0<lambda<1/200. For any u on the negative branch and any |v|<=rho,
F-lambda*k = J_u-lambda*709(s-2)/64+alpha*|v|^2+p_lambda dot (x,y),
alpha=16-53lambda/8>0,
p_lambda=(8B-lambda P,-8A-lambda Q), R=|p_lambda|.
For all permitted r,s, R>8*6.7-(1/200)*48>2alpha*rho; thus the disk minimum is uniquely at v=-rho*p_lambda/R and equals
m(r,s)=J_u-lambda*709(s-2)/64+alpha*rho^2-rho R.

Throughout the baseline rectangle, |a|<=beta, 999/1000<sqrt(r-a^2)<1001/1000.
One has J_{u,r}= -5+2(1+a)/sqrt(r-a^2)<-2.99,
J_{u,s}= 19.5-2a/sqrt(r-a^2)>19.49.
Direct A,B,P,Q differentiation gives
|(p_F)_r|_1<72, |(p_k)_r|_1<36,
|(p_F)_s|_1<24, |(p_k)_s|_1<12
with p_F=(8B,-8A). Thus |R_r|<73, |R_s|<25,
m_r< -2.99+0.001*73<0,
m_s>19.49-(709/64)/200-0.001*25>19.
The unique minimum across all negative-phase u is at r=1+epsilon,s=2-epsilon, that is u=u0. At u0, p_lambda resolved along n and i*n has components
(-8h+lambda*M/rho, -lambda*D/rho).
The chosen lambda makes -p_lambda parallel to v_delta, with positive normal and tangential components. Hence v_delta uniquely minimizes F-lambda*k on the disk.

For every feasible source k+eta>=0, lambda>0, so
F(u,v)>=F(u,v)-lambda*(k(u,v)+eta)
>=F(u0,v_delta)-lambda*(k(u0,v_delta)+eta)=F(u0,v_delta).
Equality determines u0,v_delta. The positive-phase comparison completes the absolute-deviation optimization: positive b gives J_u<37.004025 and sqrt(J_u)<6.1, so F<37.053, hence kappa>3.947. The negative witness obeys J<=45+4beta, h>6.7, G<Cdelta^2<2235beta^2, so F<44.947, hence kappa<3.947 and F>41. The negative minimizer therefore wins uniquely across both phase branches.

## Proof: rigorous cubic remainder

Let E=D^2+Mdelta+D sqrt(D^2+2Mdelta-delta^2),
q=(E-2D^2)/(2D^2) and a0=M/D^2.
Since M>0.023>delta/2, E>2D^2 and 0<q<a0delta. Exact rationalization yields
a0delta-q=(D^2+M^2)delta^2/(2D^2*E).
Since 1/(1+q)=1-q+q^2/(1+q) and G=Cdelta^2/(1+q),
0<G-Cdelta^2+C*a0delta^3
 <=C*(D^2+5M^2)/(4D^4)*delta^4.
The rational checker verifies D>17/5000, D<7/2000,
0.023<M<1/40, C<2235 and
2235*((7/2000)^2+5*(1/40)^2)/(4*(17/5000)^4)<14e9.
The coefficient of delta^3 is exactly K=-C*M/D^2.

## Actual checks and remaining research

The local Fraction/isqrt-oriented exact inequality reproduction ran and passed 22 rational tests; independently a SymPy script reconstructed original raw observer identities, both source normal/tangent coefficients modulo w^2=1+epsilon-epsilon^2, and the quadratic, cubic, quartic coefficients. Decimal endpoint evaluations are illustrations; the proof covers the complete continuous parameter rectangle via analytic rational bounds. Original local execution sources SHA256: rational checker 3ddd3eaa6dca9328691fcde9f9da5b1b7f678d06b7efcd323e8ba3f1edfae843, independent checker 2551cad46595ddad574199af0a46bfa615697afb698b96a8648ab760dc0c360c.

The current Sites gateway reported research_authority_granted=false; an attempt to read active Tasks returned CONTROL_QUOTA. GitHub author identity is awdawmip. No authenticated CLAIM, Result, independent Review or Admission is claimed. BRC reuse is source/phase/joint-observer fidelity only, with no typed native BRC execution or P000 X6 transfer.

Next PREFIX-429: enlarge delta beyond 10^-6 toward smaller eta; locate the first failure (if any) of the fixed-u0, radius-boundary, fifth-Port lower active set using an exact competitor or dual bound. An independent extension is a higher-order jet with a verified radius.