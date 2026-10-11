# Independent paper review of the reverse Gauss certificate

Verdict: PASS for the conditional algebraic identities and independently
defined constructor interface. No new finite arithmetic, lifted campaign,
provider query, Task claim or formal acceptance was performed for this note.
The old UR/LIFT target remains OPEN.

Reviewed exact author file:
INDEPENDENT_SCALAR_REVERSE_GAUSS_LIFT_CERTIFICATE_PREPARATION.md,
11012B, SHA256 4de6c2ae746acf9dad026c334b9aa2998d49e3147606fc35422be4d3901d8869,
Git blob ebb3fa41d526d25376836e56ced06bdd7a87298b. I full-read these
final bytes after independently checking the author's earlier directed
derivative/recurrence formulas. This is shared nonblind mathematical review.
Author EM-ENTERPRISE-CB50ED supplied the reverse constructor; Root
EM-DVR-4C90FB supplied direction and paper checks. I independently verify
it and supply the explicit Green expansion and Euler compatibility below.

Task RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT,
publication TP2-21DFFFD4A8788C0FF5CA. Primary Source scientific checkpoint
d9f1cc87019d8b43e7058b98f545c025bc753cfe; exact primary proof SHA256
7a99a69226b5d726aac31bc558dd9ed2fbddb489000761f444da8b43027ab0bf.
Independent reflection review SHA256
a0c78dc319555c3c4ac60f6382ca2bceeb72b71a8a0d328dd17d761a476d8659;
q descent/precision review SHA256
d1d3ee4ed9519c9e043f32cd29e4b87a7132c0adbaab100ead2b53f6401ca6c1.
All those frozen files are unchanged.

## 1. The operator and forcing signs

For p=6m+1>=7, set t=1-2x, q=4x(1-x)=1-t^2 and A=t C(q).
Primes on C denote differentiation in its own w variable. Direct chain
rules give

    A'=-2C+4t^2 C',
    A''=-24t C'+16t^3 C''.

Substituting into D_H=x(1-x)d^2+(1-2x)d-2/9 yields

    D_H[t C(q)]=4t (D_C C)(q),
    D_C=w(1-w)d^2+(1-5w/2)d-5/9.

This is the Gauss operator with parameters (2/3,5/6;1), as their sum
plus one is 5/2 and their product is 5/9. For the geometric-series forcing,

    S_p=sum_(j=0)^(p-2)x^j=4(x-x^p)/q
       =2t[(1-q)^(3m)-1]/q.

These are polynomial identities: x-x^p is divisible by x(1-x), and
((1-w)^(3m)-1) has zero constant coefficient. The apparent quotients
do not introduce a pole or restrict the identity to q nonzero. Since
D_H A=-(2/9)S_p, cancellation in the polynomial domain gives

    D_C C=-[(1-w)^(3m)-1]/(9w)=sum_(j=0)^(3m-1)r_j w^j,
    r_j=-(-1)^(j+1) binom(3m,j+1)/9.

The cancellation of 4t is a polynomial argument, not division by t at
the ramification point x=1/2.

## 2. Backward definition, terminal equation and uniqueness

For C=sum c_j w^j, its operator coefficient at index j is

    (j+1)^2 c_(j+1)-(j+2/3)(j+5/6)c_j.

Set c_(3m)=0 and define c_j downward for j=3m-1,...,0 by

    c_j=((j+1)^2 c_(j+1)-r_j)/[(j+2/3)(j+5/6)].

In Fp, 2/3=2m+1 and 5/6=m+1. Their negative residues are 4m and
5m, strictly outside 0,...,3m-1. Consequently every division is by a
unit. For p=7, m=1, the actual indices are 0,1,2 while the two excluded
zeros are 4 and 5. The top coefficient equation is included by the
terminal c_(3m)=0; this is not just a truncated forward recurrence.

Subtracting two solutions of degree <=3m-1 and descending from the
same zero terminal coefficient proves uniqueness. The descended primary
carrier solves this equation with the same degree bound, so the new
constructor equals it. It is defined without I, H, a boundary seed,
alpha inverse, a target value or a discrepancy. Its theorem of equality
consumes the preceding forcing/reflection proof; the definition itself
does not consume the desired old target equality.

## 3. Independent M constructor and exact ODE

The root-power polynomials S_0(w)=2, S_1(w)=1,
S_n=S_(n-1)-(w/4)S_(n-2) satisfy
S_n(q)=x^n+(1-x)^n, because the two roots have sum one and product q/4.
Thus M=(1/2)sum b_n S_n is independently equal to L_sym, with coefficients
over the p-integral rationals. This S_n is distinct from S_p's geometric
series above.

The exact cutoff residual is D_H L=-A_last b_(p-1)x^(p-1), where
A_last=(p-2/3)(p-1/3). Reflection commutes with D_H, giving

    D_H L_sym=-(A_last b_(p-1)/2) S_(p-1)(q).

The already proved exact pullback D_H(M(q))=4(D_G M)(q) and injective
q substitution then give the author's exact equation

    D_G M=-A_last b_(p-1) S_(p-1)/8,
    D_G=w(1-w)d^2+(1-3w/2)d-1/18.

Wilson b_(p-1)/p^2=1 mod p and A_last=2/9 mod p imply
D_G M=-p^2 S_(p-1)/36 mod p^3. Neither this ODE nor its name supplies
the still unknown CM scalar evaluation required by UR.

## 4. Exact old target and scalar precision

I independently full-read both old returns through the GitHub connector
at Source d9f1cc87019d8b43e7058b98f545c025bc753cfe. The JT2 return
ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md
is 9953B, SHA256 54ab94a1899f649ae1488bececaa7c57aafbc89aef44bdd1e40cc0b45590e827,
blob cf36004694dc2c8c9134e2e1e989c076b88e4c03. The reflected return
ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md
is 10919B, SHA256 f2dde9c2d0411285d7cd449bd2853fae87b83b0c2a00cd4f57dcfcfe47a96483,
blob 3fedf7bef09b426037840721855f9a9d05558a0b. Both are under
research_returns/. Complete connector observations are preserved locally.

They fix B_i=a_i 2^(-i), h=sum (12i+1)B_i=g+6f'(1/2), and independently
fix the OLD scalar

    R_p=2 sum_(i=1)^m B_i sum_(r=1)^i [1+6(i-r)] D_r mod p,
    D_r=2^(r-1)(r-1)!^2/[18(5/6)_r(2/3)_r].

The reflected return calls D_r by C_r and calls g itself G_p; those old
symbols must not be confused with the new polynomial C_p or G=g/p.

The new memo's M/C scalar identities match the separately checked q
preparation: at target classes, writing M_0=M(1/2), M_1=M'(1/2),
alpha=H'(x_+)/s, beta=A(x_+)/s and tau=T(x_+),

    G=M_0/p+p C(1/2)/4 mod p^2,
    h=M_0+6M_1 mod p^2,
    C(1/2)=-2 beta,    M_1=-alpha/2 mod p,
    C(1/2)M_1=alpha beta=-4 tau,
    G h=U-6p tau,
    U=(M_0/p)(M_0+6M_1) mod p^2.

M_0 needs precision p^3 before division by p, M_1 needs p^2 and the
last bilinear correction needs only Fp. In the marked form W=L+6L'/q'
equals h mod p^2, so its trace product U=(1/2)Tr[(L/p)W] is exactly
this base-field scalar. The sign and trace normalization agree.

The independently fixed old equality G h=1+p R_p becomes

    U=1+p[R_p-(3/2)C(1/2)M_1] mod p^2.

Thus the author's INDEPENDENT-LIFT sign is correct. UR remains U=1
mod p. Only after UR may (U-1)/p be formed as the old divided lift;
then LIFT asks (U-1)/p-6tau=R_p mod p. The constructors define both
sides independently, but this review does not prove they are equal.

## 5. Green kernel and Euler compatibility as next proof interfaces

Unwinding the backward recurrence, with N=3m-1, gives

    c_j=-sum_(ell=j)^N r_ell
          [prod_(a=j)^(ell-1)(a+1)^2]
          /[prod_(a=j)^ell(a+2/3)(a+5/6)].

All displayed factors are units in the indicated ranges. In particular

    c_0=sum_(r=1)^(3m) (-1)^r binom(3m,r)
              (r-1)!^2/[9(2/3)_r(5/6)_r]
       =sum_(r=1)^(3m)(-1)^r binom(3m,r)2^(2-r)D_r.

In this last identity D_r's same exact formula is extended to r<=3m;
its denominators remain units. The OLD R_p itself still uses r<=i<=m.
This shared kernel suggests a finite Green/telescoping comparison, but
it is not an assertion that the two distinct observers already agree.

The new Gauss parameters are the Euler complements of (1/6,1/3):
(1-1/3,1-1/6)=(2/3,5/6). More concretely, for k=(p+1)/2 and
J(w)=(1-w)^k, direct operator conjugation in Fp[w] gives

    D_G[J C]=J D_C C.

Here k=1/2 mod p is exactly the Euler exponent. Combining the forcing
with k+3m=p gives

    D_G[J C]=-[1-w^p-(1-w)^k]/(9w).

The apparent quotient is again polynomial. It agrees with the independently
checked cutoff residuals, because the root-power identity in Fp[w] is

    w S_(p-1)(w)/2=1-(1-w)^k.

Indeed w=4xy, x+y=1, and Frobenius gives
2xy(x^(p-1)+y^(p-1))=2(yx^p+xy^p)=1-t^(p+1).
Thus the M residual, C forcing and original Gauss cutoff have consistent
signs and precision through p^3. This is a finite polynomial Euler/Green
certificate; it is not an imported ordinary-unit-root or period formula.

Next proof work may seek an independently normalized reciprocity or
finite adjoint/telescoping evaluation of U, then the fixed OLD obstruction.
It must derive these evaluations rather than name the product a cup pairing
or fit its normalization. Full marked branches, derivatives, Jacobians,
exact lifts and h/omega tags remain. No global X6 propagation, raw-period
normalization, UR/LIFT or mother-objective completion is asserted.

Researcher-ID: EM-ENTERPRISE-3F2857 / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
