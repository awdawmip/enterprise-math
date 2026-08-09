# A3 ↔ A4 ↔ P021 ↔ A2/P023 Bridge — Supplement 12

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact witness-label erasure criterion for a whole finite count-composition algebra

## 1. From one-step defect to recursively stable identity erasure

Supplement 11 gave the exact coupling defect for one declared scalar/matrix composition count. A zero defect may occur accidentally even when the hidden witness profiles are non-uniform.

That is enough for the **current** count observable, but it does not guarantee future completeness under arbitrary later count compositions.

For a whole operation language we need a stronger, recursively stable condition.

The relevant established structure is an equitable partition / exact lumping of non-negative-integer transition matrices.

## 2. Setup

Let `X` be a finite exact witness set and let

\[
\mathcal P=\{C_1,\ldots,C_q\}
\]

be a partition whose cells are the witness identities we propose to collapse.

Let

\[
M:X\times X\to\mathbb N
\]

be a non-negative-integer transition/count matrix.

For `x in C_a`, define the block-output count to target cell `C_b`:

\[
S_M(x,b)=\sum_{y\in C_b}M_{xy}.
\]

## 3. B47 — one-step count descent iff equitability

The following are equivalent.

### (A) Block-count observable descends through the witness partition

For any `x,x'` in the same source cell `C_a`,

\[
S_M(x,b)=S_M(x',b)
\]

for every target cell `C_b`.

### (B) `P` is equitable for `M`

Every row inside one source cell has the same vector of target-cell sums.

When these conditions hold, define the exact quotient count matrix

\[
\boxed{
Q_M(a,b)=S_M(x,b)
\quad(x\in C_a),
}
\]

which is independent of the representative.

This is exactly P023 fiber-constancy/descent specialized to integer block-count observations.

## 4. B48 — equitable matrices are closed under composition

Suppose `M` and `N` are both equitable for the same partition `P`. Then `MN` is equitable and

\[
\boxed{
Q_{MN}=Q_MQ_N
}
\]

over the non-negative integers.

### Proof

Take `x in C_a`. For target cell `C_c`,

\[
\sum_{z\in C_c}(MN)_{xz}
=
\sum_y M_{xy}\sum_{z\in C_c}N_{yz}.
\]

Split the middle witnesses by cells `C_b`. Since `N` is equitable, the inner target-block sum is the constant `Q_N(b,c)` for every `y in C_b`. Therefore

\[
=
\sum_b Q_N(b,c)
\sum_{y\in C_b}M_{xy}
=
\sum_b Q_M(a,b)Q_N(b,c).
\]

The result is independent of the chosen `x in C_a`, proving both equitability of `MN` and the quotient-product identity.

## 5. B49 — finite operation-family theorem

Let

\[
\mathcal M=\{M_\alpha\}_{\alpha\in A}
\]

be a finite family of non-negative-integer transition/count matrices on the same exact witness set.

If every generator is equitable for `P`, then for every operation word

\[
w=\alpha_1\cdots\alpha_k,
\]

its exact fine transition

\[
M_w=M_{\alpha_1}\cdots M_{\alpha_k}
\]

is equitable and

\[
\boxed{
Q_{M_w}
=
Q_{M_{\alpha_1}}\cdots Q_{M_{\alpha_k}}.
}
\]

Thus the fine witness labels inside each partition cell can be erased permanently for the declared future language:

> from a source coarse cell, compute exact total weighted path counts into every target coarse cell after any finite operation word.

This is a whole-algebra future-safety theorem, not merely one-step repair.

## 6. B50 — necessity for the declared generator language

If the future language includes the one-step block-count observable for every generator `M_alpha`, then equitability of every generator is also necessary.

Indeed, if some generator has two exact states `x,x'` in the same coarse cell with different target-cell count vectors, the one-step observable already distinguishes them. The proposed witness partition is therefore not future-safe.

Hence, for this declared language,

\[
\boxed{
\text{all generator matrices equitable}
}
\]

is the exact witness-label erasure criterion.

## 7. B51 — block-total representation

Let `n_a=|C_a|`. The total fine mass from source block `C_a` into target block `C_b` is

\[
T_M(a,b)
=
\sum_{x\in C_a,y\in C_b}M_{xy}
=
 n_a Q_M(a,b).
\]

Therefore, if cell sizes are retained, block totals are information-equivalent to the quotient row-count matrix on equitable states:

\[
\boxed{
Q_M(a,b)=T_M(a,b)/n_a.
}
\]

The division is exact by equitability.

For an operation word,

\[
T_{M_w}(a,b)
=
n_a(Q_{M_{\alpha_1}}\cdots Q_{M_{\alpha_k}})_{ab}.
\]

So exact block-total path counts also close on `(cell sizes, quotient matrices)`.

## 8. B52 — local zero coupling defect is weaker than global count-lumpability

Supplement 11 showed that `Delta=0` can occur for two non-uniform profiles, for example

\[
l=(0,0,1),
\qquad
r=(0,2,1).
\]

This makes one chosen cardinality composition exact, but the hidden incidences remain distinguishable by other target-block count observables.

So

\[
\boxed{
\Delta=0\text{ for one requested join}
\not\Rightarrow
\text{equitable future count algebra}.
}
\]

The hierarchy is now precise:

- one selected current count: zero defect or retain `Delta`;
- all one-step block counts of one matrix: equitable partition;
- arbitrary words in a finite matrix family: every generator equitable;
- witness identity itself: generally retain labels or prove a still richer quotient.

## 9. P023 extraction

This supplement is a specialization, not a competing theory.

P023 already says a finite operation family descends exactly when the chosen partition/congruence respects every generator. Here the abstract condition becomes an explicit integer criterion:

\[
\boxed{
\text{row sums into each coarse witness block are constant inside source blocks.}
}
\]

P023's partition-refinement closure can therefore be applied directly to repair a non-equitable witness partition by splitting exact states according to the future block-count signatures forced by the operation family.

Do not create a second generic refinement algorithm in the bridge.

## 10. Connection to P021

P021's witness-transport lesson was that cardinality shadows lose middle-incidence identity needed for composition. Supplement 11 quantified the one-step coupling defect. B47–B52 now give the stronger recursively stable condition under which witness identity can be erased for a whole count language.

P021 remains the discovery/application source for direction transport; the bridge provides the general count-algebra specialization of P023.

## 11. Connection to A4/E001

A4/E001 can use three distinct computational states depending on requested semantics:

1. boolean relation support for existence;
2. non-negative-integer quotient matrices for block-count/path-count semantics when the witness partition is equitable;
3. exact witness incidence when equitability fails or identity-sensitive diagnostics are requested.

This makes the engineering/state choice explicit rather than heuristic.

## 12. Prior-art discipline

Equitable partitions, quotient matrices, lumpability and invariant block-constant subspaces are established graph/algebra/Markov-chain ideas. No novelty claim is made for the abstract mathematics.

The project-specific value under test is the placement of this exact criterion in the current Enterprise Math state ladder, connecting P021 witness loss, A4/E001 count semantics and P023 legal quotienting.

## 13. Executable reference

The bridge reference layer adds:

- equitability audit for integer matrices and a witness partition;
- exact quotient count matrix;
- matrix-family/word quotient verification;
- block-total reconstruction;
- counterexample showing local zero coupling defect does not imply global equitability.
