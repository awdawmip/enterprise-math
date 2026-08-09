# P018 — Finite-Precision Proof Calculus: Supplement 26

Status: `ACTIVE RESEARCH NOTE`  
Scope: one-shot transport versus self-contained reusable interfaces, exact access-model minima, and the boundary of Q119  
Depends on: P018-T175/T176, T198–T212  
Prior-art boundary: communication complexity, coding for computing, quotient algebra, and syntactic congruence are established. This note does not claim a new communication model; it identifies which already-defined Enterprise Math invariant is the correct minimum under two different information-access contracts.

---

## 1. There is no single transport minimum without an access contract

The phrase “minimum information needed to perform an operation” is ambiguous unless one specifies:

1. who can see the hidden fine state;
2. what side information the receiver already knows;
3. whether the transmitted object is used only for this operation call or must survive as a reusable state for later operations.

Supplements 19, 24, and 25 already contain two different exact minima. They answer different contracts.

### One-shot centralized correction model

The encoder sees the current fine input tuple. The decoder knows the raw coarse input tuple and asks only for the exact raw coarse output of this one call.

T200 gives

\[
\boxed{|\mathcal C|_{\min}=B_E(\mu).}
\]

### Self-contained reusable interface model

A subsystem/subtree emits a state label `I(x)`. Future callers no longer have access to the hidden fine state `x`; the interface state itself must preserve the original observation and support every declared future operation exactly.

That is a state-sufficiency problem, not a one-shot correction problem.

---

## 2. P018-T213 — Exact reusable-interface criterion

Status: `PROVED / EXECUTABLE`

Let

\[
I:X\to Z
\]

be a candidate reusable interface and let

\[
R_I=\ker(I).
\]

For an operation language `Sigma`, `I` is an exact reusable interface preserving the raw observation `O` exactly when:

1. raw observation factors through the interface,

   \[
   \boxed{R_I\subseteq\ker(O),}
   \]

   so `I` never identifies states that `O` distinguishes;
2. `R_I` is a `Sigma`-congruence, so every declared operation descends to the interface state space.

Equivalently: a reusable interface is precisely an observation-respecting exact quotient/refinement state for the declared operation language.

---

## 3. P018-T214 — Contextual closure is the minimum reusable exact interface

Status: `PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

Let

\[
R_*=\operatorname{Syn}_\Sigma(\ker O)
\]

be the contextual closure from T171–T175.

If `I` is any exact reusable interface, T213 says `R_I` is a `Sigma`-congruence contained in `ker(O)`. By maximality of `R_*`,

\[
\boxed{R_I\subseteq R_*.}
\]

Therefore every exact reusable interface must distinguish at least all contextual-closure classes. Hence

\[
\boxed{
|I(X)|
\ge
|X/R_*|.
}
\]

Conversely the canonical quotient map

\[
X\to X/R_*
\]

is itself an exact reusable interface.

Thus

\[
\boxed{
\min\#\text{ reusable interface states}
=
|X/R_*|.
}
\]

T175 is therefore also the exact reusable-interface minimum theorem.

---

## 4. P018-T215 — Future operation language parametrizes the minimum reusable state

Status: `PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

Let

\[
\Gamma\subseteq\Sigma.
\]

If a module promises exact reuse only under the smaller future language `Gamma`, its canonical minimum interface is

\[
X/\operatorname{Syn}_\Gamma(E).
\]

If it must support the larger language `Sigma`, T179 gives

\[
\operatorname{Syn}_\Sigma(E)
\subseteq
\operatorname{Syn}_\Gamma(E).
\]

Therefore

\[
\boxed{
|X/\operatorname{Syn}_\Sigma(E)|
\ge
|X/\operatorname{Syn}_\Gamma(E)|.
}
\]

Reusable precision is therefore not only observation-dependent; it is a contract on the **future operation language**.

---

## 5. P018-T216 — One-shot token and reusable state can differ without bound

Status: `PROVED / EXECUTABLE FAMILY`

For every radix `r>=2`, consider the finite cyclic state space

\[
X_r=\mathbb Z/(2r)\mathbb Z
\]

represented by states

\[
\{0,1,\ldots,2r-1\},
\]

with addition modulo `2r`.

Observe only the upper radix block:

\[
O_r(x)=\left\lfloor\frac xr\right\rfloor\in\{0,1\}.
\]

### One-shot transport

For fixed raw coarse inputs, the exact raw coarse output of modular addition has only two possibilities, corresponding to the residue carry/wrap bit. Hence

\[
\boxed{B_{E_r}(+)=2.}
\]

So the minimum one-shot correction token has only two symbols for every `r`.

### Reusable exact state

Take any two distinct states in the same raw block,

\[
x=qr+u,
\qquad y=qr+v,
\qquad 0\le u<v<r.
\]

Add the context constant

\[
t=r-1-u
\]

modulo `2r`.

If `q=0`, then

\[
O_r(x+t)=0,
\qquad
O_r(y+t)=1.
\]

If `q=1`, modular wrap reverses the two blocks:

\[
O_r(x+t)=1,
\qquad
O_r(y+t)=0.
\]

Thus every distinct pair inside each raw block is separated by some allowed addition context. Therefore

\[
\boxed{
\operatorname{Syn}_{+}(E_r)=\Delta,
}
\]

and the minimum self-contained reusable interface has all

\[
\boxed{2r}
\]

states.

Hence the ratio

\[
\boxed{
\frac{\text{minimum reusable states}}
     {\text{minimum one-shot token symbols}}
=r
}
\]

is unbounded.

A tiny transient correction message can coexist with arbitrarily large persistent reusable state complexity.

---

## 6. P018-C25 — Small transient token does not imply a small reusable module state

Status: `COUNTERWEIGHT / ACCESS-MODEL BOUNDARY`

T216 rules out the inference

\[
B_E(\mu)\text{ small}
\quad\Longrightarrow\quad
\text{small exact reusable state}.
\]

The one-shot encoder is allowed to inspect the hidden fine operands for the current call. A reusable subtree/module state is not: after emission, future operations can see only the interface state.

These are different information-access contracts.

The binary carry is therefore not a replacement for the operand remainder state. It is a compact transient output correction available because the current encoder still has access to the operand detail.

---

## 7. P018-T217 — Q119 access-model classification

Status: `RESOLVED AT THE TWO CANONICAL ACCESS EXTREMES`

For finite state spaces and finite finitary operation signatures, two canonical transport/state minima are now exact:

### Model A — one-shot centralized correction

- encoder sees the fine input tuple;
- decoder knows the raw coarse input tuple;
- message is used once to recover the raw coarse output.

Minimum token alphabet:

\[
\boxed{B_E(\mu).}
\]

### Model B — self-contained reusable exact interface

- hidden fine state is no longer available after interface emission;
- raw observation must be recoverable from the interface;
- every declared future operation must remain exact.

Minimum reusable state space:

\[
\boxed{X/\operatorname{Syn}_\Sigma(E).}
\]

These minima can be arbitrarily far apart by T216.

Therefore Q119 has no unique scalar answer until the **access/lifetime model** is fixed.

---

## 8. P018-T218 — Structured transport lives between the two minima, not instead of them

Status: `STRUCTURAL SYNTHESIS / EXECUTABLE EXEMPLAR`

Supplement 25's radix-addition `(carry,remainder)` law now has a precise location:

- the persistent remainder is part of the reusable exact state required by Model B;
- the carry is the operation-specific one-shot transport coordinate from Model A;
- their associative combination provides a reusable structured protocol without confusing the two information roles.

Thus a structured transport algebra should be modelled as a law acting **over** sufficient reusable state detail, possibly exposing a smaller transient token at operation boundaries.

It is not a substitute for contextual closure.

---

## 9. P018-C26 — “Transport complexity” is not well-defined without access and lifetime metadata

Status: `FOUNDATIONAL GUARDRAIL`

A request for “the transport complexity of an operation” is underspecified unless it states at least:

1. what fine information the encoder may inspect;
2. what coarse or contextual state the decoder already has;
3. whether the message is transient or must become the next reusable state;
4. which future operation language must remain exact;
5. whether composition/interactivity/variable-length coding is allowed.

Without these metadata, different valid models yield different exact minima.

P018 should therefore never report a single transport-complexity number without its access contract.

---

## 10. What remains open after the classification

The two canonical endpoints are exact, but substantial structure remains open between them:

- minimal composable interfaces when only a restricted future operation tree is known;
- fusion gains for multi-stage computations;
- representation-stable token laws under legitimate precision chart changes;
- interactive or distributed encoder models;
- variable-length / average-cost models;
- operation families with the same `B_E(mu)` but sharply different algebraic composability.

These should be treated as separate transport protocols, not folded back into the state ontology.

---

## 11. Executable validation

Added:

- `src/enterprise_math/reusable_interface.py`
- `tests/test_reusable_interface.py`

The tests verify:

1. exhaustive two-state reusable interfaces refine the canonical contextual closure;
2. raw observation can fail as a reusable interface even though it trivially preserves itself;
3. full-state identity is always a reusable exact interface;
4. the cyclic radix-addition family has one-shot `B=2` while the canonical reusable state has `2r` classes;
5. the one-shot/reusable gap grows linearly and without bound in `r`.
