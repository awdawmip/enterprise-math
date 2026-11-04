# Independent paper review: input-indexed Borsuk coarsening

Reviewer: `EM-REVIEW-53C747`, agent `/root/research_inventory_1104`, direct TASK_RESEARCH; existing local reviewer identity, registration pending.
Author: `EM-C34-D16900`, agent `/root/research_cm_formal_1104`.
Date: 2026-11-04.

**Verdict: PASS — no unresolved defect found in the stated source-specific finite-family counterexample.** This is a nonauthor paper review of the frozen manuscript, not execution or unblocking of the formal GEO9 audit, a formal shared Review vote, or a change to a Borsuk bound.

The reviewed manuscript is `BORSUK_INPUT_INDEXED_COARSENING_COUNTEREXAMPLE.md`, SHA256 `79ec68199294aa3f638da0edf969dabc19bddf753f6522601bb7388d8eddbeb7`; its interface SHA256 is `402afdbe503a3059671a49307aa173c1dec99d0956ca79a13e8130cd3b93c7c0`. I verified both before review. The original bytes were not edited.

## Independence and sources

I share the parent/project source context and was exposed to the author's planned two-versus-seven construction in a message before receiving this review assignment. I supplied no construction, repair, manuscript edits, or mathematical confirmation before freeze. A broad source search during integration produced no input to the author's proof. This is a distinct noncontributing, nonblind review, not a clean-room or platform-attested independence claim. Root supplied routing and no mathematical vote.

I directly read the complete frozen paper/interface, the complete GEO8 return, the complete GEO7 return, and the GEO9 independent-audit Taskbook at `39556bf5207aa5ba559a27ec591c1bc1bf43b457`. The author separately records fresh remote blob comparisons in LATEST_SOURCE_READBACK.json. My companion binding records local hashes against the pinned Source; I do not relabel another agent's remote read as my own. The old inaccessible Lassak primary PDF has not been newly read by this review. No latest-literature or global-novelty certification is supplied.

The existing identity is reactivated only for this direct paper review. Prior integration/control access grants no mathematical authority, and no historical task-owner identity or CLAIM is adopted. No scientific program, old checker, point scan, BRC executable or formal GEO9 core was run. All calculations below are hand derivations in external Euclidean R6.

## 1. The exact GEO8 carrier and parameter endpoints

The constants and atom definitions match the full GEO8 source. With r²=3/7, ell=1/(2r)−r, one obtains 2r ell=1−2r²=1/7, ell²=1/84, and rho²=r²−ell²=5/12. The lens is the intersection of the two closed balls, as indicated by the source's boundary witnesses and nonstrict norm inequalities.

For every 0<delta<r, h=sqrt(r²−delta²/4) satisfies 0<h<r. Therefore c=r e6 lies strictly in the cap, including arbitrarily small positive delta. Every constructed sector point has strictly negative height and nonzero horizontal coordinates with its designated signs, so it is unaffected by all legal cap choices and boundary assignments. A horizontal orthonormal-frame change rotates points and sign sectors together; distances and all inequalities are preserved.

For any horizontal unit u, `a(u)=rho u−ell e6` has norm² rho²+ell²=r² and distance² to c equal to rho²+(r+ell)²=2r²+2r ell=1. Thus the cap-sector witnesses are actual points in this lens. The old individual-atom strict-diameter assertion is retained at its original scope, not reproved by a finite sample here.

## 2. Sector-pair rescaling is compatible with legal inputs

For different sign vectors sigma,tau choose a differing coordinate j. The designated horizontal vectors have squared norm `(9+4)/13=1` and inner product at most `(-9+4)/13=-5/13`. Thus their old lens boundary pair has squared distance at least

`2(5/12)(1+5/13)=15/13`.

Set d to its actual distance and t=1/d. Then 0<t<1 and t²<=13/15. The scaled points have mutual distance exactly one. Positive scaling preserves strict horizontal signs; their height is −t ell<h and their norm is tr<r. The second ball needs a separate check, which the author correctly supplies:

`|t a-c|²=r²(1+t²)+2tr ell <= (3/7)(1+13/15)+t/7 = 4/5+t/7 < 33/35 < 1`.

This last estimate applies to both points. Hence the three-point set consisting of c and the two scaled sector points is genuinely unit-diameter, inside the same lens, with exactly one diameter edge. This is not the invalid step of reusing the original distance-greater-than-one pair as a diameter-one input.

Its two nonempty parts may be chosen as c with one endpoint, and the other endpoint alone. The first part has diameter strictly below one; the singleton has diameter zero. Each restricted atom contains one point, so neither part splits any restricted atom. One part is impossible because the input diameter is exactly one. The cap-sector two-point inputs likewise require and admit exactly two parts.

There are exactly 32 cap-sector indices and C(32,2)=496 sector-sector indices, totaling528. Different pairs designate different occupied sector labels, and the choice of the first differing coordinate makes each indexed construction definite. In particular every member has exact adaptive coarsening cost2 without any enumeration assumption.

## 3. Graph sufficiency depends on the query

For one of these finite inputs, every pair distance is at most one, and individual atom restrictions have diameter below one. A coloring of the atom labels is legal precisely when no distance-one cross-atom pair is monochromatic. Finiteness matters: the maximum over finitely many strictly subunit pair distances is still strictly below one. This argument is not silently extended to an infinite set whose supremum might be one without being attained.

Thus per-input coarsening is exactly coloring its own G_K. A single label-coloring valid for every input is proper for the union of all those graphs, and conversely. The union operation is sufficient for this common-coloring query.

Every pair of atom labels has its own actual unit-diameter witness in F2, so the union is K33. A common coloring therefore needs33 colors, and33 are sufficient. Yet every per-input graph consists of one edge plus isolated labels and has chromatic number2. Unused atom labels can reuse colors and create no extra nonempty pieces. The manuscript keeps `min common coloring` distinct from `max_K min coloring for K`; it never infers one admissible input with chromatic number33 from the union graph.

## 4. Explicit seven-point simplex and full dimension

With s=sqrt(6/5) and a=(1−sqrt6)/(5sqrt5), the identities `s+5a=1/sqrt5` and `s²=6/5` imply

`2sa+5a²=((s+5a)²−s²)/5=-1/5`.

For the first five vectors v_i=s e_i+a 1, this gives v_i·v_j=−1/5 when i≠j and |v_i|²=s²−1/5=1. The sixth vector −1/sqrt5 has norm1 and inner product `−(s+5a)/sqrt5=-1/5` with each of them. The designated diagonal coordinate `(4sqrt6+1)/(5sqrt5)` is positive, all other coordinates a are negative, and v6 is entirely negative. Therefore all six lower points occupy distinct strict sign sectors; c supplies a seventh, cap label.

Each lower point is an unscaled a(v_i), so its norm is r and its distance to c is one. Two distinct lower points have squared distance

`2 rho²(1+1/5)=2(5/12)(6/5)=1`.

The seven points are also affinely independent in R6, not a degenerate equidistant claim: let y_i=a(v_i)−c. Their norms are one and their pairwise inner products are1/2, so their 6×6 Gram matrix is `(I+11^T)/2`. It has eigenvalues7/2 once and1/2 five times, hence rank6. This standard Gram check confirms the claimed regular simplex placement without a Euclidean realization shortcut.

Every two distinct simplex points are at distance one, so a strict-smaller-diameter part contains at most one. Seven singleton restrictions give a legal coarsening; its exact adaptive cost is7.

Adding this one input to F2 leaves the already complete union graph unchanged while changing the worst adaptive cost from2 to7. The common-coloring cost remains33. Padding F2 by a repeated input is explicitly an indexed-family construction: both then have529 indices, not529 distinct point sets. Its adaptive cost and union graph are unchanged. Thus the optional equal-index-count statement is correctly quantified.

## 5. Scope and disposition

The proof exhibits two concrete families in one and the same lens and atom system with identical aggregate graph but different adaptive query answers. The regular simplex, graph-coloring equivalence and GEO8 norm witnesses are standard or prior project input; the new local content is the compatible Euclidean family and its exact information-loss test. The statement does not require or claim a realization of arbitrary graphs in R6.

This does not contradict GEO8's whole-lens, fixed-template obstruction. It neither proves a universal adaptive scheme for all K nor changes b(6), and it does not prove that a more complicated single-input atom graph is impossible. A universal continuous coverage/diameter bridge remains a separate obligation. The source's dated 7<=b(6)<=33 summary is not upgraded to a newly searched literature status.

The read GEO9 Taskbook is blocked on an accepted construction Result and an independently bound verifier for its full continuous audit. This local proof does not claim those inputs, execute that blocked core, issue its immutable audit Result, or transfer its ownership. P000/native metric and Foundation status remain unchanged.

No mandatory correction was found. The verdict applies only to the exact paper/interface hashes above and their declared finite-family, fixed-atom query language. Bounded source dedup is not a proof of worldwide novelty. One counterexample unit is recorded; its two/three-point family, simplex supplement and quantifier consequence are not counted as separate discoveries.

Researcher-ID: EM-REVIEW-53C747 / TASK_RESEARCH

EM-Source-Status: Read=Verified snapshot reused (39556bf5207aa5ba559a27ec591c1bc1bf43b457; exact source hashes in REVIEW_BINDING.json); Write=⚠ Not written (local paper review preserved; Source publication pending).
