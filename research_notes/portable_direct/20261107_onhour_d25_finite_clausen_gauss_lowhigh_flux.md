# D25 — Finite Clausen-square third-digit bridge and universal signed low–high boundary

Date: 2026-11-07 (Asia/Hong_Kong). Research lane: chatgpt-research-onhour-enterprise-math-20260923. Publication: TP2-B6F4FC938FF94941C1B7; original frozen scientific input pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Source role/CLAIM unavailable on this turn; status: AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED. This mathematical arithmetic calculation is NOT the native H0/B0 benchmark.

## Theorem (every prime p=6m+1>3)

All congruences below take place in the localized rational ring Z_(p); z=1/2. Put

- a_n=(2n)!(3n)!/[216^n(n!)^5] = (1/2)_n(1/3)_n(2/3)_n/[2^n(n!)^3].
- W_p=Σ_{n=0}^{p-1}(6n+1)a_n.
- u_k=(1/6)_k(1/3)_k/(k!)², F_p(z)=Σ_{k=0}^{p-1}u_k z^k.
- h_1=1/10 in F_p and h_(ell+1)=h_ell *18ell²/[(6ell+5)(3ell+2)] in F_p for 1<=ell<m.
- K_p=Σ_{i=1}^m Σ_{ell=1}^i (6(i-ell)+1) (u_i mod p) h_ell 2^[-(i-ell)] in F_p.

Then the exact third-digit identity is

**W_p ≡ F_p(1/2)[F_p(1/2)+6F'_p(1/2)] - p² K_p (mod p³).**

The kernel K_p is a signed/provenance-labelled sum of low–high coefficient pairs; the h recurrence is independent of p except the length m and coefficient reduction.

## Proof

1. Classical Clausen identity, as a formal rational power series, gives
   [2F1(1/6,1/3;1;z)]² = 3F2(1/2,1/3,2/3;1,1;z).
   Its degree n coefficient for n<p is exactly a_n/(z/2)^n, in the sense that the coefficient of z^n is 2^n a_n. Reference: NIST DLMF §16.12.2, https://dlmf.nist.gov/16.12.
   For the finite F_p, truncating its square at degree <p therefore yields Σ_{n=0}^{p-1}(2^n a_n)z^n, exactly over Q. Applying (1+6z d/dz) at z=1/2 yields W_p.

2. Define the exact finite polynomial tail B_p(z)=Σ_{0<=i,j<p; i+j>=p}(6(i+j)+1)u_i u_j z^{i+j}. From the previous equality, for z=1/2 in Q,
   W_p = F_p(z)[F_p(z)+12zF'_p(z)] - B_p(z).
   Thus the coefficient 6 multiplying F'_p at z=1/2 is exact, not a heuristic truncation.

3. The unique p-divisible factor in (1/6)_k appears upon k=m+1, and in (1/3)_k upon k=2m+1. Since k<p, the exact valuations are
   v_p(u_k)=0 for 0<=k<=m; =1 for m<k<=2m; =2 for 2m<k<p.
   Among ordered pairs (i,j) with i+j>=p, valuation exactly 2 is possible ONLY if 1<=i<=m and p-i<=j<p, or with i,j reversed. Middle–middle cannot reach index p; middle–high has valuation >=3 and high–high >=4. Hence B_p(1/2) is divisible by p², and modulo p³ only these two ordered low–high bands remain.

4. Set h_ell ≡u_(p-ell)/p² (mod p), 1<=ell<=m. First,
   u_(p-1)/p² = [Π_(r=0..p-2,r≠m)(6r+1)] [Π_(r=0..p-2,r≠2m)(3r+1)] / [18^(p-1)((p-1)!)²].
   Each numerator product runs through all nonzero residues except the missing r=p-1 factor: these are -5 and -2 respectively. Wilson and Fermat therefore give h_1 = 1/10 (mod p).
   From u_k/u_(k-1)=(6k-5)(3k-2)/(18k²) and k=p-ell, obtain
   h_(ell+1)/h_ell ≡18ell²/[(6ell+5)(3ell+2)] (mod p).
   All denominators are invertible for 1<=ell<m. This determines the entire high-index p² residue from one universal kernel.

5. In the two low–high strips, substitute j=p-ell and pair the symmetric (j,i) term. Since 2*2^(-p) ≡1 (mod p), and 6(i+p-ell)+1 ≡6(i-ell)+1 (mod p),
   B_p(1/2)/p² ≡ Σ_(i=1..m)Σ_(ell=1..i)(6(i-ell)+1)u_i h_ell 2^[-(i-ell)] =K_p (mod p).
   Substituting into Step 2 proves the theorem.

## Exact arithmetic and observations

Checker: d25_clausen_finite_tail_20261107.py, Python 3 standard library; it constructs original a_n and Gauss u_k via independent hypergeometric recurrences modulo p³; directly checks the full double-index tail for p<=373, checks the full lower–higher band for every p, independently checks h_ell from its universal recurrence against u_(p-ell)/p², and verifies the theorem against the original W_p. Executed for every prime p≡1 (mod6), 7<=p<=1999 (148 primes), plus p=5113: all PASS. This is a finite exact arithmetic check, complementary to the general proof.

Explicit (p, K_p, Gauss-product mod p³, W_p mod p³):
- (13, 0, 13, 13);
- (19, 12, 4351, 19); p² K=4332;
- (67, 21, 94336, 67); p² K=94269;
- (373, 196, 27269657, 373); p² K=27269284;
- (5113, 300, 7842835813, 5113).
At p=19 and p=373, the boundary is nonzero and removes precisely the excess of the full Gauss-product observer over W_p. Do not identify this K_p with older Clausen J_p without an independently checked observer map.

## Frozen mother objective and next exact action

Mother goal (still open): W_p ≡p (mod p³) for p≡13,19 (mod24), equivalently frozen Δ_p-R_p≡0 (mod p).

For the subfamily in which F_p(1/2) ≡0 (mod p), the theorem reduces the mother target to the exact Gauss-jet/boundary congruence
   [F_p(1/2)/p]*[F_p(1/2)+6F'_p(1/2)] ≡1+p K_p (mod p²).
The division requires the stated mod-p vanishing. All-prime residue-class zero-port selection is a separate open obligation; previous 611-prime Pfaff evidence is finite, not a proof. Test analytic/finite-field transformations for port selection; in parallel construct a WZ or Gauss-jet certificate for the displayed p² congruence using the explicit K_p, preserving the original signed boundary. Never dismiss K_p as a negligible tail.

BRC COMPOSE_APPLIED: population = ordered (i,j) with i+j>=p; state=(i,j, u_i,u_j,v_p, signed (6(i+j)+1)2^[-(i+j)]); observer = weighted sum modulo p³; operation = derivative then finite truncation. Both orientation/valuation labels are retained until exact symmetric pairing. Replacing this carrier by a total without the p² correction loses K_p (witness p=19). No native BRC runtime invocation is claimed.

### Durable recovery (author-side only)

- Prior immutable author-side frontier: ec1882fee656ccf64a4172677e02225e8e8a337b, previous Pfaff/Hensel port result; existing original216 three-shell, Green and Franel results consumed, not repeated.
- This new note/checker/continuation form source-separated author-side research, not an admitted Source checkpoint or native RESULT.
- Original request_id: onhour11-20261106-1400-exact-research-lane-continuation; prior receipt QUEUED is historical. This turn em_status, receipt and checkpoint read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Site config phase CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false. Native session/CLAIM/open/run NOT_VERIFIED; historical checkpoint rev22 not refreshed.
- Recovery: verify a dedicated Site-bound backend client, backend version and secure user-entered credential through the legitimate operator route; then read original receipt/continuation before any session or CLAIM. No maintenance-lane identity used.
- Native p=373 H0/B0 divided-power/Frobenius/Hesse Green and independent reproduction remain NOT_EXECUTED / PENDING_OWNER under issue #1559; new portable arithmetic does not substitute for that benchmark.
