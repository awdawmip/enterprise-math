# P025 Supplement 05 — Arithmetic Wronskian Witness-Budget Chain

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-arithmetic-witness-budget`  
Parent payload: `program/p025-abc-support-collapse@6c854aeb`  
Prior-art status: Pasten arithmetic derivatives/Wronskians are prior art; finite proof-budget interpretation `NOVELTY_UNVERIFIED`

## 1. Goal

Supplement 04 calibrated the classical polynomial Mason proof with a finite slack decomposition. The integer side must not inherit that degree formula by analogy alone.

Instead, start directly from Pasten's exact prime-coordinate arithmetic derivative and arithmetic Wronskian [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]. For a primitive triple

\[
a+b=c,
\qquad
\gcd(a,b)=1,
\]

and a support-restricted relation-adapted derivation `psi`, define

\[
d^\psi(n)
=
\sum_{p\mid n}
\frac{n}{p}v_p(n)\psi(\xi_p).
\]

Pasten's construction requires

\[
d^\psi(a)+d^\psi(b)=d^\psi(c)
\]

and defines

\[
W^\psi(x,y)=x d^\psi(y)-y d^\psi(x).
\]

The present supplement asks what exact finite information is discarded as one passes from this witness to the norm-only bound used in an `abc` estimate.

## 2. P025-T14 — local multiplicity residual is absorbed by the arithmetic derivative

For a positive integer `n`, recall

\[
m(n)=\frac{n}{\operatorname{rad}(n)}.
\]

Then for every prime-coordinate derivation `psi`,

\[
\boxed{m(n)\mid d^\psi(n).}
\]

### Proof

Each summand of `d^psi(n)` is

\[
\frac{n}{p}v_p(n)\psi(\xi_p).
\]

For every prime `q|n`, the exponent of `q` in `m(n)` is `v_q(n)-1`. In a summand indexed by `p=q`, the factor `n/p` still contains `q^{v_q(n)-1}`; in every other summand it contains the full `q^{v_q(n)}`. Thus every summand is divisible by `m(n)`, hence so is their sum.

This is the exact integer analogue of the familiar polynomial fact that the repeated-factor residual divides the derivative. It follows directly from Pasten's universal derivative formula and is not claimed as new number theory.

## 3. P025-T15 — the full abc multiplicity residual divides a common arithmetic Wronskian

Put

\[
M=m(a)m(b)m(c)
=
\frac{abc}{\operatorname{rad}(abc)}.
\]

Because a primitive `abc` triple has pairwise-disjoint prime support, the three residuals `m(a),m(b),m(c)` are pairwise coprime.

For a relation-adapted `psi`, additivity gives

\[
\begin{aligned}
W^\psi(a,b)
&=a d^\psi(b)-b d^\psi(a),\\
&=a d^\psi(c)-c d^\psi(a),\\
&=c d^\psi(b)-b d^\psi(c).
\end{aligned}
\]

Up to the orientation sign these are the same cyclic witness.

By P025-T14:

- `m(a)` divides the first expression;
- `m(b)` divides the first expression;
- `m(c)` divides the second or third expression.

Pairwise coprimality therefore yields

\[
\boxed{
M\mid W^\psi(a,b).
}
\]

The same holds for every cyclic orientation. If the witness is non-degenerate,

\[
\boxed{M\le |W^\psi|.}
\]

This is the integer residual-to-common-witness absorber used in the arithmetic derivative approach.

## 4. P025-T16 — exact four-level integer witness-budget chain

Fix an ordered pair `(x,y)` chosen from the triple. Expanding the arithmetic Wronskian in prime coordinates gives

\[
W^\psi(x,y)
=
\sum_{p\mid y}
 x\frac{y}{p}v_p(y)\psi(\xi_p)
-
\sum_{p\mid x}
 y\frac{x}{p}v_p(x)\psi(\xi_p).
\]

Define the **absolute-coordinate budget**

\[
B_{\rm abs}^{x,y}(\psi)
=
\sum_{p\mid y}
\left|x\frac{y}{p}v_p(y)\psi(\xi_p)\right|
+
\sum_{p\mid x}
\left|y\frac{x}{p}v_p(x)\psi(\xi_p)\right|.
\]

This forgets the signed cancellation among exact prime-coordinate contributions.

Now let

\[
\|\psi\|_\infty
=
\max_{p\mid abc}|\psi(\xi_p)|
\]

and define the pair coefficient mass

\[
H_{x,y}
=
\sum_{p\mid y}x\frac{y}{p}v_p(y)
+
\sum_{p\mid x}y\frac{x}{p}v_p(x).
\]

The **norm-only budget** is

\[
B_{\|\psi\|}^{x,y}
=
\|\psi\|_\infty H_{x,y}.
\]

It forgets the coordinate-by-coordinate magnitudes and retains only the maximum derivation coordinate.

For every non-degenerate relation-adapted witness,

\[
\boxed{
M
\le
|W^\psi(x,y)|
\le
B_{\rm abs}^{x,y}(\psi)
\le
B_{\|\psi\|}^{x,y}.
}
\]

The first inequality is P025-T15; the second is the triangle inequality; the third is the definition of the `L_infinity` norm.

All four quantities are integers.

## 5. P025-T17 — exact telescoping proof-loss shells

Define

\[
\begin{aligned}
g_1&=|W^\psi|-M,\\
g_2&=B_{\rm abs}^{x,y}(\psi)-|W^\psi|,\\
g_3&=B_{\|\psi\|}^{x,y}-B_{\rm abs}^{x,y}(\psi).
\end{aligned}
\]

Then

\[
g_1,g_2,g_3\ge0
\]

and exactly

\[
\boxed{
B_{\|\psi\|}^{x,y}-M=g_1+g_2+g_3.
}
\]

The three coordinates have distinct semantics:

1. `g_1` — **absorption gap**: witness size beyond the multiplicity demand;
2. `g_2` — **cancellation gap**: capacity introduced by forgetting prime-coordinate signs;
3. `g_3` — **norm-projection gap**: capacity introduced by replacing the actual coordinate magnitudes with one maximum norm.

This is a pure finite integer precision-shell decomposition of the proof relaxation. It is not an additional `abc` inequality.

## 6. Exact pre-log abc envelope

Because `M=abc/rad(abc)`, P025-T16 immediately gives the integer cross-multiplied bound

\[
\boxed{
abc
\le
\operatorname{rad}(abc)\,
B_{\|\psi\|}^{x,y}.
}
\]

If `z` is the third element complementary to the pair `(x,y)`, canceling the positive factor `xy` gives the equivalent classical-looking expression

\[
\boxed{
z
\le
\operatorname{rad}(abc)\,\|\psi\|_\infty
\left(
\sum_{p\mid x}\frac{v_p(x)}{p}
+
\sum_{p\mid y}\frac{v_p(y)}{p}
\right).
}
\]

Applying ordinary estimates to the reciprocal-prime/valuation sum recovers the kind of norm contribution used in Pasten's `abc` estimate. P025 does not claim this inequality or that analytic step as new; the purpose here is to stop **before** logarithmic smoothing and expose the exact integer proof-loss layers.

## 7. P025-T18 — witness precision is exactly the optimizable norm-budget factor

Fix the target `c`, so the relevant complementary Wronskian pair is `(a,b)`. The coefficient mass

\[
H_{a,b}
\]

depends only on the arithmetic triple. It does not depend on which relation-adapted witness is chosen.

Recall from Supplement 01 the exact witness precision

\[
\mu(a,b,c)
=
\min_{\psi\in\mathscr T(a,b)\setminus\mathscr T^\circ(a,b)}
\|\psi\|_\infty.
\]

Therefore

\[
\boxed{
\min_{\psi\in\mathscr T(a,b)\setminus\mathscr T^\circ(a,b)}
B_{\|\psi\|}^{a,b}
=
H_{a,b}\,\mu(a,b,c).
}
\]

Consequently

\[
\boxed{
M\le H_{a,b}\,\mu(a,b,c).
}
\]

and equivalently

\[
\boxed{
abc
\le
\operatorname{rad}(abc)\,H_{a,b}\,\mu(a,b,c).
}
\]

### Architecture meaning

This identifies the earlier task-relative witness precision with an actual proof resource:

> `mu` is exactly the only factor in the norm-relaxed target-`c` capacity that must be optimized over the witness family.

The relation-conditioned witness search and the final norm-based `abc` proof budget are therefore not merely analogous. They share the same minimum integer precision parameter.

This mathematical link is already implicit in Pasten's small-derivative program; P025's contribution is the finite-collapse interpretation and explicit routing back to precision semantics.

## 8. Boundary example — same radical coarse state, different proof-relaxation loss

The earlier P025 counterexample can now be re-read at proof-budget level.

### `1+2=3`

Take the minimum adapted witness

\[
\psi(\xi_2)=1,
\qquad
\psi(\xi_3)=1.
\]

For the target-`c` pair `(1,2)`:

\[
M=1,
\quad
|W|=1,
\quad
B_{\rm abs}=1,
\quad
B_{\|\psi\|}=1.
\]

Every gap vanishes and `mu=1`.

### `1+8=9`

The same radical triple is `(1,2,3)`, but the relation forces a primitive minimum witness

\[
\psi(\xi_2)=1,
\qquad
\psi(\xi_3)=2,
\]

so `mu=2`. For the target-`c` pair `(1,8)`:

\[
M=12,
\quad
|W|=12,
\quad
B_{\rm abs}=12,
\quad
B_{\|\psi\|}=24.
\]

Thus

\[
(g_1,g_2,g_3)=(0,0,12).
\]

The repeated-prime demand is absorbed exactly and there is no sign-cancellation loss. The entire looseness enters only when the full relation witness is collapsed to its maximum norm.

This makes the previous witness-precision separation operational: the same radical coarse state can require a strictly larger norm-only proof budget because the active additive relation forces a larger coordinate elsewhere in the witness state.

## 9. Orientation is typed proof state, not an intrinsic slack

For a relation-adapted `psi`, the three cyclic Wronskians agree up to sign, hence have the same absolute witness level. Their envelopes need not agree.

For the same `1+8=9` minimum witness:

\[
\begin{array}{c|ccc}
(x,y)&|W|&B_{\rm abs}&B_{\|\psi\|}\\
\hline
(1,8)&12&12&24\\
(8,9)&12&204&312\\
(9,1)&12&12&12
\end{array}
\]

So `g_2,g_3` are not intrinsic properties of the abstract witness alone. They are properties of a **typed proof orientation** `(target, complementary pair)`.

For a fixed norm, the norm-budget ordering is determined by the integer coefficient masses `H_{x,y}` and is independent of the particular witness vector. This separates two decisions:

1. witness search controls `||psi||`;
2. proof orientation controls `H_{x,y}`.

For the classical target-`c` question the complementary pair `(a,b)` is fixed, so `mu` remains the correct witness optimization parameter. For other proof-query languages, orientation itself is another finite selector state.

## 10. A nontrivial cancellation sample

For

\[
2+3=5
\]

choose the adapted witness

\[
(\psi(\xi_2),\psi(\xi_3),\psi(\xi_5))=(1,1,2).
\]

For pair `(2,3)`:

\[
M=1,
\quad
|W|=1,
\quad
B_{\rm abs}=5,
\quad
B_{\|\psi\|}=10,
\]

so

\[
(g_1,g_2,g_3)=(0,4,5).
\]

Here both sign cancellation and norm projection lose information even though residual absorption is exact.

A different adapted witness on the same triple can redistribute these gaps. Hence a final bound is generally not a complete state for proof-provenance questions.

## 11. Relation to P018/P023 and ownership boundary

The generic arithmetic fact

\[
D\le W\le U
\Longrightarrow
U-D=(W-D)+(U-W)
\]

is elementary accounting and is not a new mother theorem.

Likewise, P023 already owns generic task-relative observation/minimal-repair structure, and current P018 work already treats defect/margin coordinates as optional state above weaker pair/kernel structure.

Therefore the correct routing is:

- **P025 owns** the arithmetic-derivative specialization, exact examples, and `abc` pressure-test semantics;
- **P018/P023 may consume** the four-level chain as a proof-state pressure test;
- **do not create** a duplicate generic A2 theorem merely because the same arithmetic chain is useful here.

The genuinely useful cross-route message is that proof relaxations themselves can be typed finite precision changes, and their individual gaps should be retained only when the future query consumes proof provenance.

## 12. Prior-art boundary

Pasten defines the prime-coordinate arithmetic derivative, relation-adapted module, `L_infinity` norm, arithmetic Wronskian, non-degeneracy condition, controlled-size derivatives, and an `abc` estimate containing the derivative norm [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES].

P025-T14--T18 are direct exact unpackings and finite-state reorganizations of those ingredients plus elementary divisibility/triangle/norm arguments. No priority is claimed for the underlying inequalities.

The project-side research candidate is only the integration

\[
\text{relation witness precision}
\to
\text{exact proof-budget shells}
\to
\text{task-relative erasure/provenance}.
\]

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable evidence

This generation adds:

- `src/enterprise_math/arithmetic_witness_budget.py`;
- `tests/test_arithmetic_witness_budget.py`.

The executable layer checks:

- `m(n)|d^psi(n)` on exact integer examples;
- residual product divisibility of every cyclic adapted Wronskian;
- the four-level chain and three-gap telescoping law;
- the two same-radical witness-precision examples;
- simultaneous positive cancellation and norm-projection gaps;
- cyclic witness equality with orientation-dependent envelopes;
- rejection of non-adapted and degenerate witnesses.

An independent bounded scan over primitive triples with `c<40`, support dimension at most four, and derivation coordinates in `[-2,2]` checked 3,312 adapted non-degenerate witness states, hence 9,936 cyclic pair-budget profiles, with no failure of the chain or residual divisibility. This is regression evidence, not proof.

## 14. Next frontier

The next useful questions are now sharper:

1. determine whether minimizing `mu` alone explains all witness-dependent loss in Pasten's norm estimate, while the remaining factor is entirely triple-determined;
2. compare the target-`c` coefficient mass `H_{a,b}` against radical/residual coordinates on high-quality triples and search for exact further collapse;
3. test whether the three-gap vector `(g1,g2,g3)` has any monotone or sparse structure on minimum witnesses;
4. only if a nontrivial invariant survives this pressure test should it be abstracted toward P018/P023;
5. continue treating Pasten's analytic `abc` estimate and small-derivative equivalence as prior art rather than a project proof.
