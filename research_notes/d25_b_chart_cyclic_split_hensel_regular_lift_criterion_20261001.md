# D25 portable research: observer-regular Hensel lift criterion after a mod-p cyclic cancellation

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit follows the exact p=811 cyclic-gauge cancellation checkpoint on the same portable upper-B-chart lane. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## 1. Setup

Let

L(F)(x) := q(x)F(x+1)-F(x),

with

q(x)=4 (x+1/3)(x+5/6)/((x+1/4)(x+3/4)).

For every prime p>3, define

Q_0(x)=1,
Q_j(x)=prod_{i=0}^{j-1} q(x+i).

In F_p(x),

Q_p(x)=4,

so L is invertible on F_p(x). Explicitly, for any G in F_p(x),

L^{-1}(G)(x)
=
(1/3) sum_{j=0}^{p-1} G(x+j) Q_j(x).          (1)

Indeed the numerator sum S_G satisfies L(S_G)=3G. The homogeneous kernel is zero because one full p-cycle would imply H=4H.

For the Omega/tau cocycle, G=K gives the unique mod-p cyclic splitting gauge R_0.

## 2. Why a regular mod-p split does not automatically give a p^2 split

Suppose the arithmetic observer is x=m=(p-1)/6 and the reduced gauge R_0 is regular there. This occurs at p=811 by the preceding checkpoint.

Choose any rational lift

Rtilde_0 in Z_(p)(x)

such that

Rtilde_0 mod p = R_0,

and the denominator of Rtilde_0 is a p-adic unit at x=m. Such a lift exists because R_0 itself is regular at the observer: write R_0=A/B in reduced F_p(x) form with B(m) != 0 and lift A,B coefficientwise.

Since L(R_0)=K mod p, the defect

D_{Rtilde_0}(x)
:=
[L(Rtilde_0)(x)-K(x)]/p mod p                 (2)

is a well-defined element of F_p(x).

A candidate observer-regular lift through p^2 has the form

Rtilde_0 + p T.

Substitution gives

L(Rtilde_0+pT)-K
=
p [ D_{Rtilde_0}+L(T) ]
mod p^2.

Therefore a lift exists exactly when

L(T)=-D_{Rtilde_0}.                            (3)

Because L is invertible over F_p(x), the correction is unique:

T
=
- L^{-1}(D_{Rtilde_0})
=
-(1/3) sum_{j=0}^{p-1}
D_{Rtilde_0}(x+j)Q_j(x).                       (4)

## 3. Observer-regular lift criterion

Equation (4) gives the exact next obstruction:

boxed:
an observer-regular p^2 splitting exists
iff
T is regular at x=m.                           (5)

Equivalently, after reducing T to a rational function, its principal part at x=m must vanish.

This criterion is independent of the chosen observer-regular lift Rtilde_0.

Proof: if another lift is

Rtilde_0' = Rtilde_0 + p H

with H regular at x=m, then

D_{Rtilde_0'} = D_{Rtilde_0}+L(H),

and hence, by uniqueness of L^{-1},

T' = T-H.

Thus T is regular at the observer iff T' is regular there. The obstruction class is therefore well-defined modulo observer-regular gauge changes.

## 4. BRC interpretation

The preceding p=811 result proves only that the first cyclic pole coordinate H_p vanishes.

The present result shows what must be retained next:

- mod-p observer obstruction: principal part of R_0 at x=m;
- if that vanishes, mod-p^2 observer obstruction: principal part of the unique correction T in (4).

Therefore safe quotienting is precision-typed. A mod-p regular split is not a license to delete Omega from all future observers; the next divided digit must pass criterion (5).

This is exactly the residual-faithful rule: when a visible defect cancels, restore the next operation-sensitive residual rather than declaring the state globally redundant.

Reuse disposition: COMPOSE_APPLIED using the existing finite-field cyclic inverse, p-adic precision typing, and observer-regular BRC lease.

## 5. Current status and next exact unit

For p=811 the mod-p obstruction is known to vanish exactly. This note does not yet evaluate the correction T in (4), so no p^2 splitting is claimed.

The next smallest executable unit is now completely finite:

1. construct the reduced regular rational R_0 in F_811(x);
2. choose any coefficientwise lift with denominator nonzero at x=135;
3. compute D from (2);
4. apply the cyclic inverse (4);
5. inspect the principal part of T at x=135.

A nonzero principal part blocks an observer-regular p^2 lift; zero advances the Hensel test by one digit.
