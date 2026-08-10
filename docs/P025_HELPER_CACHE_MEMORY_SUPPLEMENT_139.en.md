# P025 Supplement 139 — Auxiliary helper state is endpoint cache but runtime memory

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. Legal saturated section

Use the legal raw initialization contract from Stage 138. Let `C_raw` be the set of raw states already closed under the pure k-way conjunction law, and let the sequential helper compiler run to saturation from each raw closed state with all helpers initially absent.

Define

\[
H:C_{raw}\to X_{ext}^{sat}
\]

by this legal saturation.

For every raw closed state `X`,

\[
\boxed{\pi(H(X))=X.}
\]

Therefore `H` is injective. Consequently

\[
\boxed{
|\operatorname{im}H|=|C_{raw}|.
}
\]

On the legal saturated endpoint space, helper coordinates add **no new semantic state distinctions** beyond the raw closed state. They are deterministic derived cache coordinates.

This is stronger than merely saying the raw projection is correct: the legal saturated internal state is a section over the raw semantic state.

## 2. Transient collision under raw projection

Now change the future language from saturated endpoint to stepwise execution.

For the four-way sequential compiler

\[
a_1a_2\Rightarrow e_2,
\qquad e_2a_3\Rightarrow e_3,
\qquad e_3a_4\Rightarrow z,
\]

start from

\[
S=\{a_1,a_2,a_3\},
\]

leaving `a_4` absent. The raw projection never changes, but the internal trace contains

\[
T_1=\{a_1,a_2,a_3,e_2\}
\]

and

\[
T_2=\{a_1,a_2,a_3,e_2,e_3\}.
\]

They satisfy

\[
\boxed{\pi(T_1)=\pi(T_2)=S,}
\]

but their runtime futures differ:

- from `T_1`, the next parallel step adds `e_3`;
- `T_2` is already stable because `a_4` is absent.

Thus raw projection is not future-safe for the stepwise internal language.

## 3. Cache/memory phase boundary

The same helper coordinate can therefore have two statuses depending on the declared future:

### Saturated endpoint future

`H(X)` is functionally determined by raw closed `X`. Helper state is cache and can be quotiented away without losing endpoint semantics.

### Stepwise/runtime future

Transient helper progress changes the next enabled update, remaining derivation depth, and internal trace. Helper state is genuine runtime memory and cannot be quotiented away by raw projection.

Hence

\[
\boxed{
\text{cache versus memory is future-language-relative, not coordinate-intrinsic.}
}
\]

## 4. Precision consequence

Auxiliary-state dimension alone does not say how much **semantic precision** it contributes. One must ask whether those coordinates are

- deterministic functions of the visible state at the declared endpoint;
- or independent progress/history coordinates for the declared runtime future.

This gives an exact finite example where a coordinate contributes zero endpoint-state refinement but nonzero runtime-state refinement.

## 5. Prior-art boundary

Derived caches, sufficient state, hidden execution progress and refinement maps are standard computer-science/control ideas. P025 claims no generic novelty. The project-side result is the exact future-relative phase boundary linking Stage138 legality to state-precision accounting.
