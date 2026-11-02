# EC49ES — Exact complete H=6 three-resource Pareto frontier for native X6/BRC

**Research date:** 2026-11-02. **Parent:** EC49ER at `ed3ade49956f8a4deba33d0718097d5b30657539`, Draft PR #1730. **Deliverable:** author-side finite exhaustive theorem, exact integer-DP computation, independent native-path and solver checks. **Admission:** `PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`.

**Immutable scientific inputs inherited from EC49ER/EC49EQ:** global scientific pin `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. These pins fix scientific assumptions; they do not replace current behavioral policy. Current read of global canonical `main@41469f7a38c888c0cba5a7324b90d92ac2664700` and EM control `main@80f47c5080f82e11f23708516aa337f3504ff261` was used only for rules/control context. Protected P000/ACTIVE worldview remain unchanged.

## 1. Exact population and three costs

Work in the ambient six-dimensional native X6 signed cell torsor; the following **restricted path family** happens to have coordinates 4–6 equal to zero and does not redefine native spatial dimension. Native words comprise the seven operation tokens:

```
a=(-E1,-E1), b=(-E2,-E2)
c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1)
e=(+E3,+E1,+E1,-E3), f=(+E1,-E1), g=(+E2,-E2)
```

A horizon-`h` word has exactly `h` operation tokens and is legal when its *ordered signed primitive path* returns net displacement `(2,0,0,0,0,0)`. For each `h=2,3,4,5,6` choose finitely many legal words all with one identical complete **six-component positive-step count** `p(h)`. Their collective nine-state first-A/B-event terminal observation map (five mutually exclusive terminal buckets) must have rank 9 over rational numbers. Preserve word identity, signed primitive order, and the terminal transfer signature separately.

For the selected union, define:

* `E`: number of distinct **nonempty ordered signed primitive-step prefixes**. Prefixes are charged once globally, including across horizons; this is an algorithmic path-edge count, not elapsed time.
* `M`: number of distinct **complete six-component** vectors `p(h)`, which key pairs of symbolic positive-weight BRC multiplication factors. The distinct word/time/path states are not identified by this cache.
* `S`: number of distinct nine-state exact terminal transfer signatures; the nine-state observation representation is retained when grouping equal signatures.

For `h=2`, the essential words `ce,de,ec,ed` give `E=28`, one positive-step key `p0=(3,1,1,0,0,0)`, and four mandatory signatures `T4`. The other possible essential signature family `T2` has two members and occurs exactly in a full-rank `q=0` fiber; `q` counts `c,d`. Finite all-fiber rank checks through `h=6`, and the EC49EL/EC49ER transfer classification, establish that every rank-nine fiber has exactly one inclusion-minimal signature family: `T4` for `q>0`, `T2` for `q=0`. Removing optional extra signatures/words cannot increase any of `E,M,S`. Thus nondominated solutions have `S=4` (all later fibers `T4`) or `S=6` (at least one `T2` fiber).

## 2. Main theorem: full H=6 Pareto set

For the declared population, the full nondominated set, under coordinatewise minimization of `(E,M,S)`, is **exactly**

\[
\boxed{\mathcal P_6=\{(54,4,6),\ (60,5,4),\ (68,3,6),\ (72,4,4),\ (84,3,4),\ (90,2,6)\}.}
\]

Equivalently, the resource-conditioned sharp minima are:

| BRC keys `M` | signatures `S` | exact minimum `E` | provenance |
|---:|---:|---:|---|
| 2 | 6 | **90** | inherited verified EC49ER, three exhaustive p assignments |
| 3 | 6 | **68** | inherited verified EC49ER, 424 p assignments |
| 3 | 4 | **84** | inherited verified EC49ER, ten p assignments |
| 4 | 6 | **54** | inherited EC49EM edge-only theorem, nested native paths |
| 4 | 4 | **72** | **new EC49ES**, exhaustive 647 candidate assignments |
| 5 | 4 | **60** | **new EC49ES**, exhaustive 5,349 candidate assignments with exact pruning |

At `S=6,M=5`, the feasible region is dominated by `(54,4,6)`, because 54 is the globally proved edge-only minimum. A single BRC key cannot cover h=2 through 6, and at most five distinct keys occur because there are five selected horizons. These exhaust the resource classes after elimination of unnecessary signatures. All six listed triples are realized by actual signed-native words and are pairwise non-dominating.

**Consequences:** restricting observation storage to four transition matrices raises the edge-only optimum 54 to 60 and uses one extra BRC cache key (five rather than four). If the cache allows only four keys and the observer remains four matrices, the exact edge cost is 72. These are *counts* for the declared path population; measured computation time, bit-cost, memory for constructing the input, precomputation, and hardware-specific speedup are not inferred.

## 3. New finite optimality proof for S=4

For `h=3,4,5,6`, complete exact enumeration of full-rank `T4` positive-step fibers gives respectively **3, 7, 13, 22** choices. The product has 6006 assignments of `p3,p4,p5,p6`; the forced `p0` is counted separately. Exactly **10** assignments have `M=3`, **647** have `M=4`, and **5349** have `M=5`. The ten `M=3` cases were already solved by EC49ER. The new proof covers the entire remaining population by an exact short-horizon lower bound and a complete integer prefix-trie DP over the survivors.

**Prefix-free terminal-edge lemma.** Each of the seven native operation encodings is prefix-free in signed primitive steps: all first-two-step pairs are distinct. Hence a complete six-operation word cannot be an ordered primitive prefix of any completed word with at most five operation tokens. At `h=6,S=4`, four distinct terminal signatures `T4` are necessary, so at least four distinct six-operation word terminals are selected. Each has a different last primitive prefix edge, absent from the union of the shorter-horizon word prefix tries. Therefore, for every fixed `(p3,p4,p5,p6)`:

\[
  E_{2:6}(p_3,p_4,p_5,p_6)\geq E_{2:5}^{\min}(p_3,p_4,p_5)+4.
\]

The right side is a **lower bound**, irrespective of how the four `h=6` words share earlier prefixes with shorter words. This is why the screening rule is rigorous rather than heuristic.

Compute `E_{2:5}^{min}` by the complete signed-prefix integer OR-mask DP of EC49ER on all **273** triples `(p3,p4,p5)` (`3×7×13`). With a previously exhibited **feasible** bound `B4=80` for `M=4,S=4`, any four-key assignment with `E_{2:5}^{min}+4>80` cannot improve the bound and is discarded. **267** of the 647 assignments are excluded; the remaining **380** are solved exactly with threshold 80. Their minimum is **72**, attained by native words in Section 4. This improved the prior upper bound of 80 by eight primitive edges.

Likewise, the known nested four-signature construction supplies **feasible** bound `B5=60` for `M=5,S=4`. The same certified screen excludes **5,173** of the 5,349 assignments, leaving **176**. Each survivor's exact minimum at or below 60 is computed by a bounded integer DP, and the minimum is **60**. For every pruned cell or dynamic-programming state the accumulated native-edge cost already exceeds its feasible bound; all later contributions are nonnegative. Thus bounded DP can discard that cell without losing a solution at or below the bound. The four- and five-key enumerations together prove sharp global minima **72 and 60**.

**Exact DP recurrence.** Build the trie of every legal word in each chosen full-rank fiber whose terminal signature belongs to its four essential T4 signatures. Color terminal nodes with the 16 required bits `(h,signature)` for `h=3,..,6`. At each signed primitive-prefix subtree record the lowest integer cost for each achievable OR-mask. Merge children with `(m1,c1)\otimes(m2,c2)=(m1\lor m2,c1+c2)`, take the minimum cost for equal masks, and charge the current edge exactly once when retaining any nonempty collection of its descendant terminals. The 28 baseline `h=2` edges are already paid and are charged zero for reuse. This computes the minimum additional edge count for each fixed assignment. In the bounded implementation, states with incurred cost above `B−28` are dropped by nonnegativity; an exact solution at or below `B` is unaffected. The full 16-bit target OR-mask establishes four observer signatures for each of the four later horizons. Terminal path and complete positive-step information are never quotient-erased.

The finite proof relies on exhaustive word/fiber/assignment coverage, this recurrence, the certified screening lemma, the recorded executable source, and the actual execution results; it does not infer universal-window or runtime results from a finite search.

## 4. Explicit attaining words

For the **new optimum `(72,4,4)`**, use the mandatory `h=2` words `ce,de,ec,ed` and:

| h | four words | complete p (final axes 4–6 zero) |
|---:|---|---|
| 3 | `ceg,deg,ecg,edg` | `(3,2,1)` |
| 4 | `cegg,degg,ecgg,edgg` | `(3,3,1)` |
| 5 | `ceggc,deggd,ecggc,edggd` | `(4,4,1)` |
| 6 | `ceggfg,degggf,ecggfg,edgggf` | `(4,4,1)` |

For the **new optimum `(60,5,4)`**, again retain the mandatory h2 words and set, for every `h=3,4,5,6`,

\[
 \{ceg^{h-2},\ deg^{h-2},\ ecg^{h-2},\ edg^{h-2}\}.
\]

Their `p(h)=(3,h-1,1,0,0,0)`, giving five keys including `p0`. Each selected horizon has exact nine-state rational rank 9; all words return net `+2E1`; the prefix trie has exactly 60 distinct primitive edges, and there are precisely four transition signatures. The four other Pareto witnesses are inherited from the parent EC49ER and EC49EM, and are checked by the independent JavaScript program in this delivery.

## 5. Validation and scope

All source and JSON evidence is preserved in this directory, with a direct reproduction procedure (`REPRODUCE_EC49ES.md`). On the declared frozen problem:

* `RUN_SCREENED_EC49ES.py`: exact enumeration of all **647 + 5349** cases, certified initial screening, integer OR-mask DP of all remaining **380 + 176** cases; outputs `EC49ES_EXECUTED.json`, status `PASS`.
* `CROSSCHECK_EC49ES.py`: **18** deterministic configurations (including over-bound cases) compare the bounded recurrence with the original unbounded EC49ER dynamic program exactly; `PASS`.
* `VERIFY_EC49ES_MILP.py`: an independently formulated SciPy/HiGHS 0–1 integer model confirms both best fixed-p cases (72 and 60), `gap=0`, dual objectives equal the two integer primal optima; this solver is crosscheck rather than the full-case proof.
* `VERIFY_EC49ES_INDEPENDENT.js`: independent Node.js signed-X6 simulation checks **all six** Pareto witnesses, full primitive-prefix counts, identical complete BRC p within horizons, and rank 9 at every horizon; it also independently enumerates 8, 51, 304, 1770, 10224 legal return words and 1, 4, 9, 17, 28 rank-nine p fibers for h=2..6; `PASS`.

For the 9-state terminal map, the stored checker reduces rank modulo prime 1,000,003. A modular 9×9 nonzero minor guarantees rational rank 9; the full rank equivalence used in exhaustive fiber classification follows the published integer Hadamard bound `|det|≤3^9<1,000,003` for the relevant 0–1 columns. The independent Node implementation provides a separately written numerical-symbolic check. Full P000 is assumed as project framing, not proved or replaced; this theorem is about a precisely specified typed finite submodel. BRC factors are positive symbolic monomials, not signed phase amplitudes. No claim is made here about general native time dynamics, complete full-world rotations, or physical calibration.

## 6. Authority and successor

At this run, authenticated GitHub account was `awdawmip` and remote repository reports `push/admin=true`. Native service `em_status` version `0.6.11` returned `research_authority_granted=false`; a bounded current-owner query returned `CONTROL_QUOTA`. Accordingly, there is **no independently confirmed active research owner and no authenticated native CLAIM, Result, Driver review or mathematical admission** for EC49ES. Project GitHub publication is a durable **author-side portable frontier** and does not invent state-machine authority. Frozen science pins, P000, ACTIVE worldview, taskbook, and other owners' claims have not been modified.

**Next EC49ET:** determine the complete H=7 three-resource Pareto set, first exploiting the new `E_{2:H}≥E_{2:H-1}+k` signature-terminal bound for certified pruning; test the exact scope where 4 signatures suffice and whether the resource tradeoff linearizes for large H. Preserve actual native-path preparation cost and BRC caching semantics. See `NEXT_EC49ET.md`.
