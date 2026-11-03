# D25 onhour: 216–2304 signed two-tail bridge and new 2304 finite high-strip theorem

2026-11-03; TASK_RESEARCH author-side research, logical lane `chatgpt-research-onhour-enterprise-math-20260923`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: **AUTHOR-DERIVED / SCOPED PROOF / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. D25 mother goal `W216_p=p (mod p^3)` for `p=13,19 (mod24)` remains OPEN. This note is not a native Source checkpoint or a H0/B0 experiment execution.

## Objects and full quantifiers

For every prime `p>=5`, in `Z_(p)`, put `h=(p-1)/2`, `u=floor(2p/3)-h`, `v=floor(3p/4)-h` and

```
b_k=binom(2k,k)^2*binom(3k,k)/216^k;
c_k=(4k)!/((k!)^4*2304^k);
W_p=sum_{k=0}^{p-1}(6k+1)b_k; W_h=sum_{k=0}^h(6k+1)b_k;
S_p=sum_{k=0}^{p-1}(8k+1)c_k; S_h=sum_{k=0}^h(8k+1)c_k.
```

Previously proved valuation inputs: `v_p(b_k)=floor(2k/p)+floor(3k/p)`, `v_p(c_k)=floor(4k/p)` for `k<p` (D25 source eeb6f882aae70ec0a2b37d74ea7b7f988ee1a9c4). Distinguish the 216 order-two strip ending `floor(2p/3)` from the 2304 strip ending `floor(3p/4)`.

## Theorem A, proved here, universal 2304 high tail

Define `a_t=(1)_t(3/4)_t(5/4)_t/((3/2)_t^3*9^t)` in `F_p` for `0<=t<v`, and `Q4_p(x)=sum_{t=0}^{v-1} a_t*x^t`, `theta=x*d/dx`. All denominators are p-units. Then:

```
c_(h+1)/p^2 = 1/36 (mod p),
c_(h+1+t)/p^2 = a_t/36 (mod p) for 0<=t<v,
S_p - S_h = p^2/36 * [(5+8theta)Q4_p](1) (mod p^3).
```

*Proof.* Since `4(h+1)=2p+2`, Wilson and p-block factorials give `(2p+2)!/p^2=4 (mod p)`. Wilson also gives `(h!)^2=(-1)^(h+1) (mod p)`, so `((h+1)!)^4=1/16`. As `2304=48^2`, Fermat implies `2304^(h+1)=2304 (mod p)`. Hence `c_(h+1)/p^2=4/(2304/16)=1/36`. The exact recurrence

```
c_(k+1)/c_k=(4k+1)(4k+2)(4k+3)/(576(k+1)^3)
```

at `k=h+s` reduces to `s(4s-1)(4s+1)/(18(2s+1)^3)`; this is exactly `a_s/a_(s-1)`. The original weight at `k=h+1+t` is `4p+8t+5`, so its mod-p value is `8t+5`. For `k>floor(3p/4)`, `v_p(c_k)>=3`; the weighted tail vanishes mod `p^3`. This proves the formula with *no inferred cancellation*.

## Theorem B, proved here, terminating 2304 differential identity

The *complete finite polynomial*, including its endpoint, satisfies in `F_p[x]`:

```
[ theta*(theta+1/2)^3
 -(x/9)*(theta+1)^2*(theta+3/4)*(theta+5/4) ] Q4_p(x) = 0.
```

For internal coefficients it is the ratio of Theorem A. At the only potential boundary term `x^v`, the right factor contains `(v-1/4)(v+1/4)`: for `p=4m+1`, `v=m`, `4v+1=p`; for `p=4m+3`, `v=m+1`, `4v-1=p`. Thus it vanishes exactly modulo p; no untracked end term remains.

## Theorem C, proved signed two-tail reduction

Consume the previously proved original 216 mirror (without re-proving): let `Q3_p(x)=sum_{t=0}^{u-1} (1)_t(5/6)_t(7/6)_t*x^t /((3/2)_t^3*2^t)`, `chi6=(6/p)`. Then for all primes `p>=5`,

```
W_p-S_p = (W_h-S_h) + p^2*(
   chi6/9 * [(4+6theta)Q3_p](1)
 - 1/36  * [(5+8theta)Q4_p](1))  (mod p^3).
```

For D25 target primes the accepted D24 first-digit result and the independently sourced 2304 theorem imply `W_p-S_p=0 (mod p^2)`; each tail separately has order at least two. The remaining **unproved** all-target bridge `W_p=S_p (mod p^3)` is therefore equivalent to

```
(W_h-S_h)/p^2 + chi6/9*[(4+6theta)Q3_p](1)
              - 1/36*[(5+8theta)Q4_p](1) = 0 (mod p).
```

This is a signed, provenance-preserving BRC observer composition (`COMPOSE_APPLIED`); it preserves original factorial labels, valuations, truncation, and denominator units. No new P000 assumption or X6 coordinate is introduced.

## New explicit conjecture and exact finite discrimination

The specific, **unproved** prospective lemma is `[(5+8theta)Q4_p](1)=0 (mod p)` for all primes `p>=5`; by Theorem A it is equivalent to `S_p=S_h (mod p^3)`. Since the first 2304 high coefficient is the nonzero unit `1/36`, this is a *signed cancellation*, not termwise disappearance.

Companion checker executed for all **301 primes 5<=p<=2000**, including 77 D25 target primes. It uses p-free factorial-unit modular arithmetic, independent finite hypergeometric ratios, and eight selected primes checked again with the original integer binomial/factorial coefficients. All 301 exact two-tail equations passed; 301/301 passed the *candidate* 2304 high-tail zero; 301/301 passed the *candidate* full 216–2304 bridge. These tests are not all-prime proofs.

| p | (W_h-S_h)/p² mod p | 216 high tail /p² mod p | 2304 high tail /p² mod p | signed total |
|---:|---:|---:|---:|---:|
| 13 | 3 | 10 | 0 | 0 |
| 19 | 10 | 9 | 0 | 0 |
| 37 | 17 | 20 | 0 | 0 |
| 373 | 107 | 266 | 0 | 0 |

At p=373, p²=139129, W_h=14887176, S_h=373 modulo p³: their difference is **14886803=107*139129**. The original 216 high strip contributes 266*139129; the observed 2304 high strip contributes zero; 107+266-0=373=0 mod373.

## Open obligations and next exact scientific move

Prove or falsify `(5+8theta)Q4_p(1)=0` via terminating, p-dependent WZ/adjoint, preserving **both** `4v±1=p` termination classes and original derivative weight. Then use the now-proved signed two-tail equation to isolate the actual 216 half-carry cancellation against 2304. The 216–2304 all-target p³ bridge and D25 mother goal remain OPEN.

Native benchmark #1559 still requires original p373 H0/B0 divided-power `[X]U mod139129`, module rank, real semilinear Frobenius, eta/signed observer and independent reproduction. **NOT EXECUTED**; current ordinary integer checks cannot substitute for it. Original dispatch request `research-onhour-20261031-0205-dispatch-r15` historically FAILED/UPSTREAM_CODE_REVIEW_REQUIRED; this turn's read returned CONTROL_REQUEST_NOT_FOUND, and exact Source continuation returned CONTROL_QUOTA. Fresh Sites read 2026-11-03 06:02Z shows `research_authority_granted=false`, `write_relay_enabled=false`. No native Researcher session/CLAIM/run/Source checkpoint/Result/admission. Control support #1558 already exists; no duplicate. Need authenticated Research execution configuration, not borrowing maintenance lane identity. Preserve current frozen pins and author-side contribution provenance.

External existing 2304 source, not a proof of the 216 bridge: Guo–Zudilin, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, arXiv:1803.01830, proves `S_p=p*(-3/p) (mod p^3)` for p>3.
