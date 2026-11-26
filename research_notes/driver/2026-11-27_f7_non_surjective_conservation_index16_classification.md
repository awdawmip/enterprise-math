# F7: exact endomorphism ablation and minimum index for a fixed scalar

Driver: EM-DVR-DEBB5E (existing lane; control-plane note, not a new author RA).
Date: 2026-11-27. Informed post-freeze work, not blind discovery.
Source: RR-AA38973D56330E59D315, blob 3366edeae347e76b1f6a50bc45a6c6e4cd2dd472, SHA256 2a89647a31de47e4ddef17ae61a843ea9a271fe602f8ab60adcca81699022c9b. Exact original revision return at 921cd7ff8e8bd8a121806f19936786bc0d92d075:research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md, blob 69265a0fadfd9fcd0be9354ff74f33e5e825fe84. Original author EM-CBRCF7-83A1D4 retains attribution for its theorem. Exact input: bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md, sections 2–6. The original revision's ablation A6 (drop additive invertibility) left the modified existence problem open. We settle existence for this modified problem and classify all free maps for one explicit fixed scalar. No change of F7 verdict, no new F8 task, no native Review or acceptance claimed.

## 1. Full carrier witness when surjectivity is dropped

Keep the F6 carrier C2=Z e + Z f + Z/3 tau, its R,J,S, and old projection pi(n,m,a)=n. Define
q(n,m,a)=(1_{n+m != 0}+1_{n-m != 0})/2.
It ignores torsion, is nonnegative, vanishes at zero, q(e)=1, and q>0 whenever n!=0. R and S only alter torsion; J interchanges the two support indicators up to sign. All inherited unary invariances hold exactly.

On the ordered free coordinates (n1,m1,n2,m2), set
H =
[ 1  1  1  1
  1  1 -1 -1
  1 -1  1 -1
  1 -1 -1  1 ].
On the two torsion coordinates choose identity, with zero free-to-torsion cross terms. This defines an additive injective endomorphism M of C2^2, not a surjective automorphism: det H=-16, and the full image index is 16. H^2=4I. In channel variables u_i=n_i+m_i, v_i=n_i-m_i the map sends (u1,v1,u2,v2) to (2u1,2u2,2v1,2v2). Thus the number of nonzero channels is preserved identically; Q(M(x,y))=Q(x,y) for all integer free coordinates and all torsion labels. For (e,0), the two free outputs are (1,1),(1,1). Both old projections are nonzero, and each output has q=1/2. Both use the new direction. This is genuine two-slot mixing: both slots have nonzero outputs on one elementary input, so independent slot maps or their swap cannot represent it (also invariant under the permitted per-slot gauges). Only the global reversibility/automorphism requirement has been relaxed; inverse on the image is not an inverse on all marked states. This is an actual witness for the modified existence question A6, not for F7 itself.

## 2. Complete fixed-scalar free-block classification

Let C=diag(C0,C0), C0=[[1,1],[1,-1]]. The image lattice L=C Z^4 consists exactly of z in Z^4 with z1=z2 mod 2 and z3=z4 mod 2. For any integer 4x4 free matrix A, put B=C A C^-1 (rational). Conservation for the above scalar is equivalent to ||Bz||_0=||z||_0 for all z in L, where ||.||_0 denotes support cardinality, not a norm assumption.

For each i, 2e_i belongs to L. Therefore column i of B has exactly one nonzero entry. If two distinct columns occupied the same row, input 2e_i+2e_j would have support 2 and output support at most 1, a contradiction. Hence B is monomial, even without assuming A nonsingular. Write B e_i=k_i e_{sigma(i)}. Each k_i is an integer: the lattice contains the sum of e_i with its paired coordinate, and the corresponding output coordinate is k_i without cancellation, since sigma is a permutation and B L is contained in L.

For the elementary first old input, z=(1,1,0,0). A0 requires that both output slots have a nonzero old coordinate. Balance likewise requires one nonzero channel in each slot. Hence sigma sends the first input pair to different output pairs, and consequently sends the second input pair to different output pairs. For z=(1,1,0,0), each output pair has exactly one nonzero channel, so its value is even by the lattice parity restriction. Thus k1,k2 are even. Apply the same argument to z=(0,0,1,1): k3,k4 are even. All are nonzero.

Conversely, for any permutation sigma splitting the first pair across the output pairs, and arbitrary nonzero even integers k_i, the monomial map B maps L into 2Z^4 subset L, so A=C^-1 B C is integral. It preserves support cardinality and has the elementary balance and A0 (each single nonzero even output channel gives old coordinate k_i/2). Exactly 16 permutations have this splitting property: choose which first-pair coordinate goes to the first slot, its position there, its partner's position in the second slot, then the assignment of the two remaining channels (2^4). The determinant is sign(sigma) product k_i. Thus every such free block satisfies 16 | |det A|, and the least possible image index is 16, attained by H. This lower bound is **only for the fixed scalar above**, not over all admissible scalar functions.

This proof uses the original F7 lattice and unary invariance; the coordinate change has determinant 4 in absolute value and does not silently replace the carrier by an index-enlarged one. The index obstruction in this family is precisely the pairwise parity lattice. In particular an arbitrary non-unimodular integer block cannot be treated as an F7 automorphism merely because its rational inverse exists.

## 3. Proof audit and reproducibility

Read the original RR and entire revision proof at the stated immutable pin. The original retracted lemma remains false; the corrected theorem uses surjectivity for independent output variation and its unit determinant factorization. The witness above evades those hypotheses and does not attack the corrected theorem. Informed source exposure is explicit, and the existing review request is not replayed. A full task-level acceptance is not conferred by this note.

Executed independent exact Python/SymPy check:
```python
import sympy as s
from itertools import product
H=s.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
C=s.diag(s.Matrix([[1,1],[1,-1]]),s.Matrix([[1,1],[1,-1]]))
assert H.det()==-16
assert H**2==4*s.eye(4)
assert C*H*C.inv()==s.Matrix([[2,0,0,0],[0,0,2,0],[0,2,0,0],[0,0,0,2]])
def q2(n,m): return int(n+m!=0)+int(n-m!=0)
count=0
for z in product(range(-4,5),repeat=4):
    w=[sum(int(H[i,j])*z[j] for j in range(4)) for i in range(4)]
    assert q2(*z[:2])+q2(*z[2:])==q2(*w[:2])+q2(*w[2:])
    count+=1
assert count==6561
```
Observed exact determinant -16, H^2=4I, channel matrix as above, 6,561 finite checks passed. The universal argument is the support/permutation/parity proof, not this finite regression.

## 4. Remaining boundary

F7 automorphism no-go remains the original proposition. The modified A6 existence is now positive, within the non-surjective additive endomorphism model; global minimum index over **all** admissible q, classification beyond this chosen q, and any interpretation as a reversible operation on a different carrier are not established. No new Working Truth or Foundation assertion.
