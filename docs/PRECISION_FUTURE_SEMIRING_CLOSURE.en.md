# Future-Language Closure as a Semimodule: Integer, Boolean, and Quotient Precision

Status: `RESEARCH BRIDGE / NONCANONICAL`

This note extracts one common algebraic skeleton from the integer future-observability work and the A4 relation-support work.  It is an architecture statement, not a claim that all world laws are linear or that one coefficient system is physically preferred.

## 1. Common closure formula

Fix a finite named state coordinate set and a coefficient semiring `R`.

Let total actions act linearly on column states by matrices `A_a`, and let declared linear observations be rows `C`.  A literal action word `w=a_1...a_t` contributes future rows

`C A_w = C A_(a_t) ... A_(a_1)`

under the chosen word convention.

Let

`L_h = span_R { C A_w : |w| <= h }`.

Then distributivity gives the exact recurrence

`L_(h+1) = L_h + sum_a L_h A_a`.

This is the common future-closure object.

The coefficient algebra determines what `span`, `+`, and reconstructibility mean; the recurrence itself does not.

## 2. Universal plateau certificate

For any semiring/module setting in which the expression above is defined, if

`L_(h+1)=L_h`,

then `L_h A_a subseteq L_h` for every declared action.  Therefore every longer product also preserves `L_h` and

`L_(h+t)=L_h`

for every `t>=0`.

So **one exact equal closure step is a permanent stop certificate**.

This does not imply that every coefficient semiring must reach such a plateau at a bounded horizon.  Finite stabilization requires additional algebraic structure.

## 3. Integer specialization: `R = Z`

For integer actions and observations, `L_h` is an embedded submodule of `Z^n`.

`Z^n` is Noetherian, so the ascending row-module chain stabilizes.  The current executable bridge gives more structure:

1. rational rank grows until the first rational plateau;
2. after rational rank stabilizes, the row lattice may still enlarge inside its saturated rational span;
3. every strict same-span enlargement decreases the saturation index to a proper divisor;
4. if rational stabilization occurs at horizon `h_Q` with index `I`, final integer closure is attained by

   `h_Q + Omega(I)`

   at the latest.

Hermite normal form stores the embedded row lattice without literal-word enumeration.  Smith/determinantal divisors describe abstract integer precision type:

`(hidden free rank ; Smith invariant factors)`.

They do not determine precision placement in named world coordinates.

## 4. Boolean specialization: `R = B = ({0,1}, OR, AND)`

For a finite relation `R_a`, use Boolean matrix

`A_a[target,source]=1 iff source R_a target`.

A target-observation class is an indicator row.  Then `C A_w` is exactly the predicate on initial states that some branch following word `w` can reach that observed class.

Here `span_B` is finite OR/join closure.  The ambient row set has only `2^n` elements, so the chain stabilizes for the simple reason that the Boolean semimodule is finite.

The unique finite join-irreducibles form the canonical minimal join-generating set of a closed Boolean row semimodule.  Propagating only those generators is sufficient because relation preimage distributes over OR.

This yields the exact backward dual of the A4 forward powerset compiler:

- forward support: Boolean column state `v -> A_a v`;
- backward future predicate: Boolean row `c -> c A_a`.

Literal relation words become an oracle rather than the primary execution path.

## 5. State distinction can finish before reconstructive closure

The future state partition and the full reconstructive semimodule are different precision levels.

### Integer case

The state kernel can already be zero while nonunit Smith factors remain.  Further future observations keep every state uniquely distinguishable but improve integer-coordinate reconstruction.

### Boolean case

A three-state relation example reaches the discrete raw-state partition at horizon one, yet its Boolean row semimodule still grows at horizon two by adding another support predicate.  The state partition is unchanged while OR-reconstructible support information increases.

Therefore the architecture should distinguish

`STATE-EQUALITY PRECISION`

from

`COEFFICIENT-SEMIMODULE RECONSTRUCTION PRECISION`.

The second is strictly stronger in general.

## 6. Coefficient homomorphisms induce precision quotients

Let `phi:R->S` be a semiring homomorphism and apply `phi` entrywise to the action/observation data.  Every S-valued future signature is the image under `phi` of the corresponding R-valued signature.

Hence equality in the finer R-signature implies equality in the S-signature.  Passing through a coefficient homomorphism can only preserve or merge future distinctions.

### Path counts -> path support

For nonnegative path-count semantics,

`phi:N->B`, `phi(n)=1[n>0]`

is a semiring homomorphism.

Natural-number matrix multiplication counts witness paths consistent with an action word.  Boolean multiplication remembers only whether at least one such path exists.

Therefore exact path-count precision refines reachable-support precision.

Sharp witness: one source has two relation branches into one observed class while another source has only one.  Both have the same Boolean observed support (`reachable`), while the count language returns `2` versus `1` after one action.

For equality analysis, the nonnegative count rows can be embedded into their `Z`-module envelope.  Integer combinations are an analysis/reconstruction device, not a claim that physical path counts can be negative.

### Exact integer -> modular precision

The ring quotient

`Z -> Z/MZ`

is another coefficient homomorphism.  Exact integer future equality therefore refines modulo-M equality.  This is the same mechanism behind modular collapse of some scheduler/history ambiguities.

## 7. Boolean predicate laws locate DOMAIN and RELATION defects

For raw relation `R`, existential backward predicate transformer

`T_R(P)={x : exists y in P, xRy}`

always preserves bottom and unions.

Two stronger laws diagnose different structural failures:

`T_R(X)=X`

iff every source has at least one successor — **DOMAIN / totality**.

`T_R(P intersect Q)=T_R(P) intersect T_R(Q)` for all P,Q

iff every source has at most one successor — **RELATION / functionality**.

Thus:

- partial deterministic action: meet-preserving, top-defective;
- total branching relation: top-preserving, meet-defective;
- total deterministic function: top- and meet-preserving Boolean-algebra homomorphism.

This places partial definedness and multivalued branching in one coefficient-level table without identifying them.

## 8. Semiring precision is still not literal operation capability

A smaller action family can generate the same state kernel or the same coefficient semimodule while omitting a named operation.

That proves observation-precision redundancy, not operational equivalence.  Literal action availability, provenance, guards, costs, timing, or actuator meaning are stronger DOMAIN/capability semantics.

Likewise, Boolean support forgets path multiplicity, and natural-number counts forget literal path identity once paths are aggregated to the same count.  If the future language reads those richer witnesses, a richer coefficient/object space is required.

## 9. Architecture summary

The common compiler pattern is

`declared actions + declared observations`

`-> coefficient-semimodule future closure L_h`

`-> state equality kernel + reconstructive coefficient state`.

But termination/refinement mechanisms remain coefficient-specific:

- `Z`: rational rank + lattice saturation / Smith purification;
- `B`: finite join-semilattice growth / join-irreducibles;
- other semirings: require their own finite-generation or termination theorem.

No generic finite-horizon theorem should be inferred merely from the shared recurrence.

All semiring/module, Boolean matrix, automata, Smith/Hermite, predicate-transformer, and path-count facts used here are standard prior mathematics/CS.  The Enterprise Math value is the precision-first routing: choose the coefficient semantics that matches the declared future question, then retain exactly the closure that question can reactivate.