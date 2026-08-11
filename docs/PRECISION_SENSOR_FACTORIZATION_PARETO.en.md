# CRT Sensor Factorization as a Precision Resource Pareto

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

A modular precision law does not determine one operational representation. Once the exact arithmetic content has been fixed, CRT allows that same precision to be distributed across many narrow channels or fused into fewer wider channels.

This creates a Stage131-style resource Pareto **inside one unchanged exact law**.

## 1. One arithmetic law, many exact factorizations

Let the required squarefree arithmetic content be

`L=p_1 ... p_k`

with distinct primes.

Partition the prime factors into nonempty groups

`B_1,...,B_g`

and define channel moduli

`M_r=product_(p in B_r) p`.

The M_r are pairwise coprime and

`product M_r = lcm(M_r) = L`.

CRT therefore gives

`Z/LZ ~= product_r Z/M_rZ`.

Every grouping has exactly the same equality/reflection precision. Only implementation resources change.

## 2. Two endpoint representations

### Fully fused

One channel mod L.

- channel count:1;
- widest arithmetic word;
- no CRT reconstruction if scalar mod-L output is required.

### Fully split

One channel per prime.

- channel count:k;
- narrowest atomic channels;
- maximum parallelism;
- possible CRT recombination cost if downstream requires one fused scalar residue.

Every intermediate grouping is another exact representation of the same arithmetic law.

## 3. Peak residue width

A modulus M requires

`b(M)=ceil(log2 M)`

bits to store one residue.

For a grouping define

`b_peak=max_r b(M_r)`.

Fusion reduces channel count but cannot reduce peak modulus/width. Splitting can reduce peak width until atomic factors or packing prevent further improvement.

## 4. Information lower bound for g channels

If g channels each fit in at most b bits, then every channel modulus is at most `2^b`, so

`L=product M_r <= 2^(bg)`.

Therefore

`b_peak >= ceil(log2 L / g)`.

This is the continuous information-balance lower bound.

## 5. Atomic-factor lower bound

Prime factors are indivisible in the declared factorization family. Some channel must contain the largest prime factor, so

`b_peak >= ceil(log2 p_max)`.

Combining the two:

`b_peak >= max(ceil(log2 L/g), ceil(log2 p_max))`.

The executable compiler records this lower bound for every grouping.

## 6. Sharp 210 reference frontier

Take

`L=210=2*3*5*7`.

Exact best groupings are:

- g=1: `210`, peak8 bits;
- g=2: `14 x 15`, peak4 bits;
- g=3: `6 x 5 x 7`, peak3 bits;
- g=4: `2 x 3 x 5 x 7`, peak3 bits.

All four optima hit the combined lower bound exactly.

Therefore the fully split four-channel representation is dominated by the three-channel representation: both have peak3-bit arithmetic, but three channels use one fewer channel.

The Pareto resource points are therefore

`(channels,peak_bits)=(1,8),(2,4),(3,3)`.

Splitting saturates before reaching the atomic endpoint.

## 7. Discrete factorization packing gap

The information/atomic lower bounds need not be attainable.

Take

`L=7*11*13=1001`

with g=2 channels.

The continuous information bound is5 bits and the largest-prime bound is4 bits, so the combined lower bound is5.

But three indivisible prime atoms must be packed into only two channels. One channel must contain at least two primes; the smallest possible pair is

`7*11=77`,

which needs7 bits.

Thus the true optimum is7 bits and the **factorization packing gap** is

`7-5=2 bits`.

This is a finite indivisibility defect: the total information budget appears sufficient, yet the primitive factor packing cannot realize the continuous balance.

The branch keeps this as an arithmetic packing phenomenon rather than identifying it with other project packing theorems.

## 8. Rounded total storage law

Ideal information is grouping-invariant:

`sum_r log2(M_r)=log2 L`.

With whole-bit channel storage,

`b_r=ceil(log2 M_r)`

and fused width

`B=ceil(log2 L)`,

one has

`0 <= sum_r b_r - B <= g-1`.

So splitting can sharply reduce peak width while pure rounding adds at most one bit of total residue storage per additional channel.

This theorem excludes metadata, routing, ECC, synchronization and other physical overheads; those are separate resources.

## 9. Conditional CRT reconstruction depth

A residue tuple already contains the complete arithmetic precision. If downstream semantics can consume the tuple directly, reconstruction depth is0 for every grouping.

If downstream instead demands one scalar residue mod L, g channels must be recombined.

With binary CRT merges:

- sequential depth: `g-1`;
- ideal balanced parallel depth: `ceil(log2 g)`.

Therefore factorization exchanges

`narrower peak arithmetic width`

against

`more optional scalar-reconstruction depth`.

The depth is **interface-dependent**: it vanishes for tuple-native consumers.

## 10. 210 width/depth curve

For the reference optimum groupings, if scalar reconstruction is required:

- one channel: `(peak bits, parallel depth)=(8,0)`;
- two channels: `(4,1)`;
- three channels: `(3,2)`;
- four channels: `(3,2)`.

Again the fully split point is dominated by three channels.

This is a literal storage/execution-depth Pareto for one unchanged exact arithmetic law.

## 11. Contiguous local-count capacity

For a local codebook

`{0,1,...,D}`,

a modular sensor family is exact iff its joint lcm L satisfies

`L>D`.

Hence its universal contiguous local-count capacity is exactly

`D_max=L-1`.

All CRT factorizations of the same L therefore have the same exact capacity.

The resource question begins **after** semantic capacity has been fixed.

## 12. Width × channel-count capacity law

If g channels have peak width at most b bits, then

`L<=2^(bg)`

and therefore

`D_max < 2^(bg)`.

So, in the ideal arithmetic bound, parallel channel count can compensate exponentially for per-channel residue width.

Discrete available prime factors determine whether that ideal capacity can actually be packed into the requested channel budget.

## 13. Fixed-channel optimum is a multiplicative load-balancing problem

For exactly g channels, minimizing peak modulus is

`min max_r product_(p in B_r) p`.

Taking logs converts this to balancing indivisible jobs with sizes `log p` across g bins.

The owner compiler exhaustively enumerates set partitions only for bounded research fixtures. No efficient generic optimization claim is made.

The packing-gap examples show why the continuous information bound is not always sufficient to determine the exact optimum.

## 14. Relationship to constrained sensor selection

The parent Set Cover generation chooses **which prime capabilities** are required from an allowed catalogue.

This generation assumes the selected prime factor set is fixed and asks **how to package those factors operationally**.

Thus precision design has at least two separate optimization layers:

1. semantic/capability selection;
2. arithmetic representation factorization.

Minimum selected capability and minimum-cost execution representation are not the same problem.

## 15. Stage131 interpretation

Stage131 began from the observation that the same closure law can trade rule-table storage against execution depth.

The CRT result supplies another exact instance of the same broader resource principle:

> the same exact precision law can be stored/executed in multiple semantically equivalent factorizations with different width, channel-count and reconstruction-depth costs.

Precision therefore has a **representation Pareto** even after mathematical exactness is fixed.

## Owner-local assets

- `src/enterprise_math/sensor_factorization_pareto.py`;
- `src/enterprise_math/sensor_factorization_execution_depth.py`;
- `src/enterprise_math/sensor_factorization_storage_law.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

CRT, factor grouping, set partitions, information-width bounds and load balancing are standard prior mathematics/CS. P023/A2 retains precision/future-signature ownership. This Draft owns only the explicit exact-precision factorization Pareto and Stage131 resource interpretation.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
