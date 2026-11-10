# R692c｜E* 原生X6-BRC方向许可集合：45个未来回归观察模型的精确商分类

Date: 2026-11-10. Status: AUTHOR-PROVED / EXACT_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED.
Mother task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; frozen scientific source `a72226e2430ffa4786321ac86e7f0c599d5f0389`; R691/R691b author note `df5c9edbb18b123a828e3e6ead2a1a0f606511a5`; R692 weak-observer theorem in this PR. Researcher `EM-X6-A92507`, activity `RA-576A5340A203CDF40E51F440`. No formal CLAIM or mathematical admission.

## Definition: direction-mask persistent future protocol

Let `G=S3`, `Sigma={--,-+,+-,++}`, with source order exactly as written. For each root phase `a=0,1,2`, R691's validated native E* square enumeration gives 15-path integer kernels `n(a,sigma,g)`. Choose any **nonempty** direction subset `M⊆Sigma`; keep that same subset permitted at every subsequent four-step macro. At each macro choose uniformly one of the `15|M|` labeled pairs `(i<j,sigma∈M)`; the macro is the ordered native X6 return path with R687 E* slot update. Thus its group measure is

```text
  mu_{a,M}(g) = [sum_{sigma in M} n(a,sigma,g)] / (15|M|).
```

The only allowed future observation here is `r_k(a,M)=mu_{a,M}^{*k}(e)`: the exact probability that the full S3 frame returns to its starting frame after k macros, for any integer k>=1. Root Cell, root phase and initial full frame are held fixed; the persistent mask is hidden. By R692's trace/Newton/Cayley–Hamilton lemma, two masks are equivalent for **all** such future queries if and only if their six probabilities `r_1,...,r_6` are equal.

Direction masks are encoded by bit `1=--`, `2=-+`, `4=+-`, `8=++`, so their complete finite domain is the 15 integers `1,...,15`.

## Theorem: exact all-future quotients and sharp horizons

For this exact persistent-mask model, the partitions of the 15 masks by equality of *all* future identity-return probabilities are:

| root phase a | all-time classes | classes visible by k=1 | k=2 | k=3 | non-singleton equivalence classes |
|---:|---:|---:|---:|---:|---|
| 0 | **12** | 1 | 11 | 12 | {2,5}, {6,9,15} |
| 1 | **12** | 9 | 12 | 12 | {4,10}, {6,9,15} |
| 2 | **9** | 9 | 9 | 9 | {2,5,7}, {4,10,14}, {6,9,15} |

Every other mask is a singleton class, so the table specifies all equivalence classes exhaustively. The least horizon whose `(r_1,...,r_h)` signature reproduces the full all-time quotient is sharply `h=3,2,1` at phases `a=0,1,2` respectively.

**Proof.** For all `3×15=45` fixed phase/mask combinations, sum R691's source-verified integer kernels and form the exact group convolution through horizon six. The attached actual-run checker `R692C_ESTAR_MASK_RETURN_EXACT.js` verifies at every k that the complete mass sum is `(15|M|)^k`, computes each exact rational `r_k` using integer numerators and reduced integer denominators, and groups identical six-entry return signatures. It asserts exactly the partitions and horizon counts in the table. This covers every mask and phase; no sampling or floating point is used. Six entries completely decide all later entries by R692's proven finite-group return-trace lemma with `|S3|=6`. A horizon strictly shorter than the reported value gives strictly fewer classes, so each threshold is minimal. QED.

Numerical arithmetic is exact: `(15|M|)^6 <= 60^6=46656000000 < 2^53`, and each intermediate nonnegative mass is bounded by that total. An independent Python `Fraction` enumeration over the same 45 masks reproduced all class counts, non-singleton memberships and horizon sequences. The underlying 12 R691 group kernels were themselves reconstructed and checked against all 360 original ordered square paths by the R692 program in this same PR.

## Strong example: different full group laws, identical return observations forever

For `a=0`, the equivalence class `{2,5}` consists of the single mask `M_2={-+}` and the two-direction mask `M_5={--,+-}`. Their full one-step group measures are **different**:

```text
  mu_{0,2} = (6 e + 6 tau + 3 c)/15,
  mu_{0,5} = (6 e + 6 tau + 3 c^2)/15,
```

where `e=012`, `tau=021`, `c=120`, `c²=201` in S3. Conjugating group elements by `tau` fixes `e,tau` and exchanges `c,c²`. Hence `mu_{0,5}` is the push-forward of `mu_{0,2}` under this group automorphism. Convolution commutes with group automorphisms, which fix the identity, so

```text
  r_k(0,2) = r_k(0,5) for every k>=0.
```

This is a constructive **strictly lossy** observer quotient: exact predictions of the specified return event can merge the two masks, whereas the full group-state distribution at one step distinguishes them (e.g. probability of c is 1/5 versus 0). It is a finite exact counterexample to the proposition that all-time return probabilities uniquely determine full labeled/group transition laws.

The other duplicate groups can be checked directly from the saved kernels and signatures. Some are literally identical group measures after normalization; the above conjugate pair shows the substantive additional observation loss.

## Reproduction, source fidelity and next experiment

The JavaScript program and full JSON evidence are in this PR:
- `research_notes/portable_direct/R692C_ESTAR_MASK_RETURN_EXACT.js`
- `research_notes/portable_direct/R692C_ESTAR_MASK_RETURN_RESULTS.json`

Run `node R692C_ESTAR_MASK_RETURN_EXACT.js`; it prints the complete JSON after asserting all 45 models and partitions. The code consumes only the published, exact R691 source kernel table (checked independently against 360 native square paths by `R692_ESTAR_RETURN_OBSERVER_EXACT.js`). Full results preserve per-mask integer group counts, denominators, 0..6 probabilities, equivalence memberships and horizon counts.

Source/proof classification: E* **author-level candidate** under the frozen X6 task, not a V29 or V39 native permission reconstruction. The fixed-mask protocol is an explicit new future-operation choice. No project review or P000 promotion is claimed.

**Next discriminating unit:** obtain frozen real X6 Link/Port and V29 PASS/TRANSFER update tables. For each reachable `(Cell,phase,frame,port/source)` with identical visible state, compute allowed direction sets and update-dependent compositions. Compare **both** exact full group laws and all-time return-observer signatures. This determines when the above 12/12/9 quotient survives native state-dependent permissions or needs extra residual coordinates.
