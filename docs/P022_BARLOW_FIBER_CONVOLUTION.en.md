# P022 — Multiplicative Convolution Algebra of Checkpoint Fibers

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE RE-ENCODING / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: P011 complete fiber/collision spectrum; Barlow selected-layer fiber factorization  
Prior-art boundary: multiplicative/Dirichlet convolution and power-sum moments are established mathematics

## 1. Why keep the complete fiber profile

The higher-collision note expresses ordered equal-observation tuple counts through generalized binomial power sums and then recovers P011 collision counts by a Stirling transform.

Those moments are themselves shadows of a simpler complete finite object.

For any observation quotient `O`, let

\[
c_s(O)
=
\#\{y:|O^{-1}(y)|=s\}.
\]

The finite function

\[
\boxed{C_O=(c_1,c_2,\ldots)}
\]

is the complete fiber-size distribution.

P011 already proves that the full collision spectrum and this fiber profile determine each other.  The present Barlow specialization asks how `C_O` composes when the observation is built from independent checkpoint segments.

## 2. Segment fiber profile

A length-`ell` prefix-imbalance segment has fibers

\[
\binom{\ell}{0},
\binom{\ell}{1},
\ldots,
\binom{\ell}{\ell}.
\]

Define

\[
\boxed{
B_\ell(s)
=
\#\left\{j\in\{0,\ldots,\ell\}:\binom{\ell}{j}=s\right\}.
}
\]

Examples are

\[
B_1:\{1:2\},
\]

\[
B_2:\{1:2,\ 2:1\},
\]

\[
B_3:\{1:2,\ 3:2\},
\]

and

\[
B_4:\{1:2,\ 4:2,\ 6:1\}.
\]

This profile forgets which imbalance value owns which fiber but preserves the complete multiset of fiber sizes.

## 3. P022-FC01 — independent segments compose by multiplicative convolution

For finite functions on positive integers define

\[
\boxed{
(f\star_\times g)(n)
=
\sum_{ab=n}f(a)g(b).
}
\]

This is the ordinary finite multiplicative/Dirichlet convolution restricted to finite support.

If two independent observation segments have fiber sizes `a` and `b`, then their product observation has fiber size `ab`.  The number of such product fibers is the product of the two multiplicities.

Therefore for final-observing segment lengths

\[
\ell_1,\ldots,\ell_m,
\]

the complete checkpoint fiber profile is

\[
\boxed{
C_O
=
B_{\ell_1}
\star_\times
B_{\ell_2}
\star_\times\cdots\star_\times
B_{\ell_m}.
}
\]

If an unobserved tail of length `u` remains, every fiber size is additionally multiplied by

\[
2^u.
\]

So the tail acts by a deterministic scaling of the support axis, not by another constrained segment convolution.

## 4. P022-FC02 — power moments are characters of the convolution

For integer `r>=1`, define

\[
\Phi_r(f)
=
\sum_s f(s)s^r.
\]

Then

\[
\begin{aligned}
\Phi_r(f\star_\times g)
&=
\sum_n\sum_{ab=n}f(a)g(b)n^r\\
&=
\sum_{a,b}f(a)g(b)a^rb^r\\
&=
\Phi_r(f)\Phi_r(g).
\end{aligned}
\]

Hence

\[
\boxed{
\Phi_r(f\star_\times g)
=
\Phi_r(f)\Phi_r(g).
}
\]

So the ordered equal-observation tuple moment

\[
M_r=\sum_y|O^{-1}(y)|^r
\]

is a multiplicative character of the complete fiber-profile convolution algebra.

For one segment,

\[
\Phi_r(B_\ell)
=
\sum_{j=0}^{\ell}\binom{\ell}{j}^r
=F_r(\ell),
\]

which immediately recovers the higher-collision factorization

\[
M_r
=2^{ru}\prod_jF_r(\ell_j).
\]

Thus HC01 is not an isolated identity. It is the character evaluation of FC01.

## 5. P022-FC03 — P011 collision counts are a second shadow

From the full profile,

\[
\boxed{
J_k
=
\sum_s c_s\binom{s}{k}.
}
\]

Conversely P011 binomial inversion reconstructs the complete `c_s` from the full `J_k` hierarchy.

Therefore on this finite checkpoint system,

\[
\boxed{
\text{fiber profile}
\longleftrightarrow
\text{full P011 collision spectrum}.
}
\]

The power moments `M_r` provide another complete finite re-encoding when sufficiently many orders are retained, via the finite Stirling transforms.

The hierarchy is therefore

\[
\boxed{
B_{\ell_j}
\xrightarrow{\star_\times}
C_O
\xrightarrow{\Phi_r}
M_r
\xrightarrow{\text{Stirling}}
J_k.
}
\]

Each arrow has a clear information role; the first builds the exact quotient fiber state, later arrows choose summary languages.

## 6. Segment order is invisible

Multiplicative convolution is commutative and associative. Hence

\[
C_O
\]

depends only on the multiset of checkpoint segment lengths, not their order.

This matches the direct Barlow observation semantics: selected prefix imbalances at named checkpoint layers determine segment boundaries, but once only the **fiber-size distribution** is retained, relabelling the segment order does not change the multiset of product fiber sizes.

So the complete P011 spectrum still does not recover checkpoint order.

## 7. Open identifiability problem

A sharper question remains:

> does the complete fiber-size profile determine the **multiset** of positive segment lengths?

No proof is currently claimed.

An independent exhaustive search over all positive compositions with

\[
N\le20,
\qquad m\le7
\]

examined 137,979 ordered schedules.  After quotienting segment order, no two distinct segment-length multisets produced the same complete fiber profile in that bounded search.

This is evidence only:

\[
\boxed{
\text{segment-multiset identifiability is CONJECTURAL.}
}
\]

A proof would likely require factorization properties of the finite binomial-row profiles `B_ell` under multiplicative convolution.  A counterexample would be equally valuable because it would exhibit two genuinely different checkpoint geometries with exactly the same complete P011 fiber statistics.

## 8. Prior-art discipline

The algebraic operation used here is finite Dirichlet/multiplicative convolution, which is classical.  Power-sum characters and binomial rows are also classical.

Enterprise Math does not claim invention of these ingredients.

The project-specific role is the exact identification of the Barlow checkpoint quotient's fiber state with this convolution and its placement inside the finite-precision chain

\[
\text{checkpoint geometry}
\to
\text{fiber profile}
\to
\text{future collision language}.
\]

Historical novelty of that packaging remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/p022_barlow_fiber_convolution.py`;
- `tests/test_p022_barlow_fiber_convolution.py`.

The tests compare the convolution profile with direct microscopic word enumeration, verify moment-character multiplicativity, recover the higher-collision moment and `J_k` values, and preserve only a bounded regression—not a theorem—for segment-multiset identifiability.
