# R749SC — Exact optimal recovery of named signed-Port provenance from unsigned observations

Date 2026-11-12. Author-side continuation of R749SA/R749SB, draft PR #2170, researcher EM-DIRECT-9F7D25 / RA-D46184D9060689BCC1124235, same original scientific input pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. No new native event license, Task CLAIM, Result or review.

## Finite experiment and question

Let the R749N signed C1 process P_p, 0≤p≤1, start from its stationary uniform law on 960 directed signed-Port edges. Observe only an n-vertex unsigned-support path A=Π(Z), n≥2 and m=n−2. An estimator is any possibly randomized rule that outputs one *complete named-signed-Port n-path* consistent with the observed unsigned path. What is the exact largest possible probability of recovering the entire hidden signed path?

R749SB gave the conditional lift distribution: every observed A has eight initial signed edge lifts and 2^m binary continuations, and if K of its m steps are unsigned C1 completions, the preferred hidden sign has probability t=(1+15p)/(2+14p), while the other steps are fair hidden binary choices.

## Theorem: exact optimal decoder and success probability

For a fixed unsigned block A with K=k and positive observation probability, the optimal maximum-a-posteriori (MAP) probability of guessing the *entire* hidden signed path correctly is

    M_p(A)= (1/8) · t(p)^k · (1/2)^(m-k).

The strategy is to guess any one of the eight initially uniform signed source lifts, then choose the named-source forced signed successor whenever the observed unsigned support is forced, and choose either signed lift at any unforced unsigned step. No decoder can exceed this because the conditional posterior factors into the stated independent fibers. Randomization cannot improve the maximum posterior mass.

Averaging over the observed unsigned path gives the exact optimal whole-path reconstruction success for all n≥2 and all p∈[0,1]:

    S_n(p) = E_p[M_p(A)]
           = (1/8)·((1+p)/2)^(n-2).

Two independent proofs:

(i) R749SA gives K~Binomial(m,a), a=(1+7p)/8. Therefore E[M]=(1/8)[a t+(1-a)/2]^m. Since at=q=(1+15p)/16 and (1-a)/2=7r=7(1-p)/16, the bracket is q+7r=(1+p)/2.

(ii) For each legal unsigned block with K=k, a best full signed path has unconditional mass q^k r^(m-k)/960. The number of such unsigned blocks with K=k is 120 binom(m,k) 7^(m-k). Sum max path mass over all unsigned blocks to obtain (1/8)(q+7r)^m, with the endpoint p=1 interpreted on positive-probability blocks.

The corresponding **average conditional min-entropy**, defined operationally by H_inf^avg(Z|A)=-log2 ∑_A P(A) max_Z P(Z|A), is exactly

    H_inf^avg(Z|A) = 3 + (n-2) log2(2/(1+p)) bits.

At p=0 every one of the 8·2^m hidden lifts is equiprobable and S_n(0)=2^(-m-3). At p=1 the unsigned path is deterministically C1 and has exactly eight equally likely complete signed histories, so S_n(1)=1/8 for every n. At p=1/2 and n=4, S_4=9/128. This is a quantitative reconstruction boundary for the declared unsigned-only observer; it is not an assertion of physically random signed-Port events.

## Exact finite verifier and reuse

A companion program R749SC_PROVENANCE_MAP_EXACT_CHECK.py rebuilds all 120 unsigned directed edges, counts all 120·8²=7680 unsigned four-vertex blocks by K=(0,1,2) as (5880,1680,120), and sums the largest complete signed-path mass exactly at p=0,1/2,1, comparing with the closed formula 1/32,9/128,1/8. It checks per-block optimal posterior mass on the supported blocks by exact rational arithmetic. The all-horizon result is proved by the fiber factorization and the binomial counting argument.

Operational consequence: the R749SA unsigned observer is valid for all future unsigned-support questions, but when a later operation needs the *original named signed-port history*, the three initial source bits remain indispensable even if an arbitrarily long C1-like unsigned trace is observed. A conditional posterior lift algorithm can preserve all source possibilities instead of making an unjustified unique assignment. The next question remains whether a truly native V29/V39 permitted Cell/Link/Port interaction supplies this exact two-lift observation fiber, including the BRC branch/provenance field.
