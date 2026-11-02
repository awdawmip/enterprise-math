# PREFIX-453 — Observer-safe adaptive histogram/moment codec, exact invertibility criterion, and a nine-path collision

Date: 2026-11-03 (Asia/Shanghai).
Scientific input: frozen Enterprise Math project commit f42f2906d77f24085c123f3ccfe9667d41caa96d. Current rules read through the canonical global snapshot d520e90868e7e6dd619f64085d9164668cda51a3 and current project continuation/portable protocols. This is an author-side portable research output, following PREFIX-452 at dff5390aa240f3ff3cba47a31348a3de317a14ca. Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

## 1. Problem, native object, and declared observer

Use P000's native six-axis signed spatial Cell torsor, with primitive ordered steps ±e_i (i=1,...,6). Fix path length N, history residue r = number of -e_1 steps modulo q, and nonnegative rational mass on each reachable (r,x), x in Z^6 a *raw displacement relative to a chosen Cell*. This r is typed history, not another spatial axis; no final Cell address or physical time trajectory is claimed.

For each sector r retain the 28 joint monomials of total degree ≤2, including the mixed terms:
T_{r,alpha}(mu) = sum_x mu(r,x) x^alpha,   |alpha|≤2.
Call this map Phi_2. The allowed future operation language L_2 consists of finite positive-rational alternatives with source-sector-dependent weights, target-sector labels and rational affine maps x -> A_{s,r}x+b_{s,r}, followed by observers that are linear combinations of these same degree-≤2 sector moments. All future operations in this language have exact quadratic pullbacks. This is an explicit observer/future-operation fiber certificate for the information reduction in question; history sector, mixed moments and any additional provenance needed by another consumer must remain available.

## 2. Theorem A — exact forward descent and adaptive codec

For every q≥1 and any finite nonnegative rational joint histogram mu, Phi_2 is additive and transports exactly through every operation in L_2. If F is such a BRC branch operator, there exists a linear rational operator F_2 with Phi_2(F mu)=F_2(Phi_2(mu)). This identity remains true under arbitrary *finite* serial compositions and positive-rational parallel alternatives.

Proof. The pullback of every monomial x^alpha of total degree at most two along an affine map is a rational linear combination of the same 28 monomials, so the exact transformed expectation is a rational linear combination of the stored old expectations in the indicated source sector. Weight and target-sector aggregation are additive. Compose this factorization inductively. Positivity is preserved by the assumed branch weights. QED.

Define two typed storage alternatives, HIST (the complete occupied (r,x,weight) bins) and MOMENT2_AFFINE (the 28q moments). If the downstream declaration is L_2, both represent the same entire future observation stream. Computing and retaining whichever of their two *actually serialized UTF-8 byte strings* is shorter is therefore exact for that declared consumer. No universal density-only threshold is required: both the integer/Fraction bit length and the selected JSON format contribute to the decision. A consumer requiring the full joint endpoint/history histogram or higher-order endpoint observables keeps HIST unless a stronger exact decoder certificate applies. Consumers requiring ordered paths, signed amplitudes or additional provenance retain those as separately typed source channels: HIST itself records only aggregated endpoint/history masses.

## 3. Theorem B — exact criterion for recovering histograms on a known support dictionary

Fix a known finite per-sector support dictionary S_r subset Z^6, and permit arbitrary nonnegative rational masses on S_r. Form the 28×|S_r| rational evaluation matrix V_r with column v(x)=(x^alpha)_{|alpha|≤2} for each x in S_r. The quadratic moments uniquely recover *all* histogram masses on these dictionaries if and only if rank_Q V_r=|S_r| in every sector.

Proof of sufficiency: injectivity of each sector's linear map gives a unique rational solution of V_r w_r=T_r; any left inverse recovers w_r exactly. Necessity: when columns are dependent, take a nonzero rational kernel c. The degree-zero row gives sum c_i=0, so c has both signs. The nonnegative mass vectors c^+ and c^- are distinct and have identical moments. If all dictionary locations must have strictly positive masses, adding an identical positive constant vector to both does so. This proves necessity even among positive rational masses. QED.

Consequences: any dictionary with more than 28 endpoints in one sector fails this universal recovery criterion. A dictionary of ≤28 points must still pass an actual rank check: cardinality alone is not enough. This criterion concerns a *known permitted support dictionary*, rather than assuming one can infer an unknown support from compressed data. It identifies exactly when a typed codec can reverse MOMENT2_AFFINE to HIST without changing the original population.

## 4. New explicit nine-versus-nine legal native path counterexample

For q=3, N=4, place all paths in historical residue r=2. The following are full raw six-coordinate terminal displacements with integer multiplicities of distinct unit-weight ordered native words.

Source A:
- (-2,-2,0,0,0,0) × 1
- (-2, 1,0,0,0,-1) × 4
- (-2, 1,0,0,0, 1) × 4

Source B:
- (-2,0,0,0,0,-2) × 1
- (-2,0,0,0,0, 0) × 4
- (-2,0,0,0,0, 2) × 1
- (-2,2,0,0,0, 0) × 3

Every terminal is reachable after exactly four primitive signed X6 steps with exactly two -e_1 steps. The multiplicity available from distinct ordered words at every terminal exceeds the requested mass (verified by exhaustive enumeration of 12^4 words). Each source has nine mutually distinct ordered words. Direct exact evaluation gives all 28 sector quadratic moments equal (thus all 84 joint observations equal), yet sum_x mu_A(r,x) x_2^3=0 and sum_x mu_B(r,x) x_2^3=24. Consequently a future consumer of the cubic observer distinguishes them. This is a finite, explicit residual for extending the observer language, not a defect in the exact L_2 descent theorem.

Ordering the seven union bins as B1,B2,B3,A2,A3,B4,A1 gives the integral signed kernel coefficients (-1,-4,-1,+4,+4,-3,+1); equivalently, evaluation at A1+4A2+4A3 equals evaluation at B1+4B2+B3+3B4 for each degree-≤2 monomial. The equality follows by direct monomial substitution, and the certificate independently checks every monomial and exact native path realizability.

## 5. Exact finite computation and storage regimes

The standalone executable companion 'prefix453_hybrid_codec_certificate.js' uses integer arithmetic, an exact modular nonsingularity certificate modulo 1000003 for the canonical 28-point X6 dictionary in each r=0,1,2, and exact exhaustive signed-word dynamic programming. A nonzero modular determinant establishes full rank over Q. The certificate constructs the 84-point dictionary inherited from PREFIX-450, checks all 12^4 paths and 1059 joint terminal/history bins, and checks the nine-path counterexample and cubic separator.

A second independently executed full standard-library Python/Fraction implementation checked exact rational inversion on all three 28-point dictionaries and the 168-branch rational affine BRC future by comparing direct terminal enumeration against polynomial pullback. It is retained as a run-local source in this run's evidence package. The JS companion independently reproduces the integral certificates and byte measurements below.

Storage format is compact UTF-8 JSON without compression or omitted zero moments. HIST contains records [r,[x1,...,x6],numerator,denominator]. MOMENT2_AFFINE contains all three r blocks of 28 [numerator,denominator] pairs. Both payloads include codec, q and N tags; the moment tag declares the L_2 observer scope. Measured exact byte counts:

| q=3,N=4 source | Occupied bins | HIST bytes | MOMENT2_AFFINE bytes | Shorter |
| --- | ---: | ---: | ---: | --- |
| One canonical word | 1 | 60 | 574 | HIST |
| First four canonical words | 4 | 127 | 576 | HIST |
| First 28 canonical words | 28 | 659 | 585 | MOMENT2_AFFINE |
| All 84 canonical words | 84 | 1930 | 609 | MOMENT2_AFFINE |
| All 20736 ordered words | 1059 | 25739 | 646 | MOMENT2_AFFINE |

On the fixed nested 84-word canonical sequence, the first observed shorter moment payload occurs at 25 occupied bins (24-bin bytes 571 versus 582, 25-bin bytes 593 versus 583); every later prefix through 84 remains moment-smaller for this exact encoding. Full-word dense families at N=2,3,4,5,6 have respectively 74,316,1059,2984,7379 occupied joint bins; complete byte results are in the companion log. A separately checked 84-atom positive-rational example occupies 2051 HIST bytes versus 747 MOMENT bytes in the Python exact rational encoding.

Naive exact conversion from H occupied histogram bins computes 28 joint monomials per bin, O(28H) scalar operations plus rational arithmetic/serialization cost; the full encoded byte comparison requires producing both candidates. Conversely, decoding moments on a certified rank-|S| support dictionary requires solving a rational linear system and carrying or recovering the dictionary identity. A short histogram can be smaller for sparse inputs. This is an exact, scope-typed hybrid choice, not a general-purpose lossless compression claim for the original ordered paths.

## 6. Reproducibility and next research unit

Run 'node research_notes/portable_direct/prefix453_hybrid_codec_certificate.js' from any checkout containing this artifact; no dependencies or network requests. The generated 'PREFIX453_EXACT_EXECUTION.log' contains the actual output from executing the same JS function before publication. The frozen source context for the canonical word construction is research_notes/portable_direct/prefix450_arbitrary_degree_x6_certificate.py at 84cb80025bd64c7d66f84b4634217416439474a1; native upstream classes were directly executed in PREFIX-452. This research has not modified upstream production classes. The signed X6 terminal is a raw chart-relative displacement, not the user-facing Cell identity codec.

Next question PREFIX-454: measure the exact CPU/memory cost and rational bit growth of the tagged hybrid on actual native ControlPacket, EffectHistogram and MomentState objects across q,N and higher-degree consumers. Investigate a small metadata certificate for known-support recovery, and compare the cost of dictionary storage or reconstruction against retaining HIST. Test the first cubic-separating example against an explicit cubic typed port.

Real authority: authenticated GitHub login awdawmip has repository push permission. Native Sites gateway is static read-only with research_authority_granted=false and the live bounded task query returned CONTROL_QUOTA. No current owner, native Researcher-ID, CLAIM, independent review or admission was established. This note is an author-side scientific source, not a formal Result.
