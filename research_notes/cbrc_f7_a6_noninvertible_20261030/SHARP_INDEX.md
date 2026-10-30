# CBRC F7 A6 — sharp free-index bound for the channel-support survivor

**Status:** AUTHOR_SIDE / SHARED_EXPOSED_CONTEXT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This is a supplementary theorem about the *specific scalar* from the existing draft [A6 survivor](PROOF.md), not an independent Driver review, a new Source Result, a general lower bound for all F7 scalars, or a change to the frozen reversible F7 no-go.

## Setup and exact theorem

On the free part of the F6 two-slot carrier, write (w=(n_1,m_1,n_2,m_2)^Tinmathbb Z^4) and

[
C=egin{pmatrix}1&1\\1&-1end{pmatrix},qquad D=operatorname{diag}(C,C),qquad
Q(w)=q(n_1,m_1)+q(n_2,m_2)=	frac12sum_{i=1}^{4}mathbf 1_{(Dw)_i
e0},
]

where (q(n,m)=igl(mathbf1_{n+m
e0}+mathbf1_{n-m
e0}igr)/2). Torsion labels do not enter this scalar. No native two-dimensional geometric plane is asserted.

**Theorem (sharp index 16, fixed scalar).** Let (Ain M_4(mathbb Z)) satisfy

1. (Q(Aw)=Q(w)) for every (winmathbb Z^4); and
2. for (e_1=(1,0,0,0)^T), each of the two output slots of (Ae_1) has scalar (1/2).

Then there exist a permutation matrix (P), with its images of input channel 1 and 2 in *different* output channel pairs ({1,2}) and ({3,4}), and nonzero integers (k_1,dots,k_4), such that

[
oxed{A=D,P,operatorname{diag}(k_1,k_2,k_3,k_4),D},qquad
oxed{det A=16,operatorname{sgn}(P)prod_{i=1}^{4}k_i.}
]

Conversely, every such (P) and nonzero integer (k_i) defines an integral endomorphism satisfying both conditions. Thus (|det A|ge16), (16middet A), and the bound is attained by the previously exhibited (A=DPi D). There are exactly **16** admissible split permutations (P), before choosing the four nonzero integer multipliers. In particular, conservation plus elementary balance alone force nonzero rank-one coupling in **all four** (2	imes2) slot blocks for this fixed scalar; separate block-rank assumptions are unnecessary.

## Proof

Put (L=Dmathbb Z^4={hinmathbb Z^4:h_1equiv h_2pmod2, h_3equiv h_4pmod2}), and (T=DAD^{-1}in M_4(mathbb Q)). Since (2e_jin L) for each (j), conservation says
(#operatorname{supp}(T(2e_j))=#operatorname{supp}(2e_j)=1). Thus **every column of (T) has exactly one nonzero entry**.

Also (A) is nonsingular over (mathbb Q): otherwise its rational kernel contains nonzero (winmathbb Z^4), while (Q(Aw)=0<Q(w)) (because (D) is invertible). Therefore the four nonzero column entries of (T) occur in **distinct rows**, so
(T=Poperatorname{diag}(lambda_1,ldots,lambda_4)) with a permutation (P) and (lambda_iinmathbb Q^	imes).

The input (e_1) has (De_1=(1,1,0,0)^T). Each balanced output slot has exactly one nonzero channel (its scalar equals (1/2)), so (P) sends channels 1 and 2 to opposite output pairs. Since it permutes all four channels, channels 3 and 4 must likewise occupy one unused channel in each output pair.

Write (A=D^{-1}TD=	frac12D Poperatorname{diag}(lambda_i)D), using (D^2=2I). Each (2	imes2) output-slot/input-slot block contains exactly one mapped input channel. Its four entries are consequently (pmlambda_j/2) for the unique corresponding channel (j). Since (A) is integral, (lambda_j/2inmathbb Z) for every (j). Put (lambda_j=2k_j
e0). This yields the displayed classification and the determinant formula, because (det D=4).

For the converse, (A=D Poperatorname{diag}(k_i)D) is integral and (DA=2Poperatorname{diag}(k_i)D), which permutes the four channels and multiplies each by a nonzero integer. Their supports, hence (Q), are preserved globally. The split permutation ensures the marked elementary input has precisely one nonzero channel in each output slot. Each slot block consists of a nonzero outer product, hence is rank one. The 16 split permutations are counted by choosing which output pair receives channel 1 (2 ways), its position within that pair (2 ways), channel 2's position in the other pair (2 ways), and the arrangement of channels 3 and 4 in the two leftover positions (2 ways). The witness (k_i=1), (P=Pi) gives (|det A|=16). QED.

## Scope, falsifiers, and reproducibility

The theorem classifies the **free-coordinate matrix for this particular indicator-channel scalar**. It does **not** classify arbitrary nonnegative conserved (q), torsion couplings, different ablations, or a primitive native X6 transformation. An injective full-carrier extension takes the torsion component to itself as in the original A6 witness. Proof uses exact integer/rational algebra; finite checks are only regression evidence.

A separate exact checker `SHARP_INDEX_CHECK.py` enumerates all 16 split permutations, 4,096 examples with (k_iin{-2,-1,1,2}), and 625 integer free inputs per example, checking conservation, all rank-one slot blocks, elementary balance, and the determinant formula. The universal proof above does not rely on this finite range.

Frozen Result: `RR-AA38973D56330E59D315`, original Result blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`. Existing author-side parent: draft PR #1753. Do not infer a native Review/Reference/Synthesis/Follow-up or mathematical admission from this file.
