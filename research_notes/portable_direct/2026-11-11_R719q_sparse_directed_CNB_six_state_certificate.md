# R719q — A 9-arc root repair certificate and an 18-arc sparse six-state CNB carrier

Date: 2026-11-11 (Asia/Shanghai). Research line: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Author-side mathematical construction and exact exhaustive certificate extending R719p. This is a declared active-triad admission graph, not an assertion of physical Link/Port deployment.

## Directed restriction model

Let S=012 be the rooted triad and the accessible axis palette be 01234, so there are ten 3-axis triads. Take a specified set of permitted **directed** transitions `E`, each changing exactly one active native axis (one arc of J(5,3)). A positive BRC path is an ordered rooted closed directed walk in E, with cyclic non-backtracking condition `T_(i-1) != T_(i+1)` including the seam. Transport the three ordered axis slots by the separately pinned V17 replacement law; record final `h in S3`. Each distinct valid directed path is a positive count branch.

## Theorem R719q-A: finite certificate for all lengths

Fix two distinct spare axes x=3 and y=4 and the initial triad S={0,1,2}. Assume E contains, for **each** `a in S`, all three oriented arcs of the rooted repair triangle

`S -> S-a+x -> S-a+y -> S`.

These are exactly **9 specified directed arcs** (three triangles of three arcs). Further assume that for each `m in {4,5,6}` the directed CNB rooted paths under E realize **every** of the six V17 holonomy permutations.

Then for **every integer m>=4**, the directed CNB rooted paths under E realize all six permutations.

**Proof.** Take an arbitrary legal rooted closed word W ending at S, with first neighbor F and last neighbor P. Each is a distinct active triad sharing two axes with S, so each omits exactly one a in S, respectively f and p. Choose a in S different from f and p (at most two exclusions). Append its permitted oriented triangle. The first new neighbor (S-a+x) differs from P since their omitted root axes differ. The last added neighbor (S-a+y) differs from F for the same reason; the internal turn is non-backtracking because x!=y. Hence the entire longer directed walk is cyclically non-backtracking. The three transitions replace the **same** slot by x, then y, then the original root axis a. The triangle has identity holonomy relative to the arriving ordered frame; it preserves h(W) exactly. Selecting a deterministically gives an injection `N_(m+3)(h)>=N_m(h)`. Since base m=4,5,6 each has all six states, every integer m>=4 belongs to one of the three +3 progressions. QED.

This is a finite *sufficient* certificate for any future typed/native permission graph if it genuinely admits this transition model. It is independent of event counts, raw port/Cell inventory, native event scheduler, and dependency constraints until those are explicitly mapped.

## Theorem R719q-B: sparse constructive certificate

The following 18 directed arcs (from the complete J(5,3) directed graph's 60 arcs) satisfy all nine rooted repair arcs and pass all six-state base checks:

```text
012>013 012>023 012>123 012>124
013>014 013>123
014>012 014>024
023>024 023>123
024>012 024>014
123>124 123>234
124>012 124>014 124>024
234>024
```

Exact holonomy histograms in the order (identity 012, transpositions 021/102/210, cycles 120/201) are:

| m | 012 | 021 | 102 | 120 | 201 | 210 |
|--:|--:|--:|--:|--:|--:|--:|
| 4 | 1 | 2 | 2 | 1 | 1 | 2 |
| 5 | 2 | 1 | 1 | 2 | 2 | 1 |
| 6 | 11 | 2 | 5 | 2 | 2 | 5 |

Thus this explicitly specified permission graph requires only **18/60=30% of the complete directed triad arcs** while retaining all six S3 relation results at every m>=4. This is an upper bound on the needed arc count for this sufficient family; **minimality among all such graphs is not claimed**. Notice that only a partial, directed incidence graph is used: the original full J(6,3) and its native six-axis P000 ontology remain intact.

### Concrete validation

The accompanying Node.js verifier `R719Q_DIRECTED_PORT_CERTIFICATE_VERIFY.js` uses BigInt dynamic programming on (last-but-one triad, last triad, V17 ordered frame, first root neighbor), counting all positive BRC paths including intermediate returns to S. An independent exhaustive literal DFS matches each full six-bin histogram at m=3,4,5,6,7. DP checks all six bins strictly positive at m=4..17 and checks the exact arc and repair-triangle declarations. Output `R719Q_DIRECTED_PORT_CERTIFICATE_RESULTS.json`, marker `R719Q_18_DIRECTED_ARCS_SIX_STATE_PASS`.

## Scoped conclusion and next interface

This theorem supplies a **finite test** for an actual port-permission graph, provided the graph's directed arcs are certified to correspond to legal, causally composable V17 triad updates. V29's `TRANSFER(x:a -> y:b)` itself only updates typed counts on declared allowed connections; the current V29 research file does not specify a universal directed triad-admission graph or guarantee identity-triangle schedule independence.

Next: read one exact deployed Port/Link and scheduling instance, express it as a relation on (triad, slot-frame, inventory, last-event dependency), and check the nine repair arcs and 18 source witness arcs. Where an arc fails, return its exact type, port, inventory or dependency obstruction. The theorem also gives a sound fast sufficient screen before full lifted-state reachability.

BRC: each path is a positive branch, with provenance and internal frame retained. The final S3 observation is an observer-specific reduction with a three-bit fixed-width sufficient repair only under the declared available future operations.
