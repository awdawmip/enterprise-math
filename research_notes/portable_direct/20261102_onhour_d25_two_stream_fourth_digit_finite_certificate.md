# D25 — Original weighted 216/2304 fourth-digit bridge: 428-prime exact finite certificate (2026-11-02)

**Status:** AUTHOR-DERIVED / EXACT FINITE EXHAUSTION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT. This author-side research note is durable neutral mathematical evidence, NOT a canonical Source checkpoint, Research-Activity, Result, CLAIM, run, proof of an all-prime conjecture, or independent review.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` is distinct from maintenance lane `chatgpt-hourly-enterprise-math-20260921`.

## New exact finite result — original sums, not surrogate series

For prime \(p>3\), use the **original coefficients** and original full cutoff \(0\le k<p\):

$$
W_p=\sum_{k=0}^{p-1}(6k+1)\binom{2k}{k}^2\binom{3k}{k}216^{-k},\qquad
S_p=\sum_{k=0}^{p-1}(8k+1)\binom{2k}{k}^2\binom{4k}{2k}2304^{-k}.
$$

Let \(\chi_p=1\) if \(p\equiv1\pmod3\), and \(\chi_p=-1\) if \(p\equiv2\pmod3\). The **finite theorem** was established by exact modular arithmetic for **every one of the 428 primes \(5\le p\le3000\)**:

$$
\boxed{W_p-2S_p+\chi_p p\equiv0\pmod{p^4}},\qquad
W_p\equiv S_p\equiv\chi_p p\pmod{p^3}.
$$

As an **all-prime generalization**, the first formula is a **conjecture**. This computation is not a proof outside its declared finite domain. The tested classes mod24 cover all eight nonmultiples of 3, counts: 1:46, 5:57, 7:54, 11:54, 13:53, 17:55, 19:54, 23:55.

Define the original-stream fourth digits \(\alpha_p=(W_p-\chi_pp)/p^3\bmod p\) and \(\beta_p=(S_p-\chi_pp)/p^3\bmod p\), justified by the established finite-domain mod-\(p^3\) relations. Then \(\alpha_p=2\beta_p\pmod p\) throughout the domain. Define the next bridge digit \(\gamma_p=(W_p-2S_p+\chi_pp)/p^4\bmod p\). In the 428-prime finite domain, \(\gamma_p\ne0\) for **426** primes, with \(\gamma_5=\gamma_7=0\) only; in particular, \(p=13\) is a fixed counterexample to a universal \(p^5\) strengthening.

| p | chi | alpha | beta | gamma |
|---:|---:|---:|---:|---:|
|13|+1|9|11|9|
|19|+1|12|6|14|
|373|+1|228|114|174|
|1171|+1|182|91|700|
|2999|-1|2124|1062|2396|

Original **exact** integer residues mod (p^5):
- p=373: W=2934720761840, S=3393369805886.
- p=1171: W=1724529065659850, S=1305075625589586.

These retain the full signs, weights, original integer binomial provenance and p-adic digit observer. Auxiliary p-adic digit coordinates are NOT P000 native X6 coordinates.

## Full reproducibility recipe / finite computation certificate

Initialize \(a_0=b_0=1\) with the exact original coefficient ratios

$$
\frac{a_{k+1}}{a_k}=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3},
\qquad
\frac{b_{k+1}}{b_k}=\frac{(4k+1)(2k+1)(4k+3)}{288(k+1)^3}.
$$

For each prime \(5\le p\le3000\) (deterministic sieve), calculate in \(\mathbb Z/p^5\mathbb Z\). For \(k=0,\ldots,p-1\) add \((6k+1)a_k\) and \((8k+1)b_k\) to \(W,S\) respectively, then apply the recurrences only if \(k<p-1\). Every \((k+1)^{-1}\) used is a unit because \(k+1<p\). Assert the \(p^3\) residues and \(p^4\) bridge and record \(\gamma_p\). This stand-alone Python standard-library verifier computes the entire finite proposition:

```python
from math import isqrt
isprime=[True]*3001
isprime[0]=isprime[1]=False
for d in range(2,isqrt(3000)+1):
    if isprime[d]:
        for j in range(d*d,3001,d): isprime[j]=False
total=0; fifth_zeros=[]; census={r:0 for r in (1,5,7,11,13,17,19,23)}
for p in range(5,3001):
    if not isprime[p]: continue
    M=p**5; a=b=1; W=S=0
    i36=pow(36,-1,M); i288=pow(288,-1,M)
    for k in range(p):
        W=(W+(6*k+1)*a)%M
        S=(S+(8*k+1)*b)%M
        if k<p-1:
            inv=pow(k+1,-3,M)
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*i36*inv%M
            b=b*(4*k+1)*(2*k+1)*(4*k+3)*i288*inv%M
    chi=1 if p%3==1 else -1
    assert W%p**3==chi*p%p**3 and S%p**3==chi*p%p**3
    q=(W-2*S+chi*p)%M
    assert q%p**4==0
    if q//p**4==0: fifth_zeros.append(p)
    total+=1; census[p%24]+=1
assert total==428 and fifth_zeros==[5,7]
assert census=={1:46,5:57,7:54,11:54,13:53,17:55,19:54,23:55}
```

A **second** original-binomial implementation using independent `math.comb` summation was executed on 27 test primes (all primes <=101 plus 373,1171,2999), matching both weighted residues mod p⁵. This is an arithmetic cross-check, not an independent author review. The complete author checker hashed the prime-ordered full records `p:W_mod_p5:S_mod_p5:chi:gamma\n` to SHA256:
`ed7676f565c03f733b1631d2ee424b55c49af4dde589241dc850ff8390696c56`.
The full Python checker and computed JSON were provided as author-side conversation evidence under names `d25_fourth_digit_two_model_bridge_20261102.py` and `d25_fourth_digit_two_model_bridge_20261102.check.json`.

## Scientific continuation

The original D25 mother target remains **OPEN**: \(\Delta_p-R_p\equiv0\pmod p\) for \(p\equiv13,19\pmod{24}\), equivalent under accepted D24 UR/signed Clausen reductions to \(W_p\equiv p\pmod{p^3}\). The **new scientific unit** is the distinct 4th-digit correlation of two *original* streams. Previous separate correct weighted Picard–Fuchs gauges are already recorded at \`research_notes/portable_direct/20261102_onhour_d25_weighted_gauged_pf_endpoint.md\` and need not be rederived.

Next discriminating step: construct a finite joint **weighted original 216↔2304 WZ or normalized Gauss–Manin connection** explaining \(\alpha_p=2\beta_p\), proving at least the required target-class mod-\(p^3\) relation, and retaining the signed Clausen source cutoff, twist, exact original weighted jets and both PF endpoint defects. At \(p=373\), test against original digits 228 and 114 and next bridge digit 174. This finite fourth-digit correlation is a route discriminator, not a universal theorem. A direct original \(\Delta_p-R_p\) proof is also admissible.

**Separate native experiment still open:** exact same-original-class fixed-\(p=373\) H0/B0 divided-power \([X]U\bmod139129\), module rank, true semilinear Frobenius and normalization \(\eta\), odd signed Green/Hesse, \(\kappa\), and independently reproducible native execution. Support Issue \`awdawmip/enterprise-math#1559\` remains PENDING_OWNER/NOT_EXECUTED. No portable weighted scalar, point count or jet substitutes for that original object.

**Execution and Source:** original dispatch `research-onhour-20261031-0205-dispatch-r15` at `awdawmip/kimi-query-bridge#6633` has confirmed terminal `FAILED / UPSTREAM_CODE_REVIEW_REQUIRED`; never blind-reissue. Read-only gateway 0.6.11 in this run reported no Research execution authorization, no executor binding and 5/5 active control jobs. No own authenticated native session/claim/run, checkpoint, Result, freeze or review is claimed. `REGISTER_PENDING / SYNC_DEBT` remains for formal research ingestion. Current mathematical source is frozen at the cited pin; this neutral research note does not rebase it. No scheduler or notification settings modified.


## Independent original weighted-jet discriminator (same research turn, second scientific unit)

The scalar fourth-digit relation \(\alpha_p=2\beta_p\) **does not imply** the naive weighted first-jet relation \((\theta Y_p)(1/2)=2(\theta Z_p)(1/9)\bmod p\), where \(Y_p=(1+6\theta)F_p\), \(Z_p=(1+8\theta)H_p\), \(\theta=z\,d/dz\), and \(F_p,H_p\) are the two original full-period unweighted sums. Direct integer binomial computation of every original coefficient and the independent rational-recursion construction gave:

| p | weighted W mod p | weighted S mod p | theta Y(1/2) mod p | theta Z(1/9) mod p | theta Y−2 theta Z mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 3 | 7 | 2 |
| 19 | 0 | 0 | 12 | 5 | 2 |
| **373** | 0 | 0 | **292** | **77** | **138** |
| 1171 | 0 | 0 | 760 | 886 | 159 |

At p=373 the original full-weighted fourth digits obey \(\alpha_{373}=228=2(114)=2\beta_{373}\pmod{373}\), while the **first derivative jets** obey \(292-2(77)=138\ne0\pmod{373}\). Thus the naive derivative transfer is refuted at the frozen diagnostic prime. A genuinely normalized **3x3 weighted-jet** transport remains open, with the 138 mismatch serving as an essential signed diagnostic rather than a barrier to more general transports. This retains full original weights and classical observer distinctions; it is not the native fixed-class H0/B0 run.

Execution evidence: author-side script \`d25_jet_readout_discriminator_20261102.py\`, output \`d25_jet_readout_discriminator_20261102.check.json\`. Both independent original-integer binomial and modular-recursive readouts matched on four primes. Next exact scientific step should preserve both the scalar digit ratio 228:114 and the nonzero weighted first-jet discrepancy 138 for p=373, or pursue direct signed Clausen \(\Delta_p-R_p\) proof. No original native benchmark was claimed.
