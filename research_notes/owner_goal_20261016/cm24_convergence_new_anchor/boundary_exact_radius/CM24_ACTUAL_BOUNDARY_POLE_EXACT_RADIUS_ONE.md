# CM24: an actual boundary pole forces exact radius one

Author: EM-DIRECT-88303D. Activity: RA-1E650208FBE6654C7D59AB55.
2026-10-16 UTC. New bounded author paper; independent review pending.
This consumes the previous open-disc theorem and does not reopen its proof.

For each fixed allowed prime and every fixed permitted F0, the normalized
matrices H, U=H^-1, F and F^-1 have matrix power-series radius exactly one
in the original coordinate t=r-1. None belongs to M4(K<t>), hence none to
M4(K<t>^dagger), for the whole unpunctured closed unit disc.
Their centered matrix series diverge at every point with |t|=1.
These assertions concern the entire matrix, not every individual entry.

The new certificate is a NONZERO characteristic-zero residue at t=-1/2
and residue incompatibility. Excluded-divisor dagger rings, geometry, LC
and the source functional remain outside scope.

## 1. Fixed source and the genuine remaining question

Use the exact normalized gauge and constant family of
CM24_LOG_RESIDUE_GRADES_REVIEWED_20261015.json at Source
3981c60496c24a3c1567677726c136966522d8bf. Its 13743B author proof has
SHA256 e17688c59f6d59f4611cbcd0bb518483fa381b2526d3ee82bec3dd61eb75cf5c.
The V2 reviewed carrier at that same Source fixes the integral polynomial

    H_b(x)=g(1+x^N)+(4sigma0/5)x+(sigma0/5)x^(N-1),
    N=(p-1)/2, sigma0=1-2g,

with g the saved integral lift. No new normalization is chosen.
The consumed open-disc proof is the exact 9897B paper, SHA256
cfa8974bd1b9c077cdf7210428276b6bb2af707d1de853b91d8180a9387ba26b, at
[Source d35fb1a](https://github.com/awdawmip/enterprise-math/blob/d35fb1abc3d459a9363144aabf9ee41b51fcb481/research_notes/owner_goal_20261016/cm24_convergence_new_anchor/CM24_ORIGINAL_OPEN_UNIT_DISC_LOG_COEFFICIENT_BOUND.md).
It has a genuine nonauthor PAPER_PASS, not a Native scientific acceptance.

That theorem proves all-n logarithmic bounds for H,U and original |t|<1
convergence, and the same convergence for F=H F0 sigma(U)(t^p).
It explicitly leaves boundary convergence and dagger membership open.
The older analytic theorem's shrunk-disc dagger result, factorial majorant
and ad_R^4 argument are consumed. Hesse-P3 stays terminal ACCEPTED.
The prior list of possible boundary poles did not certify the obstruction
below or an exact maximal radius.

Let O,K,v be the same unramified complete DVR, fraction field and v(p)=1,
with p congruent to 13 or 19 modulo 24. Work in the original 2+1+1 basis:

    s=S(r)=4r^3-3r, t=r-1,
    A(s)=[[-(2s-1),-1],[-(4s-5),2s-1]]/[6(s^2-1)],
    A_t=S'(r)A(S(r)),
    N(t)=[[A_t,0,0],[0,0,0],[w(1,0),-w H_b(r^2),0]],
    w=(8r^p-4r)/(1-r^2).

Here N(t) is the matrix; the H_b exponent is N=(p-1)/2.
Write R0=Res_(t=0) N(t)dt. The source equations are

    H'=N H-H R0/t, H(0)=I,
    F'=N F-F N_theta,
    N_theta=p t^(p-1) sigma(N)(t^p), theta(t)=t^p.       (1)

F0 is the old family in the corresponding original basis: mu=+/-1,
c,xi,eta in K, R0 F0=p F0 R0, det F0=p^-4; filtration is unchanged.
All entries of N are rational functions with possible poles only at

    P={0,-2,-1/2,-3/2}                               (2)

in the t-line; the fixed H_b and its sigma-image introduce no further
denominators. The selected coefficient Witt map fixes rational constants.
Traces of N,R0,N_theta vanish. The formal identities already give

    det H=det U=1, det F=p^-4, det(F^-1)=p^4.           (3)

In particular each determinant is a nonzero constant.

Heartbeat native X6 remains the project basis. This external arithmetic/module
proof identifies no native axis or physical time with t. All proper, z, V,
baseline and extension channels are retained; there is no observer quotient.

## 2. A real pole at the specified boundary point

Take a=-1/2, hence r=1/2 and s=-1. Since p>=13, |a|=1.
At s=-1 the actual proper residue is

    Q_-=Res_(s=-1) A(s)ds
        =(-1/12)[[3,-1],[9,-3]]
        =[[-1/4,1/12],[-3/4,1/4]].                   (4)

This follows by evaluating the numerator at -1 and using
6(s^2-1)=-12(s+1)+6(s+1)^2. It is nonzero.

The exact identity

    S(r)+1=(r+1)(2r-1)^2=4(r+1)(r-1/2)^2

shows ramification order TWO at r=1/2. Thus
d(S+1)/(S+1)=2d(r-1/2)/(r-1/2)+dr/(r+1).
The pullback proper residue is therefore

    Q_a=2Q_-=[[-1/2,1/6],[-3/2,1/2]] != 0.           (5)

It has rank one and square zero. The zero of S' does not cancel the pole:
it reduces the order-two denominator to the simple logarithmic pole (5).

The whole lower row is regular at a. Indeed 1-r^2=3/4 there, and H_b is
a polynomial. Consequently the FULL connection residue is

    R_a=diag(Q_a,0,0) != 0.                          (6)

The constant invertible T gives a nonzero hatted conjugate too, and transfers
all analytic conclusions between frames. This certifies an actual full-carrier
pole, rather than only a possible denominator.

The target R0/t in the H equation is regular at a. The other comparison
target N_theta is also regular there: a^p=-2^-p is nonzero and is none of the
three nonzero rational points in (2), since p>=13 and 0<2^-p<1/2 in Q.
This rational inequality is only an exact non-equality test; no real norm is
substituted for the p-adic norm. The denominator values may have positive
p-adic valuation, but they are nonzero in characteristic zero. Multiplication
by p t^(p-1) introduces no pole at a. Hence

    Res_a(R0/t)dt=0,   Res_a N_theta dt=0.             (7)

The fact that theta fixes the reduced residue class is not equality of these
characteristic-zero pole locations.

## 3. The analytic residue condition, with no geometric import

Here K<t> is the Tate algebra of series sum m_n t^n with v(m_n)->+infinity.
Its members and derivatives are analytic near each point of the closed unit
disc; differentiation preserves the algebra because |n|<=1.
K<t>^dagger means series converging on some closed disc of radius rho>1,
so K<t>^dagger is contained in K<t>. These rings are not treated as DVRs.

Suppose a matrix M is analytic near a, invertible at a, and satisfies

    M'=N1 M-M N2,

where N1,N2 have at most simple poles at a. Taking the residue of this identity
gives the necessary condition

    (Res_a N1)M(a)=M(a)(Res_a N2).                    (8)

The derivative has zero residue. Equivalently the two residues are conjugate
by M(a). This is direct matrix algebra, not an imported log-crystalline or
semistable comparison theorem.

For the present rational matrices the same conclusion is available without
assuming an analytic continuation of a germ from 0: clear all denominators
in the formal identity. If M is in the Tate algebra, this is an identity of
Tate series. Evaluation at a after removing the one simple zero in the
source denominator yields exactly (8). Thus formal equality at 0 suffices
under the stated Tate hypothesis.

Assume first H has all entries in K<t>. By det H=1, its adjugate gives an
inverse in the same algebra, and H(a) is invertible. Equations (6)-(8), with
N1=N and N2=R0/t, would imply R_a H(a)=0, hence R_a=0, a contradiction.
Therefore

    H not in M4(K<t>).                              (9)

Similarly, if F had all entries in K<t>, (3) would make F(a) invertible.
Using N2=N_theta and (7)-(8) gives R_a F(a)=0, the same contradiction.
This argument applies to EVERY fixed permitted F0, because its nonzero
constant determinant is the only F0 information needed. No special choice
of c,xi,eta or mu can remove (6). Thus

    F not in M4(K<t>) for every permitted F0.        (10)

If U were entrywise Tate, det U=1 would put its adjugate H in Tate,
contradicting (9). If F^-1 were entrywise Tate, its nonzero constant
determinant would similarly put F in Tate. Both inverses are therefore
non-Tate as well. Since dagger is contained in Tate, all four matrices
also fail whole-disc dagger membership. Multiplication by any fixed
nonzero scalar in K cannot change this analytic nonmembership.
The old rescaled-disc dagger theorem is unaffected.

## 4. Exact radius and every unit-norm point

The consumed theorem gives convergence of H,U,F on every |t|<1.
The identity F^-1=sigma(H)(t^p) F0^-1 U(t) gives it for F^-1 as well.
Therefore their matrix radii are at least one.

If any of these matrices had matrix radius greater than one, all its entries
would converge on a closed disc of some radius rho>1 and would belong to
K<t>, contradicting section 3. Each matrix radius is consequently exactly one.
Here matrix radius is the minimum of the finitely many entry radii; this
does not assert that every entry has radius one.

More strongly, for a matrix series M(t)=sum M_n t^n, convergence at a point
xi with |xi|=1 requires M_n xi^n->0. But
v(M_n xi^n)=v(M_n), with minimum-entry valuation. If it converged at even one
such point in any complete isometric valued extension, v(M_n) would tend
to +infinity and every entry would lie in K<t>, again a contradiction.
Thus none of these centered MATRIX series converges at any unit-norm point.
Some individual entries, such as constant diagonal channels, may converge;
no stronger entrywise divergence is asserted.

This does not rule out a function represented by other local expressions
on a domain with excluded poles, or a good-locus dagger comparison after its
correct divisors and lift have been specified. Analytic continuation and
centered-series boundary convergence are different claims. The result supplies
an exact necessary divisor/holomorphic-gauge test, not actual geometric
Frobenius, LC-D, gluing, source constants, Y/Z/kappa or parent completion.

Reuse is COMPOSE_APPLIED to the exact source, open-disc theorem, determinants
and residue compatibility; returned catalog tools do not supply this boundary
certificate. No new tool family, novelty claim, scientific program or prime
sample is used. Root supplied control only. A separate genuine nonauthor
review of this new argument is pending; the old PAPER_PASS does not cover it.

Researcher-ID: EM-DIRECT-88303D / TASK_RESEARCH

