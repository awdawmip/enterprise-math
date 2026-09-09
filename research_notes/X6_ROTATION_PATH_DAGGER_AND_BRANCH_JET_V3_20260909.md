# X6 rotation paths: dagger-category correction and the first lossless branch jet

Status: `FREE_RESEARCH / EXACT TYPE CORRECTION + FINITE JET CLASSIFICATION / NOT_FOUNDATION`
Date: `2026-09-09`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent line: `#1255`, consuming `X6_ROTATION_PATH_GROUPOID_V2_20260906.md` and `X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`
Checker: `experiments/x6_rotation_path_dagger_jet_20260909/check_rotation_path_dagger_jet.py`
Checker commit: `1d782f657f6f9f2dfacd28d73a4f9cc9c7562eea`

## 1. Concrete-history-preserving rotation paths are not a groupoid

Let a rotation-path arrow from a native Cell `x` be `(g,gamma)`, where `g` is a typed signed frame action and `gamma` is the **concrete primitive Cell path** from `x` to `g x`. Composition is literal path concatenation.

If path history is retained as the note V2 requires, then reversing a path does not give a categorical inverse. For a nonempty path `gamma`,

`gamma ; reverse(gamma)`

is a nonempty backtracking loop. It is not the empty identity path under literal path equality. Therefore the simultaneously asserted pair

- concrete path history survives composition, and
- `reverse(gamma)` is a true categorical inverse

is inconsistent unless an additional cancellation/homotopy quotient is explicitly imposed.

The correct provenance-preserving type is a **dagger/path category**:

- objects: native X6 Cells;
- arrows: concrete typed rotation paths `(g,gamma)`;
- composition: literal concatenation;
- identity: empty path;
- dagger: `(g,gamma)^dagger=(g^{-1},reverse(gamma))`.

Then dagger is involutive and reverses composition, but generally

`f^dagger o f != id`.

Freeze at this research strength:

`CONCRETE_PATH_REVERSAL = DAGGER / INVOLUTION`.

`CONCRETE_PATH_REVERSAL != CATEGORICAL_INVERSE WITHOUT AN EXPLICIT CANCELLATION QUOTIENT`.

This is a type correction, not a rejection of the useful V2 path carrier. The frame/action groupoid remains a valid quotient when path history is deliberately erased under an appropriate observer lease.

## 2. Exact noncommutative discrete path jets

For a primitive-step path

`gamma=(s_1,...,s_M)`

with signed native-axis steps, define

\[
S_k(\gamma)
=\sum_{1\le r_1<\cdots<r_k\le M}
 s_{r_1}\otimes\cdots\otimes s_{r_k},
\qquad S_0(\gamma)=1.
\]

For literal concatenation `gamma delta`, the ordered-index split is exact:

\[
\boxed{
S_n(\gamma\delta)
=\sum_{p+q=n} S_p(\gamma)\otimes S_q(\delta).
}
\]

Thus the truncated tuple

\[
J_{\le d}(\gamma)=(S_0,S_1,\ldots,S_d)
\]

has an exact finite composition law. No continuous interpolation, logarithm, or imported signature theorem is needed for this finite identity.

## 3. BRC population: one complete triadic frame cycle

Fix one intrinsic triadic signed-C6 generator `Q_S`. Its six macro edges each have exactly two shortest native lifts, INNER or OUTER. The concatenated-shortest population for one complete frame cycle therefore has

\[
2^6=64
\]

labeled branch words

\[
\beta=(\beta_0,\ldots,\beta_5)\in\{I,O\}^6.
\]

This population retains branch identity and ordered native steps exactly as required by the current P000/BRC provenance contract.

## 4. Exact first-lossless jet threshold on the 64-word population

The exhaustive integer checker gives the exact class census

\[
\boxed{
\#J_{\le1}=1,\qquad
\#J_{\le2}=27,\qquad
\#J_{\le3}=64.
}
\]

Hence degree three is the first lossless truncation among degrees one, two and three for this declared finite population.

Degree two has a particularly transparent residual. It identifies a branch word exactly through the three antipodal-pair counts

\[
n_r=\mathbf 1_{\beta_r=O}+\mathbf 1_{\beta_{r+3}=O}
\in\{0,1,2\},
\qquad r=0,1,2.
\]

Therefore

\[
\boxed{
J_{\le2}\text{ has exactly }3^3=27\text{ fibers on the 64 shortest cycle words.}
}
\]

It remembers how many OUTER choices occur in each antipodal macro-edge pair but forgets which member of the pair carried the OUTER choice.

By contrast,

\[
\boxed{
J_{\le3}\text{ is injective on all }64\text{ branch words.}
}
\]

## 5. Relation to the antisymmetric area summary

The simpler second-order state

\[
d=\sum_r s_r,
\qquad
A=\sum_{r<t}s_r\wedge s_t
\]

has the exact concatenation law

\[
(M,d,A)\star(N,e,B)
=(M+N,d+e,A+B+d\wedge e).
\]

It distinguishes the two local shortest paths between one pair of macro endpoints and separates the all-INNER from all-OUTER full cycle. But on the full 64-word cycle population it has the same essential second-order loss: it cannot recover all six branch bits.

So a second-order area coordinate is useful but not sufficient for arbitrary future branch inspection on this population.

## 6. Exact observer lease

BRC resolution:

`REUSE_APPLIED = LABELED BRANCH POPULATION + OBSERVER/FUTURE-OPERATION FACTORIZATION TEST`.

- If future operations ask only for outputs known to factor through `J_{<=2}`, the 27-class quotient may be used.
- If future operations may recover the six INNER/OUTER branch labels for one shortest six-edge cycle, degree two is unsafe and degree three is sufficient.
- No claim is made that degree three is sufficient for arbitrary path lengths, arbitrary concatenations, arbitrary frame words, or the full unbounded rotation-path category.

This last point is the next exact research problem.

## 7. Durable frontier for handoff

Do not redo:

1. the V2 provenance-preserving concrete path carrier itself;
2. the exact two-branch shortest macro-edge result;
3. the 64-word full-cycle population;
4. the present dagger correction;
5. the exact `1 / 27 / 64` jet census.

Next smallest units are:

- formalize/audit the dagger-category correction and retype any consumer that requires true inverses;
- determine whether a fixed finite jet order can be operation-safe for longer/all rotation paths, or prove a growing-order/no-finite-order obstruction;
- characterize the smallest composition-safe observer for the root-compatible all-OUTER law versus the full BRC path population.
