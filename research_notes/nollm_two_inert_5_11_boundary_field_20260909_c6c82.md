# Two inert directions: 5/11 residue field, boundary compatibility, and shape cost

Status: RESEARCH_NOTE / DERIVATIONS_AND_EXACT_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-TWO-INERT-511-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local key, not an authenticated server ID)
Mode: TASK_RESEARCH / direct user continuation / no formal Task-ID or CLAIM
Date: 2026-09-09
Source snapshot: enterprise-math@d40aa672623d6fc82af4cbb60964e6a628267e62
Parent: research_notes/nollm_split_prime_boundary_extension_20260909_c6c82.md at 1772bdf67e9ace59823a47a096401d69e83c4390
Frozen executable dependency: experiments/nollm_split_prime_extension_20260909_c6c82.py at b8c099329b1949becf544599e86fcf32045ccebc
Dependency SHA256: 0efac96492fcfa12980ef2c1e9ea80b22b4936a5401dd31d01b7fe6a9c10bda6
New executable: experiments/nollm_two_inert_511_20260909_c6c82.py

## 1. Scope and recovery

The five existing activity checkpoints are retained. The exact new question is whether a second inert-prime direction, 11, can coexist with 5 and the split-prime directions while retaining nearest quotient representatives, future refinement stability, lattice-convex sections, and finite local candidate sets.

This is ordinary rank-two lattice mathematics with Q(q,r)=q^2+qr+r^2, used as a comparison/research slice. It does not modify P000, Nollm physical layers, or runtime architecture. Quotient capacity multiplication is NOT an intrinsic planar implementation of ordinary integer-label multiplication. No mathematical acceptance is created by this note.

## 2. Two exact inert chains and their intersection

Let W=[[0,-1],[1,1]], A5=[[2,-1],[1,2]], A11=[[3,-1],[2,3]]. The determinants of A5 and A11 are 5 and 11. For each p in {5,11}, choose Bp=adj(Ap)W, so Ap Bp=pW. In particular B11=[[1,-2],[3,5]].

Define Lp_(2t)=p^t Z^2 and Lp_(2t+1)=p^t W^t Ap Z^2. These are the same nested two-phase chains expressed as lattices: W is unimodular, so the even-stage W^t factor can be omitted without changing the lattice. Consecutive indices are p.

Keep G7=[[1,-2],[2,3]], G13=[[1,-3],[3,4]], G19=[[2,-3],[3,5]]. All are commuting integral hex similarities, with Q(Gp x)=p Q(x).

For exponents (a,c,b,d,e), in the order (5,11,7,13,19), write t=floor(a/2), u=floor(c/2), epsilon=a mod 2, eta=c mod 2, and U=G7^b G13^d G19^e. Define L as the intersection of the five prime-power component lattices. Coprime lattice CRT gives index 5^a 11^c 7^b 13^d 19^e and path-independent quotient projections. A 5/11 interchange acts by a permutation of local digit ranks; identical rank words are not asserted to commute.

After removing the common similarity T=5^t 11^u U, the remaining lattice H is described by at most two modular line constraints:

- when epsilon=1, x mod 5 lies on U^(-1)W^t im(A5);
- when eta=1, x mod 11 lies on U^(-1)W^u im(A11).

Only projective lines matter, so scalar inverses do not change these constraints. The lines of A5 and A11 have slopes 3 mod 5 and 8 mod 11. Write infinity for the vertical line.

For two finite slopes l mod 5 and k mod 11, a basis is [[1,0],[s,55]], where s=l+5*(9*(k-l) mod 11). When one or both lines are vertical, use [[5,0],[(5k mod 11),11]], [[11,0],[(11l mod 5),5]], or [[55,0],[0,1]]. Single active constraints give the analogous determinant-5 or determinant-11 bases. The executable performs exact integer Gauss reduction, preserving the lattice and choosing positive orientation.

Thus P=T H is an exact basis for L. Containment in all component lattices and equality of product indices also independently prove the intersection formula.

## 3. Finite atlas, but more state than with one inert prime

There are 6 lines over F5 and 12 over F11. The normalized atlas contains

1 + 6 + 12 + 6*12 = 91

DISTINCT NORMALIZED SUBLATTICES. This is not a claim of 91 inequivalent Euclidean similarity classes or a minimal automaton. The full finite phase description retains the two parity bits and both line positions, including an inactive line that is needed at a future odd step: 4*6*12=288 possible states.

The inverse G7 action on the selected F11 line cycles through
8,9,4,infinity,6,1,2,0,3,5,7,10.
Its F5 cycle is the predecessor's six-cycle. Breadth-first exact modular computation with G7,G13,G19 reaches all 72 pairs of active lines. Thus treating the two active directions as a single six-state phase would lose reachable future distinctions.

Normalized transitions are especially simple. Opening a 5 phase inserts its current line with E=I. Closing that phase uses E=5I, removes its constraint, and rotates its stored line by W for the next cycle. The 11 transitions are analogous. A split step uses E=Gell and applies E^(-1) to both line positions. In every case C=E H_next is contained in H_parent and [H_parent:C]=ell. Right transition matrices telescope around every refinement square. This proves abstract order consistency before any geometric section is chosen.

## 4. Boundary constraints become a finite compatibility problem

Reuse the predecessor's selector type. For an integer anchor v, let D_v(x)=2<v,x>_hex and C_v(x)=det(v,x). On a nonregular section compare

(Q(x), -D_v(x)C_v(x), D_v(x)^2)

lexicographically. On a regular section retain the positive-chirality half of every tied Voronoi facet.

On a facet normal w the sign of the secondary comparison is governed by

A(v,w)=D_v(w)^2-3C_v(w)^2.

Crucially, A need not be positive on EVERY shared facet. Parent and child need the SAME nonzero sign on the particular facet that survives. Insisting that all signs be positive is unnecessarily restrictive.

Build a node for each normalized lattice and unoriented relevant facet pair. Identify nodes connected by a shared-facet transition. Similarities preserve the chiral sign, so a component needs one common sign. Components containing regular-section facets have sign +1; other components can choose either sign.

With the 15 split-prime exceptional matrices specified below plus the 5/11 transitions, the exact graph has 81 components, of which three contain regular-facet constraints. A small exact backtracking search over integer anchor directions finds a simultaneous assignment. The search enumerates anchors in [-15,15]^2 and performs Boolean sign propagation; it is not floating-point optimization. The resulting anchors have squared norms among {1,3,7,39,97}. This is a found feasible witness, not a minimum-cost or uniqueness claim.

The executable RECHECKS the found table by integer arithmetic in all 288*17=4896 phase/prime cases. For each actual shared normal w, the parent sign and the transformed-child-anchor sign have strictly positive product. No guessed tolerance or coarse norm observer replaces this check.

## 5. Why the same guarantees follow at every scale

The predecessor's proofs apply to the NEW feasible table:

1. Each coset has a shortest Q representative. The identity D_v(x)^2+3C_v(x)^2=4Q(v)Q(x) shows equal three-term keys determine x up to sign. An odd-index quotient cannot have distinct antipodes among shortest representatives of a single class, so selection is unique.
2. Each comparison with x-lattice_vector subtracts quadratic forms to give affine expressions. The lexicographic cone is convex. Intersecting these comparison regions proves S=conv(S) intersect Z^2 for nonregular sections. Every section is centrally symmetric and has exact centroid zero.
3. Regular sections have the predecessor's contiguous half-facet rule, no integer regular Voronoi vertices or facet midpoints because the similarity index is coprime to 6, and exact C6 symmetry. They also have no omitted convex-hull lattice sites.
4. A shortest parent representative remains shortest in the child because the child competitor lattice is smaller. Only co-nearest translations that survive require agreement. These lie in the shared relevant facet sets; all normalized lattices here have strict hexagonal, not rectangular, Voronoi cells. The finite sign certificate supplies the required agreement. Therefore S_parent is contained in S_child along every allowed prime direction.
5. Consequently every parent has exactly p children, no two parents collide, both orders around a coprime square reach the same representatives, and old addresses are stable UNDER FUTURE REFINEMENT IN THIS NEW CONVENTION.

These are elementary derivations plus finite exact certificates, not formalized or accepted EM theorems. New anchors can migrate predecessor boundary representatives; no zero-movement migration from every earlier address map is claimed.

A negative control makes the need for coordination concrete. For base slopes (0 mod 5, 2 mod 11) and scalar 5, the lattice basis is [[-15,-55],[25,0]], index 1375. Applying positive chirality blindly to every tied facet selects only 1373 representatives. The repaired quadratic selector, with anchor (-15,10), supplies all 1375; its representatives (-23,-9) and (23,9) belong to the two missing classes. This is a counterexample to that naive rule, not a no-go for all selectors.

## 6. The exceptional-prime set stays finite, but becomes larger

The complete squared-norm support of relevant facets of the 91 normalized sublattices is

{1,3,7,13,19,21,25,31,37,39,43,49,57,61,67,73,75,79,91,93,97,103,109,111,121,129,175,183,325,327,757,2269}.

A shared facet under a norm-ell similarity satisfies w=E z and Q(w)=ell Q(z). Therefore a split prime introducing a new shared-facet comparison must divide this finite support. The complete candidate support is

{7,13,19,31,37,43,61,67,73,79,97,103,109,757,2269}.

For 7,13,19 retain the predecessor generators. For each other listed prime the code chooses the lexicographically first nonnegative solution (a,b) of a^2+ab+b^2=ell and E=[[a,-b],[b,a+b]]. All fifteen actually have a shared-facet case for these chosen directions, and all are covered by the found anchor table. Different associates or conjugates of these exceptional directions require a new compatibility check.

For any other split prime, no shared facet exists in this atlas, so no new boundary sign constraints arise. Thus the argument extends to any finite collection of split primes with these exceptional choices fixed and an integral norm-prime similarity supplied for each additional prime. The code explicitly materializes full sections only for 5,11,7,13,19; the larger split-family statement is the finite-support/sign-certificate derivation, not a claim to have enumerated infinitely many objects.

## 7. Local candidate counts and physical cost

Reuse the exact predecessor Voronoi/Minkowski polygon compiler for H_parent^(-1)(V(E H_child)-V(H_parent)), but enumerate its WHOLE rational bounding box. The old radius cutoff for 5/7 is not reused.

Across all normalized transitions for the five active primes, exact candidate maxima are:

5:17; 11:29; 7:19; 13:31; 19:43.

Exactly p candidates survive. There are 597 distinct normalized geometric edge types after duplicate inactive-line states are removed. The finite polygon certificates prove these per-prime bounds independent of depth for this atlas. They do not bound integer bit complexity or finest-grid movement. Physical fanout <=7 for 11/13/19 has not been implemented.

## 8. A new obstruction to uniform roundness: reachable unit-thin 55 lattices

Among the 72 doubly active normalized lattices, three contain a native unit vector. The horizontal example is Z*(1,0)+Z*(0,55). For any integer basis C of this lattice, a nonzero integer vector maps to the unit vector, so its smallest Euclidean singular value is at most 1. With determinant 55, its singular-value ratio is at least 55.

The lower bound is attained by [[1,-27],[0,55]]: in the hex Euclidean basis it is diag(1,55). This is a statement about the best possible LINEAR BASIS MAP, not the cloud covariance. The canonical 55-point section has numerical standard-deviation axis ratio about 49.59593; at scalar 5 its 1375-point section has ratio about 47.69387. Both are hole-free and centrally symmetric.

This bad shape is reachable, not an unused atlas corner. Starting with both initial odd chains, split steps 7,7,13,19,19 take the pair of normalized lines to (0,0). The actual index is 12,647,635. Its normalized shape and exact matrix were computed; that whole large point cloud was NOT enumerated.

Therefore compatible refinement, lattice-convexity and stable addresses do not ensure uniformly ROUND shapes. Adding inert directions can multiply aspect costs: in a family containing a common unit direction for all active inert constraints, index is the product of those primes, giving the corresponding basis-ratio lower bound. This does not prove such a bad state is reachable for every possible future generator family, nor that all memory-field constructions must suffer it.

The cardinality test is only necessary: 55=1 mod 6 removes the previous count obstruction, but the constructed 55-point section is not C6-symmetric. Completing both inert pairs gives regular sections and restores exact C6.

## 9. Executed finite checks

- 4896 exact normalized sign/integrality cases, including the fifteen exceptional split directions.
- All 91 normalized lattices at scalar 1 and scalar 5: 182 complete sections, 107198 point appearances.
- All 597 distinct active-prime normalized edges: 21621 complete parents, exact degree, residue uniqueness, future stability and hole-free child sections.
- 84 actual exponent sections: 1352566 point appearances, largest 275275. Every section has central symmetry and zero convex-hull lattice holes; all regular sections have exact C6 and integer covariance identities.
- 122 additional full actual-chain edges with 27728 parents.
- 108 complete permutation runs: all six orders for the triples (5,11,7) and (5,11,13), and all 24 orders for (5,11,7,13), from three starting sections. Endpoints and parent fibers agree exactly; zero order mismatches.
- Exact BFS reaches all 72 line pairs; the three unit-thin shapes and the explicit route are checked.
- The separate naive-chiral negative control has 1373 versus 1375 distinct classes; the repaired rule restores both.

Point appearances across different sections and routes are not independent memories. Numerical axis ratios are readouts, not acceptance tests.

Example actual chain (index; cloud axis ratio): 5;1.73205 -> 55;1.12786 -> 385;1.58747 -> 5005;3.67185 -> 25025;1.36735 -> 275275;1 exactly. The final index is 5^2*11^2*7*13.

## 10. BRC resolution and remaining research unit

REUSE_EXECUTED: hash-pinned predecessor quotient geometry, exact Gauss/Voronoi arithmetic, quadratic comparison, rational Minkowski compiler and integer hull observer. EXTEND_EXISTING_TOOL: task-local two-line CRT adapter and finite sign-compatibility solver, not a new global family. COMPOSE_APPLIED: retain both projective lines, two parity bits, full similarity, quotient identity and local digit provenance. Connected components compress ONLY surviving boundary comparisons; they do not identify memory content, collapse path multiplicity, or certify geometric roundness.

This closes a two-inert-direction compatibility construction within the declared slice. It does not close the original problem of ordinary multiplication intrinsic to a planar address field. The next substantive question should confront the roundness/state-cost tradeoff: can a different 11-chain or an adaptive retained phase avoid the reachable unit-thin states while preserving quotient consistency, rather than merely adding a third inert prime and another larger table?

Classical context: CRT and ideal-lattice constructions are established; compare Li, Gan and Ling, Coprime Sensing via Chinese Remaindering over Quadratic Fields, Parts I and II, arXiv:1808.07505 and 1808.07511. These do not automatically prove the nonideal 5/11 selector. The claimed project contribution is the explicit finite compatibility certificate, its extension boundary, and the demonstrated shape-cost obstruction, with no priority claim for CRT, Voronoi theory or finite-field projective lines.
