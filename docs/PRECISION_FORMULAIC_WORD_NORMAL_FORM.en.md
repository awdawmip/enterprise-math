# Formulaic Word Algebra versus Tabulated Semantic Monoid

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The finite transformation-monoid theorem compresses literal words to semantic effects, but a generic implementation still stores an `m x m` Cayley table and an `m x n` effect-action table.

Those tables are not fundamental lower bounds. A large exact monoid can admit a very small **formulaic presentation** whose multiplication and state action are computed directly.

A commuting-idempotent bitmask family gives a sharp executable witness.

## 1. Commuting idempotent generators

Take k generators and k-bit mask states

`X={0,...,2^k-1}`.

Generator i acts by

`x -> x OR 2^i`.

Each generator is idempotent and all generators commute.

## 2. Exact literal-word normal form

For a word w, define

`nu(w)=OR of all one-hot generator bits appearing in w`.

Then the induced transformation is exactly

`x -> x OR nu(w)`.

Hence:

`nu(uv)=nu(u) OR nu(v)`.

The normal form is independent of action order and repeated generators disappear automatically.

## 3. Exact semantic monoid size

Every mask occurs as the normal form of a word using precisely that subset of generators.

Therefore the generated transformation monoid has exactly

`m=2^k`

elements.

The state set also has

`n=2^k`.

This is not a “small monoid” example. The semantic effect family itself is exponentially large in the generator count.

## 4. Generic table cost is 4^k

A generic finite-monoid implementation would store:

- Cayley multiplication table: `m^2=4^k` effect-ID entries;
- effect action table on fine states: `m*n=4^k` state-ID entries.

So both generic semantic tables grow exponentially faster than the k-bit parameterization of one effect.

## 5. Formulaic representation removes both tables

Represent state and effect by k-bit masks.

Then:

- normal-form multiplication is bitwise OR;
- applying an effect to a state is the same bitwise OR;
- generator metadata is only the mapping from k action names to k bit positions.

No Cayley table and no effect-action table are required.

Thus the exact `2^k`-element monoid is represented by one k-bit data type plus one closed operation law.

## 6. Information-optimal effect representation

There are exactly `2^k` semantic effects, so any injective fixed-length binary effect ID needs at least k bits.

The mask normal form uses exactly k bits.

Hence the per-effect representation is information-theoretically optimal while remaining directly compositional.

The huge gap lies not in effect identity but in whether the multiplication/action law is tabulated or formulaic.

## 7. Horizon-dependent reachable effect count

Through word horizon H, a nonidentity effect is reachable exactly when its support subset has size at most H.

Therefore

`N_nonid(k,H)=sum_(j=1)^min(k,H) C(k,j)`.

Including identity:

`N(k,H)=1+N_nonid(k,H)`.

Once `H>=k`, all `2^k` semantic effects have appeared and effect count saturates permanently, while literal word count continues to grow as `sum k^i`.

## 8. Parallel formulaic normalization

A length-H word gives H one-hot masks. Reduce them by a balanced OR tree.

Normalization depth:

`ceil(log2 H)`.

Apply the resulting mask to the state in one further OR round.

Total depth:

`ceil(log2 H)+1`.

This exactly matches the depth of a generic full-Cayley parallel normalizer while eliminating the `4^k` Cayley storage.

## 9. Bit-level work law

A balanced reduction uses H-1 word-level OR gates.

Treating one k-bit OR as k independent bit operations:

`normalization bit work = k*(H-1)`.

State application costs another k bit ORs, so

`total bit work = k*H`.

Thus the formulaic representation exchanges table memory for runtime circuit work:

- algebra storage: O(k) schema/metadata plus k-bit values;
- total work: O(kH);
- parallel depth: O(log H).

## 10. Sharp k=5, H=20 resource comparison

Take k=5.

Then:

`n=m=32`.

Generic semantic tables:

- Cayley cells:1024;
- effect-action cells:1024.

Literal word index through H=20 contains

`sum_(i=1)^20 5^i`

entries, far above `10^10`.

Formulaic route:

- normal form width:5 bits;
- generator metadata:5 positions;
- parallel normalization depth:5;
- total normalization+application depth:6;
- total bit work:100 primitive bit ORs.

The same exact law has representations whose storage differs by orders of magnitude without changing semantic precision.

## 11. Formulaic complexity is independent from monoid cardinality

The example proves:

`large exact operation set`

does not imply

`large operation-law table`.

Monoid cardinality measures how many semantic operations exist. Formula/presentation complexity measures how hard it is to represent their composition and action.

These are different precision resources.

## 12. Table complexity versus presentation complexity

The current representation ladder therefore has another axis:

### Tabulated algebra

Store arbitrary operation products explicitly. Cost scales with the number of semantic elements.

### Formulaic algebra

Store parameters plus a closed composition formula. Cost can scale with parameter dimension rather than monoid cardinality.

The correct resource question is not only

`how many exact operations exist?`

but also

`what is the smallest exact compositional presentation of those operations?`

## 13. Relationship to P024

P024's guarded translation profile `(T,H)` already demonstrates the same architectural phenomenon in an infinite parameterized monoid: a closed max-plus-style product represents exact guarded word semantics without enumerating all literal words or all operation elements.

The bitmask example supplies a finite, fully executable sharp witness where the table-vs-formula storage gap is exponential and easy to count exactly.

## 14. Stage131 consequence

Stage131's resource axis now has at least three distinct layers:

1. literal consequence caching — precompute words/rules versus runtime composition;
2. semantic quotienting — merge literal words with equal exact operation;
3. algebra presentation — tabulate semantic multiplication versus compute it by a compact formula/circuit.

Each layer can change storage and execution depth while preserving the same exact future law.

Therefore “rule count” alone is not a sufficient complexity measure for relation-law precision.

## 15. Scope boundary

This owner exploits a special commuting-idempotent semilattice law. It does not claim every finite monoid admits a comparably compact formulaic presentation.

Finding or proving lower bounds on the smallest exact algebraic/circuit presentation is a different complexity problem. The generic Cayley table remains a universal fallback when no smaller law is known.

## Owner-local assets

- `src/enterprise_math/formulaic_idempotent_word_normal_form.py`;
- `src/enterprise_math/formulaic_normal_form_work_depth.py`;
- corresponding tests;
- this bilingual theorem note.

## Prior art / status

Semilattices, commuting idempotents, bitmask normal forms and circuit work/depth are standard prior algebra/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the explicit formulaic-versus-tabulated future-law representation specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
