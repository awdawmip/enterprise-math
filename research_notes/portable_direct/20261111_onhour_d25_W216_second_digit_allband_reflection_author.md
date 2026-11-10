# D25/LIFT: second-digit all-band W216 reflection and top-band low-index reconstruction

Date: 2026-11-11 (run began 2026-11-10 23:55 +08). Status: **AUTHOR-PROVED ALGEBRA / EXACT-INTEGER VERIFIED / UNREVIEWED / NOT_ADMITTED**. This portable author note is not the canonical Source execution checkpoint, not a native CM benchmark and not a claim to have proved LIFT. Frozen science: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Mother task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Original `[X]U mod 139129` native H0/B0 benchmark tracked by #1559 remains `NOT_RUN / PENDING_OWNER`.

## 1. New theorem (all primes p > 3, every 1 <= k < p)

In the p-local rationals, put
[
 a_k=\frac{(2k)!(3k)!}{216^k(k!)^5},\quad s_2=\left\lfloor\frac{2k}{p}\right\rfloor,\ r_2=2k-s_2p,\quad s_3=\left\lfloor\frac{3k}{p}\right\rfloor,\ r_3=3k-s_3p.
]
Then `1 <= r_2,r_3 < p`; define `H_0=0`, `H_n=Σ_{j=1}^n j^{-1} mod p`, and `q_p(216)=(216^(p-1)-1)/p mod p`. All inverses below are of p-units.

**Second-digit reflection law:**
[
\boxed{\frac{a_k a_{p-k}}{p^3}\equiv
\frac{-(-1)^{s_2+s_3}s_3!(2-s_3)!}{36k^3}
\left[1+p\left(2H_{r_2-1}+3H_{r_3-1}-5H_{k-1}-q_p(216)\right)\right]\pmod{p^2}.}
]
Here `v_p(a_k)=s_2+s_3` and `v_p(a_{p-k})=3-s_2-s_3`, so the divided product is integral. The leading digit is the already-published four-band product theorem at `main@98d550c159790526ba395db5915b7343f2f7d36a`. The new information is the explicit **next digit modulo p²** and its Wilson-quotient cancellation; no independent theorem priority/novelty beyond the existing repository lineage is claimed.

## 2. Proof

For a prime p>3, q in {0,1,2}, 0 <= r < p, write `w_p=((p-1)!+1)/p`. Removing the p-multiples in factorial blocks gives
[
\frac{(qp+r)!}{p^q}\equiv
(-1)^q q!r!\bigl(1+qp(H_r-w_p)\bigr)\pmod{p^2}.
]
Indeed, every complete non-multiple block contributes `(p-1)! ≡ -1+p w_p` (so the sign-normalized factor is `1-p w_p`), while its linear-in-p correction is `b p H_{p-1}=0 mod p²` by `H_{p-1}=0 mod p`. The last partial block contributes `1+qp H_r`.

For 1<=r<p, using the reverse terminal factorial product similarly yields
[
r!(p-r)!\equiv (-1)^r r\bigl(1+p(H_{r-1}-w_p)\bigr)\pmod{p^2}.
]
Apply the first identity to both numerators `(2k)!, (2p-2k)!` with block counts `s_2,1-s_2`, and `(3k)!, (3p-3k)!` with block counts `s_3,2-s_3`. Apply the second identity to the two complementary numerator remainders and to `k!(p-k)!`, the latter raised to the fifth power. The numerator contributes `-5w_p` in total; the denominator contributes `-5w_p` and these cancel **exactly in the first p-adic digit**.

The factor `216^{-p}=216^{-1}(1-pq_p(216)) mod p²`. After collecting the remaining harmonic terms, the unsimplified correction is
[
egin{aligned}
L={}&s_2 H_{r_2}+(1-s_2)H_{p-r_2}+H_{r_2-1}\
&+s_3 H_{r_3}+(2-s_3)H_{p-r_3}+H_{r_3-1}\
&-5H_{k-1}-q_p(216)-\frac{s_2}{2k}-\frac{s_3}{3k}\pmod p.
end{aligned}
]
The final two fractions arise when replacing `r_2 r_3=(2k-s_2p)(3k-s_3p)` by `6k²` at the next digit. Since `H_{p-r}=H_{r-1} mod p` and `r_2=2k mod p`, `r_3=3k mod p`, the s-dependent harmonic fractions cancel, leaving
[
L=2H_{r_2-1}+3H_{r_3-1}-5H_{k-1}-q_p(216)\pmod p.
]
The leading sign/factor is precisely the original four-band Wilson product calculation. This proves the boxed claim in every band, with labeled original k and p-k.

Consistency check: replacing k by p-k changes the harmonic correction by `-3/k mod p`, exactly compensating the change of the leading `(p-k)^{-3}` factor at precision p². Thus the formula respects the original involution.

## 3. New derived top-band duality (target p=6m+1)

For `1<=k<=2m`, both block quotients s vanish. Hence the original fourth band `T_p=Σ_{j=4m+1}^{p-1}(6j+1)a_j` satisfies
[
\boxed{\frac{T_p}{p^3}\equiv
\sum_{k=1}^{2m}
\frac{(6k-1)+p\left[(6k-1)D_k-6\right]}{18k^3a_k}\pmod{p^2},}
]
where `D_k=2H_{2k-1}+3H_{3k-1}-5H_{k-1}-q_p(216) mod p`.

This is a **p^5-precision** source-index-preserving reconstruction of the high band entirely from the low-band p-unit sequence, including the original signed weight and the p correction. It extends the previous `mod p` high/low reflection duality (published at `7341336e7ddfde169fedf8facd4836922551ef75`) and independently cross-checks the published top-band Wilson-harmonic `p^5` expression at `28496e782a5e2001135a0f11c78988dc1d9ce4d6`.

## 4. Deterministic exact experiment (no floating point)

The accompanying standard-library program recomputes `a_0,...,a_{p-1}` using the **original coefficient recurrence modulo p^5**, evaluates both sides of the pointwise law at every index, and independently reconstructs `T_p/p³ mod p²` using its original high-band sum and the new low-band dual. For the 312 target primes `p<=10000, p mod24 in {13,19}`: **1,475,586** pointwise pairs verified and all **312** band sums matched. Eleven extra non-target primes contribute 312 further pointwise pairs. The code independently compares the original binomial factorial expression to the recurrence for selected primes.

Selected `T_p/p³ mod p²`: p13:70 (5+5p); p19:156 (4+8p); p109:3677 (80+33p); p139:6591 (58+47p); p157:22547 (96+143p); p373:109567 (278+293p); p997:655376 (347+657p); p2131:756 (756+0p). All checked. Exact finite evidence supports the algebraic proof, rather than replacing its universal quantifier.

## 5. Parent-frontier and next action

This proof preserves `k, p-k, s_2,s_3,r_2,r_3, v_p, q_p(216)`, original coefficients and signed band weights. Reduction modulo p follows the stated precision-specific operator only after dividing the product by p³. The theorem's fourth-band p⁵ precision is a **separate auxiliary** achievement: LIFT still requires the original `Delta_p-R_p mod p` or equivalent `W_p=p mod p³` uniformly. Do not count this as new evidence for native H0/B0 `[X]U mod 139129`. Its next **highest-priority original-class** action is the still-unowned #1559 native benchmark with true module rank, Frobenius semilinear direction, eta, signed odd Hesse/Green observer, kappa, original Delta/R and independent validation. Source event authority and owner remain separately governed; no private session capability or winning CLAIM was used here.
