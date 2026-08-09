# P022 — Exact Minimax Scheduling for the Largest Checkpoint Fiber

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER OPTIMIZATION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: Barlow selected-layer fiber factorization; P011 collision spectrum  
Cross-route relevance: P023/P024 task-relative precision; finite observation design

## 1. A third checkpoint objective

For a final-observing checkpoint schedule with positive segment lengths

\[
\ell_1+\cdots+\ell_m=N,
\qquad \ell_j\ge1,
\]

two natural objectives were already solved:

- maximize the number of observable states;
- minimize pair collisions `J_2`.

Both select ordinary near-uniform segment lengths.

A different future language may care about **worst-case unresolved ambiguity**:

\[
\boxed{
M_{\max}(O)=\max_y|O^{-1}(y)|.
}
\]

This is also the largest collision order that can possibly remain nonzero: if every fiber has size at most `M`, then

\[
J_k=0\qquad(k>M).
\]

So minimizing `M_max` pushes the zero tail of the entire P011 collision spectrum as far down as possible.

The optimizer is not, in general, ordinary equal spacing.

## 2. Segment cost

A segment of length `ell` has binomial fiber sizes

\[
\binom{\ell}{0},\binom{\ell}{1},\ldots,\binom{\ell}{\ell}.
\]

Its largest fiber is

\[
\boxed{
C_\ell=\binom{\ell}{\lfloor\ell/2\rfloor}.
}
\]

Segment independence therefore gives

\[
\boxed{
M_{\max}=\prod_{j=1}^{m}C_{\ell_j}.
}
\]

We must minimize this product under a fixed sum and fixed number of segments.

## 3. P022-WF01 — exact marginal costs

Two elementary ratios control the problem.

### Odd to next even

For every `j>=0`,

\[
\frac{C_{2j+2}}{C_{2j+1}}=2.
\]

So adding one unit to an odd segment costs the same multiplicative factor `2`, independent of its size.

### Odd to next odd by a two-unit packet

For `j>=1`,

\[
\boxed{
\frac{C_{2j+1}}{C_{2j-1}}
=
\frac{2(2j+1)}{j+1}
=4-\frac{2}{j+1}.
}
\]

This pair-increment factor is strictly increasing in `j` and is always less than `4`.

Hence two separate one-unit odd-to-even increments cost `4`, while converting those same two units into one additional odd-to-odd pair increment costs strictly less than `4`.

## 4. P022-WF02 — a minimizer has at most one even segment

Start every segment at length one.  Any extra unit is either part of a two-unit packet or is an unpaired single.

Suppose two different segments are even.  Remove one unit from each.  Both become odd, dividing the objective by

\[
2\cdot2=4.
\]

Use the freed two units as one additional pair increment on one odd segment.  By WF01 this multiplies by strictly less than `4`.

The product therefore decreases.

Thus no minimizer can contain two even segments:

\[
\boxed{
\text{every minimax schedule has at most one even segment.}
}
\]

Equivalently, all but possibly one of the extra units can be grouped into two-unit packets.

## 5. P022-WF03 — pair packets are distributed as evenly as possible

Let

\[
E=N-m
\]

be the number of units beyond the all-one baseline, and write

\[
P=\left\lfloor\frac E2\right\rfloor.
\]

A segment receiving `p` pair packets has odd length

\[
1+2p.
\]

Its multiplicative cost is the product of the first `p` pair-increment factors

\[
\prod_{j=1}^{p}\left(4-\frac{2}{j+1}\right).
\]

Because these marginal factors are strictly increasing, if two segments have packet counts differing by at least two, moving the last packet from the more-loaded segment to the less-loaded one strictly decreases the product.

Therefore packet counts in a minimizer differ by at most one.

Write

\[
P=qm+r,
\qquad0\le r<m.
\]

Then exactly `m-r` segments receive `q` packets and `r` segments receive `q+1` packets, before handling a possible leftover single unit.

## 6. P022-WF04 — closed minimax value

Let

\[
e=E\bmod2\in\{0,1\}.
\]

Before the possible leftover single, the two odd segment lengths are

\[
2q+1
\]

and

\[
2q+3.
\]

If `e=1`, one arbitrary odd segment becomes the next even length, multiplying the objective by exactly `2`.  Which odd size receives this unit does not change the minimax value, so multiple segment multisets may tie.

The exact minimum is

\[
\boxed{
M_{\min}(N,m)
=
2^e
\binom{2q+1}{q}^{m-r}
\binom{2q+3}{q+1}^{r}.
}
\]

This is an entirely finite integer formula.

The corresponding segment family is **odd-balanced / pair-balanced**:

- distribute two-unit packets as evenly as possible;
- keep every segment odd;
- if one unit remains, place it on exactly one segment.

## 7. Contrast with ordinary balanced spacing

Ordinary length balancing and pair balancing agree asymptotically often, but they differ at important finite scales.

The smallest example is

\[
N=4,\qquad m=2.
\]

Ordinary balancing chooses

\[
(2,2),
\]

with

\[
M_{\max}=2\cdot2=4.
\]

Pair balancing chooses

\[
(1,3),
\]

with

\[
M_{\max}=1\cdot3=3.
\]

This is exactly the same pair-vs-four-way collision tradeoff from the higher-collision note:

- `(2,2)` has smaller `J_2`;
- `(1,3)` has no `J_4` at all.

So the disagreement between precision objectives has a direct minimax explanation.

## 8. Infinite near-dense specialization

For every

\[
m\ge2,
\qquad N=m+2,
\]

there are exactly two extra units beyond the all-one baseline.

Pair balancing places both on one segment:

\[
\boxed{(3,1,\ldots,1)}
\]

up to order, giving

\[
M_{\min}=3.
\]

Ordinary balancing places them on two segments:

\[
(2,2,1,\ldots,1),
\]

with maximum fiber `4`.

Thus the pair-vs-four-way conflict persists for every checkpoint count in this family.

## 9. Collision-cutoff interpretation

For any observation quotient, define

\[
K_0=1+M_{\max}.
\]

Then

\[
\boxed{
J_k=0\quad\text{for every }k\ge K_0.
}
\]

No smaller universal cutoff follows from the maximum fiber alone, because a fiber of size `M_max` contributes to `J_{M_max}`.

Therefore the pair-balanced schedule solves a distinct exact problem:

\[
\boxed{
\text{minimize the highest possible nonzero collision order.}
}
\]

This objective is neither image capacity nor pair ambiguity.

## 10. Precision consequence

We now have three checkpoint objectives with two different exact optimizers:

| Future statistic | Exact optimizer |
|---|---|
| observable image size | ordinary balanced lengths |
| pair collision `J_2` | ordinary balanced lengths |
| maximum fiber / collision cutoff | odd-balanced pair packets |

So even after the number of checkpoints is fixed, **precision is not checkpoint density**.  The correct placement depends on which unresolved distinctions the future language penalizes.

This supplies another concrete P022 specialization of the P023/P024 principle:

\[
\boxed{
\text{same state budget} + \text{different future statistic}
\Longrightarrow
\text{different optimal quotient geometry}.
}
\]

## 11. Verification

Added:

- `src/enterprise_math/p022_barlow_worst_fiber_scheduling.py`;
- `tests/test_p022_barlow_worst_fiber_scheduling.py`.

An independent exhaustive in-session search over all positive compositions with `N<=17` and `m<=7` found no mismatch with the closed minimax value.  The repository tests additionally enumerate all compositions in a smaller regression range.  These checks support the proof but do not replace canonical CI/formalization.
