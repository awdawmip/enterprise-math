# R5 — Arbitrarily many shared-gate bilinear products: affine-observer rigidity

Date 2026-11-04. AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother objective and frozen context
R5 seeks a strictly positive finite P/Q BRC whose COMPLETE four-observer convex hulls agree for FULL and seedless LR, while its actual real-policy images differ. The prior one-product affine theorem is at enterprise-math@1ae1db7defa9fea8c8016fda0ed1c08f3602f19e, research_notes/brc_r5_one_product_affine_rigidity_20261104_t1840/RESEARCH.md. This new theorem covers an *auxiliary independent shared-gate occupancy geometry*, not a demonstrated full P/Q tree. Frozen scientific sources: Global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e; P000 and ACTIVE worldview unchanged.

## All-k theorem

Let k>=1, let V be any real vector space, and A,B_i,C_i in V. Define the actual behavioral images

F_k = { x A + sum_i(y_i B_i + z_i C_i) : 0<=x<=1, 0<=y_i<=1, 0<=z_i<=x },
L_k = { x A + sum_i(y_i B_i + x*y_i C_i) : 0<=x<=1, 0<=y_i<=1 }.

All i constraints are independent: there is no additional sum_i z_i<=x constraint. The same x is used in every bilinear product.

**Theorem.** The following are equivalent, for all real parameters and in every real observation dimension:

(1) conv(F_k)=conv(L_k);
(2) F_k=L_k as *actual real-behavior sets*;
(3) for every i, B_i=0, or C_i=lambda_i B_i for a real lambda_i>=0.

If (3) holds, every FULL point has an explicit LR realization with the SAME upstream x:

- for B_i=0 take y_i'=z_i/x when x>0 and y_i'=0 when x=0;
- otherwise take y_i'=(y_i+lambda_i*z_i)/(1+lambda_i*x).

The construction respects [0,1] and preserves each vector summand exactly. It includes zero vectors, dependent coefficients and degenerate dimensions.

## Analytic proof and quantitative exact separator

The FULL domain is a convex polytope. Its affine image F_k is compact convex; at x=0 its endpoint set is sum_i[0,B_i], and at x=1 its endpoint set is A+sum_i[0,B_i]+sum_i[0,C_i]. Every intermediate FULL state is a convex combination of two such endpoints, using z_i/x where x>0.

The LR map is multi-affine. For fixed x and y, its vector equals
(1-x)*sum_i y_i B_i + x*(A+sum_i y_i(B_i+C_i)).
Therefore conv(L_k) is the convex hull of sum_i[0,B_i] and A+sum_i[0,B_i+C_i]. In both cases the endpoint zonotope extremizers may be taken at 0/1 coordinates.

Choose any linear functional ell on the finite coefficient span, and put
a=ell(A), p_i=ell(B_i), q_i=ell(C_i),
S=sum_i max(p_i,0),
U=a+sum_i max(q_i,0),
D=sum_i[max(p_i,0)+max(q_i,0)-max(p_i+q_i,0)].

The exact supports, from the two endpoint families, are
h_F(ell)=S+max(0,U),
h_L(ell)=S+max(0,U-D).
Consequently the exact support gap is
Delta(ell)=min(D,max(0,U))>=0.

Each summand of D is zero when p_i*q_i>=0 and equals min(|p_i|,|q_i|)>0 when p_i*q_i<0. Also D(-ell)=D(ell), and
U(ell)+U(-ell)=Q:=sum_i |q_i|.

If some i has p_i*q_i<0 for an ell, then D>0 and Q>0. Among ell and -ell, at least one has U>=Q/2, giving the *quantitative strict separation*
Delta >= min(D,Q/2)>0.
This holds for every A: adjusting the shared upstream affine weight cannot remove the gap on both opposite support directions.

Thus hull equality requires ell(B_i)*ell(C_i)>=0 for every i and every ell. For B_i!=0, if C_i is linearly independent of B_i, choose ell(B_i)=1 and ell(C_i)=-1 and extend the linear functional to the finite coefficient span. If C_i=lambda_i B_i with lambda_i<0, choose ell(B_i)=1. Both violate the requirement. Therefore C_i=lambda_i B_i with lambda_i>=0. There is no restriction on C_i when B_i=0.

Conversely under this alignment, the formulas for y_i' above satisfy 0<=y_i'<=1 since 0<=z_i<=x, and
y_i'B_i+x*y_i'C_i=(y_i+lambda_i*z_i)B_i
when B_i!=0, or x*y_i'C_i=z_i C_i when B_i=0. Summing proves F_k subset L_k; the reverse inclusion is immediate. Hence (3)=>(2)=>(1)=>(3).

For V=R^d with sup norm, if a FULL point W maximizes ell_n, then
dist_infinity(W, conv(L_k)) >= Delta(n)/||n||_1
by the l1/linfinity duality inequality.

## Explicit two-product cross-coupled example

A=(2,1), B1=(1,0), B2=(0,1), C1=(0,1), C2=(1,0).
For n=(1,-1), direct integer computation gives S=1, U=2, D=2, h_F=3, h_L=1, gap=2. The FULL point W=(4,1) is realized by x=1,y1=1,y2=0,z1=0,z2=1; n.W=3. Hence its distance in sup norm from the entire LR convex hull is at least 2/2=1. Both products are genuinely cross-directional.

Equality illustration with two nonzero products: A=(2,-1), B1=(1,0), C1=(2,0), B2=(0,1), C2=(0,3). The exact formulas y1'=(y1+2z1)/(1+2x) and y2'=(y2+3z2)/(1+3x) preserve all real points.

## Executed finite evidence

The accompanying Python standard-library verifier was actually executed. It exhausts all 9^5=59,049 tuples of 2-component integer vectors A,B1,B2,C1,C2 with coordinates in {-1,0,1}. For each it builds the exact 8 endpoint LR observations and 20 endpoint FULL observations; integer monotone-chain hull membership (including 0D and 1D degenerate cases) exactly tests equality. It checks the analytic vector alignment criterion for each tuple and independently verifies both support formulas on four signed coordinate axes.

Observed: 5,625 equal hulls, 53,424 strict hulls, zero mismatches. It also verifies 2,048 three-product Fraction behavior reconstructions including B_i=0, and the explicit cross-coupled separating certificate. All assertions pass. Output marker: PASS_EXACT_R5_ALL_K_COMMON_X_MULTIPRODUCT_AFFINE_RIGIDITY. The finite check is complete *only within its 59,049-element box*; the all-real/all-k claim is proved analytically above. This is author verification, not independent review or canonical mathematical admission.

## Scope and discriminating continuation

The theorem applies to the specified independent z_i in [0,x] relaxation and arbitrary affine readout. It does not classify competing-child flows with sum_i z_i<=x, two linked upstream resources, free terminal P/Q declaration fibers, or all BRCs. It gives a rigorous reason not to repeat mere independent-product affine observer searches. The R5 mother problem remains open.

Next: derive a strictly positive finite P/Q BRC where child capacities compete, keep source/route and all time-likelihood keys, and permit free stopping and terminal P/Q declarations. Enumerate all complete four-observer deterministic FULL and LR vectors. If convex hulls agree, prove a real-behavior non-membership point using its polynomial constraints; otherwise retain the exact rational Farkas separator. Preserve P000, ACTIVE worldview, frozen pins, and actual admission/ownership authority.
