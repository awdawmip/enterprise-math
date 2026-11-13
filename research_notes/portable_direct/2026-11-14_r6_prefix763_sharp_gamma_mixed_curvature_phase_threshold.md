# PREFIX-763 / R6 — Sharp Gamma mixed-curvature phase threshold

Date: 2026-11-14. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_ANALYTIC_PROOF_AND_EXACT_RATIONAL_WITNESS / UNREVIEWED / NOT_ADMITTED.
Scope: external independent two-Gamma-clock auxiliary. No native X6 or three-dimensional-slice transfer is asserted.

## 1. Model and inherited exact results

Let T_x be the first-stop layer of the frozen 189-layer BRC kernel, with T_x at most 189. Given T_x=m, the independent clock C_x has the Gamma(m,1) law. Set Y(p,z)=max(C_p,C_z) for 0<=p,z<=1/2, mu=E[Y], M2=E[Y^2], Var=M2-mu^2, and V_q=q^2 Var-q mu for q>0.

Write S_i(x)=P(T_x>i), 0<=i<=188, and H_x(t)=P(C_x>t)=exp(-t) sum_i S_i(x)t^i/i!. PREFIX-755--757 establish that each polynomial S_i is symmetric under x->1-x, with S_i'(x)>=0 for 0<=x<=1/2. In particular, S_25(x)=1-x^25-(1-x)^25 has S_25'(x)=25[(1-x)^24-x^24]>0 on 0<=x<1/2.

## 2. Exact mixed-curvature factorization

For 0<=p,z<1/2 define U_p(t)=partial_p H_p(t), U_z(t)=partial_z H_z(t) and

- A=integral U_p(t)U_z(t) dt;
- B=integral t U_p(t)U_z(t) dt;
- u=partial_p mu=integral U_p(t)(1-H_z(t)) dt;
- v=partial_z mu=integral U_z(t)(1-H_p(t)) dt.

Each integral is over t from 0 to infinity. All are finite and strictly positive: U_p and U_z have nonnegative polynomial coefficients and the row-25 coefficient is positive. The independent-max survival identity is P(Y>t)=H_p+H_z-H_p H_z. Differentiating the finite Erlang sums and integrating yields

partial_pz mu=-A,
partial_pz M2=-2B,
partial_pz Var=-2(B+uv-mu A).

Define Theta(p,z)=B/A+uv/A-mu(p,z).

**Theorem 763.1.** On 0<=p,z<1/2 and for every real q>0,

partial_pz Var = -2 A Theta,
partial_pz V_q = q A (1-2q Theta).

Thus the sign of mixed variance curvature is the opposite of Theta; for Theta>0 the V_q mixed curvature switches at the unique pointwise q=1/(2Theta), while for Theta<=0 it is positive for all q>0.

## 3. Endpoint extension and explicit finite bounds

Symmetry gives S_i'(1/2)=0. Hence the quotient a_i(x)=S_i'(x)/(1-2x) extends polynomially to x=1/2 and is nonnegative on the closed half-interval. Crucially a_25(1/2)=600/2^23>0.

Put W_x(t)=exp(-t) sum_i a_i(x)t^i/i!, so U_x=(1-2x)W_x, and define A0=integral W_p W_z>0, B0=integral t W_p W_z, u0=integral W_p(1-H_z), v0=integral W_z(1-H_p). The representation Theta=B0/A0+u0 v0/A0-mu extends continuously to the compact square [0,1/2]^2 and attains a finite maximum Theta_max.

For 0<=i,j<=188 let K_ij=binom(i+j,i)/2^(i+j+1). Then

min K_ij = 2^-189, with equality exactly at (0,188) and (188,0).

Proof: K_(i+1,j)/K_(i,j)=(i+j+1)/(2(i+1)); for each fixed j, K increases then decreases as i increases, so its minimum is at an endpoint. Repeating in j reduces the global minimum to the four corners. K_00=1/2, K_(0,188)=K_(188,0)=2^-189, and K_(188,188)>=2^-189 since binom(376,188)>=2^188.

Let a=sum_i a_i(p)>0 and b=sum_j a_j(z)>0. Then A0=sum_ij a_i(p)a_j(z)K_ij>=2^-189 ab, while 0<u0<=a and 0<v0<=b. Further B0/A0 is a weighted mean of (i+j+1)/2, so B0/A0<=377/2. As mu>0,

Theta_max < 2^189+377/2.

## 4. Certified phase transition

The exact PREFIX-760 Fraction witnesses, reused by PREFIX-762, determine two rectangles:

R_minus=[0,1/4] in p times [0,1/4] in z;
R_plus=[0,1/4] in p times [1/4,1/2] in z.

On R_plus, the exact rectangular mixed variance difference is >155, so partial_pz Var is positive at some interior point. Thus Theta<0 somewhere.

On R_minus, exact subtraction of PREFIX-760's rational deltaVar and deltaV2 gives

Delta_Rminus Var = -527.252710710715...,
Delta_Rminus mu  = -100.180677622301...,

where these decimals are displays of exact Fractions. The accompanying checker verifies

Delta_Rminus V_(191/1000)<0

by exact Fraction comparison (approximately -0.10019671357808489). Hence partial_pz V_(191/1000) is negative at some interior point, giving Theta_max>1/(2*(191/1000))>0.

**Theorem 763.2 (sharp global phase).** Put q_c=1/(2 Theta_max). Then

1/(2^190+377) < q_c < 191/1000.

For every 0<q<=q_c, V_q is globally supermodular on [0,1/2]^2 (nonnegative mixed differences on every parameter rectangle). For every q>q_c, its mixed derivatives take both positive and negative values in the interior; hence V_q is neither globally supermodular nor globally submodular. For every q>0 it is not globally submodular.

Proof: Theta_max>0 and the uniform bound above give the strict q_c bracket. The factorization implies partial_pz V_q>=0 everywhere when q<=q_c. When q>q_c, some interior point has Theta>1/(2q), using continuity even if the maximum is attained only on the boundary; the mixed derivative is negative there. An interior point with Theta<0, certified by R_plus, has positive mixed derivative for every q>0. Integrating the mixed derivative over rectangles proves both signs and the supermodularity claim. QED.

Consequently every project-relevant q>=2 lies in the curvature-sign-changing phase. The new conclusion also proves the existence of a nonempty small-q regime of global supermodularity. No historical 1/768-cell exclusion area is added.

## 5. Reproduction and next frontier

The attached Python Fraction checker reuses the published PREFIX-760 full exact result (24,743 bytes, SHA-256 1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76), checks all 35,721 rational K_ij values and their minimum, reconstructs both rectangular mixed differences, and checks the negative exact 191/1000 witness. Local result: ALL_CHECKS_PASS PREFIX763. The continuous factorization and compactness argument are author-level analytic proofs; source Bernstein monotonicity and the 189-layer recurrence are inherited, not freshly rerun.

Next question: obtain a materially sharper bound or exact characterization of Theta_max from the pinned 189-layer coefficient kernel; explore whether its finite coefficient representation can contribute robust interval certificates on genuinely uncertified 1/768 parameter cells.
