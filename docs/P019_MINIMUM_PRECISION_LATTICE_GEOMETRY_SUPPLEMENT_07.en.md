# P019 Supplement 07 — Compressed Fiber Witnesses and Oriented Contraction Flags

Status: `RESEARCH WIP / PROVED LOCALLY + ENUMERATION PRESSURE TEST`

## 1. Goal

Supplement 06 proved

\[
\text{minimum-value associativity}
\not\Rightarrow
\text{selected-boundary-witness associativity}.
\]

Therefore `ContractionTrace` cannot simply be deleted, but this does not justify storing every fine state, every tree, and every fiber explicitly.

We separate four layers:

1. `minimum-value layer`: only the fiber minimum is queried;
2. `full-witness-relation layer`: every currently feasible fine witness is retained;
3. `selected-boundary layer`: each directed fiber selects only a right/left boundary representative;
4. `historical-identity layer`: the exact fine witness / contraction history that actually occurred is itself queried.

These layers must not be conflated.

## 2. Balanced power kernel

For `m>=1, s>=1, c in Z`,

\[
\Psi_{m,s}(c)
=
\min_{a_1+\cdots+a_m=c}
\sum_{i=1}^m |a_i|^s.
\]

Write

\[
|c|=mq+r,
\qquad 0\le r<m.
\]

Then

\[
\boxed{
\Psi_{m,s}(c)
=(m-r)q^s+r(q+1)^s.
}
\]

In particular,

\[
\Psi_{m,s}(1)=1.
\]

## 3. P019-X09 — Complete minimum-witness classification for `s>1`

For `s>1`, every minimum fine witness at fixed total `c` has:

- all nonzero coordinates with the sign of `c`;
- absolute values differing by at most one.

Thus if `|c|=mq+r`, every minimizer consists of

- `m-r` coordinates of magnitude `q`;
- `r` coordinates of magnitude `q+1`.

The labeled minimizer count is therefore

\[
\boxed{
M^{\min}_{m,s}(c)=\binom mr,
\qquad s>1.
}
\]

The proof is an integer exchange argument. If same-sign magnitudes satisfy `u>=v+2`, replacing `(u,v)` by `(u-1,v+1)` strictly lowers `u^s+v^s`. If positive and negative coordinates coexist, moving both one step toward zero preserves the total and strictly lowers energy.

### The special case `s=1`

`Psi_(m,1)(c)=|c|`. Minimizers need not be balanced; they need only avoid sign cancellation.

For `c!=0`, the labeled minimizer count is the weak-composition count

\[
\boxed{
M^{\min}_{m,1}(c)
=
\binom{|c|+m-1}{m-1}.
}
\]

So the value layer is unified across `s`, while witness degeneracy changes at `s=1`.

## 4. P019-X10 — Two-block argmin profile is a finite integer interval

Merge blocks of sizes `m,n` with total `c`.

For `s>1`, write

\[
|c|=(m+n)q+r,
\qquad 0\le r<m+n.
\]

If the left block receives `h` of the `r` extra `q+1` slots, then

\[
\max(0,r-n)
\le h\le
\min(m,r).
\]

With `sigma=sgn(c)`, the block totals are

\[
a=\sigma(mq+h),
\qquad
b=c-a.
\]

The exact labeled fine-witness multiplicity supporting this split is

\[
\boxed{
\binom mh\binom n{r-h}.
}
\]

Summing the whole argmin profile gives

\[
\sum_h
\binom mh\binom n{r-h}
=
\binom{m+n}{r}.
\]

Thus minimum-witness provenance composes under block merge without a contraction tree.

## 5. Provenance polynomial

For blocks `m=(m_1,...,m_k)` and total remainder `r`, define

\[
P_{\mathbf m,r}(z_1,\ldots,z_k)
=
[t^r]
\prod_{i=1}^k(1+z_i t)^{m_i}.
\]

Its coefficients satisfy

\[
[z_1^{h_1}\cdots z_k^{h_k}]
P_{\mathbf m,r}
=
\prod_i\binom{m_i}{h_i},
\qquad
\sum_i h_i=r.
\]

Merging blocks `i,j` and identifying `z_i=z_j=z` replaces their factors exactly by

\[
(1+zt)^{m_i+m_j}.
\]

Hence this minimum-provenance representation is strictly associative under block merge.

This is a candidate provenance tool. General semiring/provenance prior art must be mapped before promotion; no priority claim is made here.

## 6. P019-X11 — A full fiber sublevel relation needs only two integers

For two blocks of sizes `m,n` and total `c`, define

\[
f(a)
=
\Psi_{m,s}(a)
+
\Psi_{n,s}(c-a),
\]

with merged minimum

\[
f_{\min}=\Psi_{m+n,s}(c).
\]

For nonnegative slack `omega`, define

\[
I_{m,n,s}(c,\omega)
=
\{a\in\mathbb Z:
 f(a)-f_{\min}\le\omega
\}.
\]

Let

\[
\Delta\Psi_{m,s}(u)
=
\Psi_{m,s}(u+1)-\Psi_{m,s}(u).
\]

`Delta Psi` is nondecreasing on the integer line. Therefore

\[
f(a+1)-f(a)
=
\Delta\Psi_{m,s}(a)
-
\Delta\Psi_{n,s}(c-a-1)
\]

is nondecreasing as well. Thus `f` is one-dimensional discrete convex and every finite sublevel set is an integer interval:

\[
\boxed{
I_{m,n,s}(c,\omega)
=[L,U]\cap\mathbb Z.
}
\]

The complete block-total witness relation therefore needs only

\[
\boxed{(L,U)}.
\]

Its block-total fiber multiplicity is

\[
\boxed{M=U-L+1.}
\]

This directly connects P019 contraction fibers with the P011 multiplicity language.

## 7. Directed boundary is a fiber endpoint

If transfer direction is `donor -> receiver` and receiver total is `a`, the split edge crosses the sublevel boundary exactly when

\[
f(a)\le f_{\min}+\omega
< f(a+1).
\]

Since the feasible set is `[L,U]`, the unique right-boundary witness is

\[
\boxed{a=U.}
\]

The opposite direction selects `L`.

A boundary representative is therefore not a new primitive. It is an endpoint selection from the full fiber relation.

## 8. Oriented contraction histories are maximal chains in the partition lattice

Start with `N` labeled unit slots and merge two current blocks at each step.

Ignoring receiver/donor orientation, a stage with `k` current blocks has

\[
\binom k2
\]

possible merges. Hence

\[
\boxed{
H_N^{\mathrm{unoriented}}
=
\prod_{k=2}^N\binom k2
=
\frac{N!(N-1)!}{2^{N-1}}.
}
\]

If each merge also records receiver/donor order, the stage has `k(k-1)` choices and

\[
\boxed{
H_N^{\mathrm{oriented}}
=
\prod_{k=2}^N k(k-1)
=
N!(N-1)!.
}
\]

Thus an exact directed trace grows factorially if stored without quotienting.

Partition-lattice maximal-chain counting is established combinatorics. The P019 question is not to rename this count, but to determine when this history can be safely quotiented in finite-precision contraction.

## 9. P019-X12 — An oriented flag is sufficient to replay the selected boundary witness

A complete oriented contraction history records an ordered pair at each merge:

`(receiver_block, donor_block)`.

Given power `s`, global threshold `T`, and the complete oriented history, start from the final one-block state of total zero and replay backward.

At each reverse split:

1. let the merged block total be `c`;
2. compute the minimum energy `E_other` of all other current blocks;
3. compute fiber slack

\[
\omega
=T-E_{other}-\Psi_{m+n,s}(c);
\]

4. compute `[L,U]`;
5. assign `U` to the receiver child;
6. continue to the singleton partition.

Hence oriented partition flag + `(s,T)` is a sufficient trace for selected-boundary replay.

## 10. Exhaustive small-dimensional evidence: final partition is far from sufficient

For `s=2`, all labeled oriented contraction histories were enumerated and their complete boundary-witness maps compared over multiple integer thresholds.

Results:

- `N=3`: `12` histories and `12` distinct labeled witness maps;
- `N=4`: `144` histories and `144` distinct labeled witness maps;
- `N=5`: `2880` histories and, after scanning even thresholds `0..100`, `2880` distinct labeled witness maps.

This is not a general injectivity theorem, but it is a strong finite counterexample corpus: at these sizes no two distinct oriented histories can be unconditionally merged under the tested future queries.

Therefore tree shape, final block size, and final minimum energy are not sufficient for exact selected-boundary history.

## 11. Current precision layers

### A. Value only

Store

`visible totals + block sizes + power`.

### B. Minimum witness multiplicity/provenance

For `s>1`, block sizes plus totals/remainders determine the binomial provenance profile. No contraction history is needed.

### C. Full one-step fiber relation

Store only the interval endpoints `[L,U]`.

### D. Selected multi-step boundary witness

Currently known sufficient object:

`oriented contraction flag + power + threshold`.

Further compression must be defined relative to the allowed future operation/observation family.

### E. Exact historical identity

If the query itself asks which exact fine witness actually occurred, any summary identifying two different actual witnesses is not history-exact.

That is a provenance/ontology choice, not something the value algebra can silently decide.

## 12. Implementation

Added:

- `src/enterprise_math/contraction_trace.py`
  - `balanced_minimizer_count`
  - `two_block_argmin_profile`
  - `fiber_witness_interval`
  - `fiber_witness_multiplicity`
  - `directed_boundary_split`
  - `reverse_boundary_witness`
  - partition-chain counts
- `tests/test_contraction_trace.py`

The formulas were cross-checked by direct enumeration for powers `s=1..4`, several block sizes, positive/negative totals, and multiple slack values.

## 13. Next step

The next problem is no longer to search for one universal smallest trace. Instead:

> For a specified family of future operations, what is the coarsest quotient that preserves every future compositional answer?

Supplement 08 formalizes this as future-composition equivalence / safe trace erasure.
