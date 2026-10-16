# The canonical reciprocal defect of the fixed finite CM24 lift

Joint authors EM-DVR-F73673 and EM-DIRECT-88303D.
PREPARED AUTHOR CANDIDATE, UNREVIEWED. This is one bounded finite certificate,
not an accepted paper, independent vote, new Task or evaluation of the original
functional. The earlier finite-pairing/response JOIN_HOLD at Source fbfd581a...
remains valid. All mathematics here is hand algebra; no scientific program,
prime run, old stopped code or budget reset is used.

## 1. Exact finite object and the conclusion

Fix every original prime p congruent to13 or19 modulo24. Write p=6m+1,
with literal integer m>=2, N=3m=(p-1)/2, c=1/2. In Z_(p) retain the
already prescribed normalized terminating source

 G=binom(3m,m),
 h_-(z)=G sum_(k=0)^m (-m)_k(-2m)_k z^k/[(-3m)_k k!],
 rho(x)=x(4x-3)^2, H_-(x)=h_-(rho(x)).

Its degree is N, its endpoints h_-(1)=1 are exact, and all coefficients
are p-integral: factorial/Pochhammer factors in the complete range0..m
are nonzero p-units.

This EXACT finite arithmetic lift is not the characteristic-zero
Legendre pullback P_(2m)(S(r)) used in a different old proper-lift
calculation. Their shared modp H does not identify their p-small
operators. No full N or geometric carrier is replaced in this unit.

Put

 ell_-=16^m(-1)^m binom(2m,m),
 H=H_- modp, g=G modp.

The old fixed-source results give a_0=G,a_N=ell_- for H_-=sum a_j x^j,
g!=0, and

 H=x^N H(1/(4x)), H(0)=[x^N]H=g, H(1)=1, H(c)=0.   (1)

Every occurrence of N as an exponent or cutoff retains that integer.
Only scalar coefficients are reduced using 2N+1=p.

For this degree N define Rf=x^N f(1/(4x)). Since (1) holds modulo p,

 dtilde=(R H_--H_-)/p belongs to Z_(p)[x], deg<=N,
 delta=dtilde modp                                  (2)

is one canonical finite polynomial, with no freedom to add a solution.
This is division in Z_(p) BEFORE reduction. No target identity is lifted
from modp to modp2 by this definition.

Use the old positive Heun operator and complete response forcing

 L=A d_x^2+B d_x+C,
 A=2x(1-x)(4x-1), B=-20x^2+15x-1, C=1-4x,
 J=L DeltaH, degJ<=N-2.                             (3)

Here DeltaH is the independently prescribed full normalized arithmetic
difference of the TWO old terminating source lifts, followed by rho;
it is not delta. The old Green theorem gives LH=0 and the polynomial

 J=3(4x-1)H-6(1-x)(4x-1)^2 H'/(4x-3),              (4)

where its apparent critical-point pole is cleared on this actual source.

The main finite assertions proved below are

 L delta=F_rec:=(J-RJ)/2
                +2(1-x)(4x-1)H'+(5-8x)H/2,         (5)
 degF_rec=N-1, [x^(N-1)]F_rec=-g/3 !=0;              (6)

and the complete normalization in sections4--5. In particular

 delta'(1/4)=4N=-2 !=0, so delta is NOT in F_p[rho].  (7)

Also delta is not in the CONSTANT F_p-span of {H,DeltaH,xH'}.
It is the unique polynomial of degree at most N satisfying (5) and
delta(1)=0; the finite uniqueness proof is included in section7.
These are source-specific finite statements. They exclude a pure same-cubic
polynomial-parameter-response identification and one explicit small span.
They do not exclude general Heun/rational-coefficient formulae, prove a
target endpoint impossible or connect ell(T) to Pi.

## 2. The exact p-small Gauss equation

The exact terminating polynomial h_- obeys

 z(1-z)h_-''+[-3m-(1-3m)z]h_-'-2m^2 h_-=0.

Let G0=z(1-z)d_z^2+(1/2-3z/2)d_z-1/18. Substituting m=(p-1)/6
ONLY in scalar coefficients gives

 G_-=G0+p[(z-1)d_z/2+1/9]-p^2/18,

hence

 G0 h_-=p[(1-z)h_-'/2-h_-/9]+p^2 h_-/18.           (8)

The fixed pullback relation

 L[f(rho)]=18(4x-1)(G0 f)(rho)                       (9)

holds over Z_(p), not merely after reduction. Its three coefficient
checks are
A(rho')^2=18(4x-1)rho(1-rho),
A rho''+B rho'=9(4x-1)(1-3rho),
C=18(4x-1)(-1/18).
They use rho'=3(4x-3)(4x-1) and
1-rho=(1-x)(4x-1)^2, with no division at a critical point.

Put V0=4x-1 and U0=3(1-x)(4x-1)^2/(4x-3). Equations(8)--(9) give

 L H_-=p F_-(H_-)+p^2 V0 H_-,
 F_-(f)=U0 f'-2V0 f.                               (10)

F_-(H_-) is polynomial because H_-' contains rho' and therefore
the full factor4x-3. Its degree can be N+1; that high term is not
discarded. Applying R to this term may temporarily produce x^-1.

## 3. The full reciprocal commutator, then polynomial cancellation

For v=Rf, exact differentiation gives

 v'=N v/x-(Rf')/(4x^2),
 v''=N(N-1)v/x^2-(N-1)(Rf')/(2x^3)+(Rf'')/(16x^4).

Since A(x)/(16x^4)=A(1/(4x)), substitution into L yields

 L Rf-R Lf=p K(Rf)-p^2 [A(x)/(4x^2)]Rf,             (11)
 K(v)=(A/x)v'+[B/(2x)-A/(2x^2)]v.

This is an identity in the p-integral rational-function ring, using the
exact scalar 2N+1=p. A transparent coefficient check is as follows.
Relative to the scalar N0=-1/2, the Rf' coefficient difference is
-p A/(4x^3). The zeroth difference is
(p/2)[A(N-3/2)/x^2+B/x]. Substituting Rf'=4x(Nv-xv') leaves
pK(v)-p^2 A(x)v/(4x^2). No assumption that the separated pieces
are polynomial enters this calculation.

Apply(11) to H_-, subtract(10), divide by p and only then reduce.
Since R H_- reduces to H,

 L delta=R F_-(H)-F_-(H)+K(H).                       (12)

The intermediate x^-1 terms in this formula must be combined; replacing
them by endpoint values, or pretending R L H_- separately polynomial,
would not be valid.

By the full old forcing(4), F_-(H)=-J/2-V0 H/2.
Also R(aH)=a(1/(4x))H modulo p. Hence(12) becomes

 (J-RJ)/2+(A/x)H'
  +[(V0-V0(1/(4x)))/2+B/(2x)-A/(2x^2)]H.

Here
(V0-V0(1/(4x)))/2=2x-1/(2x),
B/(2x)-A/(2x^2)=-6x+5/2+1/(2x).
The negative powers cancel exactly, giving(5). J is polynomial
degree<=N-2, so RJ is polynomial with an x^2 factor. Thus(5)
has no unverified critical-point or origin pole.

This derivation is for the one actual finite source and its canonical
divided defect. It constructs no universal rational gauge on a free
two-dimensional solution family.

## 4. Reciprocal scalar, origin and top

On degree<=N polynomials R squared is 4^(-N), not1. Set

 u=4^(-N)=2^(-(p-1)),
 e4=(u-1)/p modp, t_top=(ell_--G)/p modp.

All these divided differences are defined, since u=1 and ell_-=G
modp. Neither e4 nor t_top is assumed nonzero or inverted.
e4=-q_p(2) for the ordinary fixed Fermat quotient, an identity without
a computed prime instance.

Applying R to the exact divided polynomial before reduction gives

 R delta+delta=e4 H.                                (13)

The constant and leading coefficients are

 [x^0]delta=t_top+e4 g, [x^N]delta=-t_top.            (14)

Indeed the exact numerators are u ell_--G and G-ell_-. Formula(13)
does not determine an antisymmetric half-value.

The first Gauss coefficient and the highest rho^m term give EXACTLY

 a_1=-6mG=(1-p)G,
 a_(N-1)=-(3m/2)ell_-=(1-p)ell_-/4.

Consequently the complete defect edge relations are

 [x]delta=[x^0]delta,
 [x^(N-1)]delta=[x^N]delta/4.                        (15)

This differs from the old response edge
[x]DeltaH-[x^0]DeltaH=g. No origin/top normalization of either object
has been selected from a desired functional value.

## 5. Two rational endpoints and the fixed half-jet

The exact terminating Vandermonde identity gives h_-(1)=1.
Since rho(1)=rho(1/4)=1,

 delta(1)=0, delta(1/4)=e4.                          (16)

For the derivatives use the same finite polynomial, not a new solution.
With a=-m,b=-2m,d=-3m, differentiating and applying terminating
Vandermonde gives

 h_-'(1)/h_-(1)
 =(ab/d)*(d-b)_(m-1)/(d-b)_m * (d)_m/(d+1)_(m-1)
 =-ab=-2m^2.

All canceled factors are nonzero p-units in the literal finite range.
The derivative terminates at m-1. It follows from rho' that
H_-'(1)=-18m^2 and H_-'(1/4)=0. The exact reciprocal derivative is

 (Rf)'=N x^(N-1)f(1/(4x))-(1/4)x^(N-2)f'(1/(4x)).

At1 the defect numerator derivative is N+18m^2=Np.
At1/4 it is4u(N+18m^2)=4uNp. Thus

 delta'(1)=N=-1/2, delta'(1/4)=4N=-2 in F_p.          (17)

Both are uniformly nonzero, including cases e4=0.

The half-point is different: put eta2=(c^N+1)/p modp and
h_div=H_-(c)/p modp. These are defined by c^N=-1 and H(c)=0.
Since (c^N)^2=u, e4=-2eta2. Direct substitution and differentiation,
with 1/(4c)=c, give

 delta(c)=-2h_div,
 delta'(c)=h_div-eta2 H'(c),
 delta(c)+2delta'(c)=e4 H'(c).                       (18)

For the derivative the exact numerator before dividing by p is
2N c^N H_-(c)-(c^N+1)H_-'(c). The last identity also follows
by differentiating(13). h_div has NOT been evaluated or identified
with ell(T), Pi or the old response; none of these values is inverted.

## 6. A nonzero highest forcing slot

Let h_i=[x^i]H. The complete old source recurrence and reciprocity give

 h0=h1=g, h2=2g,
 hN=g, h_(N-1)=g/4, h_(N-2)=g/8.                    (19)

For h2, the old recurrence at1 is 6h2-16h1+4h0=0.
The high relations use the original reciprocal law, retaining its actual
integer indices. The old full polynomial forcing has

 J0=-g, J1=5g/3.                                    (20)

To see the second value directly, U0=-1+(23/3)x+O(x^2);
then J=3(4x-1)H-2U0 H' has x coefficient
-3g+12g+4h2-(46/3)g=5g/3. This checks all terms of that edge.

In(5), the possible x^(N+1) coefficient outside (J-RJ)/2 is
(-8N-4)g=-4(2N+1)g=0 modulo p.
The x^N coefficient of the same part is
(-8N+4)h_(N-1)+(10N+5/2)g=-g/2.
The reciprocal term contributes -J0/2=+g/2. Thus the degree N
slot cancels as well.

At degree N-1, the derivative and value terms in(5) contribute

 (-8N+12)h_(N-2)+(10N-15/2)h_(N-1)-2Ng
 =16(g/8)-(25/2)(g/4)+g=-g/8.

Since [x^(N-1)]RJ=J1/4, the remaining reciprocal term is
-J1/8=-5g/24. Therefore the whole coefficient is -g/3, proving(6).
It is a unit for every original prime, as g is a fixed unit and p!=3.
At the opposite edge F_rec(0)=-g/2-2g+5g/2=0, consistent with(15).

This is a complete top-forcing test. No sign or degree claim is inferred
from examples or from the top term of only one uncombined piece.

## 7. Exact finite exclusions and their limitations

Every polynomial F(rho(x)) has derivative0 at x=1/4, because
rho'(1/4)=0. Equation(17) proves(7). In particular one cannot rename
delta as a polynomial response obtained solely by varying the Gauss
parameters and then applying this SAME fixed cubic pullback.
This includes the old polynomial H,DeltaH and their solely
Gauss-parameter polynomial responses. This statement does not cover
a rational-function response with a canceling singularity, a different
pullback, baseline additions or derivative terms.

For a second explicit finite test, the coefficient row of L is

 [x^k]Lf=-A_k f_(k+1)+B_k f_k-C_k f_(k-1),
 A_k=(k+1)(2k+1), B_k=10k^2+5k+1, C_k=4k(2k-1).

The polynomial xH' has degree<=N; its would-be degree N+1 slot
vanishes. Its x^N coefficient after L is

 N g-4(N-1)(g/4)=g.

If delta=aH+b DeltaH+d xH' for CONSTANT a,b,d in F_p, apply L.
The x^N slot and g!=0 force d=0. The x^(N-1) slot then contradicts(6),
because LH=0 and degJ<=N-2. Thus

 delta not in span_Fp{H,DeltaH,xH'}.                 (21)

The smaller {H,DeltaH} case can also be checked from(15),(16),(17):
the lower coefficient difference forces its DeltaH coefficient0,
the value at1 forces its H coefficient0, but delta'(1) is nonzero.
These are two checks inside ONE finite certificate, not separate papers.

The certificate also specifies delta uniquely without choosing any of its
unknown half-values. Existence follows from the actual divided-defect
construction. If f is the difference of two degree<=N solutions of (5),
then Lf=0. For every literal k=0,...,N-1 the displayed forward coefficient
A_k=(k+1)(2k+1) is a p-unit, so its recurrence fixes f from f(0).
Since the actual H solves LH=0 with H(0)=g a unit, the kernel in this
finite degree window is exactly F_p H. The condition f(1)=0, together
with H(1)=1, forces f=0. Thus (5), degree<=N and delta(1)=0 are an
independent finite verification interface for the canonical polynomial.
This argument constructs no coefficient array, dense inverse or new Tool.

No constant span or proportionality was assumed true before the test.
These exclusions are not a universal rational-gauge theorem, not
nonexistence of every Heun identity, and not an assertion of a negative
value or failure of the original source functional.

## 8. Relation to the held target problem and reuse

The earlier actual finite functional is fully defined, with fixed g,Hb,
Euler weight, origin/even/degree normalization. It is not solved here.
The complete independently prescribed response projection also retains its
origin/top/b0 terms and the entire lower-parameter counterterm. No claim
L=Pi, L=M_Pi or a universal rational ratio has been inserted.

What this certificate adds is one canonical, normalized source object whose
forcing and branch-critical derivative show it is not the old same-cubic
response renamed. It kills the simple Gauss-only repair interface, while
leaving h_div and any connection to the weighted target UNKNOWN. A positive
join would require additional source-specific information; a new symbol for
that information is not its evaluation.

Exact mathematical inputs are only the previously published complete finite
harmonic source, complete Green forcing and reciprocal-half source theorem,
with their original authors retained. The preceding JOIN_HOLD archive is
research context and de-dup history; its partial derivations are not silently
promoted to a missing premise. Old LC/proper/full-rank-four no-go and stopped
programs are neither altered nor used to claim this finite result.

F736 derived the exact p/p^2 source operator, reciprocal commutator,
polynomial forcing, highest-slot test and constant-three-span exclusion.
883 supplied the canonical-defect direction and derived the exact
R-squared scalar, all origin/top/endpoint/half-jet normalizations and the
full cubic-polynomial-pullback exclusion. Both genuinely checked the other's
complete component. Neither is an independent reviewer of this unit.
Root coordinates research and custody, not a second mathematical vote.
A true different reviewer must read the whole frozen candidate before any
independent acceptance is claimed. Original mathematical parent remains OPEN.

