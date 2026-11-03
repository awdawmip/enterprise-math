# D25 — universal normalized valuation-two port of the quartic 2304 comparator

Date: 2026-11-04 (+08). Classification: **AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is portable mathematics, not a native Source checkpoint, Result, native experiment, CLAIM or independent review.

**Frozen linkage:** Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Ordinary-control Research conversation `chatgpt-research-onhour-enterprise-math-20260923`; distinct maintenance conversation `chatgpt-hourly-enterprise-math-20260921` (no identity/claim borrowing). Source predecessor: `research_notes/portable_direct/20261104_onhour_d25_original216_quartic_bridge_ports.md` (author-side work). The proven Guo–Zudilin comparator for the entire quartic sum remains separately sourced there. The W-to-V bridge is still open.

## Exact theorem: p-independent normalized valuation-two terms

For every prime `p>=5` put `h=(p-1)/2`, `N=floor((p+1)/4)` and, in `Z_(p)`,

```text
b_k = (4k)! / ((k!)^4 * 2304^k),
V_{p,2} = sum over 0<=k<p with floor(4k/p)=2 of (8k+1)*b_k.
d_n = (4n-2)!*(n!)^4 / (9^n*((2n)!)^4),  1<=n<=N.
S_N = sum_{n=1}^N (8n-3)*d_n.
```

The valuation-two indices are *exactly* `k=h+n, 1<=n<=N`. Their coefficients satisfy the **universal, prime-independent normalization**

```text
    (b_{h+n}/p^2) mod p = (2*d_n) mod p.                  (1)
```

Consequently the entire weighted valuation-two port has the exact congruence

```text
    V_{p,2} = 2*p^2*S_N (mod p^3).                      (2)
```

The rational numbers `d_n` have p-unit denominators for `n<=N` and obey

```text
    d_1 = 1/72,
    d_{n+1}/d_n = n*(16*n^2-1) / (18*(2*n+1)^3),        (3)
```

with all displayed quotients legitimate modulo p for `1<=n<N`. In particular the candidate all-prime vanishing `V_{p,2}=0 (mod p^3)` is **equivalent**, for each p, to the short finite-field relation `S_N=0 (mod p)`. This is a proved equivalence, not yet a proof of that last relation.

There is nontrivial cancellation inside this band for every `p>=7`: the first weighted term alone is nonzero modulo `p^3`, since `(8(h+1)+1)*b_{h+1}/p^2 = 5*(1/36) mod p !=0`. Therefore a proof of whole-port vanishing must explain cancellation between its individual terms, not merely the valuation cutoff. For `p=5` this first weight is itself divisible by p.

### Proof

For `k=h+n`, `4k=2p+(4n-2)` with `0<=4n-2<p` precisely for the stated n range. Hence `v_p((4k)!)=2`, while `v_p(k!)=0` and `2304` is a p-unit. Splitting the two complete p-blocks gives

```text
(4k)!/p^2 = 2*[(p-1)!]^2*(4n-2)! = 2*(4n-2)! (mod p).
```

Wilson gives `((p-1)/2)!^4=1 (mod p)`; moreover

```text
(h+n)! = h! * product_{i=1}^n(h+i)
       = h!*(1/2)_n (mod p),
(1/2)_n = (2n)!/(4^n*n!).
```

Thus

```text
b_{h+n}/p^2
 = 2*(4n-2)! / [h!^4*(1/2)_n^4*2304^(h+n)]
 = 2*2304^(-h)*((4n-2)!*(n!)^4)/(9^n*(2n)!^4) (mod p).
```

Since `2304=48^2` and `2304^h=48^(p-1)=1 (mod p)`, this proves (1). Also `8(h+n)+1=4p+8n-3`, so multiplying (1) by the original weight and summing yields (2). Direct factorial division yields recurrence (3). For `n<=N`, `2n+1<p` and `(2n)!` is a p-unit. For `n=1`, `d_1=1/72`, so the weighted first term is `5/36` modulo p.

The construction retains original index `k`, valuation `v_p=2`, weight `8k+1`, finite-field readout `b_k/p^2`, and the invertible transport to index `n=k-h`. It is a separate port in the three-valuation-source decomposition of the original 216-to-2304 comparison, not a replacement of the full sum or the fixed H0/B0 benchmark.

## Exact computation and scope

Two independently formulated checks were **actually executed** in this research turn:

1. A recurrence-based finite-field checker evaluated `S_N mod p` via (3) for **every one of the 1,227 primes 5<=p<=10,000** (609 primes `1 mod 4`, 618 primes `3 mod 4`). **All 1,227 residues were zero**. This strengthens the previously recorded 301-prime observation, but is finite evidence, not a universal proof.
2. An independent original-coefficient BigInt recurrence evaluated `b_k mod p^3`, extracted `b_{h+n}/p^2 mod p` and checked pointwise against `2d_n mod p` for `p in {5,7,11,13,19,37,373}`. **No pointwise mismatches** and `V_{p,2}=0 mod p^3` in these seven exact cases. No floating point enters the modular coefficient computation.

Some directly reproduced data:

```text
p    N   (b_{h+1}/p²) mod p   (b_{h+N}/p²) mod p   V_{p,2} mod p³
5    1          1                       1                      0
7    2          1                       5                      0
11   3          4                       3                      0
13   3          4                       4                      0
19   5          9                      11                      0
37   9         36                      28                      0
373  93        114                     59                      0
```

For `p=13`, the three normalized coefficients are `(4,12,4)` and original weights modulo 13 are `(5,0,8)`, so the normalized sum is `5*4+0*12+8*4=52=0 mod13`. The first and last contributions are individually nonzero.

An executable JavaScript checker with no external packages is supplied as `d25_quartic_val2_universal_port_checker_20261104.mjs`. The finite-field algorithm was executed in the connected JS runtime; the saved standalone file is a reproducible implementation and needs independent replay if required for formal acceptance.

## Next exact science / continuation

Mother target: `Delta_p-R_p=0 mod p` for primes `p=13,19 mod24`. Current author-side frontier: original 216 and quartic 2304 have exact, **different** valuation partitions; the Guo–Zudilin V congruence is cited and accepted only for V; W=V modulo `p^3` still needs a full cross-band transport. This unit proves that quartic valuation-two terms admit a universal p-independent normalization and a single truncated sum `S_N`. Their all-prime cancellation is **observed but unproved**.

**Next discriminating step:** prove or disprove `S_{floor((p+1)/4)}=0 mod p` via a terminating transformation/certificate in the universal ratio (3), preserving the two distinct classes `p=4N+1` and `p=4N-1`. In parallel seek a signed original-216-to-quartic transport preserving `A_{p,0},A_{p,1},A_{p,2},B_{p,0},B_{p,1},B_{p,2}` and original endpoints. A certificate must explain cross-band compensation, not assume layerwise equality. After a mathematical candidate emerges, test its local identity at p=5,11,13,19,373.

Native evidence remains separate: support issue #1559 (same-original-class p=373 H0/B0 divided-power): original `[X]U mod 139129`, actual module rank, semilinear Frobenius, eta, signed odd Green/Hesse port, and independent replay are still required. This computation has not been performed here. Current read-only native gateway 0.6.11 reports `research_authority_granted=false`, `registered_session_count=0`, `source_sync.control.state=CODE_REVIEW_REQUIRED`, `UPSTREAM_CODE_REVIEW_REQUIRED`, and active request quota 5/5 at the run observation. Own checkpoint listing returned `ACCESS_DENIED`; therefore no Source checkpoint, native session/claim/run, Result or admission is asserted. Existing request IDs, including historical r15, are not replayed. The existing scheduled research task and notification configuration are unchanged.
