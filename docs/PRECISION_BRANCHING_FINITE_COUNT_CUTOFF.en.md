# Finite Arithmetic Cutoff for Exact Count-Branching State

Status: `RESEARCH BRIDGE / NONCANONICAL`

A finite multivalued relation can generate arbitrarily long future words, yet the exact natural-number precision required to execute its **count-sensitive branching state** is uniformly finite.

The key resource is not path-count growth. It is the maximum number of raw one-step successors.

## 1. Maximum raw outdegree

For a finite labelled relation family define

`Delta = max_(action a, source x) |R_a(x)|`.

For any current quotient partition E and any target E-class C, the exact natural coefficient used by one weighted refinement step is

`n_(a,x,C)=#{y in C : x R_a y}`.

Always

`0 <= n_(a,x,C) <= Delta`.

This remains true no matter how many refinement rounds have already occurred.

## 2. Finite modular reflection theorem

Choose any modulus M satisfying

`M > Delta`.

Reduction modulo M is injective on the entire coefficient interval

`{0,1,...,Delta}`.

Therefore, on **every current partition**, two sources have the same exact-N target-block weight vector iff they have the same mod-M weight vector.

So one exact-N refinement step and one mod-M refinement step are identical.

Starting from the same initial observation partition, induction gives

`E_h^N = E_h^(mod M)`

for every refinement depth h.

Hence the stable infinite branching quotients are exactly equal as well.

## 3. Uniform exact cutoff

A canonical guaranteed modulus is therefore

`M_safe=max(2,Delta+1)`.

This modulus reproduces:

- every intermediate count-branching partition;
- the exact stabilization horizon in partition rounds;
- the final exact natural-count branching state quotient.

The cutoff is independent of:

- future word horizon;
- cycles in the raw relation;
- accumulated path-count magnitudes.

It depends only on one-step raw branching degree.

## 4. Worst-case sharpness

The condition `M>Delta` is optimal as a **uniform theorem over all relation systems with outdegree <=Delta**.

Fix any modulus

`2 <= M <= Delta`.

Construct two same-observation source states x,y such that:

- x has zero successors;
- y has exactly M distinct successors;
- all M successors currently lie in one behavioural class.

Exact-N refinement sees coefficients

`0` versus `M`

and splits x/y.

mod-M refinement sees

`0` versus `0`

and merges them.

If `Delta>M`, add an observation-isolated source with exactly Delta successors to make the world's actual maximum outdegree equal Delta without disturbing the x/y collision.

Thus no modulus `M<=Delta` can be a universal all-world cutoff at that outdegree budget.

## 5. Relation-specific modulus can be smaller

`Delta+1` is a uniform worst-case certificate, not always the least modulus for one fixed world.

A particular relation/observation pair may never realize a critical coefficient collision modulo a smaller M, or the current observation may already distinguish the affected states.

Because `Delta+1` is guaranteed to work, the least exact branching modulus for one finite system can be found by finite search over

`M=2,3,...,max(2,Delta+1)`.

The executable branch returns the first modulus whose **complete refinement sequence**, not merely final partition, agrees with exact N.

## 6. Why this does not contradict unbounded path counts

A count-branching state stores local multiplicities of successor behavioural types.

Even after many future rounds, one source/action still has only its original raw one-step successor set, so every coefficient remains at most Delta.

Terminal path-count traces are different. Along a word of length h, one path can branch again at every step. A crude universal bound is

`total paths <= Delta^h`.

Thus a simple coefficient-reflection modulus for **all exact terminal path counts through horizon h** is

`M > max(1,Delta^h)`.

That sufficient bound grows with h while the branching-state cutoff remains `Delta+1`.

This is a direct arithmetic manifestation of the distinction between compositional state and accumulated trace value.

## 7. Sharp fixed-world branching-versus-trace gap

Take `Delta=2`, so the exact branching cutoff is

`M_safe=3`.

Use one action a and constant observation.

Sources p,q both have two first-step successors.

For p:

- two children u1,u2;
- each child has two terminal successors.

For q:

- children v1,v0;
- v1 has one terminal successor;
- v0 has none.

Therefore the exact total path counts are

| word | p | q |
|---|---:|---:|
| empty | 1 | 1 |
| a | 2 | 2 |
| a^2 | 4 | 1 |
| a^k, k>=3 | 0 | 0 |

Exact terminal count traces split p/q at `a^2`.

Modulo3,

`4 == 1`,

so the entire modular terminal trace language merges p/q forever in this acyclic fixture.

But mod3 branching is exact: at depth one it distinguishes child behavioural types with outdegrees2,1,0; depth two then sees

- p -> two degree-2 child types;
- q -> one degree-1 plus one degree-0 child type.

Thus mod3 count-branching state equals exact N branching while mod3 terminal path-count trace remains strictly too coarse.

## 8. Finite-horizon terminal trace theorem

For any relation family with maximum outdegree Delta and any word horizon h, every terminal observation count lies in

`[0,max(1,Delta^h)]`.

Therefore every modulus

`M > max(1,Delta^h)`

reflects all exact natural terminal count coefficients through that horizon, and the complete exact-N and mod-M terminal trace partitions through h coincide.

This is a safe universal bound, not claimed minimal for a fixed relation.

## 9. State versus value arithmetic precision

The same raw finite world therefore supports two different arithmetic requirements.

### Exact compositional branching state

Needs only enough coefficient precision to distinguish local successor counts:

`M > Delta`.

### Exact accumulated terminal count values through h

A direct universal reflection bound scales as

`M > Delta^h`.

The first is horizon-independent because the state recursively stores structure.

The second flattens structure into a growing accumulated scalar/count vector.

So a richer structural state can require **less numeric magnitude precision** than a poorer aggregated trace representation.

## 10. Semantic-precision consequence

This is another non-scalar precision tradeoff:

- branching representation is structurally richer;
- yet it can be exact at a much smaller coefficient modulus;
- trace representation is structurally poorer;
- but exact trace values can require larger arithmetic range.

“More structure” and “more coefficient bits” are interchangeable resources only after the future interface is declared; neither globally dominates the other.

## 11. Prior-art boundary

Finite equitable partitions, modular injectivity, branching degree bounds and path-count growth are standard prior mathematics/computer science. A4 retains raw relation/witness ownership; P023/A2 retains future-signature precision ownership.

The project value is the exact resource separation:

> **finite count-branching state has a sharp horizon-independent coefficient cutoff `Delta+1`, even when exact terminal path-count values require precision growing with future horizon.**