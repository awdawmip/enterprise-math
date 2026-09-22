# POWER feedback VIII: upper-band support certificates and bounded-error readouts

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`
Researcher-ID: `EM-DIRECT-16243626C61A`
Session: `local-power-review-16243626C61A` (same local continuation key, not a service session)
Progress-Event-ID: `power-highband-margins-20260922-16243626C61A`
Status: `PROVED_SCOPED_DERIVATIONS_AND_EXECUTED_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`
Frozen research source: `awdawmip/enterprise-math@d7e42375f863fae137b4e810b73a8cb3f610ade0`.

## 1. Scope and actual reuse

Continue the prior residual: certify large custom supports more cheaply, and distinguish
exact injectivity from robustness to an explicitly bounded readout error. The fixed support
S lies in [0,H]; the hypothesis set is all abstract periods 1..H and one above-H class.
Underlying weights are positive integer multiplicities, not amplitudes. The first result
preserves ALL reweighting collision observations on S. It does not assume extra ambient
order/character information, adaptive new probes, or physical sensor properties.

The previous `group_ring_sparse_identifiability.py`, blob
`35567d80b1b0f1bb864f381cc0ee7b4613d0273a`, executes UNCHANGED. Its difference_set,
period_closures, labeled_collision_gcd, compile_sparse_codebook and verify_codebook are
actually used. The new module imports its exact types/validators, including pinned internal
helpers: this is an extension of the existing T0/T4/T6 sparse observer interface, not a new
family, general order algorithm, or independent review of our earlier work.

Prior criterion, applied here:

    c_D(r) = gcd{d in D : r divides d}, gcd(empty)=0,
    D = {s_j-s_i : i<j}.

All hypotheses are identifiable iff c_D(r)=r for every r<=H. The following theorem removes
the need to sweep all candidates and all their multiples just to decide that property.

## 2. Exact upper-band theorem

For ANY D subset {1,...,H}, the following are equivalent:

    (A) c_D(r)=r for every r=1,...,H;
    (B) {floor(H/3)+1,...,H} is a subset of D.

Proof of necessity. Take r>H/3. If r is absent, its only possible visible proper multiple
is 2r. Thus c_D(r) is either 0 or 2r, never r. Every such r is compulsory.

Proof of sufficiency. Descend from H to 1. Above H/3 the actual lag r is present, hence
the gcd of the visible multiples equals r. For r<=H/3, both 2r and 3r have already been
proved fixed points. E_D(2r) and E_D(3r) are nonempty subsets of E_D(r), so

    c_D(r) divides gcd(c_D(2r),c_D(3r)) = gcd(2r,3r) = r.

Every member of E_D(r) is itself a multiple of r, giving the reverse divisibility.
Consequently c_D(r)=r. This closes the descending induction, including H=1,2.

Equivalently, the compulsory upper band is the unique inclusion-minimal set that generates
all integers 1..H under gcd. This finite statement does not claim historical priority.
For actual support differences the theorem gives an exact support criterion, not merely a
sufficient ruler construction. Low lags may be omitted, as the earlier H=9 example lacking
lag3 already demonstrated.

### Constructive failure witness

For any missing r>H/3, test only whether 2r occurs as a difference. If yes, periods r and
2r have identical visible signatures {2r}. If not, period r has the same empty signature
as above-H. This produces a concrete alias without evaluating all c_D values. It remains
structural aliasing under EVERY positive reweighting, not failure of just one profile.

### Sharper fixed-observer mark bounds

For k marks, distinct compulsory differences imply

    k*(k-1)/2 >= H-floor(H/3).

Also every lag >H/2 must be a cross-pair between the two halves of [0,H]. There are at most
floor(k^2/4) such pairs, hence

    floor(k^2/4) >= ceil(H/2).

In particular k >= ceil(sqrt(4*ceil(H/2))), approximately sqrt(2H). This improves our prior
simple half-band pair count, but is not asserted optimal. It is NOT a lower bound for all
order algorithms, adaptive probes, arbitrary exponent magnitudes, or factorization.

## 3. Executable certification: boolean, reusable certificate, actual observation

`high_band_identifiable` executes the old difference_set and counts its distinct compulsory
lags. Equal cardinality H-floor(H/3) establishes coverage because all counted lags are in
that band. Cost is O(k^2) pair construction with no H-candidate array or divisor sweep.
It is the fastest of the new tested paths when only a boolean is needed.

For a support described by R disjoint, sorted, maximal CLOSED INTEGER runs I_i=[l_i,h_i],
the cross-differences I_j-I_i are every integer in [l_j-h_i,h_j-l_i]. Within one run they
are 1..h_i-l_i. This is an exact full interval, not a convex-hull approximation to arbitrary
sparse marks. `certify_runs` builds/sorts these run-pair difference intervals and covers
only the compulsory upper band. Its published positive witness lists run-pair indices.
`verify_support_certificate` checks that they cover the band without gaps.

Construction: O(R^2 log(R+1)) time and O(R^2) transient records. Positive verification:
O(R + witness length), plus integer bit costs. A negative certificate uses one missing
compulsory lag; its absence and presence/absence of its double are verified by intersecting
S with S+d using two sorted interval cursors, O(R). A supplied run-pair budget returns
BUDGET_EXHAUSTED with no certificate, never structural impossibility.

An explicit k-mark input first costs O(k) to read/convert to runs. If nearly all marks are
isolated, R is about k and sorting can be more expensive than the direct boolean test.
A symbolic two-run example with H=10^30+2 was certified with three run-pair evaluations and
one covering witness. It describes about 2H/3 marks: NO modular powers for those marks were
computed. Compact combinatorial certification is not free generation of the observations.

`order_from_certified_support` binds an ACTUAL explicit support to a verified positive
certificate and executes the original labeled_collision_gcd. Its k modular exponentiations
are charged. Only on the identifying support is a nonzero gcd the exact order; zero means
order>H. This adapter refuses mismatched supports and negative certificates. It does not
turn arbitrary observed gcd multiples into exact orders.

## 4. Bounded-error and marked-erasure theorem

A verified finite codebook supplies C=H+1 code vectors z_r. Use either exact raw masses or,
coordinatewise, z_rj=K_rj/M_j^2 where M_j=sum_i w_ij is the declared total mass. The caller
must select this scale explicitly. Define

    delta = min_(r!=s) max_j |z_rj-z_sj|.

For additive error bounded by epsilon in EACH retained coordinate, every admissible readout
has a unique hypothesis iff 2*epsilon<delta. Sufficiency is the triangle inequality. For
necessity, the midpoint of a closest pair lies in both closed error boxes when
2*epsilon>=delta. Midpoints and all bounds are exact rationals in the implementation.

After at most e MARKED channel erasures, sort each pair's absolute coordinate gaps in
nonincreasing order g1>=...>=gt. The worst residual gap is g_(e+1), attained by deleting the
e largest gaps. Therefore replace delta by

    delta_e = min_(r!=s) g_(e+1)(r,s).

The same strict 2*epsilon<delta_e criterion is necessary and sufficient. This is not a
claim for unmarked adversarial channel corruption, independent random noise, missing
exponent observations, or physical measurement processes. If delta_e=0, even zero-error
unique decoding can fail for an allowed erasure pattern.

`certify_readout_margin` invokes the original full codebook verifier before computing exact
margins. Scalar margins require sorting and C-1 neighboring comparisons; multichannel
margins currently require choose(C,2) pair comparisons and sorting t gaps per pair. The
explicit cap bounds margin comparisons, not the separate existing codebook validation cost.
`verify_readout_margin` recomputes and rejects inflated/forged gaps.

`decode_bounded_readout` returns ALL hypotheses inside the declared error box. Its states
are unique-conditional, above-horizon-conditional, AMBIGUOUS and INCONSISTENT, not a forced
nearest-neighbor answer. Float/NaN inputs and unmarked erasure shortcuts are rejected.
The O(H) codebook and its validation remain charged. A unique result is conditional on the
supplied error bound and genuine readout; the code does not authenticate a measurement.

## 5. Permanent margin witness and scaling limitation

The prior H=6 support (0,1,2,3,6), weights (47,14,65,1,66), has raw codes

    37249,31909,17417,19567,12835,17191,10987.

The minimum gap is 226, between periods3 and6. Absolute errors <=112 are universally safe.
At epsilon=113, midpoint17304 is compatible with both periods. With epsilon=112 that same
midpoint is inconsistent, not a reason to guess either period. Tests cover these boundaries.

The total weight is193. Normalized separation is226/37249. Scaling every weight by10 scales
raw codes and their gap by100, but leaves normalized codes and gaps EXACTLY unchanged.
Fixed absolute-noise behavior can change with scale; relative-to-total-mass-squared behavior
cannot improve by this rescaling. Added dynamic range/bit costs are not free.

More generally, a single normalized channel lies in [b,1], b=sum_i w_i^2/M^2>=1/k.
There are H gaps between H+1 ordered distinct scalar codes, so

    delta <= (1-b)/H <= (1-1/k)/H.

Thus scalar exact injectivity alone cannot give a uniform positive normalized error radius
as H grows. Multiple independent observers may improve separation, but their computation,
channel count and erasure behavior must be assessed separately. No random-noise or
noise-resistant hardware claim is made here. The tested nonzero errors are deliberately
bounded synthetic readout perturbations, not measured physical residuals.

## 6. Validation and matched support-certification costs

Python3.13.5, local sparse checkout. 33 new +165 inherited tests =198 PASS.
Additional reproduction checks:

- 131070 arbitrary lag sets for H=1..16 versus direct gcd fixed points;
- 16368 nonempty supports for H=1..12 versus unchanged period_closures;
- 14356 constructive negative aliases, plus500 randomized larger supports;
- 15715 actual modular-group/horizon cases using certified-support order and brute order;
- 4012 exact bounded-error box checks,11 explicit erased-channel subset checks, and
  midpoint/forgery/scaling/erasure-cap tests.

All benchmark methods answer the same support-identifiability boolean. The support input
is preexisting in every method. New construction includes run extraction, interval generation,
sorting and verification. Timings are seven-call medians after one warmup; allocation tracing
is separate, not process RSS. Warm verification excludes already retained certificate setup.

| H; marks/runs | old divisor sweep ms | direct high-band ms | construct+verify run certificate ms | warm verify-only ms |
|---|---:|---:|---:|---:|
|4096;128/64|2.682798|0.444198|0.661996|0.031598|
|16384;256/128|12.425359|1.946820|2.453322|0.062735|
|65536;512/256|63.125516|7.912287|10.443096|0.127863|

For H65536, peak Python allocations old/direct-band/run-construct were7886448/4189100/2016320
bytes. Warm verify allocated2872 additional bytes EXCLUDING its retained certificate.
Published positive witnesses used43,86,171 run pairs for these three supports.
The simple direct test remained faster than constructing a certificate; choose the latter
for portable repeated verification or compact run inputs, not as a universal faster default.
These numbers measure SUPPORT CERTIFICATION, not order-finding or RSA performance.

## 7. Literature and provenance

Reused the prior topic-specific Scholar metadata at KQB Issue377/comment5775500566, through
the inherited literature observation; no new dedicated provider request was submitted.
Its job was PARTIAL/batch FAILED and the returned scope was three related snippets/metadata,
not full text. Current official arXiv HTML2408.16335v2 (Saarela/Vanhatalo, definitions in
section3) and1911.08015v1 (Lawrence et al., ruler context) were consulted as classical context.
The present high-band theorem has a self-contained proof; no priority claim follows from
an unproductive keyword search. Bounded-distance decoding uses the standard half-distance
principle, proved above directly for this finite exact codebook. No lattice hardness or
covariance/noise theorem is transferred to modular order finding.

Sources: https://arxiv.org/html/2408.16335v2 ; https://arxiv.org/html/1911.08015v1 .
The inspected abstract https://arxiv.org/abs/2003.07903 is only broader bounded-decoding
context, not evidence for a new complexity bound in this result.

## Reproduction and remaining scope

    PYTHONPATH=src pytest -q tests
    PYTHONPATH=src python research_notes/power_highband_margins_20260922_16243626C61A/validate.py --out results.json

Exact source/test/result hashes are in MANIFEST.json. This sparse checkout test suite is
NOT the full Enterprise Math repository suite. No RSA-270, Lean, independent Driver review,
Foundation admission, or generic sub-BSGS result. P000/protected worldview unchanged.
The existing no-run activity is preserved; a current read-only status request confirms no
service session. Its transport status is not native final permission. Actual PRE_FINAL
attempt/readback and publication provenance belong in the delivery record, not fabricated
formal Task/CLAIM/ER fields.

The selected cheap-support-certificate and bounded-readout-margin unit is complete at this
finite scope. Remaining mathematics includes optimizing supports for mandatory high-band
coverage and designing normalized multi-channel margins under explicit cost/erasure limits.
Those optimizations are not solved by scaling weights or repeating an exact injectivity test.
