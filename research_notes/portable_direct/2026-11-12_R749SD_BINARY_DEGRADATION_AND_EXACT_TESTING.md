# R749SD — Exact binary degradation of signed-source evidence, and finite-sample testing

Date: 2026-11-12. Researcher: EM-DIRECT-9F7D25 / RA-D46184D9060689BCC1124235 (original registered session MCP-b52a077b5aa04731bc5becbaa95d0eba, recovered read-only). Draft PR #2170; author-side exact finite-observer theorem.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, with R749N, R749SA, R749SB and R749SC source definitions unchanged. No physical native Cell/Link/Port permission is asserted.

## Question and exact finite carrier

R749SA proves that, at every signed directed edge in the 960-edge carrier, the 16 outgoing signed-Port choices partition as: one exact signed C1 continuation S, one unsigned-only C1 continuation U, and fourteen other continuations O. The R749N interpolation assigns probabilities

    q = (1+15p)/16, r = (1-p)/16, and 14r,

where p∈[0,1]. For any n-vertex path n≥2 write m=n−2 for its subsequent transitions. Let X_i=1 iff transition i is the exact named signed C1 continuation, Y_i=1 iff its projected unsigned transition is a C1 continuation. Put J=ΣX_i, K=ΣY_i.

The exact step-level joint law, uniform in the incoming state, is

    P(X=1,Y=1)=q; P(X=0,Y=1)=r; P(X=0,Y=0)=14r.

The three-class innovations are iid across steps because these transition probabilities are independent of all preceding states. Thus

    E[u^J v^K]=(14r+r v+q u v)^m.                     (1)

Equation (1) is a joint signed/unsigned-source residual generating polynomial, retaining the different source categories before observer collapse.

## Theorem 1. Explicit parameter-independent degradation channel

The signed completion indicator X is Bernoulli(q). Conditional on X=1, Y=1 with probability 1. Conditional on X=0, the 15 alternative signed successors are equally weighted and exactly one has forced unsigned support, so

    P(Y=1|X=0)=1/15, P(Y=0|X=0)=14/15.              (2)

This stochastic channel B is independent of p and of history. Each step's Y may be simulated from X with independent B-noise; the m-step experiment is B^{⊗m}. Its output parameter is

    a=P(Y=1)=q+(1-q)/15=(1+7p)/8.

The signed path experiment is statistically equivalent, for inference on p alone, to m iid Bernoulli(q) indicators X; the unsigned path experiment is equivalent to m iid Bernoulli(a) indicators Y. Here "equivalent" means an experiment can simulate the richer path labels conditional on the indicator sequence using a p-independent conditional kernel: all 15 nonforced signed choices are equiprobable, all seven nonforced unsigned choices are equiprobable, and initial edges are uniform independent of p. For an observer that queries named Port/source histories rather than only p, this experiment equivalence is not a license to erase the histories.

The sample completion counts J and K are each *minimal sufficient* statistics for the one-parameter families on 0<p<1 (ratio of probabilities for two paths is p-independent precisely when their completion counts agree). Equation (1) also gives the exact joint multinomial counting law (J,K−J,m−K)~Multinomial(m;q,r,14r).

## Theorem 2. Strict loss and impossibility of a universal reverse simulator

There is no p-independent stochastic kernel from a single unsigned completion indicator Y to the signed completion indicator X that reproduces the complete family p∈[0,1].

Proof: At p=1, Y=X=1 almost surely. Such a reverse kernel must have P(X=1|Y=1)=1. At p=0 the unsigned forced probability is P(Y=1)=1/8 while the signed forced probability is P(X=1)=1/16; the required reverse kernel would generate P(X=1)≥1/8, a contradiction. In the interior, R749SB's exact per-step information loss is

    I_signed(p)-I_unsigned(p)=8/[(1+15p)(1+7p)(1-p)]>0,

which also precludes lossless reverse simulation of the full m-step regular parametric experiment for every m≥1. This is an observer-specific information comparison, not a claim about native events or arbitrary signed observations.

## Theorem 3. Exact optimal binary hypothesis discrimination

Fix 0≤p0<p1<1 and equal prior odds. In the signed observation experiment a uniformly most powerful likelihood-ratio rule selects p1 when

    (q1/q0)^J ((1−q1)/(1−q0))^(m−J)>1,

with boundary values interpreted by limits. In the unsigned experiment replace q,J with a,K. Both likelihood ratios increase strictly with the respective completion count.

For either c(p)=q(p) or c(p)=a(p), the *exact* minimal equal-prior classification error at length n=m+2 is

    Err_c(m;p0,p1) =
       1/2 - 1/4 Σ_{k=0}^{m} binom(m,k)
           |c(p1)^k(1−c(p1))^(m−k)
            −c(p0)^k(1−c(p0))^(m−k)|.              (3)

Proof: by the stated sufficient statistics the two path likelihoods reduce to two binomial distributions. For equal priors the Bayes error is (1−TV)/2; inserting the exact binomial probabilities gives (3). It includes all finite m and requires no asymptotic or floating approximation.

Example p0=0, p1=1/2, m=2 (four vertices): q0=1/16, q1=17/32, a0=1/8, a1=9/16. Both optimal rules select p1 iff at least one forced completion is observed. The signed and unsigned TV distances are respectively 675/1024 and 147/256, so

    Err_signed=349/2048, Err_unsigned=109/512,
    Err_unsigned−Err_signed=87/2048.

These exact rational values quantify the operational price of dropping signed-source observation *for this inference task*. R749SC instead quantifies full named-path reconstruction; the two observer targets must remain distinct.

## Verification, scope and next

The standard-library exact checker R749SD_BINARY_CHANNEL_EXACT_CHECK.py tests the full three-class multinomial generating law and both binomial marginals for m=0..8 at p=0,1/4,1/2,3/4,1; evaluates exact TV/error for m=1..6 at p0=0,p1=1/2; and verifies the endpoint contradiction in Theorem 2. It does not rerun R749SA's prior 960-state adjacency enumeration; that previously verified 1:1:14 fiber partition is a named premise. All-n proofs rely on the homogeneous step partition and likelihood factorization, not finite test extrapolation.

The next discriminating scientific problem is to inspect an actually declared native V29/V39 Cell/Link/Port transition and specify its signed-source/fiber map. If it has the stated 1:1:14 partition with a source-independent noise parameter, equations (1)–(3) apply directly; otherwise determine its actual typed branching polynomial and re-evaluate observer safety without inventing a physical source event.
