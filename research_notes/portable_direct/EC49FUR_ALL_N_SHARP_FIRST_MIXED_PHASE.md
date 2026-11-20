# EC49FUR — A sharp all-n first mixed phase and unique endpoint least-favorable law

Date: 2026-11-20 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.

## Source and scope

Independent portable continuation of EC49FUQ@96ad7a2c22c274446e74906c48bc6e3234a39436 (PR #2846), EC49FUO@8df5788adcd977cc809a0e27da180833317e3dfa (uniform threshold rearrangement), and EC49FUG (n<=14 endpoint optimality). Frozen BRC16943 scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. These statements concern the *lossy clipped-price binary count observer*, not a lossless identification with native X6 signed states, joint source labels, provenance, or future observations. P000/Heartbeat World and joint-observer preservation remain upstream.

For integer n>=15, and a shared nuisance theta in the compactified interval [0,theta_E], the two equally likely hypotheses yield binomial counts with Bernoulli probabilities
\[
p_\theta=1-T_\theta,\qquad q_\theta=1-u(\theta)T_\theta,\qquad
\beta=\frac3{637},\quad \theta_E=\frac{31597745}{1653649},
\]
\[
u(\theta)=\frac{21829245984}{45529434409-456083905\theta},
\qquad T_\theta(x)=(1-x)(1-\beta x+\beta x\theta),\quad 0<x<1.
\]
The theta=0 endpoint compactifies the original negative-infinite nuisance tail. Put
\[
a=u(0),\quad b=u(\theta_E),\quad c=\beta\theta_E,\quad d=\beta(\theta_E-1)=c-\beta.
\]
All constants are exact rationals. In particular
\(47/100<a<1/2,\ 59/100<b<3/5,\ b/a>6/5,\ c>89/1000,\ 0<d<43/500,\ \beta<1/200.\)

## Theorem — all sample sizes n>=15 have a genuine two-atom phase

Define
\[
\rho_n=\left(\frac{1-a^n}{1-b^n}\right)^{1/n},
\qquad s_n=\frac{\rho_n-1}{d+\beta\rho_n},
\qquad t_{n,u}=\frac{1-u^{n-1}}{1-u^n}.
\]
Let z_n and e_n be the unique positive roots in (0,1) of
\[
T_0(z_n)=t_{n,a},\qquad T_{\theta_E}(e_n)=t_{n,b}.
\]
Then, for **every integer n>=15**, without any numerical extrapolation,
\[
\boxed{0<z_n<s_n<e_n<1.}
\]
For each such n an epsilon_n>0 exists so that throughout the nonempty real open interval
\[
\boxed{s_n<x<s_n+\epsilon_n<e_n}
\]
the **unique compactified least-favorable nuisance law has exactly two support atoms, theta=0 and theta=theta_E, with strictly positive weights**. The unique optimal binomial-count decision accepts the right hypothesis at K>=2, rejects at K=0 and accepts with a strict probability gamma_n(x) in (0,1) when K=1.

For endpoint t in {0,theta_E}, define its signed count masses and tails
\[
\Delta_t(k)=P_{q_t}(K=k)-P_{p_t}(K=k),\quad
A_t=\sum_{k=1}^n\Delta_t(k)=T_t^n(1-u(t)^n),
\]
\[
B_t=\Delta_t(1),\quad C_t=A_t-B_t=\sum_{k=2}^n\Delta_t(k).
\]
On the stated interval, B_0<0<B_E, A_0<A_E and C_0>C_E. The exact solution is
\[
\boxed{\gamma_n(x)=
\frac{C_E-C_0}{B_0-B_E}
=1-\frac{A_E-A_0}{B_E-B_0}\in(0,1),}
\]
\[
\boxed{\lambda_E(x)=\frac{-B_0}{B_E-B_0}\in(0,1),
\quad \pi^*=(1-\lambda_E)\delta_0+\lambda_E\delta_{\theta_E},}
\]
\[
\boxed{V_n(x)=\frac{1-C_0-\gamma_n(x)B_0}{2}.}
\]
Here E subscripts denote theta_E.

### Proof 1: exact ordering of the three landmarks, uniformly in n

Both T_0(x)=(1-x)(1-beta*x) and T_E(x)=(1-x)(1+d*x) strictly decrease from 1 to 0. The endpoint tail ratio A_E/A_0 increases strictly with x, and equals one only at s_n. Direct expansion gives
\[
B_t=nT_t^{n-1}\{T_t(1-u(t)^n)-(1-u(t)^{n-1})\}.
\]
Therefore B_0<0 after z_n, and B_E>0 before e_n.

First, rho_n>=1 and
\(\rho_n^n=(1-a^n)/(1-b^n)<1/(1-b)<5/2\), so rho_n<5/2.
Hence d+beta*rho_n<43/500+(1/200)(5/2)<1/10. The finite geometric identity gives
\[
\rho_n-1=\frac{(b^n-a^n)/(1-b^n)}{\sum_{i=0}^{n-1}\rho_n^i}
\ge\frac{b^n-a^n}{n(1-a^n)}.
\]
For n>=15, (a/b)^n<(5/6)^15<1/2, so
\[
s_n>\frac{10(b^n-a^n)}{n(1-a^n)}>\frac{5b^n}{n}.
\]
As 1-T_0(x)>=x, the root z_n satisfies
\[
z_n\le\frac{(1-a)a^{n-1}}{1-a^n}<2a^{n-1}.
\]
Exact inequalities a>47/100, b/a>6/5, and (6/5)^15>600/47 imply (6/5)^n>40n/47 for every n>=15 by induction (6/5>(n+1)/n). Hence 5b^n/n>2a^{n-1}. This proves z_n<s_n.

For the other inequality, the geometric identity also yields
\[
s_n<\frac{b^n}{nc(1-b^n)}.
\]
At the E endpoint, 1-T_E(x)=(1-d)x+dx^2<=x, whence
\[
e_n\ge\frac{(1-b)b^{n-1}}{1-b^n}.
\]
Consequently s_n<e_n whenever n>b/[c(1-b)]. The exact rational bounds b<3/5 and c>89/1000 give
\[
\frac{b}{c(1-b)}<\frac{3000}{178}<17.
\]
This proves s_n<e_n for all n>=17. For the two remaining integers, rational substitution at (n,x)=(15,1/3500) and (16,1/6000) verifies **both** A_E(x)>A_0(x) and B_E(x)>0. Since A_E/A_0 increases strictly, these two witnesses certify s_n<x<e_n, so n=15,16 also follow. All checks use exact fractions in the companion program.

### Proof 2: primal and dual saddle; uniqueness of the least-favorable law

At x=s_n, A_0=A_E and B_0<0<B_E, so C_0-C_E=B_E-B_0>0. Continuity supplies an epsilon_n>0 on whose right-neighborhood these three strict conditions persist, A_E>A_0, and A_E-A_0<B_E-B_0. Therefore 0<gamma_n<1, and endpoint advantages for the displayed test are exactly equal. The displayed endpoint mixture has 0<lambda_E<1 and mixed signed count mass at K=1 exactly zero.

EC49FUO proved a strict common gap max_theta p_theta < min_theta q_theta for every 0<x<1. Select reference r between them. Relative to Bin(n,r), the mass ratio Bin(n,q_theta)/Bin(n,r) strictly increases with K, whereas Bin(n,p_theta)/Bin(n,r) strictly decreases. Hence their difference, and any positive endpoint mixture of such signed differences, strictly increases in K. As the displayed mixture vanishes at K=1, its signed masses are negative at K=0 and positive at every K>=2. Thus the test is a Bayes best response to the endpoint mixture, with exactly the same value as its two endpoint advantages.

EC49FUQ proves by log-concave integration (Prékopa) that every such threshold test has D_theta>=min(D_0,D_E) for the *entire compactified nuisance interval*. The constructed primal test and dual mixture therefore form a full minimax saddle, including the full-bit randomized test class (the count statistic is sufficient for the i.i.d. Bernoulli hypotheses).

Moreover the nuisance law is unique. For our interior-randomization test the derivative-integrand h_gamma(t)>0 on (0,1), the lower integral bound p_theta is affine, and the upper bound q_theta is strictly concave in theta. For every 0<s<1, q_{sE}>(1-s)q_0+s q_E. Replacing the upper bound by its smaller affine chord, applying Prékopa to the convex *linear* strip, and using strict positivity of h_gamma gives
\[
D_{sE}(\phi)>D_0(\phi)^{1-s}D_E(\phi)^s=D_0(\phi)=D_E(\phi).
\]
Thus every dual optimizer is supported only at the two endpoints. Neither pure endpoint is least favorable: B_0<0<B_E and 0<gamma<1 give each pure endpoint a strictly better Bayes response. Any dual optimum must make count K=1 indifferent, so its endpoint-E weight is uniquely -B_0/(B_E-B_0), strictly inside (0,1). Similarly, endpoint advantage equalization fixes gamma uniquely. The zero atom lives in the compactification; the original finite-parameter game has the same supremal-risk value by continuity.

### Proof 3: asymptotic landmark separation

As n tends to infinity with 0<a<b<1, elementary log and exponential expansions yield
\[
s_n\sim\frac{b^n}{cn},\qquad
e_n\sim\frac{(1-b)b^{n-1}}{1-d},
\qquad
\boxed{\frac{s_n}{e_n}\sim
\frac{b(1-d)}{c(1-b)}\frac1n
\approx\frac{14.8068998155}{n}.}
\]
This concerns the two landmark widths. The established mixed phase is a nonempty right-neighborhood of s_n; the claim that **the entire** (s_n,e_n) is mixed is left open.

## Exact validation

The companion standard-library Python Fraction program checks all rational bounds used above; n=15/16 exact width sandwiches; and five complete endpoint saddle certificates, including comparison against every binomial threshold candidate at the indicated exact rational width:

| n | x | gamma at K=1 | endpoint-E weight | risk |
| ---: | ---: | ---: | ---: | ---: |
| 15 | 1/3500 | .998072438857 | .967372182434 | .002152842925 |
| 16 | 1/6000 | .994667477139 | .952791615746 | .001335053553 |
| 17 | 1/10000 | .989262253198 | .964123237490 | .000846397252 |
| 18 | 1/18000 | .990947885592 | .906676038275 | .000498627032 |
| 20 | 1/50000 | .982183239401 | .928138119305 | .000197610381 |

Local execution result: PASS. The universal theorem is established analytically; the five exact finite checks verify particular witnesses, not an extrapolated all-n claim. Together with EC49FUG's previously author-proved n<=14 endpoint-optimal statement, n=15 is the **sharp first** observation count requiring a genuine two-atom least-favorable law at some width, and such a phase occurs at every n>=15.

## Identity, evidence status and next problem

Historical predecessor author: EM-DIRECT-8454C6; SID MCP-44cfc4e6f2094f96861854ebefc77e84 (provenance, not a current private capability). This independent GitHub portable publication makes no formal TASK/CLAIM/PROGRESS/RESULT/REVIEW, Activity, or P000/Foundation acceptance claim. Independent mathematical review is NOT_REVIEWED.

Next: determine the full right edge of the first mixed phase for arbitrary n, including whether it always equals e_n, and test higher-count mixed-phase transitions with exact endpoint algorithms. Source-labeled BRC/X6 joint residual data remain separate from the lossy bit-count projection.
