# Enterprise BRC Half-Coupling p-adic All-Prime Proof — Research Return

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF`  
Publication: `TP2-7A652D67B412693680E0`  
Claim: `chatgpt-ebp2-20260827-0822`  
Researcher-ID: `EM-EBP2-7D2C2F`  
Execution record: `ER-D4103A95B79DB59189AC`  
Execution branch: `research/enterprise-brc-half-padic-all-prime-proof-em-ebp2-7d2c2f`  
Date: `2026-08-27`

## 0. Frozen verdict

Primary task verdict:

`PROOF_NOT_CLOSED`

Hard-target disposition:

`ENTERPRISE_BRC_HALF_COUPLING_PADIC_MOD_P3_ALL_PRIMES_PROVED_OR_REFUTED = NOT_CLOSED`

The target has **not** been refuted. Exact regression continues to support it strongly. However, this execution did not obtain a complete all-prime proof, and the literature audit did not locate a proved theorem whose verified hypotheses specialize to the exact all-prime weighted truncation.

The strongest durable progress is:

1. the target is identified exactly as the `a=1` specialization of Zhi-Wei Sun's Conjecture A14(ii), so it is prior conjectural arithmetic rather than a new Enterprise theorem;
2. the Beukers modular-form framework matches the exact coefficient family and the CM value `1/216`, but the relevant order-3 theorem has a **split-prime hypothesis** in `Q(sqrt(-6))` and therefore cannot by itself close all primes;
3. a direct exact `p`-adic valuation stratification is proved for every summand;
4. that stratification gives a rigorous no-go to the tempting "the whole tail vanishes modulo p^3" shortcut: only the last third vanishes termwise, while two middle layers survive;
5. two independent exact evaluators agree on every prime `5 <= p <= 199`, and the recurrence evaluator verifies the target for all `1227` primes `5 <= p <= 9973`; this remains finite regression only;
6. the next proof frontier is narrowed to an **inert finite-Clausen derivative bridge** controlling the surviving middle layers.

No Foundation, BRC-physical, or packet/path promotion is made by this return.

---

## 1. Exact target

For a prime `p>3`, let

\[
A_n=\binom{2n}{n}^2\binom{3n}{n}
=\frac{(2n)!(3n)!}{(n!)^5}
\]

and

\[
S_p=\sum_{n=0}^{p-1}(6n+1)\frac{A_n}{216^n}
\quad\in \mathbf Z/(p^3)\mathbf Z.
\]

The target is

\[
\boxed{
S_p\equiv p\left(\frac{-3}{p}\right)\pmod{p^3}
}
\tag{T}
\]

for every prime `p>3`.

Since `p>3`,

\[
\left(\frac{-3}{p}\right)=\left(\frac p3\right),
\]

so the right side is `+p` for `p≡1 (mod 3)` and `-p` for `p≡2 (mod 3)`.

---

## 2. Prior-art audit

### 2.1 Sun A14(ii): the target is already an exact conjecture

Source:

- Zhi-Wei Sun, *Open Conjectures on Congruences*, arXiv:0911.5665, Conjecture A14(ii).

A14(ii) contains

\[
\frac1{p^a}
\sum_{k=0}^{p^a-1}
(6k+1)\frac{\binom{2k}{k}^2\binom{3k}{k}}{6^{3k}}
\equiv
\left(\frac{p^a}{3}\right)
\pmod{p^2}.
\]

At `a=1`, because `6^3=216`, multiplication by `p` gives exactly `(T)`.

Classification:

`EXACT_PRIOR_CONJECTURE`

Therefore any proof obtained here would be a proof of a pre-existing arithmetic conjecture; the Enterprise blind experiment supplied independent finite evidence but did not originate the congruence.

### 2.2 Beukers: exact coefficient/CM match, but split-prime scope

Source:

- Frits Beukers, *Supercongruences using modular forms*, arXiv:2403.03301, current revised version audited on 2026-08-27.

The order-3 level-3 example has coefficient sequence

\[
g_n=\frac{(3n)!(2n)!}{(n!)^5}=A_n
\]

and the CM point

\[
\alpha=\frac{\sqrt{-6}}3
\]

satisfies

\[
t(\alpha)=\frac1{216}.
\]

Thus the unweighted truncated modular series is exactly the same `A_n/216^n` coefficient system as `(T)`.

The relevant Beukers theorem has the derivative combination

\[
F_p(t(\alpha))-\delta(\alpha)^{-1}\theta F_p(t(\alpha))
\pmod{p^3},
\]

which would become the required

\[
F_p+6\theta F_p
\]

if one proves exactly

\[
\delta(\alpha)=-\frac16.
\]

An independent high-precision `q`-expansion audit performed in this execution gives `delta(alpha)=-1/6` to high precision, but **that numerical identity is not promoted as proof here**. A standalone specialization would still need the exact symbolic derivation of `delta(alpha)` and the exact identification of the theorem's character factor with `(p/3)`.

More importantly for the all-prime task, the cited theorem requires `p` to split in `Q(sqrt(-6))`. For primes `p>3`:

- split classes modulo `24`: `1,5,7,11`;
- inert classes modulo `24`: `13,17,19,23`.

Hence the framework is intrinsically insufficient, as cited, for the four inert residue classes.

Classification:

`PROVED_GENERAL_FRAMEWORK / ALL-PRIME SPECIALIZATION NOT ESTABLISHED`

No `KNOWN_THEOREM_SPECIALIZATION_PROVED` verdict is claimed.

### 2.3 Shvets 2026: same mixed CM backbone, different sequence

Source:

- Alex Shvets, *Split-prime supercongruence at the mixed CM point (1/6,1/3;1)*, arXiv:2605.19773.

This paper works with the mixed hypergeometric pair `(1/6,1/3;1)` and proves a split-prime supercongruence for a symmetric-cube coefficient sequence, together with an inert obstruction.

That is structurally relevant because the exact Clausen factorization below reduces our order-3 series to the square of the same mixed `2F1`. But Shvets' theorem is **not** the derivative-weighted `p`-term truncation `(T)`, so it is not imported as a proof.

Classification:

`RELATED_PROVED_SPLIT-PRIME RESULT / DIFFERENT TARGET`

### 2.4 Literature conclusion

The scoped 2026-08-27 audit located:

- the exact prior conjecture;
- a modular framework that matches the coefficient system and CM point but is split-prime scoped;
- a 2026 result at the same mixed CM hypergeometric backbone but for a different coefficient sequence.

It did **not** locate a proved all-prime theorem whose checked hypotheses imply `(T)`.

This is an audit statement, not a proof that no such paper exists.

---

## 3. Hypergeometric reduction

The exact identity

\[
A_n
=
108^n
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}
\]

gives

\[
\frac{A_n}{216^n}
=
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}
\left(\frac12\right)^n.
\]

Let

\[
F(z)=
{}_3F_2\!\left(
\begin{matrix}
1/3,\,1/2,\,2/3\\
1,\,1
\end{matrix};z
\right).
\]

Then

\[
S_p=
\left[
(1+6\theta)
\sum_{n=0}^{p-1}
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}z^n
\right]_{z=1/2},
\qquad
\theta=z\frac d{dz}.
\tag{3.1}
\]

Clausen's identity, with `a=1/6`, `b=1/3`, gives formally

\[
\boxed{
F(z)=
{}_2F_1\!\left(
\begin{matrix}
1/6,\,1/3\\
1
\end{matrix};z
\right)^2.
}
\tag{3.2}
\]

This explains why the mixed `(1/6,1/3;1)` CM point arises naturally.

However, `(3.2)` does **not** allow one simply to square the value of a degree-`p-1` truncated `2F1`: the square contains convolution coefficients in degrees `p,...,2p-2`. Those high-degree convolution terms are exactly a finite-truncation correction that must be controlled `p`-adically. This is one concrete place where a real finite-Clausen bridge is required.

---

## 4. Lane A — modular form / CM specialization

### 4.1 What closes exactly

The following identifications are exact:

\[
g_n=A_n,
\qquad
t\!\left(\frac{\sqrt{-6}}3\right)=\frac1{216}.
\]

Thus Beukers' order-3 level-3 family is not merely analogous; it is the same coefficient family at the same denominator.

The operator shape also matches: the target weight `(6n+1)` is

\[
F_p+6\theta F_p.
\]

### 4.2 What does not close

Two obligations remain if one wants to quote Beukers as a complete restricted-class proof:

1. derive `delta(alpha)=-1/6` symbolically from the modular data rather than from numerical `q`-expansion;
2. identify the theorem's exact character factor with `(p/3)` on the relevant split prime classes.

Even if both are discharged, the theorem being used still assumes `p` split in `Q(sqrt(-6))`; it gives no all-prime result for the inert classes.

The residue-class geometry is:

| `p mod 24` | split in `Q(sqrt(-6))`? | `p mod 3` | target RHS |
|---:|---|---:|---:|
| 1 | split | 1 | `+p` |
| 5 | split | 2 | `-p` |
| 7 | split | 1 | `+p` |
| 11 | split | 2 | `-p` |
| 13 | inert | 1 | `+p` |
| 17 | inert | 2 | `-p` |
| 19 | inert | 1 | `+p` |
| 23 | inert | 2 | `-p` |

Therefore:

`LANE_A_STATUS = EXACT_COEFFICIENT_AND_CM_MATCH / ALL_PRIME_ROUTE_BLOCKED_BY_SPLIT_HYPOTHESIS`

This is not an all-prime proof.

---

## 5. Lane B — direct `p`-adic valuation and binomial expansion

This lane produced a new exact reduction that is independent of modularity.

### Lemma 5.1 — exact kernel valuation

For every prime `p>3` and integer `0<=n<p`,

\[
\boxed{
v_p\!\left(
\binom{2n}{n}^2\binom{3n}{n}
\right)
=
\left\lfloor\frac{2n}{p}\right\rfloor
+
\left\lfloor\frac{3n}{p}\right\rfloor.
}
\tag{5.1}
\]

#### Proof

Because `n<p`,

\[
v_p\binom{2n}{n}
=
v_p((2n)!)-2v_p(n!)
=
\left\lfloor\frac{2n}{p}\right\rfloor.
\]

Also `3n<3p<p^2` for `p>3`, so

\[
v_p\binom{3n}{n}
=
v_p((3n)!)-v_p((2n)!)-v_p(n!)
=
\left\lfloor\frac{3n}{p}\right\rfloor
-
\left\lfloor\frac{2n}{p}\right\rfloor.
\]

Adding two copies of the first valuation gives `(5.1)`. ∎

### Corollary 5.2 — four exact precision layers

Since `p` is not divisible by `2` or `3`, no interval boundary is integral. We obtain:

\[
v_p(A_n)=
\begin{cases}
0,&0\le n<p/3,\\
1,&p/3<n<p/2,\\
2,&p/2<n<2p/3,\\
3,&2p/3<n<p.
\end{cases}
\tag{5.2}
\]

Because `216` is a `p`-adic unit, the same valuations apply to `A_n/216^n`.

Therefore modulo `p^3`:

- the last block `2p/3<n<p` vanishes **term by term**;
- the block `p/2<n<2p/3` contributes at `p^2` precision;
- the block `p/3<n<p/2` contributes at `p` precision;
- the lower block must be known modulo `p^3`.

This is the exact precision bookkeeping demanded by the task.

### 5.3 Exact no-go for the naive tail collapse

A tempting shortcut would be to drop every term after `p/3` modulo `p^3`. Lemma 5.1 proves that this cannot be justified by termwise valuation.

It is not rescued by block cancellation in general. Exact block residues already give:

For `p=5`, modulo `125`,

\[
(B_0,B_1,B_2,B_3)=(50,45,25,0).
\]

For `p=7`, modulo `343`,

\[
(B_0,B_1,B_2,B_3)=(231,217,245,0).
\]

For `p=13`, modulo `2197`,

\[
(B_0,B_1,B_2,B_3)=(780,1937,1690,0).
\]

Here `B_j` is the weighted sum over the terms with `v_p(A_n)=j`.

Thus the valuation-1 and valuation-2 layers are genuinely nonzero and must be coupled to the lower block by a deeper identity. Only the valuation-3 block dies for free.

`LANE_B_STATUS = VALUATION_STRATIFICATION_PROVED / NAIVE_TAIL-VANISHING ROUTE REFUTED`

---

## 6. Exact recurrence and finite regression

Define

\[
a_n=\frac{A_n}{216^n}.
\]

Direct cancellation gives the exact recurrence

\[
\boxed{
\frac{a_{k+1}}{a_k}
=
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
}
\tag{6.1}
\]

For `0<=k<=p-2`, the denominator is invertible modulo `p^3`, so `(6.1)` yields a deterministic exact modular evaluator without factorials.

A second evaluator computes the integer binomial kernel directly and multiplies by `216^{-n}` modulo `p^3`.

The retained checker is:

`scripts/check_enterprise_brc_half_coupling_padic_all_prime.py`

Frozen regression result:

`research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF/regression_10000.json`

Results:

- all primes `5 <= p <= 9973`;
- `1227` primes tested;
- `0` target failures;
- `44` primes through `p=199` independently cross-checked by the direct integer evaluator;
- `0` evaluator mismatches;
- `4222` individual `(p,n)` checks of Lemma 5.1 in the independent direct range;
- `0` valuation-formula mismatches.

This is **FINITE_REGRESSION_ONLY_NOT_A_PROOF**.

The finite result cannot upgrade the all-prime theorem status.

---

## 7. Smallest unresolved proof frontier

The strongest next unit is not "test more primes" and not "search for another nearby modular theorem."

Freeze:

`INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE`

Let

\[
G(z)={}_2F_1(1/6,1/3;1;z).
\]

Formal Clausen gives `F=G^2`. For a finite `p`-term truncation, coefficients below degree `p` agree with the corresponding square convolution, but evaluation of `G_{p-1}(1/2)^2` also contains convolution degrees `>=p`.

The unresolved lemma is to control, for primes inert in `Q(sqrt(-6))`, the weighted finite correction

\[
(1+6\theta)
\left(
G_{p-1}(z)^2-F_{p-1}(z)
\right)_{z=1/2}
\]

to sufficient `p`-adic precision, together with the Frobenius sign producing `(p/3)`, while explicitly retaining the valuation-1 and valuation-2 ranges from `(5.2)`.

A successful proof can plausibly come from one of two exact forms:

1. a `p`-deformed terminating hypergeometric / creative-telescoping identity whose boundary terms expose the required `p^3`;
2. a `p`-adic Gamma expansion of the finite Clausen correction that pairs the valuation-1 and valuation-2 layers with the lower block.

The next researcher should **not** spend a stage only enlarging the numerical bound or only re-auditing split-prime literature.

---

## 8. Dependency map

| Claim used in this return | Dependency | Status here |
|---|---|---|
| target already exists as A14(ii), `a=1` | Sun, arXiv:0911.5665 | literature audit |
| Beukers coefficient family is `A_n` | Beukers, arXiv:2403.03301, order-3 level-3 example | exact source specialization |
| Beukers CM value is `1/216` | same | exact source specialization |
| Beukers theorem requires split primes | same | exact scope audit |
| Shvets mixed `(1/6,1/3;1)` split/inert result | Shvets, arXiv:2605.19773 | related result only |
| hypergeometric coefficient identity | factorial/Pochhammer algebra | verified directly |
| Clausen factorization | classical Clausen identity with `a=1/6,b=1/3` | exact algebraic identity |
| valuation Lemma 5.1 | Legendre valuation of factorials | proved above |
| recurrence (6.1) | ratio of consecutive factorial kernels | verified directly |
| finite prime evidence | retained exact checker | regression only |

No imported theorem is used to claim `(T)` itself.

---

## 9. Prior-art / novelty classification

- `ALL_PRIME TARGET`: **previously conjectured**, not proved by this execution.
- `BLIND ENTERPRISE EVIDENCE`: **finite independent evidence only**.
- `VALUATION STRATIFICATION (5.1)-(5.2)`: elementary exact reduction established in this execution; no novelty claim is made without a dedicated literature search for this lemma.
- `NAIVE WHOLE-TAIL VANISHING`: **exactly refuted as a proof mechanism**.
- `BEUKERS SPLIT CM ROUTE`: **real and highly relevant, but not an all-prime closure as cited**.
- `SHVETS 2026`: **proved related split-prime result for a different sequence**.
- `ALL_PRIME MOD-p^3 THEOREM`: **UNRESOLVED IN THIS EXECUTION**.

---

## 10. Driver recommendation

Return this result as a completed research attempt with task verdict `PROOF_NOT_CLOSED`, not as theorem success.

Recommended control-plane action:

`FOLLOWUP_TASK`

Scope the successor narrowly to:

`INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE`

with the four inert classes `p≡13,17,19,23 (mod 24)` explicitly in scope and with a prohibition on merely extending finite computation.

If Driver instead wants to harvest the split half first, issue a separate typed task whose only goal is to turn the Beukers `t=1/216` match into a line-by-line exact specialization, including symbolic `delta=-1/6` and character-sign extraction. Do not silently count that as an all-prime theorem.

---

## 11. Output manifest at research level

- `research_returns/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF_RETURN_20260827.md`
- `research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF/proof_lane_audit_20260827.json`
- `research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF/regression_10000.json`
- `scripts/check_enterprise_brc_half_coupling_padic_all_prime.py`
- `research_execution_records/RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF/ER-D4103A95B79DB59189AC.json`

Research terminal state after freeze:

`AWAITING_DRIVER_REVIEW`

The researcher does not self-issue `DONE`.
