# PREFIX-642-R6 — Poisson stopping-time cap and sevenfold two-parameter BRC valley strip

Date: 2026-11-09 (Asia/Shanghai). Research role: independent TASK_RESEARCH.
Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Proposition 642.1: uniform upper bound for the stopped Poisson maximum

In the fixed PREFIX-621/622 signed two-information-direction BRC statistical observer, each of the two independent unit-rate informative Poisson streams stops no later than its N=189th event; this follows from the exact extinction of the first-stop survivor state at layer 189. Let the corresponding two independent Gamma(N,1) arrival times be X and Z. The actual stopped times S1,S2 obey S1<=X and S2<=Z on the natural coupling. Thus Y=max(S1,S2) satisfies Y<=max(X,Z) pathwise.

Since X and Z are independent Gamma(N,1), both have mean N and variance N. Using max(X,Z)=(X+Z+|X-Z|)/2 and Cauchy-Schwarz,
  mu=E[Y] <= E[max(X,Z)] = N+(1/2)E|X-Z|
     <= N+(1/2)sqrt(E[(X-Z)^2]) = N+sqrt(N/2).
For N=189, N/2=94.5<100, so **mu<199** throughout the probability square [0,1]^2. This improves the previously used crude 0<=mu<=2N=378 without changing the statistical observer.

## Proposition 642.2: improved global mixed derivative

Reuse PREFIX-641's degree-refined Bernstein survivor derivatives and negative-binomial moments. For n from 0 to 188, the exact finite-sum envelopes are
  A=17766>=|mu_p|,
  B=4429656>=|mu_pp|,
  C=2250360>=|mu_pz|,
  D=631225980>=|mu_ppz|,
  E=35721>=|mu_z|,
  J=96451329744>=|H_ppz|,
where W=2H-mu^2 and F_q=W-mu/q. By differentiating twice in p and once in z, for all real q>=12 and p,z∈[0,1],
  |F_q,ppz| <=2(J+2AC+EB+mu*D)+D/q
             < 2(J+2AC+EB+199D)+D/12
             = **920566268685**.
The expression on the right is an exact integer (Python Fraction independently checks the identity); it is strictly below PREFIX-641's earlier 1146545169525.

## Theorem 642.3: uniform sevenfold width

Let I=[3/20,1/6], z0=19/128, and h=7/2^28=7/268435456. For every real p∈I, q∈[12,24], and z∈[z0-h,z0+h], the exact predecessor central-slice Bernstein envelopes PREFIX-639 and the new mixed bound imply
  **273 < mu_p(p,z) < 322**,
  **3000 < F_q,pp(p,z) < 72200**.

Indeed C*h<1 and (920566268685)*h<24100, so 274<mu_p(p,z0)<321 and 27100<F_q,pp(p,z0)<48100 extend by integration as claimed. PREFIX-631 proves F_q,p(3/20,z)<0<F_q,p(1/6,z) on the larger range z∈[37/256,39/256], covering the new strip. Consequently F_q(.,z) has a unique interior minimizer c(q,z) on I, smooth/real analytic in parameters by the implicit function theorem.

Furthermore, c_q=-mu_p/(q^2 F_q,pp)<0, so for the two actual BRC slots q=12,24,
  **91/577600 < c(12,z)-c(24,z) < 161/36000**.
Writing Phi(t,z)=min_{p∈I}(W(p,z)-t mu(p,z)), t=1/q,
  **273^2/72200 < -Phi_tt(t,z) < 322^2/3000**.
Thus the optimal-value function remains uniformly strongly concave and the minimizer-order theorem persists over the new strip. The second-parameter radius is seven times the PREFIX-640 radius 2^-28 and 7/4 times the PREFIX-641 radius 2^-26.

## Verification and next research unit

The companion executable Fraction certificate checks sixteen exact implications and constants. Executed locally on 2026-11-09: ALL_CHECKS_PASS 16. The gamma cap is an analytic inequality based on the 189-layer finite stop and independent unit-rate Poisson streams, while the rest is exact arithmetic applied to previously proven finite-observer identities and central Bernstein evidence. No new original 96-port native graph execution occurred; mathematical review and Source admission are pending.

Next: replace coarse global mixed derivative estimates with restricted two-variable Bernstein signs on the remaining second-parameter band. In particular inspect why the current global Lipschitz bound still forces h much smaller than 1/256, while the target entire z-band may remain positively curved. Preserve both possible exact positive certificates and exact sign witnesses as research evidence.

Provenance: PREFIX-621/622 first-stop and Poissonization; PREFIX-631 enterprise-math@cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6; PREFIX-639 enterprise-math@6acbf4f472a48d846859a71a31af243808961cff; PREFIX-641 enterprise-math@214586fa751216c77d5214bbf447b1bdfbb661d1.
