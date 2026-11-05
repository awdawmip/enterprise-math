# D25 — original 216 bottom-band p-adic two-jet, with source-preserving D_p reconstruction

2026-11-06 · TASK_RESEARCH · AUTHOR EXACT DERIVATION / 80-PRIME FINITE CHECK · UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific input pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923; separate from maintenance chatgpt-hourly-enterprise-math-20260921.

## I. Exact parameter deformation at the previously unresolved bottom-shell port

Let p=6m+1 be prime, m>=1, and n range over 0<=n<=2m. Let

a_n = (2n)!(3n)! / [216^n(n!)^5]
    = (1/2)_n(1/3)_n(2/3)_n / [2^n(n!)^3].

Set
c_n = (-3m)_n(-2m)_n(-4m)_n / [2^n(n!)^3],

and for every r=0,...,n-1 put
x_r = 1/[2(3m-r)], y_r = 1/[3(2m-r)], z_r = 2/[3(4m-r)].

All these denominators are p-units, because 0<=r<2m<p and p>3. Define the finite labeled jet observers

L_n = sum_{r=0}^{n-1}(x_r+y_r+z_r),
S_n = sum_{r=0}^{n-1}(x_r^2+y_r^2+z_r^2),
L_0=S_0=0.

**Exact identity in Q (not a congruence):**

a_n = c_n prod_{r=0}^{n-1}(1-p*x_r)(1-p*y_r)(1-p*z_r).   (1)

This follows term by term from (1/2)=(-3m+p/2), (1/3)=(-2m+p/3), and (2/3)=(-4m+2p/3). Equivalently it is the evaluation at t=p of the explicitly terminating coefficient polynomial

F_m(z;t) = sum_{n=0}^{2m} [(-3m+t/2)_n (-2m+t/3)_n (-4m+2t/3)_n / (2^n(n!)^3)] z^n.

For the weighted bottom sum B_p = sum_{n=0}^{2m}(6n+1)a_n,
B_p = [(1+6 theta) F_m(z;p)]_{z=1}, theta=z*d/dz, exactly.   (2)

## II. Two p-adic digits of the bottom compensation

Expanding the *proved exact* product (1) in Z_(p) gives, for every 0<=n<=2m,

a_n = c_n [1-p L_n+(p^2/2)(L_n^2-S_n)] (mod p^3).   (3)

Let
A0 = sum_{n=0}^{2m}(6n+1)c_n,
A1 = sum_{n=0}^{2m}(6n+1)c_n L_n,
A2 = sum_{n=0}^{2m}(6n+1)c_n(L_n^2-S_n).

The resulting **unconditional bottom-shell theorem** for all primes p=6m+1 is

B_p = A0-p A1+(p^2/2)A2 (mod p^3).                  (4)

The signs and diagonal subtraction S_n are load-bearing: the quadratic term is the off-diagonal second elementary symmetric sum of all 3n labeled factors; replacing it by L_n^2/2 would add incorrect square terms.

Keep the actual original 2304 half-sum, without fitting it to the new jet:

b_k = (4k)!/[2304^k(k!)^4],
V_h = sum_{k=0}^{h}(8k+1)b_k, h=3m.

For the frozen target classes p mod24 in {13,19}, existing accepted first-digit scalar input and previous author-side original-shell identities supply B_p = V_h (mod p). In that precisely stated regime D_p = (B_p-V_h)/p is a p-local integer. Equation (4) now proves the **source-preserving two-digit reconstruction**

D_p = (A0-V_h)/p - A1 + (p/2)A2  (mod p^2).        (5)

All p-divisions occur in Z_(p) **before** reducing modulo p^2; the numerator A0-V_h is p-divisible under the same inherited condition B_p=V_h (mod p). Thus a formerly opaque bottom difference is exposed as one terminating unperturbed 3F2 observable, its first and second parameter jets, plus the unchanged original 2304 half-sum.

This is a direct exact two-jet representation of the specific bottom D_p requested after the previous 3D middle-shell Gosper residual theorem. It does NOT assert that the two-jet representation already cancels the middle/upper shells. It gives the following equivalent, fully signed finite certificate when substituted into the earlier independently proved one-seed pairing formula (p=6m+1, target classes):

0 = (A0-V_h)/p - A1 + (p/2)A2
  + sum_{j=0}^{m-1} [(3p-2-6j)u_j
        + p(6j+4)/(36(h-j)^3 u_j)]  (mod p^2),     (6)

where u_0=a_h/p mod p^2, and
u_{j+1}/u_j = 36(h-j)^3 / [(2h-2j-1)(3h-3j-1)(3h-3j-2)]
for 0<=j<m-1. The pair formula is consumed from the preceding verified author note; (6) is a reduction/explicit observer specification, not a proof of its uniform zero.

The original scalar link remains: (W_p-p)/p^2 = Delta_p-R_p modulo p at the frozen original reflected-cutoff interface. The all-target LIFT/JT2 proof remains open.

## III. Reproducible exact evidence

Executed pure integer modular arithmetic on all 80 primes p<=997 with p=1 mod6, checking each individual n in (3), and the bottom full sum (4), against *independently constructed original binomial coefficients*. For the 45 target primes p<=997 with p mod24 in {13,19}, independently checked D_p from original binomial B_p,V_h and reconstructed formula (5), 45/45 equal. An additional Python Fraction check established the entire **exact** factorization (1) for every n at p=13 and p=19, with no modular arithmetic. Assertions failed: zero.

Representative residues (A0,A1,A2,B,V modulo p^3; D modulo p^2):

| p | A0 | A1 | A2 | B | V_h | D original = reconstructed |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 442 | 1560 | 2168 | 780 | 13 | 59 |
| 19 | 5491 | 2898 | 4752 | 5662 | 19 | 297 |
| 67 | 260228 | 13662 | 255756 | 134938 | 67 | 2013 |
| 139 | 932412 | 1124793 | 1590942 | 2535360 | 139 | 18239 |
| 373 | 15521276 | 18640164 | 23606588 | 28094360 | 373 | 75319 |

Verifier: research_notes/portable_direct/d25_216_bottom_parametric_two_jet_20261106.py.
Output: research_notes/portable_direct/20261106_onhour_d25_bottom_parametric_two_jet_results.json.

## IV. BRC provenance, scope, and native experimental debt

BRC reuse = COMPOSE_APPLIED. Population is each frozen original p and 0<=n<=2m; labeled branches are the three original hypergeometric parameters at every r. Observer preserves (model=216, n, r, p, c_n, x/y/z identities, signed weight 6n+1, first parameter jet L_n, second jet S_n, original 2304 boundary V_h). Allowed operations: exact multiplication, p-local expansion to p^3, labeled signed summation and division only when the actual numerator is p-divisible. This preserves the source identity and differentiates distinct parameter ports without treating a two-coordinate auxiliary model as a complete native X6 or 3D slice.

The precise next mathematical unit is to perform a parameter-jet-aware creative-telescoping reduction of A0, A1, A2 against the signed middle-shell rational Gosper residual basis {1,j,j^2}, the nonzero boundary at n=2m and the original V_h; then test p=13,19 and whether the resulting coupled boundary proves all-target cancellation.

Separately the highest native front remains original-class fixed p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear F and eta/kappa, odd Hesse/Green port, reproducible native operator and independent replication. Support Issue #1559 OPEN, unassigned at 2026-11-06 read. An external ordinary-Hesse norm 122102 is conditional only on native identification. Native experiment NOT_EXECUTED.

Origin is this author's new portable derivation / reproducible check, not a Source-native Result, accepted theorem, native claim or review. Existing Source predecessor contribution history and frozen input pin remain unchanged; previous three staging artifacts remain independent. The research lane has no authenticated own CLAIM/open/run used for this paper. Preserve the queued read-only Source request d25-onhour-20261106-0701-recovery-read for actual receipt/reconcile; do not reissue as a new operation.
