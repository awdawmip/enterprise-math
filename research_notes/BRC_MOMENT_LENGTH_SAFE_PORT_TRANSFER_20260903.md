# BRC Moment/Length-Safe Port Transfer

Status: `RESEARCH CANDIDATE / EXACT FORMAL+FINITE-RATIONAL / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parents:
- recurrent branch-moment lift / finite moment completeness;
- recurrent Schur/port contextual collapse `WBRC-T30..T32`.

## 1. Purpose

Ordinary recurrent Schur collapse preserves positive **all-length total mass** at `m=1,z=1`, but it intentionally forgets original walk length and explicit branch-moment information.

The moment lift supplies exact matrices

\[
W^{(m)}_{ij}=\sum_{e:i\to j}q_e^m,
\qquad m=0,1,2,\ldots
\]

for explicit positive rational branches. This note combines that lift with port elimination while retaining a formal/rational **length marker** `z`.

Generic transfer-matrix generating functions, Schur complements over rational-function fields and formal power-series elimination are classical mathematics. No generic novelty claim is made. The project-specific result proposed here is the typed two-parameter BRC port semantics and its boundaries relative to existing total-mass port collapse.

## 2. Moment matrix block form

Fix an integer moment order `m>=0`. Partition states into hidden/internal `I` and retained ports `B`:

\[
W^{(m)}
=
\begin{pmatrix}
A_m&X_m\\
Y_m&B_m
\end{pmatrix}.
\]

Introduce a formal length marker `z`. The one-original-edge transfer matrix is

\[
K_m(z)=zW^{(m)}.
\]

Because `I-zA_m` has constant term `I`, it is always invertible over the formal power-series ring `Q[[z]]` and over the rational-function field `Q(z)`:

\[
(I-zA_m)^{-1}
=\sum_{k\ge0}z^kA_m^k
\]

formally.

No analytic stability assumption is needed for this formal identity.

## 3. Length-aware effective port kernel

Define

\[
\boxed{
E_m(z)
=zB_m
+z^2Y_m(I-zA_m)^{-1}X_m.
}
\]

Expanding,

\[
E_m(z)
=zB_m
+\sum_{k\ge0}z^{k+2}Y_mA_m^kX_m.
\]

Hence the coefficient of `z^ell` is:

\[
[z^1]E_m=B_m,
\]

and for `ell>=2`,

\[
\boxed{
[z^\ell]E_m
=Y_mA_m^{\ell-2}X_m.
}
\]

This coefficient is exactly the m-th power-sum mass of port-to-port path segments of original length `ell` whose internal vertices lie entirely in `I` and whose only port visits are the endpoints.

Thus `E_m(z)` is an **irreducible port-segment generating matrix**.

## 4. Formal boundary-star theorem

### Candidate BRC-MLP1

Over `Q[[z]]` (equivalently as rational matrix functions in `Q(z)`),

\[
\boxed{
(I-zW^{(m)})^{-1}[B,B]
=(I-E_m(z))^{-1}.
}
\]

There are two equivalent proofs.

### Block algebra

Apply Schur complement to

\[
I-zW^{(m)}
=
\begin{pmatrix}
I-zA_m&-zX_m\\
-zY_m&I-zB_m
\end{pmatrix}.
\]

Its boundary Schur complement is

\[
I-zB_m-z^2Y_m(I-zA_m)^{-1}X_m
=I-E_m(z).
\]

### Path segmentation

Every original port-to-port walk has a unique decomposition at successive port visits into irreducible segments. `E_m(z)` records every such segment with exact original-length degree and exact m-th weight power-sum. The geometric closure

\[
I+E_m+E_m^2+\cdots
\]

concatenates segments, adds original lengths through powers of `z`, and multiplies m-th power weights through the moment character.

## 5. Coefficientwise path semantics

Let

\[
G_{m,B}(z)=(I-E_m(z))^{-1}.
\]

Then

\[
\boxed{
[z^n]G_{m,B}(z)_{uv}
=\sum_{\substack{p:u\to v\\|p|=n}}\operatorname{wt}(p)^m
}
\]

for every pair of retained ports and every `n>=0`.

Thus the full fixed-length branch-moment semantics survives internal recurrent elimination exactly.

At `m=0`, coefficients are exact path counts by original length.

At `m=1`, coefficients are exact positive total masses by original length.

## 6. Analytic/stable specialization

For a positive rational evaluation `z=z_0`, if the hidden matrix `z_0A_m` is stable then the formal hidden series converges to the exact rational matrix

\[
(I-z_0A_m)^{-1}.
\]

If the full/reduced positive system is stable, the formal boundary identity specializes to the ordinary exact recurrent star identity at `z_0`.

All current recurrent Foundation tools may therefore be applied to the evaluated positive matrix `z_0W^(m)` whenever its typed stability hypotheses hold.

Formal rational evaluation and positive recurrent summability must remain distinct:

```text
RATIONAL FUNCTION EXISTS
!=
POSITIVE WALK SUM CONVERGES AT THAT z.
```

A rational function may have a finite algebraic value at a positive `z` outside the convergence radius; that value is not a valid positive BRC recurrent sum.

## 7. Existing port collapse is one specialization

At `m=1`,

\[
W^{(1)}=W.
\]

If the ordinary hidden total-mass block `A_1` is stable, then at `z=1`,

\[
\boxed{
E_1(1)
=B+Y(I-A)^{-1}X
=W_{\rm eff}.
}
\]

Therefore `WBRC-T30..T32` are the `(m=1,z=1)` stable specialization of the length-aware transfer.

## 8. Count recurrence is formally retained

At `m=0`, `W^(0)=N` is the explicit branch-count adjacency matrix.

Even if the hidden support is recurrent and

\[
I+N+N^2+\cdots
\]

diverges at `z=1`, the formal port kernel

\[
\boxed{
E_0(z)
=zB_0+z^2Y_0(I-zA_0)^{-1}X_0
}
\]

is a finite matrix of rational functions in `z` and has a well-defined formal power series at `z=0`.

Example: one hidden state with one self-loop and one port-entry/port-exit route gives

\[
E_0(z)=\frac{z^2}{1-z}
=z^2+z^3+z^4+\cdots.
\]

At `z=1` the positive count sum diverges, but every fixed-length coefficient and the rational/formal generating object remain exact.

This is the desired repair of the recurrent `C=infinity` boundary.

## 9. Determinant factorization over Q(z)

The block determinant identity is

\[
\boxed{
\det(I-zW^{(m)})
=\det(I-zA_m)\det(I-E_m(z)).
}
\]

The first factor records hidden moment/length recurrence; the second records retained-port recurrence after exact elimination.

At positive rational `z` in the stable region this yields exact loop-zeta factorization for the m-th moment-lifted system.

For formal/generating-function semantics it is an algebraic factorization without any logarithmic or convergence claim.

## 10. Fixed-m port contexts

Let a future explicit positive-rational context attach only through retained ports and new external states. Apply the same moment character `m` to the context branches.

At one-edge transfer level, context blocks appear multiplied by `z`. After eliminating hidden `I`, the visible transfer kernel is

\[
\boxed{
\begin{pmatrix}
E_m(z)+zC_m&zU_m\\
zV_m&zR_m
\end{pmatrix}.
}
\]

### Candidate BRC-MLP2

For every fixed integer `m>=0`, the rational-function matrix `E_m(z)` is a complete exact port signature for all formal fixed-m length-aware visible path-moment queries and all external contexts that cannot touch hidden internal states.

If the observer sees the complete port generating star

\[
G_{m,B}(z),
\]

then

\[
\boxed{
E_m(z)=I-G_{m,B}(z)^{-1}.
}
\]

Hence `E_m(z)` is also necessary/minimal up to bijective re-encoding for this fixed-m formal observer.

If absolute determinant/zeta of the full moment-lifted module is also observed, additionally retain

\[
D_{m,\rm int}(z)=\det(I-zA_m)
\]

(or its reciprocal). For context-induced ratios/increments, the hidden factor cancels.

## 11. Gauge naturality across moment order

Under positive rational state gauge

\[
q'_e=q_e\frac{h_t}{h_s},
\]

branch m-th powers transform as

\[
(q'_e)^m=q_e^m\frac{h_t^m}{h_s^m}.
\]

Let

\[
H_m=\operatorname{diag}(h_i^m).
\]

Then

\[
W^{(m)'}=H_m^{-1}W^{(m)}H_m
\]

and therefore

\[
\boxed{
E'_m(z)
=H_{m,B}^{-1}E_m(z)H_{m,B}.
}
\]

At `m=0`, `H_0=I`, so pure branch-count transfer is exactly gauge blind.

At `m=1`, this recovers the existing rational port-gauge law.

## 12. Sequential elimination

Because Schur complements are transitive over the field `Q(z)` and the formal inverse exists at `z=0`, internal state sets may be eliminated sequentially at fixed moment order `m`, giving the same final `E_m(z)` as one-shot elimination.

Unlike the positive `z=1` total-mass theorem, the formal statement does not require every intermediate internal block to be analytically stable; it requires only the algebraic/formal Schur expressions, whose denominators have constant term 1 and are therefore invertible as formal power series.

This creates an exact formal recurrent coarse-graining hierarchy even for count semantics.

## 13. Hard negative: ordinary W_eff is not length-safe

Two modules may have equal ordinary all-length total-mass effective matrix at `m=1,z=1` while having different original length structure.

Example:

- Module A: one direct port edge of mass `1`, giving
  \[
  E_{1,A}(z)=z.
  \]
- Module B: one two-edge internal route whose product is `1`, giving
  \[
  E_{1,B}(z)=z^2.
  \]

At `z=1`, both give ordinary effective mass `1`, but

\[
E_{1,A}(z)\ne E_{1,B}(z).
\]

Therefore constant `W_eff` is not a safe signature for observers that retain original walk length.

## 14. Hard negative: primitive-edge finite moment cutoff need not survive port collapse

The finite moment-completeness theorem for primitive edge cells says that maximum local parallel multiplicity `R` makes `W^(0)..W^(R)` complete for the **primitive branch-weight multiset**.

That cutoff does not automatically make the collapsed port family `E_0(z)..E_R(z)` complete.

A sharp witness already exists with primitive local parallel multiplicity `R=1`.

Construct two modules with two disjoint length-2 internal paths from port `u` to port `v`, no parallel primitive edges, and path weights:

\[
\{1/3,2/3\}
\]

versus

\[
\{1/4,3/4\}.
\]

Both have

\[
E_0(z)=2z^2,
\qquad
E_1(z)=z^2,
\]

but

\[
E_{2,A}(z)=\frac59z^2,
\qquad
E_{2,B}(z)=\frac58z^2.
\]

Thus the port moment hierarchy can contain more moment information than the maximum primitive local parallel multiplicity suggests, because internal path multiplicity grows under composition.

No finite all-moment port cutoff is claimed here.

## 15. Two-parameter port signature frontier

The exact fixed-order family is

\[
\boxed{
\mathcal E_M(z)=\{E_m(z):m=0,1,\ldots,M\}.
}
\]

For each fixed `m` it is operation-safe and context-complete for m-th path moments by length. The full all-moment family

\[
\{E_m(z)\}_{m\ge0}
\]

captures the complete moment hierarchy of port-to-port paths.

Whether that infinite family admits a smaller finite exact port representation in general is left open. The primitive-edge Newton completeness theorem does not by itself solve the collapsed-path problem.

## 16. Prior-art boundary

Formal transfer functions, generating functions, Schur complements over rational-function fields, hidden-state elimination and fixed-order moment/partition transfers are classical/general mathematics.

No generic novelty claim is made.

The project-specific synthesis proposed here is the exact BRC statement

\[
\boxed{
\text{moment order }m
+\text{length marker }z
+\text{ported recurrent elimination}
\to E_m(z)
}
\]

which simultaneously:

- repairs recurrent count by preserving coefficients instead of collapsing to infinity;
- recovers ordinary recurrent port collapse at `(m=1,z=1)`;
- preserves exact fixed-length CWM moment information through hidden-state elimination;
- identifies the stronger signature required once original length/moment observers are admitted.

## 17. Validation plan

1. On a fixed explicit 4-state multigraph with hidden states and parallel branches, for `m=0..5` and lengths `n=0..7`, compare full explicit path moment coefficients on ports with coefficients reconstructed from the formal segment series `E_m(z)`.
2. At several rational `z` values in stable regions, verify exact block resolvent and determinant factorization for `m=0..5`.
3. Verify `(m=1,z=1)` equals ordinary `W_eff` on a stable total-mass module.
4. Verify a hidden count self-loop yields `E_0(z)=z^2/(1-z)` coefficientwise, while positive evaluation at `z=1` is outside the stable count semantics.
5. Verify fixed-m external port-context star equality at rational stable z.
6. Verify moment-order gauge naturality, including exact gauge blindness at `m=0`.
7. Verify one-shot versus sequential internal elimination at multiple `(m,z)` rational points.
8. Verify the length-loss witness `z` versus `z^2` at equal ordinary `W_eff(1)`.
9. Verify the `R=1` primitive-edge counterexample with equal `E_0,E_1` but unequal `E_2`.

A dedicated research CI gate must pass before Foundation backflow.
