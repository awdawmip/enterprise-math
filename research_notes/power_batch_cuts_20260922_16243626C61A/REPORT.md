# POWER feedback V: shared windows, dyadic cuts, and a bounded terminal index

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`
Researcher-ID: `EM-DIRECT-16243626C61A`
Session: `local-power-review-16243626C61A` (local continuation key, not a platform-authenticated ID)
Progress-Event-ID: `power-batch-cuts-20260922-16243626C61A`
Status: `PROVED_SCOPED_DERIVATIONS + BOUNDED_EXECUTABLE_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`

## 0. Continue the verified frontier, not the old audit

The preceding fixed-terminal unit is on EM at `6184fab86dacc5a9ed339cb575db1575b65042af`.
This turn verified current EM main `646115372e47bfa412d2081f4972d61fc598086e`, activity blob
`4fecb45bbb239ebce6f9ac7434ef3f889095bf78`, and unchanged terminal source blob
`354633331b05f8c7f275e852ae04df85aad63004`. The standalone preceding bundle was cloned
locally, not fetched through local/container networking. GitHub connectors remained remote I/O.

The OLD `terminal_responses` already batches several targets at ONE window and balances
its width against their number. That is not new work here. The new question is whether
several WINDOWS and several DYADIC CUTS share work, while charging setup, prefix construction
and comparing genuinely equivalent classical problems.

No P000 change, geometry interpretation, new top-level family, CLAIM, Driver acceptance,
Working Truth or Foundation admission is asserted. The existing BRC T0 positive count,
T4 finite collision readout and T6 observer-scope rules are applied. Existing
`cyclic_terminal_value` is executed unchanged for witnessed-period queries. Inherited tests
also execute the original `ControlMassQuotient` checker; this is not a new mass checker.

## 1. Frozen observer and exact positive-half law

For unit a modulo n and integer L>=1, define

    h_L(u) = sum_{d=-(L-1)}^{L-1} (L-|d|) * 1_{u*a^d=1}.

For each target v let

    S_L(v) = sum_{0<=d<L, a^d=v} (L-d).

For a unit u, h_L(u)=S_L(u)+S_L(u^-1)-L*1_{u=1}. Nonunit u has response zero.
All coefficients are nonnegative integer counts. Negative exponent labels denote inverse
group operations, not negative mass or a signed amplitude.

The finite uniform-interval program, input targets, window(s) and permitted cuts are declared.
None of these representations claims to support arbitrary additional updates or observables.

## 2. Same base, varying windows: one scan per signed target, not per window

Fix a baby width B. At a giant block boundary qB retain, for each target v,

    C = number of hits d<qB,
    D = sum of those exponents d.

Then for L=qB+t:

    S_L(v) = L*C-D + sum_{qB<=d<qB+t, a^d=v} (L-d).

The last term is a partial-block contribution. Sort the requested lengths for each target
and advance its giant trajectory monotonically. There is no reason to restart the same
trajectory for each requested length.

The implementation constructs the baby powers sequentially. Before a first return to 1,
all baby residues are distinct, so a partial block contains at most one match. If the orbit
actually closes during table construction, its first return and preceding distinct powers
prove the exact short order. The implementation switches to the inherited periodic formula;
it NEVER overwrites duplicate offsets and silently treats a periodic fiber as one hit.

Let T be the set of distinct signed unit targets, L_v the largest length requested for v,
and H the total number of requested observations. In the unclosed-orbit case the exact
accounted scans are

    B + sum_{v in T} ceil(L_v/B).

Sorting, output, target inversions, integer bit costs and input storage remain additional
costs. In particular total runtime is not independent of H: output alone costs Omega(H).
The width balances sum_v L_v, not the number of repeated identical windows. Full-orbit
closure is an explicitly reported special case; it materializes a small complete subgroup
only when that subgroup is encountered inside the budget.

API: `window_responses`. This is an extension of the existing terminal operator, not a new
BSGS complexity result.

## 3. Aligned dyadic cuts: retain valuation information and share a giant step

Let N=2^m and consider cut j, with base a^(2^j) and suffix length N/2^j. Reindexing its
triangular kernel gives

    h_j(u) = sum_{|d|<N, 2^j divides d} ((N-|d|)/2^j) * 1_{u*a^d=1}.

Choose a master width B=2^k and restrict this shared-moment backend to cuts j<=k. Write
positive exponents d=iB+l. Then

    2^j divides d  iff  2^j divides l,
    (a^(2^j))^(B/2^j) = a^B.

Every selected cut therefore has the SAME giant multiplier. At a match, put the master
weight N-iB-l into bucket min(v_2(l),J), where J is the largest selected cut and l=0 is put
in the all-divisible bucket J. Reverse cumulative bucket sums, divided exactly by 2^j,
produce each positive-half response. This retains the arithmetic information that a raw
representative merge would erase.

Before short-orbit closure, there is one baby offset per table key. Hence one giant lookup
visits at most one bucket, not every cut. With T signed targets, scanning costs

    B + |T| * N/B,

plus O(|T|*(J+1)) bucket finishing and the explicit output matrix. The lookup count is the
same as for cut 0 alone at that chosen width. It is NOT a universal claim that all other
costs vanish, and choosing B>=2^J can be expensive for very deep cuts. This backend refuses
misalignment/over-budget requests instead of asserting a false shared-table identity.

Counterexample to naive rescaling: n=7,a=3,m=3,u=3 gives h_0=11 but h_1=0, not floor(11/2).
The state is outside the subgroup generated by a^2. Divisibility of exponent offsets is
essential. The test suite preserves this witness.

API: `dyadic_cut_responses`. It is a bounded aligned backend, not an arbitrary-base cache.

## 4. The stronger comparator led to a preferable bounded index

A comparison only against separate old window calls can exaggerate novelty. Therefore two
classical references were executed: (a) compute the full order once, then shared discrete
logs; (b) do only BOUNDED order/log work needed for this same set of terminal queries.
The second comparator was consistently faster than the moment backends on the six measured
batches. The useful interface was therefore extracted, not hidden as an inconvenient result.

`compile_terminal_index(n,a,span,states)` uses conventional shared BSGS to search for:

1. the smallest positive identity exponent r<=span, if any;
2. the smallest exponent e in [0,span) for each registered target and its inverse.

The baby table is injective unless its actual first return already proved a short order.
Otherwise increasing giant blocks and their unique baby offsets yield the smallest positive
match. Finding r certifies the exact order. No positive match proves only r>span. No true
order, group-order factorization or exponent labels are provided as inputs.

If an exact period r was found and a target first appears at e, its positive hits are e+kr.
Writing c=max(0,1+floor((L-1-e)/r)),

    S_L = c*(L-e) - r*c*(c-1)/2.

If no period occurs up to span, there is at most one hit in [0,span), so S_L=max(L-e,0).
Missing targets have zero contribution only inside this bounded program. This gives all
requested lengths L<=span after one compile. A larger length or an unregistered target
raises an error; it is not silently interpreted as zero.

### All dyadic cuts from the bounded index, without the aligned-width restriction

If the period r is known, put g=gcd(r,2^j), s=r/g. A target with canonical exponent e lies
in <a^(2^j)> exactly when g divides e. Its exponent in that subgroup is

    (e/g) * (2^j/g)^(-1) modulo s.

The inherited `cyclic_terminal_value` computes the response. If no period was seen up to
span, then within a master N<=span every relevant exponent is unique; simply require its
actual bounded exponent to be divisible by 2^j and apply the scaled weight. Thus this
backend handles every requested cut j<=m once N=2^m<=span, not only aligned shallow cuts.

This is an exact finite-domain compiler for a known classical mechanism, NOT an improved
generic order-finding algorithm. It deliberately refuses to answer a larger family than
the one for which its exponent evidence is sufficient. Missing logarithms are not a global
subgroup-nonmembership proof unless an entire period was actually covered.

The retained index contains matched exponent records and a domain/period bound; the large
baby table is discarded after compilation. The returned object is local typed data, not
an authenticated external certificate. Read-only mappings prevent accidental mutation.

## 5. Actual checks and costs

Python 3.13.5, Linux x86_64, sparse local source environment.

- 40 new targeted tests + 53 inherited tests = 93 PASS.
- 23,280 varying-window observations checked against independent exponent occupancy.
- 64,692 cut observations checked against unchanged suffix code.
- 1,164 no-oracle classical comparison batches checked.
- 582 compiled-index batches checked; further all-width/empty/nonunit/repeated-state,
  period-closure, query-outside-domain, invalid-type and budget tests are in pytest.
- Explicit prefix histograms from actual forward evolution were contracted against the
  responses and matched final full evolution, with construction work separately recorded.

All benchmark calls below include construction/compilation and query evaluation, and discard
the index after the call. No saved warm index is credited as a free setup. Timings are medians
of seven complete calls after one warmup; Python allocation peaks are measured separately,
not RSS. Shared input target generation is outside all timings; validation, sorting, building,
matching and output inside each callable are timed. Small timings are host-sensitive.

### Varying windows

| n,a; queries | old grouped windows ms | shared moments ms | compiled bounded index ms | full order + shared logs ms | lightweight bounded reference ms |
|---|---:|---:|---:|---:|---:|
| 100160063,2; 32x8=256 | 17.9773 | 0.8719 | 0.6017 | 2.5728 | 0.5591 |
| 65537,3; 64x16=1024 | 35.5723 | 1.8356 | 1.2891 | 0.9797 | 1.1162 |
| 10007,5; 32x32=1024 | 19.0884 | 2.0017 | 1.2762 | 0.7692 | 1.2266 |

Exact old/shared-moment scan counts: 113763/4096, 227450/4096, 112821/4062.
First batch peak allocations: 556232 / 303244 / 203788 bytes for old/moments/compiled.
But shared-moment peak allocation INCREASED in the latter two batches (556552->585884 and
537712->646604), because query caches and outputs cost memory. Do not infer RAM reduction
from scan reduction. Compiled index peaks were 203892 and 204176 bytes in those batches.

### Dyadic cuts

| n,a; cuts x states | old separate cuts ms | aligned moments ms | compiled bounded index ms | full order + shared logs ms | lightweight bounded reference ms |
|---|---:|---:|---:|---:|---:|
| 100160063,2; 11x8=88 | 8.8474 | 3.4652 | 1.5592 | 2.8413 | 1.5808 |
| 65537,3; 9x16=144 | 2.3381 | 0.9236 | 0.5187 | 0.4553 | 0.4727 |
| 10007,5; 7x32=224 | 2.3165 | 1.0635 | 0.5165 | 0.3758 | 0.5509 |

Exact old/aligned-moment scan counts: 54747/16384, 13439/4096, 12841/4096.
The small compiled/reference timing reversals are not evidence that a typed wrapper beats
its underlying classical algorithm. For short-order/dense queries, computing full order and
sharing logs remains cheaper in these samples. For short windows inside a much longer order,
bounded work avoids unnecessary global order discovery. This is task scoping, not a new DLP
complexity advantage. All raw samples and separate allocation peaks are in results.json.

### Charge real prefix construction; do not invent a use for many copies of the same final K

For cuts (0,2,4,6), actual prefix construction takes 120 source-row updates, retains 166
prefix records across the cuts, and exposes 127 distinct response states. At n=1009,m=12,
build+query+contract took 0.7860ms versus full forward propagation 2.1731ms; at n=10007,m=16,
1.5295ms versus 24.3228ms. However a SINGLE direct terminal query already returned the same
final scalar in 0.0846ms and 0.1571ms. Therefore multi-cut contraction is wasteful when the
only desired output is that one common final K. Its value is separately requested stage
responses, diagnostics or alternate prefix inputs. Prefix cost is not waived by batching.

## 6. Literature/data-source execution and limits

The official Sage generic-group documentation describes BSGS with bounded discrete logs,
soft square-root interval time/space, and separate order-from-bounds operations:
https://doc.sagemath.org/html/en/reference/groups/sage/groups/generic.html
This was retrieved in this turn as primary implementation documentation. The present batch
bookkeeping and dyadic offset specialization are not claimed as historically first.

The current academic query route was also actually executed: KQB request Issue15, batch
9a772487-fbd8-4a91-9815-88214568333f, same-turn ID cf65989d-ca61-41ae-adf5-efe76c7b5b73,
one arxiv/paper_search job for discrete logarithm / multiple targets / precomputation.
Matched response comment5763803004 preserves the submitted SHA256. It reports one provider
query, job PARTIAL, batch FAILED, and three title/abstract records. They concern image coding,
fractional neural operators and Paillier batch embeddings, NOT evidence for the theorem or a
relevant multiple-DLP benchmark. None is used as mathematical support; no full paper was read.
This is a real but unusable search result, not an unperformed search or a positive literature
coverage claim. The request, observed-response reference and discrepancy are retained.

## 7. Publication/reproduction and next useful boundary

Candidate module: `src/enterprise_math/group_ring_batch_response.py`.
Reproduction:

    PYTHONPATH=src pytest -q tests/test_group_ring_batch_response.py tests/test_group_ring_terminal_response.py tests/test_group_ring_inverse_quotient.py
    PYTHONPATH=src python research_notes/power_batch_cuts_20260922_16243626C61A/validate.py

The source, tests, reports and raw measurements are pinned by MANIFEST.json. The standalone
bundle includes unchanged references and the earlier prototype history. Persistence does
not change theorem/admission status. No RSA-270 execution, full repository tests, independent
review, Lean, quantum speedup or generic sub-BSGS bound is claimed.

This selected unit is complete: cross-window reuse, aligned cross-cut reuse, and an explicitly
bounded shared classical index are constructed, checked and compared. A next research unit
should address a specified nonuniform prefix/weight family or a certified pruning constraint
that changes the number of necessary matches, rather than repackage BSGS again. Pure output
batching alone cannot remove the underlying group-search cost or the Omega(output) cost.
