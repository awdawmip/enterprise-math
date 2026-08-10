# P025 Supplement 107 — Quadratic Rank Observable Boundary

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonlinear-observable-stage107`  
Depends on: P025 Supplements 97, 106  
Hard block: `NONE`

## 1. Why change the observable

Stages 101–106 establish a clean state/operation precision split for the linear activation-area observable. In particular, refining endpoint semantics to full trace semantics can refine the operation-word quotient without refining the compact state generator.

Stage 107 asks whether that behavior survives when the **observable itself** is strengthened.

Keep the same ordered threshold incidence geometry, but replace activation area by the nonlinear column-rank energy

\[
\boxed{
E:=\sum_j r_j^2,
}
\]

where

\[
r_j:=\#\{k:\rho_j\ge T_k\}.
\]

## 2. Area versus quadratic energy

The linear area is

\[
A=\sum_j r_j.
\]

Thus area retains only the first moment of the column-rank distribution.

Quadratic energy retains

\[
E=\sum_jr_j^2,
\]

which is sensitive to concentration of the same total rank mass.

Therefore equal area does not in general imply equal energy.

## 3. P025-CE42 — exact arithmetic observable collision

Use the same fixed threshold grid

\[
T=\left(\frac12,1\right)
\]

and the two exact P025 dyadic pressure states already encountered in the Stage97 area collision.

### Flat orbit

For `(q,p,m)=(3,5,2)` through exponents `2,4`, the pressure values are

\[
\left(\frac12,\frac12\right).
\]

Hence the column ranks are

\[
\boxed{(1,1)}
\]

and

\[
A=2,
\qquad
E=1^2+1^2=2.
\]

### Jump orbit

For `(q,p,m)=(7,17,2)`, the pressure values are

\[
\left(\frac16,\frac{13}{6}\right).
\]

Hence the column ranks are

\[
\boxed{(0,2)}
\]

and

\[
A=2,
\qquad
E=0^2+2^2=4.
\]

Therefore

\[
\boxed{
A_{\rm flat}=A_{\rm jump}=2,
\qquad
E_{\rm flat}=2\ne4=E_{\rm jump}.
}
\]

## 4. P025-T245 — an area-sufficient state can fail for a stronger observable

The two states are merged by the scalar area coordinate but separated by the quadratic-energy future.

Hence any quotient that retains only the area distinction is not sufficient for a future language that asks for `E`.

In particular,

\[
\boxed{
\text{observable refinement can force state refinement}.
}
\]

This is the exact complement of Stage106, where a language refinement from endpoint to trace did not force state refinement.

## 5. The two axes of future refinement

Stages106–107 expose two logically independent mechanisms.

### Operation-semantic refinement

Endpoint area -> full area trace:

- compact state generator can stay fixed;
- operation-word quotient must become finer.

### Observable refinement

Area -> quadratic rank energy:

- operation language may remain unchanged;
- state quotient must become finer because equal-area states can have different energy.

Thus the slogan

> richer future means finer state

is false without specifying which future axis changed.

## 6. Architectural consequence

A future-compatible precision architecture should treat at least three declared objects separately:

1. **state observable family** — what functions of the current/future state must be predicted;
2. **operation language** — which actions/words may be applied;
3. **observation semantics** — endpoint only or intermediate trace.

Precision can be forced onto different components depending on which declaration is strengthened.

## 7. Prior-art / novelty boundary

Moments, quadratic energies and the fact that equal first moments need not determine second moments are elementary prior mathematics. P025 claims none of these facts in isolation.

The project-side result is the exact arithmetic pressure-test collision showing that observable refinement and trace refinement act on different precision components. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/abc_quadratic_rank_energy.py`;
- `tests/test_abc_quadratic_rank_energy.py`.

## 9. Next frontier

Stage108 will compute the exact finite-action response polynomial of `E`. The main pressure test is whether Stage102's second-order history closure survives this nonlinear observable or whether genuine third-order action interaction appears.