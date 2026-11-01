# D25: signed Clausen R as an invertible four-port finite transfer
2026-10-31, Asia/Hong_Kong. Logical research lane: `chatgpt-research-onhour-enterprise-math-20260923` (NOT maintenance). Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; P000 ACTIVE_LOCKED, worldview unchanged. AUTHOR-SIDE / PROVED ALGEBRAIC TRANSFER / EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Not original-class native H0/B0.

## Precisely reused input
Consume the **previously proved** mod-p signed overdegree R identification, from `research_notes/portable_direct/20261031_onhour_d25_clausen_jet_unique_overdegree_R.md`, commit `3380c77a4d5c5556d7c63698c274e8a5f537aa55`. For prime p=6l+1>=7, in F_p define
[
g_i=inom l iinom{2l}i 2^{-i},quad c_1=1/10,quad
c_{i+1}=r_i c_i,quad r_i={36i^2over(6i+5)(3i+2)},
]
[
K_0=0,quad K_i=sum_{a=1}^i(1+6(i-a))c_a,quad
R_p=2sum_{i=1}^l g_iK_i.
]
The new work is a uniform **reversible** transfer for this already-source-identified R and a concrete counterexample to a lossy scalar observer. Neither Clausen nor the c seed/recurrence is claimed new.

## Theorem 1: second-difference and degeneration
Let D_i=(6i+5)(3i+2), E_i=5D_i+36i²=126i²+135i+50 and W_i=K_{i+1}-2K_i+K_{i-1}. For 1<=i<l,
[
W_i=(5+r_i)c_i={E_iover D_i}c_i.
]
For 1<=i<=l-2 the following holds **even when E_i=0**:
[
D_{i+1}E_iW_{i+1}=36i^2E_{i+1}W_ipmod p.
]
Proof: subtract adjacent finite K sums, yielding K_{i+1}-K_i=c_{i+1}+6 sum_{a<=i}c_a; subtract again to obtain W_i=c_{i+1}+5c_i. Substitute r_i and cross-multiply without dividing by E_i. Every D_i is a p-unit because 6i+5<=p-2 and 3i+2<p. QED.

**BRC loss witness:** at target p=67, l=11, i=7, D_7=9, E_7=7169=67*107=0, c_7=39≠0 and W_7=0, but W_8=20≠0 (all residues mod67). Therefore replacing the source c_7 by the single scalar W_7 and dividing by 5+r_7 is invalid. This rules out that specific lossy normalization, not all scalar methods.

## Theorem 2: nonsingular signed four-port transfer
Let q_i=(l-i)(2l-i)/(2(i+1)²)=g_{i+1}/g_i, and write H_i=g_iK_i, V_i=g_iK_{i-1}, C_i=g_ic_i, T_i=2 sum_{a=1}^i g_aK_a. Then
[
egin{pmatrix}H_{i+1}\V_{i+1}\C_{i+1}\T_{i+1}end{pmatrix}=
egin{pmatrix}
2q_i&-q_i&q_i(5+r_i)&0\
q_i&0&0&0\
0&0&q_ir_i&0\
4q_i&-2q_i&2q_i(5+r_i)&1
end{pmatrix}
egin{pmatrix}H_i\V_i\C_i\T_iend{pmatrix},qquad 1le i<l,
]
with (H_1,V_1,C_1,T_1)=(l²/10,0,l²/10,l²/5) and **R_p=T_l**. Proof: use K_{i+1}=2K_i-K_{i-1}+(5+r_i)c_i, g_{i+1}=q_i g_i, c_{i+1}=r_i c_i and T_{i+1}=T_i+2H_{i+1}. Initial values follow from g_1=l² and c_1=K_1=1/10. QED.

The transfer determinant is **q_i³ r_i**, a nonzero p-unit for every 1<=i<l; all numerator/denominator factors are strictly between 0 and p. Therefore the complete source-aware state is invertible for every allowed step, including the p=67 scalar degeneration. This is an O(l) exact modular evaluation of original signed R, preserving its index, weight and boundary c-source. It is not a proof of the full target nor a p²/native lift of the c coefficients.

## Exact executed verification
The linked executable `d25_signed_R_unimodular_transfer_20261031.py` was actually executed. For every one of the **94 primes 7<=p<=1200 with p≡1(mod6)** (including **52** in p≡13,19(mod24)), it compared this transfer to an independently constructed literal signed double sum and checked each state coordinate and third-order identity. All PASS; 15 tested primes had E_i=0 at some interior step. Anchors (p,l,R,degenerate indices):
(19,3,12,[]), (67,11,21,[7]), (103,17,81,[2]), (211,35,119,[29]), (373,62,196,[]). At 67, transfer i=7: (46,21,38,6), i=8: (27,9,24,60). `PASS_D25_SIGNED_R_UNIMODULAR_FOUR_PORT_TRANSFER`. Exact algebra supplies the universal scope; the scan is implementation evidence only.

## Next / Source boundary
Full original A_p≡p (mod p³), p≡13,19(mod24), remains **OPEN**. Next actual math unit is to construct a finite parameter-shift/adjoint WZ identity coupling the **lower Clausen jet/carry terms** to this non-singular signed transfer, with 19,67,373 as discriminating tests; retain other lanes' endpoint Fermat-quotient/tail contributions as separately credited source. The p=373 native H0/B0 divided-power [X]U mod139129, real rank, semilinear Frobenius/eta, signed Green/Hesse, kappa and independent replay remain PENDING_OWNER on enterprise-math#1559; no surrogate accepted.

Our own Research conversation recovery is #6632: a Researcher session but no own claim/run, source_authority_verified=false. Original dispatch #6633 is FAILED / UPSTREAM_CODE_REVIEW_REQUIRED; no duplicate mutation or maintenance identity was used. No role-bound Source checkpoint, Result, mathematical admission or independent review. Historic staging remains separately preserved. Next authorized control action is to reconcile the exact original request and canonical continuation when permission permits; never rebase the frozen pin.