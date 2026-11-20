# EC49FUY — Lattice-phase residual prevents convergence of least-favorable endpoint weights

Date: 2026-11-20 (Asia/Shanghai)
Evidence classification: AUTHOR_PROVED / EXACT_FRACTION_FINITE_CROSSCHECK / ASYMPTOTIC_ARGUMENT / PARENT_DEPENDENT / NOT_REVIEWED.
Scientific input: BRC16943 frozen fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Immediate predecessor: EC49FUX, PR #2862, commit db74e155df059953b888f3e99d51bd0bef5de77c.
Parent premise: FUQ endpoint-prior reduction and FUR dual formula are author-proved and not independently reviewed. The simple cross-pair lattice result below does not need those premises; transfer to the original composite game does.

## 1. Model and question

Write E=31597745/1653649, beta=3/637,
u_theta=21829245984/(45529434409-456083905 theta),
T_theta(x)=(1-x)(1-beta x+beta theta x),
p_theta=1-T_theta, and q_theta=1-u_theta T_theta.

At a fixed width 0<x<1, set
a=p_0(x), a_-=p_E(x), b=q_E(x), b_+=q_0(x).
The frozen model has 0<a_-<a<b<b_+<1.
For n iid Bernoulli hit indicators at a common unknown theta, the equal-hypothesis-prior composite risk is V_n(x).

The preceding EC49FUX proved that -log V_n(x)/n tends to the cross-pair Chernoff information C(a,b). An exponential rate does not by itself determine the asymptotic least-favorable mixing weight. We resolve this issue for the exactly rational width x=7/20.

By the FUQ/FUR endpoint-prior dual formula, the highest-endpoint prior weight lambda maximizes

F_n(lambda) = (1/2) sum_{k=0}^n min{
    (1-lambda) Bin(n,a)[k] + lambda Bin(n,a_-)[k],
    (1-lambda) Bin(n,b_+)[k] + lambda Bin(n,b)[k]
}.

Define the simpler cross-pair subgame

G_n(lambda) = (1/2) sum_{k=0}^n min{
    (1-lambda) Bin(n,a)[k], lambda Bin(n,b)[k]
}.

Both are concave piecewise-affine functions of lambda in [0,1], and F_n >= G_n pointwise.

## 2. Exact lattice parameters

Let

A = log( b(1-a)/(a(1-b)) ) > 0,
t = log((1-a)/(1-b))/A, so a<t<b,
C = D(t||a) = D(t||b),
r_a = a(1-t)/(t(1-a)) in (0,1),
r_b = b(1-t)/(t(1-b)) > 1.

Then A=log(r_b/r_a), and for every n and every integer k,

Bin(n,b)[k] / Bin(n,a)[k] = exp(A(k-nt)).                    (1)

Set

L = r_a (1-r_b^{-1})/(1-r_a) > 0,
c = log(L)/A.

The binomial mass at k=nt+O(1), normalized by sqrt(n)exp(nC), has a geometric lattice profile. For any subsequence with fractional parts {nt} -> rho, uniformly in lambda on [0,1],

sqrt(n) exp(nC) G_n(lambda) -> H_rho(lambda),               (2)

H_rho(lambda) =
 (1/[2 sqrt(2 pi t(1-t))])
 sum_{m in Z} min{
   (1-lambda) r_a^(m-rho),
   lambda r_b^(m-rho)
 }.

The bilateral sum converges absolutely and uniformly in lambda; in the positive tail the first term dominates the bound, and in the negative tail the second dominates. Equation (2) follows from the binomial local limit at k=floor(nt)+m and these geometric tail bounds, with fixed x.

## 3. Exact maximizer of the limiting lattice game

For rho satisfying c+rho not an integer, H_rho has a unique maximizer

Lambda(rho) = 1/[1+exp(A(ceil(c+rho)-rho))].                 (3)

Proof: For a monotone likelihood-ratio threshold at lattice count j, compare the two geometric tail errors. The inequalities for zero to lie between the two slopes at a kink are

  (r_a(1-r_b^{-1})/(1-r_a)) <= exp(A(j-rho))
  <= ((1-r_b^{-1})/((1-r_a)r_b^{-1})).

The right endpoint divided by the left endpoint is r_b/r_a=exp(A). Hence exactly one integer j=ceil(c+rho) satisfies both strict inequalities off the exceptional phase. At that kink the two weighted masses are equal:
(1-lambda)r_a^(j-rho)=lambda r_b^(j-rho), proving (3).
At c+rho integer the limiting maximizer can be an interval; this exceptional phase is excluded from the stated uniqueness formula.

The nonexceptional phase map Lambda is injective on [0,1): equality of its logistic values would require an integer difference of two ceilings to equal the nonzero difference of two fractions in [0,1), impossible.

## 4. Transfer back to the original common-theta minimax game

The additional endpoint components in F_n are exponentially negligible precisely at the cross-pair decision boundary, but are not discarded as probabilities.

For any fixed delta in (0,1/2) and lambda in [delta,1-delta], the Bayes threshold for G_n is nt+O_delta(1), uniformly in lambda. Apply this very same threshold in the full mixture. Its extra false-positive term from a_- and false-negative term from b_+ are each bounded by exp[-n(C+eta_delta)] for some eta_delta>0, because

D(t||a_-) > D(t||a)=C, and
D(t||b_+) > D(t||b)=C.

Consequently,

0 <= F_n(lambda)-G_n(lambda)
   <= exp[-n(C+eta_delta)] times a bounded subexponential factor,       (4)

uniformly on [delta,1-delta]. The required bound follows by binomial Chernoff tails at thresholds nt+O(1); any fixed polynomial prefactor is harmless.

All H_rho maximizers lie in a common compact interval strictly inside (0,1): the kink j-rho belongs to [c,c+1], so
lambda belongs to
[1/(1+exp(A(c+1))), 1/(1+exp(Ac))].
Choose delta smaller than the first endpoint and 1-delta larger than the second. The one-sided slopes of H_rho at delta and 1-delta point strictly inward, uniformly over phases. By the compact-uniform limit (2) and (4), F_n increases somewhere immediately to the right of delta and decreases somewhere immediately to the left of 1-delta, for all large n. Concavity therefore confines every maximizer of F_n to [delta,1-delta].

On a subsequence {nt}->rho with c+rho not integer, (2),(4) and the preceding compact confinement give uniform convergence of the rescaled full dual to H_rho on the set containing all maximizers. Its unique maximizer (3) implies that every selection lambda_n of least-favorable highest-endpoint weights satisfies

lambda_n -> Lambda(rho) along that subsequence.               (5)

Thus the exponentially accurate Chernoff risk exponent does not force convergence of the optimizing nuisance-prior weights.

## 5. Concrete rational-width nonconvergence theorem

Choose x=7/20. Then, exactly,

a = 983/2800,
b = 122610119576/203307125225.

Direct integer arithmetic gives a(1-a)<b(1-b), equivalent to t<1/2; also a<t. Therefore t is neither 0 nor 1/2 nor an integer.

If t is irrational, its multiples modulo 1 have dense subsequential phases, with at least two distinct nonexceptional phases. If t is rational in lowest terms, its denominator is at least 3, so its periodic phase orbit has at least two distinct nonexceptional phases (only one phase modulo 1 could satisfy c+rho integer). Since Lambda is injective there, (5) supplies distinct subsequential limits.

THEOREM EC49FUY: For x=7/20, under the author-proved FUQ/FUR endpoint reduction, every sequence of exact least-favorable endpoint-prior weights lambda_n has at least two different subsequential limits as n tends to infinity. In particular lambda_n does not converge. The simple cross-pair version is unconditional within the stated Bernoulli model.

Approximate values only for orientation:
t=0.476045064293, A=1.032641039881, c=-0.508125515164.
The full nonexceptional phase envelope is approximately
[0.375678958792, 0.628248755001].
For irrational t all values in that interval are accumulation points; the theorem needs no irrationality claim.

## 6. Independently reproducible finite checks

The standard-library companion EC49FUY_LATTICE_LEAST_FAVORABLE_VERIFY.py performs exact Fraction enumeration of every affine dual kink at n=30,50,80,100, with x=7/20. It checks both the composite two-endpoint dual and the cross-pair game. The exact rational maximizers converted to display decimals are:

n | full endpoint lambda | cross-pair lambda
30 | 0.958482767093 | 0.572127238972
50 | 1.000000000000 | 0.449126294383
80 | 0.647544826193 | 0.521570129354
100 | 0.814431600302 | 0.399295139430

The script executed locally with PASS. These finite calculations are diagnostic; the subsequence theorem follows from the analytic argument rather than extrapolation from four n values. Approximate t,c and logistic predictions are floating-point and labelled separately.

## 7. Relation to the residual-first research program, and next problem

Here the fractional lattice phase {nt} is an observer-relevant residual. Suppressing it preserves the leading risk exponent C but loses an order-one distinction in the optimal endpoint-prior weight. This is a precise mathematical example of task-dependent sufficient-state compression, not a claim that the binary observation is the complete BRC/X6 native state.

The P000 six-native-axis, three-dimensional-slice and structural-residual axioms remain unchanged. The Bernoulli observer is a typed lossy projection; no native six-dimensional dynamical equivalence is asserted.

Next scientific questions:
1. Give exact finite-n bounds on the distance of the full optimal lambda_n from the corresponding phase formula, uniformly away from the exceptional fractional phase.
2. Classify exceptional-phase nonunique limits and give the full accumulation set for rational versus irrational t at fixed width.
3. Extend the phase-sensitive second-order asymptotic to the minimax risk itself (including the n^(-1/2) prefactor), and examine x shrinking toward 0 or growing toward 1 with n.

Provenance: prior author Researcher EM-DIRECT-8454C6, SID MCP-44cfc4e6f2094f96861854ebefc77e84, Activity RA-ED136F89271FD89288F3E58D. These strings identify previous contributions, not current native execution authority. Current publication is portable independent research, not a new CLAIM, formal Result, Activity CAS or independent mathematical Review.