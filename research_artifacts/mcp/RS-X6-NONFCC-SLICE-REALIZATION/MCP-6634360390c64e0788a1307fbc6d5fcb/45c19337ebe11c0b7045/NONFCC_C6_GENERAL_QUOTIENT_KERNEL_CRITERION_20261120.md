# NONFCC C6: exact kernel criterion for loss of native simple loops under any affine abelian quotient

Task: RS-X6-NONFCC-SLICE-REALIZATION (publication TP2-A3C8E1D754209B6F31D4)
Author contribution: EM-X6-C7A253; original own Sites session MCP-6634360390c64e0788a1307fbc6d5fcb
Status: AUTHOR EXACT COMBINATORIAL DERIVATION + FINITE EXHAUSTIVE CHECK; NOT INDEPENDENT REVIEW; NOT A FACE/PATH NATIVE CARRIER REALIZATION.
Input: signed X6 three-axis centered Cell subtorsor (enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md).
Prior verified source: enterprise-math@199469204ab7c4607d0a1d55f3cd136719eef898, research_artifacts/mcp/RS-X6-NONFCC-SLICE-REALIZATION/MCP-6634360390c64e0788a1307fbc6d5fcb/bc19fa74082901c9f95f/NONFCC_NATIVE_TO_CARRIER_C6_PROJECTION_LOSS_20261118.md (84/108/0/528 for STAR kernel (1,1,1)). No repeated assertion of separate STAR/FACE/PATH physical structure.

## Exact definitions
Select three *distinct* signed native X6 spatial axes and fix their chosen Cell anchor. Relative Cell coordinates are Z^3. Let W consist of all 6!=720 ordered words using each of +e1,-e1,+e2,-e2,+e3,-e3 exactly once. Their six-step native Cell paths close. W_s is the subset with all six preterminal Cell coordinates distinct. An observer in this note is an affine map f(v)=a+h(v), where h:Z^3 -> A is a homomorphism to any abelian group A. Vertex-simple after observing means the six preterminal f(v) are pairwise distinct; no claim that A has an admitted circular carrier, a physical gate/force incidence, or a primitive rotation.

## Theorem: exact universal simplicity criterion
For the entire finite class W_s,
    (every native-simple signed C6 word remains vertex-simple under f)
iff
    ker(h) ∩ ({-1,0,1}^3 \ {(0,0,0)}) = ∅.
In particular this condition depends on the kernel, not only on its ambient rank.

Proof. For any W word, each signed direction appears exactly once. Thus each coordinate of every prefix lies between -1 and 1, and any difference of two prefixes has each coordinate in {-1,0,1}; if the word is in W_s, no such difference is zero. Observed vertex equality is equivalent to a nonzero prefix difference in ker(h), proving sufficiency. For necessity, consider the native-simple word (+e1,+e2,+e3,-e1,-e2,-e3). Its 6 preterminal vertices are 0,e1,e1+e2,e1+e2+e3,e2+e3,e3. Up to permutation and sign reversal of the three coordinate labels, this word exhibits some pair of preterminal vertices with *every* prescribed nonzero ternary difference d in {-1,0,1}^3: support size one from a single step; support size two from a 2-step monotone segment; support size three from a 3-step monotone segment. Signs on axes can be independently relabeled at the combinatorial word level. Therefore the union of pairwise preterminal differences over W_s equals all 26 nonzero ternary vectors. If a vector d from that set belongs to ker(h), the corresponding path's observed preterminal vertices collide. QED.
Note: these signed label changes demonstrate only combinatorial coverage in the fixed formal word family, not a physical full signed rotation group.

For a surjective homomorphism h:Z^3 -> Z^2 with primitive rank-one kernel Z k (gcd(|k_i|)=1), the criterion specializes to max_i |k_i| >= 2: if all |k_i|<=1 then k itself belongs to the ternary cube, whereas if any |k_i|>=2 every nonzero integer multiple of k lies outside it. The specified map h(x,y,z)=(x-2y,z) is surjective and has kernel Z(2,1,0); it preserves vertex simplicity for all native-simple six-edge words despite reducing coordinate rank. This is only an algebraic observer example.

## Exact finite witness counts
A fully exhaustive standard-library checker examines all 720 permutations, finds 192 native-simple paths and exactly all 26 nonzero ternary vectors across their pair differences. For projection kernels Z k with primitive k:
- k=(1,0,0): 0/192 remain observer-simple, 192 lose simplicity;
- k=(1,1,0): 48 remain, 144 lose;
- k=(1,1,1): 84 remain, 108 lose (the previously published STAR case);
- k=(2,1,0): 192 remain, 0 lose.
These four counts are exact for the declared finite W_s family; the universal theorem's quantifier is over W_s and affine abelian observers f, not all native trajectories or the actual FACE/PATH carriers. Sign and coordinate permutation of k preserve these combinatorial counts.

## Contribution to the task
This separates two independent questions that the historical S4/FCC image can obscure: (1) can a proposed native-to-observer quotient distinguish all first six Cell positions of the allowed C6 walks? This theorem completely answers that first question via short kernel vectors, even when the observer reduces coordinate rank. (2) is that quotient an actual FACE/PATH circular carrier, and does it respect triadic incidence/rotation, Path/BRC provenance, and physical admission? Those are unresolved. A finite algebraic no-collision example does not supply an admitted non-FCC carrier. The successor must test candidate FACE/PATH relations under the frozen Cell/Port/Channel and triadic incidence rules before asserting realization.

Reproduce: python3 check_nonfcc_c6_kernel_criterion_20261120.py.
