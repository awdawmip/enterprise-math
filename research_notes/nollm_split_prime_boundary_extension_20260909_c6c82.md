# Split-prime boundary extension: 5/7/13/19 and a finite collision spectrum

Status: RESEARCH_NOTE / DERIVATIONS_AND_EXACT_FINITE_CHECKS / NOT_PROMOTED
Progress-Event-ID: NOLLM-SPLIT-EXTENSION-20260909-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local key, not a server ID)
Mode: TASK_RESEARCH / direct user continuation / no formal Task-ID or CLAIM
Date: 2026-09-09
Source snapshot: enterprise-math@e9f7310b192a07431ccc15597afdfd2c6091113d
Parent: research_notes/nollm_mixed57_boundary_compatible_selector_20260909_c6c82.md at 052dee375c2875b9e36119280be4f48115337978
Parent code: experiments/nollm_mixed57_boundary_repair_20260909_c6c82.py at 1069515fcb70c38e55cbf84dd317accabd897477
Parent code SHA256: fced7c21cc5fdd597381094531454e5b5d37711cd514b64c79b02989ced205fa
Executable: experiments/nollm_split_prime_extension_20260909_c6c82.py

## 1. Scope and recovered frontier

The parent's four published activity checkpoints are retained. This continues its six-shape coprime quotient field; it does not replay or replace the earlier source. All geometry is ordinary rank-two integer lattice mathematics with Q(q,r)=q^2+qr+r^2, a comparison/research slice, not a modification of P000 or the Nollm physical architecture. Index multiplication and commuting quotient refinement are not ordinary scalar-label multiplication in the plane.

There are two distinct results. Adding 13 needs no change to the previous anchors. Adding the chosen 19 direction exposes an exact failure of the old anchors; three anchors are then changed. The corrected four-prime convention preserves its own future addresses, not every old boundary address during migration.

## 2. Additional similarities and the same six states

Reuse W=[[0,-1],[1,1]], G7=[[1,-2],[2,3]], and the six determinant-5 bases H_j from the parent. Put

G13=[[1,-3],[3,4]], G19=[[2,-3],[3,5]].

Their determinants are 13 and 19. Each is an Eisenstein similarity, so Q(Gp x)=p Q(x). These similarities commute with one another and with W.

On the six projective lines over F_5, inverse G7 shifts the parent's line index by 1, inverse G13 by 3, and inverse G19 by 2. The exact modular checks are

G13 = 3 G7^3 (mod 5), G19 = 4 G7^2 (mod 5).

For exponents a,b,c,d of 5,7,13,19 write a=2t+epsilon and

j=b+3c+2d (mod 6), U=G7^b G13^c G19^d.

Then an exact basis for the intersection of the four prime-power sublattices is

P(a,b,c,d)=5^t W^t U H_j^epsilon.

Its index is 5^a 7^b 13^c 19^d. Containment in each component and coprime indices prove the intersection identity. Every refinement has the expected prime degree; transition matrices P(s)^(-1)P(s+e_p) are integer. Products around every square agree because both telescope to the same final basis. CRT gives the corresponding canonical quotient identity, not an assertion that unchanged local digit ranks commute.

The residue/shape phase is still six-valued. This does not erase the separate exponent vector, physical similarity, or quotient residue.

## 3. 13 is compatible; the old 19 selector fails at an explicit point

No facet normal is shared between H_j and G13 H_(j+3), for any j. Likewise the regular even-section parent has no facet shared with its 13-successor. Therefore the old 5/7 anchors extend to 13 without new boundary constraints.

This statement is false for 19. For j=1,3,5 the following respective facet pairs survive:

+/- (2,3), +/- (3,-5), +/- (5,-2), all of norm 19.

The old anchor convention has an actual address failure, not just a potential sign conflict. At s=(a,b,c,d)=(5,1,0,0), x=(121,39) is selected by the old rule. It is not selected after one 19-refinement. The equal-distance competitor is y=(-104,-61), with

Q(x)=Q(y)=20881, x-y=(225,100).

The old source secondary/tertiary keys are x:(9646875,765625), y:(37975000,12250000), so x wins. At the successor they are x:(276390625,6909765625), y:(-276390625,6909765625), so y wins. Negation gives the second lost address. Smaller sections can miss this failure because the short shared facets initially contain no applicable integer boundary points.

This is a falsifier of the OLD SELECTOR, not a no-go theorem for adding 19.

## 4. Repair by three anchor changes

Retain the parent's odd-section lexicographic quadratic key

(Q(x), -d_u(x)c_u(x), d_u(x)^2),

d_u(x)=2<u,x>_hex, c_u(x)=det(u,x),

and the even-section positive-chirality boundary convention. Replace the six normalized anchors by

u0=(-3,1), u1=(-1,3), u2=(-1,-2),
u3=(-3,2), u4=(-2,3), u5=(-2,-1).

Only u1,u3,u5 changed; all six now have norm 7. The actual odd-section anchor is 5^t W^t U u_j.

For a facet with normal v, the sign of the secondary-key difference on that facet is controlled by

A(u,v)=d_u(v)^2-3c_u(v)^2.

More precisely on d_v(x)=Q(v),

[-d_u(x-v)c_u(x-v)]-[-d_u(x)c_u(x)]
= A(u,v)c_v(x)/(2Q(v)).

Thus A(u,v)>0 gives the same chiral side choice as the even rule. At j=1, the new u=(-1,3) gives A=4 on the shared unit normal (-1,1), and A=46 on the outgoing 19 normal (2,3); both are positive. The other two elongated states have the same margins after the corresponding rotations. The old anchor had A=-66 on that 19 normal. Exact rational geometry checks all 48 phase/prime transitions, including the transformed child anchors; all retained shared comparisons now agree.

The parent's uniqueness proof still applies: d_u(x)^2+3c_u(x)^2=4Q(u)Q(x); equal key values determine x up to sign, and odd quotient order excludes distinct antipodes in the same shortest coset. The affine differences of quadratic comparisons give lattice-convex odd sections. Even sections retain the regular-hex chiral proof. Therefore all sections have one representative per coset, central symmetry, no missing integer sites in their convex hull, and C6 symmetry when a is even. Every selected point remains selected under subsequent refinement in ANY of the four directions. Odd bulk anisotropy remains.

The new convention replaces the source representative x by y already at the parent in the witness above. It is not a no-movement migration from the old convention.

## 5. The possible boundary-collision primes are finite

The squared norms of ALL facet-relevant vectors of I,H0,...,H5 form exactly

{1,3,7,19}.

Let E be any integral hex similarity with prime determinant ell. If v is a shared facet normal of H_i and E H_j, then v=Ew for a relevant child normal w and

Q(v)=ell Q(w).

Since Q(w) is a positive integer, ell divides one of 1,3,7,19. Among split primes ell=1 (mod 3), only 7 and 19 can occur. In particular 13 and EVERY split prime greater than 19 create no additional shared-facet comparisons in this six-shape family.

This is an all-prime exclusion argument, not an extrapolation from checking many primes. Its scope is crucial: these fixed six shapes and integral similarity additions, not arbitrary lattice families.

Consequently the repaired selector extends to any finite collection of distinct split primes: use the fixed representatives 1+2 omega for 7 and 2+3 omega for 19 when present; choose one norm-ell Eisenstein generator for each other split prime. Keep the existing 5-chain as the only inert-prime direction. The standard norm-prime representation for split primes is classical. Alternatively the statement may be read conditionally on supplying the chosen integral similarities.

The six-state assertion follows without a growing atlas: modulo 5, every such E is invertible and commutes with G7. Since G7 acts as a six-cycle on the six lines, every commuting permutation is a power of that cycle. Define s(E) by this power and retain j=sum e_ell s(E_ell) mod 6. Indices/exponents and Euclidean rotation still remain separate state. Including a second inert prime is not covered. Changing the specified 7 or 19 generator to another associate/conjugate requires rechecking those exceptional comparisons.

## 6. Candidate complexity increases; no false fanout claim

Reuse the prior rational Voronoi/Minkowski polygon compiler, but NOT its old radius<6 enumeration cutoff. For the new prime, enumerate all integer vectors in the exact rational polygon bounding box, then keep the vectors inside. This yields a complete stencil independently of a guessed radius.

Maximum candidate counts over the six shapes and two parities:

prime 5: 17 candidates, 5 children;
prime 7: 19 candidates, 7 children;
prime 13: 27 candidates, 13 children;
prime 19: 43 candidates, 19 children.

The tables are independent of depth for a fixed prime. There cannot be a constant materialized fanout independent of the prime, since the quotient fiber itself has ell elements. With the fixed finite shapes, the Minkowski polygon has area ell+O(sqrt(ell))+O(1) and perimeter O(sqrt(ell))+O(1); cell counting therefore gives ell+O(sqrt(ell)) candidates. This asymptotic bound concerns this family and does not bound integer bit cost. No physical <=7-fanout hierarchy for 13 or 19 has been implemented. Locality is in the current lattice basis, not the finest grid.

## 7. Fresh finite tests

The published experiment executes the frozen predecessor geometry, exact hull observer and quadratic keys after hash checks. Only the exponent adapter, anchors and complete polygon enumeration are extended.

- 48 exact phase certificates, including shared-facet signs and integer transitions.
- 51 full sections; summed cardinalities 997575; largest section 415625.
- All sections: exact distinct residues, central symmetry and zero convex-hull lattice holes. Every even-a section: full C6 set equality and exact covariance identities.
- 89 complete refinement edges; 45175 parents checked for their exact prime degree and stable old points.
- 288 exact matrix commuting squares on a bounded exponent grid.
- 132 complete permutation runs: six orders for three-prime groups and 24 orders for four-prime groups, from multiple starting sections; 3187800 descendant appearances across these runs; zero mismatches. These appearances include repeated sets and are not independent memories.
- The explicit old-19 failure is checked and the new rule retains its own canonical parent.
- The packaged published script was run again; the core result JSON matched byte-for-byte.

An example sequence has indices 5,35,455,8645,43225. Its cloud standard-deviation axis ratios are approximately 1.73205,4.43115,1.50159,1.49936,1.00000. These are numerical readouts, not symmetry tests. The final index equals 5^2*7*13*19 and is exactly C6-invariant.

## 8. BRC audit and limits

REUSE_EXECUTED: hash-pinned boundary-repair, mixed57, rational stencil and original baseline functions. EXTEND_EXISTING_TOOL: task-local prime/state adapter and selector anchors, not a new global family. COMPOSE_APPLIED: retain quotient identity and refinement provenance; compress only the projective shape permutation to a six-state sum. Counts, index, covariance and phase state are different observers. The shortest-vector norm support is sufficient to exclude new shared-facet constraints, not to reconstruct full lattice geometry or semantic neighborhoods.

Resolved in this slice: compatible 13; explicit 19 failure and repair; four-prime exact tests; an elementary finite exceptional-prime criterion and the stated split-prime family extension.

Unresolved: another inert prime such as 11; 2/3 directions; ordinary integer-label multiplication as an intrinsic geometric operation; arbitrary-prefix uniformity; physical bounded-fanout integration; semantic neighborhood quality. No theorem/Working Truth/Foundation promotion.

Classical comparison: Li-Gan-Ling, Coprime Sensing via Chinese Remaindering over Quadratic Fields, Part I, arXiv:1808.07505; Natarajan-Hong-Viterbo, Lattice Index Coding, arXiv:1410.6569. CRT/ideal lattices and finite-field actions are classical. The present claimed research content is the explicit selector compatibility/negative witness/finite exceptional-prime synthesis, not novelty of the classical ingredients.
