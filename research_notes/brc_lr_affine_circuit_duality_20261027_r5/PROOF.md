# R5 — Triple-circuit duality for likelihood-ratio affine curvature

Date: 2026-10-27; status: PORTABLE AUTHOR / UNREVIEWED / NOT_ADMITTED. Exact external finite P/Q sequential-observer mathematics, with a declared X6 native-cell path embedding. No native physical dynamics, Source CLAIM, Result, or independent review is asserted.

Frozen GLOBAL_KNOWLEDGE_V1: main@63642a91a9dc85e64eef6f87e182fbc53acd9ca3. P000 projection checked against canonical original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview and TASK/code/math routes applied. Frozen project input: enterprise-math@22b7983f19d7ed08b7ae291a8be0de9296aa4415, AGENTS, P000, native X6/time, joint-observer, portable/autonomous protocols. Mathematical source: research_notes/brc_lr_adjoint_curvature_20261027_r5/PROOF.md at 36d0691727cc281115e83709465b375cfb207c5f. Native owner query returned CONTROL_QUOTA, hence registration/progress below is author-only, not a CLAIM.

## Typed carrier and question

T0_BRC exact positive Q/P branch masses and ordered path provenance, plus T6_OPERATION_SAFE_QUOTIENT observer-safe compression, are REUSE_APPLIED. A hidden-kernel difference is a signed *observable error functional*, not a positive BRC mass. The observer is (t,R_t) during seedless LR policy choice and (tau,R_tau,D) at stopping, with permitted future stop/continue/declare actions. This work studies the affine-curvature residual in the predecessor's finite-horizon adjoint identity, not primitive heartbeat evolution.

For distinct ordered real y_1<...<y_m and real continuation values v_i, set

  rho_Y(v) = min_{A,B real} osc_i(v_i-A-B*y_i)
           = min_B [max_i(v_i-B*y_i)-min_i(v_i-B*y_i)].

## Theorem A: exact dual LP and universal triple-circuit formula

For m>=3,

  rho_Y(v)=max_{i<j<k} |[(y_k-y_j)/(y_k-y_i)]*v_i - v_j
                          +[(y_j-y_i)/(y_k-y_i)]*v_k|.        (A)

For m<=2 the residual is zero. Equivalently,

  rho_Y(v)=max {z·v: sum z_i=0, sum y_i*z_i=0, TV(z)<=1},    (B)
  TV(z)=(1/2)*sum |z_i|.

A normalized signed triple circuit z^(ijk) has coordinates
  z_i=(y_k-y_j)/(y_k-y_i), z_j=-1, z_k=(y_j-y_i)/(y_k-y_i),
and all remaining coordinates zero. Its total mass and y-first moment are zero and its TV is one.

**Proof.** The primal finite LP minimizes h-l under l<=v_i-B*y_i<=h. Its Lagrange multipliers p_i>=0 on the upper inequalities and q_i>=0 on the lower inequalities yield sum p_i=sum q_i=1 and sum y_i(p_i-q_i)=0; the dual payoff is sum(p_i-q_i)v_i. Set z=p-q. Conversely any z in (B) is p-q for such probability vectors: add a shared nonnegative mass of size 1-TV(z) to the positive/negative parts of z. The feasible bounded finite primal has strong LP duality, proving (B). Every nonzero vertex of the dual polytope has TV(z)=1, since otherwise small positive and negative scalings preserve feasibility. On a fixed sign orthant, a supported vector with more than three nonzero entries admits a two-sided nonzero perturbation preserving the three equalities sum z=0, sum y*z=0, sum sign(z)*z=2, contradicting extremality. Distinct y prohibit nonzero support of size one or two. A zero-mass, zero-first-moment vector on three ordered support points is unique up to scale and has middle sign opposite both endpoints. TV normalization makes it precisely ±z^(ijk). Linear maximization occurs at such a vertex. Taking both signs proves (A); affine interpolation proves m<=2. QED.

**Exact rational primal certificate.** For each i<j put d_ij=y_j-y_i and s_ij=(v_j-v_i)/d_ij. With R=the triple maximum in (A), primal attainment implies all intervals [s_ij-R/d_ij,s_ij+R/d_ij] intersect. Taking B=max_{i<j}(s_ij-R/d_ij) and A=min_i(v_i-B*y_i) yields 0<=v_i-A-B*y_i<=R for every i. A maximizing signed triple is the matching dual lower certificate. For rational y,v, these are fully rational verifiable primal/dual witnesses.

## Corollary B: exact signed-objective chamber fan and zero subspace

For fixed rational suffix policy, v_i(lambda)=lambda·F_i with F_i in Q^d. Put H_ijk=((y_k-y_j)/(y_k-y_i))*F_i-F_j+((y_j-y_i)/(y_k-y_i))*F_k. Then

  rho(lambda)=max_{i<j<k}|lambda·H_ijk|.                     (C)

Thus rho is a rational polyhedral seminorm on signed coefficient space, with chambers defined by finite inequalities selecting one signed dominating triple. Zero curvature is equivalent to v_i being affine in y_i on the entire support; it is enough to check the m-2 outer-endpoint chord equations

  lambda·[F_j - ((y_m-y_j)/(y_m-y_1))*F_1
               - ((y_j-y_1)/(y_m-y_1))*F_m]=0, 2<=j<=m-1. (D)

The codimension is the rank of these chord vectors, at most min(d,m-2). This is fixed-policy observer algebra, not a global optimum/hull certificate.

## Example C: predecessor's three LR levels, all signed coefficients

For Y=(1/2,1,3/2), terminal D=Q only at y=1/2, D=P otherwise, and signed lambda=(a,b,u,v0), terminal continuation values are (a/2,b,b)+3u*Y+3v0*1. Formula (A) gives rho=|a-2b|/4 for **all real signed lambda**, not merely a tested grid. The fixed-policy predecessor observer difference (7/1024,-7/512,0,0) gives J_full-J_bar=7(a-2b)/1024, while its actual-kernel bound equals (1/2)*(11/16)*(7/88)*rho=7|a-2b|/1024. Thus the curvature bound saturates in every signed direction for that fixed projection, including zero at a=2b. This does not establish support-function equality or inequality for globally optimized policies.

## Example D: eight strictly positive X6-embedded leaves; two active triple circuits

Select a native X6 chart Cell anchor o and six signed primitive native axes e_1,...,e_6. At separately typed times t=0,1,2 the eight **ordered unit-step paths** are o -> o+e_h -> o+e_h+e_{j+2} for h in {1,2} and j in {1,2,3,4}. All eight terminal Cells are distinct in Z^6; no plane or primitive diagonal is used. This is a synthetic finite observer test on native X6 Cell paths; its probabilities do not assert a native heartbeat force/evolution law.

Each time-1 hidden history has P=Q mass 1/2 and LR=1. For Y=(1/2,3/4,5/4,3/2), let
 K_1=(1/8,3/8,3/8,1/8), K_2=(3/8,1/8,1/8,3/8).
Both are strictly positive, sum to one and satisfy sum_j Y_j*K_h(j)=1. The complete second measure is P(h,j)=Y_j*Q(h,j), hence all P/Q leaves are strictly positive and each measure normalizes to one. The fixed terminal decision declares Q at j=1,3; P at j=2,4. Full policy continues at time 1 with probabilities 3/4 on hidden history 1 and 1/4 on 2 (otherwise stops/P). Occupancy-averaged seedless LR projection continues with 1/2 on both histories. Exact observer vectors are

  O_full=(31/128,3/4,3/2,3/2)
  O_bar =( 7/32,3/4,3/2,3/2)
  O_full-O_bar=(3/128,0,0,0).                               (E)

Conditional continued kernels are K_full=(3/16,5/16,5/16,3/16) and K_bar=(1/4,1/4,1/4,1/4); Delta K=(-1,1,1,-1)/16, TV(Delta K)=1/8, and initial continued Q mass dc=1/2.

For signed (a,b,u,v0), terminal suffix values equal a*Y_j for j=1,3, b for j=2,4, plus 2u*Y_j+2v0. The four triple forms are exactly

 (1,2,3): 3a/4-b
 (1,2,4): 3a/8-3b/4
 (1,3,4): -9a/8+3b/4
 (2,3,4): -5a/4+b.

Therefore rho is their maximum absolute value for **all real signed coefficients**. At a=b=1, rho=3/8, and a primal certificate is A=1/4, B=1/2. Active negative circuits are z124=(3/4,-1,0,1/4) and z134=(1/4,0,-1,3/4); the kernel defect decomposes exactly as Delta K/TV(Delta K)=-(z124+z134)/2. Each active circuit maximizes (B), so the bound is **saturated**:

  J_full(1,1,0,0)-J_bar(1,1,0,0)
     =(1/2)*Delta K·(1/2,1,5/4,1)
     =3/128=(1/2)*(1/8)*(3/8).                              (F)

Different signed directions select different circuits: a=1,b=0 selects triple (2,3,4) with rho=5/4, while a=1,b=2 selects (1,2,3) with rho=5/4. The zero-curvature subspace is a=b=0, with u,v0 arbitrary: the first two coefficient forms have determinant -3/16.

## Evidence scope and next problem

The companion Fraction-only Python verification and its executed output check eight distinct X6 terminal Cell coordinates, normalized strictly positive P/Q masses, conditional means, policy observables, the exact primal/dual triple bound and signed-face equality, 625 rational signed quadruples for each of the 3- and 4-point formulas, and one independent five-point test. Equations (A)-(D) are proved universally by finite LP duality and vertex classification, not inferred from these finite checks. This study certifies fixed-policy projection error, **not** the stronger still-open question conv(O_LR)=O_full but O_LR != O_full.

Next: use the exact circuit/chamber filter on a new rational N>=3 model, enumerate complete-history and seedless-LR deterministic four-vectors and produce exact rational hull membership or separation certificates in every direction. Only if hulls coincide should one attempt real-semialgebraic nonattainability of a specific four-vector. Preserve positive-branch/signed-defect typing, native X6 observer scope, actual owner authority and independent review.
