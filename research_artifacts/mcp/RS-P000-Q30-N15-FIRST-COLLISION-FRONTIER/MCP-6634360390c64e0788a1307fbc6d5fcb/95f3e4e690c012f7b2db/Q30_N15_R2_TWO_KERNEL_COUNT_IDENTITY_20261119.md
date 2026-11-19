# Q30 n=15 r=2 sector: direct two-kernel counting identity (2026-11-19)

Task RS-P000-Q30-N15-FIRST-COLLISION-FRONTIER. Scope: connected simple graphs on **two prescribed degree-3 labeled vertices** u,v and thirteen prescribed degree-2 labeled vertices (s=13). This is an independent combinatorial count, not a 1-WL packet or collision classification.

Suppress all maximal degree-two paths. A connected cubic multigraph on two degree-3 vertices has exactly two types: (I) three parallel u-v edges, called the theta kernel; (II) one loop at u, one loop at v, and one u-v edge, called the barbell kernel. In both cases each original simple graph corresponds to a subdivision satisfying simplicity.

**Theta.** Three unordered internally disjoint u-v paths receive nonnegative internal-vertex counts k1,k2,k3 summing to s. Simplicity permits **at most one zero** because two unsubdivided u-v paths would be duplicate simple edges. For s=13, the number of admissible ordered weak compositions is binom(15,2)-3=102. Given a composition, choosing and ordering the s distinct prescribed degree-two labels along the three oriented u-v paths gives s! possibilities, and each actual graph is counted exactly 3!=6 times by permuting the three path slots. Thus theta = 13!*102/6 = **105859353600**.

**Barbell.** Let k_u,k_v>=2 be the numbers of internal degree-two vertices on the two self-loops; a loop must have at least two subdivision vertices in a simple graph. Let k_b>=0 be those on the connecting path. The ordered solutions k_u+k_v+k_b=s number binom(s-2,2); for s=13 this is binom(11,2)=55. For every solution, after assigning and ordering the s labels, reversal of each loop's cyclic order represents the same undirected graph, so divide by 2^2=4. The distinguished labeled cubic endpoints prevent swapping the two loops. Thus barbell = 13!*55/4 = **85621536000**.

The two types are disjoint and exhaustive, so the exact r=2, s=13 connected labeled count is **191480889600**, independently equal to the vertex-neighbor/component recurrence in Q30_N15_SECTOR_TARGETS_20261119.md.

Regression at s=12 (n=14): theta = 12!*(binom(14,2)-3)/6 = 7025356800; barbell = 12!*binom(10,2)/4 = 5388768000; total = **12414124800**, matching the immutable n=14 accepted sector certificate.

This validates the r=2 sector's independent count target, **not** a list of isomorphism representatives, their orbit completeness, or the frozen Q30 exact stable packets. Next, count actual isomorphism classes of all valid subdivisions and compute equality of full frozen packets. Never infer n=15 collision freedom from these labeled graph totals.
