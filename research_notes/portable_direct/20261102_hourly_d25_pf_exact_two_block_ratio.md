# D25: exact two-block formula for the normalized 216↔2304 Picard–Fuchs boundary ratio

Date: 2026-11-02 (Asia/Hong_Kong). Status: AUTHOR-DERIVED / EXACT RATIONAL IDENTITY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Source: frozen D25 Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, original scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Previous source-bound author result: `research_notes/portable_direct/20261102_hourly_r11_d25_pf_fourth_digit_cross_boundary.md`. This is a portable arithmetic result, not native H0/B0 execution, CLAIM, Source checkpoint or Result.

## Exact theorem (every prime p >= 5)

Let `k=p-1`, `theta=z d/dz`, and

- `F_A(z)=sum_{j=0}^{p-1} c_{A,j} z^j`, with `c_{A,j}=(1/2)_j(1/3)_j(2/3)_j/(j!)^3=(2j)!(3j)!/[108^j(j!)^5]`;
- `F_B(z)=sum_{j=0}^{p-1} c_{B,j} z^j`, with `c_{B,j}=(1/4)_j(1/2)_j(3/4)_j/(j!)^3=(4j)!/[256^j(j!)^4]`.

Set `L_i=theta^3-z (theta+alpha_{i,1})(theta+alpha_{i,2})(theta+alpha_{i,3})`, with parameters as above. Define the *source-tagged, unweighted finite-boundary observations*

`E_A=(L_A F_A)(1/2)/p^3`, `E_B=(L_B F_B)(1/9)/p^3` in `Z_(p)`.

Prior exact finite Picard–Fuchs endpoint cancellation establishes

`L_i F_i(z)=-c_{i,p-1} prod_alpha(p-1+alpha) z^p`, and `v_p(c_{i,p-1})=3`.

Thus both `E_A,E_B` are p-adic units, and their **exact rational quotient** (not merely a congruence) obeys

> **`E_A/E_B = (16/3) (32/3)^(p-1) * W_1(p)/W_3(p)`**, where
> `W_r(p)=prod_{j=1}^{p-1}(rp+j)`.

### Proof

Substitute the original factorial coefficients at `k=p-1` and cancel the shared `(p-1/2)` endpoint factor:

`E_A/E_B = [ (2p-2)!(3p-3)! / ((p-1)!(4p-4)!) ] * (256/108)^(p-1) * [(p-2/3)(p-1/3)/((p-3/4)(p-1/4))] * (9/2)^p`.

For `1<=b<=p`, exact factorial splitting into whole p-blocks and the final omitted tail yields

`(ap-b)! = p^(a-1)(a-1)! [prod_{r=0}^{a-1} W_r(p)] / [prod_{j=1}^{b-1}(ap-j)]`.

Apply the identity to `(a,b)=(2,2),(3,3),(4,4)` and divide by `(p-1)!=W_0`:

`(2p-2)!(3p-3)!/[(p-1)!(4p-4)!] = (1/3) [(4p-1)(4p-2)(4p-3)]/[(2p-1)(3p-1)(3p-2)] * W_1/W_3`.

The remaining endpoint fraction is

`(p-2/3)(p-1/3)/[(p-3/4)(p-1/4)] = (16/9) [(3p-2)(3p-1)]/[(4p-3)(4p-1)]`.

All p-dependent linear factors cancel, using `(4p-2)/(2p-1)=2`. The scalar/power terms reduce to `(16/3)*(32/3)^(p-1)`, proving the exact identity in `Q`.

## Interpretation and next unit

The earlier mod-p boundary ratio `E_A/E_B=16/3 (mod p)` is the first observer quotient of this exact identity. For higher precision, the two **composite-index block products** `W_1/W_3` are retained as a genuine source carrier. Next unit: determine the strongest uniform p-adic truncation of `W_1/W_3` and identify its first nontrivial harmonic residual, without deleting the original signed 216 tail or the 13/19 resonance distinctions.

BRC interface: full finite index population, original numerator factorials, p-power divisibility, PF boundary source, rational observation point, index-block products. The declared future operations are normalized boundary ratios modulo p^2 through p^4; the exact quotient is a complete sufficient carrier for these operations. No claim is made about signed weighted complete sums or arbitrary native X6 states.
