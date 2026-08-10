# Trace Answer to Executable State: Continuation Closure

Status: `RESEARCH BRIDGE / NONCANONICAL`

A state representation can be sufficient to answer every declared terminal query while still being too coarse to continue executing the declared future transition language. This note isolates the exact repair law.

## 1. Stable-state closure operator

Fix a finite state set, relation family, coefficient semiring K, and initial observation partition `P_0`.

Let

`C_K(P)`

be the unique coarsest K-weighted transition-stable refinement of partition P.

Write

`E = C_K(P_0)`.

E is the minimal executable K-branching state below the initial observation.

## 2. Interval absorption theorem

Let T be any intermediate partition satisfying

`E refines T refines P_0`.

Then

`C_K(T)=E`.

Proof:

- E is K-stable and refines T, so by coarseness of `C_K(T)`, E refines `C_K(T)`;
- `C_K(T)` is K-stable and refines `P_0`, so by coarseness of `E=C_K(P_0)`, `C_K(T)` refines E.

Hence equality.

So once the declared transition interface is fixed, every underresolved intermediate readout in the interval repairs to the same canonical executable state.

## 3. Terminal trace answers are canonical intermediate partitions

A K-branching signature deterministically projects to all terminal K-valued word traces. Therefore

`E_branching refines T_trace`.

The empty word retains the current observation, so

`T_trace refines P_0`.

Hence the interval theorem applies:

`C_K(T_trace)=E_branching`.

Thus the coarsest transition-stable refinement of a complete terminal-trace answer is exactly the original minimal branching state.

## 4. Sufficient answer is not sufficient state

This gives a precise distinction:

- **answer precision**: enough information to answer the declared terminal queries now;
- **state precision**: enough information for the declared transition interface to remain executable and recursively usable after the answer is produced.

The second can be strictly finer.

## 5. Continuation debt

Define

`continuation debt = #blocks(E_branching) - #blocks(T_answer)`

for any answer partition in the interval.

This is the additional state distinction required solely because the representation must support future continuation rather than one-shot readout.

The branch also records the number of strict repair rounds from the answer partition back to the stable state.

## 6. Boolean support choice-timing witness

Use the six-state structure

`p = a.(b+c)`

versus

`q = a.b + a.c`.

Complete terminal Boolean-support traces merge p/q, because every literal word has the same terminal support.

Support-stable branching state separates them because the timing/location of the b/c choice is future-executable structure.

The answer partition therefore has positive continuation debt; one extra block and one repair round recover the executable state.

## 7. Exact natural-count correlation witness

Use the count-correlation fixture in which p/q have identical terminal natural path-count traces but different multisets of successor future-count types.

Again the terminal answer merges p/q while exact count-branching state separates them.

So continuation debt is not specific to Boolean support or choice timing; it also occurs when terminal summation loses successor count correlation.

## 8. No debt when the answer is already stable

If T itself is K-stable, then `C_K(T)=T`. Since T lies between E and P_0, interval absorption forces T=E.

Therefore continuation debt is zero exactly when the supplied answer representation is already a valid executable K-state.

## 9. Closure-operator interpretation

The map `C_K` behaves as a closure-to-stability operator on partitions ordered by refinement, with the direction adapted to the project's convention that finer partitions carry more state detail.

The interval theorem says that after the canonical stable state E has been determined, every coarser intermediate readout between E and the original observation lies in the same basin of continuation repair.

This is stronger than a trace-specific theorem.

## 10. Semantic-precision consequence

When a future language is declared, asking only

`what answers can this quotient return?`

is insufficient to determine whether that quotient is a reusable state.

One must also ask

`does the declared future operation still descend on this answer partition?`

If not, canonical semantic repair reintroduces exactly the continuation distinctions encoded by E.

## Owner-local assets

- `src/enterprise_math/relation_trace_to_state_closure.py`;
- `tests/test_relation_trace_to_state_closure.py`;
- `docs/PRECISION_TRACE_TO_STATE_CONTINUATION_CLOSURE.{en,zh}.md`.

Regression includes the Boolean choice-timing witness, exact-count correlation witness, zero-debt case, partition-order validation, and exhaustive four-state interval absorption checks.

## Prior art / status

Closure operators, congruence refinement, bisimulation/trace distinctions and automata minimization are standard prior mathematics/CS. A4 retains relation/witness ownership; P023/A2 retains future-signature and semantic-precision ownership. This Draft owns only the explicit answer-to-state continuation-repair specialization.

No canonical-main or new `EXECUTABLE_CHECKED` claim. Hard block: `NONE`.