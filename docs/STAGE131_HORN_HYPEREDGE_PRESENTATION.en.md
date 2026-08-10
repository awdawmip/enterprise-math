# Stage131 — Horn Hyperedge Shortcuts beyond Unary TC-Spanners

Status: `RESEARCH BRIDGE / NONCANONICAL`

Unary chains admit an ordinary shortcut-graph interpretation. Multi-premise closure rules do not. Once a conclusion requires several premises simultaneously, Stage131 presentation geometry becomes hypergraph / AND-OR derivation geometry rather than ordinary shortest paths.

## 1. Horn rule as derivation hyperedge

A finite Horn rule has the form

`P => c`,

where P is a nonempty set of premises and c is one conclusion.

A rule fires only when **all** premises in P are already available.

If d(x) is the earliest synchronous round at which atom x is known, then

`d(c)=min_(P=>c) [1+max_(p in P)d(p)]`.

The `max` is the conjunctive synchronization cost; the `min` chooses among alternative rules for the same conclusion.

## 2. Why ordinary graph shortcuts are unsound

The smallest witness is

`{a,b}=>c`.

Replacing it by unary edges

`a->c`, `b->c`

changes AND into OR and incorrectly derives c from `{a}` alone.

Therefore a multi-premise Stage131 shortcut must preserve the whole premise set as one hyperedge/macro rule. Ordinary TC-spanner distance is no longer the correct semantic execution object without state expansion.

## 3. Semantically derived Horn macro

A candidate macro

`P=>c`

is safe when c already belongs to the base closure of P.

Adding such a macro cannot change the closure operator on any seed set. If some seed S reaches every premise in P, monotonicity and idempotence of closure already imply it reaches c in the base system.

So a derived macro may reduce derivation rounds while preserving every exact closure answer.

The owner checks this exhaustively over all seed subsets on small atom systems.

## 4. Minimal multi-premise shortcut witness

Base rules:

`a=>p`,

`b=>q`,

`{p,q}=>z`.

From seeds `{a,b}`:

- p,q appear at round1;
- z appears at round2.

The derived macro

`{a,b}=>z`

is semantically redundant yet reduces z to round1.

This is the multi-premise analogue of storing a transitive chain shortcut.

## 5. Rule count is no longer enough

A unary rule has premise width1, so counting rules is a reasonable first storage measure.

A Horn macro can have hundreds or millions of premises. Presentation cost therefore needs at least:

- rule count;
- total premise-literal incidences;
- maximum premise width/fan-in;
- execution depth.

These resources can move in different directions.

## 6. Balanced binary AND tree

Take `2^h` leaf atoms. Every internal node is concluded by one local binary Horn rule from its two children.

The local semantic basis has

`2^h-1`

rules and

`2(2^h-1)`

premise literals.

Starting from all leaves, the root and complete closure both require h synchronous rounds.

## 7. Span-s macros

For `2<=s<=h`, add to every node of height at least s one derived macro from all descendants exactly s levels below that node.

Each such macro has premise width

`2^s`.

The number of added macro rules is

`M_rules(h,s)=2^(h-s+1)-1`.

The number of added premise literals is

`M_lits(h,s)=2^(h+1)-2^s`.

For s=1 no new macro is stored because the corresponding rule is exactly the original local binary rule.

## 8. Exact root-depth law

A node can move upward either one local level or s levels by a macro.

For the root at height h, the shortest derivation therefore uses as many s-level jumps as possible:

`D_root(h,s)=floor(h/s)+(h mod s)`.

This is the same coin-count recurrence as the unary `{1,s}` jump family, but the storage cost of an s-jump is now an exponential premise set rather than one edge.

## 9. Exact full-closure depth law

Reusable full closure must derive every internal node, not only the root.

The worst node height through h gives

`D_full(h,s)=floor(h/s)+max(s-2,h mod s)`.

So a presentation optimized for one root readout need not be optimized for the complete reusable state.

## 10. Giant root macro: sharp readout/state split

Take s=h.

Only one macro is added: all `2^h` leaves directly imply the root.

Resources:

- extra rule count1;
- macro premise width `2^h`;
- root depth1;
- complete closure depth `h-1`.

Thus one enormous rule can make the declared root answer immediate while leaving most reusable internal-state derivation essentially sequential.

This is a sharp multi-premise instance of

`readout shortcut != executable-state shortcut`.

## 11. Height-8 resource surface

The exact points include:

| span | total rules | total premise literals | max width | root rounds | full rounds |
|---|---:|---:|---:|---:|---:|
| 1 | 255 | 510 | 2 | 8 | 8 |
| 2 | 382 | 1018 | 4 | 4 | 4 |
| 3 | 318 | 1014 | 8 | 4 | 4 |
| 4 | 286 | 1006 | 16 | 2 | 3 |
| 8 | 256 | 766 | 256 | 1 | 7 |

The span8 presentation uses fewer total rules and premise incidences than span4, yet has sixteen times larger maximum fan-in and much worse full-state continuation depth.

No one scalar storage number captures the trade.

## 12. Root frontiers are genuine minimal premises

For the root, take all descendants exactly s levels below it. There are `2^s` of them.

That frontier derives the root, and removing any one frontier atom breaks one necessary subtree and prevents root derivation.

Hence every such level frontier is an inclusion-minimal premise set for the same root.

Their widths range

`2,4,8,...,2^h`.

So even one conclusion naturally has many rooted-circuit premises with radically different widths and execution meanings.

## 13. Rooted circuits and presentation resources

Rooted circuits record minimal premise sets for one-round conclusion access.

The AND tree shows why that object can be much larger than a local Horn basis:

- local rules describe how the law composes;
- rooted circuits enumerate alternative minimal premise frontiers from which one conclusion can be obtained in one step;
- macro presentations selectively cache some of those derived frontiers to buy execution depth.

The three objects should not be conflated.

## 14. From graph spanners to hypergraph shortcuts

Unary chain TC-spanners optimize sparse edges under path-length diameter.

Horn shortcuts must instead optimize hyperedges under min-max derivation depth, with premise width/fan-in as an additional cost.

The natural next objects are therefore Horn proof DAGs, AND/OR circuits, hypergraph shortcuts and multi-premise macro systems rather than ordinary graph spanners alone.

## Owner-local assets

- `stage131_horn_hyperedge_presentation.py` / tests;
- `stage131_horn_resource_surface.py` / tests;
- `STAGE131_HORN_HYPEREDGE_PRESENTATION.{en,zh}.md`.

## Prior art / status

Horn forward chaining, hypergraphs, AND/OR derivations and proof DAGs are standard prior mathematics/CS. The Enterprise Math value is the explicit Stage131 semantic-basis versus hyperedge-presentation resource routing.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.