# X6 Unit156 — exact shuffle lift from A_p root walks to signed native Cell BRC

Date: 2026-11-19. Mother objective PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Author provenance EM-X6-FB6990 (on-hour Research lane). Status AUTHOR_PROVED / INDEPENDENT_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen real source-to-caller relations

Historical comparison commit: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, preserved separately from the original task science pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

- `src/enterprise_math/lattice_geometry.py` blob `825ee26c918a4d7007e280aeaa1d7b750cd46aba`, lines 25–45, defines the **derived** zero-sum `A_p` lattice and root-step distance `a_graph_distance=½ sum |delta_i|`.
- `tests/test_lattice_geometry.py` blob `304ff8e769f93fa0e96a03c1ffe89960ea5dd622`, lines 23–25, 64–70, calls the actual derived implementation and checks the half-L1 distance; original test not run here.
- `src/enterprise_math/geometry.py` blob `a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152`, lines 95–101, defines `l1_distance` for **standard-axis** `Z^d` adjacency.
- `tests/test_p012_geometry.py` blob `e1a8988169f12d4294e29446fb1a8558c412c77b`, lines 6–12, 97–102, imports and checks the actual L1 function; original historical test not run here.

The two accepted graph metrics have different primitive generators: `A_p` has e_i-e_j, while signed-native standard-axis Cell motion uses ±e_i. They coincide on **endpoint location** after embedding the zero-sum lattice but not on the primitive-step typing.

## New all-integer combinatorial theorem

Fix `p>=1`, `x in Z^(p+1)` with `sum_i x_i=0`, and let `m=sum_{x_i>0}x_i=sum_{x_i<0}|x_i|`. Set `P=prod_{x_i>0}x_i!`, `N=prod_{x_i<0}|x_i|!` (empty product =1).

The number of shortest labeled `A_p` root walks from 0 to x, each primitive root of form e_i-e_j, is exactly
```text
B_Ap(x) = (m!)^2 / (P N).
```
The number of shortest standard-axis **signed native Cell** walks in `Z^(p+1)` to the same endpoint x is exactly
```text
B_native(x) = (2m)! / (P N).
```
Hence for *every* such integer endpoint, including x=0 with m=0,
```text
B_native(x) = binomial(2m,m) * B_Ap(x).
```

### Constructive bijection / proof

Any standard-axis shortest walk to x has exactly m positive generator steps and m negative generator steps; it cannot include a detour or wrong sign. Extract the ordered list of its m positive-axis labels and the ordered list of its m negative-axis labels. Pair the j-th positive label with the j-th negative label: these m ordered pairs form a unique shortest A_p root-word using e_i-e_k, and the original native word also specifies which m of the 2m slots carried positive steps. Conversely any shortest A_p root-word and any choice of m positive slots among 2m reconstruct one unique signed-native shortest word by interleaving the paired positive and negative label lists. This is a two-sided inverse and proves the binomial fiber cardinality for all p,m. It preserves actual axis labels and ordered operations and does not identify a derived root generator with a native primitive.

As a direct source-type consequence, for x=(2,2,-2,-2), m=4, the derived A3 root graph has 36 shortest root words but the standard-axis signed native graph has 2520 shortest paths, with ratio binomial(8,4)=70. The **distance** differs by the factor two, while BRC path multiplicity differs by the binomial shuffle factor depending on the positive/negative mass. This explicitly repairs any downstream inference that derived root-graph BRC counts can be inserted unchanged into signed-native Cell path counts.

## Exact finite independent check

A separate exact integer dynamic-programming checker enumerated every zero-sum x in `[-2,2]^(p+1)`, for p=1,2,3,4. Case counts are 5,19,85,381 (490 total). For each, two independent recurrences counted root-paired shortest words and native-axis shortest words and checked their factorial formulas and binomial ratio. Python normal/-O/-OO exit 0, with identical canonical JSON stdout SHA256 `a746580923de4aa3cf961660d02914de50147997622ebbd72cc8a63d10ccacf1`; check guards run in optimized modes.

The checker is a standalone reconstruction of the actual frozen generator types; it did not execute historical test modules, modify frozen code, or rerun the already completed original six-file R063 benchmark.

## 28-LP role and follow-up

This adds two formerly uninspected source-to-test relations to the actual downstream 28-LP typing corpus: **derived A_p root graph** vs **native signed standard-axis Cell path BRC**. It supplies an exact operator-preserving lift with a uniform `binomial(2m,m)` shuffling correction, rather than promoting `A_p` root edges to X6 native edges. Incomplete LP011/LP019 historical faulty caller source lines remain unresolved; separate live consumer links should be audited for possible omission of this correction. Keep existing accepted/unedited current definitions, original R063 Unit50 execution, and independent Driver review intact.

No native PROGRESS or mathematical admission is inferred from this author note. The original same-owner Source continuation, RUN generation and unknown/failing operations remain governed by current authenticated Source receipts.
