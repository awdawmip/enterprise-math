# P023 / A2 — Adaptive Acquisition and Process Precision, v3

Status: `PROVED OWNER RESEARCH`  
Owner: A2 future-compatible quotient  
Depends on: A2 Precision Incidence Core v3, A2 Conditional Scheduling Core v3, P011 collision-spectrum calculus  
Discipline: deterministic decision trees, ordered decision diagrams, Kraft-type capacity bounds, direct-sum arguments, and partition kernels are established mathematics. The project-specific role is the exact integer repair-cost interface and its integration with future-safe precision.

## 1. Final precision is not acquisition complexity

Let `X` be finite nonempty, `T:X->Z` the final target, and `Q={q_i:X->A_i}` a finite primitive query language. Fix an integer alphabet base `B>=2`.

On a current compatible block `C`, a query realizes `r=|q(C)|` answers and costs

\[
\boxed{c_B(q\mid C)=L_B(r),\qquad L_B(r)=\min\{\ell:r\le B^\ell\}.}
\]

A query constant on `C` costs zero. The target is solved exactly when `T` is constant on `C`.

The central distinction is

\[
\boxed{\text{answer precision}\preceq\text{strategy-transcript precision}\preceq\text{all-tools language-safe precision}.}
\]

## 2. A2-AA-T01 — All-tools language-safe quotient

Define

\[
\boxed{E_{T,\mathcal Q}=\ker T\cap\bigcap_{q\in\mathcal Q}\ker q.}
\]

This is the coarsest static quotient through which the target and **every allowed query** descend. The acquisition problem is unchanged after replacing `X` by `X/E_{T,Q}`: every reachable query-answer block is a union of full signature classes, and duplicate raw states inside one signature do not change realized query values or target constancy.

Hence

\[
\boxed{E_{T,\mathcal Q}=\ker T\iff\text{every primitive query factors through the target}.}
\]

If this fails, final answer precision is too coarse to simulate the full primitive tool language.

## 3. Eager global state versus lazy local refinement

`E_{T,Q}` is eager: it preserves every query everywhere. An adaptive strategy is lazy. At a typed context block `C` it uses only one local map `q|_C:C->q(C)`; different branches may invoke different future queries.

Thus a chosen strategy need not materialize the full Cartesian query signature. Global factorization remains the correct condition for one static state supporting the **entire** language; branch-local acquisition only needs the query actually invoked on that context.

## 4. A2-AA-T02 — Strategy transcript sandwich

For an exact deterministic strategy `S`, let `Tr_S(x)` be the terminal sequence of queried names and returned values and put `E_S=ker(Tr_S)`. Then

\[
\boxed{E_{T,\mathcal Q}\subseteq E_S\subseteq\ker T.}
\]

The left inclusion holds because states with the same complete target/query signature force the same deterministic path. The right inclusion holds because exactness makes the target a function of the terminal transcript.

So a strategy chooses an intermediate quotient between all available process detail and the final answer.

## 5. Proof-transcript repair spectrum

For a target value `z`, let

\[
r_S(z)=\#\{\text{terminal transcripts ending with answer }z\}.
\]

Define

\[
\boxed{\mathcal P_k(S)=\sum_z\binom{r_S(z)}k.}
\]

This is exactly the P011 collision spectrum of the final forgetting map `transcript -> answer`; binomial inversion therefore recovers the complete local proof-multiplicity distribution.

If every primitive query descends through `T`, then `E_{T,Q}=ker T`, and the sandwich forces `E_S=ker T` for any exact strategy that stops when the target is decided. In that case every answer has one transcript class.

## 6. A2-AA-T03 — Exact adaptive Bellman recurrence

For compatible block `C` and remaining queries `R`, let `A_B(C,R)` be minimum worst-case future symbol cost. If `T` is constant on `C`, it is zero. Otherwise

\[
\boxed{
A_B(C,R)=\min_{q\in R,\ |q(C)|>1}
\left[L_B(|q(C)|)+\max_{a\in q(C)}A_B(C\cap q^{-1}(a),R\setminus\{q\})\right].
}
\]

If no query path decides the target, the value is infinite/undefined. This is the exact finite acquisition compiler; no probability or expected cost is used.

## 7. A2-AA-T04 — Integer capacity lower bound

Let an exact strategy have worst cost `d`, and let a terminal leaf `lambda` have path cost `c(lambda)`. Local answer symbols concatenate to a prefix code, giving the integer Kraft-capacity inequality

\[
\boxed{\sum_\lambda B^{d-c(\lambda)}\le B^d.}
\]

Thus the number of terminal transcripts is at most `B^d`; since each exact leaf has one target answer,

\[
\boxed{A_B(T;\mathcal Q)\ge L_B(|T(X)|).}
\]

## 8. Two independent acquisition defects

Write `N_ans=|T(X)|` and `N_tr=|Tr_S(X)|`. Then

\[
\boxed{
d-L_B(N_{\rm ans})=
\underbrace{d-L_B(N_{\rm tr})}_{\text{tree/radix packing slack}}+
\underbrace{L_B(N_{\rm tr})-L_B(N_{\rm ans})}_{\text{transcript multiplicity slack}}.}
\]

Both terms can be independently nonzero.

A four-state identity target with three singleton binary tests has `N_ans=N_tr=4` but requires depth `3`: pure tree-packing slack `1`.

Conversely, with

`T=(0,0,1,1)`, `Q1=(0,1,0,1)`, `Q2=(0,1,1,0)`,

the target is the equality/XOR relation of the two query answers. Both queries are required, yielding four transcripts for two answers. Tree packing is tight at depth `2`, while transcript multiplicity contributes one full binary depth and has spectrum `(4,2)`.

## 9. A2-AA-T05 — Presentation sensitivity

In the preceding four-state system, `(Q1,Q2)` already generates the exact four-state query partition. Add the bundled query `QT=T`. Since `T` is already a function of `(Q1,Q2)`, this adds no new information class to the generated query partition, but acquisition cost drops from `2` to `1`.

Therefore

\[
\boxed{\text{same generated precision relation}\not\Rightarrow\text{same acquisition complexity}.}
\]

A query can be partition-redundant but algorithmically valuable. Primitive query presentation and precision closure are different resources.

## 10. Requirement and tool languages have opposite monotonicities

If `T'` is finer than `T`, then

\[
\boxed{A_B(T';\mathcal Q)\ge A_B(T;\mathcal Q).}
\]

If `Q subseteq Q'`, then

\[
\boxed{A_B(T;\mathcal Q')\le A_B(T;\mathcal Q).}
\]

So richer **requirement language** can only demand more distinction, whereas richer **tool language** can only make acquisition cheaper or equal. If the direct target query is available,

\[
\boxed{A_B(T;\mathcal Q\cup\{T\})=L_B(|T(X)|).}
\]

## 11. A2-AA-T06 — Adaptive / ordered / synchronous hierarchy

Three models must be separated:

1. **adaptive** — next query may depend freely on the current transcript;
2. **ordered interactive** — one global query order is fixed, but each branch may skip queries and stop early;
3. **stage-synchronous** — one global stage order is fixed, and a used query stage is exposed to every unresolved context with an alphabet large enough for the largest local branch count.

For the same finite target/query system,

\[
\boxed{L_B(|T(X)|)\le A_{\rm adaptive}\le A_{\rm ordered}\le A_{\rm stage}.}
\]

Every inequality can be strict, but different finite witnesses expose different defects.

## 12. A2-AA-C01 — True adaptive-order separation

On the Boolean cube `(x0,x1,x2,x3) in {0,1}^4`, define

\[
f=\begin{cases}
1-x_1,&x_0=0,x_2=0,\\
1-x_3,&x_0=0,x_2=1,\\
1-x_2,&x_0=1,x_1=0,\\
1-x_3,&x_0=1,x_1=1.
\end{cases}
\]

An adaptive depth-3 tree asks `x0`; on `x0=0` it asks `x2` then `x1` or `x3`; on `x0=1` it asks `x1` then `x2` or `x3`. A size-three certificate exists, so depth two is impossible.

No fixed variable order attains depth three. If `x0` is first, the `x0=0` restriction forces selector `x2` before both `x1,x3`, while the `x0=1` restriction forces selector `x1` before both `x2,x3`; one remaining global order cannot satisfy both. If `x1`, `x2`, or `x3` is first, one restriction leaves a three-variable decision-depth-three subfunction. Hence

\[
\boxed{A_{\rm adaptive}=3<A_{\rm ordered}=4.}
\]

Four binary variables are minimal: with at most three variables, adaptive depth three already equals querying all variables, while a depth-two tree can always be linearized by placing the root variable first and the branch-specific second variables later with skips.

## 13. A2-AA-C02 — Storage lower bound can be strict

For four target states with singleton tests

`A=(0,0,0,1)`, `B=(0,0,1,0)`, `C=(0,1,0,0)`,

the joint target has four classes, so binary storage depth is `2`. Every first query splits the target classes `1+3`, so no capacity-tight half split exists and an exact adaptive strategy needs depth `3`:

\[
\boxed{2=L_2(4)<A_{\rm adaptive}=3.}
\]

All queries descend through the target here; this is pure tree-packing overhead.

## 14. A2-AA-T07 — Capacity-tight balanced splitter criterion

Assume every query descends through the target and a current block contains exactly `B^d` target classes. Adaptive acquisition attains the storage lower bound `d` iff there is a recursive tree such that every node with `B^e` target classes uses a query with exactly `B^ell` realized answers and every child contains exactly `B^(e-ell)` target classes.

Necessity follows because each child can hold at most `B^(e-ell)` classes by T04 and there are at most `B^ell` children; equality of total capacity forces every inequality to be equality. Sufficiency follows by concatenating the exact local radix codes.

For binary queries this means every used query must split the currently possible target classes exactly in half.

## 15. A2-AA-C03 — Ordered interactive and stage-synchronous differ

Take eight states with

`A=(0,1,2,3,4,5,5,5)`,
`B=(0,1,1,1,2,3,4,5)`,
`C=(0,0,0,0,1,1,1,1)`,

and target `(A,B,C)`. Ordered interactive `C,A,B` can skip the irrelevant middle query branch-locally: on `C=0`, `A` determines `B`; on `C=1`, `B` determines `A`. Thus adaptive and ordered costs are both `3`.

A synchronous stage schedule cannot select different second-stage queries in the two contexts; its optimum is `5`:

\[
\boxed{A_{\rm ordered}=3<A_{\rm stage}=5.}
\]

This corrects an earlier over-strong interpretation that had mistaken non-skippable order for standard ordered interaction.

## 16. A2-AA-T08 — Adaptive direct sum

For product systems `(X1,T1,Q1)` and `(X2,T2,Q2)`, let `X=X1 x X2`, `T=(T1,T2)`, and allow only component-local lifted queries. Then

\[
\boxed{A_B(X,T;\mathcal Q_1\sqcup\mathcal Q_2)=A_B(X_1,T_1;\mathcal Q_1)+A_B(X_2,T_2;\mathcal Q_2).}
\]

Every reachable block is a rectangle `C1 x C2`. The sum of the two component Bellman values satisfies the product Bellman equation: a left query changes only the left value and leaves the right optimum unchanged, and conversely. Thus exact product decomposition is a genuine fast path for the research compiler.

## 17. Proof history as a controlled A1/A2 collapse

An exact strategy gives the quotient chain

\[
X/E_{T,\mathcal Q}\longrightarrow X/E_S\longrightarrow X/\ker T.
\]

The first arrow forgets available query distinctions unused by the chosen strategy; the second forgets proof history and keeps only the answer. P011's collision spectrum applies exactly to these forgetting maps. This is a mathematical quotient of process records, not a claim of physical irreversibility.

## 18. Tool consequence

A research compiler should now declare separately:

- **answer language** — what must finally be known;
- **primitive acquisition language** — which exact queries/operations are allowed;
- **strategy tree** — which queries are actually used in which contexts;
- **encoding model** — adaptive branch-local, fixed ordered, or synchronous stage;
- **retained proof history** — whether transcripts are discarded or retained.

Thus

\[
\boxed{\text{precision state}\ne\text{query-language complexity}\ne\text{strategy complexity}.}
\]

## 19. Prior-art boundary

Deterministic decision trees, ordered decision diagrams, dynamic programming, Kraft-style coding bounds, direct-sum reasoning, kernels, and finite partition lattices are prior mathematics. Enterprise Math does not claim these generic structures. The owner result under test is their exact integration with integer repair alphabets, future-safe quotient semantics, proof-transcript repair spectra, and theorem-lifting workflows. Historical novelty of that integrated packaging remains unverified.

## 20. Executable specification

- `src/enterprise_math/a2_adaptive_acquisition.py`
- `tests/test_a2_adaptive_acquisition.py`

The tests pin the four-bit adaptive-vs-ordered separation, its three-variable minimality boundary, pure tree-packing and transcript-multiplicity gaps, partition-redundant bundled-query speedup, balanced-split tightness, ordered-vs-stage separation, and one adaptive direct-sum witness.

## 21. Foundation-backflow boundary

These results are mature enough for a Foundation Feedback Packet but should not directly edit `FOUNDATIONS`. The weakest proved finite distinction is

\[
\boxed{\text{final sufficient distinction}\ne\text{distinction required by the allowed proof/acquisition process}.}
\]

Any broader interpretation about physical state, cognition, or ontological information requires separate hypotheses.
