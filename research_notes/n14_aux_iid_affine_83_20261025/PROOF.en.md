# N=14 auxiliary iid — 83rd exact optimal affine segment (author-level)

2026-10-25. Predecessor: awdawmip/enterprise-math@2b8a1a683122b63fd3610ae284e41cae45fc36e1 (stage82). This is an author-level exact-rational proof in a **finite auxiliary iid model**, not a native X6/BRC/Heartbeat dynamics theorem or independently reviewed Research Driver result.

## Statement

For all possibly history-adaptive randomized sequential tests with horizon N=14 and three-symbol iid laws P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), write eP=P(decide Q), eQ=Q(decide P), tP=E_P T, tQ=E_Q T, V14(alpha)=inf{max(tP,tQ):eP,eQ<=alpha}. The inherited exact endpoint is

\[
\alpha_{82}=\frac{5172016234423397153}{14900301753911083008},\
V_{82}=\frac{6127998356585438501}{465634429809721344},\
s_{82}=\frac{7532383150562527}{13926400000000000},
\]

where s82 is the immediate-Q probability at B=(12,0,1). The previous tie A82=(9,7,2) is fixed to P; A81=(11,3,3) is fixed to Q.

**Theorem.** For **every real** delta with

\[
0\le\delta\le\eta_{83}=\frac{901945}{146081389744226304},
\]

the exact global optimum is

\[
\boxed{V_{14}(\alpha_{82}+\delta)=V_{82}-\frac{27820620}{5819}\delta.}
\]

Its sharp right endpoint and optimal value are

\[
\boxed{\alpha_{83}=\frac{5172016234515395543}{14900301753911083008}},\quad
\boxed{V_{14}(\alpha_{83})=\frac{24511993371361253729}{1862537719238885376}}.
\]

The supporting line cannot be attained for alpha>alpha83.

## Exact Bellman lower bound

At state (n,a,b) with a observed zeros and b ones, Q/P=2^(a+b)/3^a. Use

\[
K_{83}=246614868/98923,\quad
\lambda_Q=K_{83},\quad
\lambda_P=72+8K_{83}/9=226335672/98923,\quad
\Gamma=\lambda_P+\lambda_Q=27820620/5819.
\]

P-normalized Bellman costs are stop P=lambdaQ*(Q/P), stop Q=lambdaP, continue=1+sum_i P_i D(child_i). Exact backward comparison of the inherited deterministic action at *every* state against *every* available alternate action gives 680 states, 1240 nonselected comparisons, 1238 strictly positive gaps, zero negative gaps, and two zero gaps exactly: A83=(8,4,4), C versus immediate Q, and B=(12,0,1), C versus immediate Q. The minimum strictly positive action gap equals 76054907033/2363059961856. The exact root is

\[
D_{root}=\frac{36257445152426828158772267}{21676213976502148005888}
=V_{82}+\Gamma\alpha_{82}.
\]

For all full-history randomized tests (not only count-based policies), conditional iid likelihood ratios are constant on count-state fibers. Therefore Bellman yields

\[
D_{root}\le t_P+\lambda_P e_P+\lambda_Q e_Q
\le \max(t_P,t_Q)+\Gamma\alpha.
\]

## Weighted ordered-path primal construction

The new tie A=(8,4,4) has 70 nominal ordered prefixes, but only 31 are first reachable under the inherited stop table. Exact *weighted* first-hit masses are

\[
p_A=31/1358954496,\quad q_A=31/429981696.
\]

The continuation suffix conditional quadruple (P-error,Q-error,additional P-time,additional Q-time) is

\[
R_A=(1177489/1179648,\ 527/1492992,\ 207371/147456,\ 17257/13824).
\]

A distinct ordered-word DFS independently counts 57 terminating suffix words, 20 terminal decision-state classes, so choosing to stop at A truncates 31*57=1767 original terminal histories. No history count is treated as probability mass.

At B=(12,0,1), all 12 nominal prefixes are first reachable, exact masses

\[
p_B=48828125/725594112,\quad q_B=48828125/362797056,
\]

and conditional suffix quadruple R_B=(63/64,1/144,9/8,13/12), with 5 terminal suffix words.

Let A stop Q with probability u and otherwise continue; let B stop Q with probability s and otherwise continue. Define

\[
X=p_A(1-R_A^{Perr})=66929/1603087953297408,\quad
Y=q_A R_A^{Qerr}=16337/641959232274432,
\]
\[
E=p_B(1-R_B^{Perr})=48828125/46438023168,\quad
H=q_B R_B^{Qerr}=48828125/52242776064.
\]

The cones of the two tie states cannot intersect: the count of zeros a never decreases, while A has a=4 and B has a=0 (and B occurs later). Hence risks and sampling times are exactly affine in u and s, with no mixed u*s coefficient. Relative to baseline (u,s)=(0,s82),

\[
\Delta e_P=Xu+E(s-s82),\quad \Delta e_Q=-Yu-H(s-s82).
\]

Balance both errors by the *exact* relation

\[
\boxed{s=s82-h83u},\quad
\boxed{h83=(X+Y)/(E+H)=41575681/1228800000000000}.
\]

Both error probabilities then equal alpha82+eta83*u since

\[
\eta83=X-Eh83=Hh83-Y=901945/146081389744226304>0.
\]

At u=1, s83=s82-h83=22597148038114427/41779200000000000; 0<s83<s82<1. The exact tP-tQ gap at u=0 and u=1 is respectively

\[
791385134454226187/1241691812825923584>0,\quad
2374155610282626305/3725075438477770752>0.
\]

These are affine in u, so tP>tQ for all **real** u in [0,1]. Because only Bellman-minimizing actions are used, the constructed strategy attains the dual bound for every real u. Set delta=eta83*u to obtain the claimed global optimum on the entire real interval.

## Strict right sharpness

If alpha>alpha83 attained the same dual line, positivity of lambdaP,lambdaQ would force both errors equal alpha and Bellman equality would force all positive-weight actions to be Bellman-minimizing. The exhaustive strict-gap certificate permits randomization only at A and B. Ordered histories with a fixed state have the same likelihood ratio and conditional continuation law, hence history-dependent tie decisions average to effective u,s in [0,1]. Since cones are disjoint, balanced errors require s=s82-h83*u, which forces alpha=alpha82+eta83*u<=alpha83: contradiction. The finite-horizon randomized policy set and its performance image are compact, so equality is strictly impossible beyond the endpoint.

## Evidence boundaries and successor

Two **local** author checkers using Python Fraction actually passed: a complete Bellman/forward exact-rational computation, and an ordered-prefix/suffix DFS with exact P/Q weights. They share the inherited stopping rule and do not establish independent Driver review. No native CLAIM, RESULT freeze, Lean proof, or P000/X6/BRC dynamical correspondence is asserted. The GitHub-portable verification scripts are source-adapted and have not been executed remotely.

Next **unproved** candidate after fixing A83 to immediate Q: K84=19502203788/8022631 at A84=(7,4,0), continue versus immediate P.
