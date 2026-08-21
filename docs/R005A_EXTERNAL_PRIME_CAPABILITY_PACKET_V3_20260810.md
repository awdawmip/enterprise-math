# R005-A — EXTERNAL PRIME CAPABILITY PACKET v3

Status: `THIRD_ROUND_CLOSURE / NOT CANONICAL / LOCAL_EXECUTABLE_CHECKED`

Task: `RS-R005-PRIME-ALGORITHM-LAB`

This is the closure round of the same R005-A task. It does not reopen the first-round taxonomy and it does not create a new taskbook.

## 0. Closure decision

After the second-round de-duplication, the third round leaves:

- **zero justified new generic Foundation/mother theorems**;
- **one strong exact Enterprise specialization** for the actual `p^2` activation transient of a multi-prime sieve;
- **one genuinely unresolved prime-specific exact quantity**, the Boolean wheel phase-separation radius `rho(P)`;
- **family-specific verifier-profile normal forms** for Pratt/Pocklington, attacked by ECPP;
- **no prime-specific compiler residue** beyond existing A2/FQ-006 continuation/quotient theory.

The main new mathematical content is therefore not a new primality algorithm. It is an exact resource separation:

`same eventual CRT-state cardinality != same finite observation depth != same activation transient`.

## 1. Actual Eratosthenes activation as an ultimately periodic future system

Fix a finite nonempty set `P` of distinct primes and put `Q = product(P)`.

For integer position `n >= 0`, define the actual relation-resolved sieve observation

`R_P(n) = {p in P : n >= p^2 and p | n}`

and the Boolean union-support observation

`U_P(n) = 1[R_P(n) is nonempty]`.

Their steady wheel counterparts are

`R_inf(n) = {p in P : p | n}`,

`U_inf(n) = 1[gcd(n,Q)>1]`.

Both actual streams are ultimately `Q`-periodic.

### T-R005A-TR1 — exact relation-resolved preperiod

Let `p_max=max(P)`. Then the earliest index from which `R_P` agrees forever with its steady wheel is

`mu_R(P) = p_max^2 - p_max + 1`.

Proof. For a fixed p, the only steady p-labels suppressed by the `p^2` activation rule occur at `p, 2p, ..., (p-1)p`. The last suppressed p-label is `p^2-p`. Taking the maximum over p gives the formula, and the last label is genuinely missing, so the boundary is sharp.

### T-R005A-TR2 — exact Boolean union-support preperiod

For p in P define

`W_<p = product({q in P:q<p})`

and

`r_P(p) = max{m : 1<=m<p and gcd(m,W_<p)=1}`.

Then

`mu_U(P) = 1 + max_{p in P} p*r_P(p)`.

Proof. A steady Boolean strike at `n<p^2` is missing from the actual sieve iff the least P-prime divisor of n is p and n=pm with m<p. That is equivalent to `gcd(m,W_<p)=1`. The last such ghost is exactly the displayed maximum.

### Prime-prefix corollary

If P consists of **all primes <= p_max**, then every `m` with `1<m<p` has a smaller prime divisor already in P, so `r_P(p)=1`. Hence

`mu_U(P)=p_max+1`.

This is the classical Eratosthenes reason that multiples `2p,...,(p-1)p` need not be newly crossed when p activates at `p^2`: they have already been eliminated by smaller primes. The underlying activation fact is therefore `PRIOR_ART_ONLY`; the contribution here is its exact future-quotient comparison with the relation-resolved language.

### Exact unbounded future-state counts

The steady tails have least period Q (frozen second-round theorem). A one-sided ultimately periodic word with minimal preperiod mu and least period Q has exactly `mu+Q` shift-residual states. Therefore

`N_R(P)=Q+mu_R(P)`,

`N_U(P)=Q+mu_U(P)`.

For a prime prefix through p:

`N_R-N_U = p(p-2)`.

So attribution erasure buys **no steady-state phase quotient compression**, but it can remove a large block of activation-transient residual states.

Classification: `ENTERPRISE_SPECIALIZATION`, not new sieve arithmetic.

## 2. Finite-horizon precision as an exact quotient chain

Let O be either actual output stream and let `mu` be its exact preperiod. Use the canonical state set

`S={0,...,mu+Q-1}`

with transition `tau(s)=s+1`, except `tau(mu+Q-1)=mu`.

For inclusive horizon H define

`Sigma_O^{<=H}(s)=(O(s),O(tau s),...,O(tau^H s))`.

The coarsest exact H-future quotient is equality of these signatures.

### T-R005A-H1 — exact refinement recursion

Define partition labels by

`pi_0(s)=O(s)`

and

`pi_{H+1}(s)=(O(s),pi_H(tau(s)))`.

Then

`Sigma_O^{<=H}(s)=Sigma_O^{<=H}(t) iff pi_H(s)=pi_H(t)`.

Thus the exact class count is

`C_O(H)=|{pi_H(s):s in S}|`.

The chain is monotone refining and stabilizes exactly at the full residual quotient `mu+Q`.

This recursion is ordinary deterministic automaton/Moore-style partition refinement and is not a novelty claim.

### Exact stabilization horizon

Let

`H_O* = max_{s!=t} min{h>=0 : O(tau^h s) != O(tau^h t)}`.

Then `H_O*` is precisely the earliest finite horizon recovering the full unbounded quotient.

### T-R005A-H2 — single-prime transient closed form

For `P={p}` there are `p^2+1` full states and

`C_p(H)=min(H+2,p^2+1)`,

`H_p*=p^2-1`.

Reason: a state is exactly the delay delta in `{0,...,p^2}` to its first active strike. For horizon H, delays `0,...,H` are individually visible and every delay >H lies in one all-zero fiber.

### T-R005A-H3 — relation-resolved steady phase recovery

For a fixed active distinct prime set P,

`H_R,steady*(P)=p_max-2`.

Upper bound: two distinct CRT phases differ modulo some p. Their next p-strike offsets are distinct in `{0,...,p-1}`, so the smaller offset is at most `p-2` and separates the two relation-labeled streams.

Sharpness: by CRT choose phases identical modulo every q != p_max and with next p_max offsets `p_max-2` and `p_max-1`. Their first relation-resolved difference is exactly at `p_max-2`.

## 3. Boolean wheel phase-separation radius

Define the steady Boolean wheel

`w_P(x)=1[gcd(x,Q)>1]`

and the exact phase-separation radius

`rho(P) = max_{a!=b mod Q} min{t>=0 : w_P(a+t) != w_P(b+t)}`.

Then, by definition and exhaustive minimization,

`H_U,steady*(P)=rho(P)`.

This is **not** Jacobsthal's function. Jacobsthal measures the maximum gap between integers coprime to a modulus; `rho(P)` measures the longest common prefix of two distinct cyclic shifts of the entire Boolean wheel word.

Exact exhaustive regressions:

| P | Q | relation H* | union rho(P) |
|---|---:|---:|---:|
| {2,3} | 6 | 1 | 3 |
| {2,3,5} | 30 | 3 | 13 |
| {2,3,5,7} | 210 | 5 | 37 |
| {2,3,5,7,11} | 2310 | 9 | 65 |
| {2,3,5,7,11,13} | 30030 | 11 | 137 |

Therefore the two steady future languages have the **same full state cardinality Q** but sharply different finite observation depths.

Targeted prior-art search found extensive literature on unary automata, wheel sieves, and Jacobsthal/primorial gap structure, but no direct source for this pairwise cyclic-shift separation statistic or these exact values. Novelty is therefore **unresolved, not claimed**.

Status: `ENTERPRISE_MATH_SPECIFIC_CANDIDATE / NOVELTY_UNVERIFIED`.

## 4. Segmented composition law

Let the segment operation be `T_B:L -> L+B` and let one segment observation reveal B consecutive sieve outputs. After D transitions, the observer has seen D+1 contiguous B-blocks, i.e. exactly `(D+1)B` consecutive symbols.

### T-R005A-S1 — exact segment/horizon composition

`C_{O,B}(D)=C_O((D+1)B-1)`.

If the full quotient stabilizes at `H_O*`, the sharp transition depth is

`D_O*(B)=ceil((H_O*+1)/B)-1`.

No better bound is possible: below this threshold the corresponding finite-horizon partition is not yet discrete; at or above it the observed block sequence contains a full distinguishing window.

This is the requested exact law connecting

`future horizon x segment execution x minimal state`.

Its generic block-observation content belongs to automata/continuation semantics; the prime-specific arithmetic input is `C_O(H)` and especially `rho(P)`.

## 5. Executable evidence

`experiments/r005a_prime_horizon_closure.py` is the closure harness.

The local research version was executed exhaustively and returned:

`R005-A closure regressions passed`.

It checks:

1. the exact `mu_R` and `mu_U` formulas for every nonempty subset of `{2,3,5,7,11}` against a periodicity oracle;
2. the prime-prefix identity `mu_U=p_max+1`;
3. the single-prime finite-horizon formula;
4. the steady relation phase-recovery theorem;
5. exact `rho(P)` regressions;
6. partition recursion against direct exhaustive future windows;
7. segmented composition against direct contiguous windows;
8. Pratt/Pocklington verifier-profile normalizations;
9. an ECPP verifier-language countermodel.

The repository version imports prime fixtures through canonical `enterprise_math.prime_toolkit.bounded_prime_enumeration`, retaining its `PrimeToolResult` and `CLASSICAL_BASELINE` provenance rather than rebuilding prime enumeration.

CI status: `CI_NOT_REQUIRED_FOR_RESEARCH`.

## 6. Verification-reflecting certificate state

The generic move

`certificate state = residual legality + observation + declared cost/resource behavior`

is not a new prime primitive. It is an A2/FQ-006-style action/quotient specialization, and complexity-sensitive proof/certificate verification has long-standing prior art.

The useful R005-A content is family-specific normalization under an explicitly declared verifier profile.

### Pratt efficient profile

Declare the verifier primitives:

- supplied child lookup;
- exact repeated division of `n-1` by a supplied child q;
- modular exponentiation;
- local equality/inequality checks;
- recursive child verification;
- **no unrestricted factorization**;
- **no witness search**;
- no arithmetic-trace replay.

For fixed subject n, a raw Pratt node normalizes to executable relation operands

`(a mod n, distinct child identities S, child references)`.

Under this profile the following serialize-only data can be deleted without changing legality, observation, or declared operation count:

- explicit valuation multiplicities: recover `v_q(n-1)` by repeated division;
- duplicate child references and child order;
- modular-exponentiation transcript.

The declared costs are then determined by `(n,a,S)`:

- exact divisions: `sum_{q in S} v_q(n-1)`;
- modular exponentiations: `1+|S|`;
- child lookups: `|S|`.

This is **profile-relative**. If supplied exponent vectors or exponentiation traces are declared as cheaper verifier primitives, deleting them need not be cost preserving.

Minimality must therefore be phrased as an operand theorem: the local order witness and child identities must remain available **up to verifier-equivalent recoding** unless the verifier is explicitly granted bounded reconstruction/search primitives. It is not a theorem that a literal text serialization is uniquely minimal.

### Pocklington attack

Pocklington/BLS-style certification needs only a sufficiently large known factored divisor `F | n-1`, not complete factor coverage.

If the certificate supplies distinct child primes S and the verifier may repeatedly divide `n-1` by each q in S, it can recover the full q-adic valuations `v_q(n-1)` and replace any supplied exponents `e_q <= v_q(n-1)` by the full valuations. The reconstructed

`F_full = product q^{v_q(n-1)}`

is at least as large as the serialized partial F, so a threshold such as `F>sqrt(n)` remains satisfied. The witness congruence/gcd conditions depend on the child prime q, not the serialized exponent.

Thus exponent serialization is unnecessary under this verifier profile. Unlike Pratt, the child support need not cover all of `n-1`.

This is an exact family-specific normalization, but it is not presented as new primality mathematics.

### ECPP attack

ECPP prevents promotion of the Pratt/Pocklington shape into a bare prime-support DAG theorem. A parent step uses elliptic-curve relation operands: chosen curve data, a point, and order information relating the parent candidate to the recursive prime obligation.

Group-operation traces can be recomputed, but deleting the parent-local curve/point/order operands makes the corresponding verifier actions illegal unless the verifier profile explicitly includes curve selection/search/reconstruction.

The stable descriptive schema across the three families is therefore

`obligation DAG + reconstruction-irreducible local relation operands + verifier profile`.

This schema is useful, but targeted proof-system prior art and existing A2/FQ-006 semantics prevent claiming it as a new universal/minimal mother theorem.

## 7. Compiler branch closure

Third-round requirement: retain this branch only if a prime-specific residual decomposition appears.

Result:

`NO_PRIME_SPECIFIC_RESIDUE_FOUND`.

No exact evidence was found for any of:

- a canonical product factorization `c_legality x c_arithmetic x c_repair`;
- a finite universal primitive repair basis produced by prime algorithms;
- a sharp prime-specific residual-state count;
- an arithmetic decomposition not already representable inside the generic continuation quotient.

Adaptive Lucas/Selfridge, AKS, and Pocklington remain meaningful specializations, but they do not justify a separate compiler mother theory in R005-A.

Route the generic theorem back to its existing owner and close the prime compiler subbranch.

## 8. Targeted prior-art attack

Primary/authoritative sources used in this closure round:

- Jonathan P. Sorenson, *An Introduction to Prime Number Sieves*, University of Wisconsin CS Technical Report 909 (1990). The segmented wheel sieve explicitly carries a per-prime previous-interval strike/factor state; segmented continuation state is therefore old implementation mathematics.
- Marek Chrobak, *Finite automata and unary languages*, Theoretical Computer Science 47 (1986), 149-158, DOI `10.1016/0304-3975(86)90142-8`. Unary ultimately-periodic/minimal-automata machinery attacks generic quotient novelty.
- Vaughan R. Pratt, *Every Prime Has a Succinct Certificate*, SIAM Journal on Computing 4(3) (1975), 214-220, DOI `10.1137/0204018`.
- John Brillhart, D. H. Lehmer, J. L. Selfridge, *New primality criteria and factorizations of 2^m +/- 1*, Mathematics of Computation 29(130) (1975), 620-647.
- Benjamin Grégoire, Laurent Théry, Benjamin Werner, *A Computational Approach to Pocklington Certificates in Type Theory*, FLOPS 2006, LNCS 3945, 97-113, DOI `10.1007/11737414_8`. This is direct prior art for computation-aware certificate checking.
- A. O. L. Atkin, François Morain, *Elliptic curves and primality proving*, Mathematics of Computation 61(203) (1993), 29-68, DOI `10.1090/S0025-5718-1993-1199989-X`.
- Stephen A. Cook, Robert A. Reckhow, *The Relative Efficiency of Propositional Proof Systems*, Journal of Symbolic Logic 44(1) (1979), 36-50, DOI `10.2307/2273702`. Proof-system efficiency/cost sensitivity is established prior art.
- Jacobsthal/primorial gap literature was searched specifically to attack `rho(P)`. It concerns runs/gaps of reduced residues, not the maximum agreement prefix between two distinct cyclic wheel shifts. No direct equivalence was located in the targeted search.

## 9. EXTERNAL PRIME CAPABILITY PACKET v3 routing

| Capability/result | Prior-art status | Exact reconstruction/result | Executable | Route | Theorem owner |
|---|---|---|---|---|---|
| `ActualSieveTransientQuotient` | p^2 activation classical; ultimately-periodic minimization classical | exact `mu_R`, `mu_U`, `Q+mu` state counts | yes | `PROMOTE_TO_TOOLKIT` | R005-A specialization |
| `FiniteHorizonSieveQuotient` | automata partition refinement prior art | exact `C_O(H)` recursion and stabilization oracle | yes | `PROMOTE_TO_TOOLKIT` | R005-A specialization / generic recursion existing theory |
| `WheelPhaseSeparationRadius` | no direct match located; Jacobsthal is different | exact definition `rho(P)=H_U,steady*`; bounded values checked | yes | `KEEP_AS_R005A_WIP` | R005-A |
| `SegmentHorizonComposition` | generic block-observation semantics prior art/existing EM | `C_{O,B}(D)=C_O((D+1)B-1)` | yes | `RETURN_TO_EXISTING_OWNER` | A2/FQ-006 for mother law; R005-A supplies sieve instance |
| `PrattVerifierProfileNormalizer` | Pratt certificate prior art; verifier complexity prior art | profile-relative deletion/reconstruction theorem | yes toy/exact local | `KEEP_AS_R005A_WIP` | R005-A specialization |
| `PocklingtonValuationElision` | Pocklington/BLS + formal certificate computation prior art | full q-adic valuations recoverable; serialized exponents unnecessary under repeated-division profile | yes toy/exact local | `PRIOR_ART_ONLY` | classical / R005-A regression |
| `ECPPRelationOperandCountermodel` | ECPP relation structure prior art | bare child obligation is insufficient for declared group-verifier actions | verifier-language toy | `PRIOR_ART_ONLY` | classical ECPP / R005-A test |
| `VerificationReflectingCertificateQuotient` | proof-system complexity + existing EM action quotient | generic cost-aware residual quotient | not needed as new tool | `RETURN_TO_EXISTING_OWNER` | A2/FQ-006 |
| `PrimeCompilerResidual` | generic continuation theory already owns mother structure | no prime-specific factorization/state theorem found | negative result | `CLOSE_BRANCH` | R005-A branch closed; generic owner A2/FQ-006 |

`PROMOTE_TO_TOOLKIT` here is a recommendation to Driver/R005-C governance, **not an automatic write into the canonical Prime Toolkit**.

## 10. Final answers required by Driver

### 1. Did finite-horizon/transient sieve produce a genuinely new exact quotient theorem?

**Yes as an exact Enterprise specialization, no justified claim of new underlying sieve/automata mathematics.**

The sharp surviving result is the pair

`mu_R(P)=p_max^2-p_max+1`,

`mu_U(P)=1+max_p p*r_P(p)`,

with prime-prefix collapse `mu_U=p_max+1`, plus the exact finite-horizon quotient chain and segment-depth law. The constituent facts root in classical sieve activation and automata minimization, but the comparison exposes a real state/precision resource boundary not visible in the usual implementation presentation.

### 2. Did verifier/cost certificate state produce a stable cross-family mother structure?

**No new mother theorem.**

The stable descriptive schema is `obligation DAG + reconstruction-irreducible local relation operands + verifier profile`, but its generic content belongs to action/quotient and proof-system complexity. Pratt and Pocklington yield useful exact profile-relative normal forms; ECPP blocks the stronger bare-support-DAG generalization.

### 3. Is the compiler branch fully absorbed by A2/FQ-006?

**Yes.** `NO_PRIME_SPECIFIC_RESIDUE_FOUND`; close the R005-A compiler subbranch.

### 4. What is mature enough to recommend for Prime Toolkit?

Recommend two exact, bounded, status-preserving research analyzers:

1. transient sieve future quotient / preperiod calculator with exhaustive oracle;
2. finite-horizon sieve partition + segment-depth explorer.

Keep `rho(P)` mathematically in R005-A WIP until novelty/properties are better understood, though the explorer can support it.

### 5. What is prior-art reconstruction?

- per-prime segmented strike continuation state;
- generic unary/ultimately-periodic quotient minimization;
- generic finite automaton refinement;
- Pratt/Pocklington/ECPP primality-certificate mathematics;
- proof-system efficiency/cost sensitivity;
- generic cost-aware residual continuation quotient.

## 11. Closure

The three apparent first-round interfaces have now reduced to:

1. **sieve** — survives as an exact transient/horizon Enterprise specialization, with one unresolved prime-specific radius `rho(P)`;
2. **certificate** — survives only as family-specific verifier-profile normalization, not a universal new theorem;
3. **compiler** — fully de-duplicates into existing A2/FQ-006 and closes.

Accordingly, the answer to the third-round closure question is:

**Mature prime tools did not merely receive new names, because the replanting exposed exact finite-horizon and activation-transient resource structure. But after aggressive de-duplication there is still no justified new generic Foundation theorem. The only genuinely unresolved prime-specific mathematical candidate remaining is the Boolean wheel phase-separation radius and its arithmetic behavior.**
