# P025 Supplement 24 — Exact Arbitrary-Support Pareto Profile from Radius-Level Absorption Drops

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 20–23; Stage-04 two-cost witness language  
Hard block: `NONE`

## 1. Closing the Stage-04 loop

Supplement 04 defined the fine witness cost

\[
C(x)=(\|x\|_\infty,\eta(x))
\]

and its Pareto frontier. Supplements 20–23 now provide exact compressed access to every additive state relevant to that language.

For each radius `r`, let `R_r` be the compressed additive reachable set from Supplement 23 and define

\[
\boxed{
E(r)=
\min\left\{
\frac{|av-bu|}{M}:
(u,v,u+v)\in\mathcal R_r,\ av-bu\ne0
\right\},
}
\]

whenever a nondegenerate state exists.

Here

\[
M=m(a)m(b)m(c).
\]

Thus `E(r)` is the best absorption redundancy available at geometric precision `r`.

## 2. P025-T70 — monotonicity and endpoints

By construction

\[
\mathcal R_r\subseteq\mathcal R_{r+1}.
\]

Therefore once defined,

\[
\boxed{E(r+1)\le E(r).}
\]

Supplement 23 gives the first defined radius:

\[
\boxed{r=\mu.}
\]

Supplement 22 gives the first radius attaining the arithmetic floor:

\[
\boxed{E(\nu)=\eta_{\min}.}
\]

Since `eta_min` is the global positive minimum, for every `r>=nu`,

\[
E(r)=\eta_{\min}.
\]

Hence all Pareto-relevant information lies in the finite integer interval

\[
\boxed{[\mu,\nu].}
\]

## 3. P025-T71 — strict drops are exactly the Pareto frontier

Define

\[
\boxed{
\mathcal P_{\rm drop}
=
\{(r,E(r)):
 r=\mu
\text{ or }
E(r)<E(r-1),
\ \mu\le r\le\nu\}.
}
\]

Then

\[
\boxed{
\mathcal P_{\rm drop}
=
\operatorname{Min}_{\preceq}
\{(\|x\|_\infty,\eta(x)):
 x\text{ nondegenerate additive witness}\}.
}
\]

### Proof

Fix radius `r`. Every witness of norm at most `r` has absorption at least `E(r)`, while by definition some compressed state attains `E(r)` and Supplement 20 supplies a fine representative at its exact minimum block cost.

If `E(r)=E(r-1)`, every cost pair first visible at radius `r` with absorption at least this value is dominated by the same absorption value already available at an earlier radius, so radius `r` contributes no new Pareto point.

If `E(r)<E(r-1)`, no witness of radius at most `r-1` can have absorption `E(r)`. Therefore any representative attaining `E(r)` must have exact global norm `r`, and `(r,E(r))` is nondominated.

Before `mu` there is no nondegenerate witness. After `nu`, `eta_min` has already been attained, so every later point is dominated by the first floor point. Thus the strict-drop graph is exactly the full Pareto frontier. ∎

## 4. P025-T72 — finite frontier cardinality bounds

Let

\[
E_0=E(\mu).
\]

Every frontier point uses a distinct radius in `[mu,nu]`, so

\[
|\mathcal P|
\le
\nu-\mu+1.
\]

Its absorption coordinates are strictly decreasing positive integers from `E_0` down to `eta_min`, so also

\[
|\mathcal P|
\le
E_0-\eta_{\min}+1.
\]

Hence

\[
\boxed{
|\mathcal P|
\le
\min\left(
\nu-\mu+1,
E(\mu)-\eta_{\min}+1
\right).
}
\]

This is an exact finite bound derived from the task coordinates themselves, not from the size of the fine witness lattice.

## 5. Examples

### `2+3=5`

\[
E(1)=2,
\qquad
E(2)=1.
\]

Thus

\[
\boxed{\mathcal P=\{(1,2),(2,1)\}.}
\]

### `2+7=9`

The exact profile is

\[
\boxed{
E(1),\ldots,E(5)
=(3,3,3,2,1).
}
\]

The strict drops occur at radii `1,4,5`, recovering

\[
\boxed{\mathcal P=\{(1,3),(4,2),(5,1)\}.}
\]

### `1+22=23`

\[
\boxed{
E(2),E(3),E(4),E(5)
=(2,2,2,1).
}
\]

Hence

\[
\boxed{\mathcal P=\{(2,2),(5,1)\}.}
\]

This is the Stage-14 squarefree access-delay tradeoff in compressed form.

### `25+704=729`

Here

\[
\mu=\nu=6,
\qquad
\eta_{\min}=6,
\]

so

\[
\boxed{\mathcal P=\{(6,6)\}.}
\]

### `1+512=513`

Likewise

\[
\mu=\nu=13,
\qquad
\eta_{\min}=3,
\]

and

\[
\boxed{\mathcal P=\{(13,3)\}.}
\]

## 6. Architectural consequence

The original infinite fine-lattice two-cost problem has now been compressed to a finite monotone integer response:

\[
\boxed{
\text{fine witness lattice}
\to
\mathcal R_r
\to
E(r)
\text{ on }[\mu,\nu]
\to
\text{strict-drop frontier}.
}
\]

For all rectangle queries

\[
\exists x:
\|x\|_\infty\le K,
\ \eta(x)\le H,
\]

the entire fine witness identity is unnecessary once this finite frontier is retained.

This is a concrete instance of P023 task-relative exact compression and A3/A4 antichain semantics; P025 does not claim a new generic Pareto theorem.

## 7. Executable assets

Added:

- `src/enterprise_math/abc_block_pareto_profile.py`
  - exact `E(r)` from compressed reachable states;
  - arbitrary-support radius profile on `[mu,nu]`;
  - strict-drop exact Pareto frontier;
  - finite cardinality bound;
  - cross-check against the earlier fine exact oracle.
- `tests/test_abc_block_pareto_profile.py`
  - exact Stage-04 frontiers;
  - squarefree access-delay profile;
  - singleton arbitrary-support examples;
  - fine/compressed agreement and cardinality bounds.

## 8. Next frontier

No hard block exists. Continue with:

1. seek low-radius / `mu=1` criteria for structured relation classes;
2. replace full reachable sets `V_n(r)` by task-minimal summaries where possible;
3. extend the radius profile from one absorption scalar to several simultaneous certificate costs;
4. compare compressed exact frontier bounds with Pasten's Geometry-of-Numbers sufficient witness bounds;
5. decide which Stage-18–24 results are P025-specific specializations versus candidates for reusable P023 tooling.
