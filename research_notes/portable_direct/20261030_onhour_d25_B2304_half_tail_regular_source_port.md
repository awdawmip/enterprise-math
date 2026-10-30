# D25 / SECOND-DIGIT-LIFT — B2304 half-tail cancellation and regular terminating source kernel

Date: 2026-10-30 Asia/Hong_Kong. Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; NOT the maintenance lane. Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.**

Status: **AUTHOR-SIDE / PROVED GZ-DEPENDENT ALL-PRIME COROLLARY AND EXACT REGULAR KERNEL / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING**. This document does not claim current Source claim/session/run or native H0/B0 experiment.

## 1. Exact prior and previously unused half-truncation

Define in Z_(p), p>3 prime,
\[
 b_n=\frac{\binom{2n}{n}^{2}\binom{4n}{2n}}{2304^n}
     =\frac{(4n)!}{(n!)^4\,2304^n},\quad
 B_p(N)=\sum_{n=0}^{N}(8n+1)b_n,\quad
 \chi_p=\left(\frac{-3}{p}\right).
\]
**Guo--Zudilin**, *A q-microscope for supercongruences*, Adv. Math. 346 (2019), 329–358, equations (2) and (3), established BOTH
\[
 B_p(p-1)\equiv p\chi_p\pmod{p^3},\qquad
 B_p((p-1)/2)\equiv p\chi_p\pmod{p^3}
\]
for every prime p>3. Source: https://arxiv.org/pdf/1803.01830 (pp. 1–2); DOI 10.1016/j.aim.2019.02.008. Both the original integer-binomial numerator and denominator 2^(8n)3^(2n)=2304^n match. These are **external previously proved results**, not claims of new proof by this author. Our previous source note \`20261030_onhour_d25_A216_B2304_proved_priors_minimal_bridge.md\` already consumed the full truncation: do not recredit it.

Their difference proves the source-labeled **upper-half cancellation**
\[
 \boxed{\sum_{n=(p+1)/2}^{p-1}(8n+1)b_n\equiv0\pmod{p^3}.}\tag{GZ-half-tail}
\]
This is cancellation of a signed/weighted tail, NOT termwise p^3 divisibility. Since \(v_p(b_n)=\lfloor4n/p\rfloor\) for n<p and p>3, put
\(n_0=(p+1)/2,\ n_3=\lfloor(3p-1)/4\rfloor,\ L=n_3-n_0\). Then
\[
 \boxed{\sum_{n=n_0}^{n_3}(8n+1)b_n\equiv0\pmod{p^3}.}\tag{1}
\]

## 2. Direct algebraic p-local normalization and natural termination

For 0≤q<p, 0≤r<p, separating all multiples of p in (qp+r)! and using Wilson gives
\[
 \frac{(qp+r)!}{p^q}\equiv(-1)^q q!\,r!\pmod p.\tag{2}
\]
For \(n_0=(p+1)/2\), (2) yields \((4n_0)!/p^2=(2p+2)!/p^2\equiv4\pmod p\). Wilson gives \(n_0!^4\equiv1/16\pmod p\); as 2304=48^2, Euler's criterion gives \(2304^{n_0}\equiv2304\pmod p\). Therefore
\[
 \boxed{b_{n_0}/p^2\equiv 1/36\pmod p.}\tag{3}
\]
The exact coefficient recurrence
\[
 \frac{b_{n+1}}{b_n}=\frac{(4n+1)(4n+2)(4n+3)}{576(n+1)^3}
\]
specializes modulo p at n=n_0+s to the **p-unit** recurrence
\[
 r_0=1,\qquad
 r_{s+1}=r_s\frac{(4s+3)(s+1)(4s+5)}{18(2s+3)^3}
 \pmod p,\quad 0\le s<L.\tag{4}
\]
For all used s, \(2s+3<p\), hence denominators are invertible. Furthermore, \((4L+3)(4L+5)\equiv0\bmod p\), placing the first zero factor in the numerator after the last included term: **natural termination without a singular denominator**. By (3)–(4),
\[
 \frac{(8(n_0+s)+1)b_{n_0+s}}{p^2}
 \equiv\frac{(8s+5)r_s}{36}\pmod p.
\]
Combining with (1), get the **all-prime regular-kernel corollary**
\[
 \boxed{H_p^{(2304)}:=\sum_{s=0}^{L}(8s+5)r_s\equiv0\pmod p,\quad p>3.}\tag{B-REG}
\]
Proof strength: rigorous elementary transformations **conditional only on the cited proven Guo–Zudilin theorems**; not an independently new supercongruence.

## 3. Two nontrivial signed source ports must survive before summation

Split the upper-half window at \(n_2=\lfloor(2p-1)/3\rfloor\). Let
\[
 T_p^{(1)}=p^{-2}\sum_{n=n_0}^{n_2}(8n+1)b_n,\quad
 T_p^{(2)}=p^{-2}\sum_{n=n_2+1}^{n_3}(8n+1)b_n
 \quad(\bmod p).
\]
Both quotients exist in Z_(p), and \(T_p^{(1)}+T_p^{(2)}=0\bmod p\) follows from (1). Neither port can be individually erased for all p:

| p | n0 | n2 | n3 | T1 mod p | T2 mod p | H1 mod p | H2 mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 8 | 9 | 7 | 6 | 5 | 8 |
| 19 | 10 | 12 | 14 | 3 | 16 | 13 | 6 |
| 373 | 187 | 248 | 279 | 92 | 281 | 328 | 45 |

Here H1,H2 denote separate sums of (8s+5)r_s on the respective windows. The exact change of observer is \(T_i=H_i/36\) mod p. Both branches are nonzero at each displayed target; only their aggregate vanishes. This is a concrete BRC signed-fiber non-redundancy witness. Individual original indexes, first/second source ports, v_p=2, and signed weights remain retained for any later Green/Hesse/κ operations. The weighted index at \(8n+1\equiv0\bmod p\) is \(n_*=((p\bmod8)p-1)/8\), which lies in the B upper half for p≡13 mod24 (p mod8=5) but in the lower half for p≡19 mod24 (p mod8=3): preserve this class-dependent provenance.

## 4. Smaller exact bridge object and unfinished question

Retain the original separate A216 coefficients
\[
 a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n,\quad
 A_p=\sum_{n=0}^{p-1}(6n+1)a_n,\quad
 D_p=A_p-2B_p(p-1)+p\chi_p.
\]
For frozen target p=6m+1≡13,19 mod24, \(\chi_p=1\). A terms n≥4m+1 have \(v_p(a_n)\ge3\); B upper-half weighted sum is zero mod p^3 **by (GZ-half-tail)**. Thus the following *source-faithful* exact reduction holds:
\[
 \boxed{
 D_p\equiv p+\sum_{n=0}^{3m}\bigl((6n+1)a_n-2(8n+1)b_n\bigr)
 +\sum_{n=3m+1}^{4m}(6n+1)a_n\pmod{p^3}.
 }\tag{MIN-BRIDGE}
\]
The last A middle port is generally NONZERO after dividing by p²; the earlier author-checked A216 signed regular kernel applies to this precise window. This theorem does **not** establish D_p≡0 mod p^3. It removes one full B upper-half *aggregate* only for the declared linear observer and precision. It is not permission to discard the B source terms before later non-linear, indexed, or native operations; the two port residues above witness why.

**Next unfinished mathematical unit:** obtain a uniform relation for the remaining low-index cross-model signed difference (n≤3m), with its A middle correction and class-dependent character; prove/kill D_p≡0 mod p³. Do not re-prove known GZ, source reflection, A regular-tail or auxiliary moment endpoints.

**Independent highest-priority native obligation remains:** https://github.com/awdawmip/enterprise-math/issues/1559 — execute fixed p=373 same-original-class H0/B0 divided-power \([X]U\bmod139129\), rank, real semilinear Frobenius direction/eta, signed odd Green/Hesse, κ and independent replication. B2304 scalar kernel is NOT that native object; no owner or pass inferred.

## 5. Execution / provenance / formal-control limits

Executed Python 3 standard-library exact-modular checker \`d25_b2304_half_tail_regular_guard_20261030.py\`. It tested all 667 primes 5≤p<5000 (166 frozen target primes) for B-REG; recomputed original full/half weighted binomial sums modulo p³, factorial-form independently sampled terms, both source ports and regular H1/H2 at p=5,7,13,19,61,67,373. Outputs: \`REGULAR_KERNEL_EXACT_PRIMES 667\`; \`FROZEN_TARGET_PRIMES 166\`; \`PASS_B2304_GZ_TWO_TRUNCATION_TAIL_AND_REGULAR_KERNEL\`. This finite execution is not the universal proof; (2)–(4) and GZ supply that proof.

BRC / Enterprise coordinates: **COMPOSE_APPLIED** to the signed p-local, source-labeled original two-model coefficient carrier (model, index, valuation, weighted residue, original p-local denominator, characteristic sign). No invented native X6 coordinate or substitution for H0/B0. Frozen source pin not reinterpreted or rebased. This is author-only durable scientific material, **UNREVIEWED / NOT_ADMITTED**; no session/CLAIM/run/Source checkpoint/Result/freeze/review acquired. Source gateway Site checked at 2026-10-30 08:01 UTC: \`research_authority_granted=false\`, \`write_relay_enabled=false\`; own checkpoint list returned \`ACCESS_DENIED\`. Formal source role registration/checkpoint are pending, no alternative identity borrowed; original pending requests must be reconciled before any reissue.
