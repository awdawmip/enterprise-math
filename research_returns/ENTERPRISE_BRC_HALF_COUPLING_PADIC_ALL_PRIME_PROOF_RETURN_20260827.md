# Enterprise BRC Half-Coupling p-adic All-Prime Proof — Research Return

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-PADIC-ALL-PRIME-PROOF`  
Publication: `TP2-7A652D67B412693680E0`  
Claim: `chatgpt-ebp2-20260827-0822`  
Researcher-ID: `EM-EBP2-7D2C2F`  
Execution record: `ER-D4103A95B79DB59189AC`

## Frozen verdict

`PROOF_NOT_CLOSED`

Hard target `ENTERPRISE_BRC_HALF_COUPLING_PADIC_MOD_P3_ALL_PRIMES_PROVED_OR_REFUTED` remains **unclosed**. No counterexample was found, but neither the two proof lanes nor the audited literature supplied a complete exact all-prime proof.

The exact target is

\[
S_p=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
\equiv p\left(\frac{-3}{p}\right)\pmod{p^3}
\qquad(p>3).
\tag{T}
\]

Finite computation is regression only.

## 1. Prior-art audit

### Sun A14(ii)

Zhi-Wei Sun, *Open Conjectures on Congruences*, arXiv:0911.5665, Conjecture A14(ii), contains

\[
\frac1{p^a}\sum_{k=0}^{p^a-1}(6k+1)
\frac{\binom{2k}{k}^2\binom{3k}{k}}{6^{3k}}
\equiv\left(\frac{p^a}{3}\right)\pmod{p^2}.
\]

For `a=1`, multiplying by `p` gives exactly `(T)` because `6^3=216` and `(-3/p)=(p/3)` for `p>3`.

Classification: `EXACT_PRIOR_CONJECTURE`. The arithmetic target is not new to Enterprise.

### Beukers modular route

Frits Beukers, *Supercongruences using modular forms*, arXiv:2403.03301, has an order-3 level-3 example with

\[
g_n=\frac{(3n)!(2n)!}{(n!)^5}
\]

and the CM value

\[
t(\sqrt{-6}/3)=1/216.
\]

Thus the coefficient family and denominator match `(T)` exactly. The relevant theorem has an `F_p-\delta^{-1}\theta F_p` shape modulo `p^3`; the target operator is `F_p+6\theta F_p`. A high-precision q-expansion audit in this execution gives `delta=-1/6`, but this numerical identification is not promoted as proof, and the exact theorem character sign was not derived here.

More importantly, the theorem requires `p` split in `Q(sqrt(-6))`. For `p>3` the split classes modulo 24 are `1,5,7,11`; the inert classes are `13,17,19,23`. Therefore the cited framework cannot by itself close the all-prime theorem.

Classification: `EXACT_COEFFICIENT_AND_CM_MATCH / ALL_PRIME_SCOPE_BLOCKED_BY_SPLIT_HYPOTHESIS`.

### Shvets 2026

Alex Shvets, *Split-prime supercongruence at the mixed CM point (1/6,1/3;1)*, arXiv:2605.19773, proves a split-prime result for a symmetric-cube coefficient sequence at the same mixed hypergeometric backbone, with an inert obstruction. It is structurally relevant but is not the derivative-weighted p-term truncation `(T)`.

Classification: `RELATED_PROVED_RESULT / DIFFERENT TARGET`.

The scoped audit found no proved all-prime theorem whose checked hypotheses imply `(T)`. This is an audit conclusion, not a proof of nonexistence.

## 2. Hypergeometric / Clausen reduction

Let

\[
A_n=\binom{2n}{n}^2\binom{3n}{n}.
\]

Then

\[
\frac{A_n}{216^n}
=
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}\left(\frac12\right)^n,
\]

so

\[
S_p=
\left[
(1+6\theta)\sum_{n=0}^{p-1}
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3}z^n
\right]_{z=1/2}.
\]

Clausen gives the exact formal identity

\[
{}_3F_2(1/3,1/2,2/3;1,1;z)
=
{}_2F_1(1/6,1/3;1;z)^2.
\tag{C}
\]

This identifies the same mixed `(1/6,1/3;1)` backbone. But evaluating the square of a degree-`p-1` truncation introduces convolution degrees `p,\ldots,2p-2`; those finite-truncation correction terms must be controlled modulo `p^3`. Formal Clausen alone is not a finite p-adic proof.

## 3. Direct p-adic lane: exact valuation theorem

### Lemma

For every prime `p>3` and `0<=n<p`,

\[
\boxed{
v_p\!\left(\binom{2n}{n}^2\binom{3n}{n}\right)
=
\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor.
}
\tag{V}
\]

Proof. Since `n<p`,

\[
v_p\binom{2n}{n}=\lfloor2n/p\rfloor.
\]

Also `3n<3p<p^2`, hence

\[
v_p\binom{3n}{n}
=
\lfloor3n/p\rfloor-\lfloor2n/p\rfloor.
\]

Adding two copies of the first valuation proves `(V)`. ∎

Therefore

\[
v_p(A_n)=
\begin{cases}
0,&0\le n<p/3,\\
1,&p/3<n<p/2,\\
2,&p/2<n<2p/3,\\
3,&2p/3<n<p.
\end{cases}
\]

Because `216` is a p-adic unit, only the last third vanishes termwise modulo `p^3`. The two middle layers survive with precisions `p` and `p^2`.

This gives an exact no-go to the naive proof route “discard every term after `p/3`”. Exact weighted block residues are already nonzero:
- `p=5` mod `125`: `(50,45,25,0)`;
- `p=7` mod `343`: `(231,217,245,0)`;
- `p=13` mod `2197`: `(780,1937,1690,0)`.

Thus a real proof must couple the two middle layers to the lower block.

## 4. Exact recurrence and regression

With `a_n=A_n/216^n`,

\[
\boxed{
\frac{a_{k+1}}{a_k}
=
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
}
\tag{R}
\]

For `k<=p-2` the denominator is invertible modulo `p^3`. The retained checker implements this recurrence and a second direct integer-binomial evaluator.

Frozen regression:
- all `1227` primes `5<=p<=9973`: target passes;
- all `44` primes through `199`: recurrence and independent direct evaluator agree;
- `4222` direct `(p,n)` checks of `(V)`: all pass;
- target failures: `0`.

Artifacts:
- `scripts/check_enterprise_brc_half_coupling_padic_all_prime.py`
- `research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF/regression_10000.json`
- `research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF/proof_lane_audit_20260827.json`

Status: `FINITE_REGRESSION_ONLY_NOT_A_PROOF`.

## 5. Separate character classes

For `p>3`, `(-3/p)=(p/3)`. Modulo 24:

| p mod 24 | Q(sqrt(-6)) | target |
|---:|---|---:|
| 1 | split | +p |
| 5 | split | -p |
| 7 | split | +p |
| 11 | split | -p |
| 13 | inert | +p |
| 17 | inert | -p |
| 19 | inert | +p |
| 23 | inert | -p |

The modular route is therefore missing both character signs on the inert half; the obstruction is not “one bad residue class”.

## 6. Smallest unresolved lemma

Freeze the next frontier as:

`INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE`

Let

\[
G(z)={}_2F_1(1/6,1/3;1;z).
\]

For primes inert in `Q(sqrt(-6))`, prove enough p-adic control of the finite correction

\[
(1+6\theta)\bigl(G_{p-1}(z)^2-F_{p-1}(z)\bigr)\big|_{z=1/2}
\]

to evaluate the surviving valuation-1 and valuation-2 blocks modulo `p^3` and recover the Frobenius sign `(p/3)`.

Two exact candidate mechanisms remain:
1. a p-deformed terminating hypergeometric/WZ identity with boundary terms visibly divisible by `p^3`;
2. a p-adic Gamma expansion of the finite Clausen correction that pairs the middle layers with the lower block.

Do not spend the successor merely extending the finite prime bound or re-citing split-prime modular theorems.

## 7. Dependency / novelty classification

- `(T)`: prior exact conjecture (Sun A14(ii)); unproved here.
- Beukers: exact coefficient/CM match; split-prime framework only as audited.
- Shvets 2026: related same-backbone result, different sequence.
- valuation lemma `(V)`: proved self-contained here; no novelty claim.
- recurrence `(R)`: exact algebra.
- naive whole-tail vanishing: exactly refuted as a proof mechanism.
- all-prime theorem: unproved and unrefuted in this execution.

No imported theorem is used to claim `(T)` itself.

## 8. Driver recommendation

Research execution is complete at `PROOF_NOT_CLOSED`.

Recommended control-plane disposition: `FOLLOWUP_TASK` focused only on `INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE`.

If Driver wants the split half harvested first, issue a separate typed task to prove the Beukers specialization line-by-line, including symbolic `delta=-1/6` and the exact character sign. Do not count that as all-prime closure.

Research state after result freeze: `AWAITING_DRIVER_REVIEW`. The researcher does not self-issue `DONE`.
