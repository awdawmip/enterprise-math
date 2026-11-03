# D25: four-port desingularization to second p-adic digit and directed ledger

Date: 2026-11-03. Research scope: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7 / frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Author-side portable evidence; not a native Source checkpoint. Previous Source read main@60a8ee68ed40e04c7cd1f80ab4f28e9ff164e5bc. Research lane label chatgpt-research-hourly-enterprise-math-20260923, not a service-signed identity.

For prime p >= 13, p mod24 in {13,19}, retain original factorial coefficients
b_k=(2k)!(3k)!/((k!)^5 216^k), c_k=(4k)!/((k!)^4 2304^k),
h_k=c_k/b_k and g_k=(8k+1)c_k/((6k+1)b_k).
The exact preceding author papers at 58dc537391b4bd1f8e2e585bdef7714c5cfdb8e2 and 01d7a2c0982291f7efec74931449e1ae0ac5e650 supply
h_k h_(p-k) = tau_p(k)(1+p E_p(k)) (mod p^2).
Here q_a=floor(a k/p), r_a=a k-p q_a, a in {2,3,4}; H_j=sum(i^{-1},1<=i<=j) modp, Q_p(a)=(a^(p-1)-1)/p modp, and
E_p(k)=Q_p(3)-5Q_p(2)+4H_(r4-1)+H_(k-1)-2H_(r2-1)-3H_(r3-1) (mod p).
The class units are tau=1/8 at the central reflected zero orbit and tau=3/16 at the outer reflected pole orbit. These lemmas are consumed at their stated author-proof status, not re-admitted.

## Theorem 1 (full two-digit exceptional-port unit formulas)

Put eta=5 for p=13 mod24 and eta=3 for p=19 mod24. The four distinct directed indices are
z=(eta*p-1)/8, z*=p-z, r=(p-1)/6, r*=p-r.
For the exact symmetric weighted ratio R_p(k)=g_k g_(p-k), the normalized quantities U_Z=R_p(z)/p=R_p(z*)/p and U_P=p R_p(r)=p R_p(r*) belong to Z_p^units. The following holds modulo p^2:

U_Z = (4 eta/7) [1+p(E_p(z)+(8-43 eta)/14)].
U_P = (-7/96) [1+p(E_p(r)-51/14)].

Consequently U_Z U_P=-eta/24 modp. All denominators 7,14,96 are p-adic units in the stated prime domain. The original four oriented ports remain distinguished for later directed telescopes.

Proof: The rational identity
R_p(k)=h_k h_(p-k) (8k+1)(8(p-k)+1)/((6k+1)(6(p-k)+1))
is exact before p-adic reduction. At z, 8z+1=eta*p and
A(z)/p=eta[2+(8-eta)p],
B(z)=[(3eta*p+1)(3(8-eta)p+7)]/16,
where A=(8k+1)(8(p-k)+1), B=(6k+1)(6(p-k)+1).
Thus (A(z)/p)/B(z)=(32eta/7)[1+p(8-43eta)/14] modp^2.
Multiply by the preceding factorial-unit law with tau=1/8.
At r, 6r+1=p and B(r)/p=2+5p, while A(r)=(4p-1)(20p+7)/9, hence A(r)/(B(r)/p)=(-7/18)[1-51p/14] modp^2. Multiply by tau=3/16 and (1+p E_p(r)). Exact reflection symmetry gives z*,r*. Multiplication of the leading units proves the cross-port formula. QED.

## Theorem 2 (directed valuation and observer certificate)

Let d=2 for eta=5 and d=1 for eta=3, B_k=(6k+1)b_k, C_k=(8k+1)c_k. The tuple of exact valuations
(v_p(b_k),v_p(c_k),v_p(B_k),v_p(C_k),v_p(g_k)) at each directed port is:

z: (d,d,d,d+1,+1)
z*: (3-d,3-d,3-d,3-d,0)
r: (0,0,1,0,-1)
r*: (3,3,3,3,0).

Proof: Legendre's exact formulas for 0<k<p are
v_p(b_k)=floor(2k/p)+floor(3k/p),
v_p(c_k)=floor(4k/p).
The four explicit indices give the tabulated floors. Exactly one of the two paired numerator weights at z,z* is p-divisible, and exactly one of the denominator weights at r,r* is p-divisible; the other weights are p-adic units. Subtraction gives the g valuations. QED.

BRC scope: The unordered reflection-product readout modulo p^2 is reconstructed by the two normalized units with the source-sensitive E_p at one representative per orbit. Directed truncated weighted sums do not factor through that unordered readout: e.g. v_p(B_r)=1 versus v_p(B_r*)=3, so the two separately contribute differently mod p^3. Preserve orientation, signed weights, carries and original 216/2304 source labels for WZ construction.

## Actual exact regression

Python standard library checker d25_four_port_normalized_second_digit_20261103.py was run locally and returned PASS on all 77 target primes 13<=p<=2000 (four directed ports/prime). It builds h_kh_(p-k) from original p-stripped factorial units, computes undivided paired weights, tests the two normalized formulas modulo p^2 and the independent Legendre-directed valuations.

Selected (p, eta, z,z*, U_Z, r,r*, U_P) modulo p^2:
(13,5,8,5,14,2,11,9)
(19,3,7,12,303,3,16,354)
(373,5,233,140,47214,62,311,15460).

Research status: AUTHOR-DERIVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Mother target W216(p-1)=p modulo p^3 for p mod24 in {13,19}, equivalently frozen Delta_p-R_p=0 modulo p, remains open. The earlier 2304 Q4 tail proof and 301-prime scalar check are consumed, not repeated.

Next scientific unit: use two normalized orbit residues AND the oriented signed-summand valuation ledger as boundary conditions of a p-dependent terminating two-index weighted telescope. Verify full low-half/Q3-216 high-tail cancellation at p=13,19,373, retaining H2 and the source-specific -2p^3 modulo p^4 boundary. Port matching is only a local necessary test, not a WZ proof. Alternate direct route: 216 low-half/Q3 cancellation.

Native state read on 2026-11-03: Gateway 0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active quota 5/5. No native CLAIM/OPEN/Source checkpoint/Result/review. Prior requests #6637 and #6638, old session and staging unchanged. Control owner support #1558 remains for source reviewed code and binding restoration.