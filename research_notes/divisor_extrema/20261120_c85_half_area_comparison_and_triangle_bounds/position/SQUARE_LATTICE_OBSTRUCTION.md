# C85 — an exact obstruction after all three source phases are averaged

The full Haar position constant is
\(I_\theta=\mathbb E_{\Lambda,\alpha}S_\theta(\Lambda,\alpha)^{1/10}\).
The C84 fixed-phase counterexample already excludes pointwise Jensen.
The calculation below shows that integrating all three phases first still
does not give a midpoint-maximization statement for each lattice.

## 1. A completely explicit fixed-lattice curve

Fix the auxiliary unit-covolume lattice \(\Lambda=\mathbb Z^2\). Let
\(F^\square_\theta(\sigma^2)\) be the probability, averaged over the three
independent uniform source phases, that no nonzero vector of
\(\sigma\mathbb Z^2\) remains in all three source cells, with marks
\((u,(1-\theta)u+\theta v,v)\). Write
\(t=\min(\theta,1-\theta)\).

**Exact formula.**

\[
\boxed{
F^\square_\theta(\sigma^2)=
\begin{cases}
2t\sigma^3,&0<\sigma\leq1/2,\\[2mm]
(2\sigma-1)^2+2\sigma(1-\sigma)(2\sigma-1)
+2t\sigma(1-\sigma)^2,&1/2\leq\sigma\leq1,\\[2mm]
1,&\sigma\geq1.
\end{cases}}
\tag{1}
\]

These formulas average phases only. They are not the Haar function
\(F_\theta\) and do not contradict its half-area comparison.

### Proof for \(0<\sigma\leq1/2\)

If an endpoint phase lies in \([\sigma,1-\sigma]\), both signs of the
corresponding axis vector are eligible at that endpoint. Their two middle
phase collision intervals cover the whole unit interval, since the sum of
the two middle step lengths is at most \(2\sigma\leq1\).
Thus uniqueness can only occur when both endpoint phases lie in their two
corner strips, each of length \(\sigma\).

If the two corner signs are opposite, the corresponding two axis vectors
have opposite middle signs with absolute step lengths
\((1-\theta)\sigma\) and \(\theta\sigma\). Their collision intervals again
cover the whole middle phase interval, because their sum is
\(\sigma\leq1\).

For either of the two same-sign corner pairs, all eligible endpoint
vectors have nonnegative integer coordinates, or all have nonpositive
integer coordinates, relative to the source. Both elementary axis vectors
are eligible, and every other nonzero eligible vector has middle magnitude
at least \(t\sigma\). Consequently the unoccupied middle phase length is
exactly \(t\sigma\). The two endpoint corner pairs each have area
\(\sigma^2\), proving \(2t\sigma^3\).

This reasoning includes all off-axis competitors such as \((1,-2)\) and
\((1,-3)\). They cannot rescue uniqueness in a region already covered by
the two axis collision intervals; in the same-sign corners they are not
eligible endpoint competitors.

### Proof for \(1/2\leq\sigma\leq1\)

Along each endpoint axis there is either no neighbor, a positive neighbor,
or a negative neighbor. Their phase measures are respectively
\(q=2\sigma-1\), \(p=1-\sigma\), and \(p\). The cases are exhaustive:

- No neighbor on either axis: phase contribution \(q^2\).
- A neighbor on exactly one axis: contributions
  \(2pq(1-\theta)\sigma+2pq\theta\sigma=2pq\sigma\).
- Same-sign neighbors on both axes: the minimum middle magnitude is
  \(t\sigma\), contributing \(2p^2t\sigma\).
- Opposite-sign neighbors on both axes: the two axis collision intervals
  cover the middle phase interval, contributing zero.

Every possible lattice point lies in this endpoint two-by-two grid, so no
other direction has been omitted. This gives the second line of (1).
For \(\sigma\geq1\), the two endpoint cells contain no nonzero vector
except on null boundaries, giving the final line.

## 2. The midpoint minimizes the phase-averaged critical moment

For \(\gamma>0\), define the fixed-lattice phase-averaged moment

\[
I^{\square}_{\theta,\gamma}
=\mathbb E_\alpha S_\theta(\mathbb Z^2,\alpha)^\gamma
=\gamma\int_0^\infty
[1-F^\square_\theta(\sigma^2)]\sigma^{\gamma-1}\,d\sigma.
\]

Subtracting (1),

\[
F^\square_{1/2}(\sigma^2)-F^\square_\theta(\sigma^2)
=(1-2t)
\begin{cases}
\sigma^3,&\sigma\leq1/2,\\
\sigma(1-\sigma)^2,&1/2\leq\sigma\leq1,\\
0,&\sigma\geq1.
\end{cases}
\]

Both nonzero pieces are positive when \(\theta\ne1/2\). Exact integration
therefore gives

\[
\boxed{I^{\square}_{\theta,\gamma}-I^{\square}_{1/2,\gamma}
=\frac{(1-2t)\gamma}{(\gamma+1)(\gamma+2)}
\left[\frac2{\gamma+3}-2^{-\gamma-1}\right]>0.}
\tag{2}
\]

For the C84/C85 high-precision exponent \(\gamma=1/10\), and the
quarter point,

\[
\boxed{I^{\square}_{1/4,1/10}-I^{\square}_{1/2,1/10}
=\frac{100}{7161}-\frac5{462}\,2^{-1/10}
>0.0038667704448956047.}
\tag{3}
\]

The strict decimal in (3) is checked by rational tenth-power bounds in
`square_lattice_certificate.json`. The identity is exact and independent
of the exploratory sampling file. In particular, the midpoint is a
strict **minimum**, rather than a maximum, of the fully phase-averaged
critical moment on this fixed lattice. Endpoint symmetrization leaves
\(\mathbb Z^2\) unchanged, so it cannot repair the failed concavity route.

Equation (1) also gives
\(F^\square_{1/4}/F^\square_{1/2}=1/2\) for \(0<\sigma\leq1/2\).
Thus a proposed ratio bound
\(F^\square_{1/4}\geq(\sqrt3/2)F^\square_{1/2}\) cannot be proved
lattice by lattice. The analogous inequality for the full Haar average
is a separate unresolved proposition.

## 3. This sign persists on a positive-measure set of lattice shapes

The fixed-lattice moment difference is continuous at \(\mathbb Z^2\).
For completeness, let a basis matrix \(B\) range over a compact
neighborhood of the identity with its least singular value bounded below.
Then the sup-norm of every nonzero vector \(Bn\) has a uniform positive
lower bound, so every critical scale has a common finite upper bound.

For each interior phase triple, at least one primitive vector has a
positive admissible scale. In a sufficiently small basis neighborhood
that same vector gives a positive lower bound. Any vector that improves
this lower bound must have bounded endpoint norm, hence comes from a
finite set of integer vectors. Each candidate's admissible scale is
continuous: a mark tending to zero eventually ceases to constrain the
minimum, while the nonzero endpoint marks bound that minimum. The maximum
over this finite set is continuous. Dominated convergence now proves
continuity after phase averaging.

The strictly positive value (3) therefore persists on an open lattice
neighborhood of positive Haar measure. Together with the independently
proved negative cusp contribution, this demonstrates that the global
comparison must balance different lattice shapes. A sign theorem for
each phase-averaged lattice would be false.

## Verification

`verify_square_lattice.py` integrates the source endpoint cells exactly
at rational scales and positions, using all endpoint-eligible integer
pairs and the exact middle-interval union. It checks (1) in 48 finite
settings, including scales admitting vectors beyond the elementary axes.
It separately checks the rational coefficients in (3) and certifies its
strict positive value. These finite checks support the implementation;
the all-scale and all-position proof is the case analysis above.
