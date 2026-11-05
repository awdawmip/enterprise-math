# D25 — Original-216 reflected endpoint and constant-space second-digit certificate

Date: 2026-11-05, Asia/Hong_Kong. TASK_RESEARCH author-side portable mathematical evidence.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
Publication: `TP2-B6F4FC938FF94941C1B7`.
Frozen science pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Status: **AUTHOR-DERIVED GENERAL FINITE-FIELD PROOF / FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED**.
This extends (without recrediting) the 20261105 original-216 upper-strip valuation and O(p)-memory certificate.

## Theorem: universal high-endpoint coefficient and reversed complementary Gauss recurrence

Let `p=6m+1>=7` be prime, `b_0=1`, and for `0<=k<p-1` let
```
 b_(k+1)/b_k=(6k+1)(3k+1)/(36(k+1)^2).
```
Thus `b_k=(1/6)_k(1/3)_k/(k!)^2 * 2^(-k)` in `Z_(p)`.
The established valuation profile is `v_p(b_k)=0,1,2` for the
successive intervals `[0,m]`, `[m+1,2m]`, `[2m+1,p-1]`.
For `1<=r<=m` define `d_r=b_(p-r)/p^2 (mod p)`.

**New exact statements** in `F_p`:
```
d_1 = 1/10
d_(r+1) = d_r * 36*r^2 / ((6*r+5)*(3*r+2))  (1<=r<m)
d_r = (1/10) * 2^(r-1) ((r-1)!)^2 /
                ((5/6)_(r-1) (2/3)_(r-1)).
```
All displayed denominators are units in this stated range.

### Proof of endpoint

The numerator of `b_(p-1)` comprises products `6j+1` and `3j+1` for `0<=j<=p-2`.
In the complete residue set `0<=j<=p-1`, the first progression has exactly
one zero, at `j=m`; the second has exactly one zero at `j=2m`.
Removing that zero and dividing by its single `p` factor leaves the product
of all nonzero residues, `-1` (Wilson's theorem). Each truncated progression
also omits the last index `j=p-1`, whose residues are respectively `-5` and `-2`.
Therefore its stripped product equals `(-1)/(-5)=1/5` and
`(-1)/(-2)=1/2`, respectively, in `F_p`.
The denominator `36^(p-1)((p-1)!)^2` is `1` modulo `p` by Fermat and
Wilson. Hence `b_(p-1)/p^2=1/10` modulo `p`.
For descending indices, invert the unit recurrence at `k=p-r-1`:
`b_(p-r-1)/b_(p-r)=36(p-r)^2/((6(p-r-1)+1)(3(p-r-1)+1))`.
Reducing modulo `p` yields the displayed `d_(r+1)/d_r`.
Its product is the terminating complementary Gauss expression above.

## Fused constant-space high-strip observer

Define the *original 216* Clausen high tail
```
T_p = sum_{0<=i,j<p; i+j>=p} (6(i+j)+1)b_i*b_j.
```
The already proved valuation support theorem yields `p^2|T_p` and
`T_p/p^2 = 2 sum_(i=1)^m b_i * sum_(r=1)^i (6(i-r)+1)d_r (mod p)`.
Set `A_i=sum_(r=1)^i d_r`, `B_i=sum_(r=1)^i r*d_r`.
Then the new reflection law makes the entire observer computable as
```
q = 0, A = 0, B = 0, d = 1/10, b = 1  (all in F_p)
for i=1..m:
    b = b*(6(i-1)+1)*(3(i-1)+1)/(36*i*i) mod p
    if i>1: d=d*36*(i-1)^2/((6(i-1)+5)*(3(i-1)+2)) mod p
    A += d; B += i*d
    q += 2*b*((6*i+1)*A-6*B)
output q mod p
```
This requires **O(m) field operations and O(1) auxiliary field elements**:
no full `p`-coefficient stream or high-strip double sum. Both time and
auxiliary storage are measured *for this precise tail observer*, from input
prime `p`; the complexity of prime generation and native H0/B0 work is separate.
It is an exact, information-preserving replacement for the previous stored
`c_k` coefficient array **only at the declared readout** `T_p/p^2 (mod p)`.
The original upper-strip valuation, ordered-pair and second-digit provenance
remain in this proof, rather than being globally erased for other observers.

## Reproducible numerical check

A newly written standalone Python 3 exact-integer checker builds `b_k mod p^3`
independently, verifies `d_1=1/10`, checks every reflected `d_r`,
and compares the fused O(1)-space observer with the uncompressed O(p^2)
upper-strip sum. Executed in this research turn for all 35 primes
`7<=p<=373, p=1 mod6`, all passed, with witnesses:

| p | m | endpoint d_1 | tail T/p^2 mod p | T mod p^3 |
|--:|--:|--:|--:|--:|
| 7 | 1 | 5 | 3 | 147 |
| 13 | 2 | 4 | 0 | 0 |
| 19 | 3 | 2 | 12 | 4332 |
| 37 | 6 | 26 | 11 | 15059 |
| 61 | 10 | 55 | 3 | 11163 |
| 373 | 62 | 112 | 196 | 27269284 |

The full checker is `research_notes/portable_direct/d25_original216_reflected_tail_20261105.py`.
Old independent O(p)-memory checker:
`research_notes/portable_direct/d25_216_clausen_linear_tail_20261105.js`.
The new proof is arithmetic generality; finite checks are a separate regression.

## Original D24 LIFT interface / continuation

The frozen source supplies `W_p==p (mod p^2)`, `G_p=g/p`,
`h=sum (12k+1)b_k`, and
`Delta_p=(G_p*h-1)/p (mod p)` for both `p mod 24 in {13,19}`.
The existing exact identity `F_p*h=W_p+T_p` now gives the stronger
space-bound explicit formula
```
Delta_p - R_p =
  (W_p-p)/p^2
  + 2*sum_(i=1)^m b_i*((6i+1)*A_i-6*B_i) - R_p    (mod p).
```
This is a stricter algorithmic reduction of the **same** second digit;
`R_p` is still the exact RHS observable of the frozen JT2 geometry.
The frozen parent return
`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md`
states `1+pR_p` without a standalone numerical readout for `R_p`.
The next discriminating action is to locate the authoritative *independent*
`R_p` definition (including source/observer/normalization) in the frozen
parent materials, then compare target `p=13,19,373` without treating
`R_p := Delta_p` as a proof.

Native D24 p373 H0/B0, divided powers `[X]U mod p^2`, Frobenius orientation,
`eta/kappa` and independent review remain their own obligations.
No Source CLAIM/OPEN/checkpoint or mathematics admission is asserted here.
BRC population/observation: ordered pairs `(i,j)`, valuation `0/1/2`,
prime residue, p-unit, signed weight `6(i+j)+1`; the proven quotient
removes only terms of valuation >=3 for this mod-p second digit.
BRC_REUSE_RESOLUTION=REUSE_APPLIED.
