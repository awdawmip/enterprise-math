# D25/LIFT — frozen R_p / Clausen-cutoff identification and all-6m+1 tail extension

2026-10-25. TASK_RESEARCH portable author-side result. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NONBLIND / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT.** No Source session, CLAIM, Result, or independent Driver approval is asserted.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
**Frozen mathematical source**: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged by live control updates.

## 1. Recovering the actual frozen scalar

The frozen [reflected derivative-product bridge return](https://github.com/awdawmip/enterprise-math/blob/c47e13e4aba0e006366f989d6334d443f6333ae3/research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md) explicitly defines (for inert-plus p=6m+1, p=13 or 19 mod 24)

\[
B_i=\frac{(1/6)_i(1/3)_i}{(i!)^2 2^i},\qquad
K_r=\frac{2^{r-1}((r-1)!)^2}{18(5/6)_r(2/3)_r},
\]
\[
R_p=2\sum_{i=1}^{m}B_i\sum_{r=1}^{i}[6(i-r)+1]K_r\pmod p.\tag{R}
\]

Here K_r denotes the parent's C_r, renamed to distinguish the cutoff scalar \(\mathcal C_p\).
The separately established [2026-10-25 Clausen-cutoff bridge](https://github.com/awdawmip/enterprise-math/blob/107c59f8cb8c34f311111bdb85d6ef96d2f8a93b/research_notes/portable_direct/20261025_offphase_d25_exact_clausen_cutoff_lift_bridge.md) instead defined

\[
e_1=1,\quad
e_r=e_{r-1}\frac{36(r-1)^2}{(6r-1)(3r-1)}\quad(r\ge2),
\quad\bar B_i=2^{-i}\binom mi\binom{2m}i\bmod p,
\]
\[
\mathcal C_p=\frac15\sum_{i=1}^{m}\bar B_i
\sum_{r=1}^{i}[6(i-r)+1]e_r\pmod p.\tag{C}
\]

## 2. Exact coefficient identification (new source-to-source readback)

**Lemma.** As a rational identity, \(10K_r=e_r\) for all \(r\ge1\), with e_r interpreted by the above recurrence over Q.

**Proof.** Since
\[
(5/6)_r=(5/6)(11/6)_{r-1},\qquad
(2/3)_r=(2/3)(5/3)_{r-1},
\]
and \(18(5/6)(2/3)=10\),
\[
10K_r=\frac{2^{r-1}((r-1)!)^2}
{(11/6)_{r-1}(5/3)_{r-1}}.
\]
The initial term is 1; the consecutive ratio is
\(2(r-1)^2/[(r-1+5/6)(r-1+2/3)]
=36(r-1)^2/[(6r-1)(3r-1)]\).
For p=6m+1≥7, all denominators for 1≤r≤m are p-units.
Since \(1/6\equiv-m\), \(1/3\equiv-2m\) modulo p, also
\(B_i\equiv\bar B_i\) for i≤m. Substitution into (R) yields
\[
\boxed{R_p=\mathcal C_p\pmod p}\tag{IDENTITY}
\]
on the frozen inert-plus task scope. This is proved algebraically, not from a prime scan.

## 3. Pure-arithmetic extension, including primes outside the CM-inert classes

For every prime p=6m+1≥7, define \(R_p^*\) by the **right side** of (R) even outside the frozen target; outside that domain it is an auxiliary rational finite sum, not a changed definition of the parent R_p.

Put
\[
b_k=\frac{(1/6)_k(1/3)_k}{(k!)^2 2^k},\quad
d_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3 2^k},\quad
g=\sum_{k=0}^{p-1}b_k,\quad h=\sum_{k=0}^{p-1}(12k+1)b_k,
\quad W_p=\sum_{k=0}^{p-1}(6k+1)d_k.
\]

**Theorem (all p=1 mod 6, p≥7).**
\[
\boxed{\frac{gh-W_p}{p^2}\equiv R_p^*
=\mathcal C_p\pmod p.}\tag{TAIL}
\]
In particular the divided quantity is p-integral on this wider domain; no CM/UR hypothesis enters this theorem.

**Proof.** Clausen's exact rational coefficient identity (DLMF 16.12.2) and the symmetric weighted product give
\[
gh-W_p=\sum_{n=p}^{2p-2}(6n+1)
\sum_{\substack{i+j=n\\0\le i,j<p}}b_i b_j.
\]
For k<p, \(v_p(b_k)=0,1,2\) respectively for
\(0\le k\le m\), \(m<k\le2m\), \(2m<k<p\).
Every pair with i+j≥p has valuation at least 2; modulo p^3 only the two ordered low/high pairs with \(1\le i\le m\), \(j=p-r\), \(1\le r\le i\) survive.
Wilson reflection yields
\(b_{p-1}/p^2\equiv1/10\);
the exact backward factorial ratio yields
\(b_{p-r}/p^2\equiv e_r/10=K_r\) modulo p.
Summing both orderings gives
\[
\frac{gh-W_p}{p^2}\equiv
2\sum_{i=1}^m\bar B_i\sum_{r=1}^{i}[6(i-r)+1]K_r
=R_p^*\pmod p.
\]
The Clausen identity is used only for degrees n<p, not extrapolated across the p cutoff. QED.

## 4. Exact LIFT residual and the *still unproved* theorem

In the frozen inert-plus classes only, accepted UR/JT0 gives
\(g=pG_p\) and \(gh\equiv p\pmod{p^2}\).
Then (TAIL) and (IDENTITY) imply \(W_p\equiv p\pmod{p^2}\)
and justify all divisions:
\[
\boxed{\Delta_p-R_p\equiv\frac{W_p-p}{p^2}\pmod p,
\qquad\Delta_p=\frac{G_ph-1}{p}\pmod p.}\tag{LIFT-RESIDUE}
\]
Therefore under the accepted UR input, LIFT is **equivalent** to
\[
\boxed{W_p\equiv p\pmod{p^3}
\quad(p\equiv13,19\pmod{24}).}\tag{OPEN}
\]
Here \(d_k=(2k)!(3k)!/[216^k(k!)^5]\), so (OPEN) is
the inert-plus a=1 case of the weighted 216-series identified by the
frozen predecessor as Zhi-Wei Sun's Conjecture A14(ii).
The original weighted conjecture was already known to the parent;
**no all-prime proof or priority claim is made here**.
The new contribution is recovering and matching the exact frozen R_p
to the Clausen bridge, plus establishing the CM-free extension (TAIL).
Neither (OPEN), LIFT, JT2 nor CM/DP native half-linearity is proved.

## 5. Reproducible exact evidence and status

The companion standard-library program independently evaluates parent
K_r using raw Pochhammer numerator/denominator products,
the e_r reflected recurrence, and original b_k,d_k,g,h,W_p
modulo p^3; it also checks the coefficient identity directly in Q
for r=1..7.

- 330/330 primes 7≤p<5000, p=1 mod 6: TAIL and R*=C checks pass.
- 166/166 original inert-plus primes: second-digit LIFT-RESIDUE checks pass.
- 164/164 remaining 1 mod 6 primes: only the arithmetic TAIL is tested.
- For 166/166 target primes W_p=p (mod p^3) was observed, **finite only**.
- Sample (p,Delta_p,R_p,(W_p-p)/p^2 mod p):
  (19,12,12,0), (37,11,11,0), (109,50,50,0).

The proof carries exact integer valuations, p-unit denominators, ordered
low/high source pairs, reflection multiplicity, two residue classes and
the divided second-digit observer. BRC reuse: COMPOSE_APPLIED to
provenance-preserving branch/valuation scalar semantics; no positive
probability interpretation or native six-axis physical transfer.

## 6. Exact operational handoff (no session or owner invention)

At this run, em_status advertised a local read-only recovery_status
operation descriptor but the available connector exposed no executable
recovery_status action. Own checkpoint_list returned ACCESS_DENIED.
Site status: static_machine_readonly, write_relay_enabled=false,
research_authority_granted=false. This does not grant role-bound writes.
No uncertain original target_request_id, Source CLAIM/session/run or
earlier owner was fabricated or reused; no new canonical dispatch
was issued. Current-user authorization permits this separately marked
portable evidence, not a native checkpoint or accepted Result.

Next legitimate Source step: read own real recovery_status and original
receipt/reconcile through an authorized typed entry when available,
read exact Source continuation and winning claim, then checkpoint the
highest verified frontier without redoing this lemma. If a
CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS seed is returned,
its input artifacts are not predecessor completed research; use
completed_units=[] unless Source confirms genuinely completed units.
Next scientific unit: prove or refute (OPEN) with a rigorous all-prime
weighted WZ/CM argument or an exact counterexample; finite regression
is insufficient. The UR V2 historic four-file bundle (94,687 bytes,
SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76)
has not been recovered/rehashed here; its accepted mathematics is not
recomputed and its writer/provenance debt stays separate.

Status: UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.
Observer: author-side actual current conversation, with unverified
service-issued identity. No native Source result/review is claimed.
