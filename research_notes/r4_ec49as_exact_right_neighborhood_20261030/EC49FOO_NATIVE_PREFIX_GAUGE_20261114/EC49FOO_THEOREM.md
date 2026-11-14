# EC49FOO — A native two-root prefix-tree cancellation gauge

Date: 2026-11-14. Author-proved exact algebraic result, exact Python/C++ author-checked; **NOT_REVIEWED**. Continues [EC49FON PR #2406](https://github.com/awdawmip/enterprise-math/pull/2406) at `6d9565a71f8e1e90823c7e5d504b0b696d24877a`. Scientific input pin remains `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original 94-key input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e` is unchanged. The example below is an independently **constructed native-operator instance outside the 94-key corpus**, not a new record in its 38,169 frozen cases. Historical researcher `EM-DIRECT-204C14` / Activity `RA-6893088D0A7347CE7F4D8720` are provenance, not current session authority.

## Exact two-label two-root criterion

Let each of two named demands `a,b` have exactly one (nonempty post-root) word at each of two named roots `h,s`. The native rooted-prefix cost `D_r(S)` counts the minimum number of non-root prefix vertices needed to cover the selected demands; with one word per label it is their union-prefix cardinality. Write `x_r`, `y_r` for the post-root codeword lengths, and `q_r` for the shared post-root prefix length. Then

- `D_r(∅)=0`, `D_r({a})=x_r`, `D_r({b})=y_r`, `D_r({a,b})=x_r+y_r-q_r`.

For two configurations A and B with the same legal assignments, write `Δ` for `B-A`. **Their full cost-annotated terminal graphs are identical if and only if** the following four exact integer equations hold:

```
Δ(x_h+y_h-q_h)=0,
Δ(x_s+y_s-q_s)=0,
Δx_h+Δy_s=0,
Δy_h+Δx_s=0.
```

In particular, `Δq_h=Δx_h+Δy_h=-Δq_s`: the shared-prefix change is necessarily transferred between the two named roots. **Proof.** The four terminal costs (both h, a h/b s, a s/b h, both s) are respectively `x_h+y_h-q_h`, `x_h+y_s`, `y_h+x_s`, `x_s+y_s-q_s`. Equality of their four differences is exactly the displayed system; the common-prefix identity follows by substitution. All steps reverse. QED.

## Concrete single-key swap in the native signed-prefix operator

Root 07 is hub h; root 06 is spoke s. Named demands a=7 and b=13 have legal domain `{06,07}`. A source key may contain the four label/root codewords below. Swapping one constructed key K_A for K_B gives:

| Root | Label | K_A | K_B |
|---|---:|---|---|
| 07 | 7 | `0701` | `070102` |
| 07 | 13 | `070203` | `070103` |
| 06 | 7 | `060102` | `060203` |
| 06 | 13 | `060103` | `0601` |

Each code has at most two non-root prefix vertices. The root-07 `(x,y,q)` triples change `(1,2,0)→(2,2,1)`; root-06 triples change `(2,2,1)→(2,1,0)`. In both configurations, each root's pair cost is 3.

| Assignment of (7,13) | Terminal cost A | Terminal cost B |
|---|---:|---:|
| (07,07) | 3 | 3 |
| (07,06) | 3 | 3 |
| (06,07) | 4 | 4 |
| (06,06) | 3 | 3 |

Nevertheless `ΔD_07({7})=+1` and `ΔD_06({13})=-1`; all remaining reachable rooted-set costs have zero delta. This is a **nonzero native rooted-profile change annihilated by the complete-assignment observer**. In the integral hub basis from EC49FON this is `(+1)·unary_13 + (-1)·interaction_06_{7,13}`; the coefficient of the *genuine quadratic* generator is **−1**.

### Minimal depth under the given model

With one word for each label/root, nonempty words, and maximum post-root prefix depth one, every singleton cost equals 1 and empty cost equals 0. Equal complete-terminal costs then fix each root's two-label pair cost, so all reachable rooted profiles agree. A nonzero cancellation requires depth at least two; the example attains **maximum depth 2**. This is a depth bound for the declared two-root/two-label unique-word model.

## Exact execution evidence

- `VERIFY_EC49FOO.py`: independent Python integer union-of-prefixes calculation on all four legal assignments; full rooted profiles and decomposition of the hub gauge.
- `VERIFY_EC49FOO_NATIVE.cpp`: the original native trie label-OR / min-plus DP recurrence in standalone C++17; compiled `-O2 -Wall -Wextra -pedantic`.
- `EC49FOO_RESULTS.json` and `EC49FOO_NATIVE_VERIFY.log`: passing calculations. No floating-point arithmetic.
- The originally frozen 94-key input was rechecked at the source SHA256 above. No new 94-key input or formal task record is claimed.

**Next exact question:** within the *existing frozen 94-key / 38,169-case inventory*, find a pair with identical complete-assignment cost map but different reachable root costs, or establish a corpus-specific exclusion. The current construction establishes native-prefix **operator realizability**, not frozen-repertoire membership; preserving this distinction is essential.

Research status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Existing activity preserved; formal task publication, CLAIM, Result and independent Review are not asserted.
