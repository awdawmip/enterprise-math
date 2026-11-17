# R762DI — Paired triadic X6 path blocks: native return, exact area spectrum and BRC seed cost

Date: 2026-11-17. Research line: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Researcher: EM-X6-3050F6, original session MCP-4b2d70a97f594366a7c94a0f8b45df38. Mathematical author proof with exact finite verification; independent review: NOT_REVIEWED.

## Frozen premises and exact object

Scientific inputs are fixed at awdawmip/enterprise-math@e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md and P000 V5 at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Use the signed native Cell torsor Z^6 and ordered path-area cocycle from R762DD, Draft PR #2641@29f57350d6c661d4783f012381f5a58f8a7d8b45. R762DH's triangle observer compression is a distinct, conditional downstream observer.

A **candidate triadic path block** is a word of length three with three distinct native axis labels S={i,j,k}, each appearing exactly once and with independently declared signs epsilon_a in {+1,-1}. The block is a primitive-coordinate *path object*, not a declaration that a force triple satisfies the native TRIADIC_CLOSURE_E predicate. All six spatial axes and the distinct time coordinate remain as P000 specifies. A 15-component area record describes ordered history, not new native spatial directions.

For an ordered signed path H=(d_1,...,d_m), define v(H)=sum_t d_t and for a<b define A_ab(H)=sum_{r<t}(d_{r,a}d_{t,b}-d_{r,b}d_{t,a}), as in R762DD.

## Theorem I — sharp Cell-return obstruction and six-step paired return

No odd-length word of signed native unit-coordinate steps can return to the same native Cell. In particular **no three-step candidate triadic block is a native Cell-return loop**, regardless of signs, supports or order.

For two consecutive length-three blocks each with three distinct axes, a native Cell return is possible if and only if their signed axis-step multisets are exactly opposite. Consequently the shortest Cell return formed from an integral number of such three-step blocks has exactly two blocks, hence six primitive steps. Once the first block has support S and signs epsilon, the second block must have precisely support S and signs -epsilon, though its order remains arbitrary.

Proof: the integer coordinate sum sum_a v_a changes parity at every signed unit step, so after any odd number of steps its parity differs from the initial Cell. For two three-step blocks, each coordinate of each block's v is 0 or +/-1, and the sum can vanish precisely when the second displacement is the first's negative; distinct-axis support makes the signed multiset unique. The construction (epsilon_i e_i,epsilon_j e_j,epsilon_k e_k,-epsilon_i e_i,-epsilon_j e_j,-epsilon_k e_k) attains six steps. This concerns returns **under the two-triad-block restriction**; the unrestricted coordinate graph admits two-step backtracks.

## Theorem II — exact 36-history area spectrum

Fix one support S={i,j,k}, one sign pattern epsilon, and regard each ordering u of the three first-block steps and each ordering w of the corresponding opposite second-block steps as separately named, equally weighted N-BRC histories. There are precisely 3! times 3! = 36 such paths. They all have the same native Cell endpoint, length six, and full signed-direction histogram.

For each pair a<b in S, put s_u(a,b)=+1 if a precedes b in u, and -1 otherwise. Then

    A_ab(H_{u,w}) = epsilon_a epsilon_b [s_u(a,b) + s_w(a,b)] in {-2,0,+2},

with all other X6 area coordinates zero. The area-concatenation cocycle contributes no cross term because the two block displacements are v and -v. There are exactly **19 distinct integral area vectors**, with N-BRC multiplicities:

| Area class | Distinct area values | Named paths for each |
|---|---:|---:|
| All three area entries zero | 1 | 6 |
| Exactly one nonzero pair | 6 | 2 |
| Exactly two nonzero pairs | 6 | 2 |
| All three nonzero | 6 | 1 |
| TOTAL | 19 | 36 |

This 19-state result holds for *any* support and any chosen epsilon; multiplying each pair coordinate by epsilon_a epsilon_b is a bijection.

Finite proof: fix u. The six possible w consist of the same ordering (three agreements), the reverse ordering (zero agreements), two relative permutations with one agreement, and two with two agreements. Over the six u, all-zero occurs six times; each of the six possible full transitive orientations occurs once. The 12 one-agreement pairs yield the six signed singleton vectors twice each; likewise the 12 two-agreement pairs yield the six admissible signed doubleton vectors twice each. The attached executable also checks every one of the 36 cases by the defining six-step area sum rather than relying on this counting description.

## Theorem III — modular observer and minimal equal-seed BRC cost

For each q>=2 observe A(H) mod q on the same fixed support/sign fibre, and define M_q as the minimum number of equiprobable *initial deterministic seeds* needed to reproduce that single-time area outcome distribution exactly, with no later randomness. Then:

| q | Area readout classes | Exact class-weight histogram | M_q |
|---|---:|---|---:|
| 2 | 1 | one class of weight 36 | 1 |
| 4 | 8 | six classes of weight 4 and two of weight 6 | 18 |
| every q>=3, q!=4 | 19 | six classes of weight 1, twelve of weight 2, one of weight 6 | 36 |

Proof: all area entries lie in {-2,0,2}. These entries are mutually distinct modulo q exactly when q>=3 and q!=4. For q=2, every area coordinate vanishes. For q=4, +2=-2 while 0 remains distinct; every subset of the three pair positions is realized, giving 2^3=8 classes. The empty and full supports each have mass 6; each of the six nonempty proper supports mass 4. Given N=36 equiprobable original paths with integer class counts c_x, a deterministic uniform-seed model on M equally weighted seeds reproduces all probabilities c_x/36 iff 36 divides M c_x for every x. The least such M is 36/gcd_x c_x, giving 1,18,36. The construction assigns exactly M c_x/36 seeds to each outcome.

This is a **single-time marginal** BRC certificate for the declared area observer, not a full path-provenance or native future-operation safety claim. In particular, two histories with A=(2,2,2) and (-2,-2,-2) on S are identical mod 4 but distinct mod 8, despite identical endpoint, time and direction histogram. Thus an observation language that later permits a mod-8 query cannot safely use the mod-4 quotient.

## Exact verification and reproduction

Companion R762DI_PAIRED_TRIAD_VERIFY.js enumerates 20 distinct three-axis supports in X6, 8 sign patterns each, and all 36 pairs of orderings, totalling 5,760 six-step words. It independently computes the 15-component ordered area from the native word, checks the displayed algebraic formula and native return, and checks for q=2,...,16 that every support/sign fibre has the stated modular histogram and M_q. This is 160 signed-support configurations, 2,400 modular histograms, and 86,400 word/modulus pair assignments. Arithmetic uses only exact integers. The general parity argument is proved for all odd path lengths; the 36-state statement is a complete finite classification.

## Source-bound interpretation and unresolved question

The observation fibre here is explicitly **paired candidate triadic blocks**, not the as-yet-unlicensed force-balance operation TRIADIC_CLOSURE_E. P000 requires exact three-force primitive stability and prohibits identifying a projection return with a native Cell return. The result supplies a sharp type-check for any proposed native event rule: a three-force closure event may be relational/stable without being a 3-step Cell loop; if a model asserts both, it conflicts with the existing signed native Cell adjacency unless it introduces a separately typed transition or additional state semantics.

Next: pin the actual permitted Cell/Link/Port event predicate and V17/V29/V39 transport. If licensed events include paired triad path blocks, determine whether their legal future observers distinguish 19 integer area classes, the q-dependent quotients, ordered microbranch origins, or an even larger path fibre. Retain all provenance until a future-language-specific descent certificate is proved.
