# Euler formula as a rotation character of finite oriented-segment states

Status: `FREE_RESEARCH / CANDIDATE / ANCHOR_EXPOSED / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Question

What is the geometric meaning of

\[
e^{i\theta}=\cos\theta+i\sin\theta
\]

when Enterprise Math treats rotation as primary, the current three-positive-axis slice has three native right sectors of 120 degrees, negative axes are not primitive, and a rotating-segment trajectory has one Cell as its instantaneous native state?

The main candidate is that the complex exponential is not the native line segment itself. It is a character/readout of a rotation quotient of the native trajectory, and the continuous unit circle is a completion of finite rotation states.

## 2. Frozen inputs and boundaries

Use the current canonical three-positive-axis Cell plane only as declared in `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`:

- three positive rays;
- three 120-degree native right sectors;
- no primitive native negative axes required;
- native metric is sector-local Pythagorean and is not the Euclidean carrier metric;
- one rotating-segment trajectory step has one Cell as its instantaneous native state.

This note does **not** identify the Enterprise native metric with the Eisenstein norm and does not promote a complex plane to primitive native ontology.

Freeze boundary:

`ROTATION_CHARACTER_REPRESENTATION != NATIVE_LENGTH_ALGEBRA`.

## 3. First quotient: three-ray rotation is C3-shaped

If a rotating trajectory admits a well-defined orientation quotient recording only which positive-ray class is occupied, the three positive ray classes carry a cyclic permutation structure

\[
C_3=\langle r\mid r^3=1\rangle.
\]

A convenient classical carrier representation sends

\[
r\mapsto \omega,\qquad \omega^3=1,\quad 1+\omega+\omega^2=0.
\]

This is only a rotation-character representation. The relation above must not be used to replace the frozen Enterprise metric by the Eisenstein norm.

Candidate interpretation: the 120-degree native right turn is represented by multiplication by a primitive cube root of unity, not by multiplication by the classical quarter-turn unit `i`.

## 4. Oriented-segment augmentation: C3 x C2

Because primitive negative axes are not required, orientation reversal is not automatically a primitive point/axis state. If one augments a positive-ray segment by one explicit reversal bit

\[
\sigma\in C_2=\{+1,-1\},
\]

then the coarse oriented-ray state space is

\[
C_3\times C_2\cong C_6.
\]

Its six character values can be represented by the six Eisenstein units

\[
\{\pm1,\pm\omega,\pm\omega^2\}.
\]

Important: the abstract isomorphism to `C6` does not assert that a 60-degree physical move is primitive. Native allowed transitions still need to be derived from the Cell trajectory law.

## 5. Exact finite lemma: half-turn and quarter-turn are different resolution requirements

Let an oriented finite rotation system be cyclic of order `N`.

- An exact half-turn element exists iff `2 | N`.
- An exact quarter-turn element `q` satisfying `q^2=-1` exists iff `4 | N`.

Proof of the second statement: write a generator `g` of `C_N`. For even `N`, `-1=g^{N/2}`. A quarter-turn requires

\[
2k\equiv N/2\pmod N.
\]

This congruence is solvable iff `gcd(2,N)=2` divides `N/2`, i.e. iff `4 | N`.

Consequences for the coarse oriented three-ray state `C3 x C2 ~= C6`:

\[
-1\ \text{exists exactly},\qquad i\ \text{does not exist as a native coarse orientation state}.
\]

Therefore the endpoint statement

\[
e^{i\pi}=-1
\]

may have an exact coarse geometric meaning even when the intermediate classical quarter-turn unit `i` is not itself a native state at that resolution.

This lemma is standard finite cyclic-group mathematics; no historical novelty is claimed.

## 6. Euler formula retyped as a rotation character

Classically, with

\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad J^2=-I,
\]

one has

\[
\exp(\theta J)=\cos\theta\,I+\sin\theta\,J.
\]

The complex number `i` is the scalar avatar of the oriented quarter-turn operator `J` under the standard identification of this two-dimensional rotation-operator algebra with `C`.

Enterprise reinterpretation candidate:

1. native object: a discrete rotating-segment/Cell trajectory;
2. derived quotient: a finite orientation state;
3. character: a multiplicative complex readout of that finite rotation state;
4. analytic completion: a continuous phase coordinate `theta` in which the character is written `e^{i theta}`.

Thus

`i = CONTINUUM_ROTATION_GENERATOR_COORDINATE`,

not automatically

`i = NATIVE_SPATIAL_AXIS`.

## 7. Discrete Euler law before any continuum angle

At finite orientation resolution, let `R` be one declared rotation transition in a cyclic quotient and let `chi` be a one-dimensional character. Then exactly

\[
\chi(R^{k+\ell})=\chi(R^k)\chi(R^\ell).
\]

Writing `z_k=chi(R^k)`,

\[
z_{k+1}z_k^{-1}=\chi(R)
\]

is the native multiplicative constant-turn law. No derivative, logarithm, sine, cosine, or real angle is required.

Only after analytic phase allocation

\[
\chi(R)=e^{i\delta}
\]

does this become

\[
z_k=e^{ik\delta}z_0.
\]

This suggests that logarithm/argument belongs to the completion/decoder layer: it converts multiplicative finite transport into additive phase.

## 8. Euler identity

Under this typing,

\[
e^{i\pi}+1=0
\]

means:

`HALF_PERIOD_ROTATION_CHARACTER = ORIENTATION_REVERSAL`.

The symbol `-1` is therefore read first as a signed/oriented reversal state in the character representation, not as evidence that a primitive negative native axis must exist.

Similarly,

\[
e^{2\pi i}=1
\]

means:

`FULL_PERIOD_ROTATION_CHARACTER = RETURN_TO_INITIAL_ORIENTATION`.

This is the strongest current geometric reading of Euler's identity compatible with the positive-axis foundation.

## 9. Dyadic rotation-refinement tower and emergence of i

Starting from an exact half-turn/reversal state `-1`, refine orientation by repeatedly adjoining square roots of the rotation operator:

\[
U_0=-1,\qquad U_{n+1}^2=U_n.
\]

In the classical complex character completion one may choose

\[
U_n=e^{i\pi/2^n}.
\]

Then:

- `U_0=-1` is half-turn;
- `U_1=i` is quarter-turn;
- `U_2=e^{i\pi/4}` introduces the `sqrt(2)` coordinate;
- further levels generate the familiar nested half-angle radical tower.

For the coarse oriented three-ray shell, the inclusion picture is naturally tested as

\[
\mu_6\subset\mu_{12}\subset\mu_{24}\subset\cdots.
\]

At the first dyadic refinement (`12` orientations), `4 | 12`, so an exact quarter-turn state becomes available. This gives a precise finite-resolution sense in which `i` can **emerge under orientation refinement** rather than being primitive.

Candidate bridge to the pi-formula program: Viète's nested radicals should be tested as the real-coordinate trace of this dyadic half-turn refinement tower; the already observed `(sqrt(2)-1)` half-angle factors in the N=58 line should be compared against the same rotation-refinement mechanism without forcing the match.

## 10. What pi means here

Euler's formula alone does not derive the numerical value of pi.

It fixes a role:

\[
\pi = \text{the continuous phase assigned to one exact half-turn},
\]

and

\[
2\pi = \text{the continuous phase assigned to one full-turn closure}.
\]

A numerical `precision-pi` therefore requires an additional geometric/readout calibration from the discrete trajectory to the analytic phase coordinate. Different pi formulas can now be tested as competing finite-to-continuous calibrations of the same rotation closure.

Freeze:

`EULER_CHARACTER_SEMANTICS != NUMERICAL_DERIVATION_OF_PI`.

## 11. Unifying research diagram

Current candidate chain:

```text
native rotating Cell trajectory
    -> operation-safe orientation quotient (to be proved)
    -> C3 positive-ray rotation
    -> optional C2 orientation-reversal augmentation
    -> C3 x C2 ~= coarse six-state oriented shell
    -> dyadic rotation-root refinements
    -> roots-of-unity character readouts
    -> analytic/topological completion U(1)
    -> e^(i theta)
```

Under this chain:

- `cos(theta)` and `sin(theta)` are coordinate readouts of the completed rotation character;
- `i` is the quarter-turn generator coordinate of the completed representation;
- `pi` is the half-period calibration;
- Euler's identity is the statement that half-period transport equals orientation reversal.

## 12. Immediate falsification targets

1. Prove or kill existence of an operation-safe orientation quotient from the actual Cell trajectory dynamics to the three-ray cycle.
2. Determine whether the reversal bit is canonical for a rotating segment or is an extra frame choice.
3. Prove which refinement operation, if any, canonically produces `mu_12` from the coarse oriented shell rather than merely postulating angle bisection.
4. Check whether the dyadic rotation-root tower predicts Viète/half-angle factors before reading the classical formulas.
5. Test whether the same rotation-completion interpretation survives Ramanujan families beyond N=58.
6. Never identify the Eisenstein carrier representation with the native Enterprise metric without a separate theorem.

## 13. Current candidate statement

`AC-EM-FREE-F6D046-EULER-ROTATION-CHARACTER-V1`:

> In the current Enterprise three-positive-axis slice, Euler's complex exponential is best typed as a character/analytic completion of a finite oriented-segment rotation quotient. The positive-ray rotation layer is C3-shaped; adding an explicit orientation-reversal bit yields a coarse C3 x C2 state with exact half-turn but no exact quarter-turn. The classical unit i appears only when orientation resolution is refined to a level divisible by four. Under continuous completion, pi is the phase assigned to half-turn and Euler's identity expresses half-period transport as orientation reversal.

Status: `RAW_AXIOM_CANDIDATE / PARTLY_STANDARD_GROUP_THEORY / NATIVE_QUOTIENT_AND_REFINEMENT_NOT_YET_DERIVED`.
