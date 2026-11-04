# D25: CM(-24) 2-/3-isogeny first-jet selection theorem (author-side)
Date: 2026-11-05. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7. Frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Grade: AUTHOR-DERIVED ALGEBRAIC PROOF / EXACT SYMBOLIC AND 168-PRIME CHECK / UNREVIEWED / NOT_ADMITTED. Auxiliary Legendre/CM result; native H0/B0 experiment remains separate.

## Theorem
For every prime p>=5, p=5 (mod 8), put m=(p-1)/2, Q(t)=t^4-140t^3+294t^2-140t+1 and A_p=F_p[t]/Q. Define
H_p(t)=sum_{j=0}^m binom(m,j)^2 t^j,
C_p(t)=16t(1-t^2)H_p'(t)+(1+2t-7t^2)H_p(t).
Then:
- p=5 (mod 24): C_p=0 in A_p and H_p is nonzero on *each* geometric root of Q.
- p=13 (mod 24): H_p=0 in A_p and C_p is nonzero on each root of Q.
Consequently the previously defined CM first-jet scalar a_p=u^r*t^(-r-1)*C_p, r=(p-1)/4, u=(t+t^(-1)+2)/24, vanishes for all split primes p=5 (mod 24). This proves the previously open general split-class zero law at author proof grade.

## 1. Explicit normalized degree-3 isogeny
Let E_t: y^2=x(x-1)(x-t), X=x-(1+t)/3 and y^2=X^3+A X+B, with A=t-(1+t)^2/3 and B=-2(1+t)^3/27+t(1+t)/3.
The 3-division polynomial is psi_3(x)=3x^4-4(1+t)x^3+6t x^2-t^2. In Q[t]/Q, the element
e=(t^3-141t^2+427t-7)/192
is an exact root of psi_3. Put v=e-(1+t)/3, g=3v^2+A and b=v^3+Av+B. The normalized Velu quotient by {O,P,-P}, x(P)=e, is
X_3=X+2g/(X-v)+4b/(X-v)^2,
Y_3=y*(1-2g/(X-v)^2-8b/(X-v)^3).
Its differential pullback is dX/(2y), and its short coefficients reduce modulo Q to
A_3=A-10g=-3(t^2+14t+1)/4,
B_3=B-14(5v^3+3Av+2B)=(1+t)(t^2-34t+1)/4.
The generic Velu map equality is an exact polynomial multiple of the short 3-division polynomial; verified by the companion symbolic program.

## 2. Two independent maps to the same Frobenius target
In A_p put f=t^p. For p=5 (mod24), f=(7-5t)/(5-7t); for p=13 (mod24), f=(5-7t)/(7-5t). The earlier degree-2 isogeny to E_f has squared scale
s_2=-(1+f)/(2(1+t)).
For the new degree-3 quotient set s_3=-(2/3)s_2=(1+f)/(3(1+t)).
A direct exact quotient-ring calculation proves both
A_f=s_3^2*A_3, B_f=s_3^3*B_3
where A_f=f-(1+f)^2/3, B_f=-2(1+f)^3/27+f(1+f)/3.
Thus the two normalized isogenies, followed by explicit (square-root-extended) short-model isomorphisms, reach the SAME E_f but scale invariant differentials by different factors. Cartier naturality of Hasse invariants yields
H_p(f)=s_2^m H_p(t)=s_3^m H_p(t).
Their ratio satisfies (s_3/s_2)^m=(-2/3)^m=(-6/p). This equals +1 for p=5 (mod24), -1 for p=13 (mod24). In the inert class the two zero-order relations force H_p=0.

## 3. The crucial first-jet identity
Work in the local etale deformation of each CM branch, differentiate the isogeny families BEFORE specializing Q=0. For the degree-2 branch t=w^2, f_2=((1-w)/(1+w))^2, s_2=-1/(1+w)^2, let
d_2=df_2/dt=-4f(1+f)/((1-t^2)(1-f)),
alpha_2=d(log s_2)/dt=d_2/(1+f)-1/(1+t).
For the degree-3 branch, the root e(t) is continued by the implicit equation psi_3(e(t),t)=0; importantly, differentiate this implicit family rather than the CM residue representative:
e'=(4e^3-6e^2+2t)/(12e(e-1)(e-t)).
Differentiate A_{f_3}=s_3^2 A_3 and B_{f_3}=s_3^3 B_3 along this lift to solve for d_3=df_3/dt and alpha_3=d(log s_3)/dt.
Exact rational quotient-ring identities (checked for BOTH Frobenius-Mobius branches) give
d_3=-d_2,   alpha_2+alpha_3=-4h(t),
h(t)=(1+2t-7t^2)/(16t(1-t^2)).
For an explicit check, in the split chart modulo Q:
d_2=(398t^3-55433t^2+77036t+243)/24,
alpha_2=(t^3-136t^2-263t+618)/48,
alpha_3=(151t^3-21171t^2+48717t-27881)/576.
The corresponding inert chart coefficients and all exact symbolic checks are in the executed certificate.
The algebraic divisions are legitimate for the specified p: denominators in the two local maps and 3-division root have no residue obstruction for p=5 (mod8); possible exceptional primes from the relevant CM resultants are among 2,3,17,23, none in the stated class.

## 4. Proof of split cancellation, and of nonzero companion factors
Differentiating Cartier/Hasse naturality along either isogeny family yields
d_i*H_p'(f)=s_i^m*[H_p'(t)+m*alpha_i*H_p(t)] (i=2,3).
For p=5 (mod24), s_3^m=s_2^m. Adding the equations and using d_3=-d_2 gives
0=s_2^m*[2H_p'+m(alpha_2+alpha_3)H_p]
 =s_2^m*[2H_p'-4m h H_p].
As m=-1/2 (mod p), it follows that H_p'+h H_p=0, equivalently C_p=0.
The polynomial H_p has only simple zeros away from t=0,1: its characteristic-p hypergeometric differential equation is
t(1-t)H_p''+(1-2t)H_p'-(1/4)H_p=0,
and a multiple zero at such a regular point would make every Taylor coefficient of the degree-m<p polynomial vanish, contradicting H_p(0)=1. Every Q-root avoids t=0,+/-1.
Inert H_p=0 therefore implies H_p' nonzero and hence C_p=16t(1-t^2)H_p' nonzero on every root. Split C_p=0 together with H_p=0 would contradict the same simplicity, so H_p is nonzero on every root. QED.

## 5. Evidence and continuation
Executed 2026-11-05: exact symbolic checks of normalized generic degree-3 Velu, CM torsion, target scale and **both** opposing first-jet identities PASS. Independent quotient-ring coefficient checks: all 168 primes 5<=p<=5000 with p=5 (mod8), 85 split and 83 inert, PASS. The full executed local Python+SymPy checker is delivered alongside this report.
BRC: COMPOSE_APPLIED on the labeled degree-2 and degree-3 isogeny branches, preserving their *opposite tangent directions*, their differential scales, the signed Hasse jet, scalar a_p and character (-6/p); collapsing to a common final Frobenius value or squared norm prematurely erases the key first-jet cancellation. Classical Legendre is a scoped auxiliary observer, not a native six-axis P000 identification.
Next scientific unit: use the proved split-class zero law in the earlier Jacobi-Green-Wronskian p^2 source-preserving defect formula and derive a CM second-digit identity. Frozen D24 native p373 H0/B0 divided-power, [X]U mod p^2, semilinear direction, eta, kappa and Delta_p-R_p remain independent source obligations. Preserve prior canonical Source checkpoint, claim history, staging and contributor IDs. No new native CLAIM/OPEN/Result/independent acceptance is asserted.
Sources: previous CM first-jet/isogeny author notes at 2026-11-05, current docs/RESEARCH_CONTINUATION_PROTOCOL.md, classical normalized Velu isogenies and Cartier naturality.