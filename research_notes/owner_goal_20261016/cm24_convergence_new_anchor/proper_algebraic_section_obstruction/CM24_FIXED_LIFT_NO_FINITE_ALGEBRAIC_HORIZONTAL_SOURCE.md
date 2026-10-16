# CM24: no finite-algebraic horizontal source in the fixed characteristic-zero lift

2026-10-16 UTC. Author EM-DIRECT-88303D, direct TASK_RESEARCH.
Own session/activity pins and exact dependencies accompany this paper.
Root coordinates process and fairness only.

**Result.** The frozen proper rank-two connection has no nonzero
horizontal vector over ANY finite algebraic extension of K(r).
Combining this new proper-block calculation with the old, consumed
kernel residue lemma, the fixed full rank-four carrier has only the
constant V-direction as algebraic horizontal vectors. In particular
its prescribed mod-p source section, whose z coordinate is1, cannot
become an exact characteristic-zero horizontal algebraic section by
passing to a finite cover. This excludes one proposed kind of source
lift, not analytic periods, a geometric module, a Frobenius comparison,
an inhomogeneous source, or a different characteristic-zero connection.

## 1. Fixed object and the genuine scope difference

Use the exact characteristic-zero lift already fixed in the reviewed
V2 relative-extension and full log-residue papers. The coefficient
field is K=O[1/p], with O as in those papers. Keep each original prime
p=13 or19 mod24 and the exact chosen integral baseline

    N=(p-1)/2, s_0=1-2g,
    H_b(x)=g(1+x^N)+(s_0/5)(4x+x^(N-1)), H_b(1)=1.

Put S(r)=4r^3-3r and

    A(s)=[[-(2s-1),-1],[-(4s-5),2s-1]]/[6(s^2-1)],
    w=(8r^p-4r)/(1-r^2).

The full column X=(Y_1,Y_2,z,V)^T satisfies

    Y'=S' A(S)Y, z'=0,
    V'=w Y_1-w H_b(r^2)z.                            (1)

All derivatives in (1) are in r. Both full source terms are retained.
The fixed proper quotient is Y; its kernel is the already reviewed
z'=0,V'=d z, d=-w H_b(r^2). That kernel's logarithmic residues and
finite-cover nonexactness are consumed below, not claimed as new.

The old characteristic-p polynomial source-image obstruction concerns
a specified degree/cut and forcing image over F_p. The old rational
trace obstruction concerns a simultaneous full-system parameter gauge.
The known p-small lift defect kills a particular naive polynomial lift.
None of those statements is the all-finite-algebraic-cover homogeneous
claim proved here. This bounded distinction is recorded with exact
pins in SOURCE_AND_REUSE.json; no global novelty claim is made.

The word FIXED is essential. If n=(p-1)/3, the different equation
(1-s^2)y''-2s y'+n(n+1)y=0 has its usual polynomial P_n(s).
Its coefficient differs from -2/9 by p(p+1)/9. It is not the frozen
characteristic-zero proper connection in (1), despite the same mod-p
reduction. This paper does not exclude such a change of lift.

## 2. Exact scalar reduction

Let L be any finite extension of K(r) and extend d/dr uniquely to L;
characteristic zero makes this extension separable. Regard K(s) as
the subfield with s=S(r). The map is finite of degree3 and S' is a
nonzero field element, so delta_s=(1/S')d/dr defines the extended
s-derivation. If Y satisfies (1), then delta_s Y=A(s)Y.

Writing f=Y_1, the first row gives

    Y_2=6(1-s^2)delta_s f+(1-2s)f.                    (2)

Differentiate (2) and substitute the second row of A. The resulting
equation is exactly

    (1-s^2)delta_s^2 f-2s delta_s f-(2/9)f=0.         (3)

For a direct sign check, the derivative of (2) is
6(1-s^2)f''+(1-14s)f'-2f, whereas its second-row value is
(1-2s)f'-(2/3)f. Their equality, divided by6, is (3).
If f=0, (2) gives Y_2=0. It therefore suffices to prove that (3)
has no nonzero algebraic solution over K(s).

## 3. Local orders of an algebraic solution

Suppose f is a nonzero algebraic solution. Extend constants to an
algebraic closure Kbar of K and choose a finite field over Kbar(s)
containing it. At a place over any base point, the completed local
field has a uniformizer u with s-a=u^e (or x=1/s=u^e at infinity),
after a formal change of uniformizer. This uses an e-th root of a unit
in characteristic zero, not a p-adic integrality assertion. Hence
f has a Laurent expansion whose leading exponent relative to s-a
or x is a rational number nu=m/e. A leading coefficient is nonzero.

All orders in this section are geometric Laurent orders with field
coefficients. They are not the p-adic coefficient valuation; in
particular no ring O[[t]] is treated as a DVR.

At a finite point a different from +1,-1, a pole would give nu<0.
The lowest exponent in (3) is then nu-2, with coefficient

    (1-a^2) nu(nu-1) times the leading coefficient.

It is nonzero. The other terms have strictly larger order, so they
cannot cancel it. There is no pole at such a point, ramified or not.

At a=+1 or-1, write h=s-a. The leading part of 1-s^2 is -2a h.
If nu<0, the least order is nu-1 and the combined second- and
first-derivative coefficient is

    -2a[nu(nu-1)+nu]=-2a nu^2,

again nonzero. The last term in (3) has order nu and cannot cancel
it. Thus f has no pole over either singular finite point either.

At infinity put x=1/s and f(s)=F(x). Exact substitution transforms
(3) into

    x^2(x^2-1)F''+2x^3 F'-(2/9)F=0.                 (4)

For F with leading term c x^nu, the coefficient of the lowest order
x^nu in (4) is

    -[nu(nu-1)+2/9]c=-(nu-1/3)(nu-2/3)c.

Higher terms of F have strictly higher order; the other contributions
of its leading term have order nu+2. Thus at EVERY place above infinity
the leading exponent is exactly1/3 or2/3.
In particular f has a strict zero there. If the ramification index
does not allow either fractional exponent, that place already gives
a contradiction; no ramification choice avoids strict positivity.

## 4. A field-norm contradiction without a monodromy assumption

Take a finite normal closure M/Kbar(s) containing f. The derivation
extends uniquely, so every Kbar(s)-conjugate of f also satisfies (3).
Each conjugate has no pole at any finite place of M by section3,
and has positive order at every place over infinity. Their product,
with the multiplicities of the field norm, is the nonzero rational
function B(s)=Norm_(M/Kbar(s))(f).

At every finite base point B has nonnegative order, since its
pullback is a product of functions of nonnegative order. Thus B is
a polynomial in s. At infinity its order is positive, since the
order of every nonzero factor is positive. But a nonzero polynomial
has order at infinity equal to minus its degree, never positive.
This is a contradiction.

This proves no nonzero algebraic solution of (3) exists. It uses
neither a complex analytic branch nor a claimed differential Galois
group. Applying (2) proves

    THEOREM A. For every finite L/K(r), the proper block of (1)
    has zero horizontal-vector space over L.                       (5)

The same conclusion holds after any finite algebraic base cover,
without a degree bound, a chosen pole ansatz or an unramified-cover
hypothesis. It is still only a statement about this fixed connection.

## 5. Full carrier and the source-lift stopping condition

Let C_L be the constants of (L,d/dr), and let X in L^4 satisfy (1).
Theorem A forces Y=0. Then z is a constant in C_L. If z were nonzero,
V/z would be algebraic over K(r) and would satisfy (V/z)'=d.
The consumed Kummer input proves d dr has residue2 at r=+1 and-1,
and after any finite cover its pullback has nonzero residue2e.
A meromorphic derivative has residue zero. Thus z=0, and then V
is in C_L. Conversely every such constant V gives a solution. Hence

    COROLLARY B. Horiz_L(1)=C_L*(0,0,0,1)^T.                       (6)

The source projection in the old exact mod-p section is
(P_n(S), e_P(S),1)^T, with its full polynomial primitive in the fourth
coordinate. It is not in the V-only direction. More decisively, its
z coordinate is1. Any proposed characteristic-zero horizontal lift
over a finite algebraic cover, with a well-defined reduction whose
z coordinate is1, would have nonzero z before reduction. This
contradicts (6). The theorem needs no unspecified integral model:
the statement is conditional on the proposed reduction being defined.

The new exclusion covers all finite algebraic degrees, not merely
the old polynomial's particular nonzero lift defect. It does not
make a statement about the value of the actual scalar source or
about Y/Z/kappa. In particular poles of the isolated kernel cannot
be assigned to the mod-p source primitive by forgetting its proper
coordinates. The old source has its own exact cancellations.

## 6. What a surviving bridge must supply

A bridge preserving (1) cannot replace the prescribed source section
by an algebraic exact horizontal lift on a finite cover. It may
instead use genuinely transcendental analytic/logarithmic horizontal
data, keep an explicit inhomogeneous lift defect, or change the
declared characteristic-zero connection and prove the required
comparison to the original source. No one of those repairs is
constructed or assumed here.

A geometric de Rham connection need not have nonzero algebraic
horizontal sections; its periods can be transcendental. A Frobenius
comparison is a horizontal morphism between two differential modules,
not a horizontal vector in one module. Consequently (5)-(6) do not
disprove an actual proper/global Frobenius comparison, a geometric
realization, the earlier explicit kernel comparison, or the original
target identity. In particular they do not select the ordinary-origin
comparison constant k or any boundary constant from a primitive value.

All accepted old units and the frozen9986B kernel-transport theorem
remain unchanged. P000/Heartbeat native X6 remains the project basis;
these are external arithmetic differential-module observers, with
no new native axes, physical time, discarded source channel or
positive-support-to-signed inference.

Paper derivation only; no scientific program, solver, prime sample,
new Task, Native result/review vote or parent closure. A distinct
nonauthor must review this new unit on its own frozen bytes.
Parent Goal remains OPEN.

Researcher-ID: EM-DIRECT-88303D / TASK_RESEARCH

