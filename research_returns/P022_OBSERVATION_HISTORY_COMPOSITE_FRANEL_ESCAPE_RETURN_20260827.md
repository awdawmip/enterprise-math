# P022 Observation-History Composite Franel Escape — Research Checkpoint

Status: `ACTIVE / NONTERMINAL / DUAL_HASSE_ADJOINT_REDUCTION_FROZEN`

Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`  
Claim: `chatgpt-p022obs-20260827-1645`  
Researcher: `EM-P022OBS-D5D438`

## Current durable advance

The accepted `q=3r-1` boundary reduction is consumed rather than replayed.
Writing

\[
M=3m,\qquad r=2M=6m,\qquad q=6M-1=18m-1,
\]

the boundary obstruction is already exactly equivalent to

\[
q\mid F_{6m}
\iff
K_{3m}\equiv0\pmod q
\iff
W_{3m}\equiv0\pmod q,
\]

where

\[
W_M=\sum_{j=0}^{2M-1}
\binom{2M}{j}\binom{M+j}{j}\binom{2M-1}{j}.
\]

The previous checkpoint further split `W_(3m)` into three equal-length
`j mod 3` sections and identified one common conductor-18 rank-nine datum.
The new advance below shows that the scalar rank-three conjugate-Hasse route
inside this structure is exactly redundant, thereby isolating the first
independent matrix-level target.

## 1. Universal fixed-parameter form of the sign-free kernel

For a general prime

\[
p=6M-1,
\]

put

\[
N=2M-1=\frac{p-2}{3}.
\]

Termwise modulo `p`,

\[
\boxed{
W_M\equiv
\sum_{j=0}^{N}
\frac{(-1/3)_j(2/3)_j(7/6)_j}{(j!)^3}
\pmod p.
}
\]

Modulo integer contiguous shifts, its numerator signature is

\[
\left(\frac16,\frac23,\frac23\right),
\]

exactly the Dwork/Galois-conjugate `j=5` character block to the already-frozen
canonical one-third datum

\[
\left(\frac56,\frac13,\frac13\right).
\]

Thus the double-horizon kernel does not introduce a new unrelated rank-three
motive; it is a contiguous realization of the conjugate sector of the same
period-two system.

## 2. Exact conjugate first-jet bridge

Define

\[
d_j=\frac{(1/6)_j(2/3)_j^2}{(j!)^3},
\qquad
D_p(z)=\sum_{j=0}^{N}d_jz^j.
\]

Then

\[
\frac{d_{j+1}}{d_j}
=\frac{(6j+1)(3j+2)^2}{54(j+1)^3},
\qquad
\frac{c_j}{d_j}=-\frac{6j+1}{3j-1},
\]

where `c_j` is the coefficient of the universal `W_M` truncation.  With

\[
R_j=\frac{81j^3}{3j-1},
\]

the exact rational Gosper identity is

\[
\boxed{
\frac{c_j}{d_j}
=-2-\frac{27}{2}j
+R_{j+1}\frac{d_{j+1}}{d_j}-R_j.
}
\]

At the endpoint `N=(p-2)/3`, the next conjugate coefficient contributes a
square factor `(3N+2)^2=p^2`, while `R_(N+1)` contributes only one denominator
factor `p`; the terminal certificate therefore vanishes modulo `p`.
Consequently

\[
\boxed{
W_M\equiv
-2D_p(1)-\frac{27}{2}\theta D_p(1)
\pmod p.
}
\]

The conjugate Picard--Fuchs equation gives at `z=1`

\[
\boxed{
81\theta^2D_p+36\theta D_p+4D_p=0.
}
\]

Its local exponents at `z=1` are `0,1,1/2`; since

\[
\deg D_p=\frac{p-2}{3}<\frac p2,
\]

a scalar zero `D_p(1)=0` is simple.  Hence a boundary zero lies in the
conjugate scalar-ordinary locus and is equivalent to

\[
\boxed{
W_M=0
\iff
\frac{\theta D_p(1)}{D_p(1)}=-\frac4{27}.
}
\]

## 3. Original and conjugate Hasse operators are exact formal adjoints

Let `P_p` be the previously frozen canonical one-third Hasse polynomial with
parameters

\[
\left(\frac56,\frac13,\frac13\right).
\]

Its differential operator in ordinary derivative form is

\[
L_P=a_3\partial^3+a_2\partial^2+a_1\partial+a_0
\]

with

\[
a_3=z^2(1-z),
\quad a_2=3z-\frac92z^2,
\quad a_1=1-\frac{19}{6}z,
\quad a_0=-\frac5{54}.
\]

The negative formal adjoint has coefficients

\[
a_3,
\quad3a_3'-a_2,
\quad3a_3''-2a_2'+a_1,
\quad a_3'''-a_2''+a_1'-a_0.
\]

They simplify exactly to the conjugate operator coefficients, whose constant
term is

\[
-\frac2{27}=-\frac16\left(\frac23\right)^2.
\]

Therefore

\[
\boxed{L_D=-L_P^*.}
\]

The associated Lagrange concomitant vanishes at `z=0`, hence identically.  At
`z=1` it becomes

\[
\boxed{
3\left(D_p\theta P_p+P_p\theta D_p\right)+P_pD_p=0.
}
\]

Thus on the joint scalar-ordinary locus

\[
\boxed{
\frac{\theta P_p}{P_p}+
\frac{\theta D_p}{D_p}
=-\frac13.
}
\]

The existing original-Hasse criterion for a one-third Franel zero is

\[
\frac{\theta P_p}{P_p}=-\frac5{27}.
\]

The conjugate boundary criterion is

\[
\frac{\theta D_p}{D_p}=-\frac4{27}.
\]

Since

\[
-\frac5{27}-\frac4{27}=-\frac13,
\]

these are not two independent first-order constraints.  They are the two
faces of the exact formal-adjoint pairing.

## 4. Route pruning

This proves a genuine negative structural result about the proof search:

> Adding the scalar Dwork-conjugate Hasse first jet cannot close the remaining
> `q=3r-1` nonvanishing problem, because it is forced by the original Franel
> first-jet condition through the adjoint Lagrange identity.

Therefore the next independent invariant must be matrix/second-order.  Viable
forms include:

- a `2 x 2` transfer minor or Casoratian for the conductor-18 three-section;
- a Cartier/Hasse--Witt off-diagonal block determinant on the `{1,5}` character
  orbit;
- an equivalent second-order invariant coupling the accepted Hahn diagonal to
  the conductor-18 section transfer.

The current preferred attack is to express the three equal-length section
functionals as contiguous operators in a common rank-three/rank-nine basis and
compute the first nonzero minor after quotienting the scalar adjoint relation.

## 5. Exact controls

The executable theorem adds two useful controls.

At `p=107`, both scalar Hasse values vanish while the Franel/boundary
obstruction is nonzero.  The conjugate scalar zero is simple.  This prevents a
false scalar-Hasse nonvanishing shortcut.

At `p=149`, the known non-target control `149 | F_50` satisfies both logarithmic
first-jet targets exactly:

\[
\frac{\theta P}{P}=-\frac5{27},
\qquad
\frac{\theta D}{D}=-\frac4{27}.
\]

This is a control for the adjoint theorem, not an admissible P022 counterexample.

## 6. Durable outputs

Added on the active research branch:

- `src/enterprise_math/p022_barlow_franel_boundary_dual_hasse_jet.py`;
- `tests/test_p022_barlow_franel_boundary_dual_hasse_jet.py`;
- `docs/P022_BARLOW_FRANEL_BOUNDARY_DUAL_HASSE_ADJOINT.en.md`.

They encode the universal truncation, exact conjugate Gosper reduction,
conjugate Picard--Fuchs gate, scalar-zero simplicity, formal-adjoint operator
identity, Lagrange relation, and paired first-jet controls.

## Current unfinished unit

The all-parameter nonvanishing theorem remains open:

\[
W_{3m}\not\equiv0\pmod{18m-1}
\]

under the admissible P022 twin-boundary prime conditions.

The smallest genuinely new unfinished unit is now:

\[
\boxed{
\text{construct and evaluate the first independent matrix/second-order
conductor-18 transfer invariant after quotienting the scalar adjoint pair.}
}
\]

No larger finite census is promoted to proof, and no task HANDOFF is emitted.
