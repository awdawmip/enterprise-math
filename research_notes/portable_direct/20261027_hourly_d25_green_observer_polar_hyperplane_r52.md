# D25/LIFT R52 — Rank-one polar residue and the safe observer hyperplane

Date: 2026-10-27 Asia/Hong_Kong. Portable TASK_RESEARCH author-side theorem continuing exact R51 (commit 549175b8d514ae4da9a126edca4387213f2647d1). Logical lane chatgpt-research-hourly-enterprise-math-20260923; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent D25/LIFT/JT2 OPEN. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Author proof / exact check / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Full source-observer sensitivity rather than a single fixed observer

Let \(w_k,s_k\) be the unchanged original factorial sources in R47–R51, \(p\ge13\) prime, \(p\equiv1\pmod6\), and \(N=\lfloor(3p-1)/4\rfloor+1\). Let \(c=(c_0,\ldots,c_{N-1})\in\mathbb Z_{(p)}^N\) be any declared p-integral finite observer. Its *labelled* response pair is

$$ L_W=\sum_{k=0}^{N-1}c_kw_k,\qquad L_S=\sum_{k=0}^{N-1}c_ks_k. $$

As R50's Green identity is valid for every solution of the rank-two recurrence, its exact endpoint coefficients are

$$
\boxed{
C_N(c)=\frac{-L_Ws_{N+1}+L_Sw_{N+1}}{D_N},\qquad
C_{N+1}(c)=\frac{L_Ws_N-L_Sw_N}{D_N},\quad
D_N=w_Ns_N(b_N-a_N).
}\tag{R52-C}
$$

These formulas preserve the two source labels and exact finite endpoints. They do not turn arbitrary c into a WZ telescoper for the original fixed input.

## Theorem: exact rank-one fourth-order polar part at three primes

Reuse R51's classification: \(v_p(D_N)=6\) for all target primes except \(p\in E=\{139,199,277\}\), where \(v_p(D_N)=7\). Put \(\bar U=w_N/p^3\bmod p\), \(\bar V=s_N/p^3\bmod p\), both units.

At **each p in E**, set
$$
t=a_N\bmod p=b_N\bmod p,\quad
\delta=D_N/p^7\bmod p=\bar U\bar V((b_N-a_N)/p)\bmod p\ne0,
$$
and define the source-sensitive observer functional
$$
\boxed{T_p(c)=(L_W\bmod p)\bar V-(L_S\bmod p)\bar U\in\mathbb F_p.}
$$

Then the exact fourth-order polar residues are
$$
\boxed{
p^4C_{N+1}(c)\equiv\delta^{-1}T_p(c),\qquad
p^4C_N(c)\equiv-t\delta^{-1}T_p(c)\pmod p.
}\tag{R52-P}
$$

Consequently \(T_p(c)\ne0\) iff **both** Green endpoint coefficients have valuation \(-4\). When \(T_p(c)=0\), **both** valuations are at least \(-3\). The exceptional fourth-order polar component is therefore rank one, with a unique codimension-one kernel among finite p-integral observer vectors modulo p:
$$
\mathcal S_p=\{c:T_p(c)=0\}\subset\mathbb F_p^N.
$$

This is a *proven safe compression for the pole-order observable*, not a claim that all future source operations collapse to one scalar. To prove the codimension, the first two observer coordinates \(c_0,c_1\) give response columns \((w_0,s_0)=(1,1)\) and \((w_1,s_1)=(7/18,3/32)\). Their determinant is \(-85/288\), a p-unit for all p in E, so \(c\mapsto(L_W,L_S)\) is onto \(\mathbb F_p^2\); the functional \(T_p\) is nonzero because \(\bar U,\bar V\) are units.

For **nonexceptional** target primes, the same explicit Cramer formula proves \(v_p(C_N(c)),v_p(C_{N+1}(c))\ge-3\). Moreover \(\min v_p(C)=-3\) iff \((L_W,L_S)\not\equiv(0,0)\pmod p\), since the leading source-to-endpoint map has determinant proportional to \(a_N-b_N\), a p-unit. If both responses vanish modulo p, both coefficient valuations are at least \(-2\). This is a precise observer-dependent refinement of R51, not a new universal obstruction for W/S supercongruence.

**Proof of (R52-P).** Substitute \(w_N=p^3U,\ s_N=p^3V\) and \(w_{N+1}=a_Nw_N,\ s_{N+1}=b_Ns_N\) in (R52-C). Since \(D_N=p^7\delta'\) with \(\delta'\equiv\delta\not\equiv0\pmod p\), multiply by \(p^4\) and reduce. The numerator of \(C_{N+1}\) contributes \(L_WV-L_SU\). The numerator of \(C_N\) contributes \(-L_Wb_NV+L_Sa_NU\equiv-t(L_WV-L_SU)\). The claims about valuations and the safe kernel follow. QED.

## Exact p-adic certificates and concrete safe observers

| p | N | (U,V) mod p | (t,delta) mod p | c=(c0,c1) with safe T=0 | pole valuations for safe c | pole valuations for c=(0,1) |
|---:|---:|---:|---:|---:|---:|---:|
| 139 | 105 | (66,105) | (115,37) | (107,1) | (-3,-3) | (-4,-4) |
| 199 | 150 | (138,68) | (46,111) | (191,1) | (-3,-3) | (-4,-4) |
| 277 | 208 | (251,224) | (217,254) | (43,1) | (-3,-3) | (-4,-4) |

All other coordinates of c vanish. For the ordinary low-rank observer c=(0,1), the two \((p^4C_N,p^4C_{N+1})\bmod p\) pairs are (107,45), (51,133), (211,82), respectively. Companion standard-library script uses the immutable R51 script as the exact source implementation; it independently checks these response residues, Cramer identities, 3 safe observers and precise valuations. Executed: PASS.

**Operational consequence.** At the three resonant primes, an independently perturbed pair of high-endpoint inputs needs one extra p-adic digit to reconstruct an observer outside \(\mathcal S_p\) to a given precision; for an observer in \(\mathcal S_p\), this *extra resonant digit* is not needed. The theorem supplies an exact test for whether a future R23/R36 low-half observer is pole-sensitive: calculate its original, source-labelled \((L_W,L_S)\) modulo p and evaluate \(T_p\). Do not replace that future observer with c=(0,1).

BRC COMPOSE_APPLIED: observer, p-adic precision debt and two original source identities remain typed. No native X6 transfer, P000 replacement, or original W/S congruence proof is claimed.

**Frontier:** R51 universal exceptional-pole classification + R52 rank-one source-sensitive residue and safe-kernel theorem. **Do not redo:** R47–R50 statements or R51's c1-specific endpoint classification. **Next precise unit:** take R23's actual original low-half p²-divided signed weights, evaluate its R52 \(T_p\) at p=139,199,277 (preserving R36 Green and all six fixed-z=2 Hasse channels), then seek a source-faithful additive cross-rank WZ compensation at p=13,19,181,373. H0/B0, Frobenius eta/kappa, native p=373 and independent Driver review remain OPEN.

No fresh winning CLAIM/open/native checkpoint verified for this lane; GitHub evidence is author-side portable only. Research-Activity semantic registration/readback remains pending. Preserve prior session/staging/request identities and controller Issue #1558.
