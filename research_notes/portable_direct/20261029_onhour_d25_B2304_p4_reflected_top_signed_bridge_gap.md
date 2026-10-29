# D25 SECOND-DIGIT-LIFT — B2304 fourth-digit reflected top port and the signed A−2B bridge gap

Date: 2026-10-29 Asia/Hong_Kong. Status: **AUTHOR-SIDE / PROVED DERIVATION + EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from the maintenance lane. Native session, CLAIM, run, continuation and Result are **not verified by this artifact**. A live Site status read on 2026-10-29 12:03 UTC returned `write_relay_enabled=false` and `research_authority_granted=false`; `em_status` / own checkpoint read returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`, with `operation_sent=false`. Neither permits declaring an empty native queue, resuming another session, or dispatching.

## Preserved original integer observer and exact theorem

For every prime p≥5, in Z_(p), let

\[
 a_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},\quad
 b_n=\frac{(4n)!}{(n!)^4 2304^n},
\quad A_p=\sum_{n=0}^{p-1}(6n+1)a_n,\quad
 B_p=\sum_{n=0}^{p-1}(8n+1)b_n.
\]

The p-adically normalized top tiers are original index sets

\[
 U_{A,p}=\sum_{n=\lceil2p/3\rceil}^{p-1}(6n+1)a_n,\qquad
 U_{B,p}=\sum_{n=\lceil3p/4\rceil}^{p-1}(8n+1)b_n.
\]

**NEW ALL-PRIME B2304 THEOREM.** For 0≤r≤floor((p−4)/4), n=p−1−r, the coefficient b_n has exact valuation v_p(b_n)=3. With every displayed denominator a p-unit,

\[
\boxed{\frac{b_{p-1-r}}{p^3}\equiv
-6\,2304^r\frac{(r!)^4}{(4r+3)!}\pmod p,}
\]

\[
\boxed{\frac{(8n+1)b_{p-1-r}}{p^3}\equiv
6(8r+7)2304^r\frac{(r!)^4}{(4r+3)!}\pmod p.}\tag{B-top}
\]

Consequently,

\[
\boxed{\frac{U_{B,p}}{p^3}\equiv
6\sum_{r=0}^{\lfloor(p-4)/4\rfloor}
(8r+7)2304^r\frac{(r!)^4}{(4r+3)!}\pmod p.}\tag{B-top-sum}
\]

**Proof.** Write 4n=3p+s, s=p−4r−4 in [0,p−1]. The factorial p-unit block identity
\((kp+s)!/p^k\equiv(-1)^k k!s!\pmod p\) for k=3 (and 3<p) gives \((4n)!/p^3\equiv-6s!\pmod p\). Wilson reflection yields \(s!\equiv1/(4r+3)!\), \((p−1−r)!\equiv(-1)^{r+1}/r!\pmod p\). Fermat gives \(2304^{-n}\equiv2304^r\pmod p\), and the original weight is \(8n+1\equiv-(8r+7)\). Combining proves both formulas. Exactly three multiples of p occur in (4n)!, and none in n!, giving the valuation. Reindex the finite original tail for the sum formula.

## Composition with already-proved A216 top port (REUSE_APPLIED)

The **previous**, separately attributed A216 theorem is `research_notes/portable_direct/20261029_onhour_d25_A216_p4_reflected_top_unit.md`, immutable commit `1e3cf81bf808d678cc2124b5c35da9a6a7bc9d95`; this note does **not** re-register it as new. Its bound and formula are

\[
\frac{U_{A,p}}{p^3}\equiv
2\sum_{r=0}^{\lfloor(p-3)/3\rfloor}
(6r+5)216^r\frac{(r!)^5}{(2r+1)!(3r+2)!}\pmod p.
\]

Define the **labelled, signed joint-port** correction

\[
\boxed{D_p=(U_{A,p}-2U_{B,p})/p^3\pmod p.}\tag{gap}
\]

The two summands come from genuinely different 216 and 2304 index populations and cannot be erased by applying the scalar sum comparison prematurely. For χ_p=(-3/p), introduce the full p⁴-bridge candidate \(C_p=A_p-2B_p+pχ_p\), and its two-top-tier-omitted version

\[
C_p^{\mathrm{low}}=(A_p-U_{A,p})-2(B_p-U_{B,p})+pχ_p.
\]

**Exact all-prime transfer identity**, with no assumed supercongruence:

\[
\boxed{C_p-C_p^{\mathrm{low}}=U_{A,p}-2U_{B,p}
\equiv p^3D_p\pmod{p^4}.}\tag{transport}
\]

The still-conjectural `C_p≡0 mod p⁴` would imply \(C_p^{low}/p³≡-D_p mod p\); this is **conditional**, not a proof of C_p. The original p³ target is unaffected by discarding these valuation-three terms, whereas the p⁴ candidate requires their source repair.

## Actually executed exact certificates, 2026-10-29

The independent stdlib check `d25_b2304_top_p4_bridge_guard_20261029.py` computed **all 237 primes 5≤p<1500** using modular coefficient recurrences, independently evaluated the two reflection sums by small integer factorials and checked original exact binomial sums at p=13,19,373. Both top-port reflections and transport identities passed for every prime; 235/237 gave nonzero D_p, with zero D_p only at p=107,1289 in this finite interval. No all-prime statement is inferred from counts. The code also checked the p⁴ bridge candidate for those cases in which the observed residue vanished; it does not promote the candidate to theorem.

| p | U_A/p³ mod p (prior theorem) | U_B/p³ mod p (new) | D_p mod p | C_low/p³ mod p (finite observation) |
|---:|---:|---:|---:|---:|
| 13 | 5 | 6 | 6 | 7 |
| 19 | 4 | 16 | 10 | 9 |
| 373 | 278 | 119 | 40 | 333 |

At p=373, \(U_{B,373}\equiv119·373^3=6,175,518,923\pmod{373^4}\); the joint high-source gap is \(40·373^3=2,075,804,680\pmod{373^4}\). The bridge with both tops deleted fails by the exact nonzero residue \(333·373^3\). This is a **counterexample to naive p⁴ top-tier erasure**, not to the full p⁴ conjecture.

BRC observer: two separately labelled signed weighted streams with original cutoffs and their p-adic valuation/precision strata; allowed operation: finite ring arithmetic through p⁴ plus signed linear comparison. Retained information: each port's cardinality, valuation, original sign/weight and independent factorial provenance. The scalar C_p is a derived observer; native Heartbeat X6 or actual H0/B0 Frobenius correspondence is not claimed.

## Frontier, scientific source and obligations

Highest verified author-side prior: finite conjectural bridge `A_p-2B_p+pχ_p≡0 (mod p⁴)` recorded at commit `33969de52a9ef512dea210487c844044ede74eda`; external Guo–Zudilin theorem proves **only** `B_p≡pχ_p (mod p³)`. The new theorem proves exactly the B top reflection and gap transport; it does not discharge the full bridge, frozen 216 first-five-port cancellation, or native benchmark.

Next **core** action: find an all-prime character-sensitive proof or falsifier for the full C_p bridge, retaining this D_p port in any p⁴ truncation. If reducing directly to p³, consume the proven p³ top invisibility and attack the original five 216 ports; do not repeat the completed A/B valuation tiers. The top coefficients are now available as an exact obstruction to an invalid fourth-digit simplification.

Native highest priority remains #1559: original fixed p=373 H0/B0 divided-power [X]U mod 139129, module rank, semilinear Frobenius direction/eta, signed odd Green/Hesse, κ and independent validation. No original native execution or owner acceptance was obtained in this author-only unit. Next capability route: canonical Source Task owner or authorized native evaluator consumes #1559 and produces its reproducible receipt. Frozen Source pin and P000 stay unchanged; do not copy the maintenance logical conversation identity.
