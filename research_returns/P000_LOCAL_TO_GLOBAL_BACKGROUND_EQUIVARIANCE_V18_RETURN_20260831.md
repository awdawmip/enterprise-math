# Research Return — P000 local-to-global background equivariance V18

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-D6A41E9C3B705F821847`  
Researcher: `EM-P000FCC18-ED9B7E`  
Claim: `chatgpt-p000fcc18-20260831-1038-ed9b7e`  
Execution: `ER-B9CD98FA15252AC5E07C`  
Result: `RR-7FED4A83F3922D37319D`  
Status: `SUCCESS / LOCAL_GENERATOR_EQUIVARIANCE_EXACTLY_EQUIVALENT_TO_GLOBAL_BACKGROUND_TRANSPARENCY`

## 0. Terminal theorem

Generation 18 closes

`P000_LOCAL_TO_GLOBAL_PF10_AND_CONNECTION_S4_EQUIVARIANCE_CRITERIA_EXACTLY_DERIVED_OR_INFORMATION_THEORETICALLY_OBSTRUCTED`.

The exact outcome is stronger than either “the Gen17 global gates are irreducible” or “checking one chosen pair of carrier generators is always enough”.

Let

- `G0` be the Gen17 structural automorphism group before contentful PF-10 / independent-connection restriction;
- `q0:G0 -> S4` be the frozen carrier readout;
- `K=ker(q0)`;
- `a=(BCD)`, `b=(AB)`, so `<a,b>=S4`;
- for a retained background `B`, `G_B={u in G0 : u preserves B}`.

Then the Gen17 global transparency condition is `G_B=G0`.

### Theorem V18.1 — full lift-fiber generator criterion

Define

`GENERATOR_FIBER_EQ(B)`

to mean that **every** structural lift in the two fibers `q0^{-1}(a)` and `q0^{-1}(b)` preserves `B`.

Assume `q0` is surjective. Then

`GENERATOR_FIBER_EQ(B)  <=>  G_B=G0`.

So the Gen17 global quantifier over all `u in G0` can be replaced exactly by two carrier-generator **lift-fiber** tests.

Proof. The reverse implication is immediate. For the forward implication, choose `ahat in q0^{-1}(a)`. For every `k in K`, `k ahat` is another lift of `a`; both `ahat` and `k ahat` lie in `G_B`, hence `k=(k ahat) ahat^{-1}` lies in `G_B`. Thus `K<=G_B`. Likewise one lift each of `a,b` lies in `G_B`, and their images generate `S4`. Given arbitrary `g in G0`, choose a word `w` in those preserved lifts with `q0(w)=q0(g)`. Then `g w^{-1} in K<=G_B`, so `g in G_B`. Therefore `G_B=G0`.

This is a genuine local-to-global reduction: only the two carrier generator fibers need to be checked. It does **not** quotient or ignore hidden kernel.

### Theorem V18.2 — chosen-lift criterion and exact hidden-kernel obstruction

Suppose instead one freezes only one coherent lift `ahat` of `a` and one coherent lift `bhat` of `b`. Let `H=<ahat,bhat>`.

Then chosen-lift `a,b` equivariance proves only

`H <= G_B`.

It is equivalent to full transparency exactly when `H=G0`; more generally, because `q0(H)=S4`, it becomes equivalent after adding

`K <= G_B`.

The exact countermodel is

`G0=C2 x S4`, `q0(k,g)=g`,

with chosen lifts `(0,a),(0,b)` and background stabilizer

`G_B={0} x S4`.

Both chosen generator lifts preserve the background, but the nontrivial `C2` kernel element does not. Exact sizes are

`|G0|=48`, `|H|=24`, `|K|=2`, `|K intersect G_B|=1`.

Thus the statement “`a,b` equivariance implies global transparency” is correct only when “generator equivariance” means either:

1. the chosen lifts actually generate all of `G0`; or
2. kernel transparency is separately known; or
3. one checks the **entire lift fibers** of `a,b`.

This is the precise `NO_KERNEL_QUOTIENT` boundary.

## 1. PF-10 local-to-global ladder

For the visible tetrahedral regression, Cells are `A,B,C,D` and the six carrier channels are the tetrahedral edges

`E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`.

The exact finite checker verifies the following non-implications.

### 1.1 One-Cell stabilizer/orbit regularity

At Cell `A`, full equivariance requires the local profile to be fixed by `Stab(A)=S3`. This condition is necessary on a transitive Cell orbit, but is not sufficient for coherent global transport.

Take `star_A=(1,1,1,0,0,0)`. It is `Stab(A)`-fixed. Assign it to every Cell. All Cells have the same local orbit type and the family is `a`-equivariant because `a=(BCD)` fixes the `A`-star, but the family is not `b`-equivariant and hence not globally transparent.

Conversely, “same local orbit type at every Cell” does not imply one-Cell stabilizer regularity: the constant profile `e_AB=(1,0,0,0,0,0)` has one common `S4` orbit type at every Cell, but is not fixed by `Stab(A)`.

Also, one-Cell regularity plus `a`-equivariance does not force the same orbit type globally: set the `A` profile to `star_A` and the `B,C,D` profiles to zero. The `a`-cycle preserves this assignment, but the local types differ.

Therefore the first two ladder conditions are genuine local regularity statements, not hidden symmetry theorems.

### 1.2 Single-generator conditions

Each single generator is strictly insufficient.

- `a` only: the constant `star_A` family is `a`-equivariant and not `b`-equivariant.
- `b` only: the constant `e_AB` family is `b`-equivariant because `b=(AB)` fixes edge `AB`, but is not `a`-equivariant.

These are exact visible finite countermodels.

### 1.3 Both generators

On the faithful visible `S4` action, coherent `a,b` equivariance implies full visible `S4` equivariance because `<a,b>=S4`.

For the actual Gen17 structural group, the correct statement is Theorem V18.1/V18.2:

- both **chosen** lifts imply invariance under their generated subgroup `H`;
- both **full lift fibers** imply full `PF10_STRUCTURAL_AUT_EQ`;
- chosen lifts suffice if the background is already known kernel-transparent or if `H=G0`.

Thus the exact local replacement for the Gen17 PF-10 gate is:

`PF10_GENERATOR_FIBER_EQ(a,b)`.

It is an equivalent verification form of the existing gate, not a new cheaper G17 atomic primitive.

## 2. Independent-connection ladder

Write the connection naturality law as

`T_{u(x),u(y)} Pi_x^u = Pi_y^u T_xy`.

Exactly the same group-generation theorem applies to this law because preservation of the entire connection is again a subgroup condition in `G0`.

### 2.1 Edgewise local type and inverse consistency

Merely requiring one edgewise transport type is weaker than connection coherence. The checker assigns the same order-three channel permutation to every oriented edge; all local transport types agree, but `T_yx != T_xy^{-1}`.

Inverse-edge consistency is still not a symmetry statement. It only says reverse transport is inverse transport.

### 2.2 Path composition

Under the standard connection semantics used in the earlier generations, transport along a path is the ordered product of edge transports. Associativity/path concatenation is then definitional; inverse-edge consistency gives the expected cancellation on backtracking.

If a model independently stores path transports rather than deriving them from edges, path composition is an additional functoriality axiom. In either interpretation it remains strictly weaker than structural naturality.

### 2.3 Single generators

Both single-generator conditions are strictly insufficient.

- `b` only: the Gen17 marked-edge connection with `T_AB=(E1 E6)` and all other undirected edge transports identity is `b`-natural but not `a`-natural.
- `a` only: propagate the same seed around the `a` orbit `AB -> AC -> AD` by conjugation, use identity on the other `a` edge orbit, and impose inverse reverse transports. This connection is exactly `a`-natural and not `b`-natural.

### 2.4 Both generators

The exact criterion mirrors PF-10:

- naturality for one chosen `ahat,bhat` pair controls only `H=<ahat,bhat>`;
- naturality for the full structural lift fibers `q0^{-1}(a),q0^{-1}(b)` is exactly equivalent to `CONNECTION_STRUCTURAL_AUT_EQ`;
- chosen-lift naturality plus kernel naturality is also equivalent.

Again, no kernel quotient is used.

### 2.5 Holonomy is a consequence, not an equivalent local replacement

Full connection transparency implies

`Hol_{u(x)}(u gamma)=Pi_x^u Hol_x(gamma) (Pi_x^u)^{-1}`

for every cycle, hence on any generating cycle basis.

The converse fails even if inverse consistency and path composition hold.

Take vertex gauges `h_A=s`, `h_B=h_C=h_D=1`, with `s` an order-three channel permutation, and define the independent connection

`T_xy=h_y h_x^{-1}`.

This is flat pure gauge: every cycle holonomy is exactly identity, so holonomy conjugacy holds on every cycle basis. But the gauge choice is structurally asymmetric and the connection fails full structural naturality. Therefore

`HOLONOMY_CONJUGACY_ON_GENERATING_BASIS != CONNECTION_STRUCTURAL_AUT_EQ`.

Conversely, nontrivial holonomy is fully compatible with symmetry. On K4, assign to each Cell edge `e` the order-two channel transport swapping channel `e` with its unique opposite tetrahedral edge. This assignment is `S4`-equivariant, inverse-consistent, and its triangle holonomy is the nonidentity global opposite-edge involution. Hence

`NONFLAT_CONNECTION != SYMMETRY_OBSTRUCTION`

is reverified exactly.

## 3. PF-10 / connection coupling question

There **is** one common mathematical proof schema:

> a retained background is a `G0`-equivariant object over the structural action groupoid; full structural equivariance is equivalent to equivariance on the full lift fibers of carrier generators `a,b`.

That is a genuine theorem because it replaces an all-`G0` global check by a finite generating-family check while retaining hidden kernel information through the lift fibers.

But it is **not** one new atomic background constraint.

PF-10 and the independent connection remain independently falsifiable. The four combinations are all realized:

1. PF-10 transparent / connection transparent;
2. PF-10 transparent / connection leaky;
3. PF-10 leaky / connection transparent;
4. PF-10 leaky / connection leaky.

Therefore a macro such as

`ALL_BACKGROUND_GENERATOR_FIBER_EQ`

must still normalize to the PF-10 instance plus the independent-connection instance. The Gen17 atomicity firewall and costs remain unchanged. Generation 18 changes the *verification form*, not the semantic constraint count.

## 4. Exact finite information-cost statement

Generation 18 distinguishes logical axiom count from finite model-selection information.

### 4.1 General kernel index

For finite `K=ker(q0)` and `K_B=K intersect G_B`, chosen-lift generator equivariance omits the kernel orbit of the background. The exact orbit index is

`[K:K_B]`.

For the exhibited finite family, the missing kernel-selection information is therefore

`log2 [K:K_B]` bits.

In the `C2 x S4` countermodel,

`[K:K_B]=2`,

so the hidden-kernel omission carries exactly `1` bit of orbit-index information.

This is why two chosen carrier generators can look complete in the quotient and still miss one independent hidden binary symmetry choice.

### 4.2 Visible Gen17 marker witnesses

The PF-10 `e_AB` marker has stabilizer order `4` in `S4`, hence visible orbit size

`24/4=6`

and orbit-index information

`log2 6 = 2.584962500721156...` bits.

The marked-edge independent connection has the same exact stabilizer order `4` and the same six-position orbit index.

Because the two marker choices are logically independent, the raw product witness family has

`6*6=36`

independent labeled choices, requiring

`log2 36 = 5.169925001442312...` bits

to specify both marks.

These numbers are exact finite orbit-index measurements for the exhibited witness families. They are **not** claimed as a universal Shannon/Kolmogorov minimum across every admissible P000 background model.

### 4.3 Logical count remains separate

When an independent connection is retained, Gen17 still has two independently charged semantic gate instances:

- PF-10 transparency;
- connection transparency.

Generation 18 does not collapse them to one `g=1` condition. It only proves that each can be verified by the same two-generator lift-fiber theorem.

## 5. Positive Gen17 regression from the weakest exact local criteria

The Gen17 conditional K4 result reconstructs without directly assuming a global all-automorphism formula.

### 5.1 No independent connection / frame-induced connection

Assume:

1. `K4_ADJ`;
2. PF-10 full-lift-fiber equivariance for `a,b`.

By Theorem V18.1, condition 2 implies `PF10_STRUCTURAL_AUT_EQ`. Frame-induced transport remains automatically natural. Therefore the Gen17 enriched group equals the K4 structural group, and the frozen Gen14/Gen17 proof gives:

- faithful `S4` splitting;
- an `Aut_prim`-fixed canonical section;
- no `UNIQUE_SECTION` claim.

The frozen Gen17 cost remains exactly

`(0,0,0,0,0,0,2,0)`.

### 5.2 Independent connection declared

Assume:

1. `K4_ADJ`;
2. PF-10 full-lift-fiber equivariance for `a,b`;
3. connection full-lift-fiber naturality for `a,b`.

The two generator-fiber theorems derive the two Gen17 global gates. The Gen17 faithful/canonical result follows with unchanged cost

`(0,0,0,0,0,0,3,0)`.

No new G15/G17 cost coordinate or cheaper macro is introduced.

## 6. Mandatory negative regressions

All required boundaries remain live.

- PF-10 `e1` profile: visible compatibility order `4<24`.
- Marked-edge independent connection: visible compatibility order `4<24`.
- P4 structural model: background transparency cannot enlarge a structurally reduced carrier image.
- Gen13 nonsplit hidden-kernel model: precisely motivates the chosen-lift/kernel distinction.
- Gen13 split/noncanonical model: full carrier surjectivity still does not imply uniqueness/canonicality without the frozen Gen14 fixed-point condition.

The new theorem does not mutate P000, does not identify carrier `S4` with the complete native P000 rotation group, and does not quotient hidden kernel.

## 7. Exact implication summary

### PF-10

`FULL GLOBAL TRANSPARENCY`
`=> full-lift-fiber a,b equivariance`
`=> chosen-lift a,b equivariance`
`=> each chosen single-generator condition`.

The first implication reverses exactly: full-lift-fiber `a,b` is equivalent to global transparency.

Chosen-lift `a,b` reverses only under `H=G0` or `K<=G_B`.

One-Cell stabilizer regularity and same-local-orbit-type conditions are necessary/useful local consistency tests but do not sit as a sufficient chain to generator equivariance; explicit countermodels separate them.

### Connection

`FULL CONNECTION TRANSPARENCY`
`=> full-lift-fiber a,b naturality`
`=> chosen-lift a,b naturality`
`=> a-only and b-only separately`;

again the first implication reverses exactly, while the chosen-lift reversal needs `H=G0` or kernel naturality.

Full transparency also implies cycle-basis holonomy conjugacy, but that implication does not reverse.

## 8. Verification

Deterministic checker:

`research_checks/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_CHECK_20260831.py`

Self-test result:

`PASS P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18_CHECK`.

Exact finite checks include:

- carrier `S4` order `24`;
- visible `<a,b>=S4`;
- PF-10 a-only and b-only countermodels;
- hidden extension `G0=C2 x S4` order `48`;
- chosen section `H` order `24`;
- hidden kernel order `2`;
- full `a,b` lift fibers generate all `48` elements;
- connection a-only and b-only countermodels;
- flat/holonomy-trivial but nonequivariant connection;
- nonflat but fully equivariant connection;
- PF-10 marker stabilizer order `4`, orbit index `6`;
- connection marker stabilizer order `4`, orbit index `6`;
- independent raw marker product count `36`.

Certificate:

`research_artifacts/P000_LOCAL_TO_GLOBAL_BACKGROUND_EQUIVARIANCE_V18/LOCAL_TO_GLOBAL_EQUIVARIANCE_CERTIFICATE.json`.

## 9. Terminal disposition

Terminal class:

`LOCAL_GENERATOR_EQUIVARIANCE_EXACTLY_EQUIVALENT_TO_GLOBAL_BACKGROUND_TRANSPARENCY`.

The precise interpretation is **full structural lift-fiber generator equivariance**. Checking only one arbitrarily chosen `a,b` lift pair is not silently promoted to a global theorem in the presence of hidden kernel.

No P000 root promotion, Working Truth promotion, kernel quotient, Gen15 mutation, Gen17 cost mutation, or canonical source mutation is authorized by this Researcher return.

Next control-plane action: Driver review this Generation-18 theorem. If accepted, the Gen17 global background gates can be retained semantically while their proof/check interface is sharpened to generator lift-fibers; any later grammar optimization must preserve two independently falsifiable background instances and the hidden-kernel boundary.
