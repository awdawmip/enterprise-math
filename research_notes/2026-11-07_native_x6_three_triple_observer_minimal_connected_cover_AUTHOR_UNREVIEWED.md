# Native X6 coordinate observers: exact minimal connected three-triple cover

Date: 2026-11-07 (Asia/Taipei)
Status: **AUTHOR_UNREVIEWED / NOT_ADMITTED / NEUTRAL_GITHUB_NOTE**
Provenance: independent *derivation* in the current automation conversation, with shared project/source context disclosed; no clean-independent Driver review, native DA/session, RESULT, review, task publication, or Working Truth is claimed. Current Source service denied backend operations with `BACKEND_IDENTITY_OR_VERSION_MISMATCH; operation_sent=false`. Frozen F7/P000 task-scientific pins and existing contributor history are unchanged.

## Statement in the existing P000 native X6 coordinate domain

Use the currently defined *raw chart* of the native spatial Cell torsor `X6_NATIVE_SPATIAL`, with `z=(z_1,...,z_6)∈Z^6` relative to a chosen native Cell anchor. This is a coordinate theorem, not a model of primitive triadic force closure `E`.

For any triple `S⊂{1,...,6}`, `|S|=3`, use the **already defined native coordinate observer**

`Obs_S(z) = can3((z_i)_(i∈S)) = (z_i - min_(j∈S) z_j)_(i∈S)`.

For a family `Q` of selected triples define `G_Q`: its vertices are the six axis labels; for each triple `S∈Q`, connect the three vertices of `S` by a 3-clique. Let `Δ=Z(1,1,1,1,1,1)`.

**Theorem.** The map `Obs_Q:z↦(Obs_S(z))_(S∈Q)` has precisely the diagonal fibers `z+Δ` **if and only if** `G_Q` is connected. If connected, the relative native coordinate `can6(z)=(z_i-min_j z_j)_i` can be reconstructed by integer differences along a spanning tree, and one additional integer **common-depth** value `h=min_i z_i` reconstructs the full spatial coordinate `z=can6(z)+h(1,...,1)`. For disconnected `G_Q` distinct relative native spatial coordinates have the same `Obs_Q`.

**Minimality and classification.** Among the 20 possible three-axis coordinate selections, a family of **three** is necessary and sufficient to recover `can6(z)` for every `z∈Z^6`. Of the `binom(20,3)=1140` unordered three-selector families, exactly **480** suffice, split into exactly **three** `S6` relabeling orbits:

| Representative triple selectors | Orbit size | Stabilizer in S6 | Pairwise intersection pattern |
| --- | ---: | ---: | --- |
| `{123,124,156}` | 180 | 4 | `(2,1,1)`, with one triple-shared vertex |
| `{123,124,356}` | 180 | 4 | `(2,1,0)`, connected path |
| `{123,145,246}` | 120 | 6 | `(1,1,1)`, with three distinct pairwise intersections |

Exactly 600 other three-selector families have two connected components; 60 have three. A singleton triple observes at most 3 axes. Two triples can cover six axes only if disjoint, but then leave a relative offset between the two components unobserved. Hence three is minimal.

## Proof

Each `Obs_S(z)` reveals all differences `z_j-z_i` for `i,j∈S`, since subtracting the common triple minimum cancels. If `G_Q` is connected, choose root axis 1 with provisional `x_1=0`. Integrate the observed integer edge differences along any spanning tree to obtain `x_i=z_i-z_1` for all six labels. Normalizing `x_i-min_j x_j` gives `can6(z)`. This proves fiber equality modulo `Δ` and exact reconstruction with `h`.

Conversely if `G_Q` has at least two components, start from `z=0` and add 1 to all coordinates in any one (proper nonempty) component. Every selected triple lies entirely within one connected component, so all triple-normalized observations remain unchanged, although the relative full `can6` changes. This is an exact information-loss witness.

For the three-triple classification, every triple is distinct and has cardinality 3. Connectivity covering all 6 labels forces the overlap incidence pattern to be one of the three displayed patterns (up to permutation); these yield orbit sizes `720/4=180`, `720/4=180`, and `720/6=120`. Direct exhaustive enumeration of all `1140` selector families and all `720` axis-label permutations reproduces their counts.

**Concrete fiber witness:** for `Q={123,456}`, `z=(0,0,0,0,0,0)` and `z'=(1,1,1,0,0,0)` have identical two triple observers but different global relative coordinates.

## Reproduction (Python standard library, exact integers)

```python
from itertools import combinations, permutations, product
from collections import Counter

V = tuple(range(1, 7))
T = tuple(combinations(V, 3))
index = {t: i for i, t in enumerate(T)}

def components(q):
    parent = list(range(7))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    def join(a, b):
        a, b = root(a), root(b)
        if a != b:
            parent[b] = a
    for t_idx in q:
        a, b, c = T[t_idx]
        join(a, b)
        join(b, c)
    return len({root(i) for i in V})

families = tuple(combinations(range(20), 3))
hist = Counter(components(q) for q in families)
good = {q for q in families if components(q) == 1}
assert len(families) == 1140
assert hist == {1: 480, 2: 600, 3: 60}
assert len(good) == 480

actions = []
for perm in permutations(V):
    renaming = dict(zip(V, perm))
    actions.append(tuple(index[tuple(sorted(renaming[i] for i in t))] for t in T))
remaining, orbit_sizes, representatives = set(good), Counter(), []
while remaining:
    rep = min(remaining)
    orbit = {tuple(sorted(action[i] for i in rep)) for action in actions}
    assert orbit <= remaining
    representatives.append(tuple(''.join(map(str, T[i])) for i in rep))
    orbit_sizes[len(orbit)] += 1
    remaining -= orbit
assert orbit_sizes == {180: 2, 120: 1}
assert representatives == [('123', '124', '156'),
                           ('123', '124', '356'),
                           ('123', '145', '246')]

def reconstruct_relative(z, q):
    edges = {i: [] for i in V}
    for ti in q:
        t = T[ti]
        u = {i: z[i-1] - min(z[j-1] for j in t) for i in t}
        for i, j in combinations(t, 2):
            edges[i].append((j, u[j]-u[i]))
            edges[j].append((i, u[i]-u[j]))
    x, frontier = {1: 0}, [1]
    for i in frontier:
        for j, diff in edges[i]:
            val = x[i] + diff
            if j in x:
                assert x[j] == val
            else:
                x[j] = val
                frontier.append(j)
    assert len(x) == 6
    a = [x[i] for i in V]
    return tuple(v-min(a) for v in a)

for q in (min(orbit) for orbit in (
    {tuple(sorted(action[i] for i in rep)) for action in actions}
    for rep in [(0, 1, 9), (0, 1, 18), (0, 7, 14)]
)):
    for z in product(range(-2, 3), repeat=6):
        assert reconstruct_relative(z, q) == tuple(v-min(z) for v in z)
print('PASS', hist, orbit_sizes, '15625 states per orbit representative')
```

The 1140/720 finite combinatorial census is exhaustive for that finite selector domain. The 15625-state checks per orbit representative are regression tests of the general spanning-tree proof (not substitutes for its universal quantifier).

## Scientific use and next exact question

The old auxiliary six-label *pair-incidence* certificate (`2026-11-07_six_triad_pair_observer_unimodular_repair_orbits_AUTHOR_UNREVIEWED.md`) requires five extra triple-coordinate queries to recover **arbitrary triple-weight vectors** from pair totals. This theorem instead studies the **already admitted X6 coordinate triple observers** and needs only three selected observer calls to recover six-axis relative spatial coordinates; the two observer maps have different inputs and readouts.

Spatial observer preservation is exact after adding global integer common depth, for any downstream spatial operation evaluated by decode/apply/reencode. Actual Enterprise primitive closure `E`, decorated force/path/BRC provenance, and future-readout safety have separately typed populations. The smallest follow-up science unit is: identify the actual `E`-admissible subset of the 20 coordinate selections and test whether any of the 480 connected three-selector covers remains admissible under the specified future-operation horizon. Keep this within an existing P000 native-coordinate/triadic-observer bridge task after current canonical state can be read; publish no duplicate task.

Current source anchors (normative/main read versus scientific pin separated):
- `awdawmip/enterprise-math@67eed0b09e7b3f777c09736d4ac1fedb93c69365:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` §§5–7, 9.
- `awdawmip/enterprise-math@67eed0b09e7b3f777c09736d4ac1fedb93c69365:p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, and `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
- Frozen F7 result `RR-AA38973D56330E59D315` with source pin `80df6ad5686052c784a8d3e69a4c6b9451a1db7a`; original F7 review must remain independent and unaltered.

Native Source review, reference passes, synthesis, follow-up and admission remain pending restoration of this conversation's real Driver authorization and Source service connectivity. This neutral GitHub note is source preservation, not `RESEARCH_DRIVER` control-plane publication.


## Addendum: three of the four established FCC/K4 STAR coordinate selectors

Date: 2026-11-07 (Asia/Taipei). Provenance: a subsequent independent *derivation* in the scheduled RESEARCH_DRIVER conversation, with its shared prior project/source and the prior author note expressly acknowledged. Status remains **AUTHOR_UNREVIEWED / NOT_ADMITTED**; this addendum creates no Source Review/DA, E-admission, closure, or new Task. The original certificate/provenance above is preserved unchanged.

**Exact restricted corollary.** Label the six X6 coordinate axes by the edges of a classical combinatorial K4: `12,13,14,23,24,34`. Its four STAR selector triples are
`S1={12,13,14}`, `S2={12,23,24}`, `S3={13,23,34}`, `S4={14,24,34}`.
For **any three distinct** selectors among `S1,S2,S3,S4`, their native *coordinate* readouts `Obs_S=can3(z|S)` determine `can6(z)` on all raw spatial charts `z ∈ Z^6`. Three are **minimal within this four-STAR family**, as any two STAR selectors jointly mention exactly five of the six axes. One common-depth integer `h=min(z)` recovers the full chart coordinate `z`. Consequently the omitted fourth STAR coordinate readout is mathematically recoverable from the selected three for this *coordinate-endpoint observation alone*.

**Proof (general, not merely finite verification).** Any two distinct K4 vertex stars meet in exactly their common edge. Hence the 3-cliques of any three STAR triples form a connected graph on **all six** edge labels. By the preceding spanning-tree theorem their `can3` observations recover all coordinate differences, and thus `can6(z)`. Two STAR triples cover `3+3-1=5` distinct axes, so the missing sixth axis can be varied without affecting them. This establishes exact necessity and sufficiency, including negative signed coordinates.

For example using `S1,S2,S3`, set a provisional `z_12=0`. `Obs_S1` gives `z_13-z_12` and `z_14-z_12`; `Obs_S2` gives `z_23-z_12` and `z_24-z_12`; `Obs_S3` supplies `z_34-z_13`. Hence all six provisional coordinates are determined, with `z_34=(z_13-z_12)+(z_34-z_13)`. Subtract their global minimum to get `can6(z)`. The other three choices follow by K4 vertex relabeling. The four families with three STAR selectors and six families with two are the full finite census inside this fixed atlas.

**Boundary and precise next test.** This is a **restricted observation/information theorem**, not a declaration that three physical carrier measurements, triadic force-closure E events, packet paths, their temporal histories or decorated joint/BRC states are interchangeable. The current X6 Foundation realizes the four STAR selectors as FCC carrier-readout triples but does not identify STAR-coordinate connectivity with admissibility of primitive `TRIADIC_CLOSURE_E` for arbitrary input. Read the actual E-admissibility and future-operation/preservation contract before attempting that bridge. The immediate non-duplicative test in the existing P000 E/observer bridge task is whether three **simultaneously E-admissible** STAR-coordinate observations can be assembled with the declared provenance/horizon; if not, exhibit the precise forbidden triple, state restriction, or operation that prevents the coordinate corollary's application. Do not open a duplicate task or promote this appendix to a formal review.

Sources of previously frozen definitions (not new task science pins): `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` §§5,6,9; `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.json` `relative_observer` / `fcc_star_carrier`; `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md` primitive `E` gate; `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` future-operation boundary.

## Addendum: exact error-correction threshold for native X6 coordinate triple observers

Date: 2026-11-07 (Asia/Taipei). Author-side continuation with shared previous project/source exposure; status **AUTHOR_UNREVIEWED / NOT_ADMITTED**. This addendum is a coordinate-only mathematical certificate. Existing frozen F7 scientific pins, contributions and formal reviews are unchanged.

Let X=Z^6/Z(1,1,1,1,1,1), and let Q be any family of distinct three-axis selectors S⊂{1,...,6}. Define the relative-coordinate code C_Q([z])=(can3(z|S))_(S in Q), where a whole triple observation counts as one code symbol. For nonempty proper A⊂{1,...,6}, write ∂Q(A) for those chosen triples intersecting both A and its complement.

**Exact distance theorem:** min Hamming distance between different elements of X under C_Q is

    d_min(Q) = min_{nonempty proper A} |∂Q(A)|.

This includes d_min=0 for noninjective codes. One can uniquely recover up to e erased triple symbols precisely when d_min≥e+1, or correct up to t arbitrary unknown corrupted triple symbols precisely when d_min≥2t+1, with the usual worst-case, unrestricted output-symbol error model.

**Proof.** Two can3 readouts on S agree exactly when the difference vector d=z'-z is constant on S. For any nonconstant d, select a proper nonempty value class A; each triple crossing that cut has nonconstant d, so the Hamming distance is at least the minimum cut. Conversely the difference d=1_A, from 0 to the cut indicator, produces disagreements on exactly the crossing triples. The standard Hamming-ball disjointness argument establishes the correction/erasure thresholds.

**Four existing FCC/K4 STAR readouts:** min distance is exactly 2. Any three STARs connect all six edge axes, so at most two STAR readouts can agree for distinct relative states. Taking d=e_12 modifies exactly the two STARs incident at edge 12; the other two are unchanged. Thus four STARs detect one corrupt whole readout and recover one known-position erasure, but cannot uniquely correct one unknown corruption. For an explicit ambiguous received word, use the S1 output from z'=e_12, the S2 output from z=0, and the common S3,S4 outputs; it is one symbol away from each possible codeword.

**Minimum six triple queries for single-error correction:** To have d_min≥3, each singleton cut must be crossed at least three times, i.e. every one of the six axis labels appears in at least three chosen triples. Thus 3|Q|≥18 and |Q|≥6. Six suffice: Q*={123,124,125,346,356,456} has every one of its 31 unordered nontrivial vertex cuts crossed by at least three triples. Hence six is the exact minimum number of selected native coordinate triple observations permitting correction of one arbitrary unknown corrupted triple readout.

Across all 38,760 distinct six-selector families, exactly 330 attain d_min=3. Under all six-axis relabelings, they split into exactly four orbits with sizes 60, 60, 180, 30.

**Finite integer certificate (Python 3 standard library):** The symbolic theorem and the lower bound hold without finite-range assumptions; this checker exhausts all selector families of cardinality up to six and all 31 unordered cuts, then all 720 axis relabelings for the orbit census.

~~~python
from itertools import combinations, permutations
from collections import Counter
tri = list(combinations(range(6), 3))
mask = [sum(1 << i for i in s) for s in tri]
idx = {s: i for i, s in enumerate(tri)}
cuts = range(1, 32)  # exactly one of each cut/complement pair
def dist(q):
    return min(sum(0 < (mask[i] & a) < mask[i] for i in q) for a in cuts)
hist = {m: Counter(dist(q) for q in combinations(range(20), m)) for m in range(1, 7)}
assert hist == {
  1: {0: 20}, 2: {0: 190}, 3: {0: 660, 1: 480},
  4: {0: 1245, 1: 3525, 2: 75},
  5: {0: 1512, 1: 10200, 2: 3792},
  6: {0: 1260, 1: 14580, 2: 22590, 3: 330},
}
good = {q for q in combinations(range(20), 6) if dist(q) == 3}
actions = []
for p in permutations(range(6)):
    actions.append(tuple(idx[tuple(sorted(p[v] for v in t))] for t in tri))
orbits = Counter()
while good:
    q = min(good)
    orbit = {tuple(sorted(a[i] for i in q)) for a in actions}
    assert orbit <= good
    orbits[len(orbit)] += 1
    good -= orbit
assert orbits == {60: 2, 180: 1, 30: 1}
qstar = tuple(idx[tuple(i - 1 for i in t)] for t in
              ((1,2,3),(1,2,4),(1,2,5),(3,4,6),(3,5,6),(4,5,6)))
assert dist(qstar) == 3
print("PASS", hist, orbits)
~~~

**Native-scope bridge:** the 20 can3 selectors are already-defined native X6 coordinate readouts; only the four STARs currently have complete FCC carrier-readout realization. The six-query optimum is an information theorem, not automatic physical simultaneous E-admissibility or path/BRC future-horizon preservation. In the existing P000 E/observer bridge task, determine the simultaneously E-admissible selectors under the precise state/horizon, then evaluate their cut threshold. A cut failing the target threshold provides an explicit coordinate-separation witness d=1_A. Do not create a duplicate Task or substitute this author note for an authorized Driver Review.

## Addendum: exact optimal multi-error correction budgets for X6 coordinate triple observers

Date: 2026-11-07 (Asia/Taipei). This is an **author-side, shared-context** mathematical continuation of the existing coordinate-observer note, not a new independent Driver review, current E-admission certificate, or canonical Result. Status: **AUTHOR_UNREVIEWED / NOT_ADMITTED**. Earlier frozen F7 scientific inputs, accepted P0 review, historical contributions and Source result/review bytes are unchanged.

**Theorem (optimal redundancy, arbitrary whole-symbol corruption).** Let \(T=\binom{[6]}3\) be the 20 possible distinct three-axis selectors and \(Q\subseteq T\). Encode the relative native raw-coordinate chart \(X=\mathbb Z^6/\mathbb Z(1,1,1,1,1,1)\) by \(C_Q([z])=(\operatorname{can3}(z|_S))_{S\in Q}\), with one entire triple readout counted as one code symbol. For each \(t=1,2,3,4\), the fewest **distinct** triple observers needed to correct every pattern of at most \(t\) arbitrary errors in unknown symbol positions is precisely \(k_{\min}(t)=4t+2\). For \(t\ge5\), no selection of the available 20 triple observers permits worst-case correction. At the optimum \(k=2d,\ d=2t+1\), a family is adequate **if and only if** every one of the six axes occurs in exactly \(d\) selected triples.

**Proof.** The earlier theorem gives the exact whole-symbol minimum Hamming distance \(D(Q)=\min_{\varnothing\neq A\subsetneq[6]}|\partial_Q(A)|\). A singleton cut has size \(\deg_Q(i)\). Since \(\sum_i\deg_Q(i)=3k\), \(D(Q)\le\lfloor k/2\rfloor\); unique worst-case \(t\)-error correction requires \(D(Q)\ge2t+1\), forcing \(k\ge4t+2\). Conversely suppose \(k=2d\) and \(\deg_Q(i)=d\) for every axis, where \(d\ge3\). A 1/5 cut has \(d\) crossing triples. A 2/4 cut with pair \(i,j\) has \(2d-\lambda_{ij}\ge d\) crossing triples, since pair-codegree \(\lambda_{ij}\le d\). A 3/3 cut has at most two wholly internal triples (one on each side), hence at least \(2d-2\ge d\) crossing triples. Complementary cuts give the other sizes. Thus \(D(Q)=d\), sufficient to correct \(t=(d-1)/2\) arbitrary corrupt whole-triple symbols. Necessity of regularity at the optimal cardinality follows because \(D(Q)\ge d\) makes all singleton degrees at least \(d\), but their sum is exactly \(6d\). The full 20-triple family has every axis in 10 triples; consequently no code can have distance 11, excluding \(t\ge5\).

**Explicit existence.** For \(t=1\), \(Q_6=\{123,124,125,346,356,456\}\) is 3-regular. For \(t=2\), \(Q_{10}=\{123,124,125,126,134,256,345,346,356,456\}\) is 5-regular. For \(t=3\), \(Q_{14}=T\setminus Q_6\) is 7-regular. For \(t=4\), \(Q_{18}=T\setminus\{123,456\}\) is 9-regular. All are within the declared unconstrained coordinate-selector universe.

**Exact finite census.** For \(k\in\{6,10,14,18\}\), enumerating all \(\binom{20}{k}\) unordered selector subfamilies, retaining those with six degrees \(k/2\), verifying all 31 complement-distinct nontrivial cuts, and quotienting by all 720 axis-label permutations yields:

| Arbitrary errors \(t\) | Optimal \(k\) | Number of optimal selector families | \(S_6\) orbit sizes |
|---:|---:|---:|---|
| 1 | 6 | 330 | 30, 60, 60, 180 |
| 2 | 10 | 1044 | 12, 72, 90, 90, 180, 240, 360 |
| 3 | 14 | 330 | 30, 60, 60, 180 |
| 4 | 18 | 10 | 10 |

The finite-domain census is an exact integer check of a universal combinatorial proof; no infinite-state enumeration is claimed.

**Mother-objective interface.** These are native X6 **raw-coordinate readout** information and error-correction statements, not claims of simultaneous physical E-admissibility, primitive triadic force closure, complete 3D slice identification, BRC branch/path provenance preservation, or future-operation-safe erasure. The immediate existing P000 bridge question remains whether the actual E-admissible joint selector subsets contain any of these \(d\)-regular families under a declared common-state and future-operation horizon. No separate task, new Driver authority, review, synthesis, or Foundation adoption follows from this author note.
