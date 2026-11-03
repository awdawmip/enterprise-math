# PREFIX-475 — Exact suffix fibers, finite-horizon BRC quotients and weighted paths for all pure-run gates a^k

**2026-11-04 · AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.** Author-side portable research, not a native Result or Review.

## 1. Exact model, dependency and objective

This extends PREFIX-474 (the aa overlap exception) to every k >= 1, with path length n >= 0. Scientific input is frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d; current normative rules are read separately. The parent question is how much ordered-path history an X6 BRC observer must retain for a specified future-operation horizon.

The P000-native six-axis signed path uses special direction x=+E1, legal only at the first step or immediately after at least k consecutive copies of ordinary a=+E2. Ten ordinary signed directions a,A,b,B,c,C,d,D,e,E (E2 through E6) are always legal. The history automaton state q in {0,...,k} is the terminal run length of a truncated at k. Ordinary a increments q up to k; all other directions reset q to 0.

The exact positive-BRC base observer f=(s,y1,...,y5,V,W) retains x-count s, five signed displacements y_i, and p_i=min(number of positive and negative steps on axis E_(i+1)). Set V=p2+2p4+p5 and W=p3+p5, with i=1,...,5; equivalently coefficients (0,1,0,2,1) and (0,0,1,0,1) on the five p coordinates. All five cancellation coordinates are detected by V or W when their signed displacement vanishes. Let S_n denote attainable base f, B_n(k)=|S_n|, and S_(n,q) denote base observations admitting a legal path ending in q. Set B_m=0 for m<0.

The imported precise base-state generating series from PREFIX-470/471 is:
\[
G_k(z)=\sum_{n\ge0}B_n(k)z^n
=\frac{(1+2z^2)(1+z)^2(1+z-z^{k+1})}{(1-z)^8(1-z^{k+1})}.
\]
The imported PREFIX-472 base-rank and PREFIX-474 reversible ordinary-word padding T_(a^j) are used at their stated scope. Appending a^j changes f according to the known signed displacement and pair cancellations; it is injective because the old signed displacement can be recovered from the new one and j, allowing the cancellation increment to be subtracted.

## 2. Theorem A — exact holes and all KMP suffix supports

For every k>=1 and n>=0 define the explicit set
\[
E_k(n)=
\{f(a^n): n\ge1\}\cup\{f(xa^{n-1}):2\le n\le k\},
\qquad
u_k(n)=|E_k(n)|=\mathbf1_{n\ge1}+\mathbf1_{2\le n\le k}.
\]
Terms with false predicates are absent. Then the following **all-length equalities of observation sets** hold:
\[
\boxed{S_{n,0}=S_n\setminus E_k(n)},\qquad
\boxed{S_{n,j}=T_{a^j}(S_{n-j,0})\quad(1\le j<k)},\qquad
\boxed{S_{n,k}=T_{a^k}(S_{n-k})}.
\]
Thus for j<k the support size is B_(n-j)-u_k(n-j); the full-match size is B_(n-k). The proper-prefix padding deficiency is at most two explicit observation fibers per length, uniformly over k and n.

**Proof.** If a legal path contains an ordinary direction c other than a, move one c to the end. This does not destroy a required k-run directly before an x: such a run contained only a, so the removed c lay outside each of them. The resulting legal representative has identical f and ends in q=0. For words consisting only of a and x, let s=#x,t=#a. If s>=2, legality requires t>=k(s-1); conversely the word x(a^k x)^(s-2) a^(k+t-k(s-1)) x is legal, has these counts and ends in q=0. If s=1, a q=0 representative exists precisely for t=0 (x) or t>=k (a^t x). With s=0 only the empty word has q=0. Therefore exactly the two displayed pure-word families lack q=0. They have no alternative representatives with other letters: their f has the prescribed s,y and V=W=0, which forces every p_i=0 and the unique pure-a/x occupancy.

For 1<=j<k, exact terminal run j occurs exactly when deletion of the last j copies of a leaves q=0. Appending those a's is always legal, hence the injective padding identity. Full q=k occurs exactly when the final k letters are a^k; deletion preserves all earlier x-gates and conversely every legal prefix can append a^k. This proves all three claims. k=2 specializes to PREFIX-474; for k=1 there is only the a^n hole and one full-match state.

## 3. Theorem B — minimum future observable quotient, all n,k,H

At fixed n, retain f and Boolean legality/results of all future words of length <=H; future readout is the final base f. Two tagged states (f,q) are equivalent iff these observations coincide. Write N_k(n,H) for their minimum exact class count.

For each 0<=r<k let
\[
e_{k,r}(n)=\mathbf1_{n\ge r+1}+\mathbf1_{r+2\le n\le k}.
\]
Then the low-state union is precisely
\[
\boxed{\bigcup_{q=0}^{r}S_{n,q} =
S_n\setminus(\{f(a^n):n\ge r+1\}\cup
\{f(xa^{n-1}):r+2\le n\le k\})}
\]
and its size equals B_n-e_(k,r)(n).

**Proof.** All f with a non-a ordinary step or at least two x's have a q=0 representative by Theorem A. A pure-a path has unique q=min(n,k); a pure path with exactly one x and 1<=t<k copies of a has unique legal order xa^t and q=t. One x with t>=k also admits q=0, as does x alone. This gives the two and only two excluded classes of pure observation fibers.

A future x can first occur after k-q copies of a, at continuation length k-q+1; the word a^(k-q)x witnesses this threshold. When 1<=H<k, put r=k-H. All q<=r have exactly the same allowed future words of length <=H (only ordinary steps); every q>r is distinguished from each lower q by its witness. This is also valid with the final f observer because an ordinary extension changes f deterministically from its current f. At H=k, all q are distinguishable; at H=0 all q collapse inside each f fiber. It follows **for every n>=0**:
\[
\boxed{N_k(n,0)=B_n;}
\]
\[
\boxed{N_k(n,H)=B_n-e_{k,r}(n)+
\sum_{j=r+1}^{k-1}(B_{n-j}-u_k(n-j))+B_{n-k},
\quad 1\le H<k,\ r=k-H;}
\]
\[
\boxed{N_k(n,H)=F_n=\sum_{j=0}^{k}B_{n-j}-
\sum_{j=0}^{k-1}u_k(n-j),\quad H\ge k.}
\]

Set U_k(z)=z/(1-z)+sum_(j=2)^k z^j and E_(k,r)(z)=z^(r+1)/(1-z)+sum_(j=r+2)^k z^j. Then:
\[
F_k(z)=(1+z+\cdots+z^k)G_k(z)-
(1+z+\cdots+z^{k-1})U_k(z)
\]
and for 1<=H<k,
\[
Q_{k,H}(z)=
(1+\sum_{j=r+1}^{k}z^j)G_k(z)
-E_{k,r}(z)-\sum_{j=r+1}^{k-1}z^j U_k(z).
\]
For H=0 this is G_k; for H>=k it is F_k. These are rational formal power series with all boundary terms included.

**Constructive coding.** Use PREFIX-472 base-rank to rank the low union S_n after skipping at most two explicitly known exceptional f. Each high proper q=j block is bijective by inverse T_(a^j) to S_(n-j) after skipping E_k(n-j) (again <=2 holes). The full q=k block bijects to all S_(n-k) by inverse padding. Concatenating these labeled blocks ranks/unranks the precise finite-horizon classes into [0,N_k(n,H)-1] without a complete-state dictionary. Its fixed width is optimally ceil(log2 N_k(n,H)) bits (0 for a singleton); fixed k reuses the prior logarithmic arbitrary-precision integer-operation base codec. The bit cost of input representation, full provenance and arithmetic is a separate engineering question.

## 4. Theorem C — suffix-resolved exact ordered-path counts and positive weights

Let a have commutative formal positive weight t, all other ordinary directions weight sum U, special x weight chi, and S=t+U. Let L_(k,q)(z) count **ordered** legal paths ending in state q, with product step weights, and L_k(z)=sum_q L_(k,q)(z). Renewal at special x gives (reusing PREFIX-466):
\[
\boxed{L_k(z)=\frac{1+\chi z}{1-Sz-\chi t^kz^{k+1}}}.
\]
The new explicit terminal-state refinement is, for every k>=1:
\[
\boxed{L_{k,j}(z)=(tz)^j(1-tz)L_k(z)\ (0\le j<k),\qquad
L_{k,k}(z)=(tz)^kL_k(z).}
\]

**Proof.** Removing the last j ordinary a's bijects all legal words with words ending in at least j consecutive a's; the weighted series is (tz)^j L_k. For j<k the exact q=j class is the difference between at-least-j and at-least-(j+1) classes; full q=k is at-least-k. The formulas telescope. For the native positive model, t=6, S=101, chi=1; for the unweighted path count, t=1, S=10, chi=1. This calculation preserves ordered multiplicity and mass separately from Boolean BRC support.

## 5. Executed certificate, scope and discriminating comparison

The actually executed JavaScript BigInt certificate (prefix475_purerun_gate_certificate.js) checks k=1,2,3,4 and n=0,...,8, comparing exact dynamic state sets with Theorems A/B and rational base coefficients. All horizons H=0,...,k+1 and all KMP support sets are checked. It additionally checks the scalar and every suffix-resolved weighted-path coefficient. For n=0,...,4 it independently enumerates every legal ordered word, recomputes f from raw direction counts and independently compares exact word multiplicities and positive masses. 391304 tagged states were processed across the grid. Computation returns ALL_CHECKS_PASS. Arbitrary-precision BigInt holds all multiplicities and weights; the bounded small n and k indexes and distinct-state cardinalities use exactly representable JavaScript integers.

At n=8:

| k | B_8 | q=0,...,k support sizes | N(8,H=0,...,k) | F_8 | ordered paths | positive mass |
|---|---:|---|---|---:|---:|---:|
| 1 | 35277 | 35276,16410 | 35277,51686 | 51686 | 117761041 | 10980799387082400 |
| 2 | 33797 | 33796,15862,6869 | 33797,40665,56527 | 56527 | 110650630 | 10938069583787562 |
| 3 | 33295 | 33294,15696,6823,2685 | 33295,35979,42802,58498 | 58498 | 110054001 | 10935893866951302 |
| 4 | 33130 | 33129,15651,6814,2683,932 | 33130,34061,36744,43558,59209 | 59209 | 110004300 | 10935785972233374 |

For k=3,n=8, the prior aba model has B=33295 and full F=58498, matching aaa's two counts, but aba has H=1 count 35980 and H=2 count 42804 whereas aaa has 35979 and 42802. Thus the two words differ in finite-horizon residual needs despite matching full counts at this length. Their positive path weights also differ because a^3 has weight 6^3 and aba has 6^2*12.

External theory checked as context: A. W. To, *Parikh Images of Regular Languages: Complexity and Applications*, arXiv:1002.1464, and L. J. Guibas & A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory A 30 (1981), 183–208, DOI:10.1016/0097-3165(81)90005-4. This note claims exact model-specific formulas, not priority over the general formal-language literature.

## 6. Source authority and next question

GitHub authentication in this run: awdawmip (admin/push on enterprise-math). Native task inventory returned CONTROL_QUOTA; the available Sites session is static machine read-only and reports research_authority_granted=false. This is author-side Source evidence without a new native CLAIM, independent review or Admission.

BRC usage: COMPOSE_APPLIED. Reuses exact X6 positive valuation update, previously proved base count and codebook-free base rank, and the reversible suffix padding. The KMP state q is typed path history, not an extra native spatial axis. Boolean support, path order/multiplicity and positive masses are distinct observables.

**Next PREFIX-476:** Test mixed-letter self-overlap patterns to find a proper-prefix padding deficiency whose size increases with n, or establish a fixed-word bound in a new nontrivial family. If growth occurs, derive a semilinear description and exact ranking correction. Keep the frozen scientific source and role boundaries.
