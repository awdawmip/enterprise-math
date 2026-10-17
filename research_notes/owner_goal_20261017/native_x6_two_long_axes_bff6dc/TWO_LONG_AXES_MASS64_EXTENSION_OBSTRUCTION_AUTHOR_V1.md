# Two long axes: a forced mass93 move in a genuine two-state fiber

Same-family RESULT_ONLY / COMPOSE author record.
Sole new mathematical author: BFF / EM-DVR-BFF6DC.
Original session MCP-47562f9f432d4978a7bea0dd60ecc4aa,
DA-144D0C4639CACEEE75DC; no Researcher RA.
LOCAL_UNREVIEWED: no new author Source or independent whole review.

## 1. Exact finite question and conclusion

Keep the original six-coordinate discrete chart and the SAME seven
joint coset readouts: six coordinate-axis coset sums and the diagonal
coset sum for Z(1,1,1,1,1,1). These are full joint coset readouts,
not only six one-coordinate marginals. The ambient spatial semantics
are unchanged; no Native time or evolution law is introduced.

The new fixed box is

    B={0,1,2,3}^2 x {0,1,2}^4.                         (1)

A configuration is any nonnegative integer array supported in B.
A fiber comprises all such configurations having all seven readouts
equal. Every intermediate state of a connecting path must stay
nonnegative at every actual site and supported in B. A literal move
is an integer zero-readout array applied with either sign. Its mass
is mu(P)=||P||_1/2; zero readouts imply zero total mass.

We give an explicit zero-readout P of mass93 such that P^+ and P^-
form their ENTIRE nonnegative fiber. Consequently every palette
universally connecting all fibers in (1) must include P up to sign
as an actual step, and its maximal move mass is at least93.
In particular the original single-long-axis mass64 bound does not
extend to this two-long-axis box.

We do NOT claim that93 is the sharp universal threshold in (1),
do not construct its entire connecting palette, and do not classify
all its indispensable moves. The lower bound also applies if moves
are represented by translated templates: some actual applied step
must be P or -P and therefore has the same mass93.

The proof is finite integer algebra and actual-site nonnegativity.
It does not rely on a previously accepted long-axis theorem or on
the mere number of terms in a proposed generating polynomial.

## 2. The full integer kernel in this exact box

Write x=X_1, y=X_2, and Z=(Z_1,Z_2,Z_3,Z_4) for the other four
coordinate variables. Set

    U=Z_1 Z_2 Z_3 Z_4,
    A=product_(i=1)^4(Z_i-1),
    G=(xyU-1)(x-1)(y-1)A.                              (2)

Work in the integer Laurent ring in all six variables. The kernel
of an axis-coset readout is (X_i-1): grouping by cosets, or integer
monic division, proves that a signed finite array has zero sums
on those cosets precisely when its Laurent polynomial is divisible
by X_i-1. The kernel of the diagonal-coset readout is (D-1), where
D is the product of all six variables. Its quotient ring is an
integer Laurent polynomial ring in five variables, by solving for
one variable as the inverse of the other five's product.

All seven generators are prime, because their quotient rings are
domains. No two divide each other: evaluating one variable at1,
or making the diagonal substitution, leaves each different
generator nonzero. Successively removing the prime factors proves

    zero all seven readouts <=> P=GQ
    with Q an integer Laurent polynomial.             (3)

This uses primality, not a false pairwise-comaximality assertion.
The Laurent ring is a domain, so Q is unique.

For each variable, the minimum and maximum exponents in a product
add: the extreme coefficients multiply nontrivially in the
integral Laurent ring of the remaining variables. G has minimum0
and maximum2 in every variable. Thus, for a nonzero P supported
in (1), (3) forces Q to have exponent0 in every Z_i and exponent
in {0,1} in both x and y. In other words

    Q=q_00+q_10 x+q_01 y+q_11 xy, q_ab in Z.            (4)

Conversely every (4) gives an array in the zero-readout kernel
supported in B. P=0 corresponds to Q=0.

Put

    H=(x-1)(y-1)Q.                                    (5)

It is supported on {0,1,2}^2 and has zero sum in every row and
every column. These assertions follow by evaluating x=1 and y=1;
they are integer identities. Then

    P=(xyU-1)HA.                                      (6)

We use the row/column constraints below as necessary conditions
for every possible configuration in the fiber. No assumption is
made that all such tables independently satisfy the remaining
actual-site inequalities.

## 3. A particular six-cycle table

Take the concrete integer polynomial

    Q_0=1+x+xy,
    H_0=(x-1)(y-1)Q_0
       =1-y-x^2+xy-xy^2+x^2y^2.                       (7)

With x as row index and y as column index, its table is

             y=0   y=1   y=2
       x=0    1    -1     0
       x=1    0     1    -1
       x=2   -1     0     1.

This table has zero row and column sums and ||H_0||_1=6.
Its six nonzero positions form one bipartite six-cycle.

Let

    P_0=GQ_0=(xyU-1)H_0 A,
    f=P_0^+, g=P_0^-.                                 (8)

Both nonnegative arrays are supported in B. Their seven readouts
coincide by (3). The rest of the proof establishes their ENTIRE
fiber and the exact mass of their difference; it does not assume
that a six-cycle alone implies a nonnegative obstruction.

## 4. All actual-site types and the two-state proof

The supports of A and UA in the last four coordinates are
{0,1}^4 and {1,2}^4, meeting at the single site e=(1,1,1,1).
Let epsilon_a be the coefficient of A at a in {0,1}^4, and
gamma_b the coefficient of UA at b in {1,2}^4.
The coefficient at e is +1 in BOTH A and UA, because there are
four remaining axes. This parity differs from the five-axis
overlap in the old single-long-axis problem and must not be
silently copied from it.

For an arbitrary H in (5), formula (6) gives exactly

    P_H(i,j,a)=-epsilon_a H(i,j),
       a in {0,1}^4 minus {e};

    P_H(i,j,b)=gamma_b H(i-1,j-1),
       b in {1,2}^4 minus {e};

    P_H(i,j,e)=H(i-1,j-1)-H(i,j).                     (9)

Extend H by zero outside {0,1,2}^2. Sites outside these two last-
coordinate cubes are zero. Each exclusive cube has15 sites.
In the lower exclusive cube the positive epsilon group has7 sites
and the negative group has8, so BOTH signs really occur.
The upper exclusive cube likewise has7 positive and8 negative
gamma sites. These counts follow from the sixteen coefficients
of product(Z_i-1), eight of each sign, with the common positive
site removed.

Now take ANY nonnegative configuration h with the same readouts
as f and support in B. By the COMPLETE integer kernel in Section2,

    f-h=P'=(xyU-1)H'A,

where H' is supported on {0,1,2}^2 and has zero row and column
sums. Nonnegativity at the lower exclusive sites in (9) gives
the following necessary restrictions, position by position:

    H_0(i,j)=0  => H'(i,j)=0;
    H_0(i,j)=1  => 0<=H'(i,j)<=1;
    H_0(i,j)=-1 => -1<=H'(i,j)<=0.                    (10)

For example when H_0=1, the lower epsilon=+1 sites have f=0,
forcing H'>=0, and the epsilon=-1 sites have f=1, forcing
H'<=1. The other cases are obtained with the same actual signs.
Thus no fractional quotient, missing sign group or projected
positivity assertion is used.

Restrictions (10) confine H' to the six-cycle support of H_0.
Let H'(0,0)=a. Zero row0 gives H'(0,1)=-a. Zero column0 gives
H'(2,0)=-a. Zero column1 then gives H'(1,1)=a; zero row1 gives
H'(1,2)=-a; zero row2 gives H'(2,2)=a. The last column sum is
automatically zero. Hence

    H'=aH_0, a an integer, 0<=a<=1.                   (11)

There are exactly two possibilities: H'=0 or H'=H_0, giving
h=f or h=g. The upper-exclusive and common-site inequalities
cannot introduce an additional candidate; the two candidates
are already the actual arrays f=P_0^+ and g=P_0^-, so BOTH
satisfy ALL actual-site inequalities. This proves the exact
two-state fiber without claiming that the lower-site necessary
conditions alone characterize arbitrary fibers.

By uniqueness in (3)-(5), H'=0 or H_0 indeed gives P'=0 or P_0.
No hidden different quotient or extra signed configuration can
remain. We have proved

    fiber_B(f)=fiber_B(g)={f,g}.                       (12)

## 5. Exact mass and the forced step

The exclusive lower sites in (9) contribute
15||H_0||_1=90 to ||P_0||_1. The exclusive upper sites contribute
the same90, since translating x,y does not change the norm.
For the remaining common site, the full polynomial is

    xyH_0-H_0
       =-1+y+x^2-x^3y-x^2y^3+x^3y^3.                 (13)

The six displayed monomials are distinct, with coefficients
+/-1, so its L1 norm is6. All three site types are disjoint.
Therefore

    ||P_0||_1=90+90+6=186,
    sum P_0=0,
    mass(f)=mass(g)=mu(P_0)=93.                       (14)

The zero total follows either from (2) or any of its zero
readouts. In particular the positive and negative masses
really are half of186.

Any path in the fiber (12) between its distinct two vertices
must contain the step f-g=P_0 or its negative; there is no
third nonnegative configuration available as an intermediate
state. Consequently every universal connecting palette for
the exact box (1) must include that actual move up to sign.
No different integer generating set, long path, signed
orientation choice or translated-template representation
avoids its mass. Thus

    least possible maximal move mass in (1) >=93>64.  (15)

This is a necessary lower bound only. No upper bound at93
and no complete Markov palette are proved here.

## 6. Inputs, scope separation and genuine author history

There were at most two known objects in the bounded selection.

The accepted old single-long-axis boxed author whole is

    repository awdawmip/enterprise-math
    Source bc863ad9b2383898d727c850d768e075e1f8973c
    research_notes/owner_goal_20261016/
    native_x6_boxed_seven_observer_fiber_connectivity_bff6dc/
    BOXED_SEVEN_OBSERVER_ALL_MASS_CONNECTING_PALETTE_AND_SHARP_MOVE_MASS_WORKING.md
    19788 bytes
    SHA256 80e543b28dac68ab8be779b7163b86b402fb45b7a114218e2ae8b8ab792ede43
    Git blob 0ede6637cf9488256efc322355093a9fb4f51667.

Its actual old box is {0,1,2,3} x {0,1,2}^5. A genuine
nonauthor peer is the16885-byte review at Source
7788ddc3b3dcb35fcf47afb89691d182cc36a90d,
research_notes/owner_goal_20261016/reviews/
native_x6_boxed_connectivity_nonauthor_7cda51/
BOXED_SEVEN_OBSERVER_CONNECTIVITY_COMPLETE_WHOLE_REVIEW_AND_CONTEXT.json,
SHA256 cedfa8972f5736ca518ba2c630b6b9c50e4d04f2cd00f26f2257c8c5a58b24e6,
Git blob 3ad1ffb42e059e07b7878d7cd57477fed70c2489.
BFF personally whole-read/authored the old unit and closed its
own author Source custody and ordinary whole peer semantics/
actual Source/exact one ADD, two Sources/36673 bytes. That history
is reused honestly; no new old Source query is claimed here.

The second known object was BFF's newly reformulated LOCAL
long-axis author argument:

    /workspace/enterprise-math/research_notes/owner_goal_20261017/
    native_x6_long_axis_bff6dc/
    LONG_AXIS_BOX_AUTHOR_REFORMULATED_V2_20261017.md
    20507 bytes
    SHA256 51e9e082bbf66db51b265efe5cd1e463ef81207eefeb2c25b8f6c9dc749a89d2
    Git blob 7d048f7ad5c1d39f3429a02389a397b3e47326b6.

It had a full earlier temporary chat-level 4A review, but NOT
final acceptance of its new durable artifact/Source/context.
It was used only as a selection/interface observation: one
long axis leaves a scalar difference path; two long axes
leave a two-dimensional zero-row/zero-column table.
All required kernel and site arguments for THIS theorem were
independently supplied in Sections2-5. The local long-axis
temporary opinion is not used as an accepted premise.

BFF asked A only for already existing coverage/occupancy
metadata, before sending any new formula, numeric bound,
working text or repair. A replied that her frozen coverage
was only the old19788 single-long-axis box; an exact frozen
two-long-axis palette/sharp/mixedcycle locator was UNKNOWN
in her personal coverage. She did not search, derive or
occupy the new proof. This is NOT a claim that the entire
library lacks the result. A's own different single-box
supplementary-readout intake was kept separate.

The new two-axis cycle/table/site construction and proof above
are BFF's author work; internal construction history is
NONZERO. Root approved one bounded manual trial and supplied
no mathematical formula, repair or vote. No other agent
provided a proof patch. A is not preselected as a zero-
construction reviewer; any future peer needs a truthful
separate scope qualification.

The discriminating target was whether the old mass64 upper
bound survives the genuinely different two-axis geometry.
The kill condition was to stop if only a formal kernel
remained without an actual nonnegative fiber and exact mass.
Equations (12)-(15) meet the stronger negative outcome by
an actual forced move. This does not reopen an old missing-
caller HOLD, change a STOP, or optimize a former constant.

No scientific code, enumeration, numerical sample, new query,
Native execution, formal Task, helper, identity, RA or budget
reset was used. This file is one same-family finite proof
record, not a new generic Tool or principal paper. It has
not received a new Source, final independent whole review
or ordinary final acceptance. Future Source and peer fields
must be bound to real observations, not prefilled from any
old unit or the author's self-reading. The old19788 and
long-axis20507 files remain unchanged.

