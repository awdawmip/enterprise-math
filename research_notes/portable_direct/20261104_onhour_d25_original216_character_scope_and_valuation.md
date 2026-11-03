# D25 original-216: exact valuation-boundary transport and a finite character-sign test

2026-11-04 (+08) | **AUTHOR-DERIVED / UNIVERSAL EXACT VALUATION LEMMA / FINITE EXACT EXPERIMENT / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Author-side mathematical evidence, not an authenticated native Source checkpoint or Result.

**Binding identity.** TASK_RESEARCH logical conversation `chatgpt-research-onhour-enterprise-math-20260923`, separate from maintenance `chatgpt-hourly-enterprise-math-20260921` and the other research lane `chatgpt-research-hourly-enterprise-math-20260923`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Parent target for p≡13,19 mod24 remains Delta_p=R_p mod p, equivalent under the frozen scalar bridge to original W_(p-1)=p mod p³. Consume earlier 216 root/curvature work at `ce0052d8af8ae6ffdba68d9a09f7b47b43142333` and F4 four-source formula; no acceptance claimed.

## Theorem — exact p-adic support boundary for the unchanged 216 series

For every prime p>=5 and 0<=k<p, define in Z_(p)

```text
b_k = binom(2k,k)^2 binom(3k,k) / 216^k
    = (2k)! (3k)! / ((k!)^5 216^k).
W_(p-1) = sum_{k=0}^{p-1} (6k+1) b_k.
```

Then, **for every such p,k**, the following exact integer valuation holds:

```text
v_p(b_k) = floor(2k/p)+floor(3k/p)
         = 1_{k>floor(p/3)} + 1_{k>floor(p/2)} + 1_{k>floor(2p/3)}.
```

Proof: p>3 makes 216 a unit. Since k<p, v_p(k!)=0; since 2k<2p and 3k<3p<p² for p>=5, Legendre's factorial formula gives exactly the floor terms. Each floor jumps precisely at the three shown bounds, which are distinct because p>3. Therefore, **unconditionally**,

```text
W_(p-1) == sum_{k=0}^{floor(2p/3)} (6k+1) b_k   (mod p^3).
```

The coefficient layers have valuations 0,1,2,>=3. The extra weight 6k+1 can increase an individual weighted-term valuation. In particular the more aggressive half-truncation k<=(p-1)/2 is not equivalent at mod p³ (p=13: half=520, full=13 mod2197). This standard Legendre calculation is a useful exact source/precision boundary, not a claim to a novel general theorem or an X6 native-space transfer.

## Discriminating scientific hypothesis — finite evidence only

For the **same unchanged original** W, test the larger-domain proposal

```text
CONJECTURE (unproved): W_(p-1) == p * (-3/p) (mod p^3) for every prime p>=5,
```

where (-3/p) is the Legendre symbol: +1 if p=1 mod3, -1 if p=2 mod3.

A standalone Python 3 standard-library integer script was executed over **every prime 5<=p<=2000 (301 primes)**. All 301 finite cases match: 148 p=1 mod3 and 153 p=2 mod3; all 301 full-versus-certified-cutoff comparisons match, 277045 exact p,k valuation pairs checked, and 13 independent direct integer-binomial summations crosschecked. Examples: p=5 -> W=120=-5 mod125; p=11 -> W=1320=-11 mod1331; p=13 -> W=13; p=19 -> W=19; p=373 -> W=373 mod 51895117. Here p373 half-truncation=14887176 and the exact valuation cutoff is k<=248. All arithmetic is exact modulo p³, no floating point.

The test's `b_k` recurrence is the **original** ratio `(2k+1)(3k+1)(3k+2)/(36(k+1)^3)` with denominators invertible for 0<=k<p-1. The independent check uses `math.comb(2k,k)^2 * math.comb(3k,k) / 216^k`. This is exhaustive only on the declared finite prime interval. **Neither the all-prime character congruence nor the original D25 mother claim has been proved by this experiment.** An existing literature proof of the stronger congruence has not been ruled out; claim no priority/novelty.

## Artifacts / observer scope

Executed author-side files (paired evidence bundle in conversation):

- `d25_original216_uniform_character_check_20261104.py`: deterministic prime sieve, original recurrence, Legendre valuations, independent binomial tests; PASS on 301 primes.
- `d25_original216_uniform_character_results_20261104.json`: exact captured outcome and examples.
- This note: theorem proof, evidence status, and continuation.

BRC observer is `(p,k,v_p(b_k),b_k mod p^3,(6k+1)b_k mod p^3)` with branch/source labels for 0/1/2 valuation layers. A scalar sign equality never proves full branch-state cancellation. The externally computed p-adic sums do not satisfy the original same-class native H0/B0 experiment; that distinct p373 rank, [X]U mod139129, semilinear Frobenius direction/basis eta, signed odd Green/Hesse, κ and independent replay are still NOT_EXECUTED, support issue #1559 OPEN/PENDING_OWNER.

## Continuation packet

**Mother target:** frozen Delta_p=R_p on p=13,19 mod24, original W_(p-1)=p mod p³. **Highest project frontier:** earlier author-side p³ four-source, CM-root and curvature transport proofs, all UNREVIEWED/NOT_ADMITTED, plus this exact p³ cutoff and finite sign experiment. No claim of native completed units.

**Next minimal scientific action:** Seek a genuinely uniform terminating signed WZ/contiguous-parameter/p-adic Gamma certificate for original 216 weighted summand and its actual 2p/3 cutoff. A useful candidate must predict both p=1 mod3 (+p) and p=2 mod3 (-p), preserve valuation-1/2 ports and terminal boundary, and be independently checked as a certificate (not just match the final sum) first at 5,11,13,19,373. If unsuccessful, return directly to the existing frozen-target F4 signed Green/WZ residual; do not repeat already completed auxiliary lemmas. Parallel native #1559 retains unchanged benchmark and acceptance, executor PENDING_OWNER.

**Control:** actual 0.6.11 status in this run: `research_authority_granted=false`, Site `write_relay_enabled=false`, `UPSTREAM_CODE_REVIEW_REQUIRED`, active quota 5/5. Existing historical request `research-onhour-20261031-0205-dispatch-r15` has been reported finally failed; it is not replayed. Own recovery_status/claim not reverified, and no native session, CLAIM, open, run, Source checkpoint or Result is asserted. This writer did not operate on the maintenance conversation, rebind staging or alter scheduling.
