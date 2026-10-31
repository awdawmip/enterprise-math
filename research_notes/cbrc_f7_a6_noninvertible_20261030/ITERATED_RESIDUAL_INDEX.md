# F7 A6 — Iterated support conservation and a 3-step residual-index cycle

**Status:** `AUTHOR_SIDE / EXPOSED_SHARED_CONTEXT / NOT_INDEPENDENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`. This is a supplementary mathematical statement about the explicit non-surjective A6 witness in this Draft PR, not a native Driver review, F7 Result rewrite, new Task, or promotion.

**Exact scope:** the fixed four-channel auxiliary scalar from `PROOF.md`, with the explicit integral matrix
[
A=egin{pmatrix}
 1&1&1&1\
 1&1&-1&-1\
 1&-1&1&-1\
 -1&1&1&-1
end{pmatrix}.
]
On the full finitely generated abelian carrier (G=(mathbb Z eoplusmathbb Z foplusmathbb Z/3,	au)^2congmathbb Z^4oplus(mathbb Z/3)^2), take (M=(A,mathrm{id}_{(mathbb Z/3)^2})). This is **not** a statement about arbitrary injective endomorphisms, native six-dimensional rotations, the frozen reversible F7 theorem, or physical dynamics.

## Theorem — 3-step exact power and cokernel cycle

Let (C=egin{psmallmatrix}1&1\\1&-1end{psmallmatrix}), (D=operatorname{diag}(C,C)), and let (Pi) be the channel permutation
((u_1,v_1,u_2,v_2)mapsto(u_1,u_2,v_2,v_1)). Then (D^2=2I_4), (Pi^3=I_4), and (A=DPi D). For every (nge0),

1. **Three-step dilation:** (A^3=8I_4); consequently (A^{3t+r}=8^t A^r) for (tge0), (rin{0,1,2}). Each iterated map (M^n) is injective and has image index (16^n).
2. **Conserved coarse observer, growing invisible index:** writing the original scalar as
   (Q(w)=sum_{j=1}^4 phi((Dw)_j)), where (phi(0)=0) and (phi(z)=1/2) for nonzero integers (z), we have
   [
   DA^n=2^nPi^n D,qquad Q(A^nw)=Q(w)
   ]
   for all (winmathbb Z^4). The support-count observer is exactly preserved at *every* step even though the cokernel/index grows. This distinguishes retained branch-support observation from the unobserved lattice-amplitude and quotient information; it does not assert a nonzero physical residual.
3. **All-time Smith form:** for (n=3t+r), the ordered Smith invariants of (A^n) are respectively
   [
   egin{array}{c|c|c}
   r & (d_1,d_2,d_3,d_4)& operatorname{exp}(operatorname{coker}M^n)\\hline
   0&8^t(1,1,1,1)&8^t\
   1&8^t(1,2,2,4)&4cdot8^t\
   2&8^t(2,4,4,8)&8cdot8^t
   end{array}
   ]
   with the convention (mathbb Z/1=0) and exponent (1) for the trivial group. In fact (operatorname{coker}M^ncongigoplus_{j=1}^4mathbb Z/d_jmathbb Z); the source ((mathbb Z/3)^2) contributes no cokernel because the torsion component is the identity.
4. **Non-closure of the marked elementary balance under composition:** for the original marked input ((e,0)), the two output slot scalar values after (n) iterations are (1/2,1/2) when (nequiv1,2pmod3), but (1,0) when (nequiv0pmod3). Therefore the one-step A0/balance condition is **not invariant under repeated composition**, despite conservation holding at every step. This conclusion concerns the *iterated* map, not a failure of A0 in the original one-step A6 witness.

## Proof

The permutation has one fixed channel and one three-cycle, hence (Pi^3=I_4). Since (D^2=2I_4),
[
A^3=DPi D,DPi D,DPi D=4DPi^3D=8I_4.
]
By induction, (DA^n=2^nPi^n D) (including (n=0)), giving the conservation law because a permutation and multiplication by a nonzero integer preserve channel nonzeroness. Also (det A=(det D)^2detPi=16), so (|det A^n|=16^n).

To compute the Smith form of (A), the gcds of its (j	imes j) minors for (j=1,2,3,4) are (1,2,4,16): an entry is (1); every (2	imes2) minor is (0) or (pm2), and (detegin{psmallmatrix}1&1\\1&-1end{psmallmatrix}=-2) occurs; (A^TA=4I) and (det A=16) imply (operatorname{adj}(A)=4A^T), so every (3	imes3) minor has absolute value (4); the determinant is (16). Successive determinantal-divisor ratios are ((1,2,2,4)).

Moreover (A^{-1}=A^T/4) and (A^3=8I), hence (A^2=2A^T). The Smith invariants of (A^2) are (2(1,2,2,4)=(2,4,4,8)). Scaling an integral matrix by (8^t) scales each Smith invariant by (8^t); this proves the table for all (n), not merely a finite sample. The torsion-label block of (M^n) is the identity, so its cokernel is exactly the free-block cokernel.

Finally (D(e,0)) has channel vector ((1,1,0,0)). Under (Pi^n), both nonzero channels occupy the first slot for (nequiv0pmod3), and they split one per slot for the other two residues; the factor (2^n) does not affect support. This proves the marked balance cycle.

## Independent calculation / limitations

A separate exact-integer symbolic regression reproduced (A^3=8I_4), (A^TA=4I_4), (det A=16), the Smith invariants of (A^n), (A^{3t+r}=8^t A^r) and (det(A^n)=16^n) for every (0le nle12). The proof above carries the universal quantifier; the finite regression is not substituted for it.

This result is author-side and exposes the same prior F7/A6 context as other notes in this PR. It **must not** serve as an independent decisive review of frozen Result `RR-AA38973D56330E59D315` (Git blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`). The original F7 `GL_4(mathbb Z)` no-go and all frozen review/provenance records stay unchanged. An authorized independent Driver may later assess the result as supplementary evidence, after reading the complete exact review set with current DA.

**Next precise scientific question (not a published Task):** classify the period, growth and observer-fiber behavior of the *other 15* channel-splitting permutations and integer multipliers in the existing A6 fixed-scalar family, without assuming this witness's three-cycle persists.
