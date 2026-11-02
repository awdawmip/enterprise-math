# D25: sixth/seventh boundary digits and exact harmonic residual after source normalization

Date: 2026-11-02 (Asia/Hong_Kong). Status: AUTHOR-DERIVED / EXACT PROOF / FINITE EXACT CHECK (428 PRIMES) / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Predecessor: `20261102_hourly_d25_pf_exact_two_block_ratio.md`; same frozen D25 publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Mathematical notation `E_A,E_B,W_r` is defined in the predecessor. This author-side result is not native Source admission.

## Theorem (all primes p>=5)

In `Z_(p)`, define `H_m=sum_{j=1}^{p-1}j^(-m)` for `m=1,2,3`. Then

> **`W_1(p)/W_3(p) = 1 + 5 p^2 H_2 (mod p^4)`**.

Consequently, the exact source-labeled boundary quotient satisfies

> **`E_A/E_B = (16/3)*(32/3)^(p-1) * (1+5p^2 H_2) (mod p^4)`**.

Here `H_2=0 (mod p)`, so the quotient has no block correction through `p^3`. Its first possible nonzero block correction is the source-specific digit

> **`(W_1/W_3-1)/p^3 = 5(H_2/p) (mod p)`**.

The corrected residual is a finite reciprocal-square observer of the entire `1..p-1` index population, not a fitted parameter. At the next precision, the full `W_1/W_3` remains the exact carrier.

### Elementary proof without external Bernoulli input

By the cyclic structure of `F_p^*`, `H_1,H_2,H_3 = 0 (mod p)` for every `p>=5`. The permutation `j->p-j`, expanded through `p^3`, gives

`2H_1 = -pH_2-p^2H_3 (mod p^3)`.

Therefore `H_1=0 (mod p^2)` and `2H_1=-pH_2 (mod p^3)`.

Put `W_r=prod_{j=1}^{p-1}(rp+j)`. Dividing by `W_0=(p-1)!` and applying the p-adic logarithm to each unit `1+rp/j` gives, modulo `p^4`,

`log(W_1/W_3) = -2pH_1+4p^2H_2-(26/3)p^3H_3`.

The final term vanishes modulo `p^4`. Using `-2pH_1=p^2H_2 (mod p^4)` yields `log(W_1/W_3)=5p^2H_2 (mod p^4)`. Its valuation is at least three, so exponentiation does not add terms modulo `p^4`, proving the theorem. All logarithmic denominators used at orders <=3 are p-units for p>=5.

## Explicit fifth-digit additive defect (all primes p>=5)

Define the integer Fermat quotients `q_p(a)=(a^(p-1)-1)/p` for `a=2,3`. From the exact ratio and `E_B=-1/96 (mod p)` one obtains

> **`3E_A-16E_B = (p/6)[q_p(3)-5q_p(2)] (mod p^2)`**.

This sharpens the predecessor's `3E_A-16E_B=0 (mod p)` and identifies a concrete Fermat-quotient source at the next digit. It does not require a general nonvanishing assertion for `q_p(3)-5q_p(2)`.

For the multiplicative ratio, equivalently,

`E_A/E_B=(16/3)*(32/3)^(p-1) (mod p^3)`.

The first potential correction to that normalized ratio is `5p^2H_2` at modulus `p^4`. The additive and multiplicative digit labels refer to these precisely specified, different observers.

## Actual exact certificate

The accompanying standard-library checker `d25_boundary_block_ratio_20261102.py` independently constructs `(c_{A,p-1}/p^3,c_{B,p-1}/p^3)` by stripped factorial products **and** by the two original Pochhammer linear-factor products; it evaluates the original PF endpoints, compares the exact block quotient modulo `p^4`, and verifies both the harmonic and Fermat-quotient congruences. All **428 primes `5<=p<=3000`** pass, without floating-point approximation. Selected `(p, (3E_A-16E_B)/p modp, (W_1/W_3-1)/p^3 modp)` are

`(5,1,0), (7,4,3), (13,1,8), (19,10,12), (37,33,19), (373,191,95), (1171,286,99)`.

Within this finite 428-prime domain the first additive defect digit is nonzero for every tested prime; the first block residual vanishes for `p=5` and is nonzero for the other 427 tested primes. These are finite arithmetic observations, not infinite nonvanishing theorems.

## BRC / frozen mother continuation

The precise observer space is the original A/B finite hypergeometric coefficient families at `z_A=1/2`, `z_B=1/9`, together with their PF boundary operators and p-adic division. The quotient normalization absorbs the known power `(32/3)^(p-1)` while the joint block source `W_1/W_3` retains composite-index relations. The p-adic safe quotient through `p^3` is proven; the harmonic repair is retained at `p^4`. No signed cancellation, Clausen cutoff, q-transport, or CM jet is silently replaced by this boundary result.

**Next executable scientific question:** test whether the pair of normalized *local* CM jet operators can be coupled by a genuinely non-scalar, source-labeled connection that respects this now-exact boundary factor, the different 13/19 resonances, the original weighted signed readout, and the five p373 witnesses `228:114,138,365,316,91`. A finite candidate must be tested against the original `S_p-T_p (mod p^3)` and cannot be accepted from boundary matching alone. Frozen mother `Delta_p-R_p=0 mod p` for target p mod24 in {13,19} remains open.

Current native control observed 2026-11-02T01:22:50Z: Gateway 0.6.11, `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, active jobs 5/5. The own Research lane's recovered service session pointer (bridge #6637) and definitively failed #6638 continuation are historical, read-only references. This proof is `UNREVIEWED/NOT_ADMITTED/REGISTER_PENDING`; no new CLAIM/OPEN/Source checkpoint/Result or native H0/B0 is asserted. Support stays with existing #1558 and #1559 owners. P000 and ACTIVE worldview unchanged.
