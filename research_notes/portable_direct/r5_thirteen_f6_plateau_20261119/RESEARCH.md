# R5 — exact 244-way thirteen-label plateau through six unflagged errors

Date: 2026-11-19 Asia/Shanghai. Role: independent portable TASK_RESEARCH, historical provenance EM-DIRECT-4C3E47. Status: **AUTHOR_EXACT_FINITE_CHECKED / COMPLETE_INDEPENDENT_SUPPORT_SIGNATURE_CHECK / NOT_REVIEWED**. No new CLAIM, native Result or mathematical Review.

## Input and scope

Preserve the frozen scalar R5 input: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`, `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b` (1,549,048 bytes), and its `stages_18.json`. For every named label h=0,...,255 and price k=214,...,314 there is one exact integer scalar center N_h(k). Fix the robust endpoint tau=58182461585441404127941754879; a correct scalar response y satisfies 2|y-N_h(k)|<=tau. At most f arbitrary, unflagged responses are errors. Minimize the worst-case sum of physical query prices.

The preceding **published twelve-label** evidence is `research_notes/portable_direct/r5_twelve_pair_synergy_20261119/RESEARCH.md` at `enterprise-math@3cc19a1b5b6588a5d1e191615d130386db8bec27`. Fix its distinguished W=(0,16,32,48,1,64,17,80,18,24,34,82), known to attain V_8(W)=8335. No native BRC/Port equivalence is inferred from a scalar mask quotient.

## Theorem R5-13-F6

For **every** t in {0,...,255}\W (all 244 distinct original names), and **each integer** 0<=f<=6,

```
V_f(W union {t}) = 735 + 950*f.
```

Thus the seven exact optimal-price values are `(735,1685,2635,3585,4535,5485,6435)` for every one of the 244 extensions. This finite quantifier covers precisely the frozen robust noise endpoint, allowed original 101 prices and declared scalar observer, not variable tau or f>=7.

## Price-aware joint-support quotient

All 244 eleven-to-thirteen augmentation instances have exactly **48** distinct priced maximal joint-support signatures. Class-size histogram: 20 classes of size 1, 8 of size 2, 8 of size 4, 8 of size 8 and 4 of size 28 (20+16+32+64+112=244). Each exact 13-label priced signature was solved for f=0,...,6 with no state-cap error. `ALL244_VALUES.csv` preserves every original t and the seven values. The full locally executed raw CSV additionally preserves its class id; SHA-256 `9fd79fa85ea108c0b161508278a1d8084c5340ac86278462245935f8123a4761`.

## Exactness argument

For any action k, the scalar response support is M_k(y)={i: |2y-2N_i(k)|<=tau}. Every nonempty support is contained in a support attained at the greatest left endpoint among the intervals containing y. Thus inclusion-maximal supports occur at the 13 doubled left endpoints 2N_i(k)-tau and use the exact integer membership predicate 0<=N_j(k)-N_i(k)<=tau. For finite capped error vector e_i in {0,...,f+1}, a support M increments each incompatible counter, capped at f+1. With <=1 live e_i<=f, V(e)=0. Otherwise

```
V(e) = min_{k with no support containing all live labels}
       ( k + max_{M in maximal_supports(k)} V(T_{k,M}(e)) ).
```

Inclusion-maximal supports suffice by monotonicity of the remaining identification game in each error counter. Positive-price actions admitting a support containing every live label can leave the relevant state unchanged and cannot improve a terminating minimax policy. Every other transition strictly advances at least one still-live counter, so this is a finite acyclic exact minimax recurrence. Identical full maximal-mask families have identical transitions and admit the cheapest representative k. None of these reductions merges original hypothesis names or inferred latent Port provenance.

## Recalculation and validation boundaries

The byte-verified local frozen input produced `window_adj.bin` with 101×256×256 exact integer comparisons. The C++17 solver `R5_THIRTEEN_EXACT.cpp` evaluates all 244 original t, deduplicating into 48 full price-aware signatures and solving every signature for f=0,...,6, with cap 5,000,000 nonterminal states per class and no cap hit. A completion log reported `CLASSES 48`, `PROFILE 735,1685,2635,3585,4535,5485,6435, 244`. Independently, Python reconstructed all 244 complete signatures directly from the frozen integer centers using doubled left endpoints, without reading `window_adj.bin`; it verified all class IDs in the raw complete table and all seven per-name values against the C++ table. This **checks independent support reconstruction and census integrity**, not an independent f>=1 Bellman implementation. A previous local bundle also independently checked the 12-label W result via a separate C++ oracle.

The historical f=0,...,3 13-label computation was already available locally; this run extends its complete exact scope to f=4,5,6. Attempts to extend the full 48-class computation to f=7 exceeded the bounded run, and **do not certify f=7 or f=8 for all 244**. Four already computed specific t at f8 had value 8335; that finite sample is not a universal 13-label plateau theorem. Full 256-label bound remains 8335<=C*_8<=8343.

## Next exact problem

Either finish the f=7/8 thirteen-label signatures with controlled search/memory bounds or find one thirteen-label t forcing V8>8335 by a rigorous adversary lower certificate, before attempting any scalar-to-native residual/Port transfer. Preserve original names, full joint supports, physical costs and frozen source pin.
