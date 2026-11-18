# S23 conditional AV: exact beta-binomial reconstruction and matching \(\sqrt{\log n/n}\) overlap rate

Date: 2026-11-06.
Status: AUTHOR_ANALYTIC_PROOF / EXACT_FINITE_CHECKS_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Parent auxiliary line: Draft PR #1777; predecessor constructive kernel at commit 165330941dcc42c594c222db0e01b418ea703aa2.
Current normative guidance was read separately from the frozen scientific source. Mother objective: original lawful ten-label S23 R_beh(k,10).

## Model and theorem

For real a,c in [1/2,7/8], let z=(1-a)c and q=(1-a)(1-c), and let P=(1-z-q,z,q) on the ordered tags (stop1,stop3,stop4). The compressed observation B=(1-z,z) records (other,stop3). In n independent trials all labels share the same unknown a,c. Let

delta_n = inf_K sup_(a,c) TV(P_(a,c)^{tensor n}, B_z^{tensor n} K),

with a single parameter-independent stochastic kernel K from compressed n-words to tagged n-words. Total variation is half of the L1 distance.

**New theorem.** There is an explicit, parameter-independent kernel K_n such that for all integers n>=20000,

1-delta_n >= (1/160)*sqrt(log(n)/n).

The earlier author-side multi-hypothesis Hoeffding certificate in this same PR yields for all n>=1000,

1-delta_n <= (28/3)*sqrt(log(n)/n)+2/n^2.

Consequently, for this *conditional tagged-AV auxiliary experiment*,

**1-delta_n = Theta(sqrt(log(n)/n))** as n tends to infinity.

The logarithm is natural. Both bounds concern all lawful real a,c, and the quantifier over K permits arbitrary correlated stochastic reconstruction.

## A universal kernel with no parameter estimation

Input: the compressed n-word y in (other,stop3)^n.
1. Copy every observed stop3 position directly into the corresponding output position.
2. Draw one shared latent R uniformly from [0,1], independently of y.
3. At every other position, independently conditionally on R, output stop4 with probability R, otherwise stop1.

This is a row-stochastic parameter-independent kernel on the correct tagged words. The shared R retains the hidden stop1/stop4 branch relation rather than sampling a fresh R for each position. It uses the observed stop3 locations without estimating z.

Write r=q/(1-z). In the lawful rectangle,

1/57 <= r <= 1/3.

Indeed, with x=1-a in [1/8,1/2], r=x(1-c)/(1-xc); it increases with x and decreases with c. Its extremal corners are (a,c)=(7/8,7/8) and (1/2,1/2). Also 1/16<=z<=7/16.

## Exact finite-n reduction

Conditional on a compressed word y containing m other positions, the true complete law fills those m positions with independent Bernoulli(r) labels (stop4 versus stop1), whereas K_n fills them using one shared R~Uniform[0,1].

Under K_n the count S of stop4 labels is *exactly uniform* on {0,...,m}:

Pr_K(S=s | y)=C(m,s)*integral_0^1 u^s(1-u)^(m-s) du
             =C(m,s)*s!*(m-s)!/(m+1)! =1/(m+1).

Under the true law S~Bin(m,r). Conditional on S and y, both the true law and K_n distribute the stop4 locations uniformly among the C(m,s) subsets. The y-marginals also agree exactly. Therefore, with M~Bin(n,1-z),

**1-TV(P^{tensor n}, B_z^{tensor n}K_n)
  = E_M [ sum_(s=0)^M min{ C(M,s) r^s(1-r)^(M-s), 1/(M+1)} ].**      (A)

This is an exact identity for every n>=1, including M=0.

## A uniform binomial-versus-uniform overlap lemma

**Lemma.** For any integer m>=10000 and any r in [1/57,1/3],

sum_(s=0)^m min{Pr(Bin(m,r)=s),1/(m+1)}
  >= (1/80)*sqrt(log(m)/m).                                      (B)

Proof. Write p_s=Pr(Bin(m,r)=s), mu=mr, and j=floor((m+1)r), a binomial mode. Its variance is mr(1-r)<=m/4. Chebyshev gives

Pr(|S-mu|<sqrt(m)) >= 3/4.

The interval contains at most 2sqrt(m)+2 <=4sqrt(m) integers, hence

p_j >= 3/(16sqrt(m)).                                             (1)

Set t=floor(sqrt(m log(m))/40). For m>=10000, t>=2 and t+2<=m/114. To see the latter, log(m)<=m/1000 for m>=10000, giving t<m/1000 and 2<=m/5000. As r and 1-r are at least r0=1/57, all intermediate adjacent ratios between j and s with |s-j|<=t obey

p_(i+1)/p_i = (1-(i-mr)/(m(1-r)))/(1+(i+1-mr)/(mr)).

Both relative deviations in the logarithms have absolute value at most (t+2)/(m r0)<=1/2. Using |log(1+u)|<=2|u| in this range,

|log(p_(i+1)/p_i)| <= 4(t+2)/(m r0).

Summing at most t adjacent ratios, using t+2<=2t and t^2<=m log(m)/1600, yields

p_s >= p_j*exp(-8t^2/(m r0))
    >= (3/16)*m^(-1/2-57/200)
    = (3/16)*m^(-157/200).                                       (2)

For m>=10000 this exceeds 1/m: equivalently m^(43/200)>16/3, true already at m=10000 since 10000^(43/200)=10^(43/50)>10^(4/5)>16/3. The last inequality follows by taking fifth powers: 10000>(16/3)^5. Thus p_s>=1/(m+1) for every integer s in [j-t,j+t], which lies inside [0,m] by r>=1/57 and t+2<=m/114.

Each of these 2t+1 locations contributes exactly 1/(m+1) to the overlap. With w=sqrt(m log(m))/40 >=1, floor(w)>=w/2, so

overlap >= (2t+1)/(m+1) >= sqrt(m log(m))/(40(m+1))
        >= (1/80)*sqrt(log(m)/m).

This proves (B).

## Completing the all-parameter rate

M~Bin(n,1-z), with E[M]=n(1-z)>=9n/16 and Var(M)<=n/4. Chebyshev implies

Pr(M<n/2) <= (n/4)/(n/16)^2 =64/n.

For n>=20000, Pr(M>=n/2)>=1/2; on that event M>=10000. The function log(x)/x decreases for x>=e, and M<=n, so lemma (B) gives conditional overlap at least (1/80)*sqrt(log(n)/n). Taking the expectation in exact identity (A) yields

1-TV(P^{tensor n}, B_z^{tensor n}K_n)
  >= (1/2)*(1/80)*sqrt(log(n)/n)
   = (1/160)*sqrt(log(n)/n).

This estimate is uniform in lawful (a,c). The definition of delta_n proves the new theorem. The earlier source's Hoeffding bound supplies the matching order in the other direction, establishing Theta.

## BRC/observer meaning and evidence scope

This kernel retains the stop3 positional trace and introduces a *shared* random hidden-branch coordinate R for the erased stop1/stop4 labels. Its uniform beta-binomial law is an exact joint observer-preserving construction at the stated output horizon, though it approximates the original hidden conditional law. The carrier is a tagged probability word with preserved branch multiplicity and no signed-amplitude cancellation; the arithmetic is ordinary auxiliary probability algebra. BRC applicability has been audited as a typed branch/observer reduction, not as an assertion of a new native BRC primitive.

VERIFY.py performs exact beta-integral factorial identities, small-m rational overlap checks, and 24 exact large-m endpoint inequalities for three integer m values and four rational r values. These are finite regression witnesses; the arbitrary-real all-n result follows from the analytic argument above. Independent mathematical review and a lawful bridge from this auxiliary tagged experiment to the original ten-label S23 encoder/decoder objective remain separate follow-ups.
