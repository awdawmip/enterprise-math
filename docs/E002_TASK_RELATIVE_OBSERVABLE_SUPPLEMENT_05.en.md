# E002 — Task-Relative Observable Precision, Supplement 05

Status: `ACTIVE ENGINEERING RESEARCH NOTE`  
Scope: correlated diagonal motion with different future observation languages  
Parent: `docs/E002_VECTOR_PRECISION_ACTUATION_SUPPLEMENT_04.en.md`  
Dependency: E002 vector precision and P023 task-relative future compatibility

## 1. Why the full-vector law is not the end of the story

Stage 4 proved that for the **complete rectangular vector quotient** the required within-cell class count is the product of coordinate projection counts. For one diagonal action with common coordinate period `P`, this can grow as

\[
C_h=\min(h+1,P)^n.
\]

That result is exact for its declared future language, but it is deliberately not universal. P023 says that the coarsest valid state depends on the future observable/operation language.

This supplement keeps the *same physical trajectory* and changes only the question asked of the future. It quantifies exactly how much fine phase becomes unnecessary when the observable has symmetry or ignores coordinates.

## 2. Crossing buckets

Use equal odd coordinate width `w`, one deterministic diagonal unit action

\[
a=(1,\ldots,1),
\]

and a horizon

\[
0\le h<w.
\]

Inside one original precision cell, a coordinate detail `r in {0,...,w-1}` first crosses to the next coarse quotient at sample

\[
\tau(r)=w-r.
\]

All crossings after the declared horizon are identified with one terminal bucket `h+1`. Define

\[
\boxed{
b_h(r)=\min(\tau(r),h+1).}
\]

There are exactly

\[
\boxed{B=h+1}
\]

observable crossing buckets.

For samples `k=0,...,h`, the coordinate quotient increment is the binary step

\[
\boxed{q_r(k)=\mathbf1_{b_h(r)\le k}.}
\]

Thus every future-language question below is a finite quotient of the same ordered tuple of crossing buckets.

## 3. E002-T29 — Complete classification of two-coordinate linear observables

Consider the scalar future observable

\[
\boxed{y_k=\alpha q_1(k)+\beta q_2(k)}
\]

with integer coefficients `alpha,beta`.

Let `B=h+1`. The exact number of within-cell future classes is

\[
\boxed{
C_{\alpha,\beta}(h)=
\begin{cases}
1,&\alpha=\beta=0,\\
B,&\text{exactly one of }\alpha,\beta\text{ is nonzero},\\
\frac{B(B+1)}2,&\alpha=\beta\ne0,\\
B(B-1)+1,&\alpha=-\beta\ne0,\\
B^2,&\text{otherwise}.
\end{cases}}
\]

### Proof by discrete jumps

A bucket pair `(t_1,t_2)` determines the entire future sequence. Look at first differences of `y`.

- coordinate 1 contributes one jump of size `alpha` at `t_1` if it crosses within the horizon;
- coordinate 2 contributes one jump of size `beta` at `t_2`;
- simultaneous crossings contribute `alpha+beta`.

If both coefficients vanish, every sequence is zero.

If exactly one coefficient is nonzero, only one crossing bucket is visible, giving `B` classes.

If `alpha=beta!=0`, exchanging the two coordinates changes nothing. The sequence determines only the unordered pair of crossing buckets, including repetition. The number of multisets of size two from `B` buckets is

\[
\binom{B+1}{2}=\frac{B(B+1)}2.
\]

If `alpha=-beta!=0`, every diagonal pair `t_1=t_2` cancels to the identical zero sequence, while every off-diagonal ordered pair is recovered from the signed jump times. There are `B(B-1)` ordered off-diagonal pairs plus one common diagonal class.

In every remaining case, `alpha`, `beta`, and `alpha+beta` are nonzero with enough distinct jump labels to recover the ordered bucket pair uniquely. Hence all `B^2` ordered pairs remain distinct. ∎

## 4. Consequence: scalar does not automatically mean compressed

A one-dimensional output can require the same fine precision as the full two-coordinate vector.

For generic coefficients,

\[
\boxed{C_{\alpha,\beta}(h)=B^2=C_{\rm full}(h).}
\]

Example at `h=4`:

- full `(q_1,q_2)`: `25` classes;
- generic scalar `q_1+2q_2`: `25` classes;
- symmetric sum `q_1+q_2`: `15` classes;
- difference `q_1-q_2`: `21` classes;
- one coordinate only: `5` classes.

The compression comes from the **symmetry/information loss of the future observable**, not merely from lowering output dimension.

## 5. E002-T30 — n-dimensional symmetric sum

Now observe only

\[
\boxed{S_k=\sum_{i=1}^n q_i(k).}
\]

The first difference `S_k-S_(k-1)` records how many coordinate crossing buckets equal `k`. Therefore the entire sequence is determined exactly by the multiset of the `n` crossing buckets.

There are `B=h+1` bucket values, so the exact class count is the multiset coefficient

\[
\boxed{
C_{\rm sum}(n,h)=\binom{B+n-1}{n}=\binom{h+n}{n}.}
\]

### Proof

Every ordered bucket tuple maps to its multiset because the sum is invariant under coordinate permutations. Conversely, the jump multiplicity at every sample reconstructs the count of every finite bucket; the remaining coordinates are in the terminal bucket. Thus two states have the same sum future sequence exactly when their crossing-bucket multisets agree. ∎

### Comparison with full vector

The complete vector requires

\[
B^n
\]

classes, while the symmetric sum needs only

\[
\binom{B+n-1}{n}.
\]

The exponent in horizon/dimension is not removed, but permutation labels are erased exactly.

## 6. E002-T31 — Boolean ANY and ALL crossing languages

Consider two even weaker future questions:

\[
A_k=\mathbf1_{\exists i:q_i(k)>0}
\]

and

\[
Z_k=\mathbf1_{\forall i:q_i(k)>0}.
\]

`A_k` is determined only by the **earliest** crossing bucket

\[
\min_i b_i,
\]

while `Z_k` is determined only by the **latest** crossing bucket

\[
\max_i b_i.
\]

Each extrema has exactly `B=h+1` possibilities. Therefore for every dimension `n>=1`,

\[
\boxed{C_{\rm ANY}(n,h)=C_{\rm ALL}(n,h)=h+1.}
\]

### Dimension-power collapse

At `n=5,h=4`, the same physical fine states give:

\[
C_{\rm full}=5^5=3125,
\]

but

\[
C_{\rm ANY}=C_{\rm ALL}=5.
\]

Thus changing only the declared future question can reduce the exact state obligation from dimension-power growth to a dimension-independent linear horizon law.

No physical state or trajectory has been changed.

## 7. E002-T32 — Boolean equality of two coarse coordinates

For two coordinates define

\[
E_k=\mathbf1_{q_1(k)=q_2(k)}.
\]

If both crossing buckets are equal, the coordinates remain equal throughout the whole horizon, and **all** diagonal bucket pairs collapse to one common class.

If the buckets differ, equality is false exactly on the interval between the two crossing times. The equality sequence therefore determines the unordered pair of distinct bucket values.

Hence

\[
\boxed{
C_{=}(h)
=1+\binom{B}{2}
=1+\frac{h(h+1)}2.
}
\]

This is strictly coarser than the antisymmetric linear difference language, which retains orientation and needs `B(B-1)+1` classes.

## 8. Exact task ladder on one physical trajectory

For the same diagonal motion, equal width, and horizon, E002 now has an explicit family of future-language state obligations:

\[
\boxed{
\begin{array}{c|c}
\text{future observable}&\text{exact classes}\\
\hline
\text{full }n\text{-vector}&B^n\\
\text{symmetric sum}&\binom{B+n-1}{n}\\
\text{ANY / ALL}&B
\end{array}}
\]

and in two dimensions:

\[
\boxed{
\begin{array}{c|c}
\text{observable}&\text{exact classes}\\
\hline
\text{generic }\alpha q_1+\beta q_2&B^2\\
q_1+q_2&B(B+1)/2\\
q_1-q_2&B(B-1)+1\\
q_1\text{ only}&B\\
q_1=q_2&1+B(B-1)/2
\end{array}}
\]

These are not heuristic compression ratios. Each row is the exact quotient cardinality of the same fine cell under a different declared future language.

## 9. Engineering interpretation

The sequence of E002 results now separates three questions that conventional use of one scalar 'precision' often mixes:

1. **what physical states are represented?** — the centered precision cell;
2. **what future dynamics may occur?** — the action language and horizon;
3. **what future distinctions matter?** — the observation/query language.

The coarsest safe state depends on all three.

Thus a world engine should not necessarily carry the maximum precision needed by every conceivable query. It may carry or refine exactly the state required by its declared future operation and observation language.

This does **not** mean that precision can be chosen arbitrarily after seeing an answer. The allowed language, horizon, and projection must be declared before discarding detail if the quotient is to be predictive rather than retrospective.

## 10. Relation to P023

P023 already states the generic rule: a coarse state is future-safe only for the operations/observables that factor through its fibers, and the coarsest repair is language-relative.

E002-T29 through T32 provide closed integer cardinalities for a concrete physical-action specialization. They do not duplicate the P023 mother theorem.

The main new negative boundary is:

> neither physical dimension, action-subgroup size, nor output dimension alone determines required precision.

The symmetry and factorization properties of the declared future observable are decisive.

## 11. Relation to Stage 4 correlation expansion

Stage 4 defined, for full rectangular observation, a correlation expansion factor comparing the action subgroup with the product of coordinate projection states.

Stage 5 shows that this expansion is itself **observable-relative**. A strongly correlated action may require `B^n` classes for full coordinates but only `B` classes for an ANY/ALL task.

Therefore Stage-4 `Delta_A` must never be promoted into a task-independent physical information quantity.

It is an exact observable-state index only for the full rectangular quotient language that defined it.

## 12. Executable audit

Implementation:

- `src/enterprise_math/precision_task_observable.py`

Tests:

- `tests/test_precision_task_observable.py`

Probe:

- `experiments/e002_task_observable_probe.py`

Independent reconstruction checked:

- all integer coefficient pairs `alpha,beta in [-3,3]`, odd widths through `11`, and every `h<w` against the T29 classification, with no counterexample;
- symmetric sums for dimensions through `4` and small odd widths against `binomial(h+n,n)`;
- ANY and ALL future signatures against the dimension-independent `h+1` law;
- two-coordinate Boolean equality against `1+h(h+1)/2`.

The committed tests repeat these checks over bounded domains.

## 13. Prior-art and novelty boundary

Step functions, symmetric polynomials/sums, multisets, binomial coefficients, Boolean threshold aggregation, and observational equivalence are established mathematics/computation/control ideas. E002 does not claim them as inventions.

The research target is the exact finite-precision state accounting obtained by holding the physical dynamics fixed and varying only the declared future observation language.

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 14. Next pressure tests

High-value next questions:

1. replace the hand-chosen observables by a finite controller/query automaton and compute its minimal predictive quotient automatically;
2. study mixed linear observables beyond the diagonal-action special case, including coefficient/action resonance;
3. move from rectangular cells to a genuinely lattice-shaped observation and test when module/SNF invariants become sufficient;
4. connect ANY/ALL collision-style queries back to E001 and measure how much vector position phase can be discarded without changing collision futures;
5. turn exact class counts into an adaptive execution policy and benchmark state/work saved against always retaining full fine coordinates.
