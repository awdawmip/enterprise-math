# Precision Calculus — Supplement 23

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact one-threshold response inside the T182 two-basin image and shared-offset coherence across quotient divisors  
Depends on: P018-T182/T195/T196, T007 integer roots, P007 discrete division  
Discipline: threshold comparisons and floor-division order laws are elementary established arithmetic. The project-specific content is the exact square-basin response law and its use as a common-offset coherence layer for later cross-scale arguments.

> **Concurrent-numbering resolution.** This note entered `main` from the concurrent QuotientBasin route under provisional labels `Supplement 14 / T113`. PR #68 already had an earlier validated T113. The integrated branch preserves that earlier numbering and relabels only this later concurrent theorem as **Supplement 23 / T197**. References to provisional T110/T111/T112 are correspondingly mapped to T182/T195/T196.

## 1. The missing information in a two-basin statement

T182 proves that for

\[
k^2\le n<(k+1)^2,
\qquad d\ge2,
\]

and

\[
j_d=R_2\!\left(\left\lfloor\frac{k^2}{d}\right\rfloor\right),
\]

the quotient root can only be

\[
j_d\quad\text{or}\quad j_d+1.
\]

That is already a strong finite image theorem, but it does not yet say **where** the switch between the two values occurs.

The switch is exact and occurs once.

---

## 2. P018-T197 — Exact quotient-root switch threshold

Status: `PROVED` and Lean-formalized.

Under the T182 hypotheses,

\[
\boxed{
R_2\!\left(\left\lfloor\frac nd\right\rfloor\right)=j_d+1
\iff
d(j_d+1)^2\le n.
}
\]

Equivalently, the lower branch holds exactly before that state threshold.

### Proof

T182 already restricts the quotient root to `j_d` or `j_d+1`.

The upper value occurs if and only if

\[
(j_d+1)^2
\le
\left\lfloor\frac nd\right\rfloor.
\]

By the exact order adjunction for natural-number floor division, this is equivalent to

\[
d(j_d+1)^2\le n.
\]

No approximation is used. ∎

The Lean theorem is

`EnterpriseMath.Precision.square_basin_div_upper_root_iff`.

---

## 3. Offset form

Write a basin state as

\[
n=k^2+s,
\qquad 0\le s\le2k.
\]

Define the positive offset threshold

\[
\boxed{
\tau_d
=d(j_d+1)^2-k^2.
}
\]

Positivity follows from the defining upper inequality for `j_d`:

\[
\left\lfloor\frac{k^2}{d}\right\rfloor<(j_d+1)^2.
\]

T197 becomes

\[
\boxed{
R_2\!\left(\left\lfloor\frac{k^2+s}{d}\right\rfloor\right)
=j_d+\mathbf1[s\ge\tau_d].
}
\]

If `tau_d>2k`, the upper branch is never reached anywhere in the basin.

Thus the quotient-root response is a literal one-switch step function in the finite basin offset.

---

## 4. Shared-offset coherence for many divisors

Fix divisors

\[
d_1,\ldots,d_h\ge2.
\]

For each `d_i`, define its T197 upper-branch bit

\[
\varepsilon_i(s)
=
\mathbf1[s\ge\tau_{d_i}].
\]

All coordinates are driven by the **same** offset `s`.

Therefore the vector

\[
\boxed{
\varepsilon(s)
=(\varepsilon_1(s),\ldots,\varepsilon_h(s))
}
\]

is not an arbitrary element of `{0,1}^h`.

As `s` increases through the finite basin, a coordinate can change only when `s` crosses its own threshold. After sorting the distinct thresholds, the vector is constant between successive threshold values. Hence

\[
\boxed{
\#\{\varepsilon(s):0\le s\le2k\}
\le h+1.
}
\]

The naive independent-bit count would be `2^h`.

This is stronger than T195 in a different direction:

- T195 says a **final quotient state** is independent of factorization of the total divisor;
- T197 says even a family of quotient-root branch bits for different divisors is constrained by one shared state coordinate.

The Python reference tests this finite pattern bound directly.

---

## 5. Divisibility and the large-modulus phase transition

If in addition a divisor `D` actually divides the basin state

\[
n=k^2+s,
\]

then

\[
\boxed{s\equiv-k^2\pmod D.}
\]

When

\[
D>2k,
\]

the allowed offset interval has length `2k+1`, so there is at most one admissible positive interior offset satisfying the congruence.

This is the lower-square-boundary coordinate form of the same unique-large-modulus phenomenon already used in P017. T197 therefore does not create a competing large-hit mechanism; it supplies the root-response coordinate that lives on top of the same finite state.

---

## 6. Mirror coordinates

For the centered square-basin mirror decomposition,

\[
M=k(k+1),
\qquad
M-r,\ M+r,
\qquad 1\le r<k,
\]

the offsets above `k^2` are

\[
\boxed{s_-=k-r,\qquad s_+=k+r.}
\]

If a divisor `p` acts on the lower mirror state, its T197 upper-root bit is

\[
\boxed{
\varepsilon_p^-(r)
=\mathbf1[k-r\ge\tau_p]
=\mathbf1[r\le k-\tau_p].
}
\]

For a divisor `q` on the upper state,

\[
\boxed{
\varepsilon_q^+(r)
=\mathbf1[k+r\ge\tau_q]
=\mathbf1[r\ge\tau_q-k].
}
\]

Thus quotient-root branch selection becomes a **bounded radius half-interval condition** that can be intersected with the existing mirror CRT progressions.

This is the intended interface with the P017 mirror-certificate route: least-factor/second-factor constraints can now use both

1. a CRT residue class for the radius, and
2. an exact quotient-root threshold interval.

Neither condition is probabilistic.

---

## 7. P017 lower-band interpretation

Suppose

\[
n=pq
\]

is a square-basin composite with least prime `p`.

T182/T195/T196 say the cofactor root descends and quotient factorization does not branch exponentially. T197 adds the exact branch selector:

\[
R_2(q)
=j_p+\mathbf1[n\ge p(j_p+1)^2].
\]

If `q` is composite, its next least prime is bounded by this exact descended root.

Hence the next-factor cutoff is not merely `j_p+1`; it can be chosen statewise as either `j_p` or `j_p+1` from one integer threshold comparison.

This is potentially useful for least-factor-gated mirror capacities, where the radius already determines the basin offset exactly.

---

## 8. Executable validation

The Python layer extends `src/enterprise_math/quotient_basin.py` with:

- `quotient_root_threshold`;
- `square_basin_offset_root_response`;
- `quotient_root_threshold_pattern`.

The tests check that:

- the threshold is always above the lower square boundary;
- the root response equals `base_root + 1[offset>=tau]` over bounded complete basins;
- some thresholds occur inside the basin and some lie beyond it;
- for fixed families of `h` divisors, the observed bit-vector family has size at most `h+1`.

The Lean layer formalizes the exact upper-branch equivalence; the finite-vector pattern statement is an elementary corollary of threshold ordering and is kept at the documentation/reference-test level unless a later proof needs a typed finite-set theorem.

---

## 9. Next target

T182/T195/T196/T197 now settle the operation-level geometry of quotient transport strongly enough for the current lower-band route:

- strict descent;
- no factorization-path explosion;
- exact one-threshold branch response;
- shared-offset coherence.

The next useful theorem should therefore be **cross-shell**, not another quotient identity.

The leading P017 candidate is the lower-band root-target overlap bound: among least primes `p` with `p^2<2k`, every descended root index appears in the T182 candidate pair of at most two distinct least-prime shells.

If proved, each lower square-root scale receives only constant-many shell channels, which is the right type of structural restriction for a recursive mass argument.
