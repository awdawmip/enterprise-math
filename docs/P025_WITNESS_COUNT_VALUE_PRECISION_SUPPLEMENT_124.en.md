# P025 Supplement 124 — Witness-Count Value Precision

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-witness-count-stage121`  
Depends on: P025 Supplements 116–123  
Hard block: `NONE`

## 1. Same query coordinate, different value precision

Supplements 121–123 strengthen joint witness semantics from existence to exact counts. Stage 124 isolates the remaining resource: even when the query geometry is fixed, the **value alphabet** carried by each query can change the recoverable state.

Let

\[
N:=c(\varnothing)=\sum_{I\in J(P)}w(I)>0
\]

be total witness multiplicity.

## 2. P025-T273 — MAY/MUST is a three-valued collapse of exact counts

For any required query \(S\),

\[
0\le c(S)\le N.
\]

The ordinary joint support semantics is recovered exactly by

\[
\boxed{
\begin{array}{ccl}
c(S)=0 &\iff& S\text{ is IMPOSSIBLE},\\
0<c(S)<N &\iff& S\text{ is MAY but not MUST},\\
c(S)=N &\iff& S\text{ is MUST}.
\end{array}}
\]

Therefore exact integer count semantics factors onto MAY/MUST semantics by the three-cell value quotient

\[
\boxed{
\{0\},
\{1,\ldots,N-1\},
\{N\}.
}
\]

This is a value collapse at fixed query coordinates; it is independent of the antichain/query-arity collapse from Stages 119–122.

## 3. P025-C42 — same support family and total can hide different counts

Take the two-element antichain \(P=\{a,b\}\). Consider two multiplicity assignments on the **same positive support family**

\[
\{\{a\},\{b\},\{a,b\}\}.
\]

Let

\[
w_1(\{a\})=1,
\quad
w_1(\{b\})=1,
\quad
w_1(\{a,b\})=2,
\]

and

\[
w_2(\{a\})=2,
\quad
w_2(\{b\})=1,
\quad
w_2(\{a,b\})=1.
\]

Both have

\[
N=4
\]

and exactly the same admissible exact-state support. Hence every existential/universal joint-MAY/MUST truth value is the same.

But

\[
\boxed{
c_1(\{b\})=3,
\qquad
c_2(\{b\})=2.}
\]

So exact witness-count semantics is strictly finer even when support identity and total multiplicity are fixed.

## 4. Precision-resource separation

Combining Stages 119–124 gives three independent axes:

1. **query/support geometry** — which essential antichain coordinates exist;
2. **query arity horizon** — how many incomparable requirements may be asked simultaneously;
3. **value precision** — what information each coordinate stores: Boolean existence, three-valued MAY/MUST, thresholded counts, or exact integer counts.

The same coordinate system can therefore support several different state quotients simply by changing its value collapse.

## 5. Relation to P023/A2

P023/FQ-004 generic future-signature machinery already says that a declared future determines the coarsest quotient on responses. Stage 124 is a finite specialization illustrating that quotienting can occur **inside the codomain values** without changing the operation/query coordinates.

It should not be promoted as a new generic threshold theorem.

## 6. Relation to A4

A4 owns witness spectra and multivalued correspondence. Stage 124 says that witness support and witness multiplicity are distinct state resources even when they live on the same witness complex.

A future asking only MAY/MUST should not retain exact counts; a future asking counts cannot be served by support alone.

## 7. Prior-art discipline

Thresholding integer counts and existential/universal semantics are elementary. No generic novelty claim is made.

The project-side result is the exact value-precision placement and executable same-support/same-total collision inside the P025/A2/A4 hierarchy. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 8. Executable assets

Added:

- `src/enterprise_math/poset_witness_count_value_precision.py`;
- `tests/test_poset_witness_count_value_precision.py`.

The executable layer verifies the IMPOSSIBLE/MAY/MUST count thresholds, same-support/same-total count collisions, and the exact MUST/IMPOSSIBLE boundaries.

## 9. Natural generation boundary

Stages 121–124 now form one coherent count-precision generation:

\[
\boxed{
\text{witness existence}
\to
\text{zeta counts}
\to
\text{exact multiplicity inversion}
\to
\text{sharp width horizon}
\to
\text{task-relative pushforward}
\to
\text{value precision}.
}
\]

The next generation should leave the ideal-state assumption and test whether width-based operation saturation survives for arbitrary A4 correspondences. It is expected to fail; an exact minimal counterexample would identify the ideal/downward-closure law as the real source of width saturation.
