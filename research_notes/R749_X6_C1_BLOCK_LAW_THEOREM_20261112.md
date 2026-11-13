# R749 — Exact finite-block distinguishability and four-bit source repair for X6 C1

Date: 2026-11-12 (Asia/Shanghai).
Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Frozen science: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R748, PR #2163, 88e37954f799941641500c3e7d502c98af50bf6c.
Status: finite candidate C1 observer theorem, author-verified; no native V29/V39 execution or formal Result/Driver review.

## 1. Exact model

Take 12 signed Ports S={(i,s):i=0,...,5;s=±1}, preserving the X6 axis and sign types. Let V be the 60 unordered pairs of Ports with distinct axes. Define adjacency v~w when v,w share exactly one identical signed Port and their union has exactly three distinct axes. Each v has 16 neighbors. There are 960 directed neighbor pairs.

The retained-source process chooses V0 uniformly from V and V1 uniformly from its 16 neighbors, then advances deterministically by V(t+1)=V(t−1) △ V(t), where △ is symmetric difference. The shift on ordered adjacent pairs is a bijection of period three.

The resampled-source process starts with the same initial two-step law, then draws V(t+1) independently and uniformly among the 16 neighbors of V(t). Its Markov matrix is P=A/16 from R748.

Let μ_n and ν_n denote the respective measures on complete visible n-blocks (V0,...,V(n−1)).

## 2. Exact all-horizon block-law theorem

For each n≥2, μ_n is uniform on precisely 960 legal blocks; ν_n is uniform on 60·16^(n−1) legal blocks. The support of μ_n is a subset of the support of ν_n. Consequently:

TV(μ_n,ν_n)=1−16^(−(n−2)).

Under ν_n, the probability that every observed consecutive triple satisfies the retained-source symmetric-difference recurrence is exactly 16^(−(n−2)). The equal-prior optimal Bayesian classification error is 1/(2·16^(n−2)). In bits, the relative entropy D_2(μ_n || ν_n)=4(n−2).

Proof: There are 60 choices of V0 and 16 choices of V1. In the retained process these determine the entire block. Under independent resampling, n−1 independent 1-of-16 branch choices follow V0. All blocks under a given process have equal probability. The retained support contains 960 blocks of resampling probability 1/(60·16^(n−1)) each, so its ν_n mass is exactly 16^(−(n−2)). For a uniform distribution on a subset versus the uniform distribution on its superset, TV is exactly one minus the superset mass of the subset. The likelihood ratio is the constant 16^(n−2) on the retained support; summing the minimum masses establishes the Bayes error, and taking base-two logarithms gives relative entropy. QED.

Although the block laws diverge, their stationary single-step visible conditionals coincide: for every v and neighbor w, Pr(V(t+1)=w | V(t)=v)=1/16 under both processes. Indeed the retained period-three shift is bijective on 960 ordered adjacent states and preserves their uniform law.

## 3. Sharp predictive-state theorem

The ordered pair (V(t−1),V(t)) is an exactly sufficient state for the retained process, with 960 possibilities. Given current v, each of its 16 possible predecessors w yields a distinct next state w △ v; hence at least 16 latent predictive classes (four bits) beyond v are needed. The previous observation provides a sharp four-bit repair.

Proof: The formula gives sufficiency. If w1 △ v = w2 △ v then symmetric-difference cancellation implies w1=w2. All 16 predecessor states have positive probability in the uniform stationary process. No predictive quotient combining any of them is exact, and the two-observation construction attains 16. QED.

This is an exact observer-specific all-horizon BRC source-fidelity certificate. It extends R747/R748 from graph spectrum and one-time returns to full block distributions, and gives an integer-count test of source memory.

## 4. Reproducibility and scope

The accompanying standard-library Python verifier enumerates all legal n-blocks for n=1,2,3,4: total counts 60,960,15360,245760. It checks μ_n support sizes, containment, TV and Bayes fractions, all 60 degrees and 960 directed edges, and 16 distinct future states for every current v. The universal n result rests on the above counting proof, not extrapolation from a finite numerical horizon.

All conclusions refer to the R745–R748 C1 signed-Port candidate model. P000, the six-axis native space, the triadic-force arity and the original frozen scientific pin remain unchanged.

## 5. Unfinished native question

Construct one legal task-frozen TRIADIC_CLOSURE_E Cell/Link/Port event using actual V29 PASS/V39 types. Calculate its one- and three-event successor and signed flow; retain branch and provenance. Check whether a typed visible pair observer exists and whether the native update commutes with (v,w)→(w,v △ w). If it does not, preserve a concrete obstruction and the smallest needed repair. Actual native equivalence, the complete parent hard target and independent Driver review remain open.
