# S23/AV: exact linear block complexity, 79 right-special words, and optimal finite-history prediction error

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE / PROVED_DERIVATION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Prior verified author-side definitions: b642370f691040e3b800db1d9e3faf1e7ce36fcc (79-state two-edge coding); e94a4146c640f7025227bd2cce534eb164ce9d77 (exact edge counts); 6275af7b9def7bdcda20cfa55fceb747dae49719 (no fixed finite-history deterministic predictor).
Carrier/observer scope: the S23/AV auxiliary irrational-rotation carry observation. Native Heartbeat World/P000, six-axis ontology, the mother ten-label capacity question, and Source Result/Review are preserved at their own authority/scope.

## Definitions and hypothesis

Let B=79 and let
  r=ln(7)/ln(10/7),
  alpha=(2074774-380295*r)/(79*r-431).
Use the existing certified fact that 1/2<alpha<2/3 and alpha is irrational.
Set x_k={k alpha} for k>=1, and C_k=floor(B x_k) in {0,...,B-1}.
For an initial phase x in [0,1), write the length-m word
  W_m(x)=(floor(B{x+j alpha}))_(j=0,...,m-1).
Let p(m) be the number of distinct length-m words actually appearing on the forward orbit, m>=1.
A length-m word is *right special* when at least two distinct next symbols occur after that word along the orbit.

For j>=1 define
  t_j={-B j alpha},  with 0<t_j<1.
All t_j are distinct: equality modulo 1 for j!=h would make B(j-h)alpha an integer. Put t_0=0 and include the endpoint 1 whenever intervals are considered.

## Theorem 1: exact block complexity for every m

For every integer m>=1,
  p(m) = B*m = 79m.

Proof. Partition the phase circle into B first-symbol cells I_c=[c/B,(c+1)/B), c=0,...,B-1. In the coordinate t=Bx-c on I_c, the j-th readout floor(B{x+j alpha}) changes precisely once, at t=t_j, for every j>=1. This follows because t has width one, the B-spaced integer thresholds are one unit apart, and B j alpha is irrational; the crossing is an interior point. For each fixed j, crossing that threshold changes the j-th symbol by +1 modulo B and it cannot change a second time inside I_c.

For the word W_m, there are exactly m-1 distinct interior thresholds t_1,...,t_(m-1) in each I_c. They partition I_c into m nonempty cells. Words from different base cells have different first symbol. Two different cells in the same I_c are separated by at least one t_j; the j-th symbol differs, because it can cross only once in I_c. Hence the map from these Bm cells to length-m words is injective. Every open cell is visited infinitely often by the irrational forward rotation, so all Bm words actually occur. QED.

Orbit endpoints cause no additional positive-time word: for k>=1 and j>=0, equality x_k=c/B-j alpha (mod1) would force (k+j)alpha rational, impossible. The half-open convention therefore agrees with the actual positive-time language.

## Theorem 2: exactly 79 right-special m-words

For every m>=1, exactly B=79 length-m words are right special. Precisely one right-special word begins with each symbol c. It has exactly two next symbols, differing by +1 modulo B. The other B(m-1) words have exactly one next symbol.

Proof. Passing from W_m to W_(m+1) adds the unique j=m threshold t_m inside each I_c. It is different from the previous t_j, and hence strictly splits exactly one of that base cell's m old atoms into two nonempty pieces. The first m symbols are equal on the two pieces, while the new symbol crosses one bin boundary and takes two distinct values. In any other old atom the new symbol remains constant. Theorem 1 makes old atoms distinct words. Irrational orbit density realizes both sides and every other open atom. QED.

Consequences:
  p(m+1)-p(m)=79;
  h_top=lim_(m->infty) log p(m)/m=0.
Despite zero symbolic topological entropy, no fixed m-block determines the next carry symbol for all future times. This sharpens the previous finite-memory obstruction from existence of ambiguous pairs to exactly 79 ambiguous word types at every finite depth.

## Theorem 3: exact optimal finite-history error

Let D_m={0,1,t_1,...,t_(m-1)}. Let
  L_m=max{t in D_m: t<t_m},
  R_m=min{t in D_m: t>t_m}.
Define d_m^-=t_m-L_m and d_m^+=R_m-t_m.
Under the unique invariant (uniform phase) measure of irrational rotation, the smallest asymptotic error frequency among all deterministic predictors f:{0,...,78}^m -> {0,...,78} based only on the past m observed symbols is exactly
  epsilon_m = min(d_m^-, d_m^+) > 0.
Moreover epsilon_m -> 0 as m -> infinity.

Proof. The unique right-special word in each base I_c occupies the interval (c+L_m,c+R_m)/B. Its two distinct next symbols occur on the left and right subintervals of respective lengths d_m^-/B and d_m^+/B. A deterministic predictor on that word must select one value, incurring at least min(d_m^-,d_m^+)/B error under uniform phase; selecting the longer branch attains it. Every other word's next symbol is uniquely determined. Summing over all B base cells gives epsilon_m=min(d_m^-,d_m^+). By Weyl equidistribution for irrational rotation, the phase-measure error equals the actual asymptotic mistake frequency along x_k, for any fixed f, since the error sets are finite unions of intervals with null boundaries.

Irrationality of B alpha makes t_1,t_2,... dense in (0,1). The maximum length of the gaps in D_m tends to zero (by compactness and density, or finite epsilon-nets). Hence 0<epsilon_m<=R_m-L_m<=max_gap(D_m)->0. QED.

Theorem 3 supplies an exact observer-compression tradeoff: finite carry history supports increasingly accurate average prediction, but a phase-sensitive one-step determinism requires retaining an additional observation or an equivalent unbounded-history recovery. This is a BRC auxiliary observer/fiber statement, not a claim about native X6 temporal physics.

## Exact finite arithmetic and independent checks

VERIFY_WORD_COMPLEXITY.py constructs an exact 160-term atanh-series interval for both logarithms, with positive geometric tail bounds, propagates it through alpha, and certifies the decimal enclosure
  585597525374294135646142/10^24
    < alpha <
  585597525374294135646143/10^24.
For m in {1,2,3,4,8,16,32,64,128}, the program certifies strict ordering/separation of all m+1 partition endpoints t_j using integer arithmetic, constructs a rational interior phase in every one of 79m atoms, proves all Bm symbol words distinct via equal lower/upper floor results, and checks 79 strict two-way successor splits. It also certifies nonzero rational intervals for epsilon_m. This tests exact finite instances of the theorems, while the proofs above establish all m.

At m=128: 10112 distinct words and 79 right-special words. The optimal one-step error is strictly between
  5525221276560321231590/10^24
and
  5525221276560321246995/10^24.
At m=1 it is strictly between
  262204504569236716045218/10^24
and
  262204504569236716045297/10^24.

Exact execution evidence is in RUN_EVIDENCE.txt; the executed Python source is VERIFY_WORD_COMPLEXITY.py. No floating-point comparison enters any certification.

## Research frontier and follow-up

The new theorem classifies the symbolic information lost by all finite carry histories, but the S23/AV critical-cell covering certificates are geometric intervals over integer witnesses. Next: read the frozen checker and formulate whether each of the 79 phase subclasses permits a witness transport at plateau i=412. A direct exact coverage certificate or a concrete failed transport example is the next discriminating result. Preserve the 79m language theorem and the epsilon_m phase-prediction law as reusable exact auxiliary results.
