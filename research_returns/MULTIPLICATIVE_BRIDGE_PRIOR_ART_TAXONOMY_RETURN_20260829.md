# Multiplicative Bridge Prior-Art Taxonomy — Research Return

Task-ID: `RS-MULTIPLICATIVE-BRIDGE-PRIOR-ART-TAXONOMY`  
Publication: `TP2-B0247164A23E5E39FF08`  
Researcher-ID: `EM-MBGP0-8C4F12`  
Execution branch: `research/multiplicative-bridge-prior-art-em-mbgp0-8c4f12`  
Date: `2026-08-29`  
Verdict: `SUCCESS / PRIOR_ART_BOUNDARY_CLASSIFIED`

## 0. Executive verdict

The broad bridge slogan

> apply one factor-blind public process to `N=pq`, let the hidden `p`- and `q`-channels behave differently, force a one-sided collapse/collision/singularity, and recover a factor by `gcd`

is **not a novel factorization mechanism**. It is already a common mechanism-level normal form for several mature families:

- Pollard `p-1`: one hidden multiplicative-group channel is annihilated first;
- Williams `p+1`: the same pattern in a Lucas/quadratic carrier;
- ECM: one hidden elliptic-curve channel is killed first, exposed as inversion failure/nonunit;
- Pollard rho: one hidden channel collides before the other;
- congruence-of-squares methods: hidden CRT square-root signs split and a gcd detects the split;
- cyclotomic methods: higher algebraic carriers generalize the same order-annihilation idea and explicitly subsume `p-1`, `p+1`, and related low-degree cases.

Therefore a future BRC result may legitimately be new mathematics at the level of **coupling, survivor classification, conservation law, or bridge-existence structure**, but it may not claim a new factorization bridge merely because it is factor-blind, splits hidden CRT behavior, or ends in a gcd/nonunit witness.

The strongest prior-art-safe novelty target is narrower:

`IRREDUCIBLE_CROSS_CHANNEL_COUPLING OR NEW_COLLAPSE_INVARIANT OR NEW_ENDPOINT_LAW`

and, for an algorithmic claim, that surviving difference must also remain factor-blind and carry a quantified success/total-cost analysis.

---

## 1. Mechanism normal form

For this audit, a factorization bridge family is normalized as

\[
\mathcal B_N=(C_N,\{\rho_r\},I,A,K,E,\mathsf{Cost}),
\]

where:

1. `C_N` is the public ambient carrier over the composite input `N`;
2. `rho_r` is the hidden reduction/projection into a prime channel for each `r|N`;
3. `I` is the factor-dependent channel invariant (order, smoothness, collision time, sign, singularity, etc.);
4. `A` is the public factor-blind action/dynamics;
5. `K` is the useful one-sided collapse/collision predicate;
6. `E` is the endpoint extraction map;
7. `Cost` records the success regime and total work, including witness generation rather than only the final gcd.

This is a **mechanism taxonomy**, not a new factoring algorithm.

### Algebraic subtraction guard

Expressions such as

\[
\gcd(x-y,N)
\]

are admissible here only because `x-y=0 mod p` is an algebraic equality/collision predicate. No use is made of `|x-y|` as number-line distance, locality, nearness, or bridge quality.

---

## 2. P0 — Six-dimensional mechanism taxonomy

| Family | Ambient carrier | Hidden invariant | Public factor-blind action | One-sided collapse/collision | Extraction | Cost/success regime |
|---|---|---|---|---|---|---|
| Pollard `p-1` | `(Z/NZ)^*`, hidden `F_p^* x F_q^*` channels | order/exponent dividing `p-1`, `q-1`; smoothness | compute `a^M mod N` | `a^M=1 mod p`, but not mod `q` | `gcd(a^M-1,N)` | succeeds when a target `p-1` is sufficiently smooth/divides `M`, without simultaneous annihilation |
| Williams `p+1` | Lucas/quadratic algebra / norm-one-type carrier | Lucas rank/order controlled by `p-(D/p)`, targeting `p+1` in nonsquare channel | public Lucas multiple/index `M` | standard Lucas identity defect vanishes mod one prime only | gcd of the defect, schematically `gcd(V_M-2,N)` | conditional on suitable parameter/nondegeneracy conditions and smooth target `p+1`/Lucas order |
| ECM | random elliptic curve over `Z/NZ`, hidden `E(F_p),E(F_q)` | random curve/point order in each prime channel | same scalar multiplication `[M]P` | identity in one channel only; composite-ring arithmetic hits a noninvertible denominator/projective coordinate | gcd of nonunit coordinate/denominator with `N` | success governed by smooth hidden curve/point order; original expected-time analysis is conjectural/heuristic in the cited sense |
| Pollard rho | iterated map on `Z/NZ`, hidden finite dynamical systems mod `p`,`q` | orbit/cycle/collision time | same public iterate `f` | `x_i=x_j mod p` but not mod `q` | `gcd(x_i-x_j,N)` or batched difference product | probabilistic collision regime; Pollard describes apparent `O(sqrt(p))` arithmetic work |
| Congruence of squares (Dixon/QS-type endpoint) | square classes / relation lattice leading to residues mod `N` | CRT sign vector of square roots | construct `x^2=y^2 mod N` | opposite hidden sign choices across prime channels | `gcd(x-y,N)` and `gcd(x+y,N)` | extraction deterministic once nontrivial congruence obtained; relation-collection cost is algorithm-specific |
| Cyclotomic extension methods | algebraic/cyclotomic carrier associated to `Phi_k` | divisibility/order governed by `Phi_k(p)` | universal algebraic construction from a multiple of `Phi_k(p)` | one hidden algebraic channel annihilates/singularizes | factor split via construction, ultimately a nonunit/gcd-type endpoint | Bach–Shallit give a universal construction; expected-time statement carries a GRH condition |
| Generic nonunit/zero-divisor endpoint | `Z/NZ` or finite algebra over it | witness zero/nonunit in one prime channel but not another | any factor-blind witness-generation process | public `z` becomes nontrivial zero-divisor/nonunit | `gcd(z,N)` or equivalent norm/resultant then gcd | endpoint cheap once witness exists; witness generation remains the real cost |

### First boundary

The following pattern is mature prior art:

\[
\text{same public action}
\to
\text{different hidden prime-channel behavior}
\to
\text{one-sided algebraic defect}
\to
\gcd(\text{defect},N).
\]

Changing terminology from `order`, `collision`, `inversion failure`, `sign split`, or `zero divisor` to `bridge` does not create a new mechanism.

---

## 3. P1 — Exact CRT-channel formulations

### 3.1 Pollard `p-1`: exact one-sided annihilation lemma

Let `N=pq` with distinct primes and let `gcd(a,N)=1`. For any public exponent `M`, set

\[
z=a^M-1\pmod N.
\]

If

\[
a^M\equiv 1\pmod p,\qquad a^M\not\equiv 1\pmod q,
\]

then

\[
\gcd(z,N)=p.
\]

This is exact and elementary: `p|z`, `q∤z`. Pollard's method arranges the first condition by choosing `M` divisible by enough prime powers that a smooth `p-1` divides `M`.

**Bridge reading:** the public action is identical in both CRT channels; the hidden group exponents differ; one channel reaches the identity first; gcd reads out the endpoint.

### 3.2 Williams `p+1`: exact endpoint, standard Lucas hypothesis upstream

Williams replaces the multiplicative-group carrier by a Lucas/quadratic carrier. Under the standard discriminant/nondegeneracy hypotheses, the relevant prime-channel Lucas order divides `p-(D/p)`; when `(D/p)=-1`, this gives the `p+1` route.

For any public Lucas defect `Delta_M` produced by the method, the endpoint implication is exact:

\[
\Delta_M\equiv0\pmod p,\qquad \Delta_M\not\equiv0\pmod q
\Longrightarrow
\gcd(\Delta_M,N)=p.
\]

In the common `Q=1` presentation the defect is schematically `V_M-2`. Exact implementation details include parameter and exceptional-case conditions, so this return does not erase them into an overbroad theorem.

**Bridge reading:** different carrier, same one-sided order-annihilation architecture.

### 3.3 ECM: exact hidden-channel endpoint

Let a public elliptic-curve model and point reduce nonsingularly modulo hidden primes `p,q|N`. Scalar multiplication by public `M` projects to the same multiplication in `E(F_p)` and `E(F_q)`.

If the `p`-channel point is killed by `M` but the `q`-channel is not, composite-modulus group arithmetic can expose a coordinate/denominator `z` satisfying

\[
z\equiv0\pmod p,\qquad z\not\equiv0\pmod q.
\]

Then exactly

\[
\gcd(z,N)=p.
\]

Lenstra explicitly presents ECM as replacing the group used by Pollard `p-1` with the group of points of a random elliptic curve. The important novelty of ECM is not “hidden channels differ then gcd”; that bridge skeleton was already present. It changes the distribution of the hidden group order by randomizing the curve.

### 3.4 Pollard rho: exact one-sided collision lemma

For a public iterate `x_{i+1}=f(x_i) mod N`, if

\[
x_i\equiv x_j\pmod p,
\qquad
x_i\not\equiv x_j\pmod q,
\]

then

\[
\gcd(x_i-x_j,N)=p.
\]

Pollard's 1975 paper explicitly batches such differences in a product before taking a gcd.

**Bridge reading:** the hidden invariant is collision time/orbit structure, not group-order smoothness, but the one-sided collision + nonunit + gcd endpoint is classical.

### 3.5 Congruence of squares: exact hidden sign split

For odd squarefree `N=pq`, suppose

\[
x^2\equiv y^2\pmod N.
\]

Each hidden prime channel chooses a sign:

\[
x\equiv \pm y\pmod p,
\qquad
x\equiv \pm y\pmod q.
\]

If the signs differ across the two channels, e.g.

\[
x\equiv y\pmod p,
\qquad
x\equiv -y\pmod q,
\]

then

\[
\gcd(x-y,N)=p,
\qquad
\gcd(x+y,N)=q.
\]

Thus “one hidden channel collapses to equality while the other occupies the opposite root” is also mature prior art.

---

## 4. Cyclotomic subsumption boundary

Bach and Shallit's 1989 construction is especially important for novelty control. Their paper states that, given a multiple of `Phi_k(p)`, a universal algebraic-number-theory construction can split a composite containing `p`; it explicitly subsumes earlier cases based on

- `X-1` (`p-1`),
- `X+1` (`p+1`),
- `X^2+1`,
- `X^2 +/- X + 1`.

Therefore this implication is frozen for future bridge claims:

`HIGHER_ALGEBRAIC_CARRIER + ORDER_ANNIHILATION + GCD_ENDPOINT != AUTOMATIC_NEW_BRIDGE_FAMILY`.

A BRC rank-two or higher-rank carrier must be tested for reducibility to a cyclotomic/algebraic order-annihilation construction, not merely compared with Pollard `p-1` in its original one-dimensional presentation.

---

## 5. P2 — Bridge-equivalence criterion

### Definition: endpoint bridge equivalence

Let

\[
\mathcal B=(C,\rho,I,A,K,E),
\qquad
\mathcal B'=(C',\rho',I',A',K',E')
\]

be public composite-input bridge families.

Call them **exactly bridge-equivalent** if there is a uniformly and efficiently computable family of factor-blind carrier maps `phi_N` (bijective on the relevant state subspaces for exact equivalence) with prime-channel maps `phi_r` such that:

1. **hidden projection compatibility**
   \[
   \rho'_r\circ\phi_N=\phi_r\circ\rho_r;
   \]
2. **action conjugacy/semiconjugacy**
   \[
   \phi_N\circ A=A'\circ\phi_N;
   \]
3. **collapse preservation**
   \[
   K(s)\Longleftrightarrow K'(\phi_N(s));
   \]
4. **endpoint preservation**: the nontrivial factor set returned by `E(s)` equals that returned by `E'(phi_N(s))`, up to swapping complementary factors/units;
5. **no hidden-factor leakage**: computing `phi_N`, the public action, or the compared invariant may not use `p`, `q`, or an oracle equivalent to already factoring `N`.

If the map is not a literal conjugacy but the candidate instantiates the same known annihilation/collision/nonunit template with the same endpoint law, classify it as `MECHANISM_SUBSUMED` rather than `EXACT_EQUIVALENT`.

### Consequence

If the carrier, collapse invariant and extraction map are equivalent in this sense, a candidate may still offer:

- a better representation,
- a unifying language,
- a better implementation,
- a different parameter distribution,
- or a new theorem about success probability,

but it must not claim a new **bridge family** merely from the repackaging.

---

## 6. BRC_NOVELTY_GUARD_V1

A future BRC/CBRC factorization claim must be rejected as a new bridge family if its only distinguishing statements are any combination of:

1. the public action does not know `p,q`;
2. hidden CRT channels behave differently;
3. one channel reaches identity/order collapse while another does not;
4. one channel collides while another does not;
5. a residue/coordinate/norm becomes a nonunit or zero divisor;
6. the endpoint is `gcd(witness,N)` or an equivalent norm/resultant followed by gcd;
7. a higher algebraic/cyclotomic carrier replaces `(Z/NZ)^*` but preserves the annihilation/extraction skeleton;
8. a nontrivial square-root/sign split is renamed a bridge.

### Minimum surviving novelty test

At least one of the following must survive an explicit reduction attempt:

**N1 — irreducible coupling.** The dynamics genuinely couple two or more hidden channels and are not computably semiconjugate/diagonalizable into independent per-channel actions of a known family.

**N2 — new collapse invariant.** The success event is not reducible to group/Lucas/cyclotomic order annihilation, ordinary orbit collision, CRT sign split, or generic nonunit/zero-divisor formation.

**N3 — new endpoint law.** Factor recovery is not equivalent to a gcd/nonunit/norm/resultant extraction already standard in algebraic factorization.

For an **algorithmic** novelty claim, `N1/N2/N3` is still insufficient unless the mechanism is public and factor-blind and comes with a quantified success regime and total cost. Hiding expensive factorization inside bridge construction, representation change, or verifier preprocessing fails the guard.

### Four output labels

- `EXACT_EQUIVALENT` — computable conjugacy/equivalence preserves channels, action, collapse, and endpoint;
- `MECHANISM_SUBSUMED` — same established annihilation/collision/nonunit template, though not literally conjugate;
- `PARTIAL_OVERLAP` — shares structural ingredients but no endpoint reduction/factorization semantics is established;
- `NOVELTY_GAP_NOT_REDUCED` — at least one essential ingredient has resisted the listed reductions. This is a **research gap label**, not a novelty theorem.

---

## 7. P3 — Current BRC/CBRC novelty gaps and falsification tests

### Gap A — balanced two-channel conservation

**Potentially distinct:** a conservation law constraining two channels jointly, rather than two independent dynamics whose outcomes are compared after the fact.

**Prior-art falsification test:** construct a factor-blind change of variables that diagonalizes the operator into independent channel actions. If each component reduces to known order/collision/cyclotomic dynamics, the “balanced bridge” is only a coupled presentation and is `MECHANISM_SUBSUMED`.

### Gap B — operator-survivor existence without endpoint

**Potentially distinct as theory:** an exact predicate deciding whether an operator admits a balanced support-splitting survivor can be mathematically new even when it does not factor `N`.

**Prior-art falsification test:** do not compare only vocabulary. Ask whether the survivor predicate is computably equivalent to a classical group-order/smoothness or cyclotomic admissibility predicate on the same effective carrier.

**Important ceiling:** even if distinct, a bridge-existence classifier is not an endpoint-recovery algorithm.

### Gap C — rank-two support coupling

**Potentially distinct:** simultaneous constraints on two support directions that cannot be represented as one classical channel plus a passive parameter.

**Prior-art falsification test:** test Smith/CRT/cyclotomic decomposition, invariant-subspace splitting, and action semiconjugacy. If the rank-two operator decomposes into two known one-channel annihilators/colliders, rank alone is not novelty.

### Gap D — genuinely different endpoint recovery

This is the strongest possible algorithmic gap.

**Prior-art falsification test:** try to rewrite the endpoint as

\[
\gcd(F(\text{public state}),N),
\]

or as an equivalent norm/resultant/nonunit computation. If successful and the upstream collapse is also known, the endpoint is not new.

If no such reduction exists, the candidate still needs a proof that the new endpoint is factor-blind, correct, and not secretly performing equivalent factorization work.

---

## 8. Mapping the accepted CBRC F3R2 result

The accepted Driver review for F3R2 freezes the exact survivor predicate for the two-slot carrier:

\[
\det(A)=\pm1,
\quad
\det(D)\ne0\pmod3,
\quad
\gcd(|a|,|d|)>1,
\quad
\gcd(|b|,|c|)>1.
\]

It also freezes that the support-splitting strata cover the full free survivor set and that membership reduces to two Euclidean gcd tests inside the ambient automorphism class.

This audit does **not** re-prove or re-review that theorem. It asks only what prior-art bridge class it occupies.

### Classification: `PARTIAL_OVERLAP`

At its accepted scope, F3R2 is an exact **operator-survivor / support-splitting classifier**. It does not yet provide all of the following:

- a public semiprime input `N=pq` whose factors are hidden;
- factor-blind BRC dynamics projected into hidden `p` and `q` CRT channels;
- a public one-sided collision/singularity/nonunit witness modulo `N`;
- an endpoint map recovering `p` or `q`;
- a success probability/regime and total-cost model.

The coefficient gcds in the survivor theorem therefore must **not** be confused with a factorization endpoint gcd. They certify support structure of an operator; they do not presently recover a hidden factor of a supplied `N`.

### Current legally supportable novelty ceiling

Without further prior-art work on the exact BRC carrier, the safe statement is:

> F3R2 supplies a project-specific exact survivor/support-splitting classification that is relevant to bridge-existence semantics.

The following statements are **not supported** by F3R2 alone:

- “new factor-blind factorization bridge”;
- “new CRT-channel collapse factorization algorithm”;
- “new zero-divisor endpoint extraction”;
- “new factoring complexity class.”

---

## 9. P4 — Literature ledger and evidence discipline

### [S1] Pollard 1974 — `p-1`

J. M. Pollard, **Theorems on factorization and primality testing**, *Mathematical Proceedings of the Cambridge Philosophical Society* 76 (1974), 521–528.  
DOI: `10.1017/S0305004100049252`.

Use here: primary provenance for Pollard `p-1` / order-smoothness factorization.  
Do not infer: no unconditional globally fast factoring theorem follows from the conditional smoothness success regime.

### [S2] Williams 1982 — `p+1`

H. C. Williams, **A p+1 method of factoring**, *Mathematics of Computation* 39 (1982), 225–234.  
DOI: `10.1090/S0025-5718-1982-0658227-7`.

Use here: primary `p+1`/Lucas carrier and its analogy with `p-1`.  
Do not infer: the schematic Lucas defect used in the mechanism table erases no implementation-specific exceptional cases.

### [S3] Lenstra 1987 — ECM

H. W. Lenstra Jr., **Factoring integers with elliptic curves**, *Annals of Mathematics* 126 (1987), 649–673.  
DOI: `10.2307/1971363`.

Use here: ECM replaces Pollard's multiplicative-group carrier by random elliptic-curve groups; primary expected-time discussion.  
Do not infer: the source's conjectural expected-time statement is not promoted to an unconditional theorem.

### [S4] Pollard 1975 — rho

J. M. Pollard, **A Monte Carlo method for factorization**, *BIT* 15 (1975), 331–334.  
DOI: `10.1007/BF01933667`.

Use here: public iteration, product of differences, gcd extraction, and the source's “apparently `O(p^{1/2})` arithmetic operations” performance description.  
Do not infer: this wording is not a deterministic worst-case theorem.

### [S5] Pomerance 1984 — quadratic sieve

Carl Pomerance, **The Quadratic Sieve Factoring Algorithm**, EUROCRYPT 1984, LNCS, pp. 169–182.  
DOI: `10.1007/3-540-39757-4_17`.

Use here: representative primary source for the modern congruence-of-squares relation-collection family.  
Do not infer: no one asymptotic formula in this return is assigned to all Dixon/QS/NFS-like congruence-of-squares mechanisms.

### [S6] Bach–Shallit 1989 — cyclotomic family

Eric Bach and Jeffrey Shallit, **Factoring with Cyclotomic Polynomials**, *Mathematics of Computation* 52 (1989), 201–219.  
DOI: `10.1090/S0025-5718-1989-0947467-1`.

Use here: universal `Phi_k` construction and explicit subsumption of `p-1`, `p+1`, and several low-degree cyclotomic methods.  
Do not infer: the paper's expected-time statement is retained with its generalized-Riemann-hypothesis condition.

---

## 10. Tool-reuse resolution

Current project inventory was checked before creating a reusable guard.

- `domain.prime_toolkit` already covers bounded exact prime/factor witnesses and should be reused if finite examples later need factor verification.
- `collision.common_collapse_inversion` provides useful internal collision vocabulary.
- No current reusable method entry provides a source-backed **factorization mechanism-equivalence audit** or a **BRC prior-art novelty guard**.

Resolution:

`COMPOSE_APPLIED_WITH_SCOPE_GAP`.

This task adds a taxonomy/guard, **not** another factorization engine.

---

## 11. Hard-target disposition

### P0 Mechanism taxonomy

`PASS` — seven mechanism/meta-families classified in the required dimensions.

### P1 CRT-channel formulation

`PASS` — exact hidden-channel formulations supplied for `p-1`, rho, congruence of squares; exact endpoint formulations with standard upstream hypotheses supplied for `p+1` and ECM.

### P2 Bridge-equivalence criterion

`PASS` — hidden-projection-compatible computable conjugacy/semiconjugacy + collapse preservation + endpoint preservation + no factor leakage.

### P3 Novelty gaps

`PASS` — four explicit possible gaps with a falsification test for each.

### P4 Literature ledger

`PASS` — primary/authoritative sources recorded with use scope and non-inference guards.

---

## 12. Final BRC novelty boundary

Freeze the following guard for downstream review:

`FACTOR_BLIND + HIDDEN_CRT_ASYMMETRY + ONE_SIDED_COLLAPSE + GCD_ENDPOINT = PRIOR_ART_SKELETON`

and

`HIGHER_RANK_OR_BALANCED_NAME != NOVELTY`.

A future BRC bridge can exceed this boundary only by demonstrating an irreducible new coupling/collapse/extraction component that survives computable reduction to the established families above.

### Recommended downstream audit order

1. Attempt to decompose the BRC operator into independent hidden-channel actions.
2. Test each action against order/cyclotomic annihilation and collision families.
3. Normalize every proposed endpoint to a nonunit/norm/resultant/gcd form if possible.
4. If a component survives, only then measure factor-blind success and total cost.
5. Keep “new structural bridge theory” separate from “new factorization algorithm.”

No claim of a new factoring algorithm or competitive factoring benchmark is made by this return.
