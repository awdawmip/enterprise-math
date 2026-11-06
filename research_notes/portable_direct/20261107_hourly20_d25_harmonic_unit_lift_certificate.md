# D25 / D=-24: p-unit harmonic expansion of the frozen second-digit LIFT

Date: 2026-11-07 (Asia/Hong_Kong). Status: AUTHOR-SIDE EXACT ALGEBRA / FINITE REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Logical research lane: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance conversation). This is portable author evidence, not a new owner CLAIM or a replacement for the authenticated continuation.

## Exact source and new theorem

Take any prime p=6m+1 >=7 and B_0=1, B_{k+1}/B_k=(6k+1)(3k+1)/[36(k+1)^2] for 0<=k<p-1 in Z_(p). Let e_k=1_{k>m}+1_{k>2m}. Define the **p-unit labelled carrier**

C_k = 2^{-k} 6^{-1_{k>m}} 3^{-1_{k>2m}}
  [product_{0<=r<k, r != m}(r-m)]
  [product_{0<=r<k, r != 2m}(r-2m)] / (k!)^2.

All denominators are p-units. Define two power sums over the same *two labelled source factors*:

s_{1,k} = sum_{0<=r<k,r!=m} 1/[6(r-m)] + sum_{0<=r<k,r!=2m} 1/[3(r-2m)],
s_{2,k} = sum_{0<=r<k,r!=m} 1/[36(r-m)^2] + sum_{0<=r<k,r!=2m} 1/[9(r-2m)^2],
q_k = (s_{1,k}^2-s_{2,k})/2.

**Theorem 1 (all p=6m+1 primes; exact finite-product and lifted jet).**

B_k = p^{e_k} C_k
 [product_{r<k,r!=m}(1+p/[6(r-m)])]
 [product_{r<k,r!=2m}(1+p/[3(r-2m)]]

is an exact rational identity. Consequently,

 B_k = p^{e_k} C_k (1+p s_{1,k}+p^2 q_k) (mod p^{e_k+3}).

For every k, the modular denominator inversions are legitimate. C_k has the explicit three-band factorial form:

* 0<=k<=m: C_k=m!(2m)!/[2^k(m-k)!(2m-k)!(k!)^2].
* m<k<=2m: C_k=(-1)^{m+k}m!(2m)!(k-m-1)!/[6*2^k(2m-k)!(k!)^2].
* 2m<k<p: C_k=(-1)^m m!(2m)!(k-m-1)!(k-2m-1)!/[18*2^k(k!)^2].

Thus the previous leading valuation-band coefficients are the reductions C_k mod p; the new data s1 and q give their *first two p-adic correction jets* without hiding either exceptional p-factor.

Closed harmonic evaluation is available without an index-level inverse loop: let H_n^(r)=sum_{j=1}^n j^{-r}, H_0^(r)=0. The unscaled 1/(r-m) sum is -H_m+H_{m-k} for k<=m and -H_m+H_{k-m-1} for k>m; similarly replace m by 2m for the second factor. Its square-denominator sum is H_m^(2)-H_{m-k}^(2) if k<=m, or H_m^(2)+H_{k-m-1}^(2) if k>m; similarly for 2m. Apply factors 1/6, 1/3, 1/36, 1/9 respectively. All harmonic denominators are <p.

## Theorem 2: an entirely p-unit/harmonic carrier for the actual frozen Delta

Define source-labelled quantities in Z_(p):

A0=sum_{k=0}^m C_k,
A1=sum_{k=0}^m C_k s_{1,k} + sum_{k=m+1}^{2m} C_k,
A2=sum_{k=0}^m C_k q_k + sum_{k=m+1}^{2m} C_k s_{1,k},
W=sum_{k=2m+1}^{p-1} C_k,
H0=sum_{k=0}^m (12k+1) C_k,
H1=sum_{k=0}^m (12k+1) C_k s_{1,k},
V=sum_{k=m+1}^{2m}(12k+1)C_k.

For target primes p mod 24 in {13,19}, the accepted CM0 first digit supplies A0=0 mod p, and the accepted UR supplies the unit condition below. Set

 X=A0/p+A1,   Y=A2+W,   J=H1+V.

Then g/p = X+pY (mod p^2) and h=H0+pJ (mod p^2), where g=sum B_k and h=sum(12k+1)B_k. The authentic frozen second-digit observer satisfies

 **Delta_p = (X H0 - 1)/p + X J + Y H0 (mod p)**,
 **X H0 = 1 (mod p)**.

Proof: expand Theorem 1 in the three valuation bands. Up to p^3,
g=A0+p A1+p^2(A2+W); up to p^2, h=H0+p(H1+V). The target-class CM0 ensures A0/p exists p-integrally, and UR ensures the displayed divided product exists. Multiplication yields the formula. No assumption about the still-unidentified target R_p was introduced. All operations preserve the separate low/middle/high k labels, the two exceptional p-factor labels, the 12k+1 h-port, and the order of quotient versus reduction.

This is an exact **re-expression** of Delta, not a proof that Delta=R_p. In particular, the new Y port contains both the low-band second harmonic jet and the high divided-p^2 tail: omitting either is an information-changing projection. H0 = H_m(1/2)+6 H_m'(1/2), where H_m(z)=sum_{k=0}^m binom(m,k)binom(2m,k)z^k, connects the re-expression to the already accepted first-digit terminating carrier.

## Independent executable evidence

The companion standard-library checker evaluates every term of Theorem 1 via independently computed factorial C_k and harmonic s1/s2 modulo p^3; it reconstructs g/p and h through Theorem 2, and compares with an independent **unexpanded** B recurrence modulo p^3. All 166 target primes p<5000 passed both termwise and final Delta comparisons. Six p<100 targets also passed independent exact Fraction recurrence. Selected (p,X mod p,Y mod p,H0 mod p,J mod p,(XH0-1)/p mod p,Delta mod p):

13: (11,8,6,11,0,0)
19: (8,12,12,10,16,12)
37: (23,10,29,25,34,11)
43: (31,0,25,18,16,15)
109: (78,58,7,79,22,50)
157: (53,90,80,72,56,82)
373: (24,288,171,82,81,196).

The two congruences are universal algebra on the stated domain; finite computation is independent regression only. It does not compute R_p, establish LIFT/JT2, produce a native X6 experiment, or count as independent project review. The public taskbook and accepted parent define the right-hand R_p only as a frozen symbol, not an executable value. The next comparison requires its actual independent pinned formula/artifact, not a definition R_p := Delta_p.

## Next minimal unit and control

Seek the exact independently defined frozen R_p (and its Phi_xx/Frobenius normalization) from authenticated task artifact provenance; substitute it into (XH0-1)/p+XJ+YH0-R_p. If that source is still absent, seek a source-backed special-prime counterexample or a telescoping identity for one labelled harmonic port without identifying R_p by fiat. Do not redo accepted UR/JT0 or present auxiliary lambda_p as Delta.

The native gateway em_status returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site connection reports CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Protected old staging/requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 are not reissued. No session registration, CLAIM, OPEN, publish_checkpoint, freeze or review occurred. Exact existing control support: awdawmip/enterprise-math#1558. Own new research remains REGISTER_PENDING; native durable frontier remains UNVERIFIED.
