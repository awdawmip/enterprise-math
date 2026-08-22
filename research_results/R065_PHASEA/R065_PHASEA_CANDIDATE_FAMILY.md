# R065 Phase A — Candidate Family

Researcher-ID: `EM-R065A-7E6F46`

Mathematical input: `research_inputs/R065_PHASEA_BLIND_PRIMITIVE_PACKET_20260822.md@00765cc76ea71f789481fbe91c29d852bbf6b209`

## 1. Structural envelope

By the orbit-classification theorem, the complete unlabeled state invariant is

`Lambda(n)=sort(n1,n2,n3)`.

Every presentation-independent scalar is an orbit function `f(Lambda)`.  Therefore the candidate family below is not an arbitrary shortlist: `Lambda` is the complete envelope, and the scalar witnesses are a minimal separating family proving nonuniqueness inside that envelope.

## 2. Retained candidates

| ID | Type | Construction | Free parameters | Symmetry | Semantic status |
|---|---|---|---|---|---|
| `R065A-C0-ORBIT` | multiset/orbit | `Lambda(n)=sort(n)` | none | `S3` invariant; token-renaming invariant | canonical structural quotient |
| `R065A-C1-PARTITION` | relation/quotient | `x~type y iff tau(x)=tau(y)` and occupied fibers | none | `S3` equivariant; unlabeled partition invariant | canonical derived relation |
| `R065A-C2-TOTAL` | scalar cardinal | `N(n)=|U(n)|=sum n_i` | none | invariant | numerical readout, no supplied magnitude role |
| `R065A-C3-SUPPORT` | scalar cardinal | `S(n)=|supp(n)|` | none | invariant | numerical readout |
| `R065A-C4-MAXBLOCK` | scalar cardinal | `M(n)=max_i n_i` | none | invariant | numerical readout |
| `R065A-C5-CROSS2` | scalar cardinal | cardinality of unordered 2-token subsets whose tokens have distinct types | none | invariant | numerical readout of a derived relation |
| `R065A-C6-SAME2` | scalar cardinal | cardinality of unordered 2-token subsets whose tokens have the same type | none | invariant | numerical readout of a derived relation |

For a two-supported content with active multiplicities `a,b`:
- `N=a+b`;
- `S` is `0,1,2` according to occupied support;
- `M=max(a,b)`;
- `CROSS2=ab`;
- `SAME2=binom(a,2)+binom(b,2)`.

The last two formulas are **derived cardinality identities**, not assumed quadratic laws.

## 3. Definability DAGs

`primitive typed tokens -> type equality -> Pi(n) -> class-size multiset -> Lambda(n)`

`U(n) -> finite cardinality -> TOTAL`

`Pi(n) -> quotient/occupied classes -> finite cardinality -> SUPPORT`

`Pi(n) -> class-size multiset -> maximum -> MAXBLOCK`

`U(n) + type inequality -> unordered 2-subsets crossing classes -> cardinality -> CROSS2`

`U(n) + type equality -> unordered 2-subsets inside classes -> cardinality -> SAME2`

No edge in these DAGs uses a target relation, metric, norm, hidden orientation, or preferred component.

## 4. Inequivalence witnesses

All retained scalar readouts are pairwise inequivalent on the tested finite domain.  Small witnesses include:
- `TOTAL != SUPPORT` at `(0,0,2)`: `2 != 1`;
- `TOTAL != MAXBLOCK` at `(0,1,1)`: `2 != 1`;
- `CROSS2 != SAME2` at `(0,0,2)`: `0 != 1`;
- `TOTAL != CROSS2` already at a unit state: `1 != 0`.

In particular, `TOTAL` and `MAXBLOCK` both satisfy:
- empty state -> `0`;
- every unit state -> `1`;
- token-renaming invariance;
- full `S3` invariance;
- componentwise monotonicity;

yet they differ at `(0,1,1)`.  Thus even these additional natural properties do not select a unique scalar.

## 5. Composition sensitivity

`TOTAL` is additive under every admissible typed disjoint union.

The orbit/partition candidates do not inherit a single-valued binary composition from separately unlabeled inputs: two unit-orbit inputs can be aligned to the same component or to two distinct components, producing different output orbits.  `SUPPORT`, `MAXBLOCK`, `CROSS2`, and `SAME2` likewise have composition behavior that depends on information not contained in their individual scalar values.

## 6. Candidate-family verdict

The blind substrate supports nontrivial canonical derived relations and several exact intrinsic scalar readouts.  It does **not** select one scalar readout as *the* finite magnitude/scale.

`SERIOUS_CANDIDATE_FAMILY_OR_EXACT_NO_GO_CLASSIFIED = PASS`.
