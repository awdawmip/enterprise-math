# Witness-oriented quotients for a finite native factor instrument

Status: SYMBOLIC_EXTENSION_AND_SOURCE_AUDIT; shared-context author research, NOT_ADMITTED. No scientific execution, host arithmetic experiment, new provider query, or remote write was performed for this note. This is a candidate interface and a proof of its scope, not an efficient factoring claim.

## 1. Audited existing tools and the precise extension

The following files were actually read through the connector at immutable Enterprise Math commit `2e81851d62c869a20b47ae083a24dde1a4c0420c`:

| Existing source | Git blob | Reused scope |
|---|---|---|
| `enterprise_toolbox_registry.json` | `3889506451091ebcfbf7a58cda6517c4af8c3597` | T0 support/result/provenance; T4 declared fibers; T8 future-observation safety |
| `src/enterprise_math/brc_histogram.py` | `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` | Exact positive-weight histograms; serial multiplication and recoalescence |
| `src/enterprise_math/brc_transport.py` | `be1debe367263931bd5e93fd750be3ed54624fe1` | Fixed-weight affine degree-at-most-two moments only; not a gcd observer |
| `src/enterprise_math/relation_observable_signature.py` | `abed242730b1736f8e277b14e808a10015a653df` | Coarsest one-step set-valued observation partition; includes undefinedness |
| `src/enterprise_math/relation_observable_composition.py` | `b7b7be69ecfe9c4b61ae0a694f0ff6c61483c025` | Composition requires the next signature to descend through the quotient |
| `src/enterprise_math/relation_future_powerset.py` | `7947f1a4400c8c674001597dd41256d9cd3ff477` | Finite support compiler; its all-word signature implementation explicitly enumerates words |
| `research_notes/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md` | `e3b1488a9bfdc44795f5d0e78c67e8c128bd30dc` | Exact representative reduction only for already declared fibers and compatible downstream predicates |

All paths have immutable URLs of the form `https://github.com/awdawmip/enterprise-math/blob/2e81851d62c869a20b47ae083a24dde1a4c0420c/<path>`.

**REUSE:** finite-horizon backward reachability, absorbing instruments, weighted lumpability, ideals, and batch gcd are standard concepts. No renaming of them as new mathematics is intended. T8 already supplies the required congruence test; T4 cannot discover an unknown useful partition for free.

**EXTENSION:** specialize the observer to a finite prescribed schedule and the first valid factor, then lift the quotient condition to the actual `WeightHistogram` carrier. A terminal success does not need to preserve any future return sequence. Distinguish an exact output instrument from a weaker procedure that merely returns some valid divisor.

**NEW IMPLEMENTATION GAP:** a small representation of pulled-back factor predicates, or a small evaluable product observer, with charged native evaluation and extraction. None of the audited files already supplies this operation on a succinct modular branch DAG.

## 2. Declared carrier, observer and allowed future

Let `N>1` and all moving endpoints be units modulo `N`. A raw active state is `(i,x,y)`, where `i` is the schedule position. At step `i`, a finite list of branches applies

`(x,y) -> (s_(i,b) x, t_(i,b) y)`

with declared unit multipliers and positive rational branch weights. Retain duplicate branches and their multiplicities. This list, its remaining horizon `L`, and its observation times are inputs. They are not replaced by all possible future powers.

After a declared observation, compute `d=gcd(N,x-y)`. If `1<d<N`, enter terminal `FACTOR(d,i)` and stop the branch. Otherwise remain active; a full collision `d=N` is not a factor. Unsuccessful active states at the horizon produce `FAIL`. If initial observation is desired, declare it at depth zero. No order or factors are constructor inputs.

For the exact instrument, terminal labels include the actual divisor and first-hit depth. For the weaker search contract, any verified `1<d<N`, `d|N` is acceptable; neither its frequency nor its first-hit depth need match a reference law. These contracts must not be interchanged.

The ratio map `u=x y^(-1)` is reused, not a new discovery. Because `y` is a unit,

`gcd(N,x-y)=gcd(N,u-1)`,

and a branch sends `u -> s_(i,b) t_(i,b)^(-1) u`. Thus this quotient commutes branch by branch with every declared update and with the factor observer. It needs a charged inverse, not an unknown order. A pair with a nonunit endpoint requires an explicit separate gcd branch; the theorem does not silently invert it.

## 3. Exact finite-schedule first-hit quotient theorem

Let `H` be the finite histogram semiring implemented by `brc_histogram.py`. An atom `[w]` means one path of weight `w`; addition is `histogram_recoalesce`, multiplication is `histogram_serial`. Its zero is the empty histogram and its identity is `[1]`.

At each depth choose a map `q_i` on active and absorbed states. Keep distinct requested terminal labels distinct. For each raw state `x` and next quotient class `C`, define the histogram-valued kernel

`K_i(x,C) = sum_(b : q_(i+1)(F_(i,b)(x))=C) [w_(i,b)]`,

where `F` includes the post-update first-hit observation. For an already terminal state, use one identity transition of histogram `[1]`.

**Theorem.** If for all `x,x'` in the same `q_i` class and every next class `C`,

`K_i(x,C)=K_i(x',C)` as complete histograms,

then pushing a raw state-indexed histogram through `q_i` and applying the quotient kernel gives exactly the same next class-indexed histograms as raw propagation followed by pushforward. By induction this preserves every requested `FACTOR(d,j)` histogram and the final failure histogram at all remaining depths.

**Proof.** For a next class `C`, raw propagation gives

`sum_x H_i(x) * K_i(x,C)`.

Group the outer sum by the current quotient class. The stated equality makes `K_i(x,C)` independent of the representative; semiring distributivity gives the quotient update. Terminal identity transitions preserve the weight and multiplicity of each already stopped history. Induct on the finite horizon. There is no limit, spectral assumption, phase cancellation or order input.

For a finite explicitly available state carrier, define partitions backward: at the horizon use the declared terminal observation; at each earlier depth group states by their present terminal observation and their complete kernel signature into the next partition. This is the coarsest recursively compatible partition for this signature contract. It need not be the coarsest partition preserving only one final marginal, and constructing it may enumerate a large carrier. No polynomial size is asserted.

**Multiplicity boundary.** The two branches `00` and `11` of a paired binary step contribute `2[1/4]` to the unchanged ratio. Replacing them by `[1/2]` preserves total mass but changes path count, the weight histogram and higher weight moments. Either keep `2[1/4]`, or explicitly weaken the observer contract to total mass. The present theorem uses the stronger contract.

**Stopping boundary.** Continuing a successful branch through four extra `[1/4]` transitions changes its stopped-history histogram even though total mass remains unchanged. The first-hit instrument uses `[1]` absorption, or simply retains the terminal record outside the live state. A separate fixed-length, unstopped path law would require another declared observer.

The ratio quotient meets the theorem by a branch-preserving bijection and gcd invariance. This proof directly supports a native comparison of full `(x,y)` expansion with ratio propagation, including complete live and `FACTOR(d,first_hit_depth)` histograms. It does not require testing all future powers.

## 4. Weaker support pullback with a paid witness extractor

Let `J_i(u)` mean that the presently observed residue already yields a proper divisor. Define a backward predicate over the *fixed* remaining schedule:

`E_L(u)=J_L(u)`,

`E_i(u)=J_i(u) OR OR_(declared b) E_(i+1)(c_(i,b)u)`.

Observation conventions can instead apply `J` after each update; the schedule must state which convention is used. Duplicate positive-weight branches do not change this Boolean predicate, while they do change the histogram instrument in Section 3.

**Extraction theorem.** Suppose a callable, exact native oracle supplies these `E_i`, and `E_0(u_0)` is true. Test the current gcd. If it is proper, stop. Otherwise inspect the finitely many child predicates and select a true child. At least one exists by the recurrence. Repeating yields a proper divisor by depth `L`. With branch fanout at most `B`, this requires at most `BL+1` predicate queries and `L` selected updates, in addition to observer and oracle construction/evaluation costs.

This is an actual interface reduction, not a cheap-oracle assertion. A plain recursive oracle can evaluate exponentially many nodes. The bit `E_i(u)` alone is not a sufficient state for the next action: two winning states can require opposite successful children. A composable implementation must supply child predicate pullbacks or a certified choice function; it cannot forget `u` and expect the winning bit to reconstruct it.

A resumable bounded implementation may return `FOUND(d,certificate)`, `EMPTY(complete_no_success_certificate)`, or `UNKNOWN(cursor,paid_work)`. `FOUND` absorbs the remaining search; `EMPTY` may be joined only after all relevant children are proved empty; a budget stop is `UNKNOWN`, not `EMPTY`. Once a verified factor has been found, merging different successful paths while retaining one valid factor is sound for the weaker search contract, even if it deliberately does not preserve the exact factor distribution.

This is T0 support/result reuse plus a witness extraction obligation. T8's generic powerset compiler does not store the needed path witness and cannot certify `EMPTY` from an unfinished search. There is no claim that the support-only procedure reproduces signed amplitudes or a QFT distribution.

## 5. What gcd and ideal strata do, and do not, close

### 5.1 Shared affine units: an exact but restrictive closure

Under `(x,y)->(b x+t,b y+t)` with unit `b`, the principal ideal generated by `x-y` modulo `N` is unchanged. Hence `gcd(N,x-y)` is an exact invariant. Weighted mixtures of these common actions descend to the gcd strata.

This action family cannot create a new factor status from a pair with gcd one or `N`. Applying different multipliers to the two endpoints is the productive operation, and it is exactly the operation not covered by this simple invariant.

### 5.2 A one-step counterexample, not an all-futures lower bound

Consider the symbolic family `N=pq`, with distinct primes and a unit `a` of order three modulo `p` and order greater than three modulo `q`. The active ratio states `u=a` and `v=a^2` both satisfy `gcd(N,u-1)=gcd(N,v-1)=1`.

In a single remaining step allowing identity and multiplication by `a`, the state `u` has no successful child: its possible residues are `a,a^2`. The state `v` has a successful `a` child: `a^3` is one modulo `p` and not one modulo `q`, yielding `p`.

Thus even a horizon-one, first-hit-and-stop observer can split the current gcd-one stratum. Both states are in the same cyclic orbit. This is a symbolic counterexample family, not a generated numerical fixture or a claim that every fixed schedule needs a large quotient.

### 5.3 A compact ideal closure that preserves the wrong quantifier

For unit `u` and declared unit multipliers `c_1,...,c_t`, let `C` consist of all binary subset products `prod_j c_j^(e_j)`. In the integers, including `N` among the ideal generators,

`<N, {u c-1 : c in C}> = <N, u-1, c_1-1,...,c_t-1>`.       (1)

**Proof.** The left side contains `u-1` (empty subset) and `u c_j-1`. Their difference is `u(c_j-1)`. Since `u` is invertible modulo `N`, this implies `c_j-1` lies in the same ideal. Conversely, `c-1` is a sum of multiples of the `c_j-1`, by telescoping the product, and `u c-1=u(c-1)+(u-1)`. Both containments follow.

Equation (1) reduces exponentially many formal generators to `t+2`, without knowing the order. It preserves the divisor common to **all** candidate differences. The desired witness predicate asks whether **some** candidate has a proper gcd. These are different quantifiers.

For example, in the symbolic squarefree case `N=pq`, one multiplier may be one only modulo `p`, and another one only modulo `q`. Both offer proper factors from `u=1`, while their joint ideal is the unit ideal. Conversely, if the generator gcd in (1) is proper, a proper divisor was already available in at least one of the short input gcds; this contraction by itself does not provide a new search advantage. It is an exact algebraic closure, not a factor-discovery primitive.

## 6. Product observer: composable but with a precise readout bill

For a finite candidate set or multiset `C`, define the ring-valued observer

`P_C(u)=prod_(c in C) (cu-1) mod N`.

For disjoint blocks, `P_(C union D)=P_C P_D mod N`. If `1<gcd(N,P_C(u))<N`, that gcd is already a valid output factor; no order, exponent difference, inverse image or individual leaf witness must be recovered. This is standard batch-gcd reuse.

The cases `gcd=1` and `gcd=N` are different: one proves every candidate difference is a unit; the other is saturation. It does not prove either existence or absence of a proper individual gcd. Symbolically, the two lists `(p,q)` and `(N,1)` both have product zero modulo `N`; only the former list has proper-gcd leaves.

**Conditional logarithmic readout theorem.** Suppose a binary product tree has height `h`, exact child products are available with their construction costs already paid, no leaf difference is zero modulo `N`, and the root product is a nonunit. Then a proper factor can be obtained with at most `2h+1` additional gcd observations. If a node gcd is proper, stop. If it is `N`, at least one child is a nonunit; test children and descend to one. Reaching a leaf with gcd `N` is excluded by the promise, so a proper gcd is encountered.

The no-zero-leaf promise is material. In a modular return problem such leaves naturally occur; proving their absence may itself be expensive. Without it, preserve the saturated node and either explore further with a charged traversal or return `UNKNOWN`. Neither normalization nor conditioning removes this obligation.

For an exponent interval, the formal polynomial recurrence

`F_(j+1)(X)=F_j(X) F_j(a^(2^j)X)`, `F_0(X)=X-1`,

describes `prod_(0<=e<2^j)(a^e X-1)`. Its description is short but its two arguments differ. Sharing source text does not share evaluated values. Direct evaluation may still take `2^j` leaf operations, and storing all child products may be equally large. No audited T0/T4/T8 API supplies this evaluation at polynomial bit cost.

This observer is worth retaining as a *target contract* if a native structural law later computes these products cheaply. Implementing a large classical product tree through full-adders alone would not answer the user's request for a new native reduction.

## 7. Smallest useful implementation and accounting boundary

The immediate bounded implementation is Section 3's first-hit relative-port instrument: actual `WeightHistogram` composition, typed unit actions and gcd, complete live/terminal histogram comparison against the same declared pair process. It should include both a successful first hit and a no-factor path, full-collision continuation, duplicate `00/11` multiplicity, and a serialized cursor containing its exact schedule and stopped outputs. A factor found is checked as a divisor; it is not inferred from a collision count.

For a later genuinely new compression tool, the API should expose:

`compile_predicate(schedule, observer, representation_budget)`;

`pullback(node, branch)` with a native semantic certificate;

`query(node, u) -> FOUND | EMPTY | UNKNOWN` and its paid cost;

`extract(node, u)` consuming those certificates rather than a hidden order table.

Charge distinct live quotient states, histogram entries, action setup, native actions and observers, predicate node construction, evaluated child nodes, storage, and extraction. Any cached quotient must bind the remaining schedule and observation contract. A quotient admitted for total mass is not automatically admitted for histogram multiplicity, path provenance or first-hit labels.

Positive result: finite-schedule first-hit absorption is an exact, composable weakening of complete-return preservation, and can terminate as soon as a valid factor exists on an observed branch. Unresolved: finding or evaluating a sufficiently small useful predicate/product representation for general unknown-order inputs. No full-Shor success probability or polynomial-cost claim follows from this note.

The current startup guard permits research/persistence under `RA-CAAAC604CB513AEA8BBC1DFC`; it is not mathematical admission. Policy Markdown and machine JSON for `ACTUAL_TYPED_BRC_ONLY` were actually read. The new GK snapshot differs from `8c6557d` only by journal/researcher metadata, not the applicable policy.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
