# P022 — The 40-Dimensional Franel Core Has Cyclic Cokernel of Order 26622

Status: `ACTIVE RESEARCH NOTE / EXACT INTEGER CERTIFICATE / SMITH STRUCTURE`  
Owner: `program/p022-geometry-v2`  
Depends on: 40-dimensional defect-core compression through segment length 150  
Cross-route relevance: P011 low-order collision identifiability; exact finite certificate compression

## 1. The modular certificate can be replaced by an exact integer

The current bounded low-order theorem originally stored the nonzero determinant residue

\[
973381\pmod{1000003}
\]

for a `151 x 151` joint valuation matrix.

Structural reduction has since shown that this certificate consists of:

1. a deterministic central-binomial prime block;
2. a pure `89 x 89` Franel-defect block;
3. 49 unimodular singleton defect pivots;
4. one residual `40 x 40` integer core.

The remaining core is small enough to evaluate with fraction-free integer elimination.

The result is unexpectedly simple:

\[
\boxed{
\det M_{40}=-26622.}
\]

Therefore the bounded theorem no longer needs an auxiliary modulus to establish nonzero determinant.

---

## 2. P022-SM01 — exact determinant

Bareiss fraction-free elimination on the exact integer core gives

\[
\boxed{
\det M_{40}
=-26622
=-2\cdot3^3\cdot17\cdot29.}
\]

No floating arithmetic or modular rank test is used.

The old residue is recovered simply by reduction:

\[
-26622
\equiv
973381
\pmod{1000003}.
\]

Thus the historical modular certificate was already seeing this small exact integer.

---

## 3. Two coprime codimension-one minors

To understand the integer structure more sharply, consider the `39 x 39` minors obtained from the core by deleting:

- row index `3` and column index `24`;
- row index `35` and column index `10`.

Their exact determinants are

\[
\boxed{-6}
\]

and

\[
\boxed{-797}. 
\]

Since

\[
\gcd(6,797)=1,
\]

the gcd of **all** `39 x 39` minors must be one.

In Smith-normal-form language, the 39th determinantal divisor is therefore

\[
\boxed{\Delta_{39}=1.}
\]

---

## 4. P022-SM02 — exact Smith invariant factors

Let

\[
d_1\mid d_2\mid\cdots\mid d_{40}
\]

be the Smith invariant factors of the core.

Standard Smith theory gives

\[
\Delta_{39}=d_1d_2\cdots d_{39}
\]

and

\[
|\det M_{40}|=d_1d_2\cdots d_{40}.
\]

Because

\[
\Delta_{39}=1,
\]

all first 39 positive invariant factors must equal one.

The final invariant is therefore

\[
26622.
\]

Hence

\[
\boxed{
\operatorname{SNF}(M_{40})
=\operatorname{diag}(
\underbrace{1,\ldots,1}_{39},26622
).}
\]

Equivalently,

\[
\boxed{
\mathbb Z^{40}/M_{40}\mathbb Z^{40}
\cong
\mathbb Z/26622\mathbb Z.}
\]

So the entire entangled finite certificate has a **cyclic cokernel**.

---

## 5. What happened to 151 dimensions?

The full compression chain can now be written more precisely:

\[
\boxed{
151
\longrightarrow
89
\longrightarrow
40
\longrightarrow
\mathbb Z/26622\mathbb Z.
}
\]

The arrows mean:

### `151 -> 89`

Eliminate 62 deterministic central-binomial prime directions.

### `89 -> 40`

Peel 49 exact `±1` Franel valuation pivots.

### `40 -> Z/26622Z`

Integer row/column operations reduce 39 further directions unimodularly; only one nontrivial Smith invariant remains.

This does **not** mean the infinite research problem is one-dimensional.  It means the current finite `N=150` certificate has only one residual integral index after all unimodular structure is removed.

---

## 6. P022-SM03 — only four exceptional prime characteristics

The prime factorization is

\[
26622=2\cdot3^3\cdot17\cdot29.
\]

Therefore reduction of the 40-dimensional core modulo a prime `p` is nonsingular for every

\[
p\notin\{2,3,17,29\}.
\]

The only exceptional prime characteristics are

\[
\boxed{2,3,17,29.}
\]

For each of these primes, the Smith form shows that the reduction loses exactly one rank:

\[
\operatorname{rank}_{\mathbb F_p}M_{40}=39.
\]

Thus the historical choice

\[
1000003
\]

was not arithmetically special; it was simply one convenient prime outside the four exceptional characteristics.

---

## 7. Why the Smith result matters for the research frontier

Before this reduction, the segment-150 theorem looked like evidence that 151 unrelated valuation directions happened to be linearly independent.

The current picture is much tighter:

- 62 directions are deterministic prime pivots;
- 49 more are exact singleton unit pivots;
- 39 of the remaining 40 integer directions are also unimodular after allowed integer row/column operations;
- the complete residual index is `26622`.

Therefore any structural explanation of the current bounded theorem only needs to account for why the last cyclic index is nonzero.

The factors

\[
2,3,17,29
\]

become natural diagnostic characteristics for the next phase: they are exactly the primes where the finite defect core acquires a one-dimensional modular relation.

This suggests a sharper experiment than extending `N`:

> track how the exceptional Smith invariant and its prime factors evolve as the segment frontier grows.

A stable pattern could reveal a genuine arithmetic mechanism; an exploding/unstructured sequence would be evidence against a simple global theorem.

---

## 8. Relation to exact low-order identifiability

Over `Q`, the determinant is nonzero, so the existing conclusion remains:

\[
(J_1,J_2,J_3)
\]

uniquely determines all segment multiplicities through length 150 plus the hidden tail.

The Smith form adds integral information that the rational rank statement did not contain.

It tells us how far the selected valuation lattice is from being unimodular and exactly which finite characteristics lose uniqueness at the linearized certificate level.

This is certificate structure, not a claim that checkpoint geometries actually alias modulo these primes as integer moment pairs.

---

## 9. Prior-art boundary

Bareiss elimination, determinantal divisors, Smith normal form and cokernel structure are standard integer linear algebra.

No novelty is claimed for those tools.

The P022-specific content is the exact Smith certificate of the structurally reduced Franel-defect matrix arising from Barlow low-order collision identifiability.

---

## 10. Executable certificate

Added:

- `src/enterprise_math/p022_barlow_defect_core_smith.py`;
- `tests/test_p022_barlow_defect_core_smith.py`.

The executable proof stores no Smith transformation matrices.  It recomputes:

1. the exact `40 x 40` determinant by Bareiss elimination;
2. the two coprime `39 x 39` witness minors `-6` and `-797`;
3. the forced Smith diagonal `(1^39,26622)`;
4. the exceptional prime set `{2,3,17,29}`;
5. the historical residue `973381` by reducing `-26622` modulo `1000003`.
