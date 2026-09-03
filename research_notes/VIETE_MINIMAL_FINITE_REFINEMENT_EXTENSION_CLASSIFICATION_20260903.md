# Viète minimal finite refinement extension: necessity and sufficiency of connected binary cover + exact distance halving + inversion-safe tie retention

Status: `FREE_RESEARCH / EXACT NECESSITY-SUFFICIENCY CLASSIFICATION IN DECLARED FINITE-CYCLE ARCHITECTURE / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parents:
- `research_notes/VIETE_FINITE_CYCLIC_SHORTEST_ROOT_REFINEMENT_20260903.md`
- `research_notes/VIETE_BINARY_CYCLE_COVERS_2ADIC_VS_ANALYTIC_COMPLETION_20260903.md`
- `research_notes/VIETE_GATE_DISTANCE_HALVING_AND_GATE_PI_READOUT_20260903.md`

## 1. Classification question

Current P000 does not uniquely select a native finite 6D rotation law. #1158 therefore should not hide the remaining gap behind the phrase “derive the Cell refinement law.”

Instead ask a narrower mathematical question:

> inside the explicit finite architecture where an orientation quotient is a cycle and one precision step is a binary refinement of that cycle, what is the weakest finite structure that forces the Viète half-root relation uniquely?

This note proves an exact answer at that declared architecture strength.

## 2. Architecture class

Let the coarse orientation state be a cycle graph

\[
\Gamma_N,
\qquad N\ge3.
\]

A one-step refinement consists of:

- a finite refined graph `Gamma'`;
- a two-to-one local graph covering
  \[
  \pi:\Gamma'\to\Gamma_N;
  \]
- a refinement relation `R(x)` assigning one or more fine lifts in `pi^{-1}(x)`.

Require the ordinary inversion symmetry of the cycle to act on both levels:

\[
S_N(k)=-k.
\]

No real angle, trig function, continuous circle, or target `pi` is part of this architecture.

## 3. Clause A — connected binary cover

`A1 BINARY`: every coarse state has exactly two refined lifts.

`A2 CONNECTED`: the refined orientation graph is connected.

A finite connected two-fold cover of an `N`-cycle is uniquely a `2N`-cycle up to cover isomorphism:

\[
\boxed{
A1+A2\Longrightarrow \Gamma'\cong\Gamma_{2N}.
}
\]

Thus the state-refinement carrier is forced to be

\[
C_{2N}\to C_N.
\]

### Why both clauses matter

If `CONNECTED` is dropped, another valid two-fold local cover is

\[
\Gamma_N\sqcup\Gamma_N\to\Gamma_N,
\]

which adds a detached copy rather than finer cyclic resolution and does not force a new half-cycle state.

If `BINARY` is dropped, connected `k`-fold covers

\[
\Gamma_{kN}\to\Gamma_N
\]

exist for every `k>=2`, so dyadic refinement is not selected.

Therefore, within ordinary cycle covers, connectedness and degree two are both necessary to force the `N->2N` precision carrier.

## 4. Clause B — exact normalized-distance halving

On `C_N`, define normalized finite rotation distance

\[
\theta_N(x)=\frac{\delta_N(x,e)}{N}.
\]

Require a retained refined lift `y in R(x)` to satisfy

\[
\boxed{
\theta_{2N}(y)=\frac12\theta_N(x).
}
\]

This clause contains the operational meaning of “half-refinement” but no angle variable.

The gate-distance theorem proves that among the two lifts of `x`, exactly the Cayley-shortest lift(s) satisfy this equality.

Hence:

\[
\boxed{
A+B\Longrightarrow R(x)\subseteq\operatorname*{argmin}_{\pi(y)=x}\delta_{2N}(y,e).
}
\]

Away from the half-turn this set has one element, so the retained root is unique.

### Why Clause B is necessary for the Viète half-root, not merely convenient

Without the distance-halving requirement, both antipodal lifts are equally valid as group-theoretic preimages of the coarse state. For a non-half-turn state one may consistently choose the farther lift instead of the identity-near one.

That farther lift does not halve normalized distance; its distance is

\[
\frac12-\frac12\theta_N(x).
\]

Thus the binary cover alone does not distinguish half-refinement from its antipodal complement.

Any rule intended to mean “halve the unresolved rotation relative to identity” needs a root-separating locality condition; exact normalized-distance halving is the minimal discrete form used here.

## 5. Clause C — inversion covariance and complete tie retention

Require

\[
R(S_Nx)=S_{2N}R(x)
\]

as a relation.

At a non-half-turn state, the unique shortest lift automatically satisfies inversion covariance.

At the half-turn `h`, inversion fixes the coarse state:

\[
S_N(h)=h,
\]

but swaps the two equally short fine lifts.

Therefore no nonempty **single-valued** inversion-equivariant refinement exists at `h`.

An inversion-equivariant relation must retain the entire pair:

\[
\boxed{
R(h)=\{q_+,q_-\}.
}
\]

Thus all-tie retention is not optional if both inversion symmetry and nonempty refinement are required.

This is exactly the two-sheeted Viète seed.

## 6. Necessity-sufficiency theorem

Within the architecture of Section 2, impose:

1. connected two-sheeted cycle refinement;
2. exact halving of normalized identity distance for retained lifts;
3. inversion covariance and nonempty refinement.

Then, up to cycle-cover isomorphism, there is exactly one refinement relation:

\[
\boxed{
R_N(x)=
\operatorname*{argmin}_{\pi_N(y)=x}\delta_{2N}(y,e).
}
\]

It has:

- one retained lift for every non-half-turn state;
- exactly two retained lifts at the half-turn;
- exact square-root/cover compatibility;
- exact `theta -> theta/2` finite precision;
- inversion-paired branch propagation.

Conversely this shortest-lift relation satisfies all three clauses.

Therefore:

\[
\boxed{
\text{CONNECTED BINARY COVER}
+
\text{EXACT DISTANCE HALVING}
+
\text{INVERSION-SAFE TIE RETENTION}
}
\]

is a necessary-and-sufficient finite specification for the #1158 Viète refinement **inside this declared cycle-cover architecture**.

## 7. Nested radicals are then forced at the scalar character layer

Once the finite state relation is fixed, a unit character trace satisfies

\[
c_{m+1}^2=\frac{1+c_m}{2}.
\]

The identity-near/shortest lift gives the positive longitudinal branch, so

\[
\boxed{
c_{m+1}=\sqrt{\frac{1+c_m}{2}}.}
\]

At the half-turn the two oriented roots differ only by turn-sense inversion and have the same scalar longitudinal coordinate.

Hence the scalar nested-radical chain is uniquely forced by the three finite clauses; no additional chirality selector is needed.

## 8. Exact failure modes when one clause is removed

### Remove binary degree

Possible refinement carriers include `C_(kN)` for arbitrary `k`; no dyadic radical hierarchy is selected.

### Remove connectedness

The two-sheet cover may be `C_N disjoint_union C_N`; no new cyclic phase resolution or half-turn emergence is forced.

### Remove distance halving

The far antipodal lift may be selected; the refinement no longer means a half-step toward identity and the normalized-equal-resultant branch is not forced.

### Remove inversion covariance / tie retention

At the half-turn a deterministic selector may arbitrarily choose one quarter-root, introducing an untyped absolute chirality break. The scalar result may survive, but the oriented construction ceases to be symmetry-canonical.

These countermodels establish that the three clauses do real discriminating work.

## 9. Relation to current native rotation state

Current Cell-rotation semantics separately requires a local orientation/sweep variable `epsilon`. Its two-state reversal torsor can be identified with the finite turn-sense torsor up to a global `C2` gauge.

However, the three clauses above are **not all currently frozen G0 consequences**:

- current three-ray cyclic structure supports the coarse `C3` quotient;
- current P000 does not itself require physical Cell rotation to refine by connected binary covers;
- current P000 does not itself impose exact normalized cycle-distance halving as the refinement semantics;
- current rotation correction requires orientation reversal consistency but leaves the exact Cell transition law open.

Therefore this note identifies the minimal missing extension **inside a precise model class** rather than silently promoting it to native Foundation.

## 10. Native-extension boundary for #1158

The remaining G0 question can now be asked sharply:

> Does actual Enterprise Cell rotation satisfy the two nontrivial finite extension principles
> `CONNECTED_BINARY_ORIENTATION_REFINEMENT`
> and
> `NORMALIZED_ROTATION_DISTANCE_HALVING`,
> with the already-required orientation reversal enforcing complete half-turn tie retention?

If yes, the finite Viète refinement follows uniquely.

If no, the scalar G1/G2 Viète reconstruction remains valid but is not the native Cell refinement law.

This is substantially narrower than “derive the whole half-angle formula from Cell geometry.”
