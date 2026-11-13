# X6: Common-depth descent and maximal equivariant finite quotients of signed C6 candidates

Date: 2026-11-13 (Asia/Shanghai). Scientific input remains frozen at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This continues the author-side candidate from Draft PR #2211 (https://github.com/awdawmip/enterprise-math/pull/2211). It is an algebraic result about six signed native coordinate directions, not a change to P000 and not a certification of native TRIADIC_CLOSURE_E, carrier incidence, C12/C24 dynamics, or physical interpretation. Formal Task CLAIM and independent review remain separate.

## Definitions

Fix one native Cell chart. Let M=Z^6, let u=(1,1,1,1,1,1), and let q:M→M/Zu be the min-zero relative-coordinate observation. Its chosen representative is q_min(x)=x-min_i(x_i)u, and exact reconstruction uses the integer common depth min_i(x_i). The groups identified by the prior exact candidate result are

- G_all=(C2)^6 ⋊ A6, all signs and even underlying permutations, order 23040;
- G_even=(C2)^5 ⋊ A6, even sign parity and even permutations, order 11520.

Each acts on M by integer signed permutations.

## Theorem 1: exact q-descender subgroup

For either candidate group, the elements inducing a well-defined action on M/Zu are precisely H={±I}×A6, of order 720.

Proof. A signed permutation preserves Zu iff its image of u is ±u. The image is a vector of six signs, so this condition says the signs are uniform. The underlying even permutation can be any A6 element. Because six is even, -I belongs to both candidate groups and commutes with A6.

An explicit obstruction for the individual six-cycle T_123: q(0)=q(u), but T_123 u=(-1,1,1,1,1,1), whose min-zero image is (0,2,2,2,2,2), whereas T_123 0 has relative image zero. For the compensated generator U_123;4, the image of u is (-1,1,1,-1,1,1), with min-zero image (0,2,2,0,2,2). Therefore neither generator admits a q-only update. QED.

## Theorem 2: universal common-depth-erasing equivariant quotient

For G≤Aut_Z(M), define the orbit lattice L_G=<g u: g∈G>_Z. Then M/L_G is the largest abelian-group quotient of M that annihilates u and supports a well-defined full G action. More precisely, every equivariant quotient M/N with u∈N factors uniquely through M/L_G.

Proof. The G-orbit of u generates the smallest G-stable integer subgroup containing u. Any G-stable kernel containing u contains this orbit and hence its integer span. QED.

For G_all, the orbit is every sign pattern of u. Taking differences from u gives 2e_i for every coordinate; hence

L_all=Zu+2Z^6; Q_all=M/L_all≅(Z/2)^5, |Q_all|=32.

For G_even, the orbit is precisely the sign patterns with an even number of minuses. Their differences from u give 2 times the indicators of even-cardinality subsets. Pair indicators span D6={a∈Z^6:sum_i a_i even}, giving

L_even=Zu+2D6; Q_even=M/L_even≅Z/4×(Z/2)^4, |Q_even|=64.

Proof of the second group structure. Since [Z^6:D6]=2, [Z^6:2D6]=128. The class of u modulo 2D6 has order 2: u is not in 2D6 and 2u is, because six is even. Thus [Z^6:L_even]=64. Every 4e_i belongs to L_even, while 2e_i does not, so the quotient has exponent four. Modulo 2, L_even reduces to the one-dimensional all-ones span, making Q_even/2Q_even five-dimensional over F2. The 2-group classification then gives one Z/4 factor and four Z/2 factors. QED.

## Theorem 3: faithfulness of the finite actions

The action of G_even on its 64-element quotient Q_even is faithful: its kernel is trivial. By contrast, the kernel of the action of G_all on Q_all is precisely the full 64-element sign subgroup, with induced faithful A6 action of order 360.

Proof. If a signed permutation acts identically on Q_even then for every basis vector e_i, its image ±e_j has difference ±e_j-e_i in L_even. Such a difference with j≠i has odd entries in only two places, but vectors in L_even have either all-even or all-odd coordinates, so j=i. A negative sign with j=i would require -2e_i∈L_even, which fails because e_i has odd coordinate sum and 2e_i∉2D6. Thus every basis vector is fixed. For Q_all, -e_i and e_i have equal classes because 2e_i∈L_all, so all sign changes act trivially; any nonidentity permutation moves at least one basis class as e_j-e_i∉L_all for j≠i. QED.

## Scientific significance and exact scope

The 64-state finite quotient faithfully represents all 11520 candidate transformations as group automorphisms while retaining only a compact torsion-valued observer of the original coordinates. This is a novel exact algebraic bridge for finite symmetry/phase calculations. It is not a lossless native Cell-address codec or a general BRC path/history observer: raw six-coordinate positions, branch identities, multiplicities, intermediate Cell states and time must still be retained where those later observations require them. The full integer common-depth repair (q_min(x), min_i x_i) is a bijective encoding of M and supports all signed permutations without information loss.

## Verification

The companion Python 3 standard-library verifier exhausts 23040 and 11520 signed permutations by exact BFS, counts 720 descenders for each, computes action kernels 64 and 1 respectively, checks every residue of (Z/4)^6 (4096 cases) against the stated orbit-lattice membership, and verifies the concrete min-zero witness. All checks passed in local CPython; EXACT_OUTPUT.json contains actual program output. No floating-point calculations are used.

## Next executable mathematical questions

Classify the G_even orbits and stabilizers on the nonzero 64-state quotient and find whether any such orbit yields a useful exact C12/C24 observer with declared paths and time. Independently test the concrete candidate generators against the native triadic closure and carrier incidence contracts. For narrower operation families, compute the orbit lattice of only those authorized operations rather than requiring full G_even invariance.

**Control**: This is research preservation on a Draft PR branch, not a claimed formal Result. A previously dispatched X6 Task request and a new native session registration were QUEUED when this note was authored; ownership must be checked against the completed original receipts before prepare/CLAIM/open.


## Theorem 4: complete 64-state orbit classification

The faithful G_even action on Q_even has exactly **five orbits**, of sizes **1, 1, 12, 20 and 30**. The two fixed points are the classes of 0 and 2e_1 (the latter equals every 2e_i in Q_even). All other 62 states lie in three nonzero-parity orbits.

Proof. Reduction modulo 2 induces the G_even-equivariant map Q_even → V=F2^6/<u>, with 32 target classes and fibers of size two. The A6-action on V classifies its vectors by the number k of ones up to complement, k=0,1,2,3. The respective counts are 1,6,15,10. The two elements over k=0 are 0 and z=[2e_1]; every signed permutation fixes both because [±2e_j]=z in Q_even. For any nonconstant parity vector b, select i and j with b_i≠b_j. The allowed even sign flip D_{ij} changes [x] by [−2x_i e_i−2x_j e_j]=(b_i+b_j)z=z, interchanging the two points above b. Since A6 acts transitively on k-element subsets of {1,...,6} for k=1,2,3 (and complement does not change the class), the three nonzero classes yield one orbit each, of sizes 2·6=12, 2·10=20 and 2·15=30. QED.

A separate exhaustive modular quotient test in EXPERIMENT_Q64_ORBITS.py enumerates all 4^6=4096 residues, constructs the 64 quotient classes, and applies all 60 compensated candidate generators. It confirms these five orbit sizes and, for one chosen order-six U generator, cycle decomposition **1^8 · 2^4 · 3^8 · 6^4** (8 fixed classes, four 2-cycles, eight 3-cycles, four 6-cycles). The cycle result is a precise finite test for that chosen generator; an extension to all constrained native dynamics remains a separate question.

The exact 12-state orbit is a natural next compact signed-direction/phase research candidate. Its relation to the project's actual BRC C12 carrier semantics is to be established by a typed observer and future-operation bridge, while preserving full path provenance.


## Theorem 5: exact minimal-memory C(6m) lift of a selected C6 cycle

A full enumeration of the 11,520 elements of G_even gives possible element orders only **1, 2, 3, 4, 5, 6, 8, 10**. Consequently no *single signed-permutation element* of this exact candidate group can produce a 12-cycle or 24-cycle on any quotient. This follows algebraically because the underlying permutation lies in A6, whose possible cycle types are 1^6, 2^2·1^2, 3·1^3, 3^2, 4·2 and 5·1; on a signed cycle of length d the lifted order is either d or 2d, yielding only the listed orders after taking least common multiples. The code exhaustively verifies the distribution for G_even:
order 1:1, 2:391, 3:800, 4:2520, 5:2304, 6:1760, 8:1440, 10:2304.

Nevertheless, the selected compensated generator g=U_123;4 has an exact six-state orbit O={x_0,...,x_5} on Q_even (the concrete states are in PHASE_COVER_OUTPUT.json). For **every positive integer m**, introduce a separate residual fiber Z/mZ and define the skew-product update on O×Z/mZ:

Phi_m(x_j,r) = (x_{j+1 mod 6}, r + 1_{j=5} mod m).

**Theorem.** Phi_m is one cycle of exact length **6m** on the 6m states of O×Z/mZ. Moreover, among all deterministic lifts of the same fixed six-cycle on O that have an exact 6m-cycle, a fiber with at least m states is necessary. Thus the construction uses the minimum possible number of discrete residual states per base Cell-observer state.

**Proof.** Every six steps traverse the chosen orbit once, crossing j=5 exactly once, so Phi_m^6(x_j,r)=(x_j,r+1 mod m). Returning to the initial base position requires a multiple 6k of steps; returning simultaneously to the initial fiber requires k≡0 mod m. Thus the first full return occurs after 6m steps. For any other lift with a 6m-cycle projecting to a six-cycle, each of the six base points appears exactly m times in the 6m distinct extended states, so each base fiber has at least m states. QED.

For m=2, a **single residual bit** yields an exact 12-step cycle; for m=4, **two residual bits** yield an exact 24-step cycle. The extension creates temporal/order-dependent residual structure on a specifically selected candidate orbit, not a new seventh spatial coordinate and not a frozen heartbeat period. A discrete event trace may be written (x_t,r_t;t) with separately typed time t; physical calibration and native C12/C24 carrier compatibility remain to be established. This provides an explicit constructive alternative to identifying C12/C24 with the order of one signed spatial rotation.

Exact tests for m=1,2,3,4,5,7 verify periods 6,12,18,24,30,42 and minimal full-state return, with no changed scientific input. Program: VERIFY_X6_PHASE_COVER.py; evidence: PHASE_COVER_OUTPUT.json. Next: incorporate actual primitive path/branch information into the carry event and determine which typed C12/C24 observers factor through the resulting lifted state.
