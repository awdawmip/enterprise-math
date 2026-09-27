# A consistent native suffix-path row estimator

Status: AUTHOR_ACTUAL_NATIVE_BOUNDED_EXECUTION / SHARED_CONTEXT / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC.
Project source: 671530e485921a9eeed91c1635decd60cc195dc3.
Global knowledge lease supplied by the coordinating author: f44ed5959c92e6e088c61c102951d1ab2c5e98d4.

This unit implements a point-row estimator and checks its exact variance.
It executes no approximate sampler and establishes no lower bound on sampling
total variation. The complete stored prefix is a charged input. No unknown
order, factors, ideal QFT propagation or classical ideal reference run enters
the implementation or checker.

## 1. Ordered expansion and the unbiased function

Let g be a fixed measured prefix of length k, with complete raw native state
v_g, and let h extend g to length i=k+ell. Write

    A_j = (-1)^(h_j) T_(h[:j]) P_j,
    K_j = (I+A_j)/2,                       k <= j < i.

P_j permutes work labels and transports every internal coordinate. T is the
actual admitted native feedback word in its original temporal order. The
carrier is real, complete and orthogonal; no residual coordinate is removed.
The work permutation and internal T commute within one round because they
act on different factors. Different T words need not commute.

For e in {0,1}^ell define

    Z_(h,e) = A_(i-1)^(e_(ell-1)) ... A_k^(e_0) v_g.

There is no factor 2^-ell in Z. Product expansion in this exact order gives

    v_h = 2^-ell sum_e Z_(h,e),       ||Z_(h,e)||^2 = M_g := ||v_g||^2.

Fix m complete paths before any row query. The function

    u_h(w) = (1/m) sum_(j=1)^m Z_(h,e_j)(w)

is then one coherent full row function. A path is never redrawn in response
to a queried label or the sampler's private latent work label. Independent
uniform paths sampled with replacement give E u_h=v_h. The implementation
also accepts explicit finite lists for exhaustive validation; that interface
does not certify iid randomness.

## 2. Exact raw-mass variance and its scope

Orthogonality and unbiasedness give the finite identity

    E_e ||Z_(h,e)-v_h||^2 = M_g-M_h,
    E ||u_h-v_h||^2 = (M_g-M_h)/m.

The second equation uses independence of the m paths within this estimator.
Independence between estimators for different target histories is unnecessary
for the following sum of expectations. Actual instrument completeness gives

    sum_(h extends g) M_h = M_g,
    sum_(h extends g) E ||u_h-v_h||^2 = (2^ell-1) M_g/m.

Summing over every raw prefix g at depth k yields (2^ell-1)/m, since
sum_g M_g=1. The fixed-prefix expression must retain its M_g factor; it is
not generally (2^ell-1)/m by itself.

These equations quantify one iid estimator's raw L2 error. They do not say
that a sampler must incur that error as TV. In particular, exact-reference
histories with M_h=0 have zero weight in a reference-kernel sampling bound,
even when their estimated raw functions have positive squared error.

For a symbolic counterexample, take a=1 and the standard initial work label
1. Along the sole positive-reference measured history all prior bits are
zero, so feedback is I and every P is I. Every path on this history is the
same vector, and the estimator is exact. The local sampler emits plus with
probability one, exactly as the native instrument. Impossible measured
histories account for the positive aggregate raw L2 variance above. This
is an analytic illustration, not another execution or a claim about hard
factoring inputs. Global raw L2 accuracy is sufficient rather than necessary
for accurate measurement sampling.

The sharper bounds in ../observer_contracts/PROJECTIVE_AND_COHERENCE_BOUNDS.md
allow a common scalar per complete prefix function, use exact-reference
mass weighting, or directly certify interference. This path unit does not
construct such cheaper certificates.

## 3. Actual point-query implementation

`suffix_path_estimator.py` exposes:

- `draw_path_list(prefix_history, target_history, sample_count, rng)` draws
  m*ell software random bits before any query label is available. An exhausted
  random interface returns INCOMPLETE_PATH_RANDOM_SOURCE and is not accepted
  as a completed estimator. Conditional-uniform independent randomness is an
  interface assumption; a deterministic seed is only a reproducibility fixture.
- `SuffixPathEstimator(program, prefix_state, prefix_den, prefix_history,
  target_history, paths, construction_receipt=None)` copies the complete raw
  prefix into immutable rows. The constructor checks shape and exact integer
  representation; authenticity as a reachable prefix is a caller obligation.
  This checker supplies actual native prefixes, rather than asserting that
  any shaped dictionary is an authenticated reachable state.
- `point_path(j,w)` applies requested actual typed inverse modular columns in
  reverse selected-round order to locate the prefix row. It then applies the
  selected native feedback words in forward order, with the corresponding
  measured signs. It performs no branching recurrence and builds no suffix
  work-amplitude table.
- `point_mean(w)` uses the same path list for every w, aligns exact dyadic
  denominators, and evaluates signed coordinate sums through the inherited
  actual PositivePathObserver. Division by m yields a general rational
  MeanRow. This is an observer of a consistent function, not a new native
  gate with an arbitrary rational primitive coefficient.

The PointRowOracle dependency is used for native arithmetic, feedback and
observers only. Its recursive query method is never called. In particular,
its zero cached-row count is not a claim that no prefix rows are stored.

All nonzero paths retain signed residuals. Structural zero skipping and
one-term signed wiring follow the frozen observer's existing rules. Native
phase words and the two-H4 branch identity come from the admitted dependency;
all full61 columns are checked before optional exact six-coordinate boundary
encoding. Internal primitive words themselves are never truncated.

## 4. Construction, query and evidence costs

With s stored prefix rows and internal dimension D, input storage costs sD
integer coordinates plus their common denominator. The fixed list costs
m*ell bits. Its random construction takes exactly m*ell successful bit
draws, excluding source preparation and random-source implementation cost.

One point-mean query requests at most m*ell typed inverse modular columns,
m prefix-row lookups and m*ell ordered feedback applications. A feedback
application can itself contain up to i admitted phase factors; its full
native-word application cost and integer bit lengths remain charged.
Mean formation visits mD aligned coordinate terms. This implementation
temporarily retains m D-dimensional path rows rather than claiming O(D)
workspace. The complete prefix, typed column caches, native certificates,
query receipts and positive-path graphs add to storage. Point-query cost
alone is not the cost of an entire sampler or of discovering a useful m.

Reports separately record path/mean requests, inverse-column requests,
selected factors, actual phase-vector applications, scalar slots and maximum
denominator/numerator sizes. Modular arithmetic uses the existing typed
full-adder/shift-add/division executor. Its digit replays and bit wiring are
distinct resource units from native core invocations. Shared program-table
metrics are cumulative and are not cold costs attributable to one query.

The checker is deliberately exhaustive and materializes all path vectors
over their union support for validation. This enumeration occurs only in the
checker, not in the point-query API. Its own cost is not presented as a fast
sampling algorithm. Equal permutation certificates can describe separate
forward/inverse cache instances: the final evidence keeps each actual table
instance and its columns/costs. The superseded first packaging, which could
merge those instances, is retained under prior_table_instance_packaging.

## 5. Bounded execution

The exact input is N=21, a=2, t=4, k=2, ell=2. Both D=61 and the already
proved exact D=6 boundary codec use the same actual direct-word bank. That
bank has a recorded terminal error certificate 1/2 relative to its target;
this is not the tighter default complete-factorization budget. Comparisons
here are with the same actual native words, not with ideal Shor amplitudes.

For each dimension the checker prepares all four raw prefixes, completes all
four suffix histories per prefix, and evaluates all four preparation paths
per target. Every path norm equals M_g. Every coordinate of the four-path
mean exactly equals the actual native raw target state. Every target also
checks all 16 ordered with-replacement path pairs, 256 pairs per dimension.

| Prefix g | M_g | Sum of one-path variances | Sum of m=2 errors |
| --- | --- | --- | --- |
| 00 | 3/8 | 9/8 | 9/16 |
| 01 | 1/8 | 3/8 | 3/16 |
| 10 | 1/4 | 3/4 | 3/8 |
| 11 | 1/4 | 3/4 | 3/8 |
| All raw prefixes | 1 | 3 | 3/2 |

The D=6 and D=61 observations agree exactly and retain a nonzero residual
in the complete set of cases. Additional interface checks cover m=3,
query-order consistency, ell=0, exhausted random construction and five
invalid inputs. A single seeded m=3 list demonstrates the fixed-function
API, not statistical accuracy of an approximate sampler.

Final execution and source hashes, resource counts and full primitive
receipts are in SUFFIX_PATH_SUMMARY.json and SUFFIX_PATH_RESULTS.json.gz.
The final run used 12,459 actual native core calls including admission,
comparators and interface checks. For each dimension the estimator fixture
recorded 3,840 point-path requests, 1,632 point-mean requests, 2,200 native
phase-vector applications and 6,106 positive-path observer calls. Its five
distinct modular table instances computed 20 columns, with 3,472 typed adder
digit replays and 37,456 host bit-wiring operations including their setup.
These per-dimension figures include exhaustive validation work and shared
caches; they are not the cost of a single fresh query. The maximum recorded
path and mean denominators required 77 and 79 bits respectively.

The final payload SHA256 is
`1c22dd5a0e3970052eb0aeac84c20485c094c742a50346d2c1c38f986ddaa19f`.
Only the evidence-table packaging and resource summary changed between the
first and final runs; the estimator algorithm stayed fixed. Neither run
supplied an order or factors, performed an ideal-reference execution, or
executed approximate conditional sampling.

Global-Knowledge-Sync: main@f44ed595 / GLOBAL_KNOWLEDGE_V1
