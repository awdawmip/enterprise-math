# P000 six-axis mixed-invariant alignment compression return

Status: `SUCCESS / MINIMAL_MIXED_PACKET_FOUND / DERIVED-ONLY / DRIVER_REVIEW_PENDING`

- Task: `RS-P000-SIX-AXIS-MIXED-INVARIANT-ALIGNMENT-COMPRESSION`
- Publication: `TP2-DD63F0FB296D3DBBE311`
- Researcher: `EM-P000MIAC1-3DBBE1`
- Claim: `chatgpt-p000miac1-20260830-2324-3dbbe1`
- Execution record: `ER-9E4FE4B244F9F4A9E8EF`
- Result: `RR-B96585874709743F94BC`
- Taskbook: `research_tasks/P000_SIX_AXIS_MIXED_INVARIANT_ALIGNMENT_COMPRESSION_V2_20260830.md` / `sha1:02ba87854c8fb5336985b215725d126786ef0cba`
- Parent accepted Result: `RR-2FFF3D2DFED3FF2535E3`
- Parent Driver review: `DR-58E2B5C0EC95B39C59CF`

Hard target:
`P000_SIX_AXIS_ALIGNMENT_RESIDUE_MINIMAL_MIXED_INVARIANT_PACKET_CLASSIFIED_OR_FROZEN_GRAMMAR_INSUFFICIENT`.

Terminal disposition:
`MINIMAL_MIXED_PACKET_FOUND`.

## 1. Exact classification

With separate marginals `H={h1,h2,h3}` and `T={t1,t2,t3}` already supplied, freeze

`P11=sum_i h_i t_i`,
`P21=sum_i h_i^2 t_i`,
`P12=sum_i h_i t_i^2`.

The global subset classification is:

| retained moments | maximum residual `K/Gamma` fiber | verdict |
|---|---:|---|
| none | 6 | insufficient |
| `P11` | 2 | insufficient |
| `P21` | 3 | insufficient |
| `P12` | 3 | insufficient |
| `P11,P21` | 1 | sufficient |
| `P11,P12` | 1 | sufficient |
| `P21,P12` | 2 | insufficient |
| all three | 1 | sufficient but redundant |

Therefore:

`MINIMAL_CARDINALITY=2`.

The only inclusion-minimal sufficient packets are
`{P11,P21}` and `{P11,P12}`.

Moreover `P11` is necessary in every sufficient subpacket of the frozen grammar.

## 2. Invariance and pairability

`Gamma=C2 wr S3`: the within-pair `C2^3` swaps preserve
`h_i=a_i+b_i` and `t_i=a_i b_i`; `S3` simultaneously permutes the three pair labels.
Hence every frozen mixed sum is exactly `Gamma`-invariant.

An aligned state `(h,t)` comes from one unordered integer pair `{a,b}` iff
`Delta=h^2-4t` is a nonnegative perfect square and
`sqrt(Delta) congruent h (mod 2)`.
Thus recovery of `K=multiset{(h_i,t_i)}` is exactly recovery of the parent derived
pair packet modulo `Gamma`.

## 3. Sufficiency of `{P11,P21}`

If the three values of `H` are distinct, write `S_T=sum T`. For any ordering
`(h_i,h_j,h_k)`, Vandermonde/Lagrange elimination gives

`t_i=[P21-(h_j+h_k)P11+h_j h_k S_T]/[(h_i-h_j)(h_i-h_k)]`.

So all three products are reconstructed.

If `H={h,h,k}`, `k!=h`, then

`t_at_k=(P11-h S_T)/(k-h)`.

The remaining two products sit on equal `h` slots and their exchange does not change
`K`. Triple `H` is already aligned. Hence `{P11,P21}` is globally sufficient.

## 4. Sufficiency of `{P11,P12}`

Dually, with `S_H=sum H`, when `T` is distinct,

`h_i=[P12-(t_j+t_k)P11+t_j t_k S_H]/[(t_i-t_j)(t_i-t_k)]`.

If `T={t,t,u}`, `u!=t`, then

`h_at_u=(P11-t S_H)/(u-t)`.

The repeated-`t` exchange does not change `K`; triple `T` is already aligned.
Hence `{P11,P12}` is globally sufficient.

## 5. Exact obstruction witnesses

### `P11` alone

Fix `H={-4,-1,1}`, `T={-30,-12,0}`.

`K_A={(-4,-12),(-1,0),(1,-30)}`,
`K_B={(-4,0),(-1,-30),(1,-12)}`

are both pairable. Their local root pairs are respectively

`{-6,2},{-1,0},{-5,6}` and
`{-4,0},{-6,5},{-3,4}`.

Both have `P11=18`, but

`(P21,P12)(K_A)=(-222,324)`,
`(P21,P12)(K_B)=(-42,-756)`.

So `P11` alone is insufficient and the sharp residual fiber is at least two.

### `{P21,P12}` without `P11`

Fix `H={-5,0,5}`, `T={-6,-1,6}`.

`K_A={(-5,-6),(0,-1),(5,6)}`,
`K_B={(-5,6),(0,-1),(5,-6)}`

are pairable and satisfy

`P21(K_A)=P21(K_B)=0`,
`P12(K_A)=P12(K_B)=0`,

while

`P11(K_A)=60`, `P11(K_B)=-60`.

Therefore even the full packet omitting `P11` fails. This proves `P11` is necessary.

## 6. Sharp global fiber bounds

For `P11`, repeated `H` or repeated `T` strata are injective on the unique slot.
When both marginals are distinct, the six assignments form the strict `S3`
permutahedron; a linear level set contains at most two vertices. The witness above
attains two.

For `P21`, the assignment weights are `h_i^2`. Three distinct squares give the
same at-most-two permutahedron bound; a `2+1` square pattern leaves at most a
two-way swap; all three squares equal forces `H` to use only `a,-a`, so at most
three minority-slot choices remain. The sharp three-way witness is

`H={-5,-5,5}`, `T={-6,0,6}`,

with `P21=25 sum(T)=0` for all three pairable minority-slot choices.

The `P12` argument is dual. A sharp pairable three-way witness is

`H={-29,29,37}`, `T={-210,210,210}`,

for which every `h` pairs with both signs of `210`, and

`P12=210^2 sum(H)=1631700`

for all three choices of the unique `-210` slot.

For `{P21,P12}`, a three-way `P21` fiber can only arise when all `h_i^2` are equal.
With majority sign `a` and minority `-a`, the `P12` value for minority product `t_j`
is

`a sum_i t_i^2 - 2a t_j^2`.

Three distinct residual alignments would require three distinct products with equal
squares, impossible over the integers. Hence the joint fiber is at most two, and
the witness in Section 5 attains two.

The empty packet has the parent sharp six-way witness

`H={-3,3,9}`, `T={-70,-10,0}`,

for which all six matchings are pairable.

## 7. Frozen deterministic census

Before reading outcomes, freeze the local-root census to

`-6 <= a <= b <= 6`.

It contains exactly `91` distinct `(h=a+b,t=ab)` relation states and

`C(93,3)=129766`

three-state `K/Gamma` multisets. No adaptive enlargement was made.

The checker verifies all applicable reconstruction formulas and all eight subpackets.
It executes `1386781` assertions and returns

`PASS ... census_max=EMPTY:4,P11:2,P21:3,P12:2,P11_P21:1,P11_P12:1,P21_P12:2,ALL:1 global_max=EMPTY:6,P11:2,P21:3,P12:3,P11_P21:1,P11_P12:1,P21_P12:2,ALL:1 minimal=P11+P21|P11+P12`.

The global `EMPTY=6` and `P12=3` sharp witnesses are direct exact certificates
outside the fixed `B=6` box. Finite enumeration is regression/falsification evidence,
not the all-domain proof.

## 8. Pfaffian-orientation firewall

The parent oriented scalar is

`Q=t1-t2+t3=S_T-2*t_negative_slot`.

A `Gamma`-invariant mixed packet reconstructs `K/Gamma`; it does not choose the
distinguished negative slot. The residual oriented scalar candidate set is

`{S_T-2t : t in distinct(T)}`,

so it has exactly 1, 2, or 3 candidates according as `T` is triple, `2+1`, or
fully distinct. No native signed-carrier/orientation statement follows.

## 9. Prior-art boundary

The invariant-theory ingredients are classical, with no historical novelty claim:

- Francesco Vaccarino, *The ring of multisymmetric functions*, Ann. Inst. Fourier
  55(3) (2005), 717-731, DOI `10.5802/aif.2111`.
- David Rydh, *A minimal set of generators for the ring of multisymmetric functions*,
  Ann. Inst. Fourier 57(6) (2007), 1741-1769, DOI `10.5802/aif.2312`.
- Vandermonde/Lagrange interpolation and finite permutation-group invariant theory
  are standard.

Thus `P11,P21,P12` are standard polarized/multisymmetric mixed power sums. The
task-specific result is only the exact frozen-interface separator/fiber classification
after fixing the `H,T` marginals and integer-pairability gate.

## 10. Control boundary

Freeze:

`MINIMAL_MIXED_PACKET_FOUND`.

`MINIMAL_PACKETS={P11,P21} OR {P11,P12}`.

`P11_NECESSARY_WITHIN_FROZEN_GRAMMAR=TRUE`.

`ORIENTATION_FIREWALL_PRESERVED=TRUE`.

The Result is `RESULT_ONLY / NOT_INDEPENDENT / NONBLIND_DISCLOSED`. It grants no
Working Truth, Foundation, L4, native geometry, native orientation, factorization,
Full-Cell lift, or canonical promotion.

Next action: Driver review the immutable Result. The researcher lane makes no
downstream task decision.
