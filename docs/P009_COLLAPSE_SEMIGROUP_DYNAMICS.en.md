# P009 — Dynamics of the collapse-only semigroup

Status: `PROVED` for the collapse-only subproblem  
Open problem: `P009` remains `PARTIAL-RESOLUTION` because the original problem also includes scale maps  
Scope: ordinary mathematics

## 1. Scope

Let

\[
W=C_{p_m}\circ\cdots\circ C_{p_1}
\]

be a fixed finite word of positive-exponent perfect-power collapse operators, and let

\[
L=\operatorname{lcm}(p_1,\ldots,p_m).
\]

For the empty word, take \(W=\operatorname{id}\) and \(L=1\).

P004 proved

\[
\operatorname{Fix}(W)=\operatorname{Fix}(C_L).
\]

This note classifies the forward iteration of every such fixed collapse word.

It does **not** classify the larger semigroup after scale-refinement or scale-projection maps are added. That part of P009 remains open.

## 2. Basic order properties

### P009-T01 — Every collapse word is monotone and reductive

Status: `PROVED`

For every natural state \(n\),

\[
W(n)\le n.
\]

Moreover, \(W\) is monotone.

### Proof

Each generator \(C_p\) is monotone by T009 and reductive by T004. Finite composition preserves monotonicity. Applying the reductive inequality at every stage gives

\[
C_{p_m}(\cdots C_{p_1}(n)\cdots)
\le\cdots\le C_{p_1}(n)\le n.
\]

∎

Thus for the orbit

\[
n_{t+1}=W(n_t),
\]

we have

\[
n_0\ge n_1\ge n_2\ge\cdots.
\]

## 3. A persistent lower bound

### P009-T02 — The lcm-collapse state is invariant below the orbit

Status: `PROVED`

Let

\[
a=C_L(n_0).
\]

Then for every \(t\ge0\),

\[
a\le n_t.
\]

### Proof

Because each \(p_i\mid L\), every perfect \(L\)-th power is a perfect \(p_i\)-th power. Therefore every generator fixes \(a\), and hence

\[
W(a)=a.
\]

At \(t=0\), contractivity of \(C_L\) gives \(a\le n_0\). If \(a\le n_t\), monotonicity of \(W\) gives

\[
a=W(a)\le W(n_t)=n_{t+1}.
\]

Induction completes the proof. ∎

So the orbit is trapped in the finite integer interval

\[
[C_L(n_0),n_0].
\]

## 4. Exact convergence

### P009-T03 — Iteration converges exactly to the lcm collapse

Status: `PROVED`

For every initial state \(n_0\), repeated iteration of the fixed word \(W\) stabilizes after finitely many steps, and its eventual value is exactly

\[
C_L(n_0).
\]

Equivalently, there exists \(T\) such that for all \(t\ge T\),

\[
W^t(n_0)=C_L(n_0).
\]

### Proof

By P009-T01, the orbit is nonincreasing in \(\mathbb N\). Whenever \(n_{t+1}\ne n_t\), reductivity implies

\[
n_{t+1}<n_t.
\]

A natural-number sequence cannot strictly decrease forever, so the orbit stabilizes at some state \(z\) satisfying

\[
W(z)=z.
\]

By P004, fixed points of \(W\) are exactly perfect \(L\)-th powers. Hence \(z\) is a perfect \(L\)-th power. Since the entire orbit is nonincreasing,

\[
z\le n_0.
\]

By definition, \(C_L(n_0)\) is the greatest perfect \(L\)-th power not exceeding \(n_0\), so

\[
z\le C_L(n_0).
\]

But P009-T02 gives the reverse inequality

\[
C_L(n_0)\le z.
\]

Therefore

\[
z=C_L(n_0).
\]

∎

This is stronger than P004: word order affects transient states, but repeated application erases that difference completely.

## 5. Finite convergence bound

### P009-T04 — Crude strict-decrease bound

Status: `PROVED`

The number of nonstationary iterations before convergence is at most

\[
n_0-C_L(n_0).
\]

### Proof

Every nonstationary step decreases the integer state by at least one, while P009-T02 prevents the orbit from dropping below \(C_L(n_0)\). ∎

This bound is intentionally crude. Sharper bounds depending on the exponent word are a separate optimization problem.

## 6. No nontrivial cycles

### P009-T05 — Collapse words have no cycles of period greater than one

Status: `PROVED`

For a fixed collapse word \(W\), every periodic point is a fixed point.

### Proof

If

\[
n_0\mapsto n_1\mapsto\cdots\mapsto n_{r-1}\mapsto n_0,
\]

then reductivity gives

\[
n_0\ge n_1\ge\cdots\ge n_{r-1}\ge n_0.
\]

Antisymmetry forces all states to be equal. ∎

Thus the collapse-only dynamics is acyclic apart from fixed points.

## 7. Attractors and basins

### P009-T06 — Attractors and eventual basins

Status: `PROVED`

For the fixed word \(W\) with lcm exponent \(L\):

- the attractors are exactly the perfect \(L\)-th powers;
- the eventual attractor reached from \(n\) is \(C_L(n)\);
- therefore the eventual basin of \(k^L\) is exactly

\[
\{n:k^L\le n<(k+1)^L\},
\]

which is the ordinary \(L\)-collapse basin.

So iteration converts an order-sensitive transient word into an order-insensitive asymptotic projection.

## 8. Word order survives only transiently

Take the incomparable exponents \(2\) and \(3\). At \(n=8\):

\[
C_2(C_3(8))=4,
\qquad
C_3(C_2(8))=1.
\]

The one-pass actions differ. But both words have \(L=6\). Under repeated iteration, both converge to

\[
C_6(8)=1.
\]

Thus P003 and P009 describe two different layers:

- **one-step algebra:** sensitive to divisibility comparability and word order;
- **long-run dynamics:** determined only by the lcm of the exponent support.

## 9. Collapse-only semigroup classification obtained so far

For every element represented by a finite collapse word, we now know:

1. its fixed-point set;
2. every forward orbit's exact eventual attractor;
3. all eventual basins;
4. that nontrivial periodic cycles do not exist;
5. a finite convergence bound for each initial state.

What is **not** yet classified is equality of arbitrary distinct words as functions. P003 solves the two-generator commutation question, but different longer words can have the same fixed and asymptotic behavior while differing on transients.

## 10. Why P009 remains partially open

The original P009 also includes scale maps. Scale refinement/projection need not share the simple reductive-on-one-state-space behavior used above. Once they are added, the state space and order dynamics can change substantially.

Therefore the project status should be:

- collapse-only attractor/fixed-point/cycle dynamics: `PROVED`;
- equality/normal forms of arbitrary collapse words: open;
- the full semigroup generated jointly by collapse and scale maps: open;
- overall P009: `PARTIAL-RESOLUTION`.

## 11. Prior-art discipline

The proof uses elementary facts about monotone reductive maps on a well-founded discrete order, P004's fixed-point theorem, and the definition of greatest perfect powers. These ingredients are established mathematics.

A targeted search did not identify this exact collapse-family asymptotic statement as a named prior theorem. That search result is not evidence of historical priority. The exact formulation therefore remains `NOVELTY_UNVERIFIED` even though the theorem itself is `PROVED`.
