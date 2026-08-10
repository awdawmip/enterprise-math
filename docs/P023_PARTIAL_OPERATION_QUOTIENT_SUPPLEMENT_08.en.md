# P023 — Legality-Sensitive Partial-Operation Quotients, Supplement 08

Status: `CANONICAL RESULT / EXECUTABLE-CHECKED / NOT LEAN-CHECKED`  
Scope: finite deterministic partial operation families with state-dependent action domains  
Depends on: FQ-004 functional-kernel layering, P023 total operation-family closure  
Resolution source: FQ-20260809-006, research return PR #285  
Discipline: partial transition systems, partial maps, automata with disabled actions, behavioral equivalence, sink totalization, and finite partition refinement are established prior mathematics. No generic novelty claim is made here.

## 1. Why total operations are not enough

Canonical P023 operation-family closure originally assumes a finite family of total deterministic endomaps

\[
F_a:X\to X.
\]

For a guarded action, legality may itself depend on the current state. The correct generic object is then a deterministic partial operation

\[
\boxed{F_a:D_a\to X,\qquad D_a\subseteq X.}
\]

A future-safe quotient for such a language must preserve not only the observed result of legal words, but also whether each declared action and prefix is legal. A disabled action is therefore not silently interpreted as identity or omission.

Throughout this supplement, `X` is a finite nonempty typed state set, `A` is a finite nonempty set of action names, each `F_a` is a deterministic partial map on `X`, and

\[
q_0:X\to Q_0
\]

is the initial observation / represented-precision partition.

## 2. Partial-operation compatibility

A partition `q:X->Q` is **compatible** with one partial operation `F_a:D_a->X` when equality of quotient classes implies both:

1. the two states agree on domain membership,
   \[
   x\in D_a\iff y\in D_a;
   \]
2. when the action is enabled, the targets lie in the same quotient class,
   \[
   x,y\in D_a\Longrightarrow q(F_a(x))=q(F_a(y)).
   \]

A partition is compatible with the family when this holds for every `a in A`.

This is exactly the condition required for the action to descend to the quotient **with its domain preserved**.

## 3. Legality-sensitive refinement

Given a current partition `q_t`, define the generator behavior

\[
B^t_a(x)=
\begin{cases}
(1,q_t(F_a(x))), & x\in D_a,\\
(0,\bot), & x\notin D_a,
\end{cases}
\]

where `bot` is only a signature marker for undefinedness, not an element of `X`.

Define

\[
\boxed{
q_{t+1}(x)
=
\left(q_t(x),(B^t_a(x))_{a\in A}\right),
}
\]

up to arbitrary relabeling of the induced finite partition.

## 4. P023-S4-T01 — Monotone finite stabilization

Status: `PROVED` for finite state spaces; executable checked.

Every `q_(t+1)` refines `q_t`. If the refinement is strict, the number of classes rises by at least one. Hence, writing `N=|X|` and `c_0` for the number of initial classes, there are at most

\[
\boxed{N-c_0}
\]

strict refinement rounds.

Therefore the process reaches a finite stable partition `q_*`.

### Proof

The first coordinate of `q_(t+1)` is `q_t`, so no previously distinguished states can merge. A strict refinement of a finite partition increases class count, which is bounded by `N`. ∎

## 5. P023-S4-T02 — Stable quotient preserves legality and targets

Status: `PROVED`; executable checked.

At stability, every declared partial operation descends through `q_*` with its domain preserved. Explicitly,

\[
q_*(x)=q_*(y)
\Longrightarrow
\left[
 x\in D_a\iff y\in D_a
\right]
\]

for every `a`, and when enabled,

\[
q_*(F_a(x))=q_*(F_a(y)).
\]

### Proof

At a fixed point, equal `q_*` classes have equal full one-step signatures. Equality of the enabled bit gives domain agreement; equality of the target-class coordinate gives target compatibility when enabled. ∎

## 6. P023-S4-T03 — Bounded legality-sensitive word semantics

Status: `PROVED`; executable checked exhaustively on finite small systems.

For a named action word

\[
w=a_1\cdots a_k,
\]

follow the partial maps from left to right. The word is **defined at `x`** exactly when every visited prefix is enabled. For every word of length at most `t`, record either

\[
(\mathrm{DEFINED},q_0(F_w(x)))
\]

when the full word is defined, or

\[
\mathrm{UNDEFINED}
\]

when some prefix is disabled.

Then

\[
\boxed{
q_t(x)=q_t(y)
\iff
\text{the two states have identical legality-sensitive observation signatures for all }|w|\le t.
}
\]

Because every prefix of a word of length at most `t` is itself among the words of length at most `t`, the signature also preserves the complete prefix-definedness language.

### Proof

Induct on `t`. At `t=0`, the signature is exactly `q_0`. The refinement step records the current class and, for each first generator, either disabledness or the previous-depth class of the reached state. By the induction hypothesis, that target class is exactly the remaining word signature through depth `t`. ∎

## 7. P023-S4-T04 — Coarsest compatible refinement

Status: `PROVED`; executable checked by exhaustive small finite partition enumeration.

Let `s:X->S` be any partition such that:

1. `s` refines `q_0`;
2. every partial operation descends through `s` with domain membership preserved.

Then `s` refines every `q_t`, hence `s` refines `q_*`.

Therefore

\[
\boxed{
q_*
\text{ is the coarsest refinement of }q_0
\text{ compatible with the declared partial operation family.}
}
\]

### Proof

Induct on `t`. If `s` refines `q_t`, equality under `s` gives equality of `q_t`, equal enabledness for every generator, and—when enabled—targets in the same `s`-class. The induction hypothesis applied to those targets gives equality of their `q_t` classes, so the full `q_(t+1)` signatures agree. ∎

## 8. P023-S4-T05 — Exact reduction to the total-operation case

Status: `PROVED`; executable checked exhaustively on all two-state two-generator total families used by the reference suite.

If every domain is all of `X`,

\[
D_a=X\qquad\text{for every }a,
\]

then every enabledness bit is constant. Removing those constant coordinates leaves exactly the canonical P023 total-family refinement

\[
q_{t+1}(x)
=
\left(q_t(x),(q_t(F_a(x)))_{a\in A}\right).
\]

Thus the partial-operation construction is a strict interface extension of the existing total-operation theory, not a replacement for it.

## 9. Distinguished-UNDEFINED totalization boundary

A partial family may be converted, for verification purposes, to a total family on

\[
X^\bot=X\sqcup\{\bot\}
\]

by sending every disabled transition to one absorbing `bot` state.

This verification construction reproduces the genuine partial quotient on the original states only when:

1. `bot` is absorbing for every action; and
2. its observation is explicitly distinguished from every ordinary state observation.

If the added sink is observationally identified with ordinary states, totalization can spuriously merge a state where an action is enabled with one where it is disabled.

Therefore:

\[
\boxed{
\text{verification sink}\neq\text{new ontic/world state assumption}.
}
\]

The canonical semantic interface remains the genuine partial map `F_a:D_a->X`.

## 10. Foundation interface consequence

FQ-006 extends the FQ-004 layering only when the declared future language contains guarded/partial actions:

\[
\boxed{
\text{typed state}
\to
\text{current observation kernel}
\to
\text{declared partial future language}
\to
\text{legality-sensitive future-signature kernel}.
}
\]

For total languages, this collapses exactly to the already-canonical P023/FQ-004 interface.

No application-specific legality law is made primitive. An application must declare its own action domains. The generic quotient merely states what information must be retained once those domains have been declared.

## 11. Prior-art and ownership boundary

The abstract machinery belongs to established finite partial-transition / automata / behavioral-equivalence / partition-refinement mathematics. P023 does not claim generic priority for it.

Ownership remains:

- FQ-004 / A1–A2: generic functional-kernel and declared-future layering;
- P023: quotient compatibility and coarsest safe refinement, now including partial deterministic families;
- P024 and application programs: special action languages and their exact domain/legality laws;
- A4: multivalued correspondence/support, not identified with one partial deterministic function family.

## 12. Executable reference and verification status

Canonical executable reference:

- `src/enterprise_math/partial_operation_quotient.py`
- `tests/test_partial_operation_quotient.py`

The regression suite checks bounded-word equivalence, finite stabilization, coarsest-compatible minimality, exact reduction to the total-operation implementation, distinguished absorbing-undefined totalization, and the failure of an undistinguished sink.

This supplement is **not Lean-checked**. `LEAN_CHECKED_MAIN` must not be inferred from the existence of the Python reference or from other P023 Lean modules.
