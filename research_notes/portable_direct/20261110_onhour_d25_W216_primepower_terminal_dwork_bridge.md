# D25 / W216 — prime-power terminal carry and a finite Frobenius-lift witness

Date: 2026-11-10 (Asia/Hong_Kong). Source: original frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research-lane local author-side continuation only; status **PROVED (terminal theorem) / EXACT_FINITE_EXPERIMENT (Frobenius hypothesis) / UNREVIEWED / NOT_ADMITTED**.

## 1. Prime-power theorem (all p>3, r>=1)

Let `a_k = binom(2k,k)^2 binom(3k,k) /216^k = (2k)!(3k)! / ((k!)^5 216^k)`, and let `d_k=-(k-1)(6k+5)/(3(k+1)^2)`. Set `n=p^r`, `N=n-1`, `W_n=sum_(0<=k<n)(6k+1)a_k`, and `S_n=sum_(0<=k<n-1) d_k a_k`.

**Theorem A.** For every prime p>3, every r>=1:
1. `v_p(a_(p^r-1))=3r` and `a_(p^r-1)/p^(3r) = -1 (mod p)` in the p-local integers.
2. Each term `d_k a_k` for `0<=k<n-1` is p-integral, including indices `k+1` divisible by p. More precisely, if `t=v_p(k+1)`, then `v_p(d_k a_k)>=t`.
3. Reusing the **previously proved** exact inverse-moment telescoping identity at general n,
`W_n-S_n=(7-6n)a_(n-1)` over Q. Therefore
`W_(p^r)-S_(p^r) = -7p^(3r) (mod p^(3r+1))`,
and `W_(p^r)=S_(p^r) (mod p^(3r))`.
For p=7 the displayed leading boundary charge is itself zero modulo `p^(3r+1)`; this is an arithmetic specialization, not a different theorem.

### Proof of the valuation and leading unit

For t=1,2,3 write `M_t=t(p^r-1)` and `A_r=sum_(i=0)^(r-1) p^i`. Since p>3, Legendre's factorial formula gives exactly
`v_p(M_t!)=t A_r-r`.
The coefficient is `a_N=(2N)!(3N)!/(N!)^5 *216^(-N)`, with 216 a p-unit. Thus
`v_p(a_N)=(2A_r-r)+(3A_r-r)-5(A_r-r)=3r`.

Let `U_p(m!)=m!/p^(v_p(m!)) (mod p)`. Recursive extraction of multiples of p from successive factorial blocks and Wilson's theorem give the exact digit-unit identity
`U_p(m!)=(-1)^(v_p(m!)) prod_(base-p digits d of m) d! (mod p)`.
For `M_t=tp^r-t` the base-p digits, from low to high, are `p-t`, then `r-1` digits `p-1`, then `t-1`. Since `A_r=r (mod 2)` and `(p-t)!(t-1)!=(-1)^t (mod p)`, one obtains
`U_p(M_t!)=(-1)^(tr+t-1) (mod p)`.
Consequently the units for t=1,2,3 are respectively `(-1)^r,-1,(-1)^r`; their factorial ratio `U_p((2N)!)U_p((3N)!)/U_p(N!)^5=-1 (mod p)`. Fermat gives `216^(-N)=1 (mod p)` because `p-1|p^r-1`. The claimed terminal leading unit follows.

### Proof of the denominator-compensating valuation

If `t=v_p(k+1)>0`, the lowest t base-p digits of k are all `p-1`. Adding k+k entails at least t carries, and adding k+2k entails at least t carries (the low t digits of 2k are those of `-2 mod p^t`). By Kummer, `v_p(bin(2k,k))>=t` and `v_p(bin(3k,k))>=t`. Thus `v_p(a_k)>=3t`. The denominator of `d_k` has at most p-adic valuation `2t` (3 is a unit); hence `v_p(d_k a_k)>=t`. When t=0, integrality is immediate. Applying the prior exact identity and the terminal leading unit proves part 3.

This is a digit-level BRC carry certificate: retaining the composite binomial factors, index digits, denominator order and boundary operator is necessary to justify the higher-scale p-local projection. It does not identify the fixed native H0/B0 crystal.

## 2. New finite experimental direction: signed Frobenius recurrence

For p>3 let `chi_p=1` if `p=1 (mod 3)`, otherwise `chi_p=-1`. In each tested prime, the known first-scale candidate `W_p=chi_p*p (mod p^3)` holds; define the observed third-digit `c_p=((W_p-chi_p*p)/p^3) mod p`.

**Conjectural mechanism (not proved):** for r>=2,
`W_(p^r)-chi_p*p*W_(p^(r-1)) = c_p*p^(3r) (mod p^(3r+1))`.
It predicts that the first Dwork-style defect after the `p^(3r)` threshold has the same signed residue as the base-scale fourth digit; it is not an assertion of native crystalline Frobenius.

Exact finite witnesses with independent integer-binomial summation: at r=2, p=5,7,11,13,17,19,23,29,31,37, with c_p respectively `0,1,2,9,8,12,8,19,22,19`. At r=3: p=5,7,11,13, same c_p. At r=4: p=5,7, same c_p. The 16 p,r cases matched the claimed residue mod `p^(3r+1)`. A finite test of the stronger conjecture remains non-universal evidence; the complete proof of Theorem A is independent of this observation.

## 3. Reproduction, source boundary, next exact action

Independent original-integer factorial/binomial path checked the terminal valuation/unit and `W_n-S_n` for 16 p,r pairs (p=5,7,11,13,19,31, with r up to 3); no floating point or hidden division by p. The separate Frobenius probe checked the 16 listed pairs. Checker `d25_w216_primepower_terminal_dwork_20261110.py` outputs all witnesses.

The mother objective remains **original signed** `Delta_p-R_p=0 (mod p)` for p=13,19 (mod24), with frozen source; this note is a directly compatible prime-power coefficient/valuation unit and a distinct testable Frobenius-lift candidate, not a formal acceptance or a substitute for H0/B0.

**Highest native evidence debt**: original-class fixed H0/B0 `[X]U mod139129` at p=373, module rank, semilinear Frobenius normalization eta, signed kappa, original Delta-R mapping and independent source-pinned verification. Existing Issue #1559; responsible native compute path remains PENDING_OWNER/NOT_RUN.

**Next exact action**: derive a bounded finite `p^r` WZ/contiguous identity that predicts the observed Dwork defect, beginning at r=2 and p=13/19 with independent digit-block terms; if it fails, retain a minimal exact counterexample. Separately preserve existing p=373 native benchmark for an authorized executor; do not equate this ordinary finite Frobenius observation with the native matrix.
