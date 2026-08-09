# P025 Supplement 27 — Certificate Precision Dimension as Augmented Relation-Rank Gain

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 25–26; P023 exact certificate quotient semantics  
Hard block: `NONE`

## 1. Counting outputs is the wrong precision measure

Supplement 26 gives a relation-conditioned block-value state

\[
\Lambda_{L,A}
\]

of rational rank

\[
s-\operatorname{rank}L,
\]

where `s` is the number of active blocks.

Now add a finite family of exact block-linear certificates collected into a matrix

\[
H.
\]

The number of rows of `H` can be arbitrarily large. The actual new precision is the number of relation-state directions that those rows separate.

## 2. P025-T78 — exact certificate rank-gain formula

Let

\[
K=\ker_{\mathbb Q}L
\subseteq\mathbb Q^s.
\]

The certificate family restricts to

\[
H|_K:K\to\mathbb Q^q.
\]

Then

\[
\boxed{
\operatorname{rank}(H|_K)
=
\operatorname{rank}
\begin{pmatrix}L\\H\end{pmatrix}
-
\operatorname{rank}L.
}
\]

### Proof

The combined map

\[
x\mapsto(Lx,Hx)
\]

has kernel

\[
\ker L\cap\ker H.
\]

Therefore

\[
\operatorname{rank}[L;H]
=s-\dim(\ker L\cap\ker H).
\]

Meanwhile

\[
\operatorname{rank}L=s-\dim\ker L.
\]

Subtracting gives

\[
\dim\ker L-\dim(\ker L\cap\ker H),
\]

which is exactly the rank of `H` restricted to `ker L`. ∎

Define the **certificate rank gain**

\[
\boxed{
\Delta_H
=
\operatorname{rank}[L;H]-\operatorname{rank}L.
}
\]

## 3. P025-T79 — residual exact-certificate fiber rank

The exact certificate vector identifies two relation states when their difference lies in

\[
\ker L\cap\ker H.
\]

Hence the residual rational rank left invisible by the certificate family is

\[
\boxed{
\operatorname{rank}_{\rm residual}
=
(s-\operatorname{rank}L)-\Delta_H.
}
\]

Equivalently,

\[
\boxed{
\operatorname{rank}_{\rm residual}
=
s-\operatorname{rank}[L;H].
}
\]

So the certificate rank gain is an exact dimension-level measure of refinement over the already-declared relation state.

## 4. Two endpoint criteria

### Relation-redundant certificate family

\[
\boxed{
\Delta_H=0
}
\]

iff the certificates add no rational distinction on the relation kernel. In particular, certificate rows lying in the rational row span of `L` vanish identically on relation states.

### Block-value complete certificate family

\[
\boxed{
\Delta_H=s-\operatorname{rank}L
}
\]

iff the residual certificate fiber rank is zero. Then the full exact labelled certificate vector is injective on the rational relation state and therefore on the integer compressed lattice.

This generalizes Stage 25's rank-two completeness criterion.

## 5. ABC calibration

For a non-unit abc triple,

\[
L=(1,1,-1),
\qquad
s=3,
\qquad
\operatorname{rank}L=1.
\]

### One Wronskian

The block-value Wronskian row is

\[
H_W=(-b,a,0).
\]

It is independent of `L`, so

\[
\operatorname{rank}[L;H_W]=2
\]

and

\[
\boxed{\Delta_{H_W}=1.}
\]

Thus one Wronskian removes one of the two block-value directions and leaves a one-dimensional fiber. Stage 22's affine floor line is exactly this residual rank-one fiber at a fixed Wronskian value.

### Wronskian plus one independent certificate

For `2+3=5`, add certificate `t_a`, with row

\[
(1,0,0).
\]

Then

\[
\operatorname{rank}
\begin{pmatrix}
1&1&-1\\
-3&2&0\\
1&0&0
\end{pmatrix}
=3.
\]

Hence

\[
\boxed{\Delta_H=2}
\]

and the residual fiber rank is zero: the pair `(W,t_a)` recovers the complete block-value state.

### Many dependent Wronskians

Rows

\[
H_W,
\ 2H_W,
\ -7H_W
\]

still give

\[
\boxed{\Delta_H=1,}
\]

not three. Output count and precision-rank gain are different quantities.

## 6. Unit abc boundary

For `1+b=c`, after deleting the unit block there are two active variables and one relation row `(1,-1)`. Thus the compressed rank is one.

Any nonzero certificate direction on that line has rank gain one and is block-value complete.

This explains why the single common derivative/Wronskian value completely parameterizes the unit relation state.

## 7. Multiple-relation calibration

For blocks `(1,2,3,5)` with relations

\[
1+2=3,
\qquad
2+3=5,
\]

there are three active blocks and relation rank two, so only one derivative-value direction remains.

Any certificate row nonzero on that direction has

\[
\boxed{\Delta_H=1}
\]

and is complete, no matter how many other dependent outputs accompany it.

## 8. Architectural consequence

For exact block-linear certificate languages, the natural precision-dimension increment is

\[
\boxed{
\Delta_H
=
\operatorname{rank}[L;H]-\operatorname{rank}L,
}
\]

not:

- the number of certificate outputs;
- the ambient prime-coordinate dimension;
- the size of a chosen generator list;
- or a universal scalar precision level.

This gives a compact relation-relative accounting rule:

\[
\boxed{
\text{declared relations}
\to
\text{remaining relation kernel}
\to
\text{certificate rank gain}
\to
\text{residual hidden directions}.
}
\]

It is a dimension-level theorem only. Integer torsion, labelled image constraints, access costs, and threshold semantics may still distinguish systems with the same rank gain.

## 9. P023 ownership boundary

The exact certificate quotient itself is simply the image

\[
H(\Lambda_{L,A}),
\]

and its kernel relation is the coarsest exact equivalence for the full certificate vector. That factorization/minimal-repair principle is already P023/general quotient mathematics.

P025 therefore should relay the rank-gain formula as a reusable relation-specific coordinate, not claim a new generic quotient theorem.

## 10. Prior-art boundary

Rank-nullity, stacked-matrix rank identities, restricted linear-map rank, and quotient-kernel dimension are standard linear algebra.

P025 does not claim them. The project-side candidate is their exact use as a precision-dimension accounting layer after arithmetic block-value compression.

This result should be routed to A3/P023 for ownership audit before any broader promotion.

## 11. Executable assets

Added:

- `src/enterprise_math/relation_certificate_rank.py`
  - exact augmented rank gain;
  - residual certificate-kernel rank;
  - relation-redundant / block-complete flags;
  - abc Wronskian row helper.
- `tests/test_relation_certificate_rank.py`
  - one Wronskian gain one;
  - dependent certificate multiplicity;
  - Wronskian plus independent certificate completeness;
  - relation-row redundancy;
  - unit and multiple-relation boundaries.

## 12. Next frontier

No hard block exists. Continue with:

1. generalize Stage 26 beyond pairwise-coprime blocks, where shared primes couple block derivative values before relation constraints;
2. refine rank gain with integer image/torsion and labelled-image data when exact certificate values matter;
3. attach access-cost profiles to residual certificate fibers;
4. test whether relation-rank gain gives useful adaptive certificate-selection heuristics without confusing dimension with total proof cost;
5. relay the rank law/gain pair to A3/P023 as a candidate reusable research tool.
