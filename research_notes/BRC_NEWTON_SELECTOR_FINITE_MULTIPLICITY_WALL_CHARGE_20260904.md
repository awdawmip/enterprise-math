# BRC finite-multiplicity selector wall-charge law

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: arbitrary-degree Sturm root-rank state, selector event theorem, simple wall crossing, ordinary fold wall law

## 1. Problem

The current selector-event line has two local laws:

- a transverse simple root crossing an observer endpoint gives an oriented jump of magnitude one;
- an ordinary interior fold creates or annihilates a real pair and gives an oriented jump of magnitude two.

These are the first two members of one parity-controlled finite-multiplicity law. The useful object is not a nearby floating root approximation, but an exact integer **observer charge** attached to an isolated algebraic event.

Local polynomial singularities, Weierstrass preparation and real-root wall crossing are classical prior art. The BRC contribution here is the exact observer-typed charge ledger and its composition with the existing root-rank / interval-count carriers.

## 2. Ordinary finite-multiplicity event

Let

\[
P(t,x)\in\mathbb Q[t,x]
\]

and suppose an isolated event occurs at a rational point

\[
(t_0,x_0)\in\mathbb Q^2.
\]

Assume that the root of the event fiber has exact multiplicity \(m\ge1\):

\[
P=P_x=\cdots=P_{x^{m-1}}=0,
\qquad
P_{x^m}\ne0
\]

at \((t_0,x_0)\), and that the parameter direction is transverse:

\[
P_t(t_0,x_0)\ne0.
\]

Also require the event to be isolated from other root events in a sufficiently small rectangle. Define the exact rational orientation coefficient

\[
\boxed{
\kappa
=-\frac{m!\,P_t(t_0,x_0)}{P_{x^m}(t_0,x_0)}.
}
\]

The weighted local blow-up has leading equation

\[
\boxed{
(x-x_0)^m=\kappa(t-t_0).
}
\]

More precisely, after the scaling

\[
x-x_0=|t-t_0|^{1/m}u,
\]

the local Weierstrass polynomial converges coefficientwise to

\[
u^m-\kappa\operatorname{sgn}(t-t_0).
\]

Consequently:

- if \(m\) is odd, exactly one local real root exists on both sides and crosses \(x_0\);
- if \(m\) is even, two local real roots exist on the side \(\kappa(t-t_0)>0\), and none exist on the opposite side.

This parity split is the entire source of the observer-charge formulas below.

## 3. Root-rank wall charge

For a fixed rational probe \(r\), let

\[
\nu_t(r)
=
\#\{\alpha\in\mathbb R:P(t,\alpha)=0,\ \alpha<r\},
\]

counting distinct real roots. Write

\[
\Delta\nu(r)
=
\nu_{t_0+}(r)-\nu_{t_0-}(r).
\]

Then the isolated event contributes

\[
\boxed{
\Delta\nu(r)=
\begin{cases}
2\operatorname{sgn}(\kappa),
& m\text{ even and }x_0<r,\\[2mm]
(-1)^m\operatorname{sgn}(\kappa),
& x_0=r,\\[2mm]
0,&\text{otherwise}.
\end{cases}
}
\]

Interpretation:

- an odd root strictly to the left or right of the probe remains on that same side, hence contributes no rank jump;
- an even event strictly below the probe creates or annihilates two real roots;
- at the probe itself, an odd root crosses through the endpoint, whereas an even birth/death contributes exactly one of the symmetric pair below the endpoint.

The simple-crossing law is recovered at \(m=1\):

\[
\Delta\nu(r)
=-\operatorname{sgn}(\kappa)
=
\operatorname{sgn}\!\left(\frac{P_t}{P_x}\right).
\]

The ordinary-fold law is recovered at \(m=2\):

\[
\Delta\nu(r)=2\operatorname{sgn}(\kappa)
\quad(x_0<r).
\]

## 4. Open-interval wall charge

For fixed rational endpoints \(u<v\), define

\[
N_t(u,v)
=
\#\{\alpha\in\mathbb R:P(t,\alpha)=0,\ u<\alpha<v\}.
\]

The event charge is

\[
\boxed{
\Delta N(u,v)
=
\operatorname{sgn}(\kappa)
\begin{cases}
2,&m\text{ even and }u<x_0<v,\\
1,&x_0=u,\\
(-1)^m,&x_0=v,\\
0,&\text{otherwise}.
\end{cases}
}
\]

This simultaneously resolves all endpoint cases omitted by the ordinary-fold theorem:

- at the left endpoint, every ordinary finite-multiplicity event has charge \(+\operatorname{sgn}(\kappa)\);
- at the right endpoint, the charge is \((-1)^m\operatorname{sgn}(\kappa)\);
- an odd event in the interior has zero charge because its one real root remains inside;
- an even event in the interior has charge \(2\operatorname{sgn}(\kappa)\).

For smallest-positive selection, take \((u,v)=(0,r)\). A zero root is an endpoint event, not an interior positive root.

## 5. Wall-charge ledger and additivity

Suppose a compact parameter interval contains finitely many ordinary events, each isolated in parameter and space, and no root lies on an observer endpoint away from those listed events. Then root-count additivity gives

\[
\boxed{
N_{t_+}(u,v)-N_{t_-}(u,v)
=
\sum_j q_j(u,v),
}
\]

where \(q_j\) is the local charge above.

The same formula holds for the root-rank observer \(\nu(r)\). If several events occur at the same parameter but at distinct spatial points, their charges still add after choosing disjoint spatial neighborhoods.

Thus one-parameter chamber labels need not always be recomputed independently: after one initial exact Sturm label, the complete label sequence can be transported by an ordered integer wall-charge ledger whenever every event has been locally classified.

## 6. Mixed simple/fold witness

Consider

\[
P(t,x)
=(x-t)\bigl((x-1)^2-(t-3)\bigr)
\]

and the positive interval \((0,2)\).

There are three separated events as \(t\) increases:

1. \(t=0,x=0,m=1,\kappa=1\): the moving root enters through the left endpoint, charge \(+1\);
2. \(t=2,x=2,m=1,\kappa=1\): it exits through the right endpoint, charge \(-1\);
3. \(t=3,x=1,m=2,\kappa=1\): a pair is born inside the interval, charge \(+2\).

Hence

\[
\boxed{
\Delta N(0,2)=1-1+2=2.
}
\]

At the rank probe \(r=2\), the corresponding charges are

\[
0,-1,+2,
\]

so

\[
\boxed{\Delta\nu(2)=1.}
\]

Both totals agree with direct exact Sturm counts at the two ends of the parameter interval.

## 7. Simultaneous separated-event witness

Let

\[
P(t,x)=(x^2-t)((x-1)^2-t).
\]

At \(t=0\) there are two ordinary folds, spatially separated at \(x=0\) and \(x=1\), both with \(m=2,\kappa=1\).

For \((0,2)\):

- the endpoint fold at zero contributes \(+1\);
- the interior fold at one contributes \(+2\).

Therefore

\[
\boxed{\Delta N(0,2)=3.}
\]

For the rank probe \(r=2\), both folds lie below the probe and each contributes \(+2\), so

\[
\boxed{\Delta\nu(2)=4.}
\]

This demonstrates that simultaneous parameter events are still additive when their spatial germs are disjoint.

## 8. Exact validation

The dedicated checker uses only rational polynomial arithmetic plus the existing exact Sturm root-count engine. It verifies:

- the canonical family \((x-x_0)^m-\kappa t\) for \(m=1,\ldots,8\), four nonzero rational orientations and five centers;
- mixed ordinary germs
  \[
  (x-x_0)^m-\kappa t+t\sum_{j=1}^{m-1}c_j(x-x_0)^j
  \]
  across 420 exact samples;
- rank probes left of, at and right of the event;
- interval observers with the event in the interior, at either endpoint and outside;
- the mixed simple/fold additive ledger;
- simultaneous spatially separated folds;
- refusal when \(P_t=0\), when the requested multiplicity is incorrect, or when observer geometry is invalid.

The mixed terms test that the charge depends on the ordinary event germ and not merely on the exact monomial normal form.

## 9. Hard boundaries

- `ORDINARY_FINITE_MULTIPLICITY_EVENT` requires exact multiplicity, nonzero \(P_t\), and event isolation.
- `P_t=0` is a tangential/higher-codimension event and has no charge from this first-order orientation law.
- `P_{x^m}=0` means the supplied multiplicity is wrong; the theorem must refuse rather than guess.
- coincident interacting singular germs are not covered by spatial additivity.
- the observer counts distinct real roots, not algebraic multiplicity.
- a wall charge determines the change of a declared root-count observer, not the full local root geometry or root values.
- this is not a generic singularity classifier, complete Puiseux solver, multi-parameter CAD engine, signed branch-interference theory or infinite-state theorem.

## 10. Next frontier

The natural continuation is to combine:

1. the resultant/discriminant event generator;
2. exact event-root isolation;
3. local multiplicity and derivative classification;
4. the present integer charge law;

into a **charge-propagating one-parameter selector compiler**. Such a compiler would need one initial Sturm label and then transport all subsequent chamber labels by certified local charges, while falling back to direct relabeling only at unclassified or interacting events.
