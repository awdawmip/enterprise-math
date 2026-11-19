# R762GA — Exact signed-branch orbit classification for STAR-framed triadic BRC

Date: 2026-11-19. Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Status: AUTHOR_PROVED / EXACT_FINITE_ENUMERATION_PASS / NOT_REVIEWED.

Scientific premises: frozen P000 signed X6 and six-axis Cell torsor, native taskbook @857280d1012943290d141d1317179c40ec3cbdf8. Antecedents R762FT, R762FX, R762FY and R762FZ (Draft PR #2803@1f3e7ca206f1a6d9add963ffe42e91de90e63748). The present classification is of a **positive BRC carrier whose branch labels contain three signs**. A sign label does not cause cancellation of positive branch weight and does not grant primitive native event permission.

## Typed domain

An oriented signed triad is (g,s) where g is a 3-cycle on distinct positive-axis labels in X={0,...,5}, and s: supp(g)->{+1,-1} is a sign attached to each moved native direction. The cyclic presentation (i j k) identifies (j k i) and (k i j) but not the inverse cycle. S6 acts by (g,s)->(sigma g sigma^-1, sigma_*s), **transporting signs with axis labels**. It does not invert an individual sign by fiat. There are 40 oriented cycles, each carrying 2^3=8 sign patterns, hence 320 states.

Fix the K4 incidence frame of R762FZ with four STAR supports. Its S4 stabilizer acts on 4x2x8=64 frame-restricted signed branches. Mark one STAR as excluded; the remaining stabilizer is S3 of order six acting on 3x2x8=48 marked-frame signed branches.

## Theorem A — S6 has precisely four signed oriented-triad orbits

The only S6 orbit invariant on (g,s) is k, the **number of negative signs** on the three moved axes. The four orbits have exact sizes

| k | orbit size |
|---|---:|
| 0 | 40 |
| 1 | 120 |
| 2 | 120 |
| 3 | 40 |

**Proof.** Fix an oriented 3-cycle g. Its stabilizer in S6 is the direct product of the cyclic group C3 rotating its three moved axes and S3 permuting the three fixed axes. C3 cyclically permutes the sign entries. For length-three binary sign words, all configurations with a fixed negative count k lie in one C3-orbit (one configuration for k=0,3, three for k=1,2). Since S6 acts transitively on the 40 oriented 3-cycles, the four full orbit sizes are 40 times the per-cycle sign counts 1,3,3,1. No permutation changes k, so these orbits are distinct and exhaustive. QED.

Therefore every S6-invariant nonnegative normalized BRC kernel on these **typed signed branch labels** is specified by four nonnegative orbit masses q0,q1,q2,q3 with sum one. Each branch in k-orbit has weight qk/[40*binom(3,k)]. Symmetry alone **does not force equal mass among the four sign populations**, nor does a signed-force closure predicate follow from positive weights.

## Theorem B — fixed four-STAR frame has the same four orbit types, smaller sizes

Inside a fixed K4 frame, its S4 stabilizer acts transitively on the eight oriented STAR branches. For one such oriented branch the S4 point-stabilizer has order 24/8=3, acting on the three incident edge axes as the cyclic group C3. It therefore has exactly four sign-pattern orbits classified by k, with sizes 1,3,3,1. The full signed frame-orbit sizes are

  (8,24,24,8), summing to 64.

The unique invariant kernel **conditional on a given qk mass** is uniform within its corresponding orbit. This supplies an exact sign-preserving refinement of the previously unsigned eight-branch frame kernel.

## Theorem C — marking the excluded STAR creates four extra orbit distinctions

Fix a frame and one excluded STAR. The stabilizer S3 of the marked frame acts *freely and transitively* on the six retained oriented STAR branches: there are six branches and the action is transitive, so every point stabilizer is trivial. Consequently **each of the eight binary sign decorations of one reference oriented branch defines a distinct marked-frame S3 orbit of size six**.

The 48 signed branches split into exactly eight orbits, each of size six. Four orbits have negative counts k=0,3 once each and k=1,2 three times each:

  k=0: 1 orbit of 6;
  k=1: 3 orbits of 6;
  k=2: 3 orbits of 6;
  k=3: 1 orbit of 6.

These additional sign-pattern distinctions are real *under the fixed marked-frame group action*: identifying them by k alone requires an explicitly declared observer quotient, averaging of marks, or additional allowed transformations. The theorem does **not** imply that the extra distinctions automatically affect the physical Cell/Link/Port future; that is a question for the native permission/readout language.

## Native signed covariance and observer implications

Given a putative unframed sign-aware S6-equivariant legality predicate P(g,s), its legal set is a union of the four k-orbits. Thus the 2^4=16 such *Boolean orbit-union predicates* include the empty predicate and the all-320 predicate. The fact that sign-independent unframed permission requires all-or-none of 40 oriented cycles (R762FZ) is the special case of equal legality across k.

By contrast, if a fixed K4 frame and excluded STAR are part of the legitimate native input, a marked-frame S3-invariant legality predicate can distinguish eight orbit types. The four extra distinctions arise from the source-bearing marked carrier and must not be erased merely because the signs have the same negative count. If the sign gate changes under signed-axis flips W6, that is a **different action contract** requiring an actual sign-flip update of the incoming metadata and closure incidence bit; this paper claims only S6 axis permutation covariance.

The positive BRC operation remains a source-named branching representation; its weight is nonnegative. The signed labels are metadata used by the input and later observer, not negative weights or signed cancellation. Time labels, genuine primitive force balance, actual BLOCK semantics, and native legal update grants remain to be defined.

## Verification

The attached standalone Node.js integer checker explicitly enumerates all 720 S6 permutations, all 24 induced K4 vertex permutations and the six marked-frame stabilizer permutations; builds all oriented triples and all 8 signed patterns; constructs exact orbits under each group; and checks the results above with independent population totals. No numerical tolerance, transcendental evaluation or external libraries. Exhaustive **finite model** verification PASS, independent proof review NOT_REVIEWED.

## Next

Examine the actual frozen Source-native signed Port/event incidence metadata. Determine which of the four unframed sign-count orbits (or eight fixed marked-frame orbits) would be legal under an actual native permission predicate. Test whether sign flips act on a closure incidence bit in the genuine native rule; establish a typed source-preserving bridge to BRC or a concrete obstruction. Preserve the joint frame, source and sign relations until an explicit future-observer descent certificate is established.
