# PREFIX-481 — Exact native positive-weight collapse on X6 BRC observation fibers

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent author-side Source research; no TASK CLAIM or native Result is asserted.

## Inherited model and problem

Continuation: PREFIX-480 at commit afa574d540566e6c2551d9d8973394c318a270cd. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. P000 X6 spatial axes and the active observer-preservation discipline apply. This paper concerns the declared restricted positive-weight ordered-path model, rather than a signed-amplitude or physical-heartbeat dynamics claim.

Normal directions are aAbBcCdDeE on native E2..E6, with positive weights respectively (6,1,12,1,18,1,24,1,36,1). Distinguished x=+E1 has weight 1 and is allowed only at the beginning or immediately after a fixed ordinary gate word w; normal letters are always legal. The KMP suffix state q controls the next gate operation.

For a length-n path let s be its number of x letters, let u_i,v_i count positive/negative ordinary letters on each of the five axes i=a,b,c,d,e, and set y_i=u_i-v_i and p_i=min(u_i,v_i). The base BRC observation is

$$
O=(s,y_a,y_b,y_c,y_d,y_e,V,W),\quad
V=p_b+2p_d+p_e,\quad W=p_c+p_e.
$$

PREFIX-480 proved that full positive-path weight histograms on (n,O,q) can be propagated exactly. The present question: do these **particular native positive weights** have independent weight-histogram shape inside one fixed observation fiber, and are independent moment jets actually necessary?

## Theorem 1 — Exact positive weight factorization through (n,O)

**For every fixed ordinary gate word w, every integer n>=0 and every nonempty legal-path fiber (n,O,q), all paths in that fiber have exactly the same positive weight.** This includes repeated, mixed-sign and self-overlapping gate words. The history state q does not enter the weight formula.

Write y_i^+=max(y_i,0), and define the integer

$$
P=\frac{n-s-\sum_{i=a}^{e}|y_i|}{2}.
$$

For every reachable observation P>=0. Define

$$
A(n,O)=P+V+y_a^++2y_b^++y_c^++3y_d^++2y_e^+,
$$

$$
B(n,O)=P+W+y_a^++y_b^++2y_c^++y_d^++2y_e^+.
$$

The exact product weight of every path in the fiber is

$$
\boxed{\lambda(n,O)=2^{A(n,O)}3^{B(n,O)}}.\tag{1}
$$

Let C[n,O,q] be the number of ordered legal paths and H[n,O,q] their full positive-weight histogram. Then as a finite-support counting measure on exact positive integer weights,

$$
\boxed{H[n,O,q]=C[n,O,q] \delta_{\lambda(n,O)}}.\tag{2}
$$

For every integer r>=0, its rth raw weight moment is

$$
\boxed{M_r[n,O,q]=C[n,O,q] \lambda(n,O)^r}.\tag{3}
$$

**Proof.** From u_i=p_i+y_i^+ and v_i=p_i+max(-y_i,0),

$$
n-s=\sum_i(|y_i|+2p_i),
$$

so P=\sum_i p_i. The native weights of the five positive ordinary directions have prime-valuation rows (in order a,b,c,d,e)

$$
\alpha=(1,2,1,3,2),\qquad \beta=(1,1,2,1,2)
$$

for prime factors 2 and 3. Negative normal directions and x have weight 1. Thus the path's prime valuations are \sum_i \alpha_i*u_i and \sum_i \beta_i*u_i. But alpha-(1,1,1,1,1)=(0,1,0,2,1) is exactly the p-coefficient row defining V, while \beta-(1,1,1,1,1)=(0,0,1,0,1) is the row defining W. Substitute u_i=p_i+y_i^+ and \sum_i p_i=P. This yields A and B as displayed. Each ordered path contributes one copy of the same positive-weight atom, proving (2); calculating the moment gives (3). QED.

### Exact integer kernel behind the information collapse

At fixed (n,s,y), the information in the p_i discarded by retaining only (V,W) is precisely the integer kernel of

$$
\sum_i p_i=P,\quad p_b+2p_d+p_e=V,\quad p_c+p_e=W.
$$

This kernel has the exact Z-basis

$$
r_1=(1,-2,0,1,0),\qquad r_2=(1,-1,-1,0,1),
$$

in coordinates (p_a,p_b,p_c,p_d,p_e). Indeed, let d and e be the p_d and p_e entries of any kernel vector. The equations force the full vector to equal

$$
(d+e,-2d-e,-e,d,e)=d,r_1+e,r_2.
$$

The corresponding native weight relations are

$$
6\cdot24=12^2=144,\qquad 6\cdot36=12\cdot18=216.
$$

Thus **both** independent directions of information lost in (P,V,W) are weight-preserving. Concrete raw paths aAdD and bBbB have the same (n,O), weight 144; aAeE and bBcC have the same (n,O), weight 216. Under gate aab both paths in each pair end in q=0.

Length must be retained: the empty path and aA share O=(0,0,0,0,0,0,0,0), but their weights are 1 and 6 at lengths 0 and 2. Formula (1) therefore uses n explicitly.

## Corollary — Exact future-safe count-only histogram transfer

Declare the future interface to allow arbitrary finite legal sequences of the eleven native direction-append operations, with KMP legality, final (n,O,q) and requests for any exact positive-weight moment or complete positive-weight histogram. By PREFIX-480's proved BRC right-action and KMP state transition, the recurrence on (n,O,q) computes the exact count C. Reconstruct \lambda(n,O) by (1) and output (2) or (3). Therefore **one exact path count per reachable (O,q) fiber, plus its observation and known length, is sufficient for the entire histogram and all moments at every finite future horizon**. No separate histogram dictionary or moment truncation is necessary.

This is a certified BRC reduction within the declared positive product-weight observer. Source path IDs, raw signed-direction counts, signed phase/amplitude, physical event time and other independently queried observables have their own carriers. The exact native weight choices are a material hypothesis. For example, replacing only the weight of direction e from 36 to 35 turns the equal-observation paths aAeE and bBcC into weights 210 and 216. With those changed weights the same fiberwise collapse would fail.

## Theorem 2 — Exact quadratic valuation-label set before BRC collapse

Let S={(0,0),(1,1),(2,1),(1,2),(3,1),(2,2)} be the one-normal-step set of prime valuation pairs (v2,v3); the value (0,0) comes from the five negative normal directions. For any integer t>=0, the set of all products of **exactly t ordinary directions without a special gate restriction** corresponds to the t-fold Minkowski sum t*S and satisfies

$$
\boxed{|t*S|=3t^2+2t+1}.\tag{4}
$$

For any gated path at length n containing s special letters, its weight label belongs to (n-s)*S, so 3(n-s)^2+2(n-s)+1 bounds the number of labels before grouping by BRC fibers.

**Proof.** Let Q be the lattice polygon with cyclic vertices (0,0),(3,1),(2,2),(1,2). Its complete lattice-point set is exactly S: four primitive-edge boundary vertices and two interior points (1,1),(2,1). The shoelace area is 3 and the boundary has exactly four lattice points. A two-dimensional lattice polygon can be triangulated using its lattice points into unimodular triangles. For such a triangle with vertices v0,v1,v2, any integer point of its t-fold dilation has nonnegative integer barycentric coordinates summing to t, because (v1-v0,v2-v0) is a Z²-basis. Given z in tQ∩Z², choose a triangle of the triangulation containing z/t. Hence z is the sum of exactly t members of Q∩Z²=S. The converse inclusion is immediate, so t*S=tQ∩Z². Apply Pick's theorem to the polygon tQ: area=3t², boundary=4t, and hence total lattice-point count=3t²+(4t)/2+1. This proves (4) for t>=1; t=0 gives the singleton {(0,0)}. QED.

The valuation lattice has rank two: the independent labels (1,1) and (2,1) have determinant -1. At the native BRC observation resolution, Theorem 1 gives the stronger one-bin-per-fiber fact.

## Actual exact verification and coverage

The accompanying executed standard-library Python certificate independently evolves (a) exact prime-valuation histograms keyed by (O,q) and (b) a count-only BRC/KMP recurrence, comparing their entire per-fiber maps to (1)-(3). It also independently enumerates every ordered legal path for n=0..4. Both gate words aab and aba are checked for every n=0..8; the certificate enumerates t*S and checks (4) for t=0..30. All arithmetic is exact integer arithmetic.

At n=8, aab has 58,496 (O,q) fibers and exactly 58,496 occupied histogram bins; aba has 58,498 fibers and exactly 58,498 bins. Both have 33,295 base BRC observations and 110,054,001 ordered legal paths. Both raw-kernel collision witnesses are verified, along with the changed-weight contrast 210!=216. The program's complete stdout is in PREFIX481_EXACT_EXECUTION.log and ends ALL_CHECKS_PASS.

The universal statements follow from the algebraic/combinatorial proofs, while the finite checks target implementation consistency. Reuse: PREFIX-480 right-action and transfer law = REUSE_APPLIED; its earlier histogram implementation = EXTEND_EXISTING_TOOL. The scientific pin is unchanged.

## Resolved research question and next unit

The PREFIX-480 proposed search for a pair of native BRC fibers sharing initial moments and differing at higher moments is resolved **within the native weight model**: every nonempty fiber has a singleton histogram, hence no such pair with the same count and first moment but distinct higher moments can exist after retaining n and O. This provides a stronger exact compression mechanism than moment truncation.

PREFIX-482 candidate: Classify all positive rational direction-weight assignments for which products factor through (n,O). For the five positive weights with negatives and x fixed at 1, the expected exact criterion is that every prime-valuation row annihilates the Z-kernel spanned by r1,r2, equivalently lies in the rational span of the P,V,W rows; prove necessity on nonnegative realizable fibers and determine minimal additional coordinates when one or both kernel directions are observable. Explicitly test a changed weight e=35. This question preserves native X6, q, provenance and future-operation scope.

## Authority and version status

Read: verified current global main and current project P000/ACTIVE/method/portable/continuation rules; frozen scientific commit f42f2906d77f24085c123f3ccfe9667d41caa96d exists. Native Site identity verified static_machine_readonly with research_authority_granted=false, task listing returned CONTROL_QUOTA, and session start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Active Owner/Researcher-ID not confirmed. This is author-proved Source research with exact integer checks; independent mathematical Review, formal Result and Admission remain pending.
