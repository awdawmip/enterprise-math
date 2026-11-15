# EC49FPU–FPW — Exact mixed native-BRC observation witnesses and a wider price interval

Date: 2026-11-15. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Continuation of EC49FPT (PR #2494), EC49FPS (PR #2490) and EC49FPN (PR #2479). P000 and ACTIVE worldview remain fixed.

## Scope and prior exact results

The entire legal-root class first represented by original configuration 16995 contains 242 original source configurations, 112 distinct named-root cost profiles, 324 complete-allocation terminal scalar actions T and 96 named-root/optional-demand scalar actions R. All responses are exact integer values from the frozen native BRC Trie table. Each adaptive decision tree must uniquely identify the named-root profile; source multiplicities are retained with a uniform prior on the 242 original configurations. An R observation costs r>0 and a T observation costs t>0.

Predecessor exact Bellman certificates prove that the best pure-R and pure-T trees have total weighted observation counts 841 and 641 respectively, yielding expected prices 841r/242 and 641t/242. These earlier certificates are author-checked; formal project Review is pending.

Frozen master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
Frozen rooted-cost CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

## Three newly constructed complete policies

Starting from the previously independently replayed EC49FPT tree (weighted R=762, T=44), a local exact improvement algorithm enumerated all 420 original sensor actions at every currently reached internal node. For each action's response fiber it restricted the existing descendant tree to the fiber, removed uninformative previously used actions, and evaluated the exact configuration-weighted price of that legal continuation. It substituted the strictly cheapest improving action and repeated until no single local splice further improved the result. Every substitution strictly decreases a positive integer cost and retains all original source-profile identities. Local termination is not global Bellman optimality.

| Policy | Construction price r:t | Weighted R reads | Weighted T reads | Scaled total | Successful local substitutions |
|---|---:|---:|---:|---:|---:|
| EC49FPU | 3:5 | 692 | 83 | 2491 | 1 |
| EC49FPV | 3:4 | 634 | 121 | 2386 | 6 |
| EC49FPW | 4:5 | 586 | 158 | 3134 | 9 |

At r/t=3/5, EC49FPU costs 2491t/1210, improving EC49FPT's 2506t/1210 and pure-R 2523t/1210. At r/t=3/4, EC49FPV costs 2386t/968. At r/t=4/5, EC49FPW costs 3134t/1210, beating pure-T 3205t/1210 and pure-R 3364t/1210.

## Theorem — a wider interval where every optimum mixes sensor types

**For every positive pair of prices with**

\[
\boxed{\frac{44}{79}<\frac rt<\frac{483}{586}},
\]

**every globally optimal adaptive identifying policy uses both R and T observations on positive-prior execution paths.**

Proof. An explicit valid policy with weighted query counts (R,T) costs (Rr+Tt)/242. Its cost is strictly smaller than both globally optimal pure policies exactly when

\[
\frac{T}{841-R}<\frac rt<\frac{641-T}{R}.
\]

The four independently replayed mixed policies supply the following intervals:

| Policy | Open interval |
|---|---|
| EC49FPT | (44/79, 199/254) |
| EC49FPU | (83/149, 279/346) |
| EC49FPV | (121/207, 260/317) |
| EC49FPW | (158/255, 483/586) |

The intervals overlap consecutively, since 83/149 < 199/254, 121/207 < 279/346 and 158/255 < 260/317. Their union is exactly (44/79,483/586). At each such ratio a valid mixed tree is strictly better than the best pure-R and pure-T trees. A globally minimizing identifying tree exists, because there are finitely many states/actions and no minimum-cost tree needs an uninformative query or a repeated candidate set when every query has positive cost. Thus no optimum can be pure. QED.

The new upper endpoint 483/586 = approximately 0.82423208 improves EC49FPT's 199/254 = approximately 0.78346457. The lower endpoint 44/79 is retained.

## Verification, status, next questions

Both builder and independently implemented verification replay used the original 38,169-configuration, 94-family, 178,850-source-word master and its pinned rooted Trie cost table. They reconstructed exactly 242 source members, 112 rooted cost profiles and all 420 native actions. Three complete new JSON decision-tree certificates were generated. The independent verifier replayed every one of the 242 original configurations through each tree, checked all 112 leaf identities, confirmed weighted (R,T) totals (692,83), (634,121), (586,158), and checked the rational endpoint union. Output: ALL_242_CONFIGURATIONS_THREE_PRICE_POLICIES_PASS.

This author-verified constructive theorem strengthens the previously certified finite family; it does not assert a new global mixed Bellman optimum at r/t=3/5. The unrestricted price-dependent Bellman value and the first global departure point from pure-R optimality remain open. Further work: extend the lower endpoint by a new policy or prove the exact first global breakpoint; improve the upper endpoint, potentially using substitutions into a terminal-first tree; independently review the existing pure optimality certificates.

Full executable builder, independent verifier, frozen original data, three complete decision-tree certificates, source hashes, logs, proof and integrity manifest are retained in the associated complete evidence archive EC49FPU_FPW_MIXED_WIDER_INTERVAL_COMPLETE_20261115.tar.xz, SHA256 0488f2773623c7bc1be02fc9f301145b200fe856eb28924bb548839d477ba7fd. This PR preserves the theorem in Source, with the complete reproducible archive attached to the research conversation.

Scientific activity and formal Task/CLAIM state are separately authenticated; the existing topic RS-EC49AS was previously returned as unpublished. No new CLAIM, Result or project admission is asserted.