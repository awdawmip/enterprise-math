# POWER feedback X: minimum expanded span and unprotected mark erasures

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`  
Researcher-ID: `EM-DIRECT-16243626C61A`  
Session: `local-power-review-16243626C61A` (continuing local provenance, not service authority)  
Progress-Event-ID: `power-span-erasures-20260923-16243626C61A`  
Status: `SELF_CONTAINED_SCOPED_PROOFS + EXECUTED_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`

## 1. Different spans require a different hypothesis interface

The preceding unit fixed both exponent span and target-order horizon to H, and proved
an unavoidable unprotected-endpoint failure. Here S is a finite subset of [0,A], while
only orders1..H must be identified individually. All orders greater than H share an OUTPUT
label, not necessarily an observation: when A>H, order4 and order5 on S=0..4 already have
different equality patterns although both are above H=3. The algorithm never treats every
above-H order as a collision-free state.

Observe labeled equalities between a^x, x in S, or the entire family of positive-integer
reweighting collision masses. No ambient order restriction, hidden discrete log, adaptive
new probe or protected mark is assumed unless explicitly supplied. Erasures remove known
positions; retained modular values are exact. This is not noisy residues, channel erasure,
random failure, a physical sensor guarantee, or preservation of every old numerical mass.

Actual reuse: group_ring_sparse_identifiability.py (blob35567d80b1b0f1bb864f381cc0ee7b4613d0273a)
and group_ring_support_design.py (8efcf8a936cfe2ed5b2799cb6e9d3fe2ac96c889) execute UNCHANGED.
Their difference_set, labeled_collision_gcd, validators and fixed-span erasure checker
are imported/executed. The exact prior c_D law is applied. This is a T0 positive-mass /
T4 collision / T6 observer-specific extension; no new top-level tool family or promotion.
The prior support-design source is 0e1357b6dcc47ec93de1d3541744a0d3c9139272; its module and
activity were confirmed unchanged at current-control Source2d9b3b67673fceb17b481d71a9f5906f74e67bad.
Global startup used e77af3f4fcd01bbe8798eb6f3a02b1f0708819f0; P000 is unchanged.

## 2. Target-only identifiability and prime coarsening

Let D be all positive differences in S. The old exact label remains

    c_D(r)=gcd{d in D:r divides d}, with gcd(empty)=0.

Identification of every r<=H against every different order (including orders>H) is equivalent
to c_D(r)=r for every r<=H. Necessity: c=0 aliases an order>A; c>r aliases the actual integer
candidate c<=A. Sufficiency: equal signatures give equal closure labels. If c_D(r)=r and
c_D(s)=r, then s|r; a smaller s is also <=H and its fixed-point condition forces s=r.
The old mandatory-H/3 band remains SUFFICIENT when it is present among these differences,
but it is not necessary when longer differences up to A are available.

There is a useful finite failure basis. Losing this property means that for some r<=H,
either c_D(r)=0, or a prime p divides c_D(r)/r. In either case the surviving equality
partitions for r and p*r coincide; p=2 suffices for empty c. Thus it is enough to test

    r versus p*r,  1<=r<=H,
    p prime with p*r<=A, and p=2 always.

No arbitrary pair-of-period sweep is needed. General sparse supports may NEED odd primes:
S=(0,1,3,6), H=1, A=6 becomes aliased between1 and3 after deleting1; checking parity only
would miss this smallest destructive deletion.

For a fixed r,p, group marks by residue mod r, then by residue mod p*r. To make both
partitions identical, survivors in each coarse residue must occupy at most ONE fine class.
With no protected marks, the exact deletion cost is

    |S| - sum_(coarse residue c) max_(fine residue f) |S intersect f|.

An explicit optimum keeps the largest fine class in every coarse class. With a protected
set P, two protected fine classes in one coarse class make this coarsening impossible;
one protected fine class forces that choice; otherwise keep a largest class. This proves
the exact least permitted destructive deletion after minimizing over the finite basis.
A certificate contains an actual deletion and the aliased periods, or infinity if the
protected core already prevents every failure. Zero means initially nonidentifying.

certify_span_erasures implements this complete-multipartite vertex-cover law. It does not
enumerate 2^k deletion subsets. Its sieve costs O(A) memory, and its main mark-visit count
is k*sum_(r<=H) max(1,pi(floor(A/r))); dictionary, sorting, input and integer bit costs
remain. Explicit sieve/visit caps refuse with BUDGET_EXHAUSTED and no asserted certificate.
This general routine is not claimed faster than the old special fixed-span graph checker.

## 3. Exact minimum span for arbitrary unprotected erasures

The full interval I_A={0,...,A} dominates every S inside it: if deleting F makes two periods
indistinguishable on I_A, deleting F intersect S makes them indistinguishable on S. Therefore
the best POSSIBLE robustness at a fixed span is exactly the full interval's robustness.
This dominance is an information statement, not a recommendation to sample all those marks.

Put N=A+1. In a residue class mod r, the full interval has m consecutive r-spaced marks.
The largest mod p*r sub-class has ceil(m/p) marks. For p>=2 the cheapest destructive
coarsening is p=2, with floor(m/2) deletions. This remains valid when2r>A: the coarse
classes have at most two marks. Hence the full interval's exact destructive threshold is

    T(A,H)=min_(1<=r<=H) f_N(r),
    f_N(r)=r*floor(N/(2r)) + max(0, (N mod 2r)-r).

To survive every <=e erasures, require f_N(r)>=E=e+1 for every r<=H. Write E=q*r+t.
The first N with f_N(r)>=E is2q*r when t=0, otherwise(2q+1)*r+t. Equivalently it is

    N_r=E+r*ceil(E/r).

Thus the EXACT least span for ANY support satisfying this observer-only task is

    A_min(H,e)=e + max_(1<=r<=H) r*ceil((e+1)/r).

The full interval attains it. The formula certifies minimum SPAN, not minimum MARK COUNT.
For0<=e<H, it simplifies further:

    A_min(H,e)=e+max(H,2e).

Proof: r>=e+1 contributes r, with maximum H. For r<=e, r*ceil((e+1)/r)<=2e, and r=e
attains2e when e>0. Therefore A_min=H+e when2e<=H, but A_min=3e when H/2<e<H.
For general e the implementation groups equal floor(e/r), rather than scanning every
r if quotient blocks can be shared. It reports cap exhaustion, not a guessed optimum.

Concrete lower-bound witness: H=6,e=4 requires span12. Even the full interval0..11 loses
identification after deleting4,5,6,7: the survivors0..3 and8..11 give identical partitions
for periods4 and8. At span12 the full interval withstands every four deletions. The second
period is ABOVE the target horizon; excluding it from the audit would give a false result.

## 4. Span-optimal sparse construction without protected endpoints

For0<=e<=floor(H/3), let W=H-floor(H/3), choose1<=b<=W, and q=ceil(W/b). Thicken the
previous tail ruler by shifts0..e:

    S=[0,b+e-1] union union_(j=0..q-1) [H-j*b, H-j*b+e].

All intervals mean CLOSED INTEGER intervals. Span is A=H+e, already proved optimal in
this regime. For every mandatory d>H/3, write H-d=j*b+i,0<=i<b. The pairs

    (i+t, H-j*b+t), 0<=t<=e,

all lie in S and have difference d. Because d>e, their2(e+1) endpoints are DISTINCT.
After any e mark erasures, at least one pair for every mandatory d survives. The previous
high-band theorem then fixes every target closure to r, even though additional longer
differences can also exist. Neither endpoint is protected. Both can be erased together
when e>=2. No independent-copy assumption is made when translated supports overlap:
disjointness is proved separately for the e+1 witnesses of EACH lag.

The exact count bound is

    |S|<=b+e+(e+1)*ceil(W/b).

Choosing b=floor(sqrt((e+1)*W)) gives2sqrt((e+1)W)+O(e+1) marks. This is much smaller than
naively taking e+1 disjoint full ruler copies, and does not require a full interval.
No claim of minimum mark count is made, and this sparse proof is not extended to e>H/3.

| H | permitted losses e | minimum span | constructed marks | dense interval marks |
|---|---:|---:|---:|---:|
|4096|0|4096|105|4097|
|4096|1|4097|150|4098|
|4096|2|4098|185|4099|
|4096|3|4099|215|4100|
|65536|2|65538|727|65539|

robust_tail_order generates the support, validates actual marked erasures and calls the
unchanged labeled_collision_gcd on surviving modular powers. Nonzero gcd<=H is exact;
gcd>H OR zero returns above-H. It never claims above-H implies no collision. It pays one
actual modular exponentiation per survivor, plus construction/gcd/input work. No weighted
codebook is assumed to remain unchanged after deletions.

## 5. Necessary boundary strips and robust mark lower bound

At the optimal span H+e with0<=e<=H/2, the target lag H can only be represented by
(x,x+H),0<=x<=e. These e+1 pairs are disjoint. Every one is necessary to survive e losses,
so EVERY robust support at this span must contain BOTH boundary strips

    {0,...,e} and {H,...,H+e}.

They are compulsory SAMPLE LOCATIONS, not protected/unerasable locations. Extra redundancy
replaces the old endpoint protection assumption.

More generally every target r>(H+e)/2 needs at least e+1 pairs of difference r. Such pairs
cross the span midpoint, and a k-mark set has at most floor(k^2/4) cross pairs. Therefore

    floor(k^2/4)>=(e+1)*(H-floor((H+e)/2)),
    k>=2(e+1).

For fixed e and large H, this gives approximately sqrt(2(e+1)H) necessary marks, versus
our sqrt(8(e+1)H/3)-scale construction. The constant-factor mark-design gap remains.
This is a bound for this nonadaptive fixed-span equality observer, not all order algorithms.

## 6. Executed checks, costs and failures retained

Python3.13.5, Linux x86_64, inherited sparse source checkout from the user's verified bundle.
46 new targeted tests +233 inherited tests =279 PASS. Additional independent validation:

- 16343 arbitrary support/target/span cases against full labeled pair partitions;
- 404 protected-core cases against exhaustive allowed deletions;
- 2035 comparisons with the unchanged fixed-span erasure implementation;
- 45 full-interval thresholds checked by exhaustive deletion;
- 16512 minimum-span instances, each checking A_min and A_min-1;
- 1974 sparse constructions and267910 disjoint-lag witness checks;
- 497 complete small-pattern erasure enumerations;
- 13212 actual modular evaluations with no order supplied to the algorithm;
- 319 small-case forced-boundary-strip checks.

The independent test oracle initially omitted an extra above-H candidate when H>A. The
( H=4,A=3 ) regression exposed this BEFORE publication; the oracle now enumerates through
max(H,A)+1. Production already returned the correct zero robustness there. No hidden
experimental failure is counted as a passed test. A separate witness ensures prime3 is
not replaced by parity-only filtering on general supports.

A seven-call single-host measurement includes support construction, erasing both endpoints,
all surviving modular powers and gcd: n=100160063,a=2,H4096,e2, sparse185 marks took median
0.101953ms; dense4099 marks took2.162223ms. Full raw times are in results.json. This compares
two implementations of the SAME erasure-robust bounded query, not a speed claim against
optimized classical BSGS. No memory/RSS measurement or generic speed guarantee is claimed.
The expensive general arbitrary-support analyzer is unnecessary for the algebraically
certified construction; computing all its prime/coarse partitions would be avoidable work.

## 7. Literature, status and continuation

Reused the topic-matching dedicated Scholar response from KQB Issue446/comment5776638304,
2026-09-22: one provider call, selected metadata/snippets only, jobPARTIAL/batchFAILED.
No new provider query was issued for that same source search. Current web verification
read the publisher abstract for Liu/Vaidyanathan2019 PartI (DOI10.1109/TSP.2019.2912882),
which studies sparse-array failure robustness. This is prior context, not a full-paper
read, an assertion of historical novelty, or a transfer of covariance/sensor guarantees.
Publisher: https://ieeexplore.ieee.org/iel7/78/4359509/08695857.pdf (tool rendered abstract page).
The present finite proofs are self-contained. Search did not establish their prior-art status.

No full Enterprise Math test suite, RSA-270 run, Lean, independent Driver review, formal
Task/CLAIM, Working Truth or Foundation acceptance is asserted. Current control status
Issue917 succeeded with session=null; old direct-activity pre_final binding remains a
separate unresolved integration constraint. No role downgrade or fabricated run was used.

Reproduce:

    PYTHONPATH=src pytest -q tests
    PYTHONPATH=src python research_notes/power_span_erasures_20260923_16243626C61A/validate.py --out results.json

Next mathematical residue: reduce the robust mark-count gap while retaining the exact
minimum span; extend sparse constructions beyond e<=H/3 or combine explicit protected
cores with longer spans. Minimum span is now closed at the declared observation scope;
minimum marks, weighted readout robustness, and physical failures are NOT closed by it.
