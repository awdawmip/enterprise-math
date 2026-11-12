# R106 — Persistent guard-incidence certificates and exact weighted resilience

Date: 2026-11-13 (Asia/Shanghai). Independent author-side continuation of R105 at commit e8c8b17f09b95a8abc603a1226fba8890756063a. Scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Exact model

We retain the finite rational directed circular-source model, not unbridged native X6 dynamics. A source has its complete identity u=(t,branch) with integer coordinates and descending lexicographic rank. Fix sigma=(j,x,a,b) with integer j,a,b and rational x. For real theta, set s_u={x+(t-j)theta}, A={a theta}, B={b theta}. Eligibility M_u(theta) holds when s_u belongs to the directed half-open arc [A,B) around the circle, and is false when A=B. The first k eligible identities of S form Top_k(S,theta).

Let F,G be finite versions, C=F∩G their common sources and Delta=F△G their discrepancies. Let k>=1, and I=[L,U] be a closed rational interval. Using R105's six rational affine-phase integer-crossing families for F∪G, partition I into singleton rational cutpoints and open gaps J. On each J every source's eligibility is constant. Choose its rational representative theta_J (the point itself, or the rational midpoint). For each u∈Delta and atom J with M_u(theta_J) true, define the complete guard incidence fiber

S(u,J) = {v∈C : v>u and M_v(theta_J)}.

For an inactive u, store OUT. Full branch identity is preserved.

## R106.1 — Exact common-deletion margin theorem

Consider any common-deletion set D⊆C, applied to both versions: F_D=F\D and G_D=G\D. Then

Top_k(F_D,theta)=Top_k(G_D,theta) for all real theta∈I

if and only if

for every u∈Delta and every atom J with M_u(theta_J), |S(u,J)\D| >= k.        (1)

If (1) fails, theta_J is an exact rational witness to different Top-k lists.

Proof. Removing the same common identities from both versions preserves Delta, while the new common set is C\D. Eligibility of each identity depends only on its own identity, sigma and theta. The exact R104 pointwise rank-shield criterion says that a discrepancy can be absent from both Top-k lists precisely when it is OUT or k higher eligible common identities remain. On J the higher eligible common identities are exactly S(u,J)\D. All memberships are constant on J; singleton endpoints are separate atoms. Hence (1) holds exactly when the Top-k lists agree throughout I. A failed atom has a rational representative at which they differ. QED.

An immediate corollary: deleting a common source that does not occur in any guard incidence fiber cannot change the truth of the two versions' Top-k equivalence, even if the Top-k lists themselves change identically.

## R106.2 — Persistent certificate DAG

Let N=|Delta| times the number of atoms, m=|C|, and B=sum of sizes of all active guard fibers. Create a balanced immutable binary margin tree, with one leaf per (u,J). An active leaf contains |S(u,J)|; an OUT leaf is treated as +infinity. Internal nodes store descendant minima. A second immutable binary tree stores which common identities remain available. Retain a reverse-incidence index from each v∈C to precisely those leaves where v is a guard. Each version holds pointers to these two roots, its parent version and its latest deletion.

Deleting an available v changes only the guard-count leaves in v's reverse-incidence list, decrementing each by one, and the single availability flag of v. Path copying yields new roots with all untouched subtrees shared; any older version can become the parent of a separate branch.

By induction on historical deletions, each active leaf represents the exact remaining guard count. The root minimum is at least k exactly when the versions have equal Top-k throughout I, by R106.1. Descending to a leaf below k takes O(log(N+1)) structural node visits and retrieves a rational witness.

For r_v affected leaves, the number of newly allocated margin-tree nodes is at most (r_v+1)(ceil(log2 N)+1) for N>=1; the availability tree adds at most ceil(log2 m)+1 nodes for m>=1. A multi-point copy can share prefixes and allocate fewer nodes. A zero-incidence deletion leaves the exact margin-root object unchanged. With V retained versions, structural memory is O(N+m+B+sum_edits(1+r_v)log(N+m+1)), excluding storage of rational cutpoints, source identities and source inputs.

The structural bound counts tree nodes, not CPU bit operations. Initial exact rational phase roots, sorting, indexing and eligibility evaluation remain real costs. Afterwards, the margin updates use integers of bit length O(log(m+1)); recovering a full direct witness comparison may scan source identities. If r_v=Omega(N), there is no general sublinear-update claim.

This implementation is a working persistent DAG for fixed sigma,k,I, the exact original atomic partition, and common-source deletions. An insertion or edit changing Delta can introduce new cuts and requires local splitting and newly certified fibers; a general split/join update remains an open engineering unit.

## R106.3 — Exact minimum-cost deletion to destroy equivalence

Assume the current versions are equal, and assign each currently available common identity a nonnegative rational deletion cost w(v). At every active (u,J), let H=S(u,J)\D, h=|H|, and q=h-k+1 (which is positive under the equality assumption). Define W(u,J) as the sum of the q smallest costs among identities in H.

Then the minimum possible cost of further deleting the same common identities from both versions so that their Top-k functions differ somewhere on I is

R = min_active_(u,J) W(u,J).

Set R=+infinity if there are no active discrepancy atoms; a version already unequal has further failure cost zero.

Proof. If any further deletion T creates inequality, R106.1 forces at least q guards in some H(u,J) to be removed. Nonnegative costs imply cost(T)>=W(u,J)>=R. Conversely delete the q cheapest guards at an atom attaining R. Only k-1 guards remain there; its rational representative certifies inequality, at cost R. If no discrepancy is ever eligible, deleting common sources cannot create a discrepancy. QED.

This gives the exact adversarial edit budget for all future common-deletion choices, including weighted, zero-cost, and branching histories. It improves the fixed local edit-slack bound in R105 to a global optimum for the declared observer and edit class.

Example: sigma=(0,1/4,0,1), I=[1/2,2/3], k=2, discrepancy u=(0,0), and common guards (0,10),(0,11),(0,12),(0,13), with rational weights 2,3,5,7 respectively. All four are always eligible and higher than u. The minimum failure cost is 2+3+5=10, realized by deleting the first three; theta=1/2 is an exact mismatch witness.

## Executable verification

The complete deterministic Python program is stored as check_r106.py.gz.b64, a gzip-compressed UTF-8 source file encoded as base64; decode with standard Python gzip and base64. It uses fractions.Fraction for membership, all cutpoints, atoms, weights and witnesses. It constructs immutable segment trees, branches history versions, checks each version against direct complete source scans at every rational atom representative, and exhaustively enumerates all further common-deletion subsets in small weighted test universes.

Recorded deterministic output:

    R106_PASS 327 9201 306 21 400 1636

That means 327 branched version updates, 9,201 atomic direct comparisons, 306 still-equivalent versions, 21 witnessed differences, 400 fully exhaustive weighted-budget comparisons, and 1,636 immutable structural node copies. Of the 327 deletions, 296 touched no discrepancy-guard incidence; 268 incidence updates occurred in total. Verification data are in verification_r106.json. The finite experiments are implementation tests; universal results are proved above.

## Frontier

R106 is author-side mathematical work; an exact RS-S23-AV task query on 2026-11-13 returned NO_CURRENT_IMMUTABLE_PUBLICATION, so no shared CLAIM/Result or independent review is asserted. The frozen scientific input remains unchanged.

R107: implement persistent interval-atom split/merge for additions or edits changing Delta, with source cutpoint refinement, exact endpoint ownership, version memory and bit-cost accounting; compare its total cost against the R103 net-overlay, and full function materialization on benign/adversarial histories. Investigate maintaining weighted resilience summaries under restricted edits without rescanning every incidence fiber.
