# F7 A6: all scalar laws of general split monomial free blocks, and unconditional torsion elimination

2026-11-27; same-lane informed Driver continuation. Previous lane EM-DVR-DEBB5E; original author EM-CBRCF7-83A1D4 retains F7 theorem/retraction provenance. No new formal review or acceptance. Frozen input bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md. Extends 669363d00332e93d315a488eb9e23dccff4389ff:research_notes/driver/2026-11-27_f7_all_scaled_split_scalar_laws_and_torsion_elimination.md and the free-block classification at 60122a1647c3012f8143b89e0c416dcf5b60dbe1:research_notes/driver/2026-11-27_f7_arbitrary_scalar_full_rank_endomorphism_index_classification.md. The theorem below holds directly for every specified split block, independently of the necessity proof in that classification.

## Statement

Use all F7 scalar axioms and exact conservation; drop only the operation automorphism requirement (A6). Fix a split monomial block in oriented coordinates w=(an+bm,-an+bm), gcd(a,b)=1, ab nonzero. Write K=2|ab|. Each of the four signed channel multipliers lambda_i is a nonzero integer multiple of K. The permutation sends the two channels of each input slot to different output slots. The oriented chart differs from the earlier chart by a sign on the second channel of each slot; lambda_i include both input and output coordinate signs. The torsion lift is arbitrary: M(x,t)=(Ax,Vx+Ut) with U any 2x2 F3 matrix and V any free-to-torsion map.

ALL admissible scalars, including elementary balance, are exactly
  q(n,m,t)=G(an+bm)+G(-an+bm),
where G:Z->R_nonnegative is unique for q and
  G(0)=0; G(z)>0 for z!=0;
  G(a)=G(-a)=1/2;
  G(lambda_i z)=G(z) for all i,z.

This removes the previous 3-not-dividing-b restriction even for invertible torsion U, and handles arbitrary unequal signed multipliers. No assumption of evenness of G is required. The result combined with the previous free-block and singular-free-block necessity proofs gives the full A6 scalar-law classification subject to independent review of those earlier proofs.

## 1. Universal torsion elimination for split blocks

Let D(n,m)=max_t q(n,m,t)-min_t q(n,m,t), over F3. It is unchanged by torsion translation/permutation. The inherited J implies that in the oriented chart D(w1,w2)=D(w2,w1); R implies D(e)=0 because old coordinate 1 acts transitively on torsion.

If U is singular, use the prior kernel-shift lemma: choose nonzero (h1,h2) in ker U. Shifting both input labels leaves outputs unchanged, so the two input scalar differences sum to zero for all independent input states. Each difference is constant; summing three iterates forces zero. At least one nonzero hi generates F3, proving D identically zero.

If U is invertible but not monomial, at least one input torsion axis has no row of U supported solely on that axis (otherwise the two rows are monomial). Fix free inputs and the label on that axis; average conservation over the other label. Each output label is uniform since its row has nonzero coefficient of the averaged label. The output mean is independent of the fixed label, so the corresponding input q is independent of its torsion label for every free point. Again D=0.

It remains to treat invertible monomial U. Varying one input label while fixing everything else varies exactly one output label, bijectively. Comparing maxima and minima of conservation gives equality of D at that input free state and at the corresponding output free state. Fix the other free input to zero. The selected output depends on just one chart channel of the varied free input, by splitting. Thus D on the input slot is a function of that channel alone, say h(w_j); J swaps the two channels, so also D=h(w_{3-j}) on the chart lattice. This lattice is
  W={(u,v) in Z^2 : u-v in 2a Z, u+v in 2b Z}.
In particular (Kz,0) belongs to W for every z, and h(Kz)=h(0). Every output channel is a multiple of K, so D is the same constant h(0) on every output free state. Equality of input/output D then makes D globally constant; D(e)=0 forces it to vanish. This argument does not require any mod-3 avoidance witness, and applies equally when 3 divides b or the multipliers.

## 2. Scalar separation on the actual finite-index chart lattice

After torsion elimination, write q as a function F on W, symmetric by J. In conservation with only the first input slot nonzero, splitting yields
  F(u,v)=g1(u)+g2(v),
where g1 and g2 are evaluations of F on the respective output single-channel axes after multiplication by the appropriate lambda. These axis points belong to W because K divides every multiplier. Both functions vanish at zero and are strictly positive away from zero by old-projection separation. Applying the swap symmetry and averaging, set g=(g1+g2)/2; then
  F(u,v)=g(u)+g(v)
on W, with g positive away from zero and g(0)=0. This does not assume that W equals the full integer grid or that the operation is surjective.

For input channel i define h_i(z)=g(lambda_i z)-g(z). Conservation with the other slot zero gives h_i(u)+h_j(v)=0 for each input pair (i,j) and every (u,v) in W. In particular h_i(Kz)=0 for all i,z by taking the partner channel zero. Also h_i is K-periodic: for each z there exists a partner v with (z,v) in W by coprimality; (z+K,v) is again in W. This periodicity describes the possible separable-coordinate defect.

The key exact cancellation is stronger. For any i,j and z, lambda_j z and lambda_i z are multiples of K, hence
  g(lambda_i lambda_j z)=g(lambda_j z)=g(lambda_i z)
using the vanishing of h_i and h_j on KZ. Consequently all g(lambda_i z) coincide. Define G(z)=g(lambda_1 z). Then G(lambda_i z)=G(z) for every i, and all h_i(z) equal G(z)-g(z). Their pairwise cancellation on W proves
  F(u,v)=G(u)+G(v)
on the full domain W. G is nonnegative, strictly positive for nonzero z, zero at zero. For q(e)=1, G(a)+G(-a)=1. The elementary split outputs have exactly one nonzero channel each, so elementary balance is equivalent to G(a)=G(-a)=1/2.

Uniqueness: for each z, F(lambda_1 z,0)=G(lambda_1 z)=G(z), as this point belongs to W. Thus the coordinate defect of g does not produce a second parameterization of the same scalar.

Conversely any G satisfying the stated conditions gives a scalar on the original carrier. J swaps the oriented coordinates, R and S change only torsion, positivity holds because a,b are nonzero, and the signed monomial channel action conserves the sum term by term. Balance and A0 hold on the split elementary input; the torsion lift has no effect. This completes the direct infinite-domain proof.

## 3. Exact parameter space and sign asymmetry

Let H be the multiplicative subgroup of Q^* generated by lambda_1,...,lambda_4. For nonzero integers z,z', the equivalence generated by z~lambda_i z is precisely z'/z in H. Indeed an equality z'/z=product lambda_i^{e_i} with integer exponents can be cleared into equality of two integer products of forward multiplications. The converse follows by multiplying ratios along any path. Thus G is an arbitrary positive function on the nonzero integer intersections of H-cosets, with the cosets of a and -a normalized to 1/2. There are countably infinitely many free cosets, since prime valuations outside the finite prime support of all lambda_i remain unchanged, so there are continuum many laws. If -1 belongs to H, evenness is forced. If -1 does not belong to H, the two sign cosets of any z are distinct, and asymmetric laws exist (choose z outside the normalized cosets). In particular, take a=b=1 and lambda=(2,4,6,8) in oriented coordinates with any split permutation. G(1)=G(-1)=1/2, G(5)=1 and G(-5)=2, with all remaining nonzero cosets assigned 1/2, gives a valid asymmetric law. The actual q is also asymmetric in the new direction: q(0,5)=2, q(0,-5)=4. This is consistent with J acting on the old direction, not with an extra new-direction symmetry. For the earlier scaled H family the oriented multipliers contain both +2k and -2k, so -1 is in H and the even-G classification is recovered.

## 4. Exact finite regression (converse)

Executed JS integer arithmetic on safe integers, 5 coprime positive chart pairs (1,1),(1,3),(2,3),(3,2),(4,3), all 16 split permutations, multiplier tuples K*(1,2,3,4), K*(-1,2,-3,4), K*(-1,-2,-3,-4). For doubled G use G2(0)=0, G2(z)=1+v5(z) for z!=0, except in all-positive cases use 1+2v5(z) for negative z. All multipliers and chart a are coprime to 5. Tested every free input in [-3,3]^4, and elementary A0/balance. 240 matrix/law cases, 576240 conservation checks, all passed; 80 asymmetric-law cases. No finite test is used as the proof of necessity. Reproduction: form w=[an+bm,-an+bm,ar+bs,-ar+bs]; set out[p[i]]=lambda_i*w[i]; recover each slot by n=(u-v)/(2a),m=(u+v)/(2b); check integrality and the sum of the four G2 values before and after; for elementary w=(a,-a,0,0), check both output differences nonzero and each pair sum equals 1. All chart values and outputs stay well inside exact JS integer range.

## Remaining scope

General unequal-multiplier scalar laws and the residual torsion question are solved on the full specified split family. The earlier free-block necessity and singular obstruction remain pending independent audit, not assumed accepted. The original reversible F7 no-go remains unchanged. Nonreversible typed equivalence of distinct matrices is a separate question; no F8, native Review, Result acceptance, Task completion or mother-objective closure.
