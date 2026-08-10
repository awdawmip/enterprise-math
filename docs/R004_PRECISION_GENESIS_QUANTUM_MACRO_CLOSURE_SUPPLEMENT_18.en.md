# R004 precision genesis — Supplement 18: arithmetic cut compiler from dissociated weight supports

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + STRUCTURAL_CUT_CLOSED_FORM`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_17.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 16-17 moved the obstruction problem from Bell-number state partitions to a generator-side cut clutter, but generic extraction still allowed up to `2^|G|` retained-generator compiler calls. This supplement gives the first arithmetic family in which the carrier-cut clutter is obtained directly from integer relations among typed generator coordinates.

The additive-combinatorics notion of a dissociated / subset-sum-distinct set is prior art. R004's project-local result is the exact identification of future-language carrier cuts with support-minimal failures of dissociativity in the weighted-observation/bit-flip compiler below.

## 1. Binary weighted-observation world

Let

`X={0,1}^d`.

Choose nonzero integer weights

`a=(a_1,...,a_d)`

and current observable

`L_a(x)=sum_i a_i x_i`.

Let `P0=ker L_a` be the current observation partition.

For each coordinate `i`, declare a total future generator `F_i` that flips that bit:

`(F_i x)_i = 1-x_i`,

with all other coordinates fixed.

Let `G={F_1,...,F_d}`.

## 2. R004-COMP-T32 — exact retained-flip quotient

For retained coordinate set `S subseteq {1,...,d}`, define

`q_S(x)=(L_a(x), x|_S)`.

Then `q_S` is exactly the coarsest future-safe quotient for the retained flip language.

Proof of sufficiency. If two states have equal weighted observation and equal retained bits, any word in retained flips changes exactly the same retained coordinates from the same starting bit values. Hence every future weighted observation remains equal.

Proof of necessity. For retained `i`,

`L_a(F_i x)-L_a(x)=a_i(1-2x_i)`.

Because `a_i != 0`, the pair of current/future observations determines `x_i` exactly. Therefore any safe quotient must preserve every retained bit as well as `L_a(x)`.

Thus

`Compile_S(P0)=ker q_S`.

This is a closed-form compiler output, not an iterative partition-refinement claim.

## 3. R004-COMP-T33 — deletion failure equals subset-sum collision

Let `H=G\S` be the deleted/hidden coordinate set.

Since `x|_S` is known, injectivity of `q_S` reduces exactly to injectivity of the hidden subset-sum map

`z in {0,1}^H -> sum_(i in H) a_i z_i`.

Therefore deleting `H` breaks the full discrete carrier iff there exist distinct hidden binary vectors `u != v` with

`sum_(i in H) a_i u_i = sum_(i in H) a_i v_i`.

Subtracting gives a nonzero signed relation

`sum_(i in H) epsilon_i a_i = 0`,

where every

`epsilon_i in {-1,0,1}`.

Conversely every such signed relation splits its positive and negative supports into two different hidden subsets with equal sum, producing a carrier collision.

So:

`H is carrier-breaking <=> {a_i : i in H} is not subset-sum-distinct / dissociated`.

## 4. R004-COMP-T34 — arithmetic carrier-cut theorem

The minimal carrier cuts of this future language are exactly

`C_car = { support-minimal nonzero epsilon in {-1,0,1}^d : sum_i epsilon_i a_i = 0 }`,

where each cut edge is the support

`{i : epsilon_i != 0}`.

Equivalently:

`minimal carrier cuts = inclusion-minimal non-dissociated weight supports`.

Thus the structural obstruction clutter is derived directly from arithmetic dependencies among the weights. No retained-subset compiler calls are needed once these minimal signed dependencies are known.

This is the first R004 example of the Supplement-17 frontier

`typed algebraic invariant -> exact cut clutter`.

## 5. Equal-weight closed form

If all weights are equal and nonzero,

`a_i=c`,

then every two-coordinate set `{i,j}` has relation

`a_i-a_j=0`,

and no singleton is dependent.

Therefore

`C_car = all 2-subsets of [d]`.

The cut clutter is the edge set of the complete graph `K_d`.

Its minimal transversals are exactly the complements of one coordinate:

`B_C = { [d]\{i} : i in [d] }`.

Hence every minimal Carrier Basis has size

`d-1`.

Interpretation: the total-count observation `sum_i x_i` supplies one global relation among the coordinate bits; any `d-1` coordinate flips reveal the final hidden bit from the total.

The two-bit coupled-observation example from the earlier product-factorization boundary is the `d=2` specialization: the unique minimal cut is `{F_1,F_2}`, so either local flip alone suffices even though the observation couples the two axes.

## 6. Powers-of-two closed form

If

`a_i=2^(i-1)`,

all binary subset sums are distinct. The weight family is dissociated and `L_a` itself is injective on `{0,1}^d`.

Therefore

`C_car=empty`,

and the minimal Carrier Basis is the empty instruction set.

This does not say the future flip operations are semantically reconstructible from nothing. It says only that they are unnecessary for **carrier generation** because the current observation has already encoded the exact state. Supplement 17's semantic adequacy layer remains separate.

## 7. Intermediate arithmetic example

For weights

`a=(1,2,3)`,

the only inclusion-minimal subset-sum collision is

`1+2=3`.

Hence

`C_car={{1,2,3}}`.

Every one-coordinate retained flip is therefore a minimal Carrier Basis: revealing any one bit leaves two hidden weights whose subset sums are distinct.

This differs sharply from equal weights `(1,1,1)`, where all three two-coordinate cuts occur and every Carrier Basis has size two.

So the instruction complexity is controlled by the arithmetic dependency structure of the observation weights, not by dimension alone.

## 8. Exact validation

Independent validation covered every positive weight vector

`a_i in {1,2,3,4,5}`

for dimensions `1<=d<=4`, a total of **780** weight systems.

For every system:

1. the full flip language compiled to the discrete partition;
2. compiler-derived minimal deletion cuts matched the inclusion-minimal non-dissociated supports exactly.

No violations were found.

A stronger all-retained-subset check compared the iterative compiler output against the closed form

`ker(x -> (L_a(x),x|_S))`

for every retained `S` in the same family: **11,110** quotient cases, zero mismatches.

The executable arithmetic reference is

`src/enterprise_math/precision_arithmetic_cut_compiler.py`

with direct regressions in

`tests/test_precision_arithmetic_cut_compiler.py`.

No fresh full-repository CI or canonical-main status is claimed.

## 9. Prior-art boundary

Subset-sum-distinct / dissociated sets, and the equivalent absence of nontrivial `{-1,0,1}` relations, are established additive-combinatorics notions. The source map is recorded in

`docs/PRIOR_ART_R004_ARITHMETIC_CUT_COMPILER.*`

and

`sources_r004_arithmetic_cut_compiler.json`.

R004 does not claim dissociated-set theory or subset-sum uniqueness as inventions.

The project-local theorem is the compiler bridge:

`weighted observation + coordinate flips -> retained quotient (L_a,x|_S) -> carrier cuts = minimal non-dissociated supports`.

Historical novelty of this exact Enterprise Math specialization remains `NOVELTY_UNVERIFIED`.

## 10. Architectural consequence

The obstruction compiler now has two modes:

Generic:

`typed compiler oracle -> minimal deletion cuts -> transversal basis`.

Arithmetic closed form:

`typed integer weights -> support-minimal signed relations -> cut clutter -> transversal basis`.

This is the first proof that `C_joint/C_car` can sometimes be generated from an algebraic invariant without enumerating all retained generator subsets.

## 11. Next frontier

The natural next question is to identify other typed families whose cut clutters admit algebraic closed forms:

- quotient-module generators -> support-minimal module relations / invariant-factor defects;
- A3 determinant/exterior relation state -> minimal rank-loss supports;
- guard-image lattices -> minimal generator deletions that lower reachable guard-image rank or orthant support;
- prime-axis/exponent languages -> minimal support deletions that destroy required arithmetic axes.

The aim is not a universal new combinatorial algorithm. It is an atlas of exact algebraic cut compilers specialized to Enterprise Math's typed future-language families.
