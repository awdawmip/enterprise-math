# Euler exponential as a non-split rotation cover and winding quotient

Status: `FREE_RESEARCH / STRUCTURAL CONSEQUENCE / NOT_FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Purpose

The Cell–gate dyadic tower explains where finite half-turn roots live. This note answers the next question: why can the square-root refinement not be reduced to a globally single-valued static operation, and what is the exact finite operator whose continuous completion becomes Euler's exponential?

The answer has three parts.

1. Every even cyclic square-root cover is a non-split \(C_2\)-extension.
2. A directed path selects a root; an unoriented state does not.
3. On each finite cycle, Euler's formula is already the spectral decomposition of the successor permutation into symmetric and skew parts.

The continuous exponential then appears as the winding-history quotient of the completed finite tower.

## 2. The square-root fiber is intrinsically two-valued

Let

\[
q_N:\mu_{2N}\longrightarrow\mu_N,
\qquad
q_N(w)=w^2.
\]

For every \(z\in\mu_N\),

\[
q_N^{-1}(z)=\{w,-w\}.
\]

Thus every finite rotation root is naturally a \(C_2\)-torsor.

In additive exponent coordinates this is

\[
0\longrightarrow C_2
\longrightarrow C_{2N}
\overset{q_N}{\longrightarrow}
C_N
\longrightarrow0,
\]

where \(q_N([k]_{2N})=[k]_N\).

## 3. Non-splitting for every even phase order

Assume \(N\) is even. Suppose a group section

\[
s:C_N\longrightarrow C_{2N}
\]

of \(q_N\) existed. The generator \([1]_N\) would have to map to a residue congruent to \(1\) modulo \(N\), hence to either \([1]_{2N}\) or \([N+1]_{2N}\).

Both representatives are odd. Since \(N+1\) is odd,

\[
\gcd(N+1,2N)=1,
\]

so both possible lifts have order \(2N\). But the image of an element of order \(N\) under a homomorphism must have order dividing \(N\), a contradiction.

Therefore:

\[
\boxed{
N\text{ even}
\Longrightarrow
0\to C_2\to C_{2N}\to C_N\to0
\text{ is non-split}.
}
\]

All Enterprise Euler levels have \(N=6\cdot2^m\), so every root refinement is a non-split double cover.

Consequently, there is no globally multiplicative single-valued square-root selector on the finite rotation shell. The correct object is path/fiber-valued:

\[
\sqrt[\mathrm{rot}]{z}=\{w,-w\}.
\]

A directed rotation history and an initial branch choice select one lift along a path. This is structurally compatible with the existing path-valued square-root discipline, but it is a distinct typed application: the present root is a root of a rotation transport state, not a root of the native Pythagorean length norm.

Freeze:

`ROTATION_ROOT_FIBER != VECTOR_NORM_ROOT_FIBER`.

`GLOBAL_MULTIPLICATIVE_ROOT_SECTION_DOES_NOT_EXIST`.

## 4. Chirality is the branch selector

At the first Cell/gate refinement,

\[
q_6^{-1}(-1)=\{G_1,G_4\}.
\]

Cyclic reflection exchanges the two gates. Therefore the bare dihedral incidence structure has no invariant root choice.

After choosing a directed cyclic order, one may select the root encountered on the chosen forward short arc. Reversing chirality selects the other root.

This is not an arbitrary numerical convention. It is the minimum extra datum required to lift the reversal state through the non-split cover.

## 5. Finite exponential as a successor character

Let \(H_m=C_{2^{m+1}}\) be the distinguished dyadic factor and let \(S_m\) be its successor permutation. Choose a faithful character state

\[
\phi_m(k)=z_m^k,
\qquad
z_m^{2^m}=-1.
\]

Then

\[
S_m\phi_m=z_m\phi_m.
\]

This is the exact finite exponential law: one discrete phase transition multiplies the character by a constant root of unity. No differential equation is needed.

## 6. Symmetric/skew decomposition of the rotation step

Let \(J=z_1\), so \(J^2=-1\), and define

\[
c_m=\frac{z_m+z_m^{-1}}2,
\qquad
s_m=\frac{z_m-z_m^{-1}}{2J}.
\]

Define operators

\[
C_m=\frac{S_m+S_m^{-1}}2,
\qquad
A_m=\frac{S_m-S_m^{-1}}{2J}.
\]

Then

\[
S_m=C_m+J A_m.
\]

On the character mode \(\phi_m\),

\[
C_m\phi_m=c_m\phi_m,
\qquad
A_m\phi_m=s_m\phi_m.
\]

Therefore

\[
z_m=c_m+Js_m
\]

is the eigenvalue form of the exact operator decomposition

\[
\boxed{
\text{directed rotation successor}
=
\text{orientation-even adjacency}
+
J\cdot\text{orientation-odd incidence}.
}
\]

Under inversion of the cycle orientation, \(C_m\) is unchanged and \(A_m\) changes sign. Hence cosine is the reversal-even readout and the full \(J\)-weighted sine component is the reversal-odd readout.

## 7. Real two-dimensional mode

The conjugate character pair \(z_m,z_m^{-1}\) spans a real two-dimensional invariant mode. In a real basis, the successor is

\[
S_m\big|_{\mathrm{mode}}
=
\begin{pmatrix}
c_m&-s_m\\
s_m&c_m
\end{pmatrix}.
\]

The operator

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
J^2=-I,
\]

is the orientation operator of this real mode.

Thus \(i\) is best typed as the scalar packaging of a two-dimensional orientation operator on a rotation mode. It is not evidence for a primitive negative or imaginary spatial axis.

## 8. Exact finite derivative and Laplacian equations

For the selected character mode, define the chord-normalized skew difference

\[
D_m
=
\frac{S_m-S_m^{-1}}{2s_m}
\]

and the chord-normalized symmetric second difference

\[
L_m
=
\frac{S_m+S_m^{-1}-2I}{2(1-c_m)}.
\]

Then, exactly at every finite level,

\[
\boxed{D_m\phi_m=J\phi_m}
\]

and

\[
\boxed{L_m\phi_m=-\phi_m}.
\]

These are finite rotation-cycle analogues of

\[
f'=if,
\qquad
f''=-f,
\]

but here they are exact algebraic eigen-equations rather than limits.

The continuum derivative appears only when the finite chord normalization is identified with an additive phase increment and the refinement depth tends to infinity.

## 9. Winding history and exponential collapse

The continuous completion has the exact sequence

\[
0\longrightarrow 2\pi_{\mathrm{rot}}\mathbf Z
\longrightarrow \mathbf R
\overset{E}{\longrightarrow} U(1)
\longrightarrow1,
\]

with

\[
E(\theta)=e^{J\theta}
\]

after analytic identification.

The domain records accumulated rotation history. The codomain records only current orientation. Every pair

\[
\theta,
\qquad
\theta+2k\pi_{\mathrm{rot}}
\]

has the same orientation character.

Therefore the exponential map itself is an Enterprise-style quotient/collapse:

\[
\boxed{
\text{accumulated winding history}
\longrightarrow
\text{current orientation}
}
\]

with full-turn histories identified.

The constant \(\pi_{\mathrm{rot}}\) is half the deck period of this collapse. Euler's identity is the half-period endpoint:

\[
E(\pi_{\mathrm{rot}})=-1.
\]

## 10. The pi-free normalized form

Before radian calibration, use the normalized turn coordinate

\[
t\in\mathbf R/\mathbf Z.
\]

Then the core relations are simply

\[
E(0)=1,\qquad E(1/2)=-1,\qquad E(t+u)=E(t)E(u).
\]

No \(\pi\) occurs.

The classical symbol \(\pi\) appears when the full turn is assigned generator length \(2\pi_{\mathrm{rot}}\):

\[
\theta=2\pi_{\mathrm{rot}}t.
\]

Thus \(\pi\) is not needed to define the finite phase group. It calibrates the continuous additive cover against the normalized rotation character.

## 11. Strong geometric interpretation

The current strongest interpretation of Euler's formula is:

\[
\boxed{
e^{i\theta}
=
\text{the character-valued current orientation obtained by collapsing an accumulated directed rotation history modulo full turns}.
}
\]

Its components mean:

- \(i\): orientation generator on a real two-dimensional character mode;
- \(\cos\theta\): reversal-even part of the rotation successor;
- \(i\sin\theta\): reversal-odd part;
- \(2\pi\): one deck period of the winding-history quotient;
- \(e^{i\pi}=-1\): half a deck period equals endpoint reversal.

The finite Cell/gate tower supplies exact algebraic samples of this cover. Viète's nested radicals are the symmetric traces of repeatedly lifted half-turn roots.

## 12. Boundaries

`FINITE_NONSPLITTING_IS_PROVED_STANDARD_GROUP_THEORY`.

`FINITE_SHIFT_SPECTRAL_DECOMPOSITION_IS_PROVED_STANDARD_HARMONIC_ANALYSIS`.

`ENTERPRISE_TYPING_AND_UNIFICATION_IS_RESEARCH_CANDIDATE`.

`NO_GLOBAL_OPERATION_SAFE_CELL_TRAJECTORY_QUOTIENT_YET`.

`NO_CLAIM_THAT_CONTINUOUS_TIME_IS_NATIVE`.

`NO_CLAIM_THAT_J_IS_A_NATIVE_SPATIAL_AXIS`.

`NO_IDENTITY_YET_BETWEEN_THIS_C2_ROOT_FIBER_AND_THE_TETRAHEDRAL_OR_PELL_C2_CLASSES`.
