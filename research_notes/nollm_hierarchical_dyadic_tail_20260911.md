# Hierarchical dyadic tail: exact identity without the flat-annulus radius explosion

Status: `RESEARCH_NOTE / EXACT_DECLARED_HIERARCHICAL_CARRIER + EXHAUSTIVE_FINITE_BASE-Q40_OBSERVER / NOT_FOUNDATION / NOT_NOLLM_RUNTIME`

Date: 2026-09-11  
Research activity: `RA-nollm-multiplication-field-20260911-c6c82`

## 1. Question

The flat dyadic annulus has excellent generator locality, but identity injectivity over `1<=n<2^L` requires `b=L-2`, making its ring radius `Theta(2^L)=Theta(N)`. Can the exact higher unit-log bits be removed from that flat geometry while keeping multiplication locally editable?

This note answers **yes at the typed product-carrier level**, not yet at the single-entry Nollm physical-placement level.

## 2. BRC gate

Population: positive integers `1<=n<2^L`.  
Canonical identity: complete integer `n`.  
Exact source carrier: `n=2^v u`, `u=(-1)^eps 5^t mod 2^(B+2)`.  
Serial composition: multiplication.  
Base observer: the integer A2 annulus at fixed low precision `b`.  
Repair coordinate: an explicit finite dyadic tail; it is **not discarded or merged into the base cell**.  
Future operations: x5, x2, sign flip, Q40 Coverage on the base observer, eventual geometry-native tail realization.

`COMPOSE_APPLIED`: reuse the exact dyadic unit-log carrier and the annulus theorem. The new step is an information-preserving split between a low geometric prefix and an explicit high-bit repair coordinate.

## 3. Exact hierarchical state

Fix a bounded population `1<=n<2^L` and a base precision `b>=3`. Write `n=2^v u` with `u` odd. Let

`B_v = max(b, L-v-2)`, `d_v=B_v-b=max(L-v-2-b,0)`.

At precision `B_v`, write

`u=(-1)^eps 5^t (mod 2^(B_v+2))`, `0<=t<2^B_v`.

Split

`t = t0 + 2^b q`, with `0<=t0<2^b`, `0<=q<2^d`.

Store the tail using the binary-reflected Gray code

`g(q)=q xor (q>>1)`

on exactly `d` bits. The base geometry is the previously proved integer annulus cell

`E_b(v,eps,t0)`.

The hierarchical state is

`H_(L,b)(n) = (E_b(v,eps,t0), d, g(q))`.

### Injectivity

The annulus cell recovers `(h,t0)` with `h=2v+eps`; hence it recovers `(v,eps,t0)`. Gray decoding recovers `q`, so `t=t0+2^b q`. Finally

`2^(B_v+2) >= 2^(L-v) > u`,

so the residue `(-1)^eps 5^t mod 2^(B_v+2)` is the actual positive odd integer `u`, not only its congruence class. Thus the state reconstructs `n` exactly.

For `L=16,b=8`, exhaustive reconstruction covers all 65,535 positive integers with zero collision.

## 4. Exact local generator updates

### Multiplication by 5

For every valid pair `5n<2^L`, `v,eps,B,d` stay fixed and

`t' = t+1 mod 2^B`.

Therefore `t0` increments modulo `2^b`; `q` changes only when the low part wraps. Binary-reflected Gray code is a cyclic Hamiltonian cycle, so `q->q+1 mod 2^d` toggles exactly one tail bit. Hence:

- base A2 movement: at most two cells by the annulus theorem;
- tail update: zero bits normally, exactly one bit on a low-part carry when `d>0`.

At `L=16,b=8`, all 13,107 valid x5 pairs give:

- base distance 1: 12,243; distance 2: 864;
- tail Hamming 0: 13,056; Hamming 1: 51.

Exactly 51 pairs cross the low `t0=255` boundary.

### Multiplication by 2

For `2n<2^L`, `v' = v+1`, the odd unit is unchanged, and

`d' = max(d-1,0)`, `q' = q mod 2^d'`, `t0'=t0`.

The base annulus moves from `h=2v+eps` to `h+2`, exactly two A2 cells in the declared b=8 range. When the top tail level is removed, all retained Gray bits agree except possibly the new top retained bit, because `g_i=q_i xor q_(i+1)`. Hence the retained tail Hamming change is at most one.

All 32,767 valid x2 pairs give:

- base distance 2: 32,767;
- retained-tail Hamming 0: 16,895;
- retained-tail Hamming 1: 15,872.

### Sign sheet

Abstractly, multiplying the odd unit by `-1` only toggles `eps`, so the annulus ring index `h` changes by one, the base cell moves one A2 step, and the tail is unchanged. This is a carrier statement; the finite population in this note contains positive integers only.

## 5. Tail-size law

Let `D=L-b-2>=1`. The exact population by tail depth is

- depth 0: `2^(b+2)-1` integers;
- depth `j>=1`: `2^(b+j+1)` integers, for `1<=j<=D`.

Therefore the total number of stored tail bits across all positive integers is

`T(L,b) = (D-1)2^L + 2^(b+2)`,

and the average is `T/(2^L-1)`.

For `L=16,b=8`:

- depth histogram: `{0:1023,1:1024,2:2048,3:4096,4:8192,5:16384,6:32768}`;
- maximum tail depth: 6;
- total tail bits: 328,704;
- average tail depth: `5.0157015335`.

The base annulus has `M=256`, `R0=43`; using the same conservative signed `h<=31` observer, the outer base radius is 74. If the tail is discarded, only 4,095 base cells remain and the largest identity fiber has 64 members. With the tail retained, all 65,535 identities are reconstructed.

This should be compared carefully with the flat injective `b=14` annulus outer radius 2,762. **The hierarchical tail is still an auxiliary typed coordinate, so radius 74 is only the base-observer footprint, not yet a complete single-entry physical-placement radius.**

## 6. Actual Q40 Coverage on the b=8 base observer

The same published Nollm Q40 constants/rounding used in the previous annulus checkpoint were run exhaustively on the b=8 base cells. The tail is retained as identity metadata for this experiment but is not fed into Q40 geometry.

| direction / generator | one-step overlap | one-step max Hausdorff | two-step overlap | two-step max Hausdorff |
|---|---:|---:|---:|---:|
| up / x2 | 26.9814% | 3 | **100%** | 3 |
| up / x5 | 94.4228% | 3 | **100%** | 3 |
| down / x2 | 5.2644% | 3 | **92.9899%** | 4 |
| down / x5 | 93.4081% | 3 | **98.9014%** | 4 |

All x2 rows use 32,767 valid pairs and all x5 rows use the corrected 13,107 valid pairs. Thus lowering the base precision from b=11/14 to b=8 does not destroy the finite constant-radius Q40 support relation, though the x5 overlap is weaker than at higher base precision. This is finite geometry evidence, not semantic recall evidence or a uniform theorem.

## 7. What is solved and what is not

Solved exactly in the declared hierarchical carrier:

1. complete bounded integer identity;
2. base x5 move <=2 cells with at most one tail-bit toggle;
3. base x2 move exactly 2 cells, one tail-level deletion when present, and at most one retained tail-bit toggle;
4. sign sheet move one base cell with no tail change;
5. explicit tail-depth/storage formulas.

Measured exhaustively:

- published-Q40 one/two-step support locality of the b=8 base observer over all valid x2/x5 pairs below 65,536.

Still open:

- the Gray tail is not yet a Nollm **single physical entry**. Treating it as hidden lookup state would violate the geometry-native design goal;
- no layout is yet supplied that embeds the tail bits into actual adjacent Nollm layers/cells while retaining the exact local-update laws;
- semantic memory quality is unmeasured;
- no infinite-scale packing theorem follows.

## 8. Next exact unit

The most promising geometry-native continuation is a two-layer-per-tail-bit refinement. Nollm's adjacent-layer area/density ratio is `sqrt(2)`, so two adjacent intervals provide a factor-2 cell-capacity change—the exact information capacity of one binary refinement bit. For a maximum tail depth `D`, `2D` adjacent intervals provide capacity factor `2^D`.

This is presently a **capacity compatibility**, not a placement theorem. The next experiment should construct a matching from each parent state to one/two distinct descendants inside its real two-step Q40 support and test Hall/perfect-matching feasibility level by level. Success would turn the explicit repair coordinate into an actual one-entry hierarchical geometry; failure would identify the precise local-capacity obstruction.
