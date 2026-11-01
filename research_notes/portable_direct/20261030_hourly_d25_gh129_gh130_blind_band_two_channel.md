# D25/LIFT GH-129–GH-130: Lucas-blind first band and a p=3347 two-channel certificate

Date: 2026-10-30 Asia/Hong_Kong. Author-side portable work. Research conversation: `chatgpt-research-hourly-enterprise-math-20260923`. Parent Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged. Status `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`.

## Precise setup

For every odd prime p≥5 put q=p², N=(p−1)/2, e=(q−1)/2=N(p+1), and let B belong to k=F_q. Define g_B(X)=X²+X+B, f_B(X)=Xg_B(X), H_p(B)=[X^N]g_B(X)^N. The GH-124 character moment is

S_r(B)=Σ_(x∈k; f_B(x)≠0) χ_q(f_B(x))(x/f_B(x))^r, with χ_q(y)=y^e for nonzero y.

### GH-129. Exact full-index coefficient extraction

**Theorem 1.** For all integers 0≤r<e and every B∈k, including singular parameters,

**S_r(B)=−[X^e](X²+X+B)^(e−r).**

**Proof.** On f_B(x)≠0, the summand equals x^e g_B(x)^(e−r). When f_B(x)=0 this polynomial also vanishes: either x=0 or g_B(x)=0, using e−r>0. Hence the punctured sum equals the full polynomial sum. Its exponents lie between e and 3e−2r<4e=2(q−1), and the only positive multiple of q−1 in that range is 2e. Since Σ_(x∈F_q)x^(2e)=−1 and every other exponent in the range has zero power sum, the claimed coefficient formula follows. QED. The case r=e is deliberately excluded; GH-128 supplies its separate root-support correction.

**Theorem 2.** For each 1≤s≤N set r=N+s, and define

C=[X^N]g_B^(N−1), D=[X^(N−1)]g_B^(N−1),
A_s=[X^N]g_B^(p−s), E_s=[X^(3N+1)]g_B^(p−s).

Then the **entire adjacent Lucas-blind band** admits the exact two-channel formula

**S_(N+s)=−A_s C^p−E_s D^p**, with
**C=H'_p(B)/N**, **D=H_p(B)−2B H'_p(B)/N**.

**Proof.** e−(N+s)=Np−s=(p−s)+p(N−1). Thus g_B^(e−r)=g_B^(p−s)(g_B^(N−1))^p. For its coefficient of X^e, only exponent pairs (N,N) and (3N+1,N−1) can occur (second entry is multiplied by p): the first-factor degree is at most 2(p−s)<2p and the second degree at most 2N−2<p. This proves the two summands. Differentiate H_p(B)=[X^N]g_B^N to obtain H'_p=NC. Put F=[X^(N−2)]g_B^(N−1). Multiplying g_B^(N−1) by g_B gives H_p=F+D+BC. Comparing [X^(N−1)] in the derivative of g_B^N with respect to X gives H_p=2F+D. Eliminating F yields D=H_p−2BC. Because 0<N<p, division by N is valid. QED.

For s>(N+1)/2, E_s=0 by degree. At B=0 the formula reduces, using Lucas, to S_(N+s)(0)=−binom(p−s,N+s) if 2s≤N+1 and 0 otherwise. Thus the blind band has both nonzero and zero examples; no all-zero extension of GH-127 is valid.

**BRC readout:** GH-127's corrected Lucas-visible matrix is a one-channel Frobenius outer product on its exact window. The new carry band has a natural two-channel coefficient readout (C^p,D^p), retaining the marked branch and root-support semantics. This is not a global minimal-encoding claim or a native X6 geometry theorem.

### GH-130. Exact marked p=3347 certificate

Use the original marked parameter T=2√2/3 and B=(1+T)/8 in F_3347[√2], where √2 has square 2 and Frobenius conjugates its sign. Encode (a,b)=a+b√2 mod 3347.

p=3347, N=1673, e=5,601,204. Independent multinomial-coefficient and differential-recurrence algorithms both obtained:

| Quantity | Exact (a,b) |
|---|---|
| B | (2092,279) |
| H_p(B) | (783,0) |
| H'_p(B) | (0,1351) |
| C | (0,645) |
| D | (568,2349) |
| A_1 | (3052,295) |
| E_1 | (2167,0) |
| **S_1674(B)** | **(3179,0)** |
| **S_1675(B)** | **(0,2701)** |

Also S_1(B)=2H'_p(B)H_p(B)^p=(0,362), matching the prior independent GH-125 exhaustive finite-field computation. At s=1,2, the coefficient matrix rows (A_s,E_s) have determinant **A_1E_2−A_2E_1=72≠0 (mod 3347)**. Thus the two natural coefficient rows are linearly independent for this marked instance. In particular S_1674(B)=3179 is nonzero in F_3347.

Actual local checks: 69 direct F_(p²) character-moment comparisons across five (p,B) cases p=11 (two B), 19, 43 and 59, including original punctured sums at both blind-band endpoints; 72 independent coefficient recurrence comparisons, including p=3347 at s=1,2,N. The recurrence uses gP'=Lg'P and the reciprocal polynomial 1+X+BX²; it does not reuse the multinomial coefficient routine. All reported comparisons passed. The 3347²-element direct sum was **not repeated** this turn; the p=3347 certificate is a rigorous symbolic coefficient calculation backed by two exact programs and the GH-125 first-moment crosscheck.

Finite-only diagnostic: for all 1,659 tested pairs (p,s), with 19 primes 11≤p<400, p≡3 (mod 8), and original marked B, the odd-s blind moments lie in F_p and even-s moments in √2 F_p. This is **conjectural for the full prime family** pending a marked conjugation involution proof or counterexample. No all-prime claim is made from the scan.

## Evidence and task continuation

Executed local scripts `d25_gh129_blind_band_check.py`, `d25_gh130_blind_band_recurrence_check.py`, `d25_gh130_parity_diagnostic.py` and stdout logs are retained together in this turn's portable research package. Prior inputs: GH-124–GH-128; GH-127 proof Git blob `2ad3c201757c02083fb92a66a81ebc8a5375ea1d` at commit `df49902b8d7dca20b526fd54101057b3a0770e76`. No formal author-independent review, Mathlib proof, originality priority, or Source scientific admission is claimed.

The branch tuple (x,f_B(x),χ_q(f_B(x)),r,B), signed weight, Frobenius and punctured root support remains the carrier. Compression to a scalar or rank-one corrected visible window is not sufficient for arbitrary later carry-band observations.

**Next exact science:** seek an independent marked CM/Jacobi/Gauss or p-adic-period evaluation of the original S_1 at T²=8/9 without assuming GH-83 or repeating GH-98–GH-103 finite-log-moment equivalences. The finite conjugation pattern offers an optional separate line. Preserve GH-3, R_3347(9), the native p=373 experiment and each independent evidence obligation.

Authenticated Gateway 0.6.11 at this turn reported research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED, active native jobs=5/5. The connected interface exposes no callable recovery_status; prior own-lane recovery/continuation and protected old staging are in Enterprise Math #1558. No new session, Claim, authorized Open, native checkpoint, freeze or review has been performed; the controller must recover lawful current Source authority and exact successor CAS before formal continuation. Historical request IDs are preserved.
