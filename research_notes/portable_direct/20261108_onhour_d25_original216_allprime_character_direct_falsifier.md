# D25 / frozen original weighted-216: exact p-free three-band evaluator and all-character falsification

2026-11-08 Asia/Hong_Kong. **TASK_RESEARCH author-side / exact original-term arithmetic identity / executed finite regression / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** No new formal Task, Source Researcher/CLAIM, Result, or native H0/B0 assertion.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, immutable publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Original accepted first-digit CM0/UR/JT0 and the exact `Delta_p-R_p=(W_p-p)/p² mod p` port alignment are consumed, not reproved.

## Actual frozen carrier and a new exact direct evaluation

For any prime `p>3`, define the **same original** integer-coefficient weighted sum in `Z_(p)`:

```
w_n = (6n+1) * binom(2n,n)^2 * binom(3n,n) / 216^n,  0<=n<p
W_p = sum_{n=0}^{p-1} w_n.
```

The frozen mother statement asks `W_p ≡ p (mod p³)` only for `p mod 24 in {13,19}`. The enlarged all-prime scan below is an **external class discriminator on the same original arithmetic object**, not a modification to task inputs or hypotheses.

**Proved exact evaluator (all p>3).** Set `L=floor((2p-1)/3)`, `q=p³`, `e_n=floor(2n/p)+floor(3n/p)`. For `0<=k<=3L<2p`, let `F_p(k)=∏_{1<=j<=k, j!=p} j mod q`; this is a unit. Then

```
W_p = sum_{n=0}^{L} (6n+1)*p^{e_n}*
      F_p(2n)*F_p(3n)*F_p(n)^{-5}*216^{-n}     (mod p³).
```

**Proof.** The original exact binomial product is `(2n)!(3n)!/(n!)^5`. Since `n<p`, the valuation of this product equals `e_n`. For `n>L`, we have `3n>=2p` and `2n>=p`, whence `e_n>=3`; these terms vanish modulo `p³`, including the weight. In the remaining range `3n<2p`, exactly `floor(k/p)` factors of `p` occur in `k!`, all to exponent one, and `n! = F_p(n)`. Removing those integer factors gives the displayed congruence with **only unit denominators**. This proof uses no conjectural cancellation. The valuation label `e_n` and original index/sign stay attached to every term. QED.

The three nontrivial branches `e=0,1,2` are the original source-resolved information carrier. For frozen `p=6m+1`, these reproduce the prior band boundaries `0..2m`, `2m+1..3m`, `3m+1..4m`. The new evaluator is an independent direct arithmetic implementation of the unchanged original `W`, not a new third-digit identity. It uses O(p) ring operations and storage per p, with modular integers of O(log p) bits, one inverse of a terminal factorial unit and one inverse of 216 (not a claim of O(p) bit complexity).

## Executed exact falsification, including two character classes

Checker: `research_notes/portable_direct/d25_original216_factorial_falsifier_20261108.py`. Execute `python d25_original216_factorial_falsifier_20261108.py 10000`. The code independently checks selected original complete binomial sums (including p=373), and scans **all 1227 primes 5<=p<=10000**. Per-class counts p mod24: `1:143, 5:157, 7:156, 11:155, 13:157, 17:152, 19:155, 23:152`.

- Frozen target classes `p mod24=13,19`: 312 primes, `W_p=p modp³` for all 312; failures 0.
- Expanded exact conjectural character prediction **`W_p = p * (−3/p) (mod p³)`**: all 1227 primes pass, failures 0; `(−3/p)=+1` for `p mod3=1` and `−1` for `p mod3=2`. This is a **finite observation**, NOT a proved all-prime hypergeometric supercongruence.
- On **all 312 frozen target primes**, the separately evaluated e=2 tail is nonzero modulo p³ after dividing by p²; the e=0+1 bulk has a nonzero opposite third-digit defect. Thus the finite set gives 312 original-source counterexamples to a bulk-only third-digit readout, **not counterexamples to frozen LIFT**. Complete source cancellation requires both.

Exact reproducible instances (all branch entries are remainders mod p³):

| p | character | `[band_e0,band_e1,band_e2]` | `W_p` | bulk digit | tail digit |
|---:|---:|---|---:|---:|---:|
| 13 | +1 | [780,1937,1690] | 13 | 3 | 10 |
| 19 | +1 | [5662,4826,3249] | 19 | 10 | 9 |
| 37 | +1 | [814,22496,27380] | 37 | 17 | 20 |
| 211 | +1 | [5478615,4316216,8993242] | 211 | 9 | 202 |
| 373 | +1 | [28094360,38687933,37008314] | 373 | 107 | 266 |
| 5 | −1 | [50,45,25] | 120=−5 mod125 | — | — |
| 11 | −1 | [220,979,121] | 1320=−11 mod1331 | — | — |

At p=373, q=51,895,117 and `W_{0+1}=14,887,176`. Thus `(W_{0+1}-373)/139129=107` and `W_2/139129=266`; `107+266=373=0 mod373`. This reproduces the prior p373 tail certificate **independently** and is an exact original-Hasse observer information-loss witness. The checker also returns a diagnostic rolling checksum `17164715295810299958` (non-cryptographic and not a source attestation).

## Source/BRC and next scientific action

**BRC = COMPOSE_APPLIED / REUSE_EXECUTED.** Population: exactly the original n-indexed p-local terms. Provenance: original denominator 216^n, source weight 6n+1, valuation grade e, ordered cutoff, three separate mod-p³ branches, and original Delta/R. Allowed operation here: linear accumulation modulo p³; branch collapse only *after* retaining the tail and the future Delta-R observer. The two-component quadratic CM algebra used in neighboring notes is an auxiliary classical field, not a native 2D Heartbeat-X6 slice. P000 and ACTIVE worldview remain unchanged.

The exact arithmetic lemma and reproducible falsifier are completed author-side. A uniform **mathematical proof** of `W_p=p modp³` for both target classes remains OPEN. The expanded sign pattern supplies a concrete two-class structure to test through existing Clausen/Fricke/Frobenius mechanisms, but 1227 finite checks do not prove either class.

The **highest mandatory experimental debt** remains the original same-class `p=373` native H0/B0 divided-power benchmark [#1559](https://github.com/awdawmip/enterprise-math/issues/1559): actual `[X]U mod139129`, native rank, semilinear Frobenius direction and eta, signed odd Green/Hesse κ, original Delta-R, raw source-bound inputs and independent verification; then p=19. This exact p-free evaluator is an original scalar regression **not** the native H0/B0 experiment, and #1559 remains `PENDING_OWNER / NOT_EXECUTED`.

No verified native Researcher/claim/run exists in the present tool context. The original request `onhour11-20261106-1400-exact-research-lane-continuation` remains pending reconciliation: this turn's `em_status` and original `em_control_result` both reported `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. Site local read `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; responsible recovery needs an independent Site-bound backend client/secure credential and lawful native benchmark executor. Do not resend the original write, use a maintenance identity, claim native completion, or rebase frozen scientific input.

**Next exact original-object mathematical action:** test/derive a source-preserving character-`(−3/p)` transformation connecting the unchanged e=0/1/2 original W sum to the previously studied 2304 Frobenius model; if the transformation lacks a valid p³ coefficient identity, seek its first explicit nonzero defect. **Next authoritative acceptance action:** #1559's original-class native p373 run by a lawful executor. Only a full proof or exact counterexample terminates the mother LIFT; the character pattern is now an independent hypothesis to discriminate.

**Status:** `AUTHOR_SIDE_EXACT_EVALUATOR_PROVED / EXECUTED_1227_PRIME_DIRECT_REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`.
