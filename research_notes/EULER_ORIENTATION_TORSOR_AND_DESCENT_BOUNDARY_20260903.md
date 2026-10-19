# Euler orientation torsor, chirality gauge, and the exact descent boundary

Status: `FREE_RESEARCH / FINITE SYMMETRY THEOREM / NATIVE DESCENT OPEN`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Why one must not call a single quarter-turn canonical

The pivot Cell, its six neighboring Cells, and the six intervening gate events give
an alternating 12-cycle. As an unoriented incidence object, this cycle admits a
reflection

\[
\rho(k)=-k\pmod{12}.
\]

If `Q(k)=k+1` is one oriented successor, then

\[
\boxed{
\rho Q\rho=Q^{-1}.
}
\]

Therefore incidence alone does not distinguish clockwise from counterclockwise.
The two possible oriented successors are exchanged by an automorphism of the bare
carrier.

The current Enterprise foundation names three positive rays successively, so a
chosen chart may provide an orientation convention. The theorem here is narrower:
without such an oriented frame, the Cell/gate incidence object itself cannot select
a principal successor.

## 2. Quarter-turn roots form a two-element torsor

Let `N` be divisible by four and write the half-turn in the additive cyclic group
`C_N` as

\[
H=\frac N2.
\]

The quarter-turn root set is

\[
\mathcal I_N
=
\{q\in C_N:2q=H\}.
\]

Solving the congruence gives exactly

\[
\boxed{
\mathcal I_N
=
\left\{
\frac N4,\frac{3N}4
\right\}.
}
\]

Addition by the half-turn acts freely and transitively:

\[
q\longmapsto q+H.
\]

Hence `I_N` is a `C2` torsor. It has a canonical unordered pair but no canonical
element.

For `N=12`,

\[
\mathcal I_{12}=\{3,9\}.
\]

Reflection exchanges the two roots:

\[
\rho(3)=9,
\qquad
\rho(9)=3.
\]

Under the standard complex character they become

\[
\{i,-i\}.
\]

Thus:

\[
\boxed{
\{i,-i\}\text{ is canonical at the unoriented level; choosing }i\text{ is an orientation trivialization.}
}
\]

The polynomial relation `X^2+1=0` is orientation-independent; a named root is not.

## 3. Complex conjugation is orientation reversal

Let `chi_Q` be the character associated with the oriented successor `Q`. Replacing
`Q` by `Q^-1` sends

\[
\chi_Q(k)\longmapsto\chi_Q(k)^{-1}.
\]

In the standard complex representation this is complex conjugation.

For the dyadic root tower,

\[
U_m\longmapsto U_m^{-1},
\qquad
J=U_1\longmapsto J^{-1}=-J.
\]

The reversal-even half-trace is fixed:

\[
\frac{U_m+U_m^{-1}}2
\longmapsto
\frac{U_m^{-1}+U_m}2.
\]

The normalized reversal-odd coordinate is also fixed, because both its numerator
and its oriented normalizer change sign:

\[
\frac{U_m-U_m^{-1}}{2J}
\longmapsto
\frac{U_m^{-1}-U_m}{-2J}.
\]

Therefore

\[
\boxed{
c_m,\ s_m,\ \Pi_m^{\rm rot},\ \Lambda_m
\text{ are chirality-gauge invariant}.}
\]

The oriented eigenvalue `2J Pi_m` conjugates, but its magnitude is unchanged.

This is an important descent result:

\[
\boxed{
\text{Euler's oriented character needs a frame, but scalar precision pi does not.}
}
\]

## 4. Euler identity is more canonical than the symbol i

The half-turn `H` is fixed by reflection:

\[
\rho(H)=H.
\]

Its character value is `-1` for either orientation. Therefore

\[
\chi(H)=-1
\]

and the endpoint identity

\[
e^{i\pi}=-1
\]

survive orientation reversal even though the selected quarter-turn root changes
from `i` to `-i`.

This yields a precise hierarchy:

1. full-turn identity: canonical;
2. half-turn/reversal: canonical;
3. unordered quarter-turn root pair: canonical after gate refinement;
4. named `i`: requires orientation/chirality;
5. scalar precision-pi readout: descends again by gauge invariance.

## 5. Exact operation-safe quotient criterion

Let `X` be a finite native state space, `F:X->X` a deterministic update, and

\[
q:X\to C_N
\]

a proposed orientation observation.

There exists a well-defined quotient update

\[
\bar F:C_N\to C_N,
\qquad
q\circ F=\bar F\circ q,
\]

if and only if

\[
\boxed{
q(x)=q(y)
\Longrightarrow
q(Fx)=q(Fy)
}
\]

for every `x,y` in `X`.

For a constant one-step rotation one needs the stronger equation

\[
\boxed{
q(Fx)=q(x)+1\pmod N.
}
\]

This is exactly the operation-safe quotient/fiber-constancy test already used in
Enterprise precision theory.

## 6. Why the native descent theorem is still open

The current native foundation supplies:

- one Cell per instantaneous rotating-trajectory state;
- Cell adjacency and triple gates;
- directed line traces and canonical reverse decoding;
- the carrier pivot-star incidence used in the `C6 -> C12` construction.

It does not yet supply a globally typed deterministic rotation update `F` on all
native line-trace/Cell states, nor a proof that two native states with the same phase
observation always have the same observed successor.

Therefore the carrier construction proves

\[
\text{there exists an exact finite phase model},
\]

but not yet

\[
\text{every native rotating trajectory factors through that model}.
\]

The missing theorem is precisely fiber constancy, not a vague request for more
geometry.

## 7. Minimal bridge contract

A future native Euler bridge should provide:

1. a typed native rotating-state domain `X`;
2. a selected pivot/base relation or a pivot-independent construction;
3. a deterministic or explicitly relational rotation transport;
4. a phase observation `q` to the Cell/gate carrier;
5. a proof of the descent implication above for every allowed operation;
6. compatibility with canonical reverse trace without identifying reverse decode
   with groupoid inversion;
7. proof that later dyadic phase refinements are observable precision refinements,
   not merely formal subdivisions.

If item 5 fails, the correct result is a no-go theorem: the coarse phase state loses
information needed to predict the next rotation state.

## 8. Finite witness models

The accompanying regression uses the existing operation-safe quotient tool on two
small models.

Good model:

\[
F(k,h)=(k+1,h),
\qquad
q(k,h)=k.
\]

The hidden state `h` does not affect the next phase, so `q` is safe.

Bad model:

\[
F(k,h)=(k+h,h),
\qquad
q(k,h)=k,
\qquad
h\in\{0,1\}.
\]

Two states in the same phase fiber have different next observed phases, so the
orientation quotient fails.

This shows exactly what must be excluded by a native rotation law.

## 9. Candidate statement

`AC-EM-FREE-F6D046-EULER-ORIENTATION-TORSOR-V1`:

> The gate-refined quarter-turn solutions form a canonical two-element torsor
> exchanged by reflection. A named imaginary unit is an oriented trivialization of
> that torsor, and complex conjugation is the character image of orientation
> reversal. Nevertheless the half-trace, normalized skew trace, Viète precision-pi
> hierarchy, and positive phase-Laplacian eigenvalues are invariant under this
> gauge and therefore descend to the unoriented carrier. Extending the phase model
> to actual native rotating trajectories is equivalent to the exact operation-safe
> fiber-constancy condition; that native descent remains open because the current
> foundation does not yet supply the required global transition law.

Status:

`QUARTER_TURN_TORSOR_EXACT`.

`NO_CANONICAL_I_WITHOUT_ORIENTATION_EXACT`.

`PRECISION_PI_CHIRALITY_DESCENT_EXACT`.

`NATIVE_ROTATION_OPERATION_DESCENT_OPEN`.
