# Gregory–Machin continuation: Gaussian direction-generator reduction and exact H=1,000,000 rational support-two Pareto frontier

Status: `FREE_RESEARCH / EXACT_GENERATOR_REDUCTION + EXECUTABLE_BOUNDED_PARETO / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-B2817C / FREE_AXIOM_DISCOVERY`
Issue: `#1160`
Checker: `research_notes/experiments/gregory_machin_rational_support2_direction_generator_h1m_20260904.py`
Depends on: exact Gaussian valuation endpoint theorem; generalized rational support-two H=1000 census; Pell complement theorem; rational-alphabet no-go and bit-resource bound.

## 1. Motivation

The complete rational support-two census at `H=1000` enumerated all primitive atoms

\[
V_{a,b}=[b+ai],\qquad 0<a<b\le H,\qquad \gcd(a,b)=1,
\]

which is intrinsically quadratic in `H`.  The next question is whether exact Gaussian arithmetic can generate only the direction classes that can actually participate in a rank-one endpoint circuit.

The answer is positive.  The key is that primitive rational atoms have an extremely rigid norm with respect to their normalized Gaussian free-valuation direction.

---

## 2. Primitive Gaussian direction norm theorem

Let

\[
\nu(z)=\bigl(v_{\pi_p}(z)-v_{\bar\pi_p}(z)\bigr)_{p\equiv1(4)}
\]

be the free Gaussian valuation vector of a primitive atom

\[
z=b+ai,\qquad 0<a<b,\qquad \gcd(a,b)=1.
\]

Write

\[
\nu(z)=m g,
\]

where `g` is a primitive integer vector, unique up to overall sign, and `m\ne0` is the signed direction multiplier.  Define

\[
\boxed{
M(g)=\prod_{p\equiv1(4)}p^{|g_p|}.
}
\]

### Theorem 2.1

For every primitive strict atom,

\[
\boxed{
a^2+b^2\in\{M(g)^{|m|},\;2M(g)^{|m|}\}.
}
\]

### Proof

Because `gcd(a,b)=1`, an odd rational prime cannot divide both Gaussian conjugate factors of `z`: if both `pi_p` and `bar pi_p` divided `z`, then their product `p` would divide both integer coordinates.  Hence, for every odd split prime `p`, all of `v_p(a^2+b^2)` occurs on exactly one Gaussian orientation and

\[
|\nu_p(z)|=v_p(a^2+b^2).
\]

The odd part of the norm is therefore

\[
\prod_p p^{|m g_p|}=M(g)^{|m|}.
\]

For a primitive integer pair, the factor at `2` is either absent or occurs exactly once: opposite-parity coordinates give an odd norm, while two odd coordinates give `v_2(a^2+b^2)=1`.  This proves the two displayed possibilities. ∎

This theorem is entirely integer/Gaussian arithmetic.  It does not use an angle or `pi`.

---

## 3. Direction-seed reduction theorem

Suppose two distinct atoms in the same normalized free direction form a candidate rank-one circuit and have signed multipliers `m_1,m_2` with

\[
|m_1|\ne |m_2|.
\]

If both denominators satisfy `b_j<=H`, let

\[
h=\max(|m_1|,|m_2|)\ge2.
\]

By Theorem 2.1,

\[
M(g)^h\le a_j^2+b_j^2<2H^2.
\]

Therefore

\[
\boxed{M(g)<\sqrt2\,H.}
\]

So **every unequal-multiplier support-two circuit under denominator height `H` comes from a primitive Gaussian free direction of norm below `sqrt(2) H`**.

This is the decisive reduction: the raw atom disk has order `H^2` lattice points, while the required direction-seed disk has norm radius only order `H`.

---

## 4. Exact generation of all atoms on one free direction

For a primitive direction `g`, choose the exact Gaussian generator

\[
\gamma_g
=\prod_{g_p>0}\pi_p^{g_p}
 \prod_{g_p<0}\bar\pi_p^{-g_p},
\qquad N(\gamma_g)=M(g).
\]

For every `h>=1`, take `gamma_g^h`, divide any positive integer gcd from its two coordinates, and fold by a Gaussian unit/conjugation to the unique strict first-octant primitive pair

\[
P_h=(b_h,a_h),\qquad 0<a_h<b_h.
\]

Its complementary pair is

\[
C(P_h)=(b_h+a_h,b_h-a_h).
\]

Unique Gaussian factorization shows:

- `P_h` and `C(P_h)` are exactly the two strict first-octant primitive atoms whose normalized free direction is `g` and whose multiplier magnitude is `h`;
- their signed multipliers are opposite;
- if `P_h` has torsion coordinate `eps_h`, then `C(P_h)` has torsion coordinate `1-eps_h mod 8`, because

\[
[P_h][C(P_h)]=\tau.
\]

Thus one Gaussian seed generates the entire rank-one rational-atom family by integer powering plus the already-proved complement map.

---

## 5. Why omitted equal-multiplier pairs cannot alter the Pareto frontier

The seed bound `M(g)<sqrt(2)H` was derived for unequal multiplier magnitudes.  If two distinct atoms have the same multiplier magnitude in one rank-one direction, the generation theorem forces them to be the complementary pair `P_h,C(P_h)`.

The earlier Pell half-turn theorem proved that every complementary pair has generalized two-factor Lehmer cost strictly above

\[
\mu_*
=\frac{2}{\log_{10}(1+\sqrt2)}
\approx5.224992277747915.
\]

But the exact support-two frontier already contains

\[
2\arctan(1/3)+\arctan(1/7)=\pi/4
\]

with denominator bit cost `5` and

\[
\mu\approx3.279197936744323.
\]

Therefore every complementary pair with denominator-bit cost at least `5` is dominated.  The minimum possible total denominator-bit cost is `4`, and the unique strict complementary pair at that cost is

\[
(1/2,1/3).
\]

Consequently:

\[
\boxed{
\text{direction seeds }M<\sqrt2H
+\text{ their powers/complements}
}
\]

plus the already generated bit-4 Euler pair is **complete for the entire `(mu, denominator-bits)` support-two Pareto frontier** under height `H`.

This is stronger than a heuristic acceleration: it is a completeness theorem for the declared Pareto problem.

---

## 6. Exact rank-one endpoint condition in generated coordinates

Within one direction, let two generated atoms have signed multipliers `m_1,m_2` and torsion coordinates `eps_1,eps_2`.  Put

\[
d=\gcd(|m_1|,|m_2|).
\]

The primitive free-coordinate kernel is

\[
(c_1^{(0)},c_2^{(0)})
=\left(\frac{m_2}{d},-\frac{m_1}{d}\right).
\]

Let

\[
e=c_1^{(0)}\varepsilon_1+c_2^{(0)}\varepsilon_2\pmod8.
\]

The pair hits the diagonal target iff `e` is odd.  As in the general valuation-circuit theorem, the least-absolute target scaling is the odd residue `e` modulo eight.

No floating angle recognition is used.

---

## 7. Regression: exact recovery of the H=1000 frontier

Applying the generator method at `H=1000` reproduces, without enumerating the full 304,191-atom box, the exact seven-point Pareto frontier previously obtained by exhaustive atom enumeration:

1. `(1/2,1/3)`;
2. `(1/3,1/7)`;
3. `(1/7,2/11)`;
4. `(1/7,3/79)`;
5. Machin `(1/5,1/239)`;
6. `(9/46,1/239)`;
7. `(3/79,29/278)`.

This is an executable completeness regression for the reduction theorem.

---

## 8. Complete H=1,000,000 direction-generated census

Set

\[
\boxed{H=1{,}000{,}000.}
\]

The exact generator checker reports:

- primitive free-direction seeds with `M<sqrt(2)H`: `224,883`;
- generated strict rational atoms within the height box: `757,785`;
- rank-one generated atom pairs checked: `977,206`;
- exact `C8` endpoint pairs in the generated sufficient universe: `612,512`.

The resulting complete two-resource Pareto frontier has exactly **nine** points:

| denominator bits | generalized `mu` | atoms `(a/b)` | coefficients |
|---:|---:|---|---|
| 4 | 5.417831369177 | `1/2`, `1/3` | `(1,1)` |
| 5 | 3.279197936744 | `1/3`, `1/7` | `(2,1)` |
| 7 | 2.533984012675 | `1/7`, `2/11` | `(3,2)` |
| 10 | 1.887269242675 | `1/7`, `3/79` | `(5,2)` |
| 11 | 1.851127652317 | `1/5`, `1/239` | `(4,-1)` |
| 14 | 1.831853174914 | `9/46`, `1/239` | `(3,4)` up to atom order |
| 16 | 1.722670919899 | `3/79`, `29/278` | `(7,5)` |
| 22 | 1.551482953201 | `3/79`, `1457/22049` | `(12,5)` |
| 27 | 1.348180573985 | `3/79`, `24478/873121` | `(17,5)` |

All reported points have exact finite tangent-sheet certificate

\[
\text{endpoint}=(1,1),\qquad\text{sheet}=0.
\]

The two new points beyond the `H=1000` frontier both lie on the same primitive Gaussian direction

\[
\boxed{p=5.}
\]

Their oriented valuation multipliers are respectively

\[
(-5,+12),
\qquad
(-5,+17),
\]

so the target coefficients are forced by the rank-one integer kernel.

---

## 9. New H=1,000,000 Lehmer leader

The final frontier point is

\[
V_1=[79+3i],
\qquad
V_2=[873121+24478i].
\]

Their exact free valuation coordinates are

\[
n_5(V_1)=-5,
\qquad
n_5(V_2)=17.
\]

Hence free cancellation forces coefficients proportional to `(17,5)`.  The `C8` pairing gives the diagonal target, so

\[
\boxed{
[79+3i]^{17}
[873121+24478i]^5
=\tau.
}
\]

The finite sheet certificate is principal.  Only after this integer certificate is fixed does analytic completion give

\[
\boxed{
\frac\pi4
=17\arctan\frac3{79}
+5\arctan\frac{24478}{873121}.
}
\]

Its generalized Lehmer coordinate is

\[
\boxed{
\mu\approx1.3481805739852035.
}
\]

This beats the `H=1000` rational support-two leader `1.72267...` and, as expected from the unrestricted rational-alphabet no-go, also falls below the integer-reciprocal Nimbran value.  It is **not** compared as a like-for-like integer-reciprocal record: its denominator-coordinate budget is explicitly larger.

---

## 10. Structural consequence

The search architecture has now changed from

\[
\text{enumerate all rational slopes}
\]

to

\[
\boxed{
\text{primitive Gaussian free direction}
\to
\text{power orbit}
\to
\text{complement branch}
\to
\text{rank-one }C_8\text{ target}
\to
\text{resource Pareto}.
}
\]

The dimension reduction is mathematically certified rather than merely empirical.

The next unresolved layer is generalized support three.  There the free valuation columns must lie in a rank-two rational plane, so the correct analogue of the present direction generator is a **Gaussian valuation-plane generator / exterior-product hash**, not a cubic scan of rational atoms.

No claim of historical novelty is made for any analytic identity appearing after completion.  The result claimed here is the exact generator reduction and the bounded `H=1,000,000` Pareto classification under the declared rational-atom resources.
