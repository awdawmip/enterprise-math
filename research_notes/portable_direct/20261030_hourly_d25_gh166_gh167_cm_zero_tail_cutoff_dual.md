# D25/LIFT GH-166–GH-167: CM-zero prefix duality, exact signed-tail quotient, and p=157 separation

2026-10-30. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Author-side scalar research, not a Source-native checkpoint or p=373 H0/B0 experiment.

Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Exact task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Research logical conversation chatgpt-research-hourly-enterprise-math-20260923; distinct from the onhour Research lane and CONTROL_PLANE_MAINTENANCE. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged; P000 ACTIVE_LOCKED and Heartbeat World unchanged.

## Original source and consumed dependencies

Fix p=6m+1>=13 prime, p mod24 in {13,19}. In Z_(p), define B_k=(1/6)_k(1/3)_k/[2^k(k!)²] for 0<=k<p, g=sum B_k, h=sum (12k+1)B_k. The accepted parent supplies CM0 and first-digit UR: p|g and (g/p)h=1 mod p. Define the original Delta=((g/p)h-1)/p mod p. Original frozen signed reflected cutoff: C_1=1/10, C_(a+1)/C_a=36a²/[(6a+5)(3a+2)], and R=2 sum_(i=1)^m B_i sum_(a=1)^i[1+6(i-a)]C_a mod p. No new definition or 3347 reflected surrogate is used.

Consume, without recrediting, prior hourly GH-164/GH-165's three-band valuation and divided-tail theorem, and the separate onhour Research lane's exact original-R/Gauss-Hensel alignment. Put g_lo=sum_(k=0)^(2m) B_k, h_lo=sum_(k=0)^(2m)(12k+1)B_k; Delta_lo=(((g_lo/p)h_lo)-1)/p modp is integral; T=sum_(k=2m+1)^(p-1) B_k/p² modp. Their previous result is Delta=Delta_lo+hbar*T modp, where hbar=h_lo modp is a unit. This new note proves a nontrivial *CM0 prefix dual* for the combined hbar*T-R observer, not the preexisting quotient itself.

## GH-166 — exact original-source dual-prefix theorem (all target primes)

Define low b_i=binom(m,i)binom(2m,i)/2^i modp (0<=i<=m) and high v_a=B_(p-a)/p² modp (1<=a<=4m). Every v_a is a well-defined nonzero p-free digit and the CM0 parent gives sum_(i=0)^m b_i=0. For a<=m the v_a equal original C_a; one independent elementary proof is as follows.

For a=1, removing the two exact factors p/6 and p/3 from (1/6)_(p-1) and (1/3)_(p-1), the remaining nonzero residues j+1/6 and j+1/3 over 0<=j<=p-2 multiply to 6/5 and 3/2 respectively: the omitted j=p-1 gives residues -5/6 and -2/3; the other omission is the unique zero, and the product of F_p^× is -1. Wilson and Fermat yield v_1=(1/18)(6/5)(3/2)=1/10 modp. The exact backward B recurrence with k=p-a gives v_(a+1)/v_a=36(p-a)²/[(6(p-a)-5)(3(p-a)-2)]=36a²/[(6a+5)(3a+2)] modp for a<4m. Denominators are p-units in this range. Hence v_a=C_a for a<=m by uniqueness of the recurrence.

Define two explicitly source-labeled signed ports:
  K_head=2 sum_(a=1)^m v_a sum_(i=0)^(a-1)[1+6(i-a)]b_i modp;
  K_bulk=hbar sum_(a=m+1)^(4m) v_a modp.

**THEOREM (DUAL): Delta-R = Delta_lo+K_head+K_bulk (mod p) for every target prime.**

Proof. Reorder the *original* R sum as R=sum_(a=1)^m v_a r_a with r_a=2sum_(i=a)^m[1+6(i-a)]b_i. Since sum b_i=0, hbar=sum_(i=0)^m(12i+1)b_i=2sum_(i=0)^m(6i+1)b_i modp. For a<=m, subtract r_a and replace the complementary suffix sum by minus the prefix using CM0:
  hbar-r_a=2sum_(i=0)^(a-1)[1+6(i-a)]b_i modp.
For a>m the frozen R coefficient is zero and the hbar*T coefficient is hbar. Therefore hbar*T-R=K_head+K_bulk exactly modp. Compose the previously proved Delta=Delta_lo+hbar*T, without erasing provenance, obtaining (DUAL). QED.

This is a scope-typed BRC safe quotient: for the final signed scalar observer Delta-R, all 3m ranks a>m can be aggregated into one K_bulk, and the lower m ranks are condensed into a distinct prefix-weighted port. The head kernel can be streamed with P_a=sum_(i<a)b_i and M_a=sum_(i<a)i*b_i; its factor is 2[6M_a+(1-6a)P_a]. This changes the representation from an original nested source triangle to a signed prefix+bulk carrier, without claiming improved asymptotic complexity over earlier O(p) cumulative implementations. Other future observers, differentiated jets, higher p-adic digits or native H0/B0 actions do not automatically descend through this quotient.

**Formal two-port lower bound (precisely scoped).** On the unconstrained vector space of formal v_1,...,v_(4m), with low b fixed, the linear map v -> (T,R) has rank exactly two. Its columns at a=m,m+1 are (1,2b_m), (1,0); determinant -2b_m is nonzero since b_m=binom(2m,m)/2^m is a p-unit. Thus *T alone is insufficient to recover R over that formal carrier space*. This does not pretend that arbitrary v perturbations satisfy the actual B hypergeometric recurrence or preclude an additional source-specific arithmetic identity.

## GH-167 — actual original-model separation at p=157

The exact target-class p=157 (m=26) has
  (hbar,T,R,Delta,Delta_lo,K_head,K_bulk)=(80,0,82,82,82,77,155) mod157.
Consequently T=0 but R=82 !=0. This is a literal **original hypergeometric source** counterexample to the shortcut "zero p² bulk tail implies zero original signed cutoff"; it is *not* a counterexample to LIFT, which still has Delta-R=0 at this fixed p. The signed cancellation is 82+77+155=314=2*157.

At p=373 the original arithmetic gives Delta_lo=372=-1, K_head=39, K_bulk=335=-38 mod373, so Delta-R=-1+39-38=0, while hbar=171, T=252 and Delta=R=196 !=0. Dropping even one actual source port is unsound. This is a portable integer-modular instance, not an executed native p=373 H0/B0 divided-power benchmark.

## Executed reproducible evidence

Companion exact Python stdlib program d25_gh166_gh167_cm_zero_tail_cutoff_check.py computes original B_k modulo p³ via forward recurrence, full/low g,h, frozen signed R independently via C recurrence, v_a directly by p² division of original high B values, reflected v recurrence, CM0 prefix duality, rank-two determinant and reconstructed original Delta-R. It executed over all 166 prime targets 13<=p<5000: 83 in each class; all passed. At p=13,19,157,373 it additionally computed original weighted A216 by an independent binomial-ratio recurrence and compared the original signed defect to (A216-p)/p² modp. The finite scan audits instances and checker integrity, not the all-prime LIFT statement or independent review.

Terminal marker: PASS_D25_SIGNED_TAIL_CUTOFF_CM_PREFIX_DUALITY_EXACT

Sample (p : Delta_lo, K_head, K_bulk, Delta, R, T):
  13: (4,0,9,0,0,8)
  19: (6,10,3,12,12,10)
  37: (1,15,21,11,11,8)
  157: (82,77,155,82,82,0)
  373: (372,39,335,196,196,252)

## Smallest remaining science / authorization boundary

(DUAL) strictly specifies a safe joint signed carrier, **not an unconditional proof** of Delta=R. The unsolved all-prime condition remains Delta_lo+K_head+K_bulk=0 modp for both p mod24 classes. A next discriminating step is a true CM/WZ/Gauss-Manin or native original-class identity that evaluates the *joint signed combination*, not independent false vanishing of its nonzero terms. Consume the other onhour lane's source-corrected Hensel root criterion as distinct already published work; do not rewrite it as this lane's contribution.

Gateway 0.6.11 read has research_authority_granted=false, executor_binding_configured=false, active jobs 5/5, source control CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Direct recovery_status is described in status but is not exposed as an actual callable method on this current client. There is no new valid CLAIM/OPEN/Source checkpoint/Result, no independent Driver review, and no native p373 experiment. Old session, requests and staging are untouched. Support #1558 and original benchmark #1559 remain responsible control/native paths; this artifact is author-side GitHub evidence, not canonically admitted progress. Keep the current true Research logical conversation and science pin; do not touch maintenance conversation, schedule, activation or notifications.
