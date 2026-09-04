# The cube frame cover: Euler half-turn parity and the Ramanujan return kernel

Status: `FREE_RESEARCH / EXACT FINITE BRIDGE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Main synthesis

The four FCC carrier slices form the vertices of `K4`.  The shortest tetrahedral normal connection has the exact triangular holonomy

\[
H_u=2u_u u_u^{\mathsf T}-I,
\]

which fixes the starting normal and negates the tangent slice.  The present note proves that this local fact controls **every** path in `K4`:

\[
\boxed{
\text{closed path holonomy at }u
=
\begin{cases}
I,&\text{even edge length},\\
H_u,&\text{odd edge length}.
\end{cases}}
\]

Thus the connection has a canonical central `C2` curvature character given by path-length parity.

The corresponding two-sheet frame cover of `K4` is the cube graph `Q3`.  Its eight vertices may be encoded by

\[
\{\pm n_A,\pm n_B,\pm n_C,\pm n_D\}
=
\{(\pm1,\pm1,\pm1)\}.
\]

The sign in this display is a **frame-phase code** for the two sheets.  It must not be misread as saying that the shortest `SO(3)` edge transport sends `n_u` to `-n_v`; it sends `n_u` to `n_v`.  The cube code records the extra tangent half-turn sheet relative to a chosen developed frame.

The same eight sign triples are exactly the step alphabet of the BCC return model whose `2n`-step return probability is

\[
\boxed{
\frac{\binom{2n}{n}^3}{8^{2n}}
=
\left(\frac{(1/2)_n}{n!}\right)^3.
}
\]

Hence the finite state space underlying the signature-`1/2` Ramanujan kernel is also the canonical frame double cover resolving the Euler half-turn holonomy.

## 2. The two-sheet cube cover

Let

\[
\widetilde V=\{(u,\epsilon):u\in\{A,B,C,D\},\ \epsilon\in\mathbf F_2\}.
\]

Put an edge between `(u,epsilon)` and `(v,epsilon+1)` whenever `u != v`.  The projection

\[
\pi:\widetilde V\to V(K_4),
\qquad
(u,\epsilon)\mapsto u
\]

is the canonical bipartite double cover of `K4`.

Encode the four zero-sheet states by

\[
\begin{aligned}
A_0&\mapsto(1,-1,-1),\\
B_0&\mapsto(-1,1,-1),\\
C_0&\mapsto(-1,-1,1),\\
D_0&\mapsto(1,1,1),
\end{aligned}
\]

and the one-sheet state by the antipodal sign triple.  If `u != v`, then the codes of `(u,epsilon)` and `(v,epsilon+1)` differ in exactly one coordinate.  Therefore

\[
\boxed{\widetilde K_4\cong Q_3.}
\]

The deck involution

\[
\delta(u,\epsilon)=(u,\epsilon+1)
\]

is encoded by the antipodal map on the cube.

### Corollary 2.1 — odd loops change the frame sheet

A lifted path toggles the sheet once per edge.  Consequently a closed base path of length `m` returns to the original sheet exactly when `m` is even.  For odd `m` it reaches the deck partner.

In particular, every triangular face loop lifts to a three-edge cube path from one code vertex to its antipode.  Two traversals are required to close upstairs.

## 3. Local transport relations

For distinct slices let `T_uv` be the shortest proper rotation carrying `u_u` to `u_v`, and let

\[
H_u=2u_u u_u^{\mathsf T}-I.
\]

The tetrahedral matrix theorem gives four relations:

\[
T_{vu}T_{uv}=I,
\tag{3.1}
\]

\[
T_{vw}T_{uv}=T_{uw}H_u
\qquad(u,v,w\text{ distinct}),
\tag{3.2}
\]

\[
T_{uv}H_u=H_vT_{uv},
\tag{3.3}
\]

\[
H_u^2=I.
\tag{3.4}
\]

Equation (3.2) is the face-holonomy theorem with the closing edge removed.  Equation (3.3) says that a proper transport carries the starting-axis half-turn to the endpoint-axis half-turn.

## 4. Arbitrary path theorem

For a path

\[
P=(v_0,v_1,\ldots,v_m),
\qquad v_{j+1}\ne v_j,
\]

define the ordered transport

\[
T(P)=T_{v_{m-1}v_m}\cdots T_{v_0v_1}.
\]

### Theorem 4.1 — endpoint and parity determine all path transport

If `v_m != v_0`, then

\[
\boxed{
T(P)=T_{v_0v_m}H_{v_0}^{m-1}.
}
\]

If `v_m=v_0`, then

\[
\boxed{
T(P)=H_{v_0}^{m}.
}
\]

Because `H^2=I`, only the parity of the exponent matters.

Proof.  Induct on `m`.  Appending an edge to a path ending at the start gives `T_{uw}H_u^m`.  Appending an edge to a path ending away from the start has two cases.  Returning directly to the start uses (3.1) and changes the desired exponent by two.  Moving to a third vertex uses (3.2) and toggles the exponent once.  Equation (3.4) closes the parity reductions.  This proves both formulas simultaneously.

### Corollary 4.2 — complete closed-loop holonomy

For every closed path based at `u`,

\[
\boxed{
T(P)=H_u^{|P|}.
}
\]

Thus even loops have identity holonomy and odd loops have the Euler tangent half-turn.

### Corollary 4.3 — flat development on the cube

Two base paths from `u` to `v` induce the same transport exactly when their lengths have the same parity.  Equivalently, transport is path independent after endpoints are lifted to the cube frame cover.

A developed frame can therefore be assigned to every cube vertex.  The deck involution at the slice `v` acts on that frame by `H_v`.  The connection is flat upstairs and has a `C2` descent defect downstairs.

## 5. The canonical `S4`-invariant curvature class

Give every edge of `K4` the coefficient one:

\[
\omega(e)=1\in\mathbf F_2.
\]

Its evaluation on a closed path is its edge length modulo two.  Every triangular cycle therefore has value one and every even cycle value zero.

In the previously established identification

\[
C^1(K_4;\mathbf F_2)/\delta C^0(K_4;\mathbf F_2)
\cong\mathbf F_2^3,
\]

the class of `omega` is

\[
\boxed{(1,1,1).}
\]

An exhaustive `S4` action calculation gives:

\[
\boxed{
\left(H^1(K_4;\mathbf F_2)\right)^{S_4}
=\{0,[\omega]\}.
}
\]

So `[omega]` is the unique nonzero fully tetrahedrally symmetric `C2` class.  The shortest normal connection realizes precisely this class as central tangent half-turn curvature.

This coefficient must be typed correctly.  It is not the earlier edge bit saying whether a handoff maps `J` to `+J` or `-J`.  Shortest proper rotations preserve local chirality.  The present class records the **central phase holonomy** accumulated around odd cycles.

## 6. Spin refinement and double-angle structure

For the integral edge spinors

\[
p_{uv}=\left(1,\frac{n_u\times n_v}{2}\right),
\qquad N(p_{uv})=3,
\]

the unit lift is `q_uv=p_uv/sqrt(3)`.  Around an oriented face,

\[
q_{wu}q_{vw}q_{uv}
=\pm J_u^{\rm Spin},
\]

where the sign is the orientation of the face and

\[
(J_u^{\rm Spin})^2=-1.
\]

Its adjoint action on the tangent slice is the vector half-turn:

\[
\operatorname{Ad}_{\pm J_u^{\rm Spin}}|_{u_u^\perp}=-I.
\]

Hence one face traversal has:

- order four in the Spin lift;
- order two in the tangent-vector representation;
- an orientation sign exchanged by reversing the loop;
- the same projected Euler endpoint `-1` in both orientations.

This is the finite double-angle mechanism behind the familiar distinction between `2pi` vector periodicity and `4pi` spin periodicity.

## 7. The cube return count

Let

\[
\Omega=\{(\sigma_1,\sigma_2,\sigma_3):\sigma_i\in\{+1,-1\}\}
\]

be the eight cube states.  At each time choose one element of `Omega` uniformly and add it as a step in `Z^3`.

A `2n`-step sequence returns to the origin exactly when each coordinate has `n` plus signs and `n` minus signs.  Since the three coordinate sign sequences are independent, the number of return words is

\[
\boxed{R_{2n}=\binom{2n}{n}^3.}
\]

There are `8^(2n)` total words, so

\[
\boxed{
\Pr(S_{2n}=0)
=
\frac{\binom{2n}{n}^3}{8^{2n}}
=
\left(\frac{\binom{2n}{n}}{4^n}\right)^3
=
\left(\frac{(1/2)_n}{n!}\right)^3.
}
\]

The generating function is

\[
\boxed{
G(z)=\sum_{n\ge0}
\left(\frac{(1/2)_n}{n!}\right)^3 z^{2n}
={}_3F_2\!\left(\frac12,\frac12,\frac12;1,1;z^2\right).
}
\]

This is the classical signature-`1/2`/BCC return kernel.  The new project-level bridge is that its eight-step alphabet is the same finite cube that develops the four-slice Euler half-turn connection.

## 8. Euler and Ramanujan as two readouts of one finite cover

The cube now supports two distinct operations.

### Holonomy readout

A base triangle changes the frame sheet and its shortest transport acts as

\[
H_u|_{u_u^\perp}=-I.
\]

After continuous phase completion, this is

\[
\exp(\pi J_u)=-I.
\]

### Return-statistics readout

Long words in the same eight-state alphabet are aggregated by coordinate balance.  Their return kernel is the hypergeometric coefficient

\[
\left((1/2)_n/n!\right)^3.
\]

Classical Ramanujan identities apply a first-order response to this Green function at a special algebraic state and recover `1/pi`.

These are not the same map.  The first uses noncommutative slice transport; the second uses commutative return aggregation.  But they now share an exact finite carrier:

\[
\boxed{
\text{four slices plus central half-turn sheet}
\cong
Q_3
\cong
\text{eight BCC sign directions}.
}
\]

This supports a sharper research program: Ramanujan acceleration may be interpreted as a statistical compression of the same frame-resolved rotation cover whose elementary odd loop realizes the Euler half-turn.

## 9. Boundaries

Proved at the selected carrier level:

- the cube is the canonical bipartite/frame double cover of `K4`;
- all path transports depend only on endpoint and edge-length parity;
- all closed holonomies are identity or tangent half-turn;
- the parity class is the unique nonzero `S4`-fixed class in `H^1(K4;F2)`;
- the Spin face lift is an order-four refinement of the order-two vector holonomy;
- the cube/BCC return count is exactly the signature-`1/2` hypergeometric kernel.

Not proved:

- that the frame-sheet cube is a primitive P000 native state space;
- that shortest tetrahedral transport is forced by all native six-dimensional dynamics;
- that a Ramanujan `1/pi` functional follows from the holonomy theorem alone;
- that the central phase class equals the O(2) chirality class, tetrahedral residual torsion, backtracking sign, or Pell-shell sign;
- that the special Ramanujan evaluation parameter is derived from this cube without the separate Cell-overlap bridge.

The exact advance is nevertheless substantial: Euler half-turn holonomy and the Ramanujan signature-`1/2` return kernel now arise from the same eight-state finite cover, with their distinct readout operations explicitly separated.