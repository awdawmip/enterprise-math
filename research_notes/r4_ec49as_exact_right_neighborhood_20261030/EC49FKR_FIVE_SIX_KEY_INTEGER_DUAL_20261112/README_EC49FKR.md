# EC49FKR — five six-key subsets have a solver-free integer lower bound of 100 native prefixes

Date: 2026-11-12. Status: author-side complete finite combinatorial certificate; independent Driver mathematical review pending. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Question and answer

EC49FKQ left nine six-full-key subsets to a HiGHS 0–1 mixed-integer solver. This note removes the dependence on that solver's internal branch-and-bound trace **for five of those nine subsets, indices 4–8**. Each of these five fixed allowed-key sets requires at least **100** distinct literal, ordered, signed X6 microstep prefixes to satisfy the 24 labelled observations. The earlier MIP witness upper bound is 112; the present lower bound need only exclude 93.

The key sets share
`K4={(2,1,1),(3,0,1),(3,1,1),(4,2,1)}`.
Their remaining two keys are: #4 `(6,4,1),(6,6,1)`; #5 `(6,4,1),(7,5,1)`; #6 `(6,4,1),(7,6,1)`; #7 `(6,4,1),(8,4,1)`; #8 `(6,4,1),(8,5,1)`.

## Integer-prefix charging theorem

Fix one allowed key set K. From **every** frozen admissible native signed path with key in K, build the literal ordered native-microstep prefix forest V; the empty prefix is a virtual root and is not charged. Let D be all 24 demand labels, and T_i the set of complete terminal prefixes realizing label i. Each label must have at least one selected terminal. A feasible prefix union is a parent-closed subset S of V intersecting every T_i.

Choose nonnegative **integer** label weights `a_i`. For each prefix vertex v put
`c(v)=sum(a_i for i with v in T_i)`.
For a nonroot-level vertex v (one having a parent within V), calculate, in bottom-up order,

`z(v)=max(0, c(v)+sum_{u child of v} z(u)-1)`.

For each top-level vertex r (whose parent is the virtual empty prefix), check
`c(r)+sum_{u child of r} z(u)<=1`.
These are exact integer conditions, with z=0 on the top-level external edge.

**Lemma.** If the top-level checks hold, every feasible S satisfies `|S|>=sum_i a_i`.

**Proof.** Extend the transfer z by 0 at top-level vertices. Every vertex then satisfies
`c(v)+sum_{u child of v}z(u)-z(v)<=1`.
Multiply by the membership indicator x_v of S and sum over V. Because S is parent-closed, `x_parent(u)>=x_u`, hence the transfer terms sum to
`sum_{u non-top}z(u)(x_parent(u)-x_u)>=0`.
Consequently `sum_v c(v)x_v<=sum_v x_v=|S|`. Moreover,
`sum_v c(v)x_v = sum_i a_i sum_{v in T_i}x_v >=sum_i a_i`,
since S meets every T_i. QED.

A *single* weight vector works simultaneously for all five fixed key sets. In ascending `(window,signature)` order, use

`a=(6,6,2,2,4,4,4,4,3,3,7,7,7,7,3,4,3,4,3,3,3,3,4,4)`.

Its sum is **100**. The bottom-up algorithm checks each top-level inequality exactly; this is a proof-producing finite verification whose witness is just the stated 24 integers and the frozen full catalogue. No LP/MIP solver, floating point, geometry projection, or merging of signed/order information is used.

## Exact execution / scope

Source generator: `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py` and adjacent `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, as pinned by prior EC49FJD/EC49FKQ. The relevant generator operations `all_words,pref,raw_key` match the GitHub source for the frozen model. Execute from this directory:
`python VERIFY_EC49FKR.py`.

All 178,850 admissible words, all 94 complete raw keys and all 24 label types are checked before certifying the five selected subsets. For these sets, the tests give:

| FKQ index | admissible words | prefix vertices | positive transfers | minimum top-level margin | lower bound |
|---|---:|---:|---:|---:|---:|
| 4 | 6,828 | 42,024 | 15,972 | 0 | 100 |
| 5 | 8,170 | 46,278 | 18,769 | 0 | 100 |
| 6 | 6,142 | 39,100 | 14,558 | 0 | 100 |
| 7 | 6,828 | 42,024 | 15,972 | 0 | 100 |
| 8 | 6,142 | 39,100 | 14,558 | 0 | 100 |

`EC49FKR_ALL_FIVE_100_PREFIX_LOWER_BOUND_PASS`.

Thus, for these five key sets, 93-prefix completion is excluded with exact integer arithmetic independent of the earlier integer optimizer. Their exact optima 112 remain supported by EC49FKQ's HiGHS certificate and checked upper-bound witnesses, not established anew by this 100 lower bound.

## Remaining frontier

The four residual subsets #0–3 have known MIP optimum 98 with independently checked witnesses. Their bare continuous relaxations give approximately 92.0833 (#0,#3) and 89.6667 (#1,#2), so this simple linear charging certificate cannot on its own exclude 93 for them. Next useful unit: derive a valid integer disjunction or a proof-emitting exact branch certificate for #0–3; use existing native prefix tree, not a new representation. Separately pursue seven-key 93-prefix constructions.

Formal Task / CLAIM / Result / independent Driver status remains separately governed. This is source-backed independent author research, not an admission or alteration of P000.
