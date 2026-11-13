# EC49FNN — Exact native-BRC seven-key radius-three, indices 32000–32999

Date: 2026-11-13. Status: author-side finite exact computational result, NOT_REVIEWED; no formal CLAIM, Result or Foundation admission. Predecessor: [EC49FNM PR #2296](https://github.com/awdawmip/enterprise-math/pull/2296). Frozen scientific pin (unchanged): `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact problem and theorem

Original nine-state BRC: 178850 original lawful operation words; 94 complete cache keys; 24 demand labels; 38169 indexed radius-three seven-key configurations. Paths preserve ordered, signed native-X6 microsteps, first-root identity, original branch and provenance. For a seven-key configuration K, C(K) minimizes the number of **distinct nonempty original signed-native prefixes** of lawful words covering all 24 labels; equality of final coordinates is not a substitute for prefix identity.

A fixed C++17 exact trie / demand-subset DP enumerated all 1000 indices 32000 through 32999, in four contiguous jobs each with a `FINISHED` log. The finite result is

```
min_{32000<=i<=32999} C(K_i) = 122.
```

The only minimizers are:
- 32970: [0,4,5,11,39,43,61], roots 05:54 + 06:68 = 122; best strictly higher root allocation 123.
- 32997: [0,4,5,11,39,46,49], roots 05:56 + 06:66 = 122; best strictly higher root allocation 124.

The largest cost in the interval is 204 at 32813 and 32936.

## New finite one-key replacement counterexample

`32281=[0,4,5,11,37,39,47]` and `32551=[0,4,5,11,37,47,50]` differ by one cache key 39→50.

| Case | Exact minimum C | Number of minimizing root-demand assignments | Next strictly higher root-assignment cost | Positive gap |
|---|---:|---:|---:|---:|
| 32281 | 134 | 1 | 140 | 6 |
| 32551 | 134 | 5 | 135 | 1 |

For 32281 a minimizer uses roots 05:63 and 06:71. For 32551 one minimizer uses roots 03:38, 05:46 and 06:50. Thus preservation of the exact minimum by a one-cache-key replacement does **not** preserve the multiplicity of minimizing root assignments or the gap to the next distinct root-assignment value.

The finite histogram of minimizing root-demand assignment counts (multiplicity: number of configurations) is:
`{1:421,2:466,3:62,4:29,5:6,6:2,7:2,8:10,12:2}`.

The positive gap histogram (gap: number of configurations) is:
`{1:703,2:156,3:86,4:9,5:19,6:11,7:16}`.

## Exhaustive method, direct evidence, verification scope

Within each first-step root r, build a trie of all original legal words for the selected complete cache keys. Terminal masks store the original observation labels. Bottom-up exact integer DP followed by superset-min closure computes f_r(S), the minimum nonempty rooted-prefix count covering required label set S (extra incidental coverage allowed). Enumerating **every admissible assignment** of the 24 labels to available roots minimizes sum_r f_r(S_r). Distinct first microsteps imply disjoint nonempty prefix sets across roots, hence the decomposition is exact. Count the assignments at the minimum and the least strictly higher sum to obtain multiplicity and positive gap.

Original frozen master input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; indexed configuration file SHA256 `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`; generator SHA256 `0fbfa02b8b9b526b44f105c93a187c809e3279954cb074149af87ac271d2b9d3`. The source is reused from EC49FNM's pinned reproducibility bundle, not changed.

The saved full EC49FNN reproduction archive contains the frozen master input, original generator, C++17 solver, four full 1000-row scan segments and FINISHED logs, all prefix certificates, Python verifier and SHA256 manifest. Its `EXACT_CERTIFICATE_EC49FNN.json.xz.b64` contains the complete lossless 1000-row costs, root-allocation multiplicities, second distinct costs, root counts and original lawful-word witnesses for four cases.

An **independent Python trie DP and allocation enumeration**, not consuming C++ root-function tables, recalculated the full (minimum, minimizing-assignment count, second-distinct cost) triple for 32281=(134,1,140), 32551=(134,5,135), 32970=(122,1,123), 32997=(122,1,124). Additionally each of these four configurations has a reconstructed set of 24 lawful original operation words covering all 24 labels and attaining exactly 134,134,122,122 distinct nonempty signed-native prefixes respectively. The remaining 996 cases are exhaustively calculated in C++ but not independently recalculated in Python.

This is an exact **finite indexed family** result; it does not lower the earlier 86-prefix minimum for the larger radius-three family or the separately reported 84-prefix feasible construction for the global seven-key problem. With prior author-side ranges, the computed continuous prefix reaches 33000/38169; remaining indices begin at **33000** (5169 cases).

Next question: give local root-function inequalities that predict when one-key substitution preserves C(K) while changing the argmin degeneracy and second-gap, retaining source label and named signed-native root semantics.

Formal task owner/claim/Result remains governed by native Source events and independent Driver review; this research PR is not task admission.
