# POWER feedback IX: cheaper mark designs and exact mark-erasure cuts

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`  
Researcher-ID: `EM-DIRECT-16243626C61A`  
Session: `local-power-review-16243626C61A` (continuing local provenance, NOT a service session)  
Progress-Event-ID: `power-tail-design-20260922-16243626C61A`  
Status: `PROVED_SCOPED_DERIVATIONS + EXECUTED_FINITE_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`  
Frozen research Source: `awdawmip/enterprise-math@6e9f0150600c81ae2289391bf3b83a442c463ed3`.

## 1. Question, observer and actual reuse

Optimize the number of exponent positions in the preceding exact support criterion, then
measure what happens when positions are actually lost. Fix S inside [0,H], with all abstract
periods 1..H and a single above-H hypothesis. Observe labeled modular-power equalities or a
suitably verified positive-weight collision code. No extra ambient-group facts are supplied.

The prior theorem says S is identifying iff its positive differences contain every integer
floor(H/3)+1,...,H. This theorem is applied, not re-counted as new work. The old modules execute
UNCHANGED: group_ring_support_certificates.py (blob 5a2fa6a7bd8e24a190709045365312ec7d307d29),
group_ring_sparse_identifiability.py (35567d80b1b0f1bb864f381cc0ee7b4613d0273a), and the classical
bounded comparator group_ring_batch_response.py (82c87f779a07b84de601d54ebd04d3bfb1856f92).
Actual calls include high_band_identifiable, period_closures, labeled_collision_gcd,
sparse_ruler, ruler_order and compile_terminal_index. New code is a T0/T4/T6 domain extension,
not a new toolbox family. P000 and physical/worldview semantics are unchanged.

Important typing: deleting marks changes the numerical collision masses. We preserve
identifiability of the declared period hypotheses, NOT every old weighted mass or arbitrary
future observations. Mark erasure below is NOT erasure of a scalar readout channel, noisy
residue corruption, or an authenticated physical failure process.

## 2. A smaller constructive upper bound

Put W=H-floor(H/3), b=floor(sqrt(W)), q=ceil(W/b), and take

    S = {0,...,b-1} union {H-j*b : 0<=j<q}.

The cross differences H-j*b-i, 0<=i<b, fill the contiguous interval
[H-q*b+1,H]. Since q*b>=W, this contains every compulsory lag. The coordinates are legal:
H-(q-1)b>H-W>=0; both endpoints belong to S. Thus S is identifying for every H>=1.

Its cardinality is at most b+q=ceil(2*sqrt(W)). To check the last equality exactly, write
W=b^2+t with 0<=t<=2b. The sum b+ceil(W/b) is 2b when t=0, 2b+1 for 1<=t<=b, and 2b+2
otherwise; these are precisely the ceiling values of 2*sqrt(W). Overlap can only reduce
cardinality. The asymptotic upper coefficient is sqrt(8/3), versus 2 for the earlier simple
complete block ruler. This is a stronger bound for the WEAKER upper-band task, not a better
construction of a complete ruler or a generic order-finding complexity improvement.

Examples (old simple complete ruler -> new construction):

    H=4096: 128 -> 105 marks
    H=16384: 256 -> 210 marks
    H=65536: 512 -> 419 marks

The old necessary bound remains approximately sqrt(2H). No global/asymptotic optimality is
proved here. tail_ruler_parameters is a compact exact descriptor; tail_ruler explicitly
charges/limits expansion. tail_ruler_order executes the inherited labeled collision routine
on the generated support, paying k modular exponentiations, not magically k unit-cost probes.

## 3. Safe deletion and finite optimum evidence

A single-pass deletion routine keeps a multiplicity count for each compulsory lag. For a
candidate mark x, count its incident pairs separately: a centered arithmetic progression
may contribute TWO pairs of the same difference, so decrementing only once is unsound.
Delete x only if every affected lag retains at least one pair.

Once x is rejected, some compulsory lag has ALL surviving pairs incident on x. Further safe
deletions cannot create a pair not incident on x; at least one such pair must survive.
Therefore x remains essential. One pass in any fixed permutation ends at an inclusion-minimal
support (relative to explicit protected marks), using O(k^2) pair/incident visits and worst-case
O(k^2) stored lag records. The returned essential-lag witnesses are verified and the preceding
high-band checker is actually executed. No minimum-cardinality approximation ratio is claimed.

Permanent non-optimality witness: H=19, our default construction/pruning keeps
(0,1,2,7,10,13,16,19), eight marks, all locally essential. But
(0,1,2,9,13,16,19) uses seven marks and is identifying. Never relabel inclusion-minimal as optimal.

A standalone deterministic C++17 enumerator exhaustively tested increasing cardinalities,
fixing mandatory endpoints 0,H. Safe pair-count and cross-half-count lower bounds skip only
impossible sizes. It stops explicitly with BUDGET_EXHAUSTED, not UNSAT, when capped.
The local run visited 32,211,153 recursive nodes and completed all 86 rows:

- exact upper-band minima for H=1..34;
- exact complete-ruler minima for the same H;
- exact one-INTERNAL-erasure-tolerant upper-band minima, endpoints protected, for H=3..20.

All returned supports were checked by separate Python routines; 37 minima at H<=13 were
also independently exhausted in Python. This is executable finite enumeration evidence,
not a formally checked unsatisfiability certificate. Raw per-cardinality traces are in
exact_minima.json in the bundle and are regenerated by the published exact_search.cpp and
validate.py. A single finite table is not an asymptotic optimum theorem.

Selected minima: H10:5 identifying /6 complete /8 tolerating one internal loss;
H15:6 /7 /9; H19:7 /8 /10. At H10, a minimum identifying set is (0,1,6,8,10), with lag3 missing.
A minimum single-internal-erasure set is (0,1,2,3,4,5,9,10), protecting 0 and10.
These are three DIFFERENT design objectives, not a single benchmark with interchangeable outputs.

## 4. Exact smallest destructive MARK erasure

Declare protected marks P subset S. For each compulsory lag d, form G_d with vertices S and
an edge {x,x+d} whenever both positions are present. Losing a set F of unprotected marks
destroys this lag exactly when F meets every edge: F is a vertex cover using only S\P.
Let tau_P(G_d) be the minimum allowed cover size, with infinity when a fully protected edge
cannot be destroyed and zero when the lag is already absent. Then

    minimum destructive mark erasure = min_(d>H/3) tau_P(G_d).

Consequently every deletion of at most e UNPROTECTED marks preserves structural identifiability
iff this minimum is greater than e. A positive-weight scalar decoder may still need redesign
or revalidation after losing marks; this theorem does not certify the old codebook unchanged.

Why this is cheaply executable here: edges at one integer distance form paths, and d>H/3
forbids four vertices in one component, because their span would be at least3d>H. Thus each
nontrivial component has just two or three vertices. Check its at most8 deletion subsets,
respecting protection, and sum minima over disjoint components. A protected edge makes the
whole lag indestructible. Pair construction dominates at O(k^2); component sorting gives a
conservative O(k^2 log(k+1)) total bound, plus integer/input costs. No 2^k erasure sweep is
used by the new certificate. An explicit minimizing erasure set and the lost lag are returned.

Permanent redundancy trap: S=(0,1,2,3,6),H6 has two representations of lag3: (0,3) and(3,6).
Deleting the SINGLE unprotected mark3 removes both and aliases periods3 and6. Counting
representations alone is not a failure-tolerance certificate.

### Endpoint obstruction and a constructive protected case

Without protection, EVERY identifying support in [0,H] loses full identifiability after one
adversarial deletion: difference H has only pair(0,H). There is no alternative support inside
the same span that removes this bottleneck. This statement is scoped to the fixed hypothesis
family, not to adaptive probing or using a larger exponent span.

Protecting only 0,H changes the task. For H>=3, even the FULL support cannot tolerate TWO
arbitrary internal deletions: remove1 and H-1, destroying lag H-1. The full support DOES
survive one internal loss. For d>H/2 except H there are at least two disjoint edges; for
H/3<d<=H/2 the full graph has d>=2 nontrivial path components. Thus its exact destructive
threshold is2. Protection is an explicit reliability assumption, not a guarantee supplied
by the arithmetic or by this chat.

These obstructions do not discard imperfect supports. The certificate identifies the actual
weak mark/lag and states the surviving scope; it distinguishes deliberate safe deletion,
noise bounds, channel loss and mark loss instead of conflating them.

## 5. Validation and same bounded-order costs

Python3.13.5, Linux x86_64, inherited sparse local checkout. 35 new +198 inherited tests=233 PASS.
Additional reproduced checks:

- 1000 constructed horizons, 11325 inherited candidate closures;
- 8140 support/protection combinations vs exhaustive allowed-mark deletion;
- 600 independently verified inclusion-minimal reductions, including all essential witnesses;
- 14930 actual modular-group/horizon order comparisons, with no order supplied;
- 86 completed finite minimum rows, 37 independently enumerated Python minima;
- forged/capped certificates, huge symbolic descriptor, missing/protected/duplicate/noninteger
  inputs, greedy nonoptimality and changed-old-mass regression cases.

Same bounded-order output, single-host seven-call complete medians in milliseconds.
Support construction is inside all applicable calls; allocation tracing is separate, not RSS.
Rows named pow use the SAME unchanged labeled_collision_gcd, so both pay one pow per mark.
Other rows are stronger classical baselines; fewer marks alone is not a universal time win.

| n,a,H | old/new marks | old pow | tail pow | old optimized block | bounded BSGS |
|---|---:|---:|---:|---:|---:|
|100160063,2,4096|128/105|0.051378|0.050196|0.018958|0.016815|
|100160063,2,65536|512/419|0.313172|0.271689|0.079379|0.049805|
|65537,3,65536|512/419|0.291138|0.276156|0.079149|0.048073|

Samples exhibit host scheduling outliers; all seven raw timings are preserved. On the last
row, old/tail pow Python peaks were57960/48568 bytes, vs41936 for bounded BSGS. The generic
pow wrapper is slower than the optimized classical comparators. Claim the proved mark-count
reduction and exact failure test, not a fast default solver, RSA result or sub-BSGS algorithm.

## 6. Literature and provenance

Sparse rulers/restricted difference bases and array-failure robustness are prior research
areas. Primary arXiv HTML2408.16335v2, section3.2, gives Wichmann constructions and the bound
sqrt(3H)+4 for COMPLETE rulers. This was read as context; our high-band task is different and
no historical-priority claim is made. arXiv2509.07442v1 abstract reports hidden dependencies
in redundant sensor arrays. It is context only, not a transferred measurement theorem.

Dedicated Scholar query was really submitted: KQB Issue446, batch8385bbc1-d1e2-453b-96a8-330a4bf90a98,
matched comment5776638304; one provider call, jobPARTIAL/batchFAILED, three title/snippet records.
They point to Liu/Vaidyanathan2019 PartsI/II and2018 optimization work. The attempted official
NSF PartI full-text fetch timed out; do not claim it was read. The extracted observation and
exact request are retained, with original raw response recoverable at the matched Issue.
The proofs here are self-contained scoped specializations, not novelty assertions based on
an incomplete literature search.

## Reproduction, status and remaining frontier

    PYTHONPATH=src pytest -q tests
    PYTHONPATH=src python research_notes/power_tail_design_20260922_16243626C61A/validate.py

validate.py compiles/runs exact_search.cpp locally and regenerates exact_minima.json.
No GitHub Actions/remote scientific executor. Source publication is candidate provenance;
no formal Task/CLAIM, independent review, Lean, Foundation or full EM suite is claimed.
The legacy no-run PRE_FINAL incompatibility from Issue441 is not repaired or bypassed by
this mathematical work. No fabricated Driver/maintenance role or parent-completion claim.

The finite design/mark-loss unit is implemented. The gap between the sqrt(2H)-scale lower
bound and sqrt(8H/3)-scale constructive upper bound remains. Another explicit next question
is how changing the exponent-span/hypothesis-span relation or providing a specified protected
core changes the minimum robust mark count. Neither can be settled by relabeling this finite
search or scaling weights. All source/test/measurement hashes are in MANIFEST.json.
