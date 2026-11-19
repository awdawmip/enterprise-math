# X6 Unit162 — Frozen C12 rotor consumer versus signed native-axis automorphism

Date 2026-11-19. Task RS-X6-LEGACY-PLANE-RECONCILIATION, publication TP2-B4A441B23DA3159232C2, mother PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Research lane chatgpt-research-onhour-enterprise-math-20260923. Original researcher EM-X6-FB6990 / SID MCP-082892eb480e45dea6d4b9fcc0491034. Frozen scientific input 59538f585d037d09ef687b28715c4bc1a3f9fe03; historical comparison fd2bcff10ca6e147348b6c1236027fc0d2877df3. Status AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. No proposal to alter P000.

## Actual producer and consumer

The historical producer `src/enterprise_math/euler_native_bisector.py` at blob `f6e0162012af2ab10685076e0ff5c0e728ba1ec0` defines `RIGHT_TURN` and `GRAM` (lines 117–118), `six_state_rotor` (185–188), `gate_rotor` (190–193), `interleaved_phase_states` (231–234), and `native_bisector_certificate` (277ff.). The exact same frozen commit contains direct test consumer `tests/test_euler_native_bisector.py`, blob `57eb499033b2432a3b5b325d711c50cf1719e4f0`, particularly lines 15–30, 42–52. The test checks a twelve-state **derived rotation-character matrix representation** over Q(r), r²=1/3; it does not call a six-coordinate native Cell displacement or native N-BRC path counter.

Under that source, R²+R+I=0, G=I+R, H=r(I+G). Thus G²=R, G³=-I, H²=G, H⁶=-I, H¹²=I. The twelve H-phases are character states, not twelve lattice translations. The source itself distinguishes its matrices from the native Enterprise length algebra.

## Exact typed signed-axis bridge / obstruction

Let V=Z^6 denote the **spatial Cell torsor displacement group** of frozen X6, with twelve primitive directions D={±e₁,…,±e₆}. Define an integer automorphism A of the *coordinate displacement graph* by

 A(x₁,x₂,x₃,x₄,x₅,x₆)=(-x₆,x₁,x₂,x₃,x₄,x₅).

Then for every integer x,

 A⁶x=-x, A¹²x=x, and A has exact order 12.

The orbit of e₁ is e₁,e₂,e₃,e₄,e₅,e₆,-e₁,-e₂,-e₃,-e₄,-e₅,-e₆. Hence C12=<A> acts **regularly** on the twelve directed primitive axes. Since A only permutes components and changes signs, for all z it preserves the native coordinate quadratic readout ∑zᵢ², primitive signed adjacency, shortest primitive length ∑|zᵢ| and the exact N-BRC geodesic multiplicity B(z)=(∑|zᵢ|)!/∏|zᵢ|!. The proof is direct: signed coordinate permutation preserves the list of absolute coordinate values; it bijects each ordered primitive step sequence to another by acting on every signed step, preserving source labels and order. This supplies an exact algebraic **candidate** bridge for the twelve-direction orbit; no geometry acceptance is inferred from its existence.

There are two sharp non-transfer facts:

1. The currently frozen positive-axis permutation skeleton S6 cannot itself realize a regular C12 orbit: no permutation of six positive labels has order 12. Indeed cycle lengths partition 6, and lcm 12 would require a cycle length divisible by 4 and another divisible by 3 (at least seven letters), or a length-12 cycle. A belongs to the larger signed permutation group B6, not the specified S6 skeleton.
2. A nonzero primitive step cannot be the translation image of a C12 group generator under any group homomorphism C12→(Z^6,+): 12v=0 in torsion-free Z^6 implies v=0. Rotation character state and primitive translation are different operation types.

The source's derived Q(r) 2×2 rotor H is **not** proved conjugate, equivariant or physically identical to A. Defining such a bridge requires an explicit observer/representation map and its relation to actual rotation operators. A is a graph-level signed-permutation comparison, not a Foundation or P000-sanctioned native rotation. In particular the representation is a different dimension from native six-coordinate spatial displacements.

## Executed exact finite certificate

An independent JavaScript BigInt integer checker constructs all 12 signed basis directions, checks regularity, and enumerates all 5⁶=15,625 vectors z in [-2,2]^6. It confirms A⁶=-I, A¹²=I, preserves squared component length, primitive graph distance and exact factorial N-BRC count for all 12 powers on each state (187,500 power tests); it separately checks A(z+s)=A(z)+A(s) for all twelve primitive step labels on all states (187,500 equivariance tests). Witness z=(2,1,-1,0,0,0) has BRC=12 throughout its orbit. The executed result and reproducible source appear in the same frozen-evidence set. The algebraic proof covers all Z^6; the bounded computation does not independently prove universality. The historical source Python tests and original R063 six-file benchmark were **not** rerun.

## Disposition and actual parent objective

This adds one previously unaccounted historical **real production→test consumer** edge to the 28-LP typed provenance record: `euler_native_bisector.py → test_euler_native_bisector.py`. It confirms a correct derived C12 test boundary and a separately constructed signed-X6 candidate automorphism, **not** a verified LP011 incorrect native argmax or LP019 subtraction of positive N-BRC path counts. Those exact faulty `commit:path:line` remain UNRESOLVED_PROVENANCE. Preserve prior Unit157 existing-P022 correction, Unit160/161 established results, Unit50 native R063 benchmark PASS and review independence. Next source-caller priority remains genuine LP011/LP019 traces, rather than counting valid derived operations as wrong native calls. Units149–152 native semantic association remains distinct pending work.