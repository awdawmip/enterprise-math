# Native BRC partial-collision factor ports: a candidate and its exact limits

Status: SYMBOLIC_DOMAIN_OPERATOR_CANDIDATE / SHARED_CONTEXT / NOT_ADMITTED / NOT_IMPLEMENTED / NOT_EXECUTED. No scientific arithmetic, provider query, experiment, or remote write was performed for this note. Source inspection and writing this proof are the only actions. This is a candidate composition of existing T0/T4/T6 and control-mass semantics, not a claimed new generic tool or a factoring speedup.

## 1. The useful change of output contract

Input: an integer N>1, a residue a with a paid certificate gcd(a,N)=1, and a public finite branch schedule. No factors, order, discrete logarithms, or complete orbit table are constructor inputs. A nonunit a is handled first by the existing gcd route; it is not passed to an inverse-based construction.

For two unit endpoints x,y, define the relative endpoint u=x*y^(-1) modulo N. Then

    gcd(x-y,N) = gcd(u-1,N).                                      (1)

Indeed x-y is congruent to y(u-1), and multiplication by the unit y preserves the ideal generated together with N. Thus a sufficient successful result is

    FACTOR(N,g),  1<g<N,  N=g*q,

with exact typed division/multiplication evidence and, if native origin is claimed, a retained representative branch provenance and the gcd(u-1,N) receipt. The exponent difference and the two individual endpoints are unnecessary for verification of this result. A factor can be composite; primality of g is not required.

This is a weaker *information requirement* than finding the complete order or an order multiple. It is not a literal inclusion of the old success ports: u=1 gives gcd=N and is not a proper-factor port, whereas a new successful partial collision has u!=1. A proper-factor witness need not satisfy a^Delta=1 modulo N at all.

For the proof only, let N=pq for distinct primes and put r_p=ord_p(a), r_q=ord_q(a), r=lcm(r_p,r_q). If r_p!=r_q, the smaller of r_p,r_q is a positive difference strictly below r and gives a proper factor. Such a collision can therefore exist before the first complete return modulo N. This does not give that exponent to an algorithm. If r_p=r_q, no difference between powers of this fixed a gives a proper factor: every difference is divisible by both p,q or neither. This is an exact failure boundary of this base and endpoint family, not a failure of all native BRC algorithms.

## 2. Exact native positive two-branch quotient

Suppose one bit independently multiplies each endpoint by either 1 or a declared unit c. On relative endpoints the four branches are

    (0,0): u -> u;       (1,1): u -> u;
    (1,0): u -> c*u;     (0,1): u -> c^(-1)*u.

For column-vector notation define P_c e_u=e_(cu). The unnormalized and normalized native positive kernels are

    B_c = 2I + P_c + P_(c^-1),       K_c = B_c/4.                  (2)

All coefficients are nonnegative rational branch masses, not quantum amplitudes. Equal endpoints recoalesce by **adding** their mass. The 2I retains the two choices; it is not a Boolean collapse that replaces their weight by one.

The map (x,y)->u is an exact deterministic operation-safe quotient for these four named branches: multiplying both endpoints by a common unit is discarded, every branch descends as displayed, and the terminal observable (1) is constant on each fiber. Composition therefore preserves the entire factor-valued terminal distribution. This proof also works on any explicitly declared reachable subset; it does not require construction of all units first.

With c_j=a^(2^j), j=0,...,t-1, and Q=2^t, the result from u=1 is

    mu_t(u) = Q^(-2) * #{(v,w): 0<=v,w<Q, a^(v-w)=u mod N}.       (3)

Hence the exact mass of the proper-factor port g is

    Q^(-2) * sum_(|Delta|<Q) (Q-|Delta|)
                   1_[gcd(a^Delta-1,N)=g],     1<g<N.            (4)

Negative exponents in this proof are justified only by the unit certificate. A constructor may obtain c_0 and its inverse once and produce their square schedules by actual typed modular multiplication. Neither (3) nor (4) licenses a host pow/gcd reference or a free extraction of a positive-mass witness.

This is a native positive branch-and-recoalescence factor-search law. It intentionally does not assert equality with the old signed Shor/QFT measurement law. The original factorization objective, rather than every intermediate QFT distribution, is the comparison target.

### A further exact symmetry quotient, with a narrower observation lease

The factor observable is invariant under u->u^(-1), since u^(-1)-1=-(u-1)u^(-1). Moreover inversion permutes the two c/c^(-1) branches of equal mass. Thus every kernel K_c is strongly lumpable on

    [u] = {u,u^(-1)}.                                           (5)

For any two representatives of a class, their outgoing total mass to every quotient class agrees. Products of the possibly different K_c preserve this quotient and the factor-valued terminal law. Fixed points u=u^(-1) have one state, not a duplicated mass. Distinct outgoing branches that land in one class still add their weights.

This is **mass-kernel safety**, not safety for each branch name individually. It is invalid if one keeps a distinguished + branch, asymmetric branch weights, signed branch observables, individual exponent labels, or arbitrary path-dependent controls. The already existing control_mass partition checker implements exactly the relevant equal-outgoing-mass criterion on an explicit finite carrier. It uses source-row matrices; an implementation of the column formulas above must declare and account for the transpose at that boundary.

For this particular four-branch kernel the result strengthens to complete `WeightHistogram` preservation: inversion gives a weight-preserving bijection between the microscopic outgoing branches, fixing 00/11 and exchanging +/-. Every branch has atom [1/4], so each target class receives the same entire histogram from either representative. The unchanged relative state receives **2[1/4]**, not [1/2]; the latter would preserve mass but alter path counts and higher weight moments. A first-hit FACTOR(g,depth) must subsequently take one [1] identity step, rather than four new [1/4] branches. The generic control_mass checker alone checks only mass, so this stronger bijection proof or a full-histogram checker is still required. Factor value and first-hit depth are invariant under inversion. This extension does not restore erased individual branch names or endpoint paths.

On a cyclic orbit of order r, the quotient has (r+gcd(r,2))/2 classes. This count is explanatory, not an input or a promised small bound. Its factors remain exponential in log N in the worst case. Classical symmetry/lumpability is the underlying mechanism; no novelty is claimed for it.

## 3. What may be merged, and what cannot

**Exact same relative state.** Merge weights at u and preserve a representative witness if only one eventual factor is requested. Preserve richer provenance if the observer requests the individual exponent pair or its law.

**Reciprocal pair.** Merge only under the symmetric mass-kernel lease (5). A practical representation can carry the two typed reciprocal residues and choose a canonical representative using a charged comparison; it need not invoke an inverse oracle at every visit.

**Already verified successful factor.** In a separately declared *stop at the first successful test* algorithm, make FACTOR(g) an absorbing state. All paths that have already returned the same g can merge without retaining their endpoint. One representative certificate suffices for a valid factor witness; preserving the mass distribution over original paths requires more provenance. Every failed test remains an active state. In particular gcd=N is not success.

This absorbing process is a different stopping contract from evaluating (4) only at the final depth. It must not be reported as preserving the latter terminal distribution. Finite-horizon time-unrolling gives a finite positive graph; the repeated factor state has normalized self-transition one. A recurrent hidden-block elimination additionally requires an actually certified stable hidden block. A stochastic recurrence is not automatically eligible for a convergent star.

**Equal current gcd or equal current FAIL.** These are generally unsafe merges before future asymmetric actions. The failure is stronger than a single counterexample:

**Proposition (a narrow exact quotient obstruction).** On N=pq as above, define

    F(d)=p if r_p divides d and r_q does not;
         q if r_q divides d and r_p does not;
         FAIL otherwise.

If r_p!=r_q, the least positive period of this *factor-valued* observation is r. Consequently the coarsest deterministic quotient preserving F after **all shifts d->d+k** on the cyclic orbit has r states.

Proof. Let h be any period. Since F(0)=FAIL, either both r_p,r_q divide h or neither does. In the first case r divides h. In the second case, choose d=r_p when r_q does not divide r_p; then F(d)=p, whereas r_p does not divide d+h, so F(d+h)!=p. If r_q divides r_p, their inequality makes d=r_q satisfy F(d)=q, and r_q does not divide d+h. Both alternatives contradict periodicity. Since r is a period, it is minimal. Two orbit states with equal observations under every future shift differ by a period and are the same state. QED.

If r_p=r_q, F is identically FAIL: one class suffices but cannot produce a factor. The theorem does not apply to a fixed restricted remaining schedule, an approximate observer, a nonlinear encoding, or the aggregate symmetric-kernel quotient (5). In particular it must not be used to contradict (5): the operation/observation languages are different.

The proposition deliberately preserves the actual factor label p or q. The displayed proof must not be copied to a Boolean proper/FAIL observer: after a shift the other proper factor could be returned. No Boolean minimal-period theorem is claimed here.

This identifies the actual new question: find a paid, executable *finite-horizon factor-observer quotient* for the remaining symmetric schedule that is substantially smaller than its explicit relative orbit, using only N,a and the schedule. A formal future-signature definition is available already; generating and certifying that quotient without enumerating its orbit is not.

## 4. Partial collision is not an uncharged unknown-prime projection

For a fixed unknown divisor p, the statement x=y modulo p identifies a useful fiber. But declaring pi_p(x)=x mod p as a cheap input would already supply p. T4 requires the observation map to be declared or derived; it does not discover the missing modulus. Our computable terminal observation is gcd(x-y,N), with its own paid arithmetic, and no modulus oracle.

The endpoint difference alone is also not generally an operation-safe carrier. Under separate multipliers x->c*x and y->d*y, the new difference depends on both endpoints, not just x-y. Under a common polynomial f, the divided difference f(x)-f(y)=(x-y)D_f(x,y) retains additional state. For f(z)=z^2+C, it is (x-y)(x+y): dropping x+y drops future collision information. The relative quotient from section 2 does not descend through this polynomial update either.

There is a useful exact but unproductive limiting case. A common affine action x->c*x+b, y->c*y+b sends D=x-y to cD. If g=gcd(D,N), then

    gcd(cD,N)=gcd(cg,N).                                        (6)

Write D=gk and N=gm with gcd(k,m)=1 to prove (6). Thus g alone is safe for this declared common-affine language. With unit c it never changes; with initial g=1 a new proper factor arises from the nonunit coefficient c itself. This closed small carrier therefore cannot manufacture previously unavailable factor information through unit transport. It is a boundary on that carrier, not on richer native dynamics.

## 5. Success probability and classical comparisons

For the independent uniform exponent-pair sampler (3), let

    C_Q(s) = [Q + 2 sum_(k=1..floor((Q-1)/s))(Q-k*s)] / Q^2.

For squarefree N=pq its exact proper-factor probability is

    C_Q(r_p) + C_Q(r_q) - 2*C_Q(lcm(r_p,r_q)).                   (7)

This follows by inclusion-exclusion of the two divisibility events; the diagonal terms cancel. If Q is a common multiple of both orders, it reduces to 1/r_p+1/r_q-2/r. This is a proof using unknown orders as analysis variables, not an executable input specification. There is no uniform positive lower bound from this construction alone. Postselecting a proper-factor port does not make inverse success probability free.

The following comparisons are algebraic identification of familiar mechanisms, not a new literature or novelty audit:

* **Pollard rho:** its gcd readout from endpoints colliding modulo an unknown prime is precisely the same partial-collision predicate. Its usual common polynomial iteration is a different update language from the multiplicative two-branch kernel. Replacing that walk by BRC nodes does not itself establish a new algorithm or better collision cost; the polynomial divided-difference obstacle above must still be represented.
* **Pollard p-1:** choosing a special exponent E and testing gcd(a^E-1,N) is exactly a special choice of our endpoint (a^E,1). Conditions such as ord_p(a)|E but ord_q(a) not dividing E explain success. A useful exponent construction and its smoothness assumptions remain part of the cost/guarantee. Native execution of this same test is not a new number-theoretic tool.
* **Batch gcd/product trees:** for an explicitly generated finite list of differences D_i, store P=product D_i mod N and test gcd(P,N). Combining batches by product is associative, and can reduce the number of gcd calls. If the result is N, a retained product tree may be split to look for individual proper-factor witnesses. A saturated product may instead arise from complete-collision leaves and reveal no proper factor. Leaf generation, product construction, tree storage and worst-case descent all remain charged. This batch product is not the positive linear total mass of (2); changing the result algebra needs a declared typed adapter.

The native opportunity would be a proved safe compression or readout that beats explicit endpoint generation for this factor-observer language. Neither a short product of kernels nor merely relabelling a classical gcd strategy supplies it.

## 6. Minimal proposed contract and complete cost ledger

The proposed domain API is conceptual, not present executable code:

    DECLARE_RELATIVE_FACTOR_CARRIER(N, a, finite_schedule, lease)
    STEP_SYMMETRIC_MASS(state, c, inverse_c, certificate)
    OBSERVE_FACTOR_PORT(state_or_selected_endpoint, provenance_requirement)
    STOP_WITH_FACTOR(g, verification_receipt)

The declaration binds full N/a/schedule, typed unit/inverse proofs, kernel normalization, row/column convention, source hashes, the fixed terminal or first-hit stopping rule, and the precise observation/provenance lease. Returned outcomes distinguish FACTOR, NO_FACTOR_AT_THIS_READOUT, and BUDGET_EXHAUSTED with retained residual state. NO_FACTOR is never PRIME. A serialized partial state must bind all retained mass, active labels, factor ports, current layer and arithmetic receipts; an uncomputed label is not zero.

Let n=ceil(log2 N), t be the number of bit layers, and S_j the number of explicit retained classes at layer j. The arithmetic library has polynomial-in-n per-column work, but it does not bound S_j.

* Build the multiplier/inverse schedules with O(t) typed modular operations plus the unit/inverse certificate. Their bit/digit work is charged separately from native kernel calls.
* Explicit sparse propagation performs O(sum_j S_j) modular actions and exact mass additions, up to fixed branch multiplicities. The reciprocal representation changes constants, not the worst-case exponent. Unnormalized mass numerators have O(t) bits; retained state requires O(S_j*(n+t)) value bits, before hash/index/receipt/provenance overhead.
* Before any successful absorption, an unmerged layer has at most min(2^(j+1)-1,r) relative labels; reciprocal classes have at most min(2^j,(r+gcd(r,2))/2). These are upper bounds, not guarantees of few labels.
* A terminal explicit port scan costs S_t typed gcd computations. First-hit absorption instead tests newly visited states at intermediate layers; those gcds and caches are not free. Sampling one path avoids a full state table but pays repetition according to its actual success law, not the positive total mass of a formal expression.
* Existing recurrent_mass_power charges explicit matrix dimension and rational arithmetic. Existing recurrent port elimination charges the explicit hidden inverse and requires stability; it does not construct a modular orbit or factor port for free. A sparse or implicit extension must retain the same semantics and separately prove its complexity.
* Report actual native core calls, replayed full-adder digits, modular/gcd operations, host wiring/index work, state/receipt size, build/observation/repetition cost and any resource exhaustion separately. Source reuse does not turn an unexecuted quotient into an actual core receipt.

## 7. Existing-source routing and exact pins

Repository source reads in this unit are from immutable enterprise-math commit `2e81851d62c869a20b47ae083a24dde1a4c0420c`, unless separately stated. They establish reusable contracts, not admission of this proposal.

1. [Tool registry](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/enterprise_toolbox_registry.json), blob `3889506451091ebcfbf7a58cda6517c4af8c3597`: T0 support/result/provenance; T4 equal-fiber witness only after the observation is supplied; T6 declared operation-safe quotient; T8 relation observation. Its affine degree-two moment lease expressly excludes arbitrary nonlinear observers. A gcd/proper-factor predicate is not supplied by that moment lease.
2. [Operation quotient](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/operation_quotient.py), blob `758a65de02a434446936cd7e37b2ae604eade863`: existing exact future refinement on an explicit finite domain. [Partial-operation quotient](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/partial_operation_quotient.py), blob `d1f86491ce07279c058a4c99f40cabb1f96da0de`: action legality must also be preserved.
3. [Control mass quotient](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_control_mass.py), blob `e8811e5f194fc57b294be7255214361fe99395d5`: `certify_control_mass_partition` compares outgoing total masses to every class; `quotient_control_mass_matrix` is the finite-carrier adapter for (5). It constructs a dense matrix over the declared state count; it is not an implicit modular-carrier implementation.
4. [Weighted recurrent core](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_weighted_recurrent.py), blob `4e6b3132580e3cd70a20a0d8bd4d28792b961afb`: positive rational mass powers and certified stable star. [Recurrent ports](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_recurrent_ports.py), blob `24a7fd37e274c067eaf560036f51fae80baa1644`: explicit stable hidden-block Schur elimination, with separate global-zeta information. No gcd witness extractor is implemented by that interface.
5. [Prime method inventory](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/prime_method_inventory.json), blob `3576d5a228e18bd3cf3ce9b248c1df638555cf71`, routes bounded classical least-factor witnesses and identifies their limitations. [Multiplier factor scan](https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/src/enterprise_math/brc_multiplier_factor_scan.py), blob `7fe48887ed3567d4a83165354625a7479f94aea3`, is a multiplier-Fermat square-gap scan with host gcd/isqrt, not this two-branch quotient. Its source may inform comparison, but is not silently substituted for actual typed arithmetic.
6. Existing [lazy gcd](https://github.com/awdawmip/enterprise-math/blob/0e6380ff74d31b842ba0b54802c1f0595a7dd60d/research_notes/directed_recovery/20260926_C6438C/optimization/lazy_modular/lazy_gcd.py), blob `cf6cd0c4aa0064424ed5c6d4e876d0a6e57eaca9`, source SHA256 `b704590f055da0785d03b6026d9fa749e75218acd2764d25e90288f32db0965e`, uses actual `Arithmetic.divide` at every Euclid step. `lazy_modular.py` SHA256 `08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4` supplies typed inverse/permutation certificates and requested columns. These are reusable verification/arithmetic, not factor discovery by themselves.
7. `research_method_inventory.json` was routed for the matching collision/quotient families. The prior source audit at `D:/em/TEMP/sep27-brc-native-shor-pivot/NATIVE_ROUTE_RESET.md` already establishes that `common_collapse.py` is an axis-aligned-body intersection/enumeration tool, not a modular collision inverter. Nothing here changes that boundary. The extra inspected `brc_histogram.py` and `weighted_relation_field.py` retain finite histogram or capacity/linear-relation semantics; neither automatically supplies the nonlinear factor port.

No exhaustive claim that the entire repository or literature lacks a related algorithm follows from these targeted reads.

## 8. The next bounded mathematical problem

The current positive result is an exact factor-sufficient relative carrier, a reciprocal mass quotient and a sound first-hit result carrier. The useful negative result is that terminal gcd labels do not generally compose, and even the weakened factor-valued deterministic observation can retain the full unknown-order period.

The next problem is therefore specific: for the remaining symmetric multiplier schedule, construct a factor-port-safe quotient or port elimination whose representation, certification and witness readout can be bounded without enumerating all reachable relative labels. A candidate must expose which future distinctions it drops, prove equal outgoing class mass or a source-defined equivalent law, and charge gcd/partition construction. If it requires a hidden prime, known order, full orbit, or an uncharged conditioned sampler, it has not solved this problem. A small typed fixture may test an implementation later, but cannot replace this structural obligation.

Global-Knowledge-Sync: main@8c6557d / GLOBAL_KNOWLEDGE_V1.
