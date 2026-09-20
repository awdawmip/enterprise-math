# Heartbeat — heterogeneous coherent product baths via rational Schur merging

Event-ID: brc-heartbeat-heterogeneous-coherent-20260920-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE; no independent review, Lean or mathematical admission.
Source authority read: global402f682de929f819e8ca9460e5d273acc6e661cb; project92b1250bed92cc09e1cd89da6a6b4a9d90096373. Standalone parent9a6781163b5776836941c96003d8083c287f935d. P000 and residual-first constraints unchanged.

## Completed mathematical unit

Stage27 completes the declared next preparation problem: independent but arbitrary nonidentical complex coherent full-rank qubit bath states, under the same permutation-invariant nonquadratic collective Hamiltonian and central-only future instruments. It does not handle arbitrary initially correlated baths or nonsymmetric dynamics as though they were symmetric.

The exact subgroup identity T_(K+1)((T_K A) tensor rho)=T_(K+1)(A tensor rho) permits sequential compilation without K! permutations. The carrier consists of positive matrix-valued total-spin blocks with multiplicities already aggregated, not scalar block weights. In the unnormalized spin-n/2 basis G(q)=C(n,q), weighted trace over all blocks is exactly one.

Appending rho=[[a,b],[c,d]] maps old block R of size n+1 into spin labels n+1 and n-1. The upper update uses weights (n+1-q)/(n+1) and q/(n+1); the lower update is
Rminus(q,p)=n/(n+1)[d R(q,p)-c R(q,p+1)-b R(q+1,p)+a R(q+1,p+1)].
The proof derives both intertwiners and their Gram normalization. Square roots cancel at the density level. Complex entries are rational pairs, all matrix terms retained. Both updates are completely positive congruences; induction proves positivity, trace preservation and the exact observer quotient for every finite K. Existing identical coherent and heterogeneous diagonal compilers are exact subcases.

There are C(K+3,3) complex matrix slots, with O(K^4) rational arithmetic for this direct sequential compiler and O(K^3) retained matrix storage. Bit complexity, initial-state construction and readout costs are counted separately. The compiler is not an optimality claim or a general exponential-state simulator. Stage24 SpinBlock and Stage25 propagate_column execute unchanged; a new exact integer contraction retains real and imaginary matrix entries.

## Information-loss witness stronger than equal means

For two independent bath qubits compare I/2 plus/minus bX with I/2 plus/minus bY. Both preparations have average local matrix I/2, identical individual eigenvalues, identical computational diagonal probabilities and identical ALL total-spin weights. Their singlet/triplet weights are1/4+b^2 and3/4-b^2. Their internal block matrices differ.

At b1/4,K2,p1/3 and default couplings J1/4,omega1/16,u1/16,g1/2, the central difference pY(t)-pX(t) is t^6/4423680-2351t^8/225485783040+O(t^10). Initial value and first five derivatives agree. At t4, pX=0.533039006862532 and pY=0.533439092672115, difference0.00040008580958298046. The exact Taylor coefficients are checked through nested rational commutators independently of the Schur compiler.

At b10^-8,t4 the difference is6.401372953327688e-19. A120-bit candidate interval excludes zero and has width about2.80e-39. Independently written100-digit full-Hilbert exponentials agree. These are model probability effects, not experimental signals or heat. All block masses being known does not make their internal phase matrices disposable.

## Nonzero preparation errors and observer boundary

For deterministic local trace-distance preparation errors eta_i, product telescoping and contraction give central trace error <=min(1,sum eta_i), uniformly in time for the same symmetric Hamiltonian. No independent-noise or zero-error assumption is used. Twelve separately recorded signed nonzero coherence perturbations check finite examples.

Site-labelled bath observations distinguish input order. A local symmetry-breaking coupling also makes two reordered inputs dynamically distinguishable: a K2 witness at t4 gives probabilities0.5289797321487425 and0.5288641854125251. The exact twirl must not be reused unchanged outside its central/symmetric lease. Duhamel bounds for the added nonsymmetric operator are proved separately, not interpreted as a vanishing physical residual.

## Executed costs

Recorded alternating local matrices are (a,Re b,Im b)=(3/5,1/10,1/8) and(7/12,-1/9,1/7), both exactly positive full rank. At time1:
K4:35 matrix slots, population0.353621394955438, median compute0.00747605s.
K8:165 slots, population0.3536728112764177, median0.050115925s.
K12:455 slots, population0.3536899944882258, median0.185288049s.
K24:2925 slots, population0.3537072045816072, median2.278582343s.
K32:6545 slots, population0.3537115116358764, median6.733700247s.
K48:20825 slots and25 blocks, population0.3537158205911237, ONE compute run34.415071511s, split into20.197159725s compilation and14.217911786s propagation/contraction. Largest preparation rational numerator/denominator405bits. Numeric probability errors below4.5e-17.

K4 through32 use three repeats each; K48 has one run. Core times exclude module import and JSON/statistics serialization. No CPU affinity. The K48 raw row survived a subsequent call timeout; summary generation resumed without replacing the measured row. The quotient represents a specified family and observation, not arbitrary2^48-state data.

## Scope and validation

343 main assertions pass: exact traces/dimensions, previous-stage subcases, input-order invariance, normalized-CG positivity checks,20 full-Hilbert populations, two-time central instrument equality, and information-loss witnesses. Three90-digit heterogeneous full-Hilbert comparisons and two100-digit paired phase comparisons pass; twelve nonzero calibration diagnostics pass. All16 raw rows and six medians replayed; no timing evidence replaced. Same author wrote candidate and separate reference paths, so this is not independent research review or Lean verification.

Finite product full rank gives a positive finite-device floor muS product_i(2mu_i), but it can decrease with K. A rational determinant-based weaker floor is implemented. It is not a temperature for non-Gibbs states or a uniform resource-size bound. The strong zero-temperature preparation goal remains; no universal zero-temperature nonexistence or Shor speedup is established.

Schur/Clebsch-Gordan structure and polynomial permutation-invariant operator representations are established prior art (Bacon-Chuang-Harrow quant-ph/0407082; Bastin-Martin2307.06141). This contribution is a tested rational density recurrence, observer-safe composition, phase witnesses and costed implementation in the current research line, not a new universal method claim.

Next: distinguished-site/multiplicity-space transport for controlled symmetry breaking. Preserve the exact heterogeneous coherent compiler and its proof, rather than repeating it. Full code, proof, frozen plan, raw evidence and prior history are delivered in the cumulative standalone Git bundle; not the entire enterprise-math repository. The existing activity identity is retained; a new event sidecar is persisted with the source. Aggregate activity-index mutation must be verified separately and is not inferred from a note upload.
