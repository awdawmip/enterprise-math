# R749SMO — Exact one-Port and sharp multi-level prediction-loss bounds for adaptive source observers

Date: 2026-11-13 (Asia/Shanghai). Continued from R749SMN at \`awdawmip/enterprise-math@c16fcd6f87d1fc57641ba9c6e8c65a38318bad33\`. Scientific inputs stay frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Researcher-side proof and exact rational checks; independent review pending.

## Observer and loss metric

Use the precisely defined finite full binary **public** observation tree of R749SMN, with fixed historical signed source \`x in (F_2)^d\`, node mask \`a_n\`, node channel bias \`lambda_n in [-1,1]\`, and conditional output \`P(y at node n | x, publicly observed history n)=(1+y lambda_n chi_(a_n)(x))/2\`. Named Port masks may be repeated, dependent, or zero. At a given source x, write \`K_lambda(.|x)\` for the probability law of the complete public root-to-leaf path. A source prior \`mu\` yields the mixture \`mu K_lambda\`. Total variation is one-half the L1 difference of finite probability laws.

The source bits and masks encode historical provenance in an auxiliary conditional observer; they are not new P000 native spatial axes. No native V29/V39 transition authorization is inferred.

## Theorem 1: single-node perturbation, exact total variation

Suppose all channels except the one at an internal node n are identical in \`lambda\` and \`lambda'\`. Let \`H_n(x)\` be the source-conditional probability of reaching n (the same in both experiments). For every source x, including deterministic/erased bias boundaries,

    TV( K_lambda(.|x), K_lambda'(.|x) )
      = H_n(x) * |lambda_n-lambda'_n| / 2.

For any prior mu,

    TV( mu K_lambda, mu K_lambda' )
      <= E_mu[H_n(x)] * |lambda_n-lambda'_n| / 2
      <= |lambda_n-lambda'_n|/2.

The fixed-source expression is sharp, and the mixture inequality can be sharp for priors supported on one source.

**Proof.** The probability distribution of paths that avoid n is identical. The probabilities of reaching n also coincide because all ancestor channels coincide. Conditional on reaching n, the two laws share the identical downstream distribution in each of the n+ and n- subtrees; those two subtrees are disjoint in the complete-path sample space. Their Bernoulli mixing weights differ by exactly \`|lambda_n-lambda'_n|/2\` (since \`|chi_(a_n)(x)|=1\`). Thus summing positive and negative discrepancies in the two disjoint subtrees gives the exact fixed-source formula. Mixture convexity gives the prior inequality. QED.

A useful special case is erasing an informative node: setting \`lambda'_n=0\` costs at most \`E_mu H_n * |lambda_n|/2\` in TV for the **specified finite-path observer**, even if exact predictive rank falls.

## Theorem 2: sharp worst-case coupling bound for many changed nodes

Let h be the common tree depth and define, for each level k,

    q_k = (1/2) max_{nodes n with |n|=k} |lambda_n - lambda'_n|,   0 <= q_k <= 1.

For every source x and every source prior mu,

    TV(K_lambda(.|x), K_lambda'(.|x))
       <= 1 - product_(k=0 to h-1) (1-q_k),

    TV(mu K_lambda, mu K_lambda')
       <= 1 - product_(k=0 to h-1) (1-q_k).

This is a **sharp universal bound given only the per-level maxima q_k**: no universally smaller function of the q_k alone holds over all finite public adaptive Walsh trees.

**Proof.** Couple the two complete-output experiments while their public prefixes remain equal. If they arrive at the same node at level k with the same fixed source, their Bernoulli output distributions differ in TV by at most q_k. A maximal coupling therefore keeps the outputs equal conditionally with probability at least 1-q_k. Inductively the joint complete paths agree with probability at least the stated product. By the coupling characterization of total variation, the first inequality follows. Couple the same x in both experiments under a shared prior mu to get the second inequality (or use convexity).

To attain equality for arbitrary finite q_k in [0,1], put every mask equal to the zero Walsh mask (so chi=1). Make the first experiment deterministically output + at every level along the all-plus path by setting its reached-node biases to +1. Set the second experiment's reached all-plus-path node biases to \`lambda'_n=1-2q_k\`. Make all other nodes identical between experiments. The first complete path is the all-plus path with probability 1, and the second assigns that path probability \`product_k(1-q_k)\`; hence TV equals one minus that product. QED.

A concrete depth-two sharp witness takes both masks and the source invariant, the first experiment with root and subsequent plus-branch bias 1, and the second with root bias 1/3 and plus-branch bias 1/2. Then q_0=1/3, q_1=1/4 and TV=1/2 exactly.

## Operational interpretation

The R749SMN exact predictive rank may change discontinuously as a node bias crosses zero. By contrast, the new finite-horizon probability-law error has an explicit continuous, often small bound when low-bias nodes are erased or approximated, including when a node is reused at several adaptive locations. The bound is for the declared complete public future observation and source distribution. Before using it for BRC or native V29/V39 source compression, obtain actual admissible named-Port event kernels, future operation scope and source/branch provenance.

## Exact computational evidence

The companion \`R749SMO_ADAPTIVE_ERASURE_TV_EXACT_CHECK.py\` uses Python \`fractions.Fraction\` and the independent leaf-law evaluator from R749SMN. It checked 2,880 exact single-node perturbation profiles, each at four source states (11,520 per-source identities), plus 500 changing-multiple-node profiles and a constructive sharp witness. All assertions returned PASS. Finite checks are regression evidence; the universal finite-depth claims follow from the proofs above.

## Next questions

Derive tight *prior-specific* and *node-specific* bounds when several masks are reused, exploiting exact reachable-prefix probabilities rather than levelwise maxima. Then test on actual permission-verified V29/V39 native kernels preserving named Port and BRC provenance, without silently treating abstract Walsh bits as native axes.

