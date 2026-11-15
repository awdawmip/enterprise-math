# X6 signed-frame word-orbit splitting and the concatenation context barrier

Date: 2026-11-16 (Asia/Shanghai)
Task: RS-X6-NATIVE-ROTATION-DYNAMICS / TP2-6A1F9D8C2047E3B51C01
Provenance: exact author's derivation, finite Burnside arithmetic crosscheck; independent Driver mathematical review pending.
Scope: the previously Source-published *candidate algebraic signed-frame action* on ordered signed primitive words. This classification is not itself a physical Heartbeat rotation law or an allowed primitive triadic force event.

## Frozen inputs and deduplication

Source-published prior result on 2026-11-15:
- group H = (C2)^6 ⋊ A6 of order 23040 and the letterwise action on Σ* with Σ={±e_1,...,±e_6};
- complete ordered word/path provenance retained; finite-depth mixed-sign quotient descent obstruction, which is not retested here.
- GitHub immutable proof:
  https://github.com/awdawmip/enterprise-math/blob/0e020615068df74e84d323325c1364029cc49641/research_artifacts/mcp/RS-X6-NATIVE-ROTATION-DYNAMICS/MCP-c618a61189764f23846a391a08518a1a/c1c9e1128e090ca4c3a7/X6_ORIENTED_TRIAD_SIGNED_C6_GROUP_AND_PATH_ACTION.md

A separate 2026-11-12 Driver note already proves sharp finite-horizon quotient memory bounds and CRT-grade augmentation:
https://github.com/awdawmip/enterprise-math/blob/cc0d2f61bbf5516bd06f32c2714d2b2a7e0cc986/research_notes/driver/2026-11-12_x6_finite_depth_signed_brc_cover_rotation_descent_and_minimum_memory.md
Consequently the present unit does not re-propose that result; it classifies the residual *word-orbit* quotient and its precise concatenation limitation.

## Theorem: all ordered signed-word H orbits and the first parity split

Let B6=(C2)^6 ⋊ S6 act on Σ={±e_i}, i=1,...,6, by signed coordinate permutations. Let H=(C2)^6 ⋊ A6 be the index-two subgroup from the earlier source result. Let W_N=Σ^N include the empty word W_0={ε}. Write S(N,k) for Stirling numbers of the second kind (partitions of N labeled positions into k nonempty unlabeled blocks). Then

  |W_N/B6| = Σ_{k=1}^{min(6,N)} S(N,k)·2^(N-k), N≥1,

  |W_N/H| = Σ_{k=1}^{min(6,N)} (1 + 1_{k≥5})·S(N,k)·2^(N-k), N≥1,

and both counts equal 1 at N=0.

In particular, for N≤4 the two orbit quotients have equal counts. Their first difference is at N=5, when exactly one B6 orbit splits into two H orbits, namely a pattern using five distinct native axes with any fixed relative signs. For N=6 the increase is 31.

### Proof

For an ordered word w of length N, partition its labeled positions by equality of their **unsigned axis**; this gives k blocks, with 1≤k≤min(6,N). The B6 action preserves that partition, and S6 acts transitively on injections of k abstract blocks into the six axes. Within each block, the C2 sign flip on the assigned axis acts by simultaneous sign reversal of all its letters. Thus a block of size s has 2^(s-1) relative-sign types, and across the k blocks there are exactly 2^(N-k) types. Conversely the unsigned-axis partition plus each block's signs relative to a fixed position reconstruct the B6 orbit. This establishes the B6 formula.

Because H is normal of index two in B6, a B6 orbit either stays one H orbit or splits into exactly two; it splits iff its point stabilizer in B6 lies inside H. A signed permutation stabilizing w must fix the **axis label of every used axis individually**: no permutation can exchange axes that appear in different positional blocks while preserving each letter at that position. The only possible odd unsigned permutation in the stabilizer is therefore an odd permutation of the 6-k unused axes. Such a permutation exists exactly if 6-k≥2 (k≤4), by transposing two unused axes, and it may use all positive signs. For k≥5 every stabilizing underlying permutation is even (indeed the identity on used axes, with at most one unused axis), so the B6 orbit splits into two H orbits. This doubles precisely those block/sign patterns with k=5 or 6. QED.

This is a group-orbit theorem for the *static frame candidate*. It is compatible with the previous letterwise full-path lift but does not identify the two H parity sectors with P000 intrinsic chirality, physically allowed rotation, or a force-balance class.

## Proposition: orbit-only factor is not composition-safe for concatenation

Let [w]_H be the H orbit of an ordered primitive-step word w under simultaneous letterwise action of one common signed frame element. The assignment w↦[w]_H is **not a monoid congruence** on Σ*: independent H-equivalence of prefixes and suffixes need not imply H-equivalence of their concatenations.

Proof: e_1 and e_2 are H-equivalent one-letter words. Also e_1 is H-equivalent to itself. But the length-two words e_1e_1 and e_1e_2 are *not* H-equivalent: the invariant partition of positions into equal unsigned axes is {{1,2}} for the first, and {{1},{2}} for the second. Therefore independent orbit classes cannot be concatenated without a shared-frame or relative-axis relation. QED.

Operational consequence: one may quotient whole N-step histories by an H frame orbit only if all future operations are proved equivariant on that *whole* history and the observation respects the orbit. A streaming protocol that compresses subwords independently must retain relative frame alignment, branch/provenance, and any typed future observer information necessary for concatenation. The theorem supplies a sharp obstruction to naïve orbit compression, not an unconditional impossibility of a repaired state machine.

## Exact integer verification

The accompanying Python program directly applies Burnside's lemma on all 23040 candidate H elements: for a signed monomial matrix g its number of fixed letters is twice the number of unsigned-axis fixed points with positive sign. Therefore fixed words of length N are f(g)^N (including N=0, the empty word). It independently evaluates the above Stirling partition formula and checks equality for each N=0,...,8.

N | H-word-orbits | B6-word-orbits | difference
--|--:|--:|--:
0 | 1 | 1 | 0
1 | 1 | 1 | 0
2 | 3 | 3 | 0
3 | 11 | 11 | 0
4 | 49 | 49 | 0
5 | 258 | 257 | 1
6 | 1570 | 1539 | 31
7 | 10900 | 10298 | 602
8 | 85312 | 75848 | 9464

Exact local test was executed PASS. Full mathematical statement for arbitrary N rests on the group/stabilizer proof, not extrapolation from finite checks.

## Relation to the mother objective and next independent unit

This separates (i) static signed-frame reorientation, (ii) whole-word orbit under a **common** frame action, and (iii) composition and observer safety of independently compressed subwords. The next genuine research question is a typed X6 Cell+time+triadic event map that both respects the P000 native 3-force closure and composes on provenance-preserving paths. Search for a minimal shared-frame/event memory that preserves the actual native transition, not merely the static-word orbit. Original FCC C6/C12 microtrace, finite-depth quotient and group-generator results are retained as prior frozen inputs. No completed native physical rotation, accepted Result, or independent review is claimed here.
