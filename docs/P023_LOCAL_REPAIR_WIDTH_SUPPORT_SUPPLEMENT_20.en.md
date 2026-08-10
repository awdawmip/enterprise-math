# P023 — Local Repair Width versus Global Repair Support, Supplement 20

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023 with a P011 repair-spectrum bridge  
Depends on: P023-S9/S11 and finite partition refinement  
Discipline: finite partition counts and binomial spectra are elementary mathematics. The project role is to separate local alphabet width from global refinement mass.

## 1. One repair alphabet size does not measure the whole refinement

Let `F subseteq E` be a finite precision refinement. For each coarse block

\[
B\in X/E,
\]

write

\[
\boxed{
s_B
=
\#\{C\in X/F:C\subseteq B\}.
}
\]

P023-S9 identifies

\[
\boxed{
R_{\max}(E\to F)=\max_B s_B
}
\]

as the exact minimum alphabet size of one globally reusable repair coordinate.

That is a **local width**: it tells how many fine classes can coexist inside the worst single coarse block.

It does not say how many coarse blocks need nontrivial repair.

## 2. Active repair support

Define

\[
\boxed{
A(E\to F)
=
\#\{B\in X/E:s_B>1\}.
}
\]

This counts coarse fibers that are genuinely split by the richer precision.

Also define the class gain

\[
\boxed{
G(E\to F)
=|X/F|-|X/E|
=
\sum_B(s_B-1).
}
\]

The local width and active support are independent complexity axes.

## 3. P023-S20-T01 — Support bounds class gain

Status: `PROVED`.

Let

\[
r=R_{\max}(E\to F).
\]

Every active coarse block contributes at least one and at most `r-1` new fine classes. Therefore

\[
\boxed{
A(E\to F)
\le
G(E\to F)
\le
(r-1)A(E\to F).
}
\]

Thus a bounded local repair alphabet does not bound total class gain unless active support is also bounded.

## 4. P023-S20-T02 — Support bounds the second repair-spectrum coordinate

Status: `PROVED`.

S11 gives

\[
\mathcal R_2(E\leftarrow F)
=
\sum_B\binom{s_B}{2}.
\]

For every active block,

\[
1\le\binom{s_B}{2}\le\binom r2.
\]

Hence

\[
\boxed{
A(E\to F)
\le
\mathcal R_2(E\leftarrow F)
\le
\binom r2 A(E\to F).
}
\]

Again the spectrum mass can grow without bound while local width `r` remains fixed.

## 5. P023-S20-T03 — Binary refinements collapse all three global burdens to one integer

Status: `PROVED`.

Assume

\[
s_B\in\{1,2\}
\]

for every coarse block. Equivalently,

\[
R_{\max}(E\to F)\le2.
\]

Then every active block contributes exactly:

- one extra fine class;
- one unordered pair of fine classes;
- one active repair site.

Therefore

\[
\boxed{
A(E\to F)
=
G(E\to F)
=
\mathcal R_2(E\leftarrow F).
}
\]

All higher repair-spectrum coordinates vanish:

\[
\boxed{
\mathcal R_j=0
\qquad(j\ge3).
}
\]

The entire global refinement burden is therefore encoded by one integer: the number of split coarse fibers.

## 6. P023-S20-T04 — Fixed local width does not imply bounded global complexity

Status: `PROVED BY EXPLICIT FAMILY`.

For every positive integer `N`, take `N` disjoint coarse blocks and split every block into exactly two fine blocks.

Then

\[
R_{\max}=2
\]

for every member of the family, while

\[
\boxed{
A=G=\mathcal R_2=N.
}
\]

As `N` grows, local alphabet width remains binary but global repair support and spectrum mass grow arbitrarily large.

Hence

\[
\boxed{
\text{bounded local repair alphabet}
\not\Rightarrow
\text{bounded global refinement burden}.
}
\]

This is a structural no-go theorem, independent of P017.

## 7. Relation to P011

For the canonical quotient projection

\[
\pi:X/F\to X/E,
\]

P011's collision spectrum is exactly the S11 repair spectrum of the refinement.

S20 now adds the missing local/global reading:

- `max |pi^{-1}(B)|` = worst local repair alphabet;
- `# {B: |pi^{-1}(B)|>1}` = active repair support;
- `J_2(pi)` = pairwise global ambiguity mass;
- in the binary case, active support and `J_2` are identical.

Thus one P011 spectrum coordinate can measure **how many local defects are active**, not how wide any one defect is.

## 8. Number-theory specialization: P017

For the P017 refinement from least-prime shell precision `P` to joint `(P,R)` factor/root precision, L064 proves

\[
R_{\max}(P\to P\cap R)\le2.
\]

L067 defines

\[
S(k)=\#\{\text{least-prime shells realizing both cofactor-root branches}\}.
\]

Therefore S20-T03 gives

\[
\boxed{
S(k)
=
A(P\to P\cap R)
=
G(P\to P\cap R)
=
\mathcal R_2(P\leftarrow P\cap R).
}
\]

L075 further proves

\[
S(k)\to\infty
\quad\text{in natural density}.
\]

So P017 gives a genuine arithmetic realization of T04 where local width is permanently two while the active global support diverges on a density-one set.

## 9. Representation consequence

A single scalar “precision cost” cannot distinguish these two situations:

1. one coarse fiber splits into two classes;
2. one million independent coarse fibers each split into two classes.

Both have the same local minimum repair alphabet `2`, but radically different global state support.

Therefore a complete finite precision report should keep at least:

\[
\boxed{
(R_{\max},A)
}
\]

or, when needed, the full repair spectrum.

Local width answers **how many symbols must one active site distinguish?**

Active support answers **how many coarse sites actually require refinement?**

## 10. Relation to sparse state design

When `r` is small but `A` is large, the natural structure is not one ever-widening global digit.

It is a sparse family of bounded local repair coordinates.

This is exactly the structure seen in P017:

\[
\boxed{
\text{many locally binary defects}
\neq
\text{one large repair alphabet}.
}
\]

This distinction should be preserved before any storage or proof-state packing step.

## 11. Executable specification

- `src/enterprise_math/precision_repair_support.py`
- `tests/test_precision_repair_support.py`

Tests verify the exact binary identity, the general width/support bounds, and a family with permanently binary local repair but arbitrarily large global active support.

## 12. Foundation feedback

S20 supplies another reason that precision is not adequately represented by one scalar.

At minimum, finite precision has separate notions of:

- local repair width;
- active repair support;
- higher-order repair spectrum;
- semantic final class depth.

Different applications may compress these quantities, but no universal theorem identifies them.
