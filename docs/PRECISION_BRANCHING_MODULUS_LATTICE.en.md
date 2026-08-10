# Modular Branching Precision and the GCD/LCM Lattice

Status: `RESEARCH BRIDGE / NONCANONICAL`

The ordinary modular precision lattice survives inside relation branching semantics, but its join must be interpreted together with the structural operation interface.

For terminal count traces, lcm is already the independent readout join. For branching operations, lcm is the **coupled compositional join** and can require additional state refinement beyond the independent modular readout join.

## 1. Divisibility remains the coefficient precision order

If

`M | N`,

reduction

`Z/NZ -> Z/MZ`

is a semiring homomorphism.

By the branching semiring-morphism theorem, mod-N branching signatures recursively project to mod-M branching signatures.

Therefore at every horizon:

`mod-N branching precision`

refines

`mod-M branching precision`.

So numerical modulus size is still not the order; divisibility is.

## 2. GCD is the common modular coefficient coarsening

For moduli M,N, let

`G=gcd(M,N)`.

When `G>1`, both coefficient semirings reduce to `Z/GZ`, so both branching partitions refine the mod-G branching partition.

When `G=1`, the formal common coefficient quotient is the trivial mod-1 coefficient world: every multiplicity is zero. The executable layer leaves this as a formal bottom rather than constructing a zero-ring branching semiring.

Thus gcd remains the modular coefficient meet/coarsening direction.

## 3. LCM embeds into the coefficient product

Let

`L=lcm(M,N)`.

The residue map

`iota: Z/LZ -> Z/MZ x Z/NZ`

`r |-> (r mod M, r mod N)`

is a semiring homomorphism.

It is injective: two residues with the same M- and N-reductions differ by a multiple of both M and N, hence by a multiple of L.

Its image is the compatible residue-pair subring; for coprime M,N this is the full CRT product.

Because the morphism is injective, the recursive signature map is injective at every branching depth. Therefore:

`mod-L branching partition`

`=`

`(mod-M x mod-N) product-semiring branching partition`.

## 4. LCM is the coupled compositional join

The compositional-interface theorem says product-semiring refinement is exactly the coarsest shared-state quotient on which both coefficient interfaces remain directly executable.

Combining with the injective LCM map gives:

`E_comp(M,N)=E_LCM(M,N)`.

So the branching analogue of arithmetic join is:

> **mod-lcm is the unique coarsest shared quotient state on which mod-M and mod-N weighted relation interfaces can continue to compose together.**

This extends the static modular lattice into a branching operation language.

## 5. Independent branching readout join can be strictly coarser

Compute the individually stable mod-M and mod-N quotients and intersect their state kernels.

This readout join is enough to recover the two final modular branching labels separately.

It need not remain stable for either transition interface after target blocks are jointly split.

Therefore:

`independent modular branching join`

can be strictly coarser than

`mod-lcm coupled branching join`.

The gap is exactly the compositional closure debt from the parent generation.

## 6. Sharp CRT witness for mod2 and mod3

Use ten states

`p,q,A,B,C,D,z1,z2,z3,z4`

with constant observation.

Action b gives the four middle states successor counts:

- A: 0;
- B: 4;
- C: 3;
- D: 1.

Their coefficient types are therefore:

| state | mod2 | mod3 | mod6 |
|---|---:|---:|---:|
| A | 0 | 0 | 0 |
| B | 0 | 1 | 4 |
| C | 1 | 0 | 3 |
| D | 1 | 1 | 1 |

Action a chooses

`p -> {A,D}`

and

`q -> {B,C}`.

### Separate mod2 view

Both p and q see one parity-zero child type and one parity-one child type.

### Separate mod3 view

Both p and q see one residue-zero child type and one residue-one child type.

Hence the stable mod2 and mod3 branching interfaces both merge p/q, and so does their independent state readout join.

### Mod6 / coupled view

mod6 remembers the paired residue types:

p reaches types `{0,1}`,

q reaches types `{4,3}`.

Therefore mod6 branching separates p/q.

This is the CRT form of cross-capability successor correlation.

## 7. Terminal modular count traces behave differently

For one terminal path-count entry n:

knowing

`n mod M`

and

`n mod N`

is exactly equivalent to knowing

`n mod L`.

Terminal word traces are just finite arrays of such coefficients indexed by word and observation label.

Therefore their state partitions obey the exact readout law:

`Trace_L = Trace_M join Trace_N`.

No additional branch-correlation closure is required because terminal trace semantics has already summed away successor grouping.

This is true even on the ten-state witness where branching operations have positive compositional debt.

## 8. Same arithmetic lcm, two semantic roles

The formula

`join = lcm`

is therefore semantically overloaded.

### Terminal count-trace interface

LCM is the ordinary independent readout join.

### Branching weighted-operation interface

LCM is the coupled compositional join after restoring shared successor-state consistency.

The arithmetic object is the same; the state precision required to realize it can differ because the structural future language differs.

## 9. Coprime CRT is the cleanest strict example

For M=2,N=3:

`Z/6Z ~= Z/2Z x Z/3Z`.

There is no coefficient redundancy at all in the product.

Yet the independent **state** join of the two stable branching interfaces can still be coarser than mod6 branching, because it forgets which mod2 child behaviour and mod3 child behaviour belong to the same successor type.

Thus the compositional debt is not caused by a bad coefficient representation. It is caused by structural pairing across successor branches.

## 10. Relation to earlier modular precision work

Earlier integer-action work established:

- divisibility as the modular precision order;
- `meet=gcd`, `join=lcm`;
- CRT decomposition of independent prime-power arithmetic precision.

The current relation result preserves those coefficient laws but adds one new structural distinction:

> **arithmetic CRT components are independent at the coefficient level, yet a branching future can require correlation between those components on the same successor state.**

This is exactly what terminal trace semantics erases and shared relation execution preserves.

## 11. Compiler consequence

For modular branching tasks:

1. reduce dominated moduli using divisibility;
2. if only terminal modular count traces are needed, combine remaining moduli by lcm directly;
3. if the weighted relation must execute on one shared quotient state space, use mod-lcm branching closure;
4. compare against the independent readout join to expose any compositional debt.

Thus arithmetic compression and structural closure are separate compiler stages.

## 12. Prior-art boundary

CRT, gcd/lcm divisibility lattices, modular semirings, weighted bisimulation and trace semantics are standard prior mathematics/computer science. A4 retains relation/witness ownership; P023/A2 retains declared future-signature and precision ownership.

The project value is the exact cross-layer theorem:

> **mod-lcm is simultaneously the coefficient join and the coupled branching-operation join, while terminal traces realize the same lcm as a simpler independent readout join.**