# D25 — S2304 B2 is an all-prime consequence of Guo–Zudilin (2026-11-02)

**Classification:** EXACT SOURCE-CONSEQUENCE / PROOF BY PUBLISHED THEOREM + LEGENDRE VALUATION / AUTHOR-SIDE DERIVATION / INDEPENDENT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINT.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` only. The 107-prime B2=0 observation was previously reported at `b46bb821037ee7f21ca0598be6a53d2fee9a655f`; this note discharges its *universal* scope from existing literature, not as a newly discovered external theorem.

## Exact observer and proved result

Let `p>3` be prime, `H=(p-1)/2`, `E=floor((3p-1)/4)`, and

```text
alpha_S(k) = (4k)! / ((k!)^4 * 2304^k)
S(N) = sum_{k=0}^N (8k+1) alpha_S(k)
U_p(k) = p^{-v_p(alpha_S(k))} alpha_S(k) in Z_p^x
B2_S(p) = sum_{k=H+1}^E (8k+1) U_p(k) mod p
```

**Theorem (exact corollary, ALL primes p>3):** `B2_S(p)=0 mod p`.

**Proof.** Guo and Zudilin, *A q-microscope for supercongruences*, Adv. Math. **346** (2019), 329–358, Theorem 1.1 and its `q→1` specialization, prove for every prime p>3:

```text
S(p-1) = p * (-3/p) mod p^3,
S((p-1)/2) = p * (-3/p) mod p^3.
```

Here `(-3/p)` is the Legendre symbol. Both series have **exactly the original denominator 2^(8k) 3^(2k)=2304^k**, factorial ratio and weight `8k+1`, so no normalization change is needed. Subtraction yields `sum_{k=H+1}^{p-1}(8k+1) alpha_S(k)=0 mod p^3`.

For `0<=k<p`, Legendre's formula gives `v_p(alpha_S(k))=floor(4k/p)`, because `p∤2304` and `v_p(k!)=0`. Thus the exact low-index valuation is **2** for `H<k<=E`, and at least **3** for `E<k<p`. Dividing the difference by `p^2` and reducing modulo p yields `B2_S(p)=0`. QED.

This is a source-specific **weighted signed tail observer**: the proof preserves the original finite population, weight, denominator, valuation and cutoff. It does not erase individual source terms or their next p-adic digit.

**Multi-scale corollary:** Specializing the same Guo–Zudilin Theorem 1.1 at `n=p^r` yields, for every `r>=1`, `S(p^r-1)-S((p^r-1)/2)=0 mod p^(r+2)`, because `[n]Φ_n(q)^2` specializes to `p^r*p^2`. This is a difference of original complete/half sums, not an H0/B0 assertion nor a claimed `p^(3r)` bound.

## Direct consequence for the existing D25 three-port decomposition

The previous exact ordinary valuation-two factorization was

```text
T2_S / p^2 = (8*M2+6*M1+M0)*B2_S + A1*B1 + A2*(M0+8*M1)  (mod p).
```

The established first term vanishes **without a CM hypothesis** for all `p>3` (using the same defined port ranges). When the separately sourced `M0=M1=0 mod p` conditions hold, the scalar three-port collapses to `T2_S/p^2=A1*B1 mod p`. At p=373 the prior original finite ports give `A1=360, B1=24`, hence `A1*B1=61 mod373`, reproducing the original 2304 ordinary v2 digit. This consumes the previously verified finite evidence rather than rerunning the native H0/B0 benchmark.

## Numerical cross-check / provenance

A second p-free factorial unit implementation independently checked all 428 primes in `5<=p<=3000`, across all eight nonzero residue classes modulo 24; each B2_S was zero. It also independently checked full and half **original weighted recurrence** modulo `p^3` at 13 primes `5,7,11,13,19,23,37,43,61,67,109,139,373`. Finite calculations corroborate the exact deduction; the universal conclusion is supplied by the **published Guo–Zudilin theorem + valuation proof**, not the 428 samples.

Verifier in this commit: `research_notes/portable_direct/d25_s2304_B2_428allprime_verify_20261102.py`. Full local execution result `d25_s2304_B2_source_consequence_20261102.check.json`.

Source: https://arxiv.org/html/1803.01830v6 (Theorem 1.1, introduction equations (2),(3)); DOI https://doi.org/10.1016/j.aim.2019.02.008.

Next unfinished unit: original ordinary valuation-one **second** digit via two source rectangles and low-rank moment transport; then recombine the five signed ports into the frozen Delta−R observer. Native fixed373 H0/B0 at https://github.com/awdawmip/enterprise-math/issues/1559 remains PENDING_OWNER / NOT_EXECUTED.
