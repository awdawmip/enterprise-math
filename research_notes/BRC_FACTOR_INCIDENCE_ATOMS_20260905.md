# BRC canonical factor-incidence atoms, minimal count signatures and regular specialization

Date: 2026-09-05
Researcher-ID: `EM-BRCWLOG-6F42A1`
Mode: `TASK_RESEARCH`
Status: `RESEARCH_CANDIDATE / EXPLICIT_PROOFS_AND_EXACT_REFERENCE_CHECKS / NOT_FOUNDATION`
Frozen baseline: `awdawmip/enterprise-math@dc86d1d26a1374fc15cfb85c8db10f8bfbef849b`.

This is a direct-user continuation of this researcher's Weighted-BRC/log line. The original scheduler task ID was not recovered. No scheduler claim, new V2 task, Driver review or Foundation promotion is asserted. P000 was loaded; the statements below make no dimensional or physical-world inference.

Parent frontier: `research_notes/BRC_FACTORIZED_SELECTOR_MOBIUS_CALCULUS_20260904.md`, main-backed PR #1238. Its last section asks for a factor-certificate compiler and compression of the all-subset gcd/Mobius tower. The earlier `research_notes/BRC_CYCLIC_LOG_MULTIPLICITY_CLOSURE_20260902.md` explicitly records the same Researcher-ID.

## 1. Advance and scope

For a supplied list of nonzero rational polynomials, replace the predecessor's all-subset gcd representation by canonical squarefree, pairwise-coprime valuation atoms. The compiler needs no irreducible factorization and no enumeration of factor subsets. The resulting certificate supports Boolean interval emptiness, failing-factor labels, distinct roots, multiplicity counts and monomial changes of factor coordinates.

A count-only observer quotient is proved strictly smaller than the full algebraic certificate. A regular-specialization theorem also repairs the identically-zero cross-resultant problem caused by permanent common factors.

The basic algebra is classical. The contribution claimed is the precise BRC interface, operation lease/minimality boundary, executable compiler and application to the predecessor's unresolved gap, not a new general-purpose factorization family.

## 2. Theorem A: canonical common valuation atoms

Let F_1,...,F_n be nonzero polynomials in Q[x]. Constants, repeated inputs and identical factors are allowed. Let c_i be the leading coefficient, D=sum_i deg(F_i), and R=deg(rad(product_i F_i)). For each monic irreducible p dividing some input, define

    v(p)=(ord_p F_1,...,ord_p F_n) in N^n minus {0}.

For each realized vector v, let G_v be the product of all monic irreducibles with that vector. Then

    F_i = c_i product_v G_v^(v_i).

The G_v are nonconstant, monic, squarefree and pairwise coprime, and their labels are distinct and nonzero. These conditions uniquely determine the certificate, up to display order. Its atom count h satisfies

    h <= R <= D.

**Proof.** Unique factorization assigns every monic irreducible its unique vector. Grouping equal vectors gives the reconstruction and pairwise-disjoint irreducible supports. Conversely, squarefreeness and pairwise coprimality place each irreducible in exactly one block; reconstruction forces its label to be its valuation vector. Distinct labels force all irreducibles with the same vector into the same block. Every block has degree at least one and their degree sum is R. QED.

The irreducible characterization is a proof, not the algorithm. In particular, a support-only label can lose multiplicity: F_1=x(x-1)^2 and F_2=x^2(x-1) have two atoms with profiles (1,2) and (2,1), despite identical membership support.

## 3. Gcd-only compiler and complexity boundary

Normalize each input to monic and compute its characteristic-zero squarefree layers

    F_i/c_i = product_e S_(i,e)^e

using polynomial gcd and exact division. Maintain squarefree pairwise-coprime blocks with partial valuation vectors. On arrival of S_(i,e), split each old block G into gcd(G,S_(i,e)) and its exact quotient. Only the common piece receives coordinate i=e. Remove each common piece from the unprocessed residual of the new layer. A nonconstant residual becomes a new block. Merge equal-profile blocks by multiplication and omit constants.

**Invariant proof.** Before every layer, each seen irreducible occurs in exactly one block with its already-processed memberships. Gcd splits exactly by membership in the next layer. Different squarefree layers of the same input are coprime, so no existing nonzero coordinate is overwritten. The residual contains precisely the newly seen irreducibles. Equal-label blocks have disjoint support, so their product remains squarefree and coprime to the rest. Induction gives Theorem A's certificate.

If L is the number of nonconstant layers, then L<=D and there are at most R blocks at every stage. Refinement therefore uses at most LR<=D^2 gcd calls. The simple preprocessing uses at most 2D further gcd calls. This is a gcd-CALL bound, not an essentially-linear or polynomial-bit-complexity claim. Input reading, rational coefficient heights, multiplication/division and n-coordinate labels are additional costs. Dense degree may itself be large relative to a compressed input encoding.

The independent verifier checks monicity, squarefreeness, pairwise coprimality, distinct nonzero profiles and exact reconstruction; it does not trust compiler counters. Zero polynomials are refused because they do not have finite real root support.

## 4. Three observers from one certificate

Fix a rational open interval I=(u,v) with u<v, and compute n_v=N_I(G_v) using the predecessor's endpoint-deflated exact Sturm law. For nonnegative outer exponents w_i define

    P_w = product_i F_i^w_i,
    e_v(w) = sum_i w_i v_i.

Then

    N_I(P_w) = sum_(e_v(w)>0) n_v,
    M_I(P_w) = sum_v e_v(w) n_v.

Boolean safety is N_I(P_w)=0. The failing original-factor support is

    U_I = {i : sum_(v_i>0) n_v > 0}.

**Proof.** Distinct atom root sets are disjoint. A root of G_v survives in P_w exactly when e_v(w)>0, and then has multiplicity e_v(w). Sum these pointwise facts. QED.

The predecessor's declared exponents m_i are one choice of w_i. A separately declared selector root r still requires F_i(r)!=0 for each active factor when its fixed multiplicity must be preserved. Interval emptiness alone does not prove that guard.

## 5. Theorem B: the exact minimal count-only signatures

Fix I and allow only deletion/activation of original labels and nonnegative outer powers. Define

    a_S = sum_(supp(v)=S) n_v,
    m_i = M_I(F_i).

Store only nonzero histogram entries. For each activation subset A,

    U(A) = sum_(S intersect A nonempty) a_S.

These queries determine the histogram uniquely. Let T=U([n]) and

    b(B)=T-U([n] minus B)=sum_(S subset B) a_S.

Boolean-lattice Mobius inversion gives

    a_S = sum_(B subset S) (-1)^(|S|-|B|) b(B).

Hence a_S is the coarsest exact signature for all activation distinct-root counts. Separately, (m_i) is the coarsest signature for all multiplicity queries, since M(P_w)=sum_i w_i m_i and unit-vector weights recover each m_i. Their joint minimal signature is

    ((a_S)_(S nonempty), (m_i)_(i=1..n)).

Boolean safety is a further quotient needing only individual factor-unsafe bits for its entire activation family. Minimality means equivalence under this exact observation family, not minimal serialized bit length. The exponential inversion proves distinguishability and is a bounded test oracle; it is not used to construct or query the sparse signature.

**Strictness.** On (-1,2), compare

    (F_1,F_2)=(x(x-1)^3, x^3(x-1))

with

    (F~_1,F~_2)=(x^2(x-1)^2, x^2(x-1)^2).

The first has two valuation atoms and the second one, but both have a_{1,2}=2 and (m_1,m_2)=(4,4). All allowed fixed-interval count queries agree. A smaller interval separating zero from one distinguishes their multiplicities. Thus the full valuation certificate is not count-observer-minimal.

**Singleton-plus-total failure.** The families

    (x(x-1), x(x-2), (x-1)(x-2))
    (x(x-1), x(x-2), x(x-2))

have individual counts (2,2,2) and full union count 3 on (-1,3), but activating only factors 2 and 3 gives 3 versus 2.

**Lease boundary.** Count-only signatures erase locations. The factors x and x-1 each have one root on (-1,2), but inserting a new factor x yields union counts 1 and 2. Arbitrary new factors or moving endpoints require retained algebraic/root-support information and, generally, new gcd/root-count work. No erased root value is recovered from a count.

## 6. Theorem C: no-gcd monomial pushforward

For a nonnegative integer n-by-m matrix B, form H_j=product_i F_i^(B_ij). Transform every profile by v -> u=B^T v. Discard zero images and merge blocks with the same nonzero image:

    G'_u = product_(v : B^T v=u) G_v,
    c'_j = product_i c_i^(B_ij),
    n'_u = sum_(v : B^T v=u) n_v.

This is exactly the canonical certificate and transported interval counts of the new factor list. For a second nonnegative integer matrix C, direct and staged transports agree because C^T(B^T v)=(BC)^T v.

**Proof.** Multiplication and nonnegative powers add valuations. Products within an image fiber stay squarefree because original blocks are pairwise coprime. Theorem A's uniqueness identifies the new certificate; disjointness proves count addition. A zero intermediate profile remains zero after every further matrix map, so deletion is safe under composition. QED.

Deletion, duplication, grouping and powers therefore require label arithmetic, scalar powers and multiplication of disjoint blocks, but NO gcd, irreducible factorization or new root counting. This is not a constant-time/cheap-bit-cost claim. Additive polynomial operations, negative exponents/division, cancellation and arbitrary new factors are excluded.

## 7. Theorem D: regular specialization

Theorem A holds over Q(t) as well. Suppose its generic atom certificate is given there. Choose a nonzero polynomial guard d(t) excluding denominators of atom coefficients and zeros/poles of the scalar units. Also exclude zeros of the reduced numerators of

    Res_x(G_v, dG_v/dx),
    Res_x(G_v,G_w) for v!=w,
    G_v(t,u), G_v(t,v).

Assume endpoint expressions are not identically zero. The squarefree part of the product of these guards is a sufficient nonzero Delta(t).

For every real t_0 with Delta(t_0)!=0, specialization of the generic certificate is the canonical atom certificate of the specialized inputs. On every connected real parameter interval avoiding the guard roots, all atom interval counts and all the above activation/weighted/count/safety queries are constant.

**Proof.** The scalar/denominator guard makes the factorization identity specialize with nonzero units. Monicity keeps atom degrees fixed. Internal resultants preserve squarefreeness; cross resultants preserve pairwise coprimality. Exact reconstruction and distinct labels survive, so Theorem A proves canonicality. Simple roots cannot cross the protected endpoints, giving local constancy of interval counts and then constancy on each connected event-free interval. Apply the observer formulas. QED.

There are h+binom(h,2) internal/cross resultant slots and 2h endpoint slots. The guard is sufficient, not minimal. Event-point labels are not inferred from equal adjacent chamber labels.

The executable atom_events.py accepts SUPPLIED monic polynomial-in-t atoms. Automatic generic atomization in Q(t)[x], rational-function denominator bookkeeping, and full parameter root isolation are not implemented here. Persistent endpoint roots are explicitly refused. The inherited Sylvester determinant is a subset-DP reference backend; a quadratic number of resultants is NOT a fast-resultant complexity claim.

### Permanent-overlap witness

    F_1=(x-t)(x-1), F_2=(x-t)(x+1), I=(-2,2).

Res(F_1,F_2) is identically zero because x-t is permanently shared. Generic atoms are x-t with profile (1,1), x-1 with profile (1,0), and x+1 with profile (0,1). Their squarefree event guard is

    Delta(t)=(t^2-1)(t^2-4).

There are three distinct interval roots for -2<t<2 except t=+-1, when two atoms collide and the count is 2. At t=+-2 the moving root is excluded by the open endpoint, and outside the interval the count is also 2. Boolean emptiness is false throughout because -1 and 1 remain. In particular, a collision can change the event-point count despite identical neighboring labels.

This repairs permanent CROSS-FACTOR overlap, not merely permanent outer multiplicity.

## 8. Exact validation actually performed

The standalone command is:

    cd experiments/brc_factor_incidence_atoms_20260905
    python check_factor_atoms.py --backend pinned --output verification.json

Observed PASS:

- 1,275 predecessor-library interval comparisons;
- 12,975 old gcd-Mobius subset terms used only as a small-instance oracle;
- 14,250 activation contexts compared with expanded-polynomial Sturm counts;
- 2,000 independently specified exact-root weighted queries;
- 100 factor-order/canonicality checks;
- 500 complete support-histogram inversions;
- 81 derivative-chain multiplicity comparisons;
- 63 monomial transports versus fresh compilation;
- 60 direct-versus-staged transports;
- 16 strict minimal-signature coarsening queries;
- 25 parameter specializations and 225 weighted parameter-observer comparisons;
- 12 invalid-input refusals and 5 corrupted-certificate refusals.

The 80-factor witness has input degree sum 160, three atoms and 235 refinement gcd calls. Its naive subset formula has 2^80-1=1208925819614629174706175 nonempty subset positions; they were NOT enumerated. This is a structural compression witness, not a universal runtime benchmark.

All arithmetic is exact integer/rational polynomial arithmetic. Known-root regressions supply root counts independently for rational linear factors, x^2-2 and root-free x^2+1. Expanded Sturm and old Mobius comparisons share the reused kernel; they are not independent arithmetic implementations.

The executed backend is PINNED_PURE_FUNCTION_TRANSCRIPTION. Connector-returned pure polynomial/Sturm and resultant functions were transcribed into standalone kernels. The full repository package was not imported; repository CI and Lean were not run. The optional repository backend is provided for an actual integration check, but no such run is claimed.

## 9. Reuse and prior art

Resolution: COMPOSE_APPLIED / EXTEND_EXISTING_TOOL for this interface; REUSE_EXECUTED only for the pinned pure source functions and REUSE_APPLIED for the operation-lease/Mobius laws.

- T0_BRC: preserve factor/root-support information until the declared observer permits loss.
- T1_SCALE_ENUMERATION_VALUATION: existing finite overlap and Mobius laws.
- T6_OPERATION_SAFE_QUOTIENT: declared future operations and their coarsest observation signature.
- src/enterprise_math/brc_critical_degeneracy.py, blob 8abc2ed4608bd222d16b6453e4f48f7b80566653: polynomial gcd/division/Sturm.
- experiments/brc_factorized_selector_mobius_check.py, blob 186cdd02f1e599b8511fb4159e9cd7af6cda1bad: endpoint-deflation, subset-gcd and derivative-chain laws.
- experiments/brc_newton_resultant_event_generator_check.py, blob ff01133934706a309e7499d702fc0a3777e88e17: polynomial-in-t and Sylvester functions.

All source pins belong to the frozen baseline. The general toolbox executable was not run; lookup is not counted as execution.

Classical antecedent: David Y. Y. Yun, On square-free decomposition algorithms, SYMSAC 1976, DOI 10.1145/800205.806320. Author-institution page: https://research.ibm.com/publications/on-square-free-decomposition-algorithms . This documents prior squarefree algorithms, not optimal complexity or novelty of the present implementation. Unique factorization, gcd refinement, finite-set Mobius inversion and resultant guards are classical; the exact specialized statements used above are proved explicitly.

## 10. Durable frontier and smallest next unit

Closed here: canonical valuation atoms; gcd-only fixed-coefficient compilation; exact simultaneous observers; minimal fixed-interval count signature; associative no-gcd monomial pushforward; regular-specialization theorem; and the permanent-overlap witness.

Next unit: an automatic generic atom compiler over Q(t)[x] with explicit denominator/scalar guards, feeding the existing event-root/chamber interface. The decisive test is producing a nonzero guarded atom certificate for the permanent-overlap family WITHOUT supplied atoms, while keeping exceptional parameter points typed. Denominator/scalar failure, nonregular atom guards and persistent endpoints must return a typed exception rather than silently specialize the generic certificate.

Not claimed: complete parametric factorization/CAD, signed/interfering branches, infinite-state semantics, independent theorem review, Lean certification or Foundation promotion.
