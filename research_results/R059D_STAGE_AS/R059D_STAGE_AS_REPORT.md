# R059D Stage AS — General-Radius Segment Footprint / Triangle-Flip Report

Researcher-ID: `EM-R059D-AS-6E2A91`

Task: `RS-R059D-STAGE-AS-GENERAL-RADIUS-SEGMENT-FOOTPRINT-TRIANGLE-FLIP-ESCAPE`

Taskbook source: `75d2e38cf20bc7c6c64e0100c6d78ea151b5cbd6`

Frozen parent: `3350ee0e0fa1d35d379275bd08fb8554f15e9d33`

## Strongest disposition

`MULTIPLE_INEQUIVALENT_GENERAL_RADIUS_SEGMENT_LIFTS_SURVIVE__PRE_CIRCLE_LENGTH_AND_ESCAPE_LAW_UNDERDETERMINED__TRIANGLE_FLIP_CHAIN_DRIFT_PROVED`

This is an exact stronger countertheorem to the preferred general-radius closure target.

## Main result

Stage AR's one-step state `(e,C)` does not have a unique general-radius extension under the currently frozen pre-circle native axioms.

Two explicit general-radius carrier families both satisfy AR reduction, radius-r axis anchors, D6, reversal, translation, prefix consistency, and all circularity firewalls:

1. `TERMINAL_SIDE_CHAIN`: ordered primitive-edge chain plus only the terminal-edge side triangle;
2. `EDGEWISE_SIDE_STRIP`: the same chain plus one side triangle per primitive edge.

At `r=1` both have exactly the twelve AR lifts. At `r=2` their fibers over the six visible axis anchors already have total sizes 12 and 24. No current native observable selects one.

## Triangle flips

For an ordered primitive-edge footprint:

- `1->2` replaces one triangle edge by the other two, preserves subpath endpoints, and changes chain edge count by `+1`;
- `2->1` is the inverse and changes edge count by `-1`;
- terminal `1->1` pivot preserves edge count but moves the free endpoint and reduces exactly to AR at `r=1`.

Thus the earlier qualitative up/down intuition has a literal chain-cardinality realization. However this is carrier/length typed, not yet a universal physical/native segment-length theorem.

No canonical general-radius compensation/axis-completion pairing is forced by one-cell incidence.

## Pre-circle length

Two native D6-invariant candidates agree on all straight axis anchors and at r=1 but disagree on a legal triangular footprint:

- `L_chain(P)=number of primitive edges`;
- `L_disp(P)=native primal graph distance from O_E to the free endpoint`.

On

`(0,0)->(1,0)->(0,1)`,

`L_chain=2` while `L_disp=1`.

Consequently a carrier-specific length observable exists, but a carrier-independent general-radius segment-length semantics is not uniquely derived.

## Escape-score underdetermination

At radius 2, inner- and outer-edge `1->2` expansions of the straight axis chain both keep free endpoint `(2,0)`, so free-endpoint shell ties them.

AQ cell shell instead gives

`SHELL(U(0,0))=0`,

`SHELL(U(1,0))=2`,

so newly-entered-cell shell strictly prefers the outer flip.

Both are source-free native D6-covariant scores. Therefore there is no unique general-radius FAR_STATE law before another independent axiom is supplied.

## Diagnostic finite atlas

### Arm A — terminal-side + fixed chain cardinality

At r=1, exact AR two-cycle-family closure is recovered with minimal period 6.

For every r>=2, each straight axis lift admits exactly two terminal pivots before the third proposed pivot reaches the already occupied prefix vertex `v_(r-2)`. Hence for r=2..6:

- J=0: 12 states;
- J=1: 12 states;
- J=2: 12 states;
- J>=3: none;
- total distinct reachable: 36;
- cycles: 0.

### Arm B — edgewise strip + raw flips

Before fixing chain cardinality as the hard length, every straight radius-r seed has stored-side `1->2` expansions. These keep the free endpoint on shell r and therefore tie the first tangential terminal pivot under free-endpoint shell. All such branches survive; each expansion has chain cardinality r+1.

Thus this equally pre-circle-compatible arm has immediate length-drift branches at J=1.

The two arms are diagnostic, not competing fits. Their incompatible behavior is the theorem: the current axioms do not define a unique general-radius state graph.

## AL support arm

With A8 disabled and `SUP` typed only as support/incidence rank, the outer-axis length-drift expansion through `(r-1,1)` remains inside `K_E(r)` because

`SUP(r-1,1)=9r^2-18r+21 <= 9r^2`

for every r>=2.

Therefore support alone does not choose the carrier/length/score or remove the earliest drift branch.

## Post-freeze circle comparison

At r=1, terminal-side AS equals AR and hence the accepted AP/AK/AL visible cycle.

At r>=2:

- Arm A has no cycle;
- Arm B has extra lawful drift branches.

So neither all-path diagnostic object equals the canonical circle. The accepted circle is not used to prune or select an AS carrier.

## Checker

Deterministic checker:

`5687 / 5687 PASS`

Digest:

`073a08162c7acc6b8387bc2c5c7f6563f0b2b764ba7243078148710607b98a50`

Coverage:

- radius/anchor typing through r=256;
- carrier fiber separation through r=16;
- terminal-side diagnostic dynamics through r=64;
- score-shell witness through r=128;
- AL support drift witness through r=256;
- exact diagnostic atlas r=2..6.

## Semantic boundaries

- native zero remains absent;
- r is primitive-unit count, distinct from native coordinate magnitude r+1;
- no source circle/angle/pi occurs in primary definitions;
- AK tau and SEG_E(r) are not primary oracles;
- AL A8 is disabled;
- triangle-flip edge-count drift is not promoted to carrier-independent physical length;
- no general-radius all-path circle closure theorem is claimed;
- no later stage is consumed.

## Remaining exact frontier

The missing ingredient is not more replay. It is an independent Enterprise-native axiom/observable selecting, for r>1:

1. the segment carrier/footprint ontology;
2. the intended pre-circle length semantics;
3. the active local site(s) and admissible flip relation;
4. the segment escape score or compensation law.

Only after that selection is derived independently can a unique general-radius state graph and a meaningful all-path closure theorem be tested.
