# S23/AV: improved constructive asymptotic coefficient by padded count-strip decoding

Date: 2026-11-07. Status: author-side mathematical proof, independent review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: research_notes/brc_s23_av_uniform_count_log_sharp_20261107_r1/PROOF.md @1f70fb8850fc05be22b3fcf8070a14d5e39e2f30.

## Exact statistical model

For all real a,c in [1/2,7/8], set z=(1-a)c, b=(1-a)(1-c), s=1-z=a+b. A complete single-trial observation has ordered label law P=(a,z,b) on (1,3,4). The compressed observation B=(z,1-z) has binary symbols (Y,N). Across n repetitions the shared unknown (a,c) is fixed and trials are conditionally independent. Define delta_n as the infimum, over parameter-independent stochastic kernels L from {Y,N}^n to {1,3,4}^n, of the supremum over legal a,c of TV(P^tensor n,B^tensor n L). All complete ordered 3^n outputs are retained.

Let p=a/s. The two partial derivatives of p=a/[1-(1-a)c] are (1-c)/s^2 and a(1-a)/s^2, both positive. Therefore alpha=2/3 <= p <= beta=56/57, and h=beta-alpha=6/19.

## Constructive decoder and exact full-output formula

Given a compressed binary word, output label 3 at each observed Y position. Let m be the number of N positions. Put

w_m = ceil(sqrt(m log(m+2)))+1,
A_m=max(0,floor(alpha*m)-w_m),
D_m=min(m,ceil(beta*m)+w_m),
L_m=D_m-A_m+1.

Sample K uniformly from the L_m integers A_m,...,D_m; choose a uniformly random K-subset of the m N positions; output label 1 on the selected sites and label 4 at other N sites. This normalized kernel is independent of a,c, preserves Y positions and all output site ordering, and includes m=0.

The target and decoder have the same distribution of Y positions. Conditional on those positions, M=m and the count K, both laws are uniform among the C(m,K) arrangements of labels 1 and 4. Under the target K~Bin(m,p); under the decoder K~Unif({A_m,...,D_m}). Taking pointwise minima gives the *exact full ordered-output* overlap identity, for every n and every legal real a,c:

O_n(a,c):=1-TV(P^tensor n,B^tensor n L_strip)
=E_{M~Bin(n,s)} F_M(p),

F_m(p)=sum_{k=A_m}^{D_m} min{ C(m,k)*p^k*(1-p)^(m-k),1/L_m }.   (1)

The count reduction in (1) is justified by the exact matching conditional arrangement laws; no independence of decoded coordinates is assumed.

## Lemma: uniform leading coefficient for binomial-to-strip overlap

For p in the full closed legal interval [alpha,beta], uniformly as m->infinity,

F_m(p)=[2 sqrt(p(1-p))/h+o(1)] sqrt(log(m)/m).    (2)

Proof. Write v=p(1-p). Since the legal p interval is compact inside (0,1), v is bounded above by 1/4 and below by a positive constant. For large m, clipping at 0,m does not affect the strip endpoints, and L_m=h*m+O(sqrt(m log m)+1). For every fixed epsilon in (0,1), the strip includes every valid integer k with |k-mp| <= (1+epsilon)sqrt(m*v*log m), because the padding is asymptotic to sqrt(m log m) and (1+epsilon)sqrt(v)<1.

For |k-mp|=O(sqrt(m log m)), let q=k/m. Two-sided Stirling estimates for the binomial factorials and a Taylor expansion of binary relative entropy D(q||p) around p, uniform in p in the closed legal interval, give

log Pr(Bin(m,p)=k)
=-0.5 log(2*pi*m*q*(1-q))-m*D(q||p)+O(1/m)
=-0.5 log(2*pi*m*v)-(k-mp)^2/(2*m*v)+o(1).   (3)

The entropy expansion remainder is O((log m)^(3/2)/sqrt(m))=o(1) uniformly because q,p stay away from 0 and 1.

For inner radius r_-=(1-epsilon)sqrt(m*v*log m), (3) implies that the binomial probability at every integer inside the radius is at least c*m^[-1/2-(1-epsilon)^2/2], where c>0 is uniform. Since the exponent is strictly less than 1, these probabilities eventually exceed 1/L_m~1/(h*m). There are 2*r_-+O(1) such integers, so the overlap is at least [2(1-epsilon)*sqrt(v)/h+o(1)]sqrt(log m/m), uniformly.

For the outer radius r_+=(1+epsilon)sqrt(m*v*log m), at most 2*r_++2 central integers contribute up to 1/L_m each, and the contribution outside is no greater than the binomial tail. The Bernoulli Bernstein inequality gives

Pr(|Bin(m,p)-mp|>=r_+)
<=2*exp[-r_+^2/(2*(m*v+r_+/3))]
=m^[-(1+epsilon)^2/2+o(1)]
=o(sqrt(log m/m))

uniformly in p. Hence F_m(p) is at most [2(1+epsilon)*sqrt(v)/h+o(1)]sqrt(log m/m). Let epsilon tend to zero after m tends to infinity. This proves (2), including alpha and beta.

## Theorem: whole-box explicit decoder coefficient

Uniformly in real a,c in [1/2,7/8],

O_n(a,c)=[C(a,c)+o(1)]sqrt(log n/n),             (4)

C(a,c)=(2/h)*sqrt(p(1-p)/s)
=(2/h)*sqrt(a*(1-a)*(1-c)/[1-(1-a)*c]^3).

Indeed M~Bin(n,s) has s in [9/16,15/16]. Hoeffding bounds the probability of |M-n*s|>n^(2/3) by 2 exp(-2*n^(1/3)). On the complementary event M/n=s+O(n^(-1/3)), log M/log n ->1 uniformly. Insert the uniformly valid (2) into (1). On the exceptional event 0<=F_M<=1, so its contribution is o(sqrt(log n/n)). This proves (4).

Minimize g(a,c)=a*b/s^3 on the legal box. Its log derivatives are

d_a log g =1/a-1/(1-a)-3*c/s < 0,
d_c log g =-1/(1-c)+3*(1-a)/s=(2*b-a)/[(1-c)*s] <= 0,

since a>=1/2, b=(1-a)(1-c)<=1/4, hence 2*b<=1/2<=a. The minimum occurs at a=c=7/8, where z=7/64, b=1/64, s=57/64 and g=3584/185193. Uniformity of (4) allows taking the infimum over the whole box, giving

lim_{n->infinity} sqrt(n/log n)*inf_{a,c} O_n(a,c)
=C_*=(19/3)*sqrt(3584/185193)
=0.8810571160592926... .                              (5)

Equivalently the explicit decoder has
sup_{a,c} TV(P^tensor n,B^tensor n L_strip)
=1-[C_*+o(1)]sqrt(log n/n).

Because delta_n is the infimum over all admissible kernels, this immediately yields the constructive MINIMAX inequality

liminf_{n->infinity} sqrt(n/log n)*(1-delta_n) >= C_*.      (6)

This coefficient improves that of the preceding count-uniform decoder, 2*sqrt(3584/185193)=0.278228562966..., by the exact multiplicative factor 19/6. Equation (5) determines the leading coefficient of this concrete decoder, and (6) is a new lower bound on the optimal overlap; identifying the exact minimax coefficient is the next open question.

## Reproducible checks, provenance and scope

VERIFY.py uses Python standard-library arbitrary precision Fraction arithmetic, checks the exact identity (1) by independently enumerating full ordered 3^n outputs for n=2,3,4,5 at five legal rational parameter pairs, verifies both laws normalize, checks a rational corner-minimization grid, and evaluates exact overlaps at n=8,16,32,64 at a=c=7/8. RUN_EVIDENCE.txt is the actual output. All-real asymptotic claims (2)-(6) are proved analytically above, rather than inferred from finite tests.

The BRC observer/provenance discipline is used to retain label-3 positions and prove the declared full-output count factorization. This is a typed, source-conditional statistical auxiliary theorem, not a native six-axis Heartbeat/BRC-Shor arithmetic execution or a six-source, ten-label S23 mother-model result. The frozen scientific input, P000 worldview, joint relation preservation and task/Owner authority are unchanged.

Next: a z-adaptive strip based on the observed number of Y symbols, with a concentration-controlled widening to remain uniform over fibers and their endpoints; a matching fixed-fiber minimax dual lower coefficient; and a lawful source/time/observer bridge for the mother experiment. Formal CLAIM and independent mathematical review remain unconfirmed.