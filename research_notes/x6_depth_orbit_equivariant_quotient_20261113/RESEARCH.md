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
