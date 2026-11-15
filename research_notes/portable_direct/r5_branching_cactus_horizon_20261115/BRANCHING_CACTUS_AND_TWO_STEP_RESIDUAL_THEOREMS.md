# R5 — branching triangle-cactus repair and finite-horizon cycle observers

Date: 2026-11-15. Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: inherited auxiliary, one-step, radius-two **indexed-center** replacement observer; binary suffixes are not native X6 cell coordinates. No changes to P000, ACTIVE worldview, task publications or protected Activity.

## 1. Inherited exact bridge kernel and source provenance

The prior proof is \`research_notes/portable_direct/r5_overlapping_triangle_chain_20261115/OVERLAPPING_TRIANGLE_CHAIN_EXACT_KERNEL.md\` at \`c177b61d1f8fd899038a91f5ecb6e99390890bce\`. For a finite simple graph G=(V,E) with nonempty E, represent each edge uv by a two-hot target suffix, and each allowed helper vertex v∈W by a one-hot old suffix. All target edge suffixes remain old-available. The exact previously proved source-labeled repair objective is

\[
\kappa_a(G,W;2)=|E|+\min_{S\subseteq W}\left(2|S|+|E[V\setminus S]|\right),
\qquad \kappa_{ab}(G,W;2)=2|E|.
\]

Here E[V\S] contains edges whose two endpoints lie outside S. The source witnesses use old core O1=0135 with first bit 0 at every edge; old cores O0=0125 and O4=0246 with first bit 1 at selected helper vertices; and O0 with first bit 1 at each edge unincident to S. The prior proof establishes both the exact lower bound and coverage of all five new single-a core types. This paper uses that exact stated scope, and explicitly rechecks the constructive cover for the finite cases below.

## 2. A genuinely branching family with a closed formula

Let T_k be the windmill of k≥1 edge-disjoint triangles (h,a_i,b_i) that all share the **same labeled hub** h, with all 2k peripheral vertices pairwise distinct. Thus |V|=2k+1 and |E|=3k. The old helper-availability language may include any peripherals; define z=[h∈W].

**Theorem A (windmill exact advice).** For every k≥1,

\[
\kappa_a(T_k,W;2)=
\begin{cases}
4k+2,& z=1,\\
6k,& z=0,
\end{cases}\qquad
\kappa_{ab}(T_k,W;2)=6k.
\]

In particular for k≥2, the central helper reduces the library by exactly 2k−2 sources, even though the triangles branch at a single shared hub. Peripheral availability does not change these optimal cardinalities.

**Proof.** Each peripheral vertex has degree two. Removing it from S decreases the source charge 2|S| by two and can uncover at most two edges. Therefore some minimizing S contains no peripheral vertex. If h is unavailable the minimum extra cost is |E|=3k. If available there are only two relevant choices: S=∅ costs 3k; S={h} costs 2+k because exactly the k peripheral-to-peripheral edges remain uncovered. For k≥1, k+2≤3k. Add the 3k mandatory edge baselines and apply the inherited joint-ab rigidity. A labeled optimal library for z=1 stores 3k edge O1 baselines, the two hub sources (O0,1,e_h), (O4,1,e_h), and k O0 edge sources on the peripheral-pair edges, totaling 4k+2. For z=0, store O1 and O0 at every edge, totaling 6k. QED.

## 3. Linear-time, source-preserving repair for any triangular cactus

Let G be a connected **triangular cactus**: every edge lies in one triangle, distinct triangles meet in at most one vertex, and their bipartite vertex–triangle incidence graph is a tree. There are k triangles, 3k edges and 2k+1 vertices. Fix any helper availability W⊆V. For binary selection s_v, disallow s_v=1 for v∉W. Define

\[
\Phi(s)=2\sum_{v\in V}s_v+
\sum_{(u,v)\in E}(1-s_u)(1-s_v).
\]

**Theorem B (factor-tree exact transfer).** All such instances admit a two-value min-plus message on each directed edge of the incidence tree. Root that tree at a vertex r. For the vertex-to-triangle message and triangle-to-vertex message, respectively, set

\[
M_{v\to T}(s)=2s+
\sum_{T'\ni v,\ T'\ne T}M_{T'\to v}(s),
\]

with M_{v→T}(1)=+∞ for unavailable v; and, writing T={v,x,y},

\[
M_{T\to v}(s)=
\min_{a,b\in\{0,1\}}
\big[M_{x\to T}(a)+M_{y\to T}(b)
+(1-s)(1-a)+(1-s)(1-b)+(1-a)(1-b)\big].
\]

The minimum of \(\Phi\) is \(\min_{s\in\{0,1\}}\big[2s+\sum_{T\ni r}M_{T\to r}(s)\big]\), with forbidden root state omitted. Consequently

\[
\boxed{\kappa_a(G,W;2)=3k+\min\Phi,\quad\kappa_{ab}(G,W;2)=6k.}
\]

The dynamic program has O(k) exact-integer operations and O(k) provenance storage. Keeping the two-bit argmin choices per triangle and tracing them from the root returns the **labeled** selected vertices S; the inherited explicit old-core construction returns every source identity.

**Proof.** The incidence graph is a tree. Removing a directed incidence edge disconnects a subtree. A vertex message charges its vertex exactly once, and every adjacent factor except its parent; a triangle message charges its three edge penalties exactly once, and minimizes only over its two child vertices. Induction on subtree size proves these are exact conditional minima. The root collects every vertex and every triangle once, with no overlap. Each triangle has four child-state possibilities for each fixed parent bit; every directed message is computed once, yielding O(k). The inherited bridge theorem converts the optimal selection into the exact minimum library and a source witness. QED.

This includes arbitrary branching degree and irregular availability masks. A cyclic necklace of triangles has a cyclic incidence graph and uses the preceding cycle-specific theorem rather than this tree factorization.

## 4. Exact finite-horizon residual equivalence for a cycle

Now return to the cyclic necklace's k labeled **spine** vertices, k≥3, and set \(u_i=1\) exactly when spine helper i is unavailable. Its current cardinality is \(\kappa_a=5k+q(u)\), where

\[
q(u)=\sum_{i\pmod k}u_i u_{i+1}.
\]

An available operation \(\mathrm{Set}_i(b)\) changes only the named bit u_i to b∈{0,1}; we may observe q immediately and after each finite operation word. Let \(O_h(u)\) be the vector of all q readouts after command words of length at most h, including the empty word. The operation words are **named**; indices are not quotient-renamed.

**Theorem C (exact observation depth and one-step collisions).** For every k≥3:

1. \(O_1\) has exactly \(2^k\) distinct values if \(4\nmid k\), and exactly \(2^k-2\) distinct values if \(4\mid k\).
2. When \(4\mid k\), the **only** two nontrivial equivalence classes are the two-element pairs
   - periodic words with ones at indices 0 mod 4 versus ones at indices 2 mod 4;
   - periodic words with ones at indices 1 mod 4 versus ones at indices 3 mod 4.
   Every other state has a singleton \(O_1\)-class.
3. \(O_2\) is injective for **all** k≥3. Thus the minimum observation horizon sufficient to retain the full named availability state is one when 4 does not divide k and two when 4 divides k. In the latter case the exact one-step quotient uses \(2^k-2\) states, but the two-step quotient requires all \(2^k\) states (k bits).

**Proof.** Write \(t_i(u)=u_{i-1}+u_{i+1}\). The two one-step readouts under \(\mathrm{Set}_i(0)\) and \(\mathrm{Set}_i(1)\) differ by \(t_i(u)\). Thus \(O_1(u)=O_1(v)\) implies \(q(u)=q(v)\), \(t_i(u)=t_i(v)\), and
\(u_i t_i(u)=v_i t_i(v)\) for every i. Let \(d_i=u_i-v_i\). Equality of neighbor sums gives the **exact integer recurrence** \(d_{i+2}=-d_i\), with cyclic indices. Every such difference has period four. If 4 does not divide k, periodic consistency forces d=0. For k divisible by four, \(d=(a,b,-a,-b)\) repeated, a,b∈{−1,0,1}. Whenever d_i≠0, the equation \(d_i t_i=0\) and nonnegative bits force both neighboring bits to be zero in both u,v. Hence a and b cannot both be nonzero. If a≠0, b=0, all odd positions vanish; the even differing bits are forced to form exactly the first pair. Similarly a=0, b≠0 yields precisely the second pair. Conversely, each indicated pair has q=0 and identical one-step named readouts (t_i=1 on the complementary parity and 0 on the selected parity). This establishes the complete classification and count.

For two-step separation, suppose u≠v yet \(O_1(u)=O_1(v)\). Choose i with \(u_i\ne v_i\). From the preceding argument \(t_i=0\), so both immediate neighbors of i are zero in both states. First issue \(\mathrm{Set}_{i-1}(1)\). Its q values agree because \(O_1\) agrees; now the left neighbor of i is 1 and its right neighbor is 0. Next issue \(\mathrm{Set}_i(0)\). The two q values decrease by \(u_i\) and \(v_i\), respectively, and are therefore unequal. Hence \(O_2\) is injective. Finally \(O_0\) is not injective for k≥3 because q(0)=q(e_i)=0, establishing the minimal horizons. QED.

This two-step exact lower bound strengthens the previous arbitrary-future k-bit distinguishability theorem: a **uniform horizon of two** suffices when first-step observations collide. Its scope is the named Set(0/1) action alphabet and the scalar q observer; other future-operation alphabets have their own residual quotient.

## 5. Executable evidence, finite scope and next frontier

The companion standard-library Python program \`VERIFY_R5_BRANCHING_HORIZON.py\` was executed locally. It directly enumerates every binary mask for O1 at k=3..12 and every two-command word for every mask at k=3..8, reproducing the two exceptional collision classes. It brute-forces all selected helper subsets for windmills with k=1..5 (hub present/absent), and tests 97 explicit triangular-cactus (shape,availability) instances of k=1..5 against the exact factor-tree recurrence. For all 107 graph tests it also builds the inherited source-labeled old-core library and checks coverage of the five single-a target types via the original radius-two distance \(\rho=|C\setminus O_j|+[t\ne s]+|x\triangle y|\).

Actual returned status: \`PASS_R5_BRANCHING_CACTUS_AND_HORIZON_TWO\`. The associated JSON records the finite ranges and sample source IDs. Universal claims above rest on the displayed symbolic proofs; the finite calculations are reproducible checks, and independent review is outstanding.

**Further unit:** general bounded-treewidth factor graphs with exact source-aware reconstruction, then partial/observation-only action alphabets where the two-step state lower bound may decrease; determine minimal quotients under explicitly limited named operations.
