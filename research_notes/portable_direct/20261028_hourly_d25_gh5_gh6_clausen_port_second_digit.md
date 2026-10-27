# D25/LIFT GH-5 / GH-6 — p-adic second digit of the labelled Clausen middle port

Date: 2026-10-28 Asia/Hong_Kong. TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923`. Parent D25/LIFT/JT2, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is not a native Source checkpoint or independent review.

## Original source and observer

Consume GH-2 and GH-3, preserving their labelled source population and exact cutoff. For prime `p ≡ 19 (mod 24)` put
[
a=(p-3)/8,quad b=(3p-1)/8,quad h=(p-1)/2,quad d=(p-3)/4.
]
Original S-Gauss carrier `u_k=(1/8)_k(3/8)_k / ((k!)² 9^k)`. For `a<i≤b` define **exact rational** p-adic units `β_i=u_i/p`. Keep the source-labelled signed middle-middle port
[
M_p=sum_{a<i,jle b, i+j>h} (8(i+j)+1),eta_ieta_jinmathbb Z_p.
]
The two source indices and finite truncation are part of the observable state; positivity/mass must not replace signed cancellation.

## GH-5: exact p² deformation theorem

For `0≤r≤d` set
[
g_r=9^r rac{(1/8)_r^2}{(3/4)_r r!},qquad
H_r=sum_{j=0}^{r-1}left(rac1{8j+8}+rac1{8j+6}-rac2{8j+1}ight), H_0=0.
]
All denominators are p-units in the stated interval. The **original** coefficient recurrence gives the exact rational reverse step
[
rac{eta_{b-r-1}}{eta_{b-r}}=
rac{9(8r+1-3p)^2}{(8r+8-3p)(8r+6-3p)},qquad 0le r<d.
]
Divide by `g_(r+1)/g_r=9(8r+1)^2/((8r+8)(8r+6))`, expand each p-unit factor to first order, and multiply. This proves
[
oxed{rac{eta_{b-r}}{eta_b}equiv g_r(1+3pH_r)pmod{p^2}}qquad(0le rle d).
]

Use GH-3's exact Clausen coefficients
[
c_t=9^trac{(1/4)_t^3}{(1/2)_t(3/4)_t t!},quad
T_p=sum_{t=0}^d(8t+1)c_t,quad C_p=sum_{t=0}^dc_t,
]
and retain the extra signed joint jet
[
K_p=sum_{r+sle d}(8(r+s)+1)g_rg_s(H_r+H_s).
]

**Theorem GH5 (all primes p≡19 mod24):**
[
oxed{rac{M_p}{eta_b^2}equiv -T_p+p(6C_p-3K_p)pmod{p^2}.}
]

**Proof.** Reverse the original two indices, `i=b-r,j=b-s`: exactly `r+s≤d`; its original weight is `6p-(8(r+s)+1)`. Substitute the displayed p² reversal expansion. The degree-t convolution of `g_r g_s` equals `c_t` **exactly** by the coefficientwise Clausen identity already used in GH-3. The zero-order term is `-T_p`, the weight's p-correction is `+6pC_p`, and the source-deformation correction is `-3pK_p`. No boundary term was discarded. QED.

**Conditional next digit.** If the still-open universal statement `T_p≡0 mod p` holds for a given p, then
[
rac{M_p}{peta_b^2}equiv -rac{T_p}{p}+6C_p-3K_ppmod p.
]
This conditional division does not assert the universal conjecture.

## GH-6: a concrete no-go for naive modulo-p² lifting

For p=19, executed exact arithmetic gives `(T_p/p,C_p,K_p) ≡ (18,3,5) mod19`, `M_p/β_b²≡76 mod361` and `M_p≡209 mod361`. The naive claim `M_p/β_b²≡-T_p mod361` predicts 19, not 76. The correction yields `-342+19(18-15)≡76 mod361`.

For p=43, `(T_p/p,C_p,K_p)≡(38,20,13) mod43`. Thus `-43·38+43(120-39)≡0 mod43²`. An independent **exact rational** evaluation of the original labelled double sum proves `v_43(M_43)=2` and `M_43/43²≡22 mod43`. This extra source-port digit coexists with `v_43(T_43)=1`: retaining the `C_p,K_p` joint residual is indispensable at the declared precision.

Executed Python-stdlib checker: on all 1227 primes `5≤p<10000`, the truncated `T_p` with `d=floor((p-1)/4)` has **observed exact** `v_p(T_p)=1`, a finite certificate not a universal theorem. On all 37 primes `p<2000,p≡19 mod24`, the original port and GH-5 agree modulo p²; p=43 is the only member with port vanishing modulo p². Independent rational original-source checks for p=19,43 pass.

## Research placement and next

The actual BRC reuse is a typed signed/provenance and valuation carrier: `T_p` alone is insufficient for the next-digit port; `(T_p,C_p,K_p,β_b)` retains it modulo p². Coefficient ranks are auxiliary, **not** native spatial dimensions. P000's native X6 and separate time remain unchanged. This theorem does not assert the original W/S supercongruence, a nonlocal WZ transformation, H0/B0, `[X]U mod p²`, Frobenius η/κ, or native p=373 results.

Next scientific action: prove or refute `T_p≡0 modp` uniformly in the 19-class, then attempt a source-labelled finite-boundary identity using the newly exposed `K_p`, GH-2/GH-4 and R36; retain six fixed-z=2 Hasse J/E labels, two finite endpoints and positive-direction infinity. Exact native continuation still requires resolution of predecessor CLAIM mismatch in enterprise-math#1558. This portable artefact makes no current CLAIM/OPEN/Result claim and does not alter old session/staging or Source pin.
