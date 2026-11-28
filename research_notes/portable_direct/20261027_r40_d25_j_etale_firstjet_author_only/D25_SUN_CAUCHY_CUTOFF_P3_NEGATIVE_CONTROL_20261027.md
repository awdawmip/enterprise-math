# D25 — exact finite Cauchy cutoff and noncommutation at the third p-adic digit

2026-10-27. **AUTHOR DERIVED / EXACT AUTHOR CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.** Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 and taskbook blob 53a3ef039325534e3715add837f0eee332289984 unchanged.

Roman Le Lan, *Series for 1/pi arising from Cauchy product*, arXiv:2604.03327v2 (10 April 2026), Lemma 1 and (3.1)–(3.2): https://arxiv.org/html/2604.03327v2 . The paper proves an analytic series identity; its Sun mod-p² congruence is explicitly conjectural. This new author-side unit examines a distinct finite-p³ observer, not the truth of that conjecture.

Let c_k=(3k)!(2k)!/[216^k(k!)^5], u_j=binom(2j,j)/8^j,
W_N=sum_{k=0}^{N-1}(6k+1)c_k, and
S_N=sum_{n=0}^{N-1}(3n-1)/2^n * sum_{k=0}^n binom(-1/3,k)binom(-2/3,n-k)binom(-1/6,k)binom(-5/6,n-k).

**All-N exact theorem.** Euler's transformation and the cited coefficientwise Cauchy lemma give, as formal Q-series,
F(1/3,1/6;1;z) F(2/3,5/6;1;z)
  = (1-z)^(-1/2) sum_{k>=0} c_k (2z)^k.
Multiplying the nth coefficient by (3n-1)/2^n proves for EVERY finite N>=1 the exact identity
  S_N = sum_{j,k>=0; j+k<N} (3(j+k)-1) u_j c_k.
Writing U_r=sum_{j<r}u_j and V_r=sum_{j<r}j*u_j, reorder finite terms to obtain the exact signed cutoff-defect formula
  E_p := S_p-W_p = sum_{k<p} c_k [(3k-1)U_{p-k}+3V_{p-k}-(6k+1)].
All steps are finite rational identities without use of any conjecture. The triangle j+k<p is NOT the original W_p single-index cutoff.

**Exact target-class counterexample to a proposed shortcut.** Independently evaluate each coefficient by the nested Pochhammer factors and the u*c convolution in Z/p³ using p-unit inverse recurrences. At p=19:
  W_19 mod6859=19; S_19 mod6859=3268;
  E_19 mod6859=3249=9*19² !=0 mod19³.
At p=373:
  W_373 mod51895117=373; S_373 mod51895117=8487242;
  E_373 mod51895117=8486869=61*373².
Exact finite regression covered p=13,19,37,43,211,373 (all assertions PASS), and separate rational coefficient checks at indices n=0..9 matched. In all reported cases W_p modp³=p, but those finite checks are not a uniform proof.

Hence formal Cauchy/Euler equivalence does NOT justify transporting a finite weighted p³ supercongruence from S_p to W_p by simply changing the summation cutoff. The p=19 result is a counterexample to that proposed transportation, **not** a counterexample to original LIFT/JT2. Sun's mod-p² conjecture does not on its own close a p³ obligation.

Independent reproduction with Python standard-library integer modular arithmetic: define A_0=B_0=c_0=u_0=1 and for 0<=k<p-1 use
  A_{k+1}=A_k*(3k+1)*(6k+1)/(18*(k+1)^2),
  B_{k+1}=B_k*(3k+2)*(6k+5)/(18*(k+1)^2),
  c_{k+1}=c_k*(2k+1)*(3k+1)*(3k+2)/(36*(k+1)^3),
  u_{k+1}=u_k*(2k+1)/(4*(k+1)),
all in Z/p³. Check for every n<p:
  2^{-n} sum_{k=0}^n A_k B_{n-k} == sum_{j=0}^n u_j c_{n-j} (mod p³).
Then weighted sum S=sum_{n<p}(3n-1)*rhs; W=sum_{k<p}(6k+1)c_k. This deterministic certificate specifies all operations and expected outputs above.

**BRC information boundary.** Source-labelled pair (j,k), signed weight and triangular cutoff are the preserved carrier; E_p retains v_19(E_19)=2 and is observable precisely at p³. The valid compression is the proven finite reordering; the invalid quotient drops cutoff provenance. E_p is NOT the previously source-aligned Clausen Q/p²=R_p. External ordinary hypergeometric arithmetic has no claimed native X6/three-dimensional-slice mapping or original H0/B0 Frobenius action.

The frozen original observer bridge (previous author note research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md, commit 2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be) is inherited, not re-proved. LIFT remains an all-prime Delta_p-R_p obligation; native original fixed-class p=373 H0/B0 [X]U mod139129, rank, semilinear orientation, normalization and signed readouts remain support Issue #1559, with no owner/native run verified. Gateway request 2026-10-27 returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; Site config remains static_machine_readonly / write_relay_enabled=false. Thus this Draft-only evidence does not assert a native session, winning CLAIM, OPEN, Source checkpoint, predecessor completed work or review.

UR V2 exact original recovery remains required: 94,687 bytes and SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; inherited UR mathematics is not repeated. Next control action is legal original-request receipt/own Source continuation then writer/provenance if truly authorized; next scientific action is exact evaluation of E_p/p² modp or the authentic original-class H0/B0–Delta-R transfer. Local full manuscript and exact author checker accompany this author's conversation handoff, but the GitHub Draft itself is *not* mathematical admission.
