# P025 Supplement 141 — Cross-job helper caches require invalidation

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. A legal cache can become stale

Within one legally initialized computation, Stage 139 shows that saturated helper coordinates are deterministic derived cache.  This does **not** imply that the same cache may be retained after the raw input is replaced by a new job.

For the sequential k-way compiler, helper `e_j` represents the already-computed raw prefix

\[
a_1\wedge\cdots\wedge a_j.
\]

Fix any

\[
2\le j\le k-1.
\]

## 2. Exact stale-helper counterexample

Choose a prior raw job

\[
S_{old}=\{a_1,\ldots,a_j\}.
\]

Legal saturation generates `e_j`.

Now start a new raw job containing only the suffix

\[
S_{new}=\{a_{j+1},\ldots,a_k\},
\]

but retain stale helper `e_j` from the prior job.

The internal seed is therefore

\[
T=\{e_j\}\cup S_{new}.
\]

The sequential helper chain resumes from `e_j` and eventually derives

\[
z.
\]

But the new raw job omits all prefix antecedents `a_1,...,a_j`, so the pure raw conjunction must not fire:

\[
cl_{raw}(S_{new})=S_{new}.
\]

Hence

\[
\boxed{
\pi(F_{ext}^*(T))\ne cl_{raw}(S_{new}).
}
\]

Every helper has such a witness.

## 3. Exact fixed-reset lower bound

Suppose the lifecycle policy between arbitrary jobs is restricted to a fixed deletion set of helper coordinates, with no version tag or revalidation mechanism.

If some helper `e_j` is not cleared, the construction above chooses a prior job that makes it true and a next job whose suffix turns that stale value into a false output.

Therefore every helper must belong to the reset set:

\[
\boxed{
\text{minimum fixed helper-clear count}=k-2.
}
\]

Clearing all helpers is sufficient by the raw-initialization simulation theorem of Stage 138.

## 4. Initialization legality is not enough

Stage 138 required helpers to be absent at the beginning of a raw computation. Stage 141 shows that this condition is a **lifecycle invariant**, not merely a one-time startup convention.

Whenever raw inputs are replaced, the implementation must either

1. clear invalid helper state;
2. revalidate/recompute it against the new raw inputs; or
3. carry additional provenance/version information that prevents stale helpers from being consumed.

Thus legal hidden state requires a maintenance operation language.

## 5. Precision consequence

The full auxiliary-state contract now has at least three layers:

- **initialization precision** — which internal states are allowed initially;
- **runtime progress precision** — which transient helper states must remain distinct during one computation;
- **lifecycle validity precision** — which retained helpers remain valid after external/raw state changes.

A cache that is semantically redundant at one saturated endpoint can still impose future obligations on reset/invalidation operations.

## 6. Prior-art boundary

Cache invalidation, stale-state hazards, versioning and lifecycle invariants are classical systems ideas. No generic novelty claim is made. P025 contributes the exact finite counterexample family and places cache invalidation inside the same future-relative precision framework as state and operation legality.
