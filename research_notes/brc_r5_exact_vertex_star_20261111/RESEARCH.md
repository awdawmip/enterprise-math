# R5 — Exact full adjacency star of a fixed 14-arc Blackwell vertex

Date: 2026-11-11 (Asia/Shanghai). Status: author-side proved finite classification with an executed exact rational verifier.

Frozen scientific pins (unchanged): global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Original model: 7 ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10), 30 allowed transfer arcs, 21 observation rows, original fixed physically lawful 14-variable parameter pair. The fixed positive witness is copied byte-for-byte in WITNESS.txt from predecessor PR #2017 (original blob f9e3671e12604bc29ee2cc07ffc59724bafacc90), also used in PR #2021. The 14-arc vertex X is the independently checked exact output from PR #2021, commit 911e6b44eb25e4855a9f32510241e22954d84020; this note restates its full rational masses in VERIFY_ADJACENCY.py. The result belongs to the finite auxiliary Blackwell observer and does not reclassify P000 or native X6 dynamics.

## Theorem: exactly 18 adjacent vertices

Let C be the original 21-by-30 marginal/first-moment observation matrix, q=C E0 with E0 the pinned strictly positive physically lawful witness, and F={E>=0:C E=q}. Let X be the pinned 14-positive-arc vertex in PR #2021. Then X is incident to exactly 18 edges of F. Ten opposite endpoints have 14 positive arcs, and eight have 15 positive arcs. The signed edge differences comprise 13 support-six circuits, two support-nine circuits, and three support-ten circuits.

All these are exact statements about the entire fiber at this fixed physical source-target pair, not a random search sample or a proposed enumerator.

## Complete proof by a one-dimensional column-space quotient

For a point E of F with positive support S, the minimal face containing E has dimension |S|-rank(C_S): its affine direction is the nullspace of C_S, and positivity in the relative interior makes the dimension exact. For distinct vertices X,Y, the midpoint has support U=supp(X) union supp(Y); hence X and Y are adjacent exactly when |U|-rank(C_U)=1.

For X, exact rational row reduction yields rank(C)=15, |S|=rank(C_S)=14. There are 16 zero arcs Z. Every adjacent Y introduces at least one arc from Z, but its union U must satisfy |U|<=16 because rank(C_U)<=15 and the adjacency face has dimension one. Thus all possible neighbors can be detected by insertion of either one or two previously zero arcs.

Choose the 14 independent observer rows I=(0,1,2,3,4,5,6,7,8,9,10,12,15,17) (zero-based). Put A=C[I,S]. This is invertible, and for each k in Z define v_k=A^{-1} C[I,k]. The complementary coordinate lambda_k=C[16,k]-C[16,S] v_k is a scalar quotient coordinate; C[16,*] is sufficient because rank(C)=15 and rank(C_S)=14. Exact evaluation gives lambda=0 on exactly ten missing arcs:
(2,1),(3,1),(4,1),(6,1),(1,3),(1,5),(2,5),(3,5),(4,5),(5,5).

The other six missing arcs have exact values
lambda_(0,2)=-13/20; lambda_(1,2)=-1/4;
lambda_(3,2)=1/4; lambda_(4,2)=1/2;
lambda_(5,2)=3/4; lambda_(6,2)=23/20.

For a single new arc k, a kernel displacement with d_k>0 and all other previously absent arcs at zero exists exactly if lambda_k=0. Its unique ray is d_k=1, d_S=-v_k. Ten such rays exist.

For two new arcs k,l, if both are genuinely new, their positive coefficients must cancel in the one-dimensional quotient: lambda_k d_k+lambda_l d_l=0, with d_k,d_l>0. If both lambdas vanish the candidate union has nullity at least two, so it is not an edge; if exactly one vanishes the other coefficient must be zero. Consequently the only two-insertion edge rays pair one of the two negative-lambda arcs with one of the four positive-lambda arcs: exactly 2*4=8 rays. The unique direction is d_k=|lambda_l|, d_l=|lambda_k|, d_S=-v_k d_k-v_l d_l.

For each of the 18 rays, the checker verifies C d=0 and that the other 16 initially zero coordinates never become negative. The exact first boundary step t=min_{i in S,d_i<0} X_i/(-d_i) is positive. Its endpoint Y=X+t d is rational and nonnegative, satisfies C Y=C X=q, has independent positive columns C_supp(Y), and its support union with X has nullity one. Thus each ray yields a distinct vertex adjacent to X. Every possible adjacent neighbor was in one of the ten single- or eight double-insertion classes above; the list is exhaustive.

The exact step sizes for all 18 endpoints appear in EXACT_OUTPUT.txt. Their positive support distribution is 10 with 14 arcs and 8 with 15 arcs. The displacements have respectively 13 supports of size six, two of size nine, and three of size ten. The 210 six-arc K_(2,3) circuits from #2017 are therefore not the whole adjacency-direction inventory: five exact edges at X change nine or ten arcs, despite six being the global minimum size for a nonzero observer-kernel circuit.

## Verification and subsequent research

Run from this note directory: python VERIFY_ADJACENCY.py. It uses SymPy exact Rational matrices and the copied immutable WITNESS.txt; it checks rank and full observer equality against E0, reconstructs the quotient, enumerates every candidate ray, verifies C d=0, positivity, exact endpoint rank, face dimension, uniqueness, and the support distributions. The previously published physical legality of E0 is reused from #2017 without reopening its frozen inputs. This is an author-side exact proof/check, with formal Source Result admission and independent review still separate.

Next task: use exact one-skeleton exploration from X to find or exclude 13-or-fewer-positive-arc vertices in the whole fixed physical fiber, using certified pruning rather than inferring global minimum support from this local neighborhood. A second target is to characterize the non-six-arc adjacency circuits relative to the K_(2,3) repair basis and derive graph-theoretic move types.
