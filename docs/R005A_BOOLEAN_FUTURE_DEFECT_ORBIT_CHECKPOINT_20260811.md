# R005-A — Boolean Future Defect / Orbit Checkpoint

Status: `PROVED STRUCTURAL CHECKPOINT / EXECUTABLE CHECKED / NOT CANONICAL / LEAN PENDING`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Researcher-ID: `R005A-7C2`  
Date: `2026-08-11`

This continues the same R005-A owner generation. It does not reopen the first-round taxonomy, does not create a new task, and does not alter canonical Prime Toolkit ownership or status.

Internal prime fixtures/helpers remain consumed through the canonical toolkit where the Python research harness needs them. This checkpoint adds no replacement primality, prime-enumeration, least-factor, square-basin, centered-coordinate, or power-free-action helper.

## 1. T-A44 — finite-defect separator lift

Let `W : Z -> {0,1}` be a `Q`-periodic steady word and let `D` be a finite defect set. Define the actual one-sided stream

`A(n) = W(n) xor 1_D(n)`.

For starts `a<b`, put `d=b-a` and define the periodic steady separator

`M_d = {x : W(x) != W(x+d)}`.

Then for every `t>=0`, exactly

`A(a+t) xor A(b+t)`

`= 1_{M_d}(a+t) xor 1_D(a+t) xor 1_D(b+t)`.

Equivalently, in absolute coordinates the mismatch set is

`E_{a,b} = (M_d triangle D triangle (D-d)) intersect [a,infinity)`,

where `D-d={x:x+d in D}`.

Hence the first distinguishing time is

`min(E_{a,b})-a`.

This is an elementary ultimately-periodic / finite-defect identity, not a novelty claim. Its value here is decomposition: **steady arithmetic geometry lives in `M_d`; activation history lives only in a finite symmetric-difference toggle.**

### Prime-prefix specialization

For the actual Boolean Eratosthenes prefix sieve with all primes `P_q={p:p<=q}`, the previously proved defect set is

`D_q={0} union P_q`.

Therefore every transient-versus-steady or transient-versus-transient distinction is an exact finite-toggle perturbation of a steady wheel separator.

The new executable checks this identity exhaustively for the `7#` system across every canonical start pair and two full periods of continuation.

## 2. Generic eventual-domination route is false

No generic ultimately-periodic theorem can prove that the full actual horizon eventually equals the steady horizon.

Take the period-two word `W=0101...`, whose two steady residuals distinguish immediately, so its steady separation radius is `0`.

For any `m`, toggle the finite defect set

`D={0,2,4,...,2m}`.

The resulting actual stream begins with `2m+2` consecutive ones. Consequently the shift residuals starting at `0` and `1` agree for exactly `2m+1` symbols before separating.

Thus finite defects can increase transient distinguishing depth arbitrarily while leaving steady radius fixed.

So the observed prime-prefix equality

`H_U^actual(q)=rho(q#)`

for larger tested prefixes, if it is true eventually, requires **prime-specific structure of `D_q={0} union P_q` and the wheel**, not generic automata theory.

## 3. T-A45 — support orbit and residual unit phase

Let `Q` be squarefree with prime set `P`. For a nonzero shift `d mod Q`, define its changed-prime support

`J(d)={p in P : p does not divide d}`.

For a fixed nonempty support `J`, write

`M_J=product(J)`,

`g_J=Q/M_J`.

Every shift with exact support `J` is uniquely of the form

`d = g_J*u mod Q`

with

`u in (Z/M_J Z)^*`.

Equivalently, two shifts have the same support iff they lie in the same multiplicative-unit orbit under `(Z/QZ)^*`.

If `v` is a unit modulo `Q`, then the steady separator sets satisfy

`M_{v d} = v M_d`.

So support collapse is exactly a multiplicative-orbit collapse.

### Classical CRT invariant: separator mass

For `J=J(d)`, simultaneous CRT counting gives

`|M_d| = 2*phi(Q) * (1 - product_{p in J} (p-2)/(p-1))`.

This is classical local-factor / simultaneous-coprimality arithmetic. In particular, separator Hamming mass depends only on `J`, not on the residual unit phase `u`.

### Additive future geometry does not descend to support

The additive execution operation is `x -> x+1`. Multiplication by a general unit does not preserve this ordered cyclic metric. Therefore the largest separator gap need not be constant on a support orbit.

The smallest clean counterexample is `Q=30`, `P={2,3,5}`:

- `d1=6`, `d2=12`;
- both have changed support `{5}`;
- `d2 = 7*d1 mod 30`, with `7` a unit;
- both separator sets have cardinality `4`;
- but their maximum cyclic separator gaps are `14` and `10`;
- hence their local horizons are `rho_6=13` and `rho_12=9`.

Therefore

`prime-support sufficient for separator mass`

but

`prime-support not sufficient for additive future depth`.

This is a hard boundary for any support-only compiler that also claims to preserve segmented/additive execution cost.

It does **not** refute Draft #333's semantic prime-support compiler: #333 remains a distinct WIP semantic/instruction layer. The result says that an additive-runtime cost language needs a further refinement.

### Canonical residual coordinate for cost geometry

For fixed support `J`, the natural extra coordinate is the unit phase

`u = d/g_J mod M_J`.

Negation is harmless for the scalar gap profile because

`M_{-d}=M_d+d`,

so translation preserves cyclic gaps and `rho_d=rho_{-d}`.

Thus `(J,[u] modulo +/-)` is a canonical sufficient refinement for the per-shift gap profile. No claim is made that it is always the globally minimal refinement; accidental further identifications may occur.

For a singleton support `J={p}`, support alone collapses `p-1` shifts to one state, whereas the additive gap geometry may retain up to `(p-1)/2` sign-classes. The `p=5`, `Q=30` example proves that at least two such classes can be genuinely distinct.

## 4. Paired-Jacobsthal prior-art attack

Let

`A=(Z/QZ)^*`

be the reduced-residue set. For one shift `d`, the pair progression splits into three event sets:

- `I_d = A intersect (A-d)` — both entries coprime (`11` event);
- `M_d = A triangle (A-d)` — exactly one entry coprime (`01/10`, XOR event);
- `B_d = A^c intersect (A-d)^c` — neither entry coprime (`00` event).

Ziller–Morack's paired Jacobsthal function is direct prior art for the **same paired progression object with a different target event**: it asks for the worst waiting time until an `I_d` (`11`) event for admissible paired progressions.

Primary prior art:

- Mario Ziller, John F. Morack, *Divisibility in paired progressions, Goldbach's conjecture, and the infinitude of prime pairs*, arXiv:1706.00317 (2017).
- Mario Ziller, John F. Morack, *A short note on the computation of the generalised Jacobsthal function for paired progressions*, arXiv:1706.03668 (2017).
- Mario Ziller, John F. Morack, *Algorithmic concepts for the computation of Jacobsthal's function*, arXiv:1611.03310 (2016).

Our Boolean wheel radius instead satisfies

`rho_d+1 = maximum cyclic gap in M_d`,

and `rho(P)=max_d rho_d`.

Therefore the generic idea “study waiting times in paired primorial progressions” is **prior art**. The R005 specialization is verifier/observation-relative: it targets XOR disagreement rather than simultaneous coprimality.

There is no simple numerical reduction from the primorial paired Jacobsthal value `h_2` to `rho+1`. For the same prime prefix the exact values already cross repeatedly:

| max prime q | rho(q#)+1 | paired h_2 for q# |
|---:|---:|---:|
| 5 | 14 | 18 |
| 7 | 38 | 30 |
| 11 | 66 | 66 |
| 13 | 138 | 150 |
| 17 | 238 | 192 |
| 19 | 366 | 258 |

Thus paired-Jacobsthal algorithms are relevant external computational prior art, but paired-Jacobsthal values do not directly answer the XOR future-separation problem.

Classification:

`GENERIC PAIRED-PROGRESSION FRAME = PRIOR_ART_ONLY`

`XOR EVENT / FUTURE-LANGUAGE SPECIALIZATION = ENTERPRISE_SPECIALIZATION / NOVELTY_UNVERIFIED`.

## 5. T-A46 — exact full actual horizon at 19#

The companion `r005a_boolean_rho19_certificate.cpp` already proves

`rho(19#)=365`.

The new defect/orbit executable exhaustively compares every transient start `0,...,19` with every steady phase modulo

`19# = 9,699,690`,

and also checks every transient/transient pair.

It proves the largest horizon among all pairs involving a transient state is exactly

`T_19=173`,

attained from transient start `18` against a steady phase whose difference is

`d=19#/19=510510`.

Therefore

`H_U^actual(19)=max(365,173)=365`.

The same executable records

`T_17=91 < rho(17#)=237`.

Together with the smaller exact checks, the current table is:

| q | steady rho | max transient-involving horizon | full actual H |
|---:|---:|---:|---:|
| 2 | 0 | 3 | 3 |
| 3 | 3 | 4 | 4 |
| 5 | 13 | 15 | 15 |
| 7 | 37 | 23 | 37 |
| 11 | 65 | 63 | 65 |
| 13 | 137 | 91 | 137 |
| 17 | 237 | 91 | 237 |
| 19 | 365 | 173 | 365 |

This supports but does not prove:

`CONJECTURE R005A-BOOL-DOM:` for every prime `q>=7`, `H_U^actual(q)=rho(q#)`.

The generic finite-defect counterexample above prevents promotion without a prime-specific argument.

## 6. T-A47 — storage / observation-depth enclosure without the conjecture

The conjecture is not needed to obtain a rigorous asymptotic separation.

### Lower bound

For the singleton changed support `{q}`, the separator count is exactly

`2*phi(Q)/(q-1)`.

Therefore its average cyclic separator gap is

`Q(q-1)/(2 phi(Q))`,

and hence

`rho(q#)+1 >= Q(q-1)/(2 phi(Q))`.

By Mertens' product theorem,

`Q/phi(Q) ~ e^gamma log q`, so

`rho(q#) >= (e^gamma/2 + o(1)) q log q`.

### Classical Jacobsthal upper bridge

For any changed coordinate `p not dividing d`, the separator contains a translated/scaled copy of the reduced residues modulo `Q/p`. Hence

`rho_d+1 <= p*j(Q/p)`.

Consequently

`rho(q#)+1 <= q*j(q#)`.

Iwaniec's classical linear-sieve bound for the Jacobsthal gap gives

`j(q#)=O(q^2)`, so

`rho(q#)=O(q^3)`.

Thus the steady Boolean future depth satisfies

`Omega(q log q) <= rho(q#) <= O(q^3)`.

### T-A48 — preperiod-additive full-horizon law

There is a much sharper bound than the generic finite-defect gap-merging estimate.

For any one-sided ultimately periodic deterministic output system with minimal preperiod `mu` and steady phase-separation radius `rho`, the full first-distinguishing horizon `H` satisfies

`rho <= H <= rho + mu`.

The lower bound is immediate because the steady states are part of the full state set. For the upper bound, take any two distinct full states. After at most `mu` transitions both tails lie in the steady cycle. If their resulting steady phases differ, they separate within a further `rho` transitions. If the resulting steady phases coincide, then any distinction between the original states must already occur before both tails enter the common steady phase.

This is generic ultimately-periodic automata mathematics, not a new mother theorem. Its prime-specific force comes from the exact Boolean activation preperiod

`mu_U(q)=q+1`.

Therefore

`rho(q#) <= H_U^actual(q) <= rho(q#) + q + 1`.

Combining this with the singleton-support lower bound

`rho(q#)+1 >= Q(q-1)/(2 phi(Q))`

and Mertens' product theorem gives the unconditional relative asymptotic

`H_U^actual(q) / rho(q#) = 1 + O(1/log q)`.

In particular,

`H_U^actual(q) / rho(q#) -> 1`.

Thus exact eventual equality remains conjectural, but **asymptotic steady domination is proved**. The activation transient can change the exact finite horizon by at most an additive `q+1`, while the steady Boolean separation radius already grows at least on the order of `q log q`.

Using the classical Iwaniec bound `C(r) << (r log r)^2` with `r=pi(q)` gives `j(q#)=O(q^2)` and hence

`H_U^actual(q)=O(q^3)`.

Together with the lower bound,

`Omega(q log q) <= H_U^actual(q) <= O(q^3)`.

Since the exact state count is

`N_U(q)=q# + q + 1`

and the prime number theorem gives `log N_U ~ q`, this becomes

`Omega(log N log log N) <= H_U^actual <= O((log N)^3)`.

The stronger conclusion is not merely the polynomial enclosure: the full actual and steady Boolean horizons have asymptotic ratio one.

### Segmented execution corollary

For a segment observation length `B`, the existing exact block-composition law gives

`D^*(B)=ceil((H+1)/B)-1`.

Let `D_actual^*(B)` and `D_steady^*(B)` be the sharp transition depths for the actual and steady Boolean systems. From the additive horizon bound,

`0 <= D_actual^*(B)-D_steady^*(B) <= ceil((q+1)/B)`.

Hence if `B>=q+1`, activation costs at most **one additional segment transition** beyond the steady wheel's exact phase-identification depth.

This is the cleanest current segmented-sieve resource law: the activation transient contributes `q+1` extra exact states but only a bounded additive execution-depth overhead, while the dominant long-horizon difficulty lies in the steady XOR separator geometry.

For relation-resolved actual observation, the preceding owner-local generation reported the executable formula

`H_R^actual(q)=max(12,q-1)` for prime `q>=5`.

This checkpoint does not re-prove or independently revalidate that relation-resolved formula, so it is used only as owner-local comparison context rather than as a new premise. The Boolean storage/depth enclosure above is independent of it.

Therefore attribution erasure has an asymptotically negligible relative state-count saving but incurs at least an `Omega(log q)=Omega(log log N)` relative observation-depth penalty.

This strengthens the previous storage/depth Pareto result without relying on the unproved exact eventual-domination conjecture; the exact equality question is reduced to a bounded additive transient residue on top of an asymptotically dominant steady radius.

## 7. Practical factor-witness backend contract tightened

External infrastructure audit remains `CLASSICAL_BASELINE`.

Current FLINT documentation distinguishes:

- bounded/incomplete trial factorization with an unresolved cofactor;
- Pollard–Brent returning one nontrivial factor, explicitly not guaranteed prime and not a complete factorization;
- probable-prime predicates;
- `fmpz_is_prime`, which attempts and, on success, returns a proved-prime result using deterministic/proof-producing methods with APRCL fallback.

Python-FLINT exposes `fmpz.factor(trial_limit=...)`, with documented incomplete-factor behavior, plus `is_prime()` and `is_probable_prime()`.

Therefore an Enterprise adapter should not equate backend search mode with certificate status. The minimal normalized outcomes remain:

- `EXACT_COMPOSITE_WITNESS(d)` once `1<d<n` and `d|n` are rechecked locally;
- `UNRESOLVED_UNDER_BUDGET` when no factor is found;
- `PROBABLE_PRIME` only when the backend provides only probable-prime status;
- `PROVED_PRIME` only after a proved-prime call;
- `PARTIAL_FACTORIZATION_WITH_COFACTOR` for incomplete factor lists;
- `COMPLETE_FACTORIZATION_PROVED` only when completeness and primality of every factor are established.

A randomized factor search can therefore feed an **exact** composite certificate: randomness affects discovery, not the validity of the verified divisor relation.

This remains external classical infrastructure and must enter any future Prime Toolkit adapter with `CLASSICAL_BASELINE` provenance.

## 8. Current four-layer return

### Already supplied by canonical Internal Prime Toolkit

No change: bounded exact prime oracle/enumeration, least-factor and visible-factor queries, first-factor shells, proof horizon, square-basin certificate, centered coordinates, #249 one-step power-free action basis, and provenance registry.

### External classical capability

- FLINT / PARI-style practical factor discovery and proved/probable factor status;
- ordinary and paired Jacobsthal algorithms / bounds;
- unary/ultimately-periodic automata and LCP machinery.

All remain `CLASSICAL_BASELINE` or `PRIOR_ART_ONLY` as appropriate.

### Enterprise specialization

- `p^2` activation defect set and exact transient quotient;
- XOR separator geometry `M_d` for Boolean future observation;
- support-orbit versus additive-future mismatch;
- unit-phase runtime refinement;
- storage / observation-depth Pareto under the chosen future language.

### Genuine theorem / boundary candidates

1. `R005A-BOOL-DOM` — exact prime-prefix steady domination `H_U^actual(q)=rho(q#)` for `q>=7`; currently **CONJECTURAL**, exact through `q=19` only. Its asymptotic ratio form `H_U^actual/rho -> 1` is now proved via T-A48.
2. `support-only runtime insufficiency` — already exact, with the `Q=30` minimal counterexample; candidate reusable negative boundary rather than new prime theorem.
3. `XOR-Jacobsthal / disagreement-gap profile` — useful Enterprise quantity, but generic paired-progression framing has direct prior art; novelty remains unverified and no new mother theory is justified.

## 9. Validation / repository status

New executable:

`experiments/r005a_boolean_future_defect_orbit.cpp`

Local command:

`g++ -O3 -std=c++17 experiments/r005a_boolean_future_defect_orbit.cpp -o /tmp/r005a_boolean_future_defect_orbit && /tmp/r005a_boolean_future_defect_orbit`

Local result:

`R005-A Boolean future defect/orbit regressions passed`

The exact run includes the `17#` and `19#` transient-vs-steady exhaustions; the current local `19#` run takes on the order of tens of seconds, so this remains a research certificate rather than a routine unit test.

`CI_NOT_REQUIRED_FOR_RESEARCH`.

No canonical theorem status is changed, no Lean claim is made, and no Prime Toolkit registry entry is promoted by this checkpoint.
