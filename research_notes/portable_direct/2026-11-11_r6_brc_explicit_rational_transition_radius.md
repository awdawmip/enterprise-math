# R6 BRC: explicit rational neighborhood of monotone diagonal-edge slot crossover

Status: AUTHOR_DERIVED / EXACT_INTEGER_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-676 at commit cd2c6681a6ed4857bb7d416e82a8642f6cc0739f; exact local transition jets and threshold at commit d344451396a9bace91a9cbcdb14475c6641a9223.
Observer/ontology: scalar p,z are observer probabilities of frozen Heartbeat World X6 first-stop dynamics, not primitive native spatial coordinates. This argument does not alter P000, research tasks, claimant ownership, or admission status.

## Statement

Let Y(p,z)=max(Y_p,Y_z) for two independent Poissonized first-stop clocks from the 189-level frozen survivor model. Define V_q=q² Var[Y(p,z)]-q E[Y(p,z)]. Let

A(z)=Delta_W(z)=W(z,z)-W(0,z),
B(z)=Delta_mu(z)=mu(z,z)-mu(0,z),
D(q,z)=V_q(z,z)-V_q(0,z)=q(q A(z)-B(z)),
q0(z)=B(z)/A(z) where A(z)>0,
R(z)=B'(z) A(z)-B(z) A'(z).

Put b=53/1000 and rho=1/40,000,000,000. Then throughout the entire CLOSED rational interval I=[b-rho,b+rho]:

A(z)>42/100, R(z)>1000, 17<q0(z)<19, and q0'(z)=R(z)/A(z)^2>0.

Consequently q0 maps I strictly monotonically onto J=[q0(b-rho),q0(b+rho)]. For EVERY real q in J, there is exactly one z in I satisfying D(q,z)=0. For q in the interior of J, D(q,z)>0 to the left of that root, and D(q,z)<0 to its right. The endpoints of J lie in (17,19), hence inside the studied [12,24] slot range.

This proves an EXPLICIT interval of uniqueness for the diagonal-edge crossing, unlike the existence-only PREFIX-676 result or the previous implicit-function local-neighborhood assertion. It does not establish uniqueness over the full (13/250,27/500) interval or identify the global two-parameter maximum.

## Universal derivative bounds (exact integer proof)

Every s_n(x)=sum_k A_n(k)x^k(1-x)^(n-k), 0<=n<=188, has Bernstein coefficients c_n,k=A_n(k)/binom(n,k) in [0,1], because survivor multiplicities are a subset of the binom(n,k) full paths. Therefore, for x in [0,1],

|s_n|<=1, |s_n'|<=n<=188, |s_n''|<=2n(n-1)<=70312.

Let N=189, M=188, D2=70312. In the exact maximum-moment formulas from PREFIX-676, let K_nm=binom(n+m,n)/2^(n+m+1), and J_nm=(n+m+1)K_nm/2. These weights satisfy K_nm>=0, sum_m K_nm<=1 (from the complete negative-binomial series), sum_nm K_nm<=N, and 0<=J_nm<=189 K_nm.

For both parameter paths (p,z)=(z,z) and (p,z)=(0,z), the same triangle-inequality majorants apply, writing H(z)=E[Y(p,z)^2]/2:

|mu|<=3N=567;
|mu'|<=4NM=142128;
|mu''|<=N(4D2+2M²)=66515904;
|H|<=3N²=107163;
|H'|<=4N²M=26862192;
|H''|<=N²(4D2+2M²)=12571505856.

Since W=2H-mu², applying the product rule yields:

|W|<=2(107163)+567²=535815;
|W'|<=2(26862192)+2(567)(142128)=214897536;
|W''|<=2(12571505856)+2[(142128)²+(567)(66515904)]=140972783616.

Thus for differences A=W_diag-W_edge and B=mu_diag-mu_edge, throughout [0,1/2]:

|A'|<=429795072 =: L_A,
|B'|<=284256 =: L_B,
|A|<=1071630, |B|<=1134,
|A''|<=281945567232, |B''|<=133031808.

A crucial cancellation holds:
R'=B''A-BA'' (the two B'A' terms cancel).
Hence

|R'| <= (2*66515904)(2*535815)+(2*567)(2*140972783616)
      = 462287149648128 =: L_R.

These are complete finite uniform bounds for all real z in [0,1/2], with no sampling-based extension.

## Rational center inequalities and radius test

The companion previous 189-layer Fraction jet certificate at b verified the strict premises

A(b)>11/25, B(b)>789/100, B'(b)>128, -A'(b)>1680.

Therefore R(b) > (11/25)*128+(789/100)*1680=332788/25=13311.52.

For |z-b|<=rho, the mean-value theorem and the uniform derivative bounds give

A(z)>11/25 - L_A*rho = 67071113/156250000 > 42/100,

R(z)>332788/25 - L_R*rho = 274115821687/156250000 >1000.

Finally, B(z)>789/100-L_B*rho, B(z)<79/10+L_B*rho, and A(z)<441/1000+L_A*rho (the last pointwise upper bound comes from the exact floor at b). Direct exact integer comparisons give

789/100-L_B*rho > 17(441/1000+L_A*rho),
79/10+L_B*rho < 19(11/25-L_A*rho).

Thus 17< B(z)/A(z)<19 throughout I. Since A>0 and R>0 on the ENTIRE interval, q0'(z)>0 and the continuous one-root conclusion follows by strict monotonicity and the intermediate-value theorem.

## Verification scope and future action

The second accompanying Python checker uses integers and Fraction to verify every displayed majorant and strict radius inequality. It does not re-run the 189-level count recursion; its pointwise premises are supplied by the separate exact local-jet certificate in the previous immutable commit. Neither this author check nor Git storage is an independent review or Foundation acceptance.

Next: increase rho by computing local, rather than worst-case global, derivative Bernstein bounds; then certify sign/number of diagonal-edge roots over the larger PREFIX-676 bracket, and integrate a sign-correct pruning rule into full two-parameter V_q maximization.
