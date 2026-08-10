# Legendre Pressure Test — Supplement 30

Status: `PROVED RESEARCH NOTE`  
Scope: no-go theorem for a single Bonferroni-depth proof axis  
Depends on: P017 L069 exact Mobius counts and L070 Bonferroni proof precision  
Discipline: this is a finite proof-language limitation, not a failure of the underlying shell theorem.

## 1. The tempting but false model

L070 introduces a useful proof-precision coordinate: the smallest odd Bonferroni depth whose lower bound proves that a p-rough branch is occupied.

One might hope that every true occupancy is eventually certified by increasing this odd depth far enough.

That is false.

The reason is elementary: when the number of small primes below `p` is even, the exact inclusion-exclusion sum may become positive only after the final **even** correction. No odd lower truncation then witnesses positivity.

## 2. P017-L071-A — Abstract finite no-go witness

Status: `PROVED`.

Take

\[
p=5
\]

and interval

\[
[2,6].
\]

The primes below `5` are `2,3`.

The exact 5-rough states are integers coprime to `6`; in this interval only

\[
q=5
\]

survives. Hence

\[
\boxed{R_5[2,6]=1.}
\]

But the only odd Bonferroni lower truncation is first order:

\[
B_1
=5-\#\{2\text{-multiples}\}-\#\{3\text{-multiples}\}
=5-3-2
=0.
\]

There is no higher odd depth because only two exclusion primes exist.

The exact positive count returns only after adding the pair-intersection term:

\[
5-3-2+1=1.
\]

Therefore

\[
\boxed{
R_p[a,b]>0
\not\Rightarrow
\exists\ d\text{ odd}:B_d(a,b,p)>0.
}
\]

## 3. P017-L071-B — The no-go occurs inside an actual split shell

Status: `PROVED BY EXACT P017 WITNESS`.

Take

\[
k=13,
\qquad
p=5.
\]

The actual least-prime shell is split across the two cofactor-root branches.

Its upper root subwindow is exactly

\[
\boxed{W_5^+=[36,39].}
\]

Among these integers, only

\[
37
\]

is coprime to `6`, so

\[
\boxed{R_5^+(13)=1.}
\]

However the first-order Bonferroni lower bound is

\[
B_1
=4-2-2
=0.
\]

Again there is no deeper odd truncation.

Thus the upper branch is genuinely occupied and the P017 shell genuinely splits, but the entire odd-Bonferroni lower-bound language fails to prove that upper occupancy.

The lower branch is easy: its first-order certificate is already positive.

Hence the same shell has

\[
\boxed{
(h_5^-,h_5^+)=(1,\mathrm{FULL}).
}

## 4. P017-L071-C — Proof precision is not one-dimensional in general

Status: `PROVED` by L071-B.

Suppose proof precision were represented solely by a scalar Bonferroni depth, with increasing depth expected to eventually resolve every true branch.

The `k=13,p=5` upper branch contradicts that model: no available odd depth resolves it, while exact Mobius inclusion-exclusion does.

Therefore a complete finite proof state must allow at least a proof-language coordinate:

\[
\boxed{
\text{proof state}
\supseteq
(\text{method/language},\text{depth within method}).
}
\]

A depth hierarchy is meaningful only inside a fixed proof language.

## 5. Method switch is not a semantic refinement of the number state

The branch truth

\[
R_5^+(13)>0
\]

is fixed throughout.

Changing from Bonferroni lower bounds to exact Mobius evaluation does not refine the represented cofactor or root state. It changes only the information available to the **proof process**.

Thus the project must keep three levels separate:

\[
\boxed{
\text{number state}
\neq
\text{task precision state}
\neq
\text{proof-method state}.
}
\]

They can interact, but they are not interchangeable coordinates.

## 6. P017-L071-D — Failure of a certificate language cannot be read as a negative theorem

Status: `PROVED / LOGICAL BOUNDARY`.

If every odd Bonferroni lower bound is nonpositive, the only valid conclusion is

\[
\boxed{
\text{this lower-bound family has not certified occupancy}.
}
\]

It does **not** imply

\[
R_p[a,b]=0.
\]

The `k=13,p=5` witness makes that distinction concrete inside the active number-theoretic problem.

This is an important general research discipline: failure to prove a statement inside one coarse proof language is an `UNKNOWN`, not evidence for the negation.

## 7. A proof-method lattice rather than a single proof-depth chain

The current P017 toolbox already contains several exact or one-sided proof languages:

- raw overshoot geometry;
- odd Bonferroni lower bounds;
- full Mobius inclusion-exclusion;
- CRT/residue reconstruction;
- rough/Buchstab recursion;
- Jacobsthal-type guaranteed occupancy bounds.

These methods are not linearly ordered by one scalar depth.

A more faithful future abstraction is a finite or locally finite **proof-method poset** where one method state is above another when every certificate available below can be mechanically recovered above.

L071 does not yet build that full poset; it proves why a single scalar proof-depth axis cannot be the universal object.

## 8. Algorithmic consequence

An adaptive proof compiler should therefore behave as follows:

1. try cheap low-depth Bonferroni certificates;
2. when the depth language saturates without a certificate, mark `UNKNOWN`, not `FALSE`;
3. switch horizontally to another exact/sufficient proof language;
4. compare method cost and certificate strength separately;
5. stop once the declared predicate is permanently certified.

This is qualitatively different from blindly increasing one precision parameter.

## 9. Executable specification

`tests/test_p017_root_split_proof_precision.py` pins both the abstract `[2,6],p=5` no-go and the actual `k=13,p=5` split-shell witness.

The test confirms:

\[
R_5^+(13)=1,
\qquad
B_1=0,
\]

while the shell remains an actual split.

## 10. Foundation feedback

L071 strengthens the emerging Enterprise Math principle:

\[
\boxed{
\text{precision is generally a structured state, not a universal scalar.}
}
\]

This now applies not only to physical/task precision but also to theorem proving itself: proof resources can require changes of representation, not merely increases of one depth parameter.
