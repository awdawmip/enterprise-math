# EC49AA — A universal quantitative post-wedge boundary certificate

**Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED (2026-10-29). Continuation of EC49Z [Draft PR #1680](https://github.com/awdawmip/enterprise-math/pull/1680), scientific commit a548fc7264e837f719ba753d851ff94ec78955ec. A native Researcher/Claim/Result/independent Driver authority was not obtained.

## Exact theorem and model

Fix the positive, source-labelled auxiliary BRC sensor law from EC49Z: histories w=0,1,2 have equal source-independent prior 1/3, paid first actions A0,A1 (unit cost), B0,B1 (cost 2), or STOP (cost 0). The first-action probabilities x_{wc} obey x_{wc}>=0, sum_c x_{wc}<=1, with h_w=1-sum_c x_{wc}. Each paid path sees a binary signal u with
\[
t_w(u)=\frac12+(2u-1)\frac{1-w}{200},\qquad \frac{99}{200}\le t_w(u)\le\frac{101}{200}.
\]
After (c,u) and erasure of w, the observer buys a second sensor S (cost 1) with probability s_{cu}; if bought, S produces z=0,1,2. Positive source laws are
\[
 P(w,u,z)=t_w(u)\left(\frac16{\bf1}_{w=z}+\frac1{12}{\bf1}_{w\ne z}\right),\qquad Q(w,u,z)=t_w(u)/9.
\]
Acceptance on sensed paths has probability a_{cuz}; STOP/no-S acceptance depends only on accessible observations. All behavioral conditional probabilities may be arbitrary real numbers in [0,1], and coins are fresh independent at each decision. In particular, no ex-ante seed persists as hidden memory. Both sources have exact stage costs C_1=43/48 and C_2=7/8. Define alpha=P(accept), beta=Q(accept), delta=alpha-beta.

**Theorem, universal over all legal real behavioral strategies:** for every delta>=0,
\[
\boxed{\alpha \ge 3\delta+\frac{2673}{3232}\max\left(0,\delta-\frac{17}{288}\right).}\tag{1}
\]
Consequently, at delta=1/16,
\[
\boxed{\frac{19689}{103424}\le \alpha_{\min}(1/16)\le\frac9{46}.}\tag{2}
\]
The right endpoint is attained by a rational causal strategy with (alpha,beta,C_1,C_2)=(9/46,49/368,43/48,7/8). The left is a rigorously certified lower bound, not an asserted attained minimum. This strengthens EC49Z's qualitative alpha>3delta beyond 17/288.

## Proof of the uniform inequality

Raw masses x and the following sums are **per-history** and omit the common 1/3 prior factor. Let
\[
a_w=x_{w,A0}+x_{w,A1},\quad b=\sum_{w,c\in\{B0,B1\}}x_{wc},\quad H=\sum_w h_w,\quad
T=\sum_{w,c}x_{wc},\quad m=\sum_{w,c,u}x_{wc}t_w(u)(1-s_{cu}).
\]
The two exact stage budgets imply
\[
T+b=3C_1=43/16,\qquad T-m=3C_2=21/8,
\]
hence b+m=1/16, 0<=b<=1/16 and
\[
H+b=3-T+b=\frac5{16}+2b\le\frac7{16}.
\]
For each w,
\[
a_w=1-h_w-b_w\ge 1-H-b\ge\frac9{16}.\tag{3}
\]
Thus every one of three historical states must occupy at least 9/16 mass in just two A labels.

Consider an accepted, second-stage sensed atom (c,u,z), and define its full-provenance masses
\[
v=x_{zc}t_z(u)s_{cu}a_{cuz},\qquad r=\sum_{w\ne z}x_{wc}t_w(u)s_{cu}a_{cuz}.
\]
Using the exact P and Q laws, **with their original 1/3 prior already incorporated into the above source laws**,
\[
\Delta_{cuz}=P(accept,c,u,z)-Q(accept,c,u,z)=\frac{2v-r}{36},
\quad \ell_{cuz}=3Q-2P=\frac r6.\tag{4}
\]
On a STOP or no-S path, the distributions of the available observation are the same under P and Q, so Delta=0 and ell=Q(atom)>=0. Thus delta=sum Delta and L:=3beta-2alpha=alpha-3delta>=sum_{sensed}ell>=0.

Fix a number
\[
0<\tau<\tau_*=\frac9{32}\frac{99}{101}=\frac{891}{3232}.
\]
Classify a sensed, accepted atom as **good** if v>0 and r<=tau v, and **bad** otherwise. For any good atom s_{cu}a_{cuz}>0, and for each w!=z positivity implies
\[
x_{wc}\le\tau\frac{t_z(u)}{t_w(u)}x_{zc}\le \kappa x_{zc},
\qquad \kappa=\tau\frac{101}{99}<9/32<1.\tag{5}
\]
A paid code cannot have good atoms centered at two distinct indices z,z': that would force x_{z'c}<=kappa x_{zc} and x_{zc}<=kappa x_{z'c} with both positive. Hence each paid code has at most one good history index across both signals u.

Both A codes cannot have good atoms: their two (possibly identical) good centers occupy at most two out of three histories, so choose a third w. Equation (5) gives x_{w,A0}<=kappa and x_{w,A1}<=kappa, whence a_w<=2kappa<9/16, contradicting (3). Thus at most one A code is good, with favorable full-provenance mass sum(v)<=1. The sum of the good favorable mass on B codes is <=b<=1/16. By Delta<=v/18, we obtain
\[
\sum_{\mathrm{good}}\Delta\le\frac{1+b}{18}\le\frac{17}{288}.\tag{6}
\]
Every bad atom with v>0 has r>tau v and Delta<=v/18<r/(18tau)=ell/(3tau); if v=0, then Delta<=0<=ell/(3tau). Consequently
\[
\sum_{\mathrm{bad}}\Delta\le\frac{L}{3\tau}.\tag{7}
\]
Unsensed atoms have Delta=0. Therefore delta<=17/288+L/(3tau), for every 0<tau<tau*. Passing to the limit tau up to tau*, and combining with L>=0, yields
\[
L\ge3\tau_*\max(0,\delta-17/288)=\frac{2673}{3232}\max(0,\delta-17/288).
\]
Since alpha=3delta+L, equation (1) follows. **This proof covers arbitrary real, causal, unseeded behavioral policies; the finite checker below is a reproducibility check of explicit identities only.**

At delta=1/16, delta-17/288=1/288, so the lower expression is 3/16+(2673/3232)/288=19689/103424.

## Exact rational upper witness

Take first-stage prefix rows in order A0,A1,B0,B1:
\[
x_0=(1,0,0,0),\quad x_1=(0,1,0,0),\quad x_2=(0,9/16,1/16,0).
\]
The unused 3/8 probability at w=2 is STOP. All paid histories buy S, so s_{cu}=1. Accept with probability 1 on (A0,z=0) and (B0,z=2); accept on (A1,z=1) with probability 2/23; reject all other paths. Terminal Bernoulli decisions are fresh and depend only on available code and z.

The pure diagonal pair contributes (alpha,beta,delta)=(17/96,17/144,17/288). The mixed A1,z=1 class has pre-thinning source masses
\[
P(A1,z=1)=41/192,\qquad Q(A1,z=1)=25/144,\qquad P-Q=23/576.
\]
Applying acceptance probability 2/23 adds delta=1/288, resulting in
\[
\alpha=17/96+(2/23)(41/192)=9/46,\qquad
\beta=17/144+(2/23)(25/144)=49/368,\qquad
\delta=1/16.
\]
The first sensor costs exactly 43/48 and the second exactly 7/8, source by source.

## Verification and scientific boundary

See VERIFY.py and EXACT_REPORT.json: actual executed standard-library Fraction calculations checked 18 positive normalized leaves per source, strict signal positivity, cost equalities, the exact rational witness, threshold and rational lower/upper enclosure. The universal claim follows from the analytic support-counting and atom inequalities above, not numerical sampling.

Typed BRC reuse consists of complete *positive source-labelled branch measures* retaining (w,c,u,z) provenance and observer fibers. The P-Q difference in (4) is a difference of probability measures, **not** a native signed BRC amplitude. No original signed/phase-BRC, native X6 three-axis-slice or Heartbeat World dynamics embedding is claimed. P000, joint-relation preservation and ACTIVE worldview remain unchanged. Review/admission/CLAIM must be handled by an independent authorized owner.

**Next EC49AB:** Determine exact alpha_min at delta=1/16 or narrow (2) using a polynomial/semi-algebraic certificate that retains all causal products x_{wc}s_{cu}a_{cuz}; also investigate the shape of the lower boundary beyond 17/288. See NEXT_TASK.md.
