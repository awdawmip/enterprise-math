# P025 Supplement 91 — Dyadic First-Activation Normal Form

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplements 86, 90  
Hard block: `NONE`

## 1. Frozen input from Stage 86

Fix distinct odd primes

\[
3\le q<p
\]

and a base exponent

\[
m\ge2.
\]

For the dyadic difference orbit define

\[
e_j:=2^j m,
\qquad
\rho_j:=\rho_{e_j,-}.
\]

Stage 86 proves the exact recurrence

\[
\boxed{
\rho_{j+1}
=ho_j u_j,
\qquad
u_j:=m(p^{e_j}+q^{e_j})\in\mathbf N_{\ge1}.
}
\]

Hence

\[
\boxed{ho_0\le\rho_1\le\rho_2\le\cdots.}
\]

Stage 91 asks what this monotonicity means for finite precision.

## 2. P025-D34 — threshold activation profile

Fix a future threshold

\[
T>0
\]

and a finite dyadic horizon

\[
0\le j\le h.
\]

Define the Boolean activation profile

\[
\boxed{
a_j(T):=\mathbf1_{\{\rho_j\ge T\}}.}
\]

Without using the transport theorem, this would appear to be an arbitrary Boolean word of length `h+1`.

## 3. P025-T206 — every dyadic activation profile is a suffix

Because the pressure sequence is nondecreasing,

\[
\rho_j\ge T
\Longrightarrow
\rho_{j+1}\ge T.
\]

Therefore

\[
\boxed{
a_j(T)\le a_{j+1}(T).}
\]

So every finite activation profile has the form

\[
\boxed{00\cdots0011\cdots11.}
\]

There can be at most one threshold-crossing transition.

## 4. P025-D35 — first activation depth

Define

\[
\boxed{
j_T:=\min\{j\in\{0,\ldots,h\}:\rho_j\ge T\},}
\]

when the set is nonempty, and write

\[
\boxed{j_T=\infty}
\]

when the threshold is not reached inside the finite horizon.

Then P025-T206 gives the exact reconstruction rule

\[
\boxed{
a_j(T)=1\iff j\ge j_T,}
\]

with the convention that no finite `j` exceeds infinity.

Thus `j_T` is a complete normal form for the threshold activation profile.

## 5. P025-T207 — exact finite state-space collapse

An unconstrained Boolean profile of length `h+1` has

\[
2^{h+1}
\]

possible states.

An upward-closed suffix profile is determined by one of

\[
0,1,\ldots,h,\infty.
\]

Hence only

\[
\boxed{h+2}
\]

profiles are compatible with dyadic pressure transport.

Therefore the transport theorem collapses the semantic threshold-profile state space from

\[
\boxed{2^{h+1}}
\]

to

\[
\boxed{h+2.}
\]

This is an exact combinatorial reduction, not an asymptotic heuristic.

## 6. P025-T208 — cumulative multiplier formula

Iterating the Stage-86 recurrence gives

\[
\boxed{
\rho_j
=ho_0
\prod_{i=0}^{j-1}u_i.
}
\]

Thus

\[
\boxed{
j_T
=
\min\left\{
0\le j\le h:
\rho_0\prod_{i<j}u_i\ge T
\right\}.}
\]

The first-activation depth is therefore a first-passage index for a cumulative product of positive integer residual multipliers.

Taking logarithms turns this into a monotone additive resource accumulation problem.

## 7. Exact nontrivial crossing fixture

Take

\[
(q,p)=(3,41),
\qquad m=2.
\]

For exponents

\[
2,4,8,16
\]

the exact difference pressures are

\[
\boxed{
\frac1{22},
\frac{13}{22},
\frac{221}{22},
\frac{221}{22}.
}
\]

At threshold

\[
T=1,
\]

the activation profile is

\[
\boxed{(0,0,1,1),}
\]

so

\[
\boxed{j_1=2.}
\]

This shows that the normal form is not restricted to the trivial boundary cases `j_T=0` or `infinity`.

## 8. Boundary fixtures

### Already active

For

\[
(q,p,m)=(23,41,2),
\]

Stage 82 gives

\[
\rho_{2,-}=\frac32>1.
\]

Hence every finite dyadic descendant is active and

\[
\boxed{j_1=0.}
\]

### No activation on the tested horizon

For

\[
(q,p,m)=(3,5,2),
\]

the finite pressures at exponents `2,4,8,16` remain `1/2`, so on that horizon

\[
\boxed{j_1=\infty.}
\]

This is a finite-horizon statement only; Stage 91 does not infer the infinite tower from a finite computation.

## 9. P025-T209 — active signed seed bounds the crossing depth

Stage 86 also proves

\[
\rho_{2m,-}
\ge
\max\{\rho_{m,-},\rho_{m,+}\}.
\]

Therefore, for any threshold `T`:

- if `rho_{m,-}>=T`, then
  \[
  \boxed{j_T=0;}
  \]
- if `rho_{m,+}>=T` while `rho_{m,-}<T`, then
  \[
  \boxed{j_T\le1.}
  \]

So an active sum state is an immediate one-step certificate that the associated difference dyadic orbit enters the active basin no later than the next node.

For example, `(q,p,m)=(5,59,3)` has active cube-sum pressure but subunit cube-difference pressure; the doubled difference state is nevertheless active.

## 10. P025-T210 — first activation depth is future-relative

The orbit is fixed, but `j_T` depends on the declared threshold.

For the `(3,41,2)` fixture:

- `T=1`: `j_T=2`;
- `T=10`: `j_T=2`;
- `T=11`: the threshold is not reached through exponent `16`.

Thus the normal form is not an intrinsic label of the orbit alone. It is a function of the future query.

This is the orbit-level analogue of Stage 90's edge-level future-relative precision.

## 11. Semantic versus exact orbit state

For the future query

> which depths up to `h` satisfy `rho_j>=T`?

`j_T` is sufficient and exact.

For the stronger future query

> what is every exact pressure `rho_j`?

`j_T` is insufficient. One must retain the base pressure and enough cumulative multiplier information.

So the same dyadic orbit again has a natural precision ladder:

\[
\boxed{
(\rho_0,u_0,\ldots,u_{h-1})
\longrightarrow
j_T
\longrightarrow
\text{one selected activation bit}.
}
\]

The correct collapse depends on the future language.

## 12. Architectural meaning

Stage 91 converts deterministic monotone transport into a finite orbit normal form.

The important reusable mechanism is:

\[
\boxed{
\text{monotone refinement orbit}
+
\text{threshold future}
\Longrightarrow
\text{first-passage precision}.
}
\]

A system should not store a full history of redundant threshold bits when the transition theorem forces them to be an upward-closed suffix.

This is stronger than merely deduplicating dyadic descendants: it identifies the exact semantic coordinate needed by the threshold future.

## 13. Prior-art / novelty discipline

Monotone Boolean sequences, first-passage indices and threshold-crossing compression are elementary/general prior concepts.

P025 claims none of those concepts in isolation.

The project-side result is their exact instantiation from the signed arithmetic pressure law of Stage 86, together with executable number-theoretic fixtures and the future-relative precision interpretation. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 14. Executable assets

Added:

- `src/enterprise_math/abc_dyadic_activation_normal.py`;
- `tests/test_abc_dyadic_activation_normal.py`.

The executable layer verifies suffix reconstruction, exact first crossings, boundary normal forms, finite state-space reduction, threshold dependence and the active-sum one-step bound.

## 15. Next frontier

No hard block exists. Continue with:

1. replace one threshold by an ordered finite family and compress the entire activation matrix into a monotone crossing-depth staircase;
2. quantify that multi-threshold state-space reduction exactly;
3. determine the minimal state for mixed queries involving both threshold activation and exact pressure at selected nodes;
4. combine the dyadic normal form with odd-prime Hasse cover labels from Stage 89;
5. use the result to define an exponent-transport orbit normal form rather than a table of descendant states.
