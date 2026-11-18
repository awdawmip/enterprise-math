# EC49FFH — BRC all-low interval cover: closed-form key count and binary depth law

Date: 2026-11-09 (Asia/Shanghai). Frozen science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original six-operation native signed-X6 BRC model and nine-state observer; P000/ACTIVE worldview unchanged.

## Statement and scope

For any integer `U>=2`, require all four low signatures `{1,2,4,8}` at **each** integer horizon `h=2,...,U`. One full BRC key may support separate ordered words in multiple horizons; no word order or source multiplicity is collapsed when subsequently computing prefix costs. The complete key is `(x,y,z)` with integers `x>=2z,z>=1,y>=0`; the theorem also holds for the strictly positive-key subdomain.

Lexicographically minimize first the number of **distinct** complete BRC keys and then the sum of the native six-axis microstep lengths of **one word per selected key**. That secondary sum is a BRC depth/search proxy, not the union of signed ordered prefixes used by the parent `C_native` objective.

Define `k = ceil(log2 U)` and `s_2(n)=popcount(n)`. Then the **exact global lexicographic optimum** is

```
key_count = k
minimum_one_word_per_key_length_sum = 4*U - 4 + 6*k - 2*s_2(U-1)
```

It is attained by canonical keys `K_H=(2+floor((H-1)/2), H-1-floor((H-1)/2), 1)` at the terminal horizons

```
H_i = 1 + ceil(U / 2**(k-i)) ; i=1,...,k.
```

The displayed sorted horizon tuple is componentwise smallest among all minimum-key covers.

**Exact increment corollary** for every integer `U>=2`:
```
L_min(U+1)-L_min(U) = 2 + 2*v_2(U) + 6*indicator(U is a power of two).
```

## Analytic proof (unbounded U)

By EC49FFD's exact nine-state staircase, a complete key with terminal horizon `H=x+y-1` has low-support interval contained in the interval of the canonical key `K_H`:

```
ceil((H+1)/2) <= h <= H-1,
equivalently h+1 <= H <= 2*h-1.
```

The canonical key is legal and strictly positive for every `H>=3`, and produces all four low signatures at every integer horizon in this interval. Its path length is `2(H+1)`; EC49FFC proves an arbitrary key with the same `H` has length `2(H+z)>=2(H+1)`. Hence canonical replacement preserves or improves coverage, key cardinality and the stated length proxy.

Consider any *minimum-cardinality* standard-key cover with increasing distinct terminal horizons `H_1<...<H_m`. Low `h=2` requires `H_1=3`. The low coverage intervals have both their left and right endpoints increasing with `H`. Since every integer horizon through `U` is covered, and no selected key in a minimum cover is redundant, successive intervals must touch or overlap:
```
H_{i+1} <= 2*H_i-1 ;   H_m >= U+1.
```
Induction from `H_1=3` gives `H_i<=2**i+1`, hence `U<=2**m` and `m>=ceil(log2 U)=k`.

With `k=ceil(log2 U)`, define `H_i^*=1+ceil(U/2**(k-i))`. As `2**(k-1)<U<=2**k`, the tuple begins at 3, ends at `U+1`, increases strictly, and obeys `H_{i+1}^*<=2H_i^*-1` from `ceil(2t)<=2ceil(t)`. It therefore covers every required low window, proving `m=k`.

For any other `k`-key cover, iterating the adjacency inequality *backwards* from `H_k>=U+1` forces
```
H_i >= 1+ceil(U/2**(k-i)) = H_i^*.
```
Together with the native length lower bound `2(H_i+1)`, this gives the claimed componentwise and total-length optimality.

Finally `ceil(U/2**j)=floor((U-1)/2**j)+1`. Since `U-1<2**k` and
`sum_{j>=0}floor(n/2**j)=2*n-s_2(n)`, a direct binary digit expansion identity,
```
sum_i 2(H_i^*+1)
 = 2[2k + sum_{j=0}^{k-1} ceil(U/2**j)]
 = 2[3k + 2(U-1)-s_2(U-1)]
 = 4U-4+6k-2s_2(U-1).
```
Taking the difference and `s_2(U)-s_2(U-1)=1-v_2(U)` proves the increment corollary.

## Independent exact evidence

`VERIFY_EC49FFH.py` uses a *separate* zero-one subset-mask dynamic program over all candidate standard terminal horizons `H=3,...,2U-1`, calculating the minimum lexicographic pair for each coverage mask. It does **not** run this proof's backward recurrence. Actually executed locally for every `U=2,...,16`: **15/15 exact matches**, with 948 maximum mask states. Additional arithmetic/interval checks at `U=17,18,19,31,32,33,63,64,65,100,1000,1000000`. `U=8`: `(3,5,9)`, sum 40. `U=9`: `(3,4,6,10)`, sum 54. `U=10`: `(3,4,6,11)`, sum 56.

The verifier and JSON report are published adjacent to this proof; complete local execution originals are preserved separately. No floating arithmetic was used.

## Research frontier

The frozen parent problem remains `full BRC keys <=5` and ordered six-axis signed-native **prefix-union edge cost `C_native<=93`**, with its actual required observer quotas. The present theorem is an unbounded exact solver for the all-low **quota/depth surrogate** subproblem. It can eliminate keys whose depth or key count is unnecessarily high, while exact native prefix optimization still retains every ordered word and full key.

**Next EC49FFI:** select an actual 22-path quota mask not contained in the EC49FEO/EC49FEU special families; enumerate legal original words under the frozen pin and compare standard/nonstandard full keys by exact signed prefix union, seeking a <=93 witness or a lower-bound certificate.

## Provenance and control

Frozen pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. EC49FFC length identity: `2dd856c416f111d90d523dcb10cde952248ec814`. EC49FFD staircase: `df0dbc54707a6926db858631e5a03fea189dccde`. EC49FFF canonical domination: `58cdba9c360bc180028183cff711405d2e2f37c0`. EC49FFG interval oracle: `300afbaf0168095367c8c006306c07e628b0fcac`. Current rules read separately: global main `c178d0d5a43cae0843bb1239c5c7dbe118fb1a20`; EM main `4a4325cc35b5721f9c7187f1f227540d1c1109a9`. Native dispatch and session-start were queued at last check. No formal CLAIM, Owner verification, native Result or Driver acceptance claimed.

**Status:** `AUTHOR_ANALYTIC_THEOREM / EXACT_INTEGER_DP_PASS_U2_TO_U16 / PORTABLE_RESEARCH_DRAFT / NOT_ADMITTED`.
