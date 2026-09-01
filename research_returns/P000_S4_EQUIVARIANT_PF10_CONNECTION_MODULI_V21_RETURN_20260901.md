# Research Return — P000 S4-equivariant PF10 / connection moduli V21

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-FBDBDBE1C5BDF65F97A0`  
Researcher: `EM-P000FCC21R-61A4CE`  
Claim: `chatgpt-p000fcc21r-20260901-1104-61a4ce`  
Execution: `ER-BD3606DBF5F21E7A3F2C`  
Status: `SUCCESS / NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`

## 0. Terminal result

Generation 21 closes the frozen Gen19 mathematical target

`P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_AND_COMMON_NONDEGENERATE_MODEL_EXACTLY_CLASSIFIED`

at the exact finite K4/tetra carrier strength requested by the task.

The terminal class is

`NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`.

The exact classification is:

- the base-Cell `S3` stabilizer has `2` vector orbits and `8` ordered channel-pair orbits;
- therefore an equivariant PF10 representative profile has exactly `2+2+8=12` independent raw value slots for `(I,O,M)`, before applying whatever componentwise PF10 value-domain restrictions are already frozen;
- evaluation at the base Cell and structural transport are inverse bijections between those stabilizer-fixed profiles and global `S4`-equivariant PF10 families;
- there are explicit raw Cell-to-Cell nonconstant PF10 families;
- for the frozen typed independent-connection value group `Sym({E1,...,E6}) ~= S6`, every fully `S4`-equivariant inverse-consistent connection is determined by one seed `t=T_AB`;
- exactly `12` seeds are legal: `1` raw identity and `11` raw nonidentity connections;
- exactly `2` raw connections are flat and `10` are nonflat;
- under the already accepted Gen10 local-`S6` presentation gauge, the `12` raw solutions form exactly `8` gauge classes: `1` flat and `7` nonflat;
- the Gen18 edge-to-opposite transposition connection is one of the nonflat classes and is therefore not an isolated accidental existence phenomenon;
- a single enriched K4 Full-Cell model simultaneously carries a nonconstant PF10 family and that nonidentity/nonflat connection, and satisfies the frozen `a^3=b^2=(ab)^4=1` structural relations on the complete enriched data.

No P000 root mutation, G15 grammar change, Gen17 cost change, hidden-kernel quotient, time rotation, or promotion of local `S6` gauge to native spatial rotation is used.

## 1. Frozen finite carrier model

Use the accepted tetrahedral carrier:

- Cells `A,B,C,D`;
- six channel labels identified in the canonical presentation with tetrahedral edges

`E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`;

- carrier group `S4` acting on Cells and hence on the six edges;
- frozen generators

`a=(BCD)`, `b=(AB)`,

with

`a^3=b^2=(ab)^4=1`.

The independent connection takes values in the finite typed presentation group

`C = Sym({E1,...,E6}) ~= S6`.

This `S6` is exactly the local channel-reindexing/presentation universe accepted at Gen10. It is not a native six-dimensional rotation group.

For the common positive witness below, the visible faithful structural model takes `G0=S4`, so the full lift fibers of `a,b` are singletons because the model itself has no hidden kernel. This is a model choice, not a quotient of a larger structural group. The Gen18 theorem remains untouched: if a different structural model has hidden kernel, one chosen `a,b` lift pair is still insufficient and full lift-fiber transparency remains required.

## 2. Exact PF10 moduli

### 2.1 Base-Cell stabilizer orbits

Fix base Cell `A`. Its stabilizer is

`H_A=Stab_S4(A) ~= S3`.

Split the six channels into

`S={E1=AB,E2=AC,E3=AD}`

(the three edges incident to `A`) and

`F={E4=BC,E5=BD,E6=CD}`

(the opposite face).

`H_A` permutes the three vertices `B,C,D`, hence it acts transitively on `S` and transitively on `F`. Therefore the exact vector orbit partition has two blocks:

1. `S`;
2. `F`.

Thus `I_A` has two independent stabilizer-fixed values and `O_A` has two.

For ordered pairs, the exact eight `H_A` orbits are:

1. `S -> S`, equal;
2. `S -> S`, distinct;
3. `F -> F`, equal;
4. `F -> F`, distinct;
5. `S -> F`, adjacent tetrahedral edges;
6. `S -> F`, opposite tetrahedral edges;
7. `F -> S`, adjacent;
8. `F -> S`, opposite.

Thus `M_A` has eight independent stabilizer-fixed slots.

So structural symmetry imposes exactly

`2(I)+2(O)+8(M)=12`

independent raw PF10 value slots.

If all PF10 entries use one frozen scalar/value carrier `D`, the stabilizer-fixed locus is canonically `D^12`. More generally it is the corresponding product of the already-frozen allowed component domains over these twelve equality classes; this return adds no new value domain or normalization axiom.

The mandatory regressions are exact:

- full pointwise local `S4` vector orbits = `1`;
- full pointwise local `S4` ordered-pair orbits = `3` (equal / adjacent distinct / opposite);
- base tetra Cell stabilizer vector orbits = `2`;
- base tetra Cell stabilizer ordered-pair orbits = `8`.

### 2.2 Global reconstruction theorem

Let `P_A=(I_A,O_A,M_A)` be any `H_A`-fixed representative profile. For Cell `x`, choose any `g in S4` with `g(A)=x` and define

`P_x = rho(g) P_A`.

This is well-defined. If `g1(A)=g2(A)=x`, then `h=g2^-1 g1` fixes `A`, so `h in H_A`; because `P_A` is `H_A`-fixed,

`rho(g1)P_A=rho(g2)rho(h)P_A=rho(g2)P_A`.

The resulting family is globally equivariant by construction.

Conversely, every global equivariant family restricts at `A` to an `H_A`-fixed profile, and reconstructing from that profile returns the original family. Evaluation at `A` is therefore the inverse map.

Hence:

`GLOBAL_EQUIVARIANT_PF10_FAMILIES <-> Fix_{H_A}(PF10_A)`

exactly, with no duplicate raw families in the frozen canonical presentation.

### 2.3 Explicit nonconstant PF10 witness

For each Cell `x`, set

- `I_x(e)=1` iff tetrahedral edge/channel `e` is incident to `x`;
- `O_x=1-I_x`;
- `M_x=I_6`.

The four `I_x` vectors are different, so the family is raw Cell-to-Cell nonconstant. Yet every carrier permutation sends the incidence star of `x` to the incidence star of `g(x)`, the complement likewise, and `I_6` is invariant. Thus the family is exactly `S4`-equivariant.

Therefore transparency does not force PF10 to be pointwise constant.

## 3. Exact connection seed theorem

Choose oriented representative Cell edge `A -> B` and write

`t=T_AB in S6`.

Because `S4` acts transitively on oriented Cell edges, a global equivariant connection is determined by `t`, provided the seed is compatible with the oriented-edge stabilizer and the reverse-edge law.

### 3.1 Oriented-edge stabilizer

The pointwise stabilizer of the oriented edge `A -> B` is

`H_AB={1,(CD)} ~= C2`.

On the six channel labels, `(CD)` induces

`kappa=(E2 E3)(E4 E5)`.

Structural transport from `A->B` must be independent of the choice of carrier element carrying the representative edge to a target oriented edge. Therefore the exact seed condition is

`[t,kappa]=1`.

### 3.2 Reverse-edge law

The carrier transposition `b=(AB)` reverses `A->B`. On channels it induces

`lambda=(E2 E4)(E3 E5)`.

Equivariance gives

`T_BA=lambda t lambda^-1`.

The accepted inverse-edge law requires

`T_BA=t^-1`.

Because `lambda` is an involution,

`lambda t lambda=t^-1`.

Thus the exact seed locus is

`Z={t in S6 : [t,kappa]=1 and lambda t lambda=t^-1}`.

Every `t in Z` propagates uniquely by carrier conjugation to a well-defined global `S4`-equivariant inverse-consistent connection, and every such connection restricts back to a seed in `Z`. This is an exact bijection.

### 3.3 Twisted-involution reduction and exact count

`kappa` and `lambda` commute. Put

`s=lambda t`.

Then

`lambda t lambda=t^-1  <=>  (lambda t)^2=1  <=>  s^2=1`,

and because `[lambda,kappa]=1`,

`[t,kappa]=1  <=>  [s,kappa]=1`.

Therefore legal seeds are in bijection with involutions in the centralizer

`C_{S6}(kappa)`.

`kappa` has cycle type `2^2 1^2`, so

`|C_{S6}(kappa)| = 2^2 * 2! * 2! = 16`.

Structurally this centralizer is `(C2 wr S2) x C2`; its first factor has six elements whose square is identity (including identity), and the last `C2` doubles them. Hence it has exactly

`12`

involutions, and therefore `|Z|=12`.

The deterministic census gives the twelve seed cycle forms:

1. `id`;
2. `(E2 E3)(E4 E5)`;
3. `(E2 E4)(E3 E5)`;
4. `(E2 E4 E3 E5)`;
5. `(E2 E5 E3 E4)`;
6. `(E2 E5)(E3 E4)`;
7. `(E1 E6)`;
8. `(E1 E6)(E2 E3)(E4 E5)`;
9. `(E1 E6)(E2 E4)(E3 E5)`;
10. `(E1 E6)(E2 E4 E3 E5)`;
11. `(E1 E6)(E2 E5 E3 E4)`;
12. `(E1 E6)(E2 E5)(E3 E4)`.

Exactly one is the raw identity connection; the other eleven are raw nonidentity connections.

## 4. Accepted gauge quotient

Gen10 already froze the local presentation-gauge law. For arbitrary local channel relabelings `g_x in S6`,

`T'_xy = g_y T_xy g_x^-1`,

and for a loop based at `x`,

`Hol'_x(gamma)=g_x Hol_x(gamma) g_x^-1`.

Use the star spanning tree

`AB, AC, AD`.

Every connection can be gauge-normalized so these three tree transports are identity. The remaining transports on

`BC, BD, CD`

form a triple. After tree normalization, the only remaining root gauge acts by simultaneous conjugation on this triple.

Therefore two connections on K4 are gauge-equivalent exactly when their three normalized non-tree transports are simultaneously `S6`-conjugate.

Applying this exact criterion to the twelve equivariant seeds gives eight gauge classes:

| class | seed representative | other raw member, if any | flat? |
|---|---|---|---|
| `C0` | `id` | `(E2 E5)(E3 E4)` | yes |
| `C1` | `(E2 E3)(E4 E5)` | — | no |
| `C2` | `(E2 E4)(E3 E5)` | — | no |
| `C3` | `(E2 E4 E3 E5)` | `(E2 E5 E3 E4)` | no |
| `C4` | `(E1 E6)` | `(E1 E6)(E2 E5)(E3 E4)` | no |
| `C5` | `(E1 E6)(E2 E3)(E4 E5)` | — | no |
| `C6` | `(E1 E6)(E2 E4)(E3 E5)` | — | no |
| `C7` | `(E1 E6)(E2 E4 E3 E5)` | `(E1 E6)(E2 E5 E3 E4)` | no |

Thus:

- raw solutions = `12`;
- raw flat = `2`;
- raw nonflat = `10`;
- gauge classes = `8`;
- flat gauge classes = `1`;
- nonflat gauge classes = `7`.

The second raw flat seed is therefore pure gauge, as expected from Gen10; flatness is exactly what permits gauge reduction to a global parallel frame connection on connected K4.

## 5. Holonomy classification

Use the K4 rank-three triangle basis

- `A-B-C-A`;
- `A-B-D-A`;
- `A-C-D-A`.

For every equivariant connection and every `u in S4`, the checker verifies the frozen holonomy conjugacy law

`Hol_{u(x)}(u gamma)=rho(u) Hol_x(gamma) rho(u)^-1`.

Within one gauge class, local gauge changes conjugate the based holonomy triple simultaneously. The eight gauge-class representatives have the following exact fingerprints:

| class | triangle holonomy cycle type | order of subgroup generated by the three basis holonomies |
|---|---:|---:|
| `C0` | `1+1+1+1+1+1` | `1` |
| `C1` | `4+2` | `24` |
| `C2` | `2+2+1+1` | `6` |
| `C3` | `2+1+1+1+1` | `6` |
| `C4` | `2+2+2` | `2` |
| `C5` | `2+2+2` | `6` |
| `C6` | `4+1+1` | `24` |
| `C7` | `5+1` | `60` |

For each class, the three basis triangle holonomies have one common `S6` conjugacy cycle type, as forced by carrier symmetry. `C4` and `C5` show why the cycle type of one triangle alone is not a complete gauge-class invariant: both use triple transpositions, but their three holonomies generate subgroups of orders `2` and `6`, respectively.

Only `C0` is flat. Hence nonflat equivariant connection content occupies seven distinct accepted gauge classes.

## 6. Same-model nondegenerate witness

Take the nonconstant PF10 family of §2.3 and, on the same four Cells and same six local channels, take connection seed

`T_AB=(E1 E6)`.

Carrier propagation gives the exact Gen18 rule:

> for every Cell edge `e`, the transport on that edge swaps channel `e` with its unique opposite tetrahedral channel.

This is class `C4`.

For each basis triangle, the holonomy is the global opposite-edge involution

`omega=(E1 E6)(E2 E5)(E3 E4) != id`.

So the connection is nonidentity and nonflat, while remaining fully carrier-`S4` equivariant.

The PF10 and connection are not separately constructed witnesses later pasted together: they are stored simultaneously on the same `A,B,C,D` Full-Cell carrier model, share the same structural channel action, and both satisfy their independent Gen17 transparency gates.

Because the complete enriched data are invariant under the structural `S4` action generated by `a,b`, and the underlying permutations satisfy

`a^3=b^2=(ab)^4=id`,

the same relations hold on the complete enriched model.

This closes the common-model requirement without adding a coupling axiom.

## 7. Degeneracy questions answered

The Gen19/21 degeneracy questions have exact answers.

### PF10 pointwise constancy

False. The stabilizer-fixed locus has twelve raw slots, strictly richer than a pointwise fully `S4`-fixed local tensor, and §2.3 gives a four-profile nonconstant global family.

### Connection gauge-equivalent to identity

False. Seven of the eight connection gauge classes are nonflat. Nontrivial loop holonomy is invariant under the accepted local gauge up to conjugation, so none of those seven classes can be gauge-equivalent to identity.

### Gen18 nonflat witness isolated?

False. The Gen18 edge-to-opposite connection is one nonflat gauge class among seven. The finite moduli space contains six further nonflat gauge classes with distinct simultaneous holonomy fingerprints.

Thus the transparency gates preserve substantial nondegenerate content.

## 8. Deterministic checker

The checker

`research_checks/P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V21_CHECK_20260901.py`

passes deterministically and verifies:

- `|S4|=24` and `<a,b>=S4`;
- full local vector orbit count `1`;
- full local ordered-pair orbit count `3`;
- base Cell stabilizer vector orbit count `2`;
- base Cell stabilizer ordered-pair orbit count `8`;
- symbolic twelve-slot PF10 parameterization and global reconstruction independence;
- an explicit nonconstant equivariant PF10 family;
- typed connection universe `S6` of order `720`;
- oriented-edge centralizer order `16`;
- exact legal seed count `12`;
- global naturality and inverse-edge consistency for all twelve seeds;
- raw flat/nonflat counts `2/10`;
- exact local-`S6` gauge partition into eight classes;
- holonomy conjugacy and the eight fingerprints above;
- exact recovery of the Gen18 edge-to-opposite nonflat connection;
- one same-model nonconstant-PF10/nonflat-connection witness;
- enriched `a^3`, `b^2`, `(ab)^4` relations;
- P000/Gen17/Gen18 guard declarations.

The task-local checker was independently executed during this run and returned `PASS`.

## 9. Guard audit

Preserved exactly:

- `P000_ROOT_ONTOLOGY_MUTATED = FALSE`;
- `G15_GRAMMAR_MUTATED = FALSE`;
- `GEN17_GATE_COUNT_OR_COST_MUTATED = FALSE`;
- `GEN18_FULL_LIFT_FIBER_CRITERION_MUTATED = FALSE`;
- `NO_KERNEL_QUOTIENT = TRUE`;
- `TIME_FIXED = TRUE`;
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`;
- local channel `S6` remains presentation/gauge only;
- no gauge or presentation bit is counted as a native spatial axis.

No `UNIQUE_SECTION` claim is made.

## 10. Tool reuse / method harvest

No new general-purpose tool family is proposed.

This execution reuses the accepted finite symmetry/orbit enumeration pattern from Gen17/18 and the accepted Gen10 gauge/holonomy law, then specializes them to the finite moduli census required here. The novel payload is the task result:

- twelve-slot PF10 stabilizer parameterization;
- twisted-involution seed theorem;
- exact `12 -> 8` connection gauge quotient;
- seven nonflat gauge classes with exact holonomy fingerprints;
- one common nondegenerate enriched model.

Method disposition: `RESULT_ONLY`.

## 11. Final disposition

Hard target:

`P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_AND_COMMON_NONDEGENERATE_MODEL_EXACTLY_CLASSIFIED`

is closed at the frozen K4/tetra `S4` carrier and typed `S6` independent-connection strength.

Unresolved residue inside this task: `NONE`.

Driver review remains required before any Working Truth, Foundation, canonical promotion, or downstream semantic mutation.

Recommended Driver action: audit the finite checker and certificate; if accepted, freeze the eight connection gauge classes and twelve-slot PF10 orbit parameterization as the closed Gen21 moduli result, retain Gen18 full-lift-fiber logic unchanged, and route any successor to the next native-P000 bridge question rather than reopening existence/nonflatness.
