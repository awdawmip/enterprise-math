# EC49FRM provenance and exact verification, 2026-11-17

## Source and scope

Frozen BRC input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original complete native 141-state / 228-query static response source and original 310 multiplicities are not changed.

Inherited exact native path-cost certificate: EC49FRL_GLOBAL_FIVE_TREE_DEPTH3_CERTIFICATE.json, SHA256 2164b2a374c46bad29d5b669573fcafe87218f946e1bdd42e78dc78642ba0dfb, from the original self-contained EC49FRL evidence archive and GitHub PR #2630. Its five native tree cost vectors are copied verbatim in the new theorem and verifier. Inherited global Bellman envelope from EC49FRJ PR #2624 remains AUTHOR_PROVED / NOT_REVIEWED; this new result is a fully proved conditional consequence, not an independent review of that load-bearing input.

## Exact local execution

The local standalone proof package was executed in Python 3 using fractions.Fraction and sympy 1.14.0. It checked:

1. For every real x in [1,3], exact affine domination of the declared Bellman winners at lambda=0,620/3299,1, by exact endpoint tests of the relevant degree-one polynomials against all five trees.
2. For every real x>=3, exact affine domination by exact value at x=3 plus nonnegative slope.
3. The tie identities B=C and D=E at lambda=620/3299.
4. Exact polynomial zero identities for both normalized endpoint regrets and the universal dual expression for each piece.
5. Ten exact rational regression prices: 1, 9/8, 3/2, 2, 5/2, 3, 25/8, 4, 10, 1000. Both endpoint regrets equal the symbolic minimax formula at every tested price.
6. The optimal deterministic regret among the five certificate trees and its exact 620/3299 relative reduction by randomization.

The original locally executed verifier has SHA256 3c1ad81e2325d037531864f4682e4d104b8b15b93a9232a532a94502bed0aada; its local execution log SHA256 8d219975e04ba4f35638be3ebcbe4170422d740a5da740e01ef0ad63b189388a. The GitHub companion verifier implements the same domain-wide algebra with a distinct, concise program layout; a hosted execution of the exact GitHub file has not been claimed.

Representative exact outputs:
* x=1: sample B with 1240/3299, C with 2059/3299; worst expected regret 76/3299; best deterministic-five regret 4/141.
* x=2: B with 930/3299; worst regret 57/3299.
* x=3: B or D with 620/3299; worst regret 38/3299.
* x=4: D with 620/3299; worst regret 38/3299.
* x=1000: D with 620/3299; worst regret 38/3299.

Local complete 5-file evidence archive (theorem, executable verifier, log, inherited five-vector JSON and manifest) preserved in the conversation:
EC49FRM_GLOBAL_MINIMAX_REGRET_COMPLETE_EVIDENCE_20261117.tar.xz
SHA256 33773f52be6e9d976aea285d77909e9e3e8f9d201f0c806efb4ab9c48e01b4fc. It was decompressed and all four content files verified against its manifest.

## Proof scope, review and continuity

The mathematical proof is algebraic/convex analytic on the original finite BRC decision-tree cost model; the new randomization selects a whole original physical tree before observation and does not modify its BRC operations. The theorem's all-real-x/all-real-lambda quantifiers rest on the inherited global Bellman theorem and symbolic identities, not on ten samples. Mathematical status: AUTHOR_PROVED / EXACT_SYMBOLIC_CHECKED / NOT_REVIEWED. No new official native CLAIM, Source Result, Driver Review, Activity checkpoint or live-owner authority is asserted.

Next two exact questions: unrestricted *deterministic* minimax regret, and optimal robust policies for a proper uncertain-prior interval [lambda_minus, lambda_plus].
