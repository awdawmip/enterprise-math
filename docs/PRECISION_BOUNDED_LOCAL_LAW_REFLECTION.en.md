# Bounded Local-Law Reflection before Unbounded Composition

Status: `RESEARCH BRIDGE / NONCANONICAL`

The structure-first path-count generation reveals a more general principle. A finite-precision observation does not need to represent every large value that can appear after many future compositions. It only needs to reflect the **bounded local law** from which those future values are deterministically generated.

This note develops that principle for finite integer-weighted transition systems and then separates its task-generic content from the weighted-relation specialization.

## 1. Primitive weighted local law

Let X be a finite state set. Each named action carries a finite integer-weighted relation

`w_a(x,y) in Z`,

with omitted edges interpreted as weight zero.

For a current target partition E and source x, the local coefficient sent to target block C is

`A_a^E(x,C)=sum_(y in C) w_a(x,y)`.

Weighted transition stability requires equivalent sources to have the same vector of these exact local aggregates for every action and target block.

## 2. The local aggregate alphabet is finite

Fix one source/action. A target partition block intersects its finite outgoing edge set in some subset. Therefore every possible block aggregate is a subset sum of the outgoing primitive weights.

Taking the union over all sources/actions gives a finite alphabet

`L_local subset Z`.

Every coefficient ever inspected by the weighted partition-refinement step belongs to this finite set, regardless of future horizon.

For a world class with primitive weights W and at most Delta outgoing edges per source/action, a safe universal alphabet is

`L(W,Delta)={sum of at most Delta elements of W}`,

where repeated primitive values are allowed because distinct edges may carry the same weight.

## 3. Generic finite-code theorem

Let

`c:L_local -> C`

be any hashable code.

If c is injective on `L_local`, then replacing every exact local aggregate by its code produces exactly the same partition-refinement step on every current partition. By induction the complete refinement sequence and stable state quotient are identical to the exact-integer world.

Crucially, C need not be a semiring. It may be an arbitrary finite label set.

The only requirement for **reflection-before-compose** is local injectivity plus a decoder on the finite alphabet.

## 4. Modular quotient is one specialization

For

`c_M(z)=z mod M`,

mod-M is exact for the whole weighted refinement whenever it is injective on `L_local`.

A simple sufficient bound is

`M > max(L_local)-min(L_local)`.

Then two distinct local values cannot differ by a nonzero multiple of M.

The branch also searches the least reflective modulus for one finite alphabet. It may be much smaller than the width bound because only the actual residue pattern matters.

Example:

`L={0,2,4}`

has width4, so M=5 is a trivial guarantee, but mod3 is already injective on L.

## 5. Universal necessity for bounded primitive classes

The injective-code condition is also necessary for a universal theorem over all worlds using primitive set W and at most Delta outgoing edges.

If two distinct bounded sums

`r != s`

receive the same code, realize r and s as sums of primitive weights on two same-observation source states whose targets all lie in one observation block.

Exact weighted refinement separates the sources in one step; the coded refinement merges them.

The owner includes a collision-to-relation compiler producing this witness automatically.

Thus for the declared world class:

`universal exact local reflection`

iff

`the local code is injective on L(W,Delta)`.

## 6. Exact local decoding reconstructs the weighted machine

Let E be the stable reflected partition. Because E is exact-weight stable, for every action, source block D and target block C the integer

`B_a[C,D]=A_a^E(x,C)`, `x in D`,

is representative-independent.

If the local code is injective, each encoded block weight has a unique lift in `L_local`. Therefore the exact integer quotient matrices B_a can be reconstructed from the finite local code.

The implementation cross-checks the reconstructed matrices against direct exact-integer quotient matrices.

## 7. Raw weighted future semantics factors through the quotient

For a word w, raw weighted execution sums products of primitive edge weights along paths.

The exact weighted quotient reproduces those word values by ordinary integer matrix multiplication.

The branch includes a separate raw-versus-quotient oracle checking literal word traces, so exact factorization is tested independently from the local-reflection code.

This is the bridge from bounded local reflection to potentially unbounded future values.

## 8. Reflect before compose versus compose then quotient

Use primitive weights 1 and2 with local alphabet

`{0,1,2}`.

mod3 is perfectly injective on the entire local law.

Take two two-step paths:

- p uses weight2 then weight2, giving exact derived value4;
- q uses weight1 then weight1, giving exact derived value1.

If one composes directly in mod3:

`4 == 1 mod3`,

so the terminal coarse values collide.

If one first reflects and decodes the local weights 1 and2, reconstructs the exact weighted machine, and then composes in Z, the derived values are correctly recovered as4 and1.

Hence

`local quotient exactness`

does not imply

`all derived values are reflected by the same quotient`.

But it **does** imply that the exact derived semantics can be generated after local decoding.

## 9. Observation code and execution algebra are separate resources

The previous example can be strengthened: the local code does not need any addition or multiplication at all.

One may encode

`0 -> "zero"`, `1 -> "one"`, `2 -> "two"`,

decode those labels, and then execute the recovered machine in Z.

Thus the architecture has three layers:

1. **local observation code** — distinguish the bounded local law;
2. **reflection/decoder theorem** — recover exact local coefficients;
3. **execution algebra** — compose the recovered law to derive future values.

A semiring homomorphism is required only if the coarse coefficient world itself must perform composition before decoding.

## 10. Capability synergy reappears as local coding synergy

On local alphabet `{0,1,2}`:

- parity alone merges0 and2;
- Boolean support alone merges1 and2;
- the paired code `(nonzero, parity)` distinguishes all three.

So two individually insufficient local channels can jointly reflect the exact primitive law.

This is the bounded-local-law version of the earlier semantic capability-join synergy.

## 11. Fixed-world split-content spectrum is sharper still

Injectivity on all of `L_local` is a safe world-level condition, but one fixed state/observation system may need less.

Follow the **exact** weighted refinement sequence. Whenever x,y lie in one current block but split at the next step, flatten their integer local signatures and define

`g_(h,x,y)=gcd(abs(coordinate differences)) > 0`.

modulus M collapses that exact split iff

`M | g_(h,x,y)`.

Therefore the exact bad-modulus set for the fixed world is

`B = union_(split events) divisors(g_event), M>=2`.

The complete mod-M sequence equals the exact sequence iff `M notin B`.

## 12. Geometry of realized exact moduli

The bad set is a finite union of divisibility down-sets.

Its complement — the exact moduli — is upward closed under divisibility.

This is a different modulus-region geometry from several earlier routes:

- static model indistinguishability used a principal divisor down-set;
- uniform affine exact certification used an up-set controlled by cokernel exponent/free structure;
- fixed weighted-refinement exactness uses the complement of a finite union of split-content divisor sets.

The branch checks the split-content criterion against literal modular refinement on the complete two-state sparse weighted family with primitive choices `{-1,1,2}` over several moduli.

## 13. Potential alphabet versus realized precision

A quotient may fail injectivity on values that are mathematically possible as local subset sums yet never compete inside one current state class.

Example: if the initial observation is already discrete, transition refinement is already exact regardless of local coefficient collisions. The split-content event set is empty and every modulus M>=2 reproduces the state sequence.

So keep distinct:

- **class-uniform local-law precision** — injective on the declared possible local alphabet;
- **one-world realized precision** — preserve only the strict splits that actually occur.

## 14. General architecture: reflect before compose

The reusable principle is not specific to path counting.

Suppose a world has:

- a finite/bounded local law alphabet;
- a finite code that reflects that local law exactly;
- a theorem that the recovered local law determines future evolution compositionally in an exact algebra.

Then finite local observation can support unbounded exact derived semantics without directly representing every future value.

The valid workflow is:

`bounded local world`

`-> finite code`

`-> exact local reflection / decode`

`-> exact compositional machine`

`-> unbounded derived semantics`.

The unsafe shortcut is:

`bounded local world`

`-> coarse code`

`-> compose entirely inside coarse code`

`-> infer exact large values without a reflection theorem`.

## 15. Relation to material/ledger routes

The theorem does **not** automatically prove an E001 material law. It supplies a reusable precision pattern.

A material/ledger route may consume it only after proving its own analogues of:

- a bounded local update alphabet;
- exact reflection of those local updates from the chosen coarse code;
- a compositional state that carries every future-relevant remainder/history channel.

If ledger provenance, expiry, branch identity or DOMAIN data can reactivate later, those channels must remain in the local law state before this theorem applies.

## Owner-local assets

- `bounded_local_law_reflection.py` / tests;
- `bounded_local_law_code.py` / tests;
- `weighted_refinement_modulus_spectrum.py` / tests;
- `PRECISION_BOUNDED_LOCAL_LAW_REFLECTION.{en,zh}.md`.

## Prior art / status

Bounded modular reconstruction, subset-sum alphabets, weighted lumping, GCD content and exact machine quotients are standard prior mathematics/CS. P023/A2 retains generic future-signature/precision ownership. This Draft owns only the explicit bounded-local-law reflection-before-compose architecture and its weighted transition pressure test.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.