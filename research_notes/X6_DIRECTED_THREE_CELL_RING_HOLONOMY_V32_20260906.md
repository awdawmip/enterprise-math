# X6 upper V32: a directed three-Cell ring plus canonical pure-triadic coupling generates exact period-three flat/odd holonomy sectors

Status: `FREE_RESEARCH / EXACT CONSTRUCTIVE MULTI-CELL DYNAMICS / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_RECIPROCAL_SYNCHRONOUS_NETWORK_PERIOD2_NOGO_V31_20260906.md`;
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`.
Checker: `experiments/x6_network_event_ledger_v29_20260906/check_reciprocal_directed_network.py`.

## 1. Purpose

V31 proves that reciprocal symmetric synchronous pair coupling cannot sustain a deterministic recurrent period above two.

The smallest network escape is a directed relation cycle.

V32 shows that three Cells already suffice, using the **existing canonical V20 pure-triadic pair coupling without any extra source-space skew coefficient**.

## 2. Canonical one-hot pure-triadic interaction

For each active triad S let `e_S` denote its one-hot triad population.

Use

`K(S,T)=C3(e_S,e_T)`.

From the V18/V20 matching frame one obtains the exact values

- `K(S,S)=6`;
- `K(S,S^c)=-6`;
- for all other distinct triads, `K(S,T) in {+2,-2}`.

In particular, for a fixed target Y, `K(T,Y)` has the unique maximum 6 exactly at `T=Y`.

## 3. Directed three-Cell ring

Take three Cells indexed modulo 3 with directed context relation

`0 <- 1 <- 2 <- 0`.

At one synchronous event layer, Cell i observes only the current active triad of Cell `i+1` and chooses, among triads adjacent to its own current triad, the unique candidate maximizing

`K(T,S_{i+1})`.

Suppose the three current triads

`A,B,C`

form a triangle in `J(6,3)`, so every pair is adjacent.

Then for Cell 0, candidate `B` is admissible and has score

`K(B,B)=6`,

strictly larger than every other candidate score. Hence Cell 0 uniquely moves to B.

Similarly Cell 1 moves to C and Cell 2 moves to A.

Therefore the network update is exactly

`(A,B,C) -> (B,C,A)`.

Iterating gives the exact period-three orbit

`(A,B,C) -> (B,C,A) -> (C,A,B) -> (A,B,C)`.

No external tie-break is used.

## 4. Each Cell traverses the same active-triad triangle

Along this period-three network orbit:

- Cell 0 follows `A -> B -> C -> A`;
- Cell 1 follows `B -> C -> A -> B`;
- Cell 2 follows `C -> A -> B -> C`.

Thus every Cell accumulates the same V17 triangle holonomy up to cyclic choice of basepoint.

The network state closes after three synchronous relation layers while each Cell carries a nontrivial route history whenever the chosen triangle is curved.

## 5. Curved example: autonomous odd holonomy

Choose

`A=012`,

`B=013`,

`C=023`.

All three pairs share two axes, so they form a `J(6,3)` triangle.

V17 shared-axis replacement transport around

`012 -> 013 -> 023 -> 012`

returns the base-frame slots as

`(0,2,1)`.

Hence the loop is a transposition of the last two base slots:

`ORI6_CHARGE=1`.

The directed three-Cell network therefore generates an odd-holonomy periodic process using only:

- current active triads;
- the canonical symmetric V20 pure-triadic coupling;
- a directed inter-Cell relation topology.

The nonreciprocity has moved from an internal source-space Omega to the **network incidence relation itself**.

## 6. Flat example

Choose instead

`A=012`,

`B=013`,

`C=014`.

The three states share the common pair `01`.

The same directed ring law gives a period-three network orbit, but the V17 transport around the active-triad triangle is identity.

Thus the same network mechanism supports both flat and odd relation sectors depending on the triad configuration.

## 7. Complete triangle census

The Johnson graph `J(6,3)` has exactly 120 unordered triangles.

Exact enumeration gives:

- 60 flat triangles with identity S3 holonomy;
- 60 curved triangles with odd transposition holonomy.

Every one of these 120 triangles supplies a deterministic period-three orbit of the directed three-Cell ring by the argument above.

Therefore the canonical V20 coupling plus one directed network 3-cycle does not merely admit an isolated odd example: half of the possible active-triad triangle sectors are odd under V17 transport.

## 8. Minimality inside this ring-copy construction

A directed ring with two Cells can only exchange their two active states, producing a period at most two and a backtracking frame path.

Three is therefore the minimum number of Cells for this particular directed-copy construction to support a period-three active-triad history and hence a triangular V17 holonomy.

The equality with the P000 primitive stable-force arity 3 is structurally suggestive but is **not** used as a proof that every primitive triadic force event must instantiate a three-Cell ring.

## 9. Relation to V26-V28

There are now two exact locations where the required nonreciprocity can live:

1. **inside one Cell**: antisymmetric passage contrast `Omega=M-M^T`;
2. **between Cells**: a directed interaction graph / transfer relation.

They should not be identified. Both are typed relation asymmetries capable of escaping the reciprocal period-two no-go.

A future network law may contain both.

## 10. Time consequence

The period-three ring is an ordered dependency process:

`state_t -> state_{t+1}`

because every Cell's next relation consumes a neighbor's current relation state.

Replacing the directed ring by an unordered bag of three pair couplings destroys the update law and returns to the reciprocal V31 class.

Thus network orientation is part of relational time/context, not a seventh spatial coordinate.

## 11. Next frontier

V32 supplies the first parameter-free recurrent odd-holonomy multi-Cell construction once a directed network relation is declared.

The remaining question is to derive or update that directed relation itself from PF-10 transfer/passages rather than fixing the ring topology externally.

The natural next step is a dynamic edge ledger in which completed inter-Cell transfers create, reinforce or reverse directed context weights while preserving V29 count conservation.
