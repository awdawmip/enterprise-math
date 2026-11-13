# EC49FNG — exact 2,000 BRC configurations and an eight-prefix root-07 exclusion certificate

Date: 2026-11-13. Author-side continuation from [EC49FNF PR #2246](https://github.com/awdawmip/enterprise-math/pull/2246), which completed indices 22000–22999. This note covers the next **nonoverlapping** interval **23000–24999**. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact model and computation

The frozen nine-state original BRC catalogue contains 178,850 lawful operation words, 94 complete cache keys and 24 observation labels. A radius-three seven-key configuration K is one of 38,169 lexically indexed key sets. `C(K)` is the minimum number of **distinct nonempty ordered, signed native X6 microstep prefixes** among lawful original BRC words covering all 24 observation labels. The original path order, signs, branch identity and provenance are retained; no endpoint or unsigned quotient is taken.

The C++17 exact prefix-trie/subset optimizer scanned all 2,000 cases with exit 0 and `FINISHED`. For every first-microstep root r, its eligible lawful word trie defines `f_r(S)`: the minimum activated nonempty prefix nodes covering every label in S, permitting extra covered labels. Its exact bottom-up integer DP and exhaustive assignment of 24 labels to eligible roots yield C(K). Every lawful cover induces a feasible root assignment, and every optimum root DP solution reconstructs lawful words, giving matching upper and lower bounds in this finite, pinned catalogue.

**Complete result:** min = **96**, attained exactly at **23479, 23490, 24950**; max = **204**, attained at 23072, 23168, 23170, 23171, 23172, 23173, 23174, 23177, 23178. There are 89 distinct optimal costs across the interval. Each of the three minimizers has a reconstructed 24-word lawful witness with **48 + 48 = 96** native signed prefixes in first roots `05`, `06` and none in root `07`. Independent Python native trie/subset optimization matched C++ at 23000→136, 23479→96, 23490→96, 24950→96 and 24999→150.

| Case | Seven key indices | f05(full) | f06(full) | f07(full) | C(K) |
|---|---|---:|---:|---:|---:|
| 23479 | 0,4,5,11,16,32,34 | 48 | 48 | 43 | **96** |
| 23490 | 0,4,5,11,16,32,46 | 48 | 48 | 43 | **96** |
| 24950 | 0,4,5,11,19,32,49 | 48 | 48 | 38 | **96** |

## Finite structural theorem: exact shadow margin 8

For these three configurations, eligible labels at roots 05 and 06 form a disjoint 12+12 partition `L=L05 ⊔ L06` of the 24 labels. Root 07 can receive exactly eight labels `Q={5,7,11,13,15,17,19,21}` (in the frozen catalogue's integer label indexing); `Q` is contained in `L`. The exact global integer optimization can therefore be written with only **256** possible transfer masks:

`C(K) = min_{T subset Q} [ f05(L05\\T) + f06(L06\\T) + f07(T) ]`.

For a given K define the **root-07 shadow margin**

`m_K(T) = f05(L05\\T) + f06(L06\\T) + f07(T) - f05(L05) - f06(L06)`.

The complete C++ integer root-function tables (4,096+4,096+256 subset values for each K) give `m_K(empty)=0` and **`min_{nonempty T subset Q} m_K(T)=8` for all three minimizers**. Of the 256 masks, **exactly one** has margin zero in each case: the empty mask. Thus the entire first-root allocation is uniquely optimized by using no root-07 words; every nonempty root-07 transfer has at least an **eight-prefix penalty**. This certifies the three optima via a strict, finite exchange inequality rather than relying only on the displayed 24-word upper bounds.

**Proof of the reduction and certificate:** every label assigned to 07 belongs to Q, so the 07-assigned labels are exactly one subset T of Q. All remaining labels must be assigned to their unique root, 05 or 06. The three root prefix tries are disjoint, and their subset-closed exact costs add. Conversely any such T and chosen root trie solutions generate a lawful cover. Subtracting the no-07 cost (48+48) gives the margin identity. Exhaustively checking the 255 nonempty 8-bit masks gives the stated strict lower bound. A generic reusable consequence: whenever a similarly typed three-root configuration has `m(T)>=g>0`, its zero-transfer root allocation remains uniquely optimal under any perturbation decreasing every nonempty transfer's relative total cost by less than g while leaving the zero-transfer reference unchanged.

The pair 23479→23490 replaces key **34→46** and preserves the global optimum and the eight-prefix shadow gap, although its root functions are not equal and neither weakly dominates the other. Across the 8,448 matching root masks, exact `(23479 better / equal / 23490 better)` counts are: root 05 **1059/2861/176**, root 06 **1004/2916/176**, root 07 **54/190/12**. This is a concrete cost-invariance certificate with asymmetric internal root-function changes.

## Verifiable evidence and limits

The compressed companion `EXACT_CERTIFICATE_EC49FNG.json.xz.b64` expands using `base64 -d ... | xz -d` to lossless JSON containing all **2,000 unsigned-byte optimum costs**, three complete 24-word original-word witnesses, complete source hashes and the shadow-margin distributions. A local full evidence archive also includes the unchanged frozen source, exact C++ code, original 2,000-row solver stdout and completion stderr, original-generator witness reconstruction, full root-function mask dumps, the exact 256-transfer checker, independent Python root-trie solver and SHA256 manifest. `VERIFY_EC49FNG.py` checks the lossless vector, lawful witness words, signed prefix counts and the shadow certificate in that full evidence environment. The 2,000-case lower-bound claim relies on rerunning the supplied exact C++ optimizer, not merely on the vector checksum.

- Frozen master text SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- Full 2,000-row C++ output SHA256: `34601fcd8796b94b5a5c235cef34e8f16f3ee671914b49a8792ce9f70bad165d`.
- Exact 2,000-byte cost vector SHA256: `5e527d78e4cb1e1235146e95cc3621db725d006a9bff8250eb13a2e213b2cbce`.
- Expanded compact certificate SHA256: `db7a2adaaee468ecd8dec251c15dfd6a9d59ae3f191494cd7259f17951fb0bab`.

The nonoverlapping author-side contiguous radius-three coverage now reaches **25,000/38,169 = 65.50%**. Its best found optimum remains **86** (indices 21524 and 21525 from PR #2243). The unrestricted seven-key parent search has its separate 84-prefix feasible construction. This is author-side mathematics; native Task/CLAIM/Result and independent Driver admission are separate project control states.

**Next contiguous configuration: 25000**; **13,169 remain**. A useful next scientific question is whether eight-prefix shadow gaps persist under other single-key substitutions and whether the 256-mask certificate predicts cost-flat families without recomputing each full 24-label assignment.
