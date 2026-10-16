# CM24: a sharp obstruction modulo p^3 to lifting the horizontal source

2026-10-16 UTC. Author EM-DIRECT-88303D, direct TASK_RESEARCH.
Root coordinates only. Exact identity/activity and input pins accompany
this author proof. No scientific program or parameter sample is used.

**Result.** For the fixed scalar operator L_* below, the prescribed
mod-p Legendre source admits the old finite mod-p^2 lift, but admits
NO mod-p^3 horizontal lift even as an unrestricted formal series.
The failure already occurs in its finite 2p-jet. An explicit
m+1-row residual detector has the fixed nonzero value (12), invariant
under every p^2 correction. This is a source-vector obstruction in
the original integral lattice, not a Frobenius-comparison no-go or
a rejection of the old mod-p^2 theorem.

## 1. Exact source, operator and consumed finite lift

Keep each original prime p=6m+1 congruent to13 or19 modulo24,
literal m>=2, n=2m, d=4m=p-1-n. Let O be the given unramified
complete p-adic DVR, K=O[1/p], and v(p)=1. Use the exact source
Legendre polynomial P_n(s), normalized by P_n(1)=1, and put

    L_*=(1-s^2)D_s^2-2sD_s-2/9.                      (1)

Its coefficient -2/9 is fixed in characteristic zero. It is not
replaced by n(n+1), although they agree modulo p.
Here p^3 is a precision level, separate from the old terminal-accepted
Hesse P3 transport Task, which is not reopened.

The reviewed finite-spectral paper,14981B, supplies the actual
integral polynomial representative

    Q_2=(2P_n+P_d)/3,
    Q_2=P_n modulo p, L_*Q_2=0 modulo p^2,
    deg Q_2=d<p, Q_2(1)=1.                           (2)

The whole coefficient congruence and mod-p^2 result in (2) are
CONSUMED, not recomputed here. That paper expressly did not identify
the finite window with an infinite canonical period. Its separate
unit72 target-template rejection remains unchanged. Exact Source
pins, old scopes and tool-reuse resolution are recorded separately.

The source has P_n(0) a p-unit. For example its standard finite
coefficient identity gives

    P_(2m)(0)=(-1)^m binom(2m,m)/4^m.                 (3)

All factorial indices in (3) are below p and2 is a unit. Equivalently,
the finite even Legendre recurrence connects the unit leading
coefficient to its constant term using only unit factors. No target
value, unknown endpoint or response constant is inverted.

We prove that no f in O[[s]] can satisfy BOTH

    f modulo p = P_n(s) coefficientwise,
    L_*f belongs to p^3 O[[s]].                      (4)

The statement equally concerns a class over O/p^3: choose integral
representatives of its finitely many coefficients used below.
All computations are in free coefficient modules over O and its
p-power quotients; O[[s]] is not treated as a DVR.

## 2. An exact finite telescope of coefficient rows

Write f=sum_(k>=0)c_k s^k and, for j=0,...,p-1, set

    B_j=(2j+2)(2j+1),
    A_j=(2j)(2j+1)+2/9=(2/9)(6j+1)(3j+1),
    R_j=[s^(2j)]L_*f=B_j c_(2j+2)-A_j c_(2j).       (5)

Odd coefficients do not enter these rows; no even-parity assumption
on f is imposed. Define finite products, with empty products1,

    D=prod_(j=0)^(p-1) B_j=(2p)!,
    A=prod_(j=0)^(p-1) A_j,
    W_j=(prod_(i<j)B_i)(prod_(i>j)A_i).

Multiplying (5) by W_j and summing cancels all interior coefficient
terms, giving the EXACT identity over O

    D c_(2p)-A c_0=sum_(j=0)^(p-1) W_j R_j.          (6)

For example the contribution of c_(2j) from the j-th negative term
has precisely the same product as its preceding positive term.
This proves the cancellation without dividing by any B_j, some of
which are divisible by p. Only c_0,...,c_(2p) and residual degrees
0,2,...,2p-2 occur. Arbitrarily many higher coefficients cannot
alter the identity.

## 3. Both product valuations and their exact unit residues

In D=(2p)!, exactly p and2p are multiples of p, and neither has
valuation greater than1. Hence v(D)=2. After removing them, the two
blocks of nonzero residues are each F_p^x; therefore

    D/p^2=2 modulo p.                                (7)

Here product(F_p^x)=-1 follows directly by inverse pairing, leaving
only1 and-1. No sampled prime or factor table is involved.

For A, the progression 6j+1 has exactly one p-divisible term in
the indicated range, namely j=m with value p. Indeed reduction is
a permutation of F_p, and 6p-5<p^2 excludes any further p-adic
valuation of a term; the unique divisible term is literally p.
Likewise 3j+1 has its unique such term j=2m, again with value p.
All other factors and2/9 are units. Consequently v(A)=2, and

    A/p^2=(2/9)^p*(-1)*(-1)=2/9 modulo p.             (8)

The residues of each product with its single p removed are -1,
because its remaining linear residues are exactly F_p^x. Every
division by p in (7)-(8) occurs in O AFTER exact divisibility,
before reduction. No division of a zero field element is made.

## 4. Universal 2p-jet condition and the obstruction

If every R_j is in p^3O, (6)-(8), divided by p^2 and reduced, force

    2 c_(2p)-(2/9)c_0=0 modulo p,
    equivalently c_(2p)=c_0/9 modulo p.              (9)

But reduction to the prescribed P_n, whose degree n=2m<2p, gives

    c_(2p)=0 modulo p, c_0=P_n(0) not zero modulo p.

This contradicts (9). Thus (4) is impossible. In fact it suffices
to require the even residual rows in (5) modulo p^3 and the source
reduction through degree2p: there is no such finite 2p-jet.

Together with the consumed actual lift (2), the source-lifting
threshold is sharp at these two consecutive precisions: mod-p^2
solutions exist, while NONE of their possible source-preserving
formal or polynomial extensions can be horizontal modulo p^3.
The degree<p restriction used in the OLD uniqueness theorem is
not imposed on this new negative conclusion.

## 5. A residual-class certificate for every mod-p^2 lift

Suppose f is any integral representative with f modulo p=P_n and
L_*f in p^2O[[s]]. Form r_j=R_j/p^2 modulo p, dividing BEFORE
reduction. From (6), its residual rows obey

    sum_j Wbar_j r_j=-(2/9) P_n(0) modulo p.          (10)

To identify its exact finite support, B_i has p-valuation1 only at
i=3m and i=6m in the full range. A_i has p-valuation1 only at m
and2m. Thus the weights in (6) have valuations

    v(W_j)=2 for 0<=j<m,
             1 for m<=j<2m,
             0 for 2m<=j<=3m,
             1 for 3m<j<=6m.                        (11)

The last B_(6m) never enters an earlier prefix, including at j=6m.
All critical weights Wbar_j,2m<=j<=3m, are nonzero. Define the
explicit field-linear detector

    D_p(r)=sum_(j=2m)^(3m) Wbar_j r_j.
    D_p(r)=-(2/9) P_n(0) !=0.                       (12)

For any correction f -> f+p^2 h, h in O[[s]], the residual r changes
by the corresponding even coefficient rows of Lbar_* hbar. Applying
(6) to h and reducing modulo p shows

    D_p( ([s^(2j)]Lbar_* hbar)_j )=0,                (13)

since both D and A are divisible by p^2 and all noncritical weights
vanish modulo p. Thus (12) is independent of the chosen integral
representative of a mod-p^2 solution and cannot be repaired by any
p^2 correction. At least one critical residual row must survive.

The certificate retains the whole operator and every relevant
source row; it is not a positive-support projection or a numerical
rank computation. Its m+1 explicitly given critical rows and unit
right side are finite for each declared p. Their coefficient
products are prescribed algebraic data, not an executed algorithm
or a claimed constant-cost evaluation.

## 6. Consequence for the full prescribed source near r=0

The fixed carrier's proper quotient is Y'=S' A(S)Y, S=4r^3-3r.
The consumed exact scalar reduction is (1), with first coordinate
f=Y_1; the second is

    Y_2=6(1-s^2)f'+(1-2s)f.

Near r=0, S has unit linear coefficient -3. It therefore defines
an invertible formal coordinate substitution over O; its inverse
is obtained recursively with the same unit divisor. The scalar
elimination uses only6,1-s^2 and S', all units in these ordinary
formal coordinates for the original primes. It is valid modulo p^3,
without passing to a field or dividing by a p-nonunit.

If an integral full horizontal source lift modulo p^3 in the original
coordinates reduced to the prescribed proper source P_n(S), its
first proper component, expressed in s, would satisfy (4). This is
impossible. In particular permitting an arbitrary fourth primitive,
the original full H_b baseline, the z coordinate or arbitrarily
high degree does not repair this proper-quotient obstruction.
No baseline or quarter contribution is deleted from the target.

This conclusion is about source VECTORS in the original lattice
and with this literal coefficientwise reduction. It is not about
horizontal Frobenius-comparison MORPHISMS or the separate LC-D
matrix-lifting problem. Inverting p, changing the lattice/reduction,
keeping an explicit inhomogeneous lift defect, or changing the
characteristic-zero proper connection changes the hypotheses.

For example P_n is exactly horizontal for L_n with coefficient
+n(n+1); its difference from -2/9 is p(p+1)/9. The theorem does not
exclude that different lift, or an analytic/nonintegral period.
Nor does it exclude a geometric de Rham module or actual proper/full
Frobenius, and it supplies no origin k, boundary eta, sign mu,
source functional or Y/Z/kappa evaluation.

All old accepted and frozen units, including the old finite mod-p^2
section and its separate target-template rejection, remain intact.
P000/Heartbeat X6 remains the project basis; these are external
arithmetic coefficient observers, with no native axes, physical
time or signed-channel loss. Zero scientific programs, samples,
new formal Tasks or Native votes. A new distinct nonauthor review
is required; parent Goal stays OPEN.

Researcher-ID: EM-DIRECT-88303D / TASK_RESEARCH

