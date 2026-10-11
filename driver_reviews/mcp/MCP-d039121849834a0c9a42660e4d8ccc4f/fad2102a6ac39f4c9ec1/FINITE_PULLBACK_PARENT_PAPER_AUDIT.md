# Directed audit of the finite CM first-digit certificate

Verdict: PASS for the complete finite pullback/pole/CM proof, subject to
Root's separate formal publication and third-party final-byte review.
The mathematical first digit U_0=1 and UR-SUM follow from the stated
frozen finite inputs. The p^3 second-digit LIFT remains OPEN.

This is Root-directed local paper preparation by
`cm24_ur_adjoint_frontier`, not a new researcher identity, Claim, Source
write or formal Driver acceptance. P000, Heartbeat and residual-fidelity
contracts were read; this is finite external arithmetic with no new
native spatial model. The initial Wronskian boundary came from this
agent; the finite signature-3 rational pullback and Frobenius-pole idea
came from delegated `ur_cm_boundary_complement`. We exchanged pole and
factorial calculations before the final proof. Therefore this is a
shared, nonblind mathematical audit, not blind independence.

Exact final input files and output pins are in FINAL_UNIT_PINS.json.
The final complement certificate was fully read, including its closing
sign explanation: 9550 bytes, SHA256
8a6e7882799eed3b846df92a6b5dd8e98b061f8751805419ac343ba34c572a3e.
The companion SYMBOLIC JSON and executable use exact SymPy algebra;
no new prime calculation or provider query was made. Thirteen rational
identities vanish exactly. The pole and finite-characteristic arguments
are checked below as proofs rather than inferred from those checks.

## 1. Finite truncation and the exact rational pullback

For p=6m+1, the coefficient b_n contains its first p factor after n=2m
and its second after n=4m. Consequently F=sum_(n=0)^(4m)b_n z^n agrees
with the full p-1 Hesse truncation modulo p^2. Its exact residual is
-(4m+1/3)(4m+2/3)b_(4m)z^(4m); the second factor is 2p/3 and the
coefficient has one p factor. Thus D_HF=0 mod p^2 is genuinely finite.

Put A=(3z-1)/(z-1)^3, B=(3z-1)^2/(z+1)^3,
L=(z+1)/(2(1-z)), K=B(1-B)/B'. With the finite differential operator

    O(Y)=(K Y')'-(2/9)B'Y,

the following two identities hold exactly over the p-integral rational
function ring, before any reduction:

    O(F(B))=B' (D_HF)(B),
    O(L F(A))=A'/(2L) (D_HF)(A).

The second follows by checking its F'',F',F coefficients; these are
the leading/first/zero entries in the symbolic check. In particular
this derives the transformation without importing an analytic modular
period or silently asserting an isogeny normalization. For f=F(B),
g=LF(A), R=K(fg'-gf'), these identities give R'=0 mod p^2.

All rational denominators are supported at z=1,-1, plus the constant
units 2 and 3. The zeros of K at 0,3,1/3 are regular evaluation points
of f and g, so R vanishes at all three exactly. At infinity f and g
are bounded and their derivatives are O(z^-2), whereas K=O(z), so
R=O(z^-1). These statements persist after coefficientwise division.

## 2. Divisibility is proved before R/p is used

Modulo p, F=H has degree 2m. At z=1, g has pole order <=p and its top
derivative coefficient -p vanishes, so R has pole order <=p.
At z=-1, f has pole order p-1 and g has a simple zero (H(1/2) is a
unit); the top Wronskian coefficient is 1+(p-1)=0. The remaining pole
order in the bracket is <=p-2; K's double pole gives R order <=p.

The derivative kernel in F_p(z) is F_p(z^p). The pole bounds and decay
at infinity imply denominator (z^p-1)(z^p+1) with numerator degree
at most 1 in z^p. Three distinct regular zeros 0,3,1/3 force this
numerator to vanish. Thus R=0 mod p is proved, not inferred from CM0,
an assumed determinant or the desired answer.

Only then is R_1=R/p mod p defined. Full F degree 4m allows poles
at most 2p at both endpoints. Since R'=0 mod p^2, R_1 belongs to
F_p(z^p); its decay and three zeros force

    R_1=C J(z^p),
    J(t)=t(t-3)(3t-1)/[(t-1)^2(t+1)^2].

There is no extra polynomial or integration constant. A common
denominator supported at the two endpoints permits coefficientwise
division by p and evaluation at each of the three regular zeros.

## 3. Independent short factorial check of the top-pole constant

At z=1 the top-pole coefficient determines

    C=(b_(4m)/p) 2^(4m)H(1/2)/3,
    b_(4m)/p=(2m)!(2m-1)!/[3(4m)!],
    H(1/2)=(-1)^m(2m)!/[2^(2m)(m!)^2].

I independently evaluated C with a different short duplication path:

    (4m)!=2^(4m)(2m)!(3m)!/m!,
    (2m)!^2=(-1)^m2^(2m)m!(3m)!       mod p.

Both are the usual even/odd product identity followed by 1/2=-3m
mod p; every factorial index is below p. Substituting gives

    C=1/(18m)=-1/3 mod p.

This agrees with the complement's Wilson/even-product proof. It uses
neither U nor a target value, and covers all p=6m+1>=7.

## 4. CM substitution, markings and the divided rho

Write delta^2=2, z=3-2delta. In the two specified prime classes,
delta^p=-delta, hence z^p=1/z. Exact reduction by z^2-6z+1 gives

    A=(2+delta)/4, B=(2-delta)/4, L=delta/2,
    A+B=1, 4A(1-A)=1/2,
    A'=B'=-3/(8z), K A'=1/8, J(z^p)=1/4.

All evaluation denominators are units: z is nonzero, and z=+-1 would
give respectively -4 or 8 in its quadratic equation, impossible for
p>=7. These reductions preserve the two actual marked branches; no
literal p-power lift modulo p^2 is substituted for Frobenius.

H=V(4x(1-x)), d=V'(1/2) gives H'(A)=-2delta d and H'(B)=2delta d.
CM0 makes F(A),F(B) divisible by p. The exact symmetric M constructor
directly supplies (F(A)+F(B))/2=M(1/2) mod p^2; discarded coefficients
each have two p factors. Evaluation of the actual rational Wronskian is

    R_1=-(d/4)[F(A)/p+F(B)/p]
       =-(d/2)M(1/2)/p=-U_0/12.

The L'F(A)F(B)/p term vanishes because it still has a p factor.
The finite rational certificate gives R_1=-(1/3)(1/4)=-1/12. Thus
U_0=1, with the original exact M lift and its p-divided value retained.
Using the previously proved boundary U_0=6rho d+24P(1/2)-2 gives
UR-SUM exactly. In particular rho was neither zeroed nor fitted.

## 5. Scope and saved failures

The earlier bare primitive P had a degree-p Wronskian kernel and had
to retain -w^p/6. The earlier integral endpoint P(1)=1/6 alone did
not determine the CM half endpoint or rho. This new finite pullback
uses two actual poles and three exact zeros to determine a different
Frobenius rational invariant, and genuinely closes that missing CM
boundary. No old six-prime/77-prime campaign or Clausen-tail audit
was repeated. A direct terminating Saalschutz/Whipple matching attempt
at argument 1/2 did not supply a summation identity; it is not used
in the proof.

Root's separate prior-art scout reported a potentially matching
Chisholm-Deines-Long-Nebe-Swisher 2013 theorem for the weighted first
digit. Its primary parameters are being checked separately. This file
makes no first-discovery or novelty claim; the local result is an
independent finite differential/pole certificate. The first digit and
the second digit must retain separate statuses.

The one meaningful next mathematical unit is to lift this same R
construction to precision p^3 with its explicit D_HF forcing retained,
and compare the next coefficient with the already fixed OLD-R plus
6tau. The new poles and forcing must be computed, not assigned from
the target. That second-digit work has not been performed here.
