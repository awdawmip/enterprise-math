# PREFIX-598-R2 — Universal exact positive image cone for the 48-state native X6-BRC tail

Date: 2026-11-08. Scientific input pinned to enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Author-side proof and executed rational/integer certificate; independent Driver review pending. Researcher EM-DIRECT-A9F022; native activity RA-BB6445D786B142A6E5EC58D2. Depends on PREFIX-587, PREFIX-596 and PREFIX-597. Original four STAR triples, 48 phases, 96 bit ports, 576 typed edges, six native axes and the three marked gate actions are unchanged.

## Theorem 598.1: all positive-parameter one-step output cones coincide

Let the phase set be P={(a,p,c)} from the original X6-BRC four-STAR construction, S the 48x48 phase adjacency, g=4 the marked gate target, and R the reversal permutation rho(a,p,c)=(a,c,p). For each signed current-axis s in {-6,...,-1,1,...,6}, let G_s={i:c_i=s}; each G_s consists of exactly four phases.

The exact PREFIX-596 compact transition has form

    Q(x,z)=Dx * Drow * S * Dcol(z),

where Dx[i,i]=x_|c_i|, Drow[g,g]=1, Drow[i,i]=2 otherwise, Dcol(z)[g,g]=(z+3)/2, and Dcol(z)[j,j]=1 for j!=g. Assume x_a>0 for all six axes and z>=0. Write W0 as the block diagonal direct sum of twelve blocks J4-I4, indexed by signed current-axis groups. Then, as equality of subsets of real 48-space,

    Q(x,z) R_+^48 = Drow W0 R_+^48.

In particular the entire positive output image cone is the same for EVERY choice of six positive axis weights and nonnegative gate weight, including z=0, and is a full-dimensional simplicial polyhedral cone with exactly 48 extreme rays and 48 irredundant facets.

Put w_i=v_i/Drow[i,i]. The following 48 explicit four-coordinate facet inequalities are NECESSARY AND SUFFICIENT for membership:

    for every signed-axis s and every i in G_s:
    3*w_i <= sum_{k in G_s} w_k.

All genuine tail snapshots after at least one tail transition have these inequalities (provided the six axis weights at the last transition are strictly positive). With axis weights zero the formula still gives a valid forward positive transition; image equality/invertibility requires strict positivity.

## Proof

PREFIX-587's exact native combinatorial identity S*R=W0 is a matrix identity: each signed current-axis group contributes J4-I4 and there are no cross-group entries. Therefore S=W0*R because R is an involution. Both R and positive Dcol(z) map the nonnegative orthant bijectively to itself. Consequently

    Q R_+ = Dx Drow W0 R_+.

For each signed-axis s, Dx acts on the entire corresponding four-coordinate block by the same strictly positive scalar x_|s|; it commutes with W0 and maps W0 R_+ onto itself, while Drow also commutes with Dx. Hence the latter cone equals Drow W0 R_+, independently of x and z.

Within a four-coordinate block, W=J4-I4 is invertible with W^-1=J4/3-I4. Thus w=W lambda with lambda>=0 if and only if

    lambda_i=(sum_{k in block}w_k)/3 - w_i >=0

for each of the four coordinates. Multiplying by 3 yields exactly the 48 displayed inequalities. Since W is invertible, the 48 transformed coordinate generators are linearly independent extreme rays, and their 48 dual coordinate inequalities are irredundant facets. To witness irredundancy, on any one block set w=(4,1,1,1) with nonnegative zeros on all other blocks; the 4-coordinate fails precisely the selected inequality while the other three local facet inequalities hold strictly.

## Theorem 598.2: four-local exact inverse and integer predecessor

For fixed x_a>0,z>=0, the PREFIX-596 determinant

    det Q=2^46 * 3^12 * (z+3) * product_{a=1}^6 x_a^8 > 0

ensures Q is invertible. Its inverse is explicitly

    Q^-1=Dcol(z)^-1 * R * W0^-1 * Drow^-1 * Dx^-1.

Given any current rational or real v, calculate

    b_i=v_i/(Drow[i,i] * x_|c_i|).
    lambda_i= (sum_{k in G_(c_i)}b_k)/3 - b_i.
    u_j=lambda_(rho(j))/Dcol(z)[j,j].

Then u=Q^-1 v is the UNIQUE previous compact 48-state vector. Every output u_j depends on only four coordinates of v in a single signed-current-axis group. The 48 facet inequalities are equivalent to u_j>=0 for all j. For nonnegative integer original weights and candidate integer current state v, v has a previous nonnegative INTEGER compact tail state if and only if these 48 explicitly recovered fractions are all nonnegative integers. This yields complete local nonnegative-integral predecessor tests for each fixed positive integer x and nonnegative integer z.

This predecessor theorem concerns the single 48-state tail step from arbitrary nonnegative compact input. A backwards extension into the original unrestricted 96-port initial state additionally requires the separate PREFIX-595 first-step image condition.

## Explicit counterexample: parity and port positivity are insufficient

Let z=1 and take v with v[2]=2 and all other entries zero. PREFIX-597's instantaneous 96-port decoder has delta=0; it returns a nonnegative integral original 96-port vector because all other phase pairs split evenly. Nevertheless the signed-current-axis block containing coordinate 2 has w_2=1 and all other w_i=0, so its cone inequality reads 3<=1 and fails. Hence for every x_a>0 and every nonnegative z this v has no nonnegative 48-tail predecessor (for z=1 it also passes the PREFIX-597 parity/port-readout test). This is an exact counterexample to sufficiency of the simple decoder's integrality and port-positivity conditions for dynamic reachability.

## Executed self-contained original-native validation

Companion certificate PREFIX598_R2_parameter_independent_image_cone_certificate.py reconstructs all 48 phases, successor relation, reversed phases, 12 four-phase signed-current-axis groups and native Q from original four STAR triples. It checks every one of 2304 entries in S R=W0, all 48 irredundant-facet witnesses, and 720 exact rational forward/inverse/facet runs at gate z=0,1,2,5 with positive axis weights. In particular 360 arbitrary nonnegative integer candidate v satisfy exact equivalence of all facet signs and Q^-1 v >=0, and the explicit v[2]=2 counterexample is checked. The locally executed program returned ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED. Finite tests verify the implemented native model; general parameter claims follow from the displayed exact factorization and algebraic proof.

## Next scientific units

(1) Characterize the integer points of this parameter-independent cone and the weight-dependent integer predecessor congruences. (2) Implement an end-to-end, input/output- and bit-cost-accounted benchmark comparing optimized original 96-port propagation and 48-state propagation with PREFIX-597 instantaneous snapshot decoding. (3) Test separate preservation of ordered-path and provenance-sensitive BRC observers, with a necessary repair coordinate or exact non-factorization witness.

No P000 changes; no formal Task CLAIM, native Result or independent mathematical review asserted.