# The descended carrier and the scalar JT2 product

Status: PROVED_CONDITIONAL_ALGEBRAIC_PREPARATION / NO_NEW_LIFT_CAMPAIGN.
This is a separate paper consequence of the already proved p^3 carrier
and its independently reviewed global reflection condition. It introduces
no new Task, branch, provider query, numerical campaign or formal acceptance.
The immutable primary proof and earlier supplements retain their exact bytes.

Task RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT,
publication TP2-21DFFFD4A8788C0FF5CA. Primary scientific Source checkpoint:
d9f1cc87019d8b43e7058b98f545c025bc753cfe. Its exact main proof is
HESSE_P3_SECOND_DIGIT_PROOF_FINAL.md, 14441B, SHA256
7a99a69226b5d726aac31bc558dd9ed2fbddb489000761f444da8b43027ab0bf.
Consumed independent reflection supplement: 10042B, SHA256
a0c78dc319555c3c4ac60f6382ca2bceeb72b71a8a0d328dd17d761a476d8659.
Wronskian supplement: 6262B, SHA256
ee3f73f6b81985333694ce83d826e11e1db9902681be6bff490e2a2ab9430b1e.

The old h observer was independently full-read through the GitHub connector
at the same immutable Source commit, path
research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md,
9953B, SHA256 54ab94a1899f649ae1488bececaa7c57aafbc89aef44bdd1e40cc0b45590e827,
Git blob cf36004694dc2c8c9134e2e1e989c076b88e4c03. This confirms precisely
B_k=a_k 2^(-k), g=sum B_k and h=sum (12k+1)B_k. The new correction
polynomial below is called C_p, to avoid collision with the independently
fixed old JT2 target scalar R_p.

## Construction and descent

Fix p=6m+1>=7, t=1-2x, q=4x(1-x)=1-t^2. The full Fp correction
A=I-I(1)H/2 is odd under x -> 1-x. Hence the odd polynomial
A((1-t)/2) has the unique form t c(t^2). Define C_p(w)=c(1-w).
Then

    A(x)=t C_p(q) in Fp[x],       deg C_p <=3m-1.

This definition uses the already independent Fp I/H recurrences alone.
Let Lsym=(L_p(x)+L_p(1-x))/2, over the exact p-integral rationals.
After x=(1-t)/2 it is even in t. It therefore uniquely descends to
an exact p-integral rational polynomial M_p(w):

    Lsym(x)=M_p(q),              deg M_p <=3m.

Both constructions are coefficient identities, not fits to a marked point.
They need no division by t when evaluated at its zero: oddness first
guarantees polynomial divisibility by t, and the resulting quotient is even.

The reflected difference proved earlier is E-R E=A, with
E=(f_p(q)-L_p)/p^2 mod p. Thus

    (L_p-L_p(1-x))/2 = -p^2 A/2 mod p^3,
    f_p(q)=Lsym+p^2(x^p-1/2)A mod p^3.

In Fp[x], x^p-1/2=-t^p/2. With k=(p+1)/2=3m+1 this gives

    f_p(q)=M_p(q)-(p^2/2)(1-q)^k C_p(q) mod p^3.

The substitution map w ->4x(1-x) is injective also over Z_p/p^3:
the leading coefficient of a nonzero polynomial of degree d acquires
the unit multiplier (-4)^d at degree 2d. It cannot vanish or be cancelled
by lower terms. Therefore the uniform descended identity is

    f_p(w)=M_p(w)-(p^2/2)(1-w)^k C_p(w) mod p^3.       (Q3)

Any coefficient lifts of C_p give the same identity. The degrees are
consistent: k+deg C_p <=(3m+1)+(3m-1)=6m=p-1, the original cutoff.
For p=7, M has degree <=3, C has degree <=2, and k=4.

## Ramification jets

The explicit difference in (Q3) has a factor (1-w)^k. Hence for every
integer 0<=r<k,

    f_p^(r)(1)=M_p^(r)(1) mod p^3.

This follows by formal differentiation of a coefficientwise congruence;
no inference from finitely many numerical points is involved. The equality
also holds for normalized Taylor coefficients, since r<p and r! is a unit.
At r=k the factor no longer forces zero, so the stated range is essential.
This extends the x=1/2 value consequence to a finite high-order jet
interface at the ramification value w=1, without dividing by q'=0.

## Target value and trace at the required precision

Now restrict to the inherited target classes p mod 24 in {13,19}.
CM0 supplies p|g=f_p(1/2), and (2/p)=-1. Write

    M_0=M_p(1/2),       M_1=M'_p(1/2),       C_0=C_p(1/2).

Equation (Q3) implies p|M_0. Euler's criterion gives
2^(-k)=-1/2 mod p; division of (Q3) by p therefore yields

    G=g/p=M_0/p+p C_0/4 mod p^2.                       (G2)

The exact rational M_0 must be known modulo p^3 before dividing by p.
Only C_0 modulo p is needed in its term multiplied by p. Merely knowing
M_0/p modulo p would erase the second digit and is insufficient.

For the exact two branches x_+=(2+s)/4, x_-=(2-s)/4, s^2=2,

    M_0 = (L_p(x_+)+L_p(x_-))/2

as an exact rational identity. Thus M_0/p is precisely
Tr[L_p(x_+)/p]/2. It is the old exact quadratic trace, computed instead
by the descended base-field polynomial. The branch lifts are not identified
or discarded in this equivalence.

At x_+, t=-s/2. Write A(x_+)=I(x_+)=beta s and
H'(x_+)=alpha s, with alpha a nonzero Fp scalar. Then

    C_0=-2 beta,        M_1=-alpha/2 mod p.

The first identity is A=t C. For the second, M_p(q)=Lsym and
M_p(q) mod p=H(x); differentiating gives q' M'_p=H'. At x_+,
q'=-2s is a unit, so M_1=H'/q'=-alpha/2. This requires only residue
values, not an additional lifted derivative normalization.

The Wronskian T=x(1-x)(I'H-IH') is invariant under reflection.
Its independently defined CM value tau=T(x_+) is a scalar in Fp and
equals T(x_-). Since x(1-x)=1/8 and H=0,

    tau=-(1/8)(beta s)(alpha s)=-alpha beta/4,
    C_0 M_1=alpha beta=-4 tau mod p.

Consequently p C_0/4=2p tau/alpha. This verifies precisely the earlier
trace correction and its sign: (G2) equals
G=Tr[L_p(x_+)/p]/2+2p tau/alpha mod p^2.

## The old weighted observer and scalar product

The independently read old definition gives exactly

    h=sum_(n=0)^(p-1)(12n+1)a_n 2^(-n)
      =g+6 f'_p(1/2).

Formal differentiation of (Q3) preserves coefficientwise p^3 precision.
The entire correction and its derivative are multiples of p^2, so

    h=M_0+6M_1 mod p^2.

Combining this with (G2), and using p|M_0, gives

    G h=(M_0/p)(M_0+6M_1)+(3p/2)C_0 M_1
       =(M_0/p)(M_0+6M_1)-6p tau mod p^2.             (U2)

The omitted p C_0 M_0/4 term is zero modulo p^2 because M_0 is
divisible by p. The coefficient 6 here is tied to the old weight 12n+1;
it must not be replaced by the observer with weight 6n+1.

For (U2), M_0 needs precision p^3, M_1 precision p^2, and tau only
precision p. These are base-field rational/residue inputs. No exact
quadratic extension lift is needed to compute this particular scalar
product, although the complete marked extension states remain available
for future observers. Also h mod p=-3 alpha is a unit by SIMPLE.

The old JT2 condition is still G h=1+p R_p mod p^2, with R_p fixed
independently by its original taskbook. Equation (U2) computes the left
side without inventing a new target. UR still asks whether this scalar is
1 modulo p; only after UR is proved may its divided first digit be
compared with the independently fixed R_p for LIFT. Defining R_p from
(U2), fitting a period constant from it, or claiming UR/LIFT proved by
this representation would be circular.

## Contribution and retained state

I proposed the q descent after the independent reflection review. Root
EM-DVR-4C90FB independently checked the descent, ramification jet range,
precision and scalar-product algebra and requested this preparation.
Author EM-ENTERPRISE-CB50ED confirmed the old h definition and independently
checked the M/C identities. This is shared paper development, not a blind
review, not exclusive discovery and not an additional finite regression.
No old or new lift campaign was run for this note.

The new interface is a finite arithmetic certificate for the stated value,
weighted derivative and scalar product. It preserves the original two
branches, signed H/I/A derivatives, Jacobians, exact lifts and h/omega^r
marks. It does not claim the base-field scalar determines all future
marked observations, does not collapse the native X6 state, and does not
resolve external raw period normalization. UR, LIFT and the mathematical
mother objective remain OPEN.

Researcher-ID: EM-ENTERPRISE-3F2857 / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
