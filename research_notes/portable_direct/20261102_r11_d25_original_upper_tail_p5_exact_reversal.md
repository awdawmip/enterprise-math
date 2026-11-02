# D25 — Exact original 216 upper-tail reversal and the next p-adic digit

2026-11-02. Author-side theorem and finite exact replay; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Original D25 task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 remains fixed. This extends, without replacing, the original mod-p^4 upper-tail theorem at 22670bdb8c7fd5130c3ed38e7a11d254d7c0cd2a. The mother goal remains Delta_p-R_p = 0 mod p for p = 13,19 mod 24 and the authentic native p373 H0/B0 experiment.

## Original coefficient, cutoff and source coordinate

For every prime p>3, define the original
  b_k = (1/2)_k (1/3)_k (2/3)_k / ((k!)^3 2^k)
      = C(2k,k)^2 C(3k,k) / 216^k,
  W_p(N) = sum_{k=0}^N (6k+1)b_k,
  h=floor(2p/3), R=floor((p-3)/3),
  T_p=W_p(p-1)-W_p(h).
All b_k are p-integral for k<p. Each of the three Pochhammer factors contributing to b_{p-1} has exactly one factor divisible by p, so v_p(b_{p-1})=3. Retain the **exact original boundary source** A_p=-b_{p-1}/p^3, a p-adic unit. The previous original boundary theorem gives A_p=1 mod p. We make no assumption that A_p=1 mod p^2.

## Theorem 1 — exact terminating reversal over Q

For each r=0,...,R,
$$
\boxed{\frac{b_{p-1-r}}{b_{p-1}} =
 2^r\frac{(1-p)_r^3}{(3/2-p)_r(4/3-p)_r(5/3-p)_r}.}\tag{1}
$$
Consequently, with all signed weights and original source indices retained,
$$
\boxed{T_p=-p^3A_p\sum_{r=0}^{R}(6p-6r-5)
 2^r\frac{(1-p)_r^3}{(3/2-p)_r(4/3-p)_r(5/3-p)_r}.}\tag{2}
$$
These are exact rational identities, not merely congruences. All denominators are p-units for 0<=r<=R.

Proof: From the original coefficient,
 b_{k-1}/b_k = 2k^3/((k-1/2)(k-1/3)(k-2/3)).
Putting k=p-1-t makes the reverse factor
 2(t+1-p)^3 / ((t+3/2-p)(t+4/3-p)(t+5/3-p)).
Taking the ordered product t=0,...,r-1 gives (1). Since 6(p-1-r)+1=6p-6r-5 and b_{p-1}=-p^3A_p, direct summation gives (2). QED.

## Theorem 2 — next full terminal-band digit, modulo p^5

In Z_(p)/p^2 define
$$
d_0=1,\qquad
d_{r+1}=d_r\frac{36(r+1)^3}{(2r+3)(3r+4)(3r+5)},
$$
$$
H_0=0,\qquad H_{r+1}=H_r+
 \frac2{2r+3}+\frac3{3r+4}+\frac3{3r+5}-\frac3{r+1}.
$$
Then for **every prime p>3**, term by term and in the full sum,
$$
\boxed{\frac{T_p}{p^3}\equiv
 A_p\sum_{r=0}^{R}d_r
 \big((6r+5)+p((6r+5)H_r-6)\big)\pmod{p^2}.}\tag{3}
$$
Proof: Expand each ratio in (1) to first order in p. Its numerator contributes -3 sum_{t<r}(t+1)^-1 and the inverse denominator contributes sum_{t<r}[(t+3/2)^-1+(t+4/3)^-1+(t+5/3)^-1], exactly H_r. The p=0 ratio is d_r. Multiply by the exact original signed weight -(6p-6r-5)=6r+5-6p, the exact boundary A_p, and sum. All denominators are units; remainder is p^2 after division by p^3. QED.

Reducing (3) modulo p recovers the previously published mod-p^4 first digit. The new sources needed at the next digit are A_p mod p^2, the logarithmic deformation H_r mod p, and the weight shift -6p. This is an explicit BRC observer-repair certificate: preserving only the earlier first-digit scalar does not allow the specified future division by p^3 followed by mod-p^2 readout.

## Independent executed arithmetic

The accompanying same-commit Python standard-library verifier computes **every original** b_k by its p-integral forward recurrence, checks every reversed weighted original term against (3), and compares the whole tail modulo p^5 for all **428 primes 5<=p<=3000**, i.e. **197723** terminal indices. All pass. For 27 selected primes (all p<=103 and p=373,1171) it independently checks each coefficient against integer binomials. For p=5,7,13,19 it checks the unmodded exact-rational equality (1).

| p | A_p mod p^2 | T_p/p^3 mod p^2 | previous first digit | new second digit |
|---:|---:|---:|---:|---:|
| 5 | 11 | 0 | 0 | 0 |
| 7 | 1 | 20 | 6 | 2 |
| 13 | 79 | 70 | 5 | 5 |
| 19 | 191 | 156 | 4 | 8 |
| 37 | 186 | 803 | 26 | 21 |
| 373 | 63411 | **109567** | **278** | **293** |
| 1171 | 724850 | 825662 | 107 | 705 |

Thus for p=373,
$$
\boxed{W_{373}(372)-W_{373}(248)\equiv
373^3(278+293\cdot373)\pmod{373^5}.}
$$

## Inheritance, status, and next exact action

Reused: original p^4 full-tail proof (22670bdb...), frozen D25 statement and accepted earlier CM0/Clausen/Wilson premises; no repeated proof of those. The carrier is (p,k,r=p-1-k, original rational coefficient, valuation, signed weight, boundary A_p and deformation H_r); the observer is the original signed tail modulo p^5. This is external p-adic scalar arithmetic, not native X6 geometry. The script is finite validation, not a formal checker, mathematical admission, or native H0/B0 experiment.

**Next smallest mother-goal unit:** seek a genuinely matching published theorem or construct a terminating weighted WZ/contiguous certificate for W_p(floor(2p/3)) = p mod p^3 in target classes p=13,19 mod24, checking p=13,19,373 and controls p=5,7. Use (1)-(3) only when p^4/p^5 precision or division by p^3 demands the original-tail repair. Native p373 H0/B0 [X]U/rank/Frobenius/odd signed Green-Hesse-kappa remains unexecuted under existing issue #1559; control support remains #1558.

**Control/source:** 2026-11-02T12:23Z Gateway 0.6.11 returned UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false. Prior ordinary request issue #6637 gives a historical read-only recovery_status, and #6638 gives an exact FAILED continuation; no replay. These historical receipts do not prove present ownership. No current native CLAIM/OPEN/Source checkpoint/Result/admission is asserted. Stable research logical ID specified by user: chatgpt-research-hourly-enterprise-math-20260923; maintenance ID chatgpt-hourly-enterprise-math-20260921 is not used. Other research lanes' service identities are not borrowed. Existing schedule/notifications unchanged.
