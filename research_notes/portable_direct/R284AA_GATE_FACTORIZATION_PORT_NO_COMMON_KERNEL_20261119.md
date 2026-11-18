# R284AA — Stable nonnegative Port witness with full matching, identically singular independent unit edits, and no fixed kernel

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASSED / NOT_REVIEWED**.
Lineage: R284Y (matching-minor and terminal Schur certificate) and R284Z (positive path-pair formula and planar rigidity). Maintains frozen scientific source pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. The present calculation is an **auxiliary exact rational named-Port observer** within the project's X6/Heartbeat interpretation. It is not a new native X6 primitive, a BRC–Shor trajectory, a native residual attribution, a formal Task CLAIM, or a peer Review.

## Main result: the open Port-sign/stability witness exists

Let `P=(p1,p2)`, `A=(a1,a2)`, `B=(b1,b2)`, `Q=(q1,q2)` be eight **distinct named ports**, `S=A union B`, and use the vertex order `P,A,B,Q`. Take `W` to have exactly the following possibly nonzero entries:

- `p_i -> a_i` of weight `g_i>0`; `a_i -> a_i` of weight `lambda_i>=0`;
- `a_i -> b_j` of weight `C_ij>0`, for all `i,j in {1,2}`;
- `b_j -> b_j` of weight `mu_j>=0`; `b_j -> q_j` of weight `h_j>0`;
- all other transitions vanish.

Assume all row sums of `W` are strictly below one. Write `L=diag(lambda1,lambda2)`, `U=diag(mu1,mu2)`, and `D_g=diag(g1,g2)`, `D_h=diag(h1,h2)`. For the ordered complementary matrix `A_Port=(I-W)[S,P; S,Q]`, with rows `(S,P)` and columns `(S,Q)`, define `G=I-W_SS` and `T=W_PQ+W_PS G^{-1} W_SQ` as in R284Z.

**Theorem AA1 (gate factorization and exact loop cancellation).** In this family,

`T = D_g (I-L)^(-1) C (I-U)^(-1) D_h`, and

`det A_Port = g1*g2*h1*h2 * det C`.

For an arbitrary number `k>=2` of input/output channels with the same layered pattern, `det A_Port=(-1)^k (product_i g_i h_i)*det C`; the rank of `A_Port` is `2k+rank C`. The internal self-loop parameters **cancel exactly from the complementary determinant**, although they survive in the transfer observations. All identities hold as exact rational functions on the strictly substochastic domain.

**Proof.** Order `S=(A,B)`. Then

`G = [[I-L, -C], [0, I-U]]`,

`G^(-1) = [[(I-L)^(-1), (I-L)^(-1) C (I-U)^(-1)], [0,(I-U)^(-1)]]`.

`W_PS=[D_g,0]`, `W_SQ=[0;D_h]`, `W_PQ=0`, so multiplication gives the displayed transfer. Since `G` is invertible, the block Schur identity yields `det A_Port=det G *det(-T)`. Each gate diagonal is invertible, `det G=det(I-L)det(I-U)`, and all loop denominators cancel, proving the formula. The same invertible block eliminations give `rank A_Port=2k+rank T=2k+rank C`. QED.

**Corollary AA2 (matching without a fixed kernel, for independently edited matrix units).** Choose `C` to be any positive, singular `2x2` matrix. Let **four independent named updates** change the four distinct physical edges `p1->a1`, `p2->a2`, `b1->q1`, and `b2->q2` by separate additive variables, each varying in a nontrivial open positive interval; leave the central `C`, internal loops and remaining edges fixed. Then, throughout the stable parameter box:

1. The bipartite support of `A_Port` admits a perfect matching, and both terminal permutations have strictly positive vertex-disjoint path routings.
2. `det A_Port` vanishes *identically* in all four independent unit-entry edit variables; the pointwise rank of `A_Port` is `5`.
3. `intersection_z ker A_Port(z)={0}` and `intersection_z ker A_Port(z)^T={0}`. In particular, there is **no shared nonzero constant left or right kernel**, despite each individual matrix being singular.

**Proof.** The routes `p1->a1->b1->q1` and `p2->a2->b2->q2` use distinct vertices and give the identity pairing; selecting `a1->b2` and `a2->b1` gives the swapped pairing. R284Z's support/routing correspondence therefore proves a support perfect matching. Because `det C=0`, AA1 gives the polynomial identity in the four independent gates. Since `C` is positive singular `2x2`, `rank C=1`, hence `rank A_Port=4+1=5`.

Write `T=D_g (I-L)^(-1) C (I-U)^(-1) D_h`. If a constant column vector `q` satisfied `T(z)q=0` for all independent `h1,h2` in an open box, take the difference of two parameter values that vary only `h_j`. Invertibility of the first two factors forces `C e_j*q_j=0`. Each column of positive `C` is nonzero; hence both `q_j=0`. Similarly independent changes to `g1,g2` and the nonzero rows of `C` force any common *left* kernel vector of `T` to vanish.

For the full complementary matrix `A_Port=[[G,-W_SQ],[-W_PS,0]]`, a fixed right-null vector `(s,q)` obeys `s=G^(-1) W_SQ q` and `Tq=0`; therefore `q=0` and `s=0`. A fixed left-null vector `(r,p)` obeys `r^T=p^T W_PS G^(-1)` and `p^T T=0`; therefore `p=0` and `r=0`. This rules out any constant full-matrix kernel. QED.

**Structural generalization AA3.** For `k>=2`, any singular central `k x k` matrix `C` with no zero row or column, and independent strictly-positive gate variations in every `g_i,h_j`, satisfies the same no-common-kernel conclusion. Full positive support `C_ij>0` guarantees support perfect matching. Taking `C` to be the positive all-ones matrix times a sufficiently small rational yields `rank A_Port=2k+1` and determinant identically zero; all `k!` terminal matchings survive. The proof of the kernel intersection uses coordinatewise differences of `h` and `g` exactly as above; it does **not** assume a fixed null vector of a pointwise singular family.

## Explicit eight-Port rational witness, including feedback self-loops

Use vertices `P=(0,1)`, `A=(2,3)`, `B=(4,5)`, `Q=(6,7)`. Let

`C = [[1/16,1/16],[1/16,1/16]]`,

`(lambda1,lambda2,mu1,mu2)=(1/16,1/32,1/24,1/20)`,

`g1=1/8+x`, `g2=1/8+y`, `h1=1/8+u`, `h2=1/8+v`,

with four **independent** `0<=x,y,u,v<=1/16`. Each variable adds its own named unit transition `E_(0,2), E_(1,3), E_(4,6), E_(5,7)`. Each row sum is `<1`; `W` is nonnegative with internal cycles (self-loops) and full `I-W` invertible. In the order `S=(2,3,4,5)`, `P=(0,1)`, `Q=(6,7)`,

`T_ij = (g_i/(1-lambda_i)) * (1/16) * (h_j/(1-mu_j))`.

Thus both positively weighted route-pairing classes contribute the same exact product `g1*g2*h1*h2/256` (each routing uses all four internal vertices, so its residual principal determinant is one). Their signed difference is zero, **even though both pairings have support** and no constant null vector exists. This resolves the outstanding R284Y/R284Z existential Port-witness question *for this precisely defined auxiliary class*.

**Observer-numerator realization.** With `M=I-W`, choose `F_(0,6)=(M^(-1))_(0,6)` and a fifth independent target-edge perturbation `s:E_(7,1)` in `W`. For the cofactor numerator `N_(0,6)=(-1)^(0+6)det M[V\{6},V\{0}]`, the coefficient of `s` is `-det M[V\{6,7},V\{0,1}]=-det A_Port=0`. The row reordering from `(0,1,S)` to `(S,0,1)` has even parity. For sufficiently small nonnegative `s`, the full model remains strictly substochastic. **This is a vanishing numerator coefficient, not a claim that the complete rational observer `F_(0,6)` is independent of `s`: its denominator may depend on `s`.**

**Sharp edit boundary.** If an additional independent edit `eta:E_(2,4)` changes only `C_11` from `1/16` to `1/16+eta`, then

`det C(eta)=eta/16`, and `det A_Port(eta)=g1*g2*h1*h2*eta/16`.

For every positive `eta`, the complementary determinant becomes strictly positive; this reveals exactly why the identity is stable under *gate edits* but generally not under unrestricted *core mixing edits*. It also distinguishes a genuine signed pairing cancellation from loss of path support.

## Exact checks, verification boundary and reproducibility

Program: `research_notes/portable_direct/R284AA_separable_port_kernel_checker.py`; JSON: `research_notes/portable_direct/R284AA_exact_verification.json`. Python standard-library `Fraction`, exact elimination/rank, direct support-permutation enumeration and two-point independent-kernel tests. The actual program evaluates:

- 81 grid instances `(0,1/64,1/16)^4`, each checking strict substochasticity, perfect matching, rank `5`, zero `6x6` complementary determinant, rank-one and zero determinant of the independently written `2x2` transfer formula;
- 16 distinct binary corners `(0,1/16)^4` for the multiaffine polynomial;
- 16 mixing-perturbation corners `(0,1/64)^4` at `eta=1/32`, checking the **nonzero** determinant, closed form and rank `6`; at zero gates edits the exact determinant is `1/2097152`;
- two stacked matrices for both left/right shared-kernel tests, each of full column rank `6`;
- 16 instances comparing the observation cofactor numerator at `s=0` and `s=1/32`, each equal exactly.

All checks PASS. Finite checks do not promote the mathematical result to an independent Review, native world correspondence or BRC time-evolution finding. The algebraic proof covers all positive gates/loops and core matrices under the stated nonnegative stability conditions; no error-tolerance or floating-point assumption is used.

## Consequence, cost, and next unresolved unit

AA1 turns a potentially exponential edit-matching enumeration in four gate variables into one central `det C=0` test after confirming the named layered graph. For an `k x k` core, exact rational elimination costs `O(k^3)` field operations after the graph/edge-type certification; gate values and loops do not need sampled. This is not a universal polynomial-time recognition algorithm for arbitrary Port graphs, and rational bit-complexity depends on numerator/denominator growth.

The important distinction is **structural rank (perfect matching) versus algebraic rank (cancellation of routing weights), with parameter-varying kernels**. The positive transfer matrix is rank deficient although the support allows all pairings; collapsing named paths to a single scalar too early would obscure the cancellation mechanism and its edit boundary. Named branches, gates and loops remain recorded.

Next: characterize the broadest independently editable Port subgraphs that preserve a determinantal identity when the internal `C` has nontrivial feedback coupling (not merely independent self-loops); test whether a small separator factorization or signed disjoint-routing involution provides an exact, low-bit-cost certificate, and prove its valid observer/future-operation scope. A separate optional line is minimal internal-vertex count for no-common-kernel witnesses subject to all four independently editable gate edges; **no minimality claim is made here**.
