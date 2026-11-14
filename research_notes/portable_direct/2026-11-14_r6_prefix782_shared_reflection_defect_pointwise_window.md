# PREFIX-782 — Exact sign-loss window with one shared reflection defect

Date 2026-11-14. Status AUTHOR_PROVED / EXACT_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED. Prior scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d. Research provenance EM-DIRECT-E77192, MCP-d9aca4ec6e00440eba66035326ea5a4e, RA-66BBE259AEE1AD543D9454A3. Independent auxiliary-model research; no shared CLAIM.

## Definition and scope

Reusing the 189-step BRC–Gamma external auxiliary model and the rational grid cells R1=[38,39]^2/768, R2=[39,40]^2/768 together with their reflections under the second-parameter involution, let x_i(q)=A_i-qB_i for 0<B1<B2 and q>0. The unperturbed mixed differences of V_q divided by q are (x1,x2,-x1,-x2).

Each base square has three private corner errors; each is exactly equal to the error at its reflected private corner. Their independently attainable signed sums range over u_i in [-S_i,S_i], where S_i is the sum of its three nonnegative corner budgets. The base squares share an error h at one corner, and their reflected squares share a separate error h' at the reflected partner, obeying |h|<=c, |h'|<=c, |h-h'|<=delta, c,delta>=0. The four normalized observed mixed differences are

\[
a_1=x_1+h+u_1,\quad a_2=x_2+h+u_2,\quad
a_3=-(x_1+h'+u_1),\quad a_4=-(x_2+h'+u_2).
\]

## Theorem 782.1: sharp fixed-parameter existence criterion

At any prescribed real q>0, there exists a permitted fourteen-corner error assignment whose four mixed differences do not contain both a strictly positive and a strictly negative value **if and only if**

\[
\boxed{|x_1|\le S_1+c,\qquad |x_2|\le S_2+c,\qquad
|x_1-x_2|\le S_1+S_2+\min(\delta,2c).}
\]

If any inequality fails, *every* error assignment in this class preserves both strict signs. Equality is permitted in the existence condition.

**Proof, necessity.** A finite real tuple lacks both strict signs precisely when all its entries are nonnegative or all are nonpositive. If all a_i>=0, then for i=1,2 we have x_i+h+u_i>=0 and x_i+h'+u_i<=0, so h>=h'. Put r=h-h', s=(h+h')/2. The shared bounds imply 0<=r<=min(delta,2c), |s|<=c-r/2. The cell inequalities become |x_i+s+u_i|<=r/2. Hence s belongs simultaneously to the three intervals

\[
J_0=[-c+r/2,c-r/2],\qquad
J_i=[-x_i-S_i-r/2,-x_i+S_i+r/2]\ (i=1,2).
\]

Their pairwise intersections force |x_i|<=S_i+c and |x1-x2|<=S1+S2+r. All a_i<=0 is identical after swapping h and h'.

**Proof, sufficiency and construction.** If the three boxed inequalities hold, choose r=max(0,|x1-x2|-S1-S2), which lies in [0,min(delta,2c)]. The same three intervals J0,J1,J2 pairwise intersect; for intervals on the line this implies common intersection. Choose s in it, let h=s+r/2, h'=s-r/2, and set u_i equal to the clamp of -(x_i+s) onto [-S_i,S_i]. Then |x_i+s+u_i|<=r/2, and all four a_i are >=0. The shared bounds hold by construction. Every u_i is realized by allocating |u_i| among the three private corner error budgets with their mixed-difference coefficient signs; repeat those private errors at the reflected corners. Thus the constructed aggregate is a legitimate fourteen-corner observer. Reversing h and h' gives the all-nonpositive case. QED.

## Corollary 782.2: the complete positive-q interval

Set T_i=S_i+c and U=S1+S2+min(delta,2c). For 0<B1<B2, the exact set of positive q permitting a sign-loss observer is the intersection of (0,infinity) and three closed rational-affine intervals

\[
\begin{aligned}
I_1&=[(A_1-T_1)/B_1,(A_1+T_1)/B_1],\\
I_2&=[(A_2-T_2)/B_2,(A_2+T_2)/B_2],\\
I_3&=[(A_2-A_1-U)/(B_2-B_1),(A_2-A_1+U)/(B_2-B_1)].
\end{aligned}
\]

It may be empty. Outside the intersection every permitted observation retains both strict signs. For delta=0 this reduces exactly to PREFIX-781's equivariant cancellation window. The one shared reflection defect increases only the width of I3 and saturates at delta>=2c.

Quantifiers: the bad observer can be chosen separately for each q; this is a pointwise theorem, not a simultaneous all-q observer construction.

## Explicit new rational witness

Let A1=1,A2=2,B1=2,B2=3, S1=1/5,S2=3/20,c=1/10. At delta=0, the bad-q set is the singleton {13/20}. With delta=1/10 it is [7/12,13/20]. At q=3/5 choose h=0,h'=-1/20,u1=1/5,u2=-3/20. Then x1=-1/5, x2=1/5 and the four normalized differences equal (0,1/20,1/20,0). The private budgets (1/10,1/20,1/20) on R1 and (1/20,1/20,1/20) on R2 realize both sums, with exact private reflection. Thus a single shared reflection defect creates loss of both strict signs for a q at which the previous exact-reflection class had a strict two-sign guarantee.

## Validation and next research

Companion program PREFIX782_R6_SHARED_REFLECTION_POINTWISE_CHECK.py uses only the Python standard library Fraction and checks 12,960 deterministic rational coefficient/budget/parameter cases: 616 sign-loss-feasible and 12,344 infeasible. It checks direct constructive geometry against exact interval membership, the explicit rational witness, and private corner distribution. Output: ALL_CHECKS_PASS PREFIX782 SHARED_DEFECT_POINTWISE_WINDOW. The universal real-parameter result is proved by the interval argument; regression covers only those finite cases.

The historical 189-layer BRC/Gamma recurrence and its coefficients are reused without rerunning the original computation. The example uses independent small rational coefficients. Native BRC/X6 comparison remains unresolved: inspect actual Cell/Link/Port, signed-source, branch and event-time reflection records; prove whether the six private corner pairs satisfy exact observation equality, bound the shared pair difference, then evaluate this exact q-window with the actual model coefficients. Native comparator grid exclusions added: zero.

Source pointers: PREFIX-781 paper at enterprise-math commit 7d70facce45b39ab1ee764ec6ff2ca118f4ef379; PREFIX-780 paper at commit f1f1ec77037225da01fd5ea24bb3f311508c5a4d. Locked P000 and ACTIVE worldview control the original X6 ontology; these two scalar parameters belong only to the external auxiliary model.

Next exact question: if one private reflection pair fails equality, characterize the resulting four-sign observation polytope with *measured* private defects rather than assuming this restricted observation class.
