# P000 six-axis mixed-invariant alignment compression return

Status: `SUCCESS / MINIMAL_MIXED_PACKET_FOUND / DERIVED-ONLY / DRIVER_REVIEW_PENDING`

- Task: `RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION`
- Publication: `TP2-DD63F0FB296D3DBBE311`
- Researcher: `EM-P000MIAC1-3DBBE1`
- Claim: `chatgpt-p000miac1-20260830-2324-3dbbe1`
- Execution record: `ER-9E4FE4B244F9F4A9E8EF`
- Result: `RR-B96585874709743F94BC`
- Frozen taskbook: `research_tasks/P000_SIX_AXIS_MIXED_INVARIANT_ALIGNMENT_COMPRESSION_V2_20260830.md` / `sha1:02ba87854c8fb5336985b215725d126786ef0cba`
- Parent Result: `RR-2FFF3D2DFED3FF2535E3`
- Parent Driver review: `DR-58E2B5C0EC95B39C59CF`

Hard target:

`P000_SIX_AXIS_ALIGNMENT_RESIDUE_MINIMAL_MIXED_INVARIANT_PACKET_CLASSIFIED_OR_FROZEN_GRAMMAR_INSUFFICIENT`.

Terminal disposition:

`MINIMAL_MIXED_PACKET_FOUND`.

The exact answer inside the frozen grammar is:

`MINIMAL_CARDINALITY=2`.

There are exactly two globally sufficient minimal subpackets,

`{P11,P21}` and `{P11,P12}`,

and `P11` belongs to every sufficient subpacket. The pair `{P21,P12}` is not sufficient.

## 1. Frozen interface and invariance

The parent interface supplies the separate multisets

`H={h1,h2,h3}`, `T={t1,t2,t3}`

and asks only for the residual relative matching needed to reconstruct

`K=multiset{(h_i,t_i)}`

modulo the declared derived symmetry `Gamma=C2 wr S3`.

The frozen mixed grammar is

- `P11=sum_i h_i t_i`;
- `P21=sum_i h_i^2 t_i`;
- `P12=sum_i h_i t_i^2`.

The `C2^3` within-pair swaps preserve every `h_i=a_i+b_i` and `t_i=a_i b_i`. The `S3` factor simultaneously permutes the three pair labels. Hence every `Pab=sum_i h_i^a t_i^b` above is exactly `Gamma`-invariant.

The pairability gate is exact: `(h,t)` comes from one unordered integer pair `{a,b}` iff

`Delta=h^2-4t`

is a nonnegative perfect square and `sqrt(Delta) == h (mod 2)`. Once the aligned packet `K` is known, this gate recovers the three unordered local integer pairs, exactly at the parent Result's derived strength.

## 2. `{P11,P21}` is globally sufficient

Assume first that `H` has three distinct values. Choose any ordering `(h_i,h_j,h_k)` of the known multiset and write `S_T=sum T`. The equations

`S_T=t_i+t_j+t_k`,
`P11=h_i t_i+h_j t_j+h_k t_k`,
`P21=h_i^2 t_i+h_j^2 t_j+h_k^2 t_k`

form a Vandermonde system. Lagrange elimination gives the exact formula

`t_i = [P21-(h_j+h_k)P11+h_j h_k S_T] / [(h_i-h_j)(h_i-h_k)]`.

Thus all three `t_i` are recovered and therefore so is `K`.

If `H={h,h,k}` with `k!=h`, then

`t_at_k=(P11-h S_T)/(k-h)`.

The remaining two products are attached to equal `h` values, so swapping them does not change the multiset `K`. If all three `h` values are equal, `K` was already determined by the separate marginals. Therefore `{P11,P21}` is globally sufficient on all multiplicity strata.

## 3. `{P11,P12}` is globally sufficient

The exact dual argument uses the known `S_H=sum H`. When `T` has three distinct values,

`h_i = [P12-(t_j+t_k)P11+t_j t_k S_H] / [(t_i-t_j)(t_i-t_k)]`.

When `T={t,t,u}` with `u!=t`,

`h_at_u=(P11-t S_H)/(u-t)`,

and the two equal-`t` slots are indistinguishable in `K`. Triple `T` is already aligned. Hence `{P11,P12}` is also globally sufficient.

This proves that cardinality two is enough. It remains to prove minimality and to classify the other subsets.

## 4. Exact insufficiency witnesses and necessity of `P11`

### 4.1 `P11` alone fails

Fix

`H={-4,-1,1}`, `T={-30,-12,0}`.

Two pairable aligned packets are

`K_A={(-4,-12),(-1,0),(1,-30)}`,
`K_B={(-4,0),(-1,-30),(1,-12)}`.

Their local unordered root pairs are respectively

`K_A: {-6,2},{-1,0},{-5,6}`,
`K_B: {-4,0},{-6,5},{-3,4}`.

Both have

`P11=18`,

but

`(P21,P12)(K_A)=(-222,324)`,
`(P21,P12)(K_B)=(-42,-756)`.

So `{P11}` is insufficient.

### 4.2 `{P21,P12}` fails

Fix

`H={-5,0,5}`, `T={-6,-1,6}`.

Take

`K_A={(-5,-6),(0,-1),(5,6)}`,
`K_B={(-5,6),(0,-1),(5,-6)}`.

All six displayed `(h,t)` states are pairable. Both packets have

`P21=0`, `P12=0`,

while

`P11(K_A)=60`, `P11(K_B)=-60`.

Thus even retaining both moments that omit `P11` does not determine the alignment. Consequently every globally sufficient subpacket of the frozen three-moment grammar must contain `P11`. In particular `P21` alone and `P12` alone are also insufficient.

Together with Sections 2-3, this proves that the only inclusion-minimal sufficient subpackets are exactly

`{P11,P21}`, `{P11,P12}`.

The full triple is sufficient but redundant.

## 5. Exact residual-fiber atlas

For fixed separate marginals `H,T`, let the fiber size be the number of distinct aligned `K/Gamma` packets retaining the listed mixed data. The global sharp maxima are

| retained mixed data | global maximum fiber | classification |
|---|---:|---|
| none | 6 | insufficient |
| `P11` | 2 | insufficient |
| `P21` | 3 | insufficient |
| `P12` | 3 | insufficient |
| `P11,P21` | 1 | sufficient |
| `P11,P12` | 1 | sufficient |
| `P21,P12` | 2 | insufficient |
| all three | 1 | sufficient, redundant |

The upper bounds are exact.

For `P11`, if one marginal has a `2+1` multiplicity then `P11` identifies the value attached to the unique slot. If both marginals are distinct, the six relative assignments are the vertices of the strict `S3` permutahedron; a linear level set meets at most two vertices. The witness in Section 4.1 attains two.

For `P21`, the assignment weights are `h_i^2`. Three distinct squares reduce to the same strict-permutahedron bound two; a `2+1` square pattern leaves at most a two-way swap; and when all three squares are equal the multiset `H` uses only `a,-a`, leaving at most three choices for the product attached to the minority sign. The sharp three-way witness is

`H={-5,-5,5}`, `T={-6,0,6}`.

Every cross-state needed for the three minority-slot choices is pairable, and `P21=25*sum(T)=0` for all three.

The `P12` argument is dual in `T^2`. A sharp three-way integer-pairable witness is

`H={-29,29,37}`, `T={-210,210,210}`.

Each of the three `h` values is pairable with both `210` and `-210`, and

`P12=210^2*sum(H)=1,631,700`

regardless of which `h` is attached to the unique `-210`.

For `{P21,P12}`, a three-way `P21` fiber can occur only in the all-equal `h_i^2` regime. Writing the majority sign as `a` and the minority as `-a`, the `P12` value for minority product `t_j` is

`a*sum_i t_i^2 - 2a*t_j^2`.

Three distinct alignment orbits could remain equal only if three distinct products had equal squares, impossible because one absolute value has at most two integer signs. Hence the joint fiber is at most two; Section 4.2 attains two.

The empty packet has the parent sharp six-way witness

`H={-3,3,9}`, `T={-70,-10,0}`;

all six matchings pass the exact pairability gate.

## 6. Frozen deterministic census

Before reading census outcomes I froze the finite regression universe to all unordered local root pairs

`-6 <= a <= b <= 6`.

This gives exactly `91` distinct relation states `(h=a+b,t=ab)` and exactly

`C(91+3-1,3)=129,766`

three-state `K/Gamma` multisets. There was no adaptive enlargement after outcomes.

The exact checker evaluates all eight frozen subpackets and also verifies the reconstruction formulas on every applicable census orbit. It returns:

`EMPTY:4, P11:2, P21:3, P12:2, P11_P21:1, P11_P12:1, P21_P12:2, ALL:1`.

The global `EMPTY=6` and `P12=3` maxima are certified separately by the exact fixed witnesses above; they intentionally lie outside the frozen `B=6` census. Thus the finite computation is only regression/falsification evidence and is not used as an all-domain proof.

Checker expected terminal line:

`PASS task=RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION checks=1386781 B=6 relation_states=91 K_orbits=129766 census_max=EMPTY:4,P11:2,P21:3,P12:2,P11_P21:1,P11_P12:1,P21_P12:2,ALL:1 global_max=EMPTY:6,P11:2,P21:3,P12:3,P11_P21:1,P11_P12:1,P21_P12:2,ALL:1 minimal=P11+P21|P11+P12`.

## 7. Pfaffian-orientation firewall

The parent oriented scalar is

`Q=t1-t2+t3=S_T-2*t_negative_slot`.

A `Gamma`-invariant alignment packet can reconstruct `K/Gamma`, but `Gamma` contains the complementary-pair permutations and therefore does not select the distinguished negative slot. Even after a minimal sufficient mixed packet has reconstructed the aligned derived state, the oriented scalar candidate set remains exactly

`{S_T-2t : t in distinct(T)}`.

Hence there are exactly:

- `1` candidate if `T` is triple;
- `2` candidates on a `2+1` product stratum;
- `3` candidates when the three products are distinct.

No mixed-invariant success here is a native signed-carrier, orientation, Full-Cell, dimension-reduction, or factorization statement.

## 8. Prior-art boundary

The invariant-theory ingredients are classical and are not claimed as Enterprise novelty.

- Francesco Vaccarino, *The ring of multisymmetric functions*, Annales de l'Institut Fourier 55(3) (2005), 717-731, DOI `10.5802/aif.2111`, treats diagonal permutation invariants/multisymmetric functions and their generators/relations over commutative rings.
- David Rydh, *A minimal set of generators for the ring of multisymmetric functions*, Annales de l'Institut Fourier 57(6) (2007), 1741-1769, DOI `10.5802/aif.2312`, gives explicit minimal generator results for multisymmetric rings.
- The Vandermonde/Lagrange reconstruction used above is standard classical interpolation.

Accordingly `P11,P21,P12` are ordinary polarized/multisymmetric mixed power sums. The task-specific result is only the exact **frozen-interface specialization**: after the separate `H,T` marginals, the integer-pairability gate, and this three-moment grammar are fixed, `P11` plus either asymmetric second mixed moment is necessary and sufficient, with the exact fiber atlas above. No historical novelty claim is made.

## 9. Scope and control disposition

Freeze:

`MINIMAL_MIXED_PACKET_FOUND`.

`MINIMAL_CARDINALITY=2`.

`MINIMAL_PACKETS={P11,P21} OR {P11,P12}`.

`P11_NECESSARY_WITHIN_FROZEN_GRAMMAR=TRUE`.

`P21_P12_WITHOUT_P11_INSUFFICIENT=TRUE`.

`ORIENTATION_FIREWALL_PRESERVED=TRUE`.

This Result remains `RESULT_ONLY / NOT_INDEPENDENT / NONBLIND_DISCLOSED`. It grants no Working Truth, Foundation, L4, native geometry, native orientation, factorization mechanism, or canonical promotion.

Next control-plane action: Driver review this immutable Result. The researcher lane makes no downstream task decision.
