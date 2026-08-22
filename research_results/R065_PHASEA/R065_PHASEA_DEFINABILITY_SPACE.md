# R065 Phase A — Definability Space

Researcher-ID: `EM-R065A-7E6F46`

Mathematical input: `research_inputs/R065_PHASEA_BLIND_PRIMITIVE_PACKET_20260822.md@00765cc76ea71f789481fbe91c29d852bbf6b209`

## 1. Primitive groupoid

Let `C` be an abstract three-element component-type set.  The sector family is exactly the set of all two-element subsets of `C`, so its full automorphism group is `S3`; no type, sector, orientation, or ordered pair is distinguished.

A content is a function

`n : C -> N`

whose support has cardinality at most two.  Its token realization `U(n)` is a finite set equipped only with a type map `tau:U(n)->C`.  Token names are presentation data.

The Phase-A presentation groupoid has:
- objects: sector-supported typed finite contents;
- morphisms: a permutation `sigma in S3` together with bijections from each token fiber `tau^-1(c)` to the target fiber over `sigma(c)`.

The primitive partial composition is typed disjoint union / componentwise addition whenever the resulting support still has cardinality at most two.

## 2. Complete unlabeled invariant

Define

`Lambda(n) = sort(n1,n2,n3)`,

including zero entries.

### Orbit-classification theorem

Two contents `n,m` are isomorphic in the Phase-A presentation groupoid **iff**

`Lambda(n)=Lambda(m)`.

**Proof.**  
If an isomorphism exists, it permutes the three component types and bijects corresponding token fibers, hence preserves the multiset of the three fiber cardinalities.  Therefore the sorted triples agree.

Conversely, if the sorted triples agree, some permutation of the three components matches equal multiplicities.  Finite sets of equal cardinality admit bijections fiber by fiber, yielding a typed-token isomorphism.  ∎

Thus the unlabeled state space is exactly

`O = { (a,b,c) in N^3 : a<=b<=c and a=0 }`.

`Lambda` is a canonical, maximally informative **structural quotient** of the presentation data.  It is not yet a scalar magnitude.

### Scalar-factorization corollary

Every scalar-valued construction `F` that is invariant under token renaming and `S3` component relabeling factors uniquely through `Lambda`:

`F = f o Lambda`

for a function `f` on `O`.

This is a complete structural classification of where an intrinsic scalar may depend.  It does **not** select `f`.  The primitive packet supplies no valuation principle that chooses one orbit function over another.

## 3. Parameter-free finite constructions justified from the substrate

The theorem-relevant construction language generated without extra mathematical primitives is:

1. token equality and inequality;
2. component-type equality and inequality;
3. the derived equivalence relation
   `x ~type y iff tau(x)=tau(y)`;
4. the corresponding finite partition `Pi(n)` of `U(n)` into occupied type fibers;
5. the occupied support set and quotient `U(n)/~type`;
6. the multiset of fiber cardinalities, equivalently the positive part of `Lambda(n)`;
7. finite products, subsets, unions, intersections and complements defined using only the atomic equality/type predicates;
8. cardinality **after** a finite object has been specified;
9. the `S3`-orbit / unlabeled isomorphism class.

These operations are admissible because they are ordinary exact finite constructions on data already present in the blind packet.  None imports a metric, target formula, or preferred observation scale.

## 4. Smallest canonical relational objects

The type-equality relation `~type` is canonical because the primitive token typing is canonical up to relabeling.  Its unlabeled partition is invariant under every admissible presentation change.

From `Pi(n)` one canonically obtains:
- occupied-class count;
- unordered class-size multiset;
- finite sets of unordered two-token subsets lying in one class;
- finite sets of unordered two-token subsets meeting two distinct classes.

The underlying finite objects are more primitive than any numerical cardinality assigned to them.

## 5. Infinite scalarization envelope

Because `Lambda` is complete, **every** intrinsic scalar is an orbit function `f(Lambda)`.  Ordinary finite mathematics permits many parameter-free examples; therefore the definability space is not a single scalar but an envelope.

The task does not need to enumerate every syntactic orbit function.  Instead, completeness is obtained by:
- classifying the structural orbit `Lambda`;
- retaining a separating family of minimal intrinsic finite objects/readouts;
- proving that inequivalent scalarizations already survive all primitive symmetries.

This avoids both under-enumeration and an impossible attempt to list every finite-arithmetic expression.

## 6. What is not definable without extra datum

The primitive packet does not by itself distinguish:
- which derived finite object is the observation carrier;
- which valuation/cardinality law should be used;
- whether a composition law is required of the readout;
- any normalization beyond what one explicitly adds;
- the semantic role “magnitude”, “scale”, “distance”, “energy”, or similar.

Accordingly, canonicity of `Lambda` or `Pi` does not imply canonicity of a numerical or semantic readout.

**Gate:** `DEFINABILITY_SPACE_EXPLICIT = PASS`.
