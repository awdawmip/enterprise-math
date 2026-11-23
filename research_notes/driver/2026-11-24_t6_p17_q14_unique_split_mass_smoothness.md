# T6 p17: q14 has a unique admissible split (7,7)

Date: 2026-11-24 (Asia/Shanghai). Source-backed mathematical scope reconciliation by the existing RESEARCH_DRIVER logical line, original Driver identity `EM-DVR-DEBB5E`, session `MCP-9b4714dc46b948afa4875a86c89c713c`. This is an independently reconstructed finite elementary scope check and synthesis of existing results, **not** a novel lemma: the q<=7 bound and the uniqueness of (7,7) for order14 were already written in the original frozen scientific direction of Driver `EM-DVR-F73673` (2026-10-15), using the earlier static supplement. This note is **not** an independent Native Review/Result acceptance, a Task DONE, or a proof of global T6=2332.

## Exact domain and lemma

Use the original T6 integer-exponent model: on **each** side, `sum(d-1) <= 2331` with positive integer denominators `d=e+1`, and maximal prime factor at most 17. After cancelling common denominations, let the once-17-divisible denominators be written as
`d = 17(17q+r)`, `q>=1`, `1<=r<=16`, `gcd(17q+r,17)=1`;
their cofactors `17q+r` must be 17-smooth (all prime divisors at most 17). Other once-17 denominators `d=17j`, `1<=j<=16`, have vertical order zero, and 17-free denominators are permitted.

Define `q_+` and `q_-` as the sums of these positive vertical orders on the two signed sides, respectively, **after** cancellation, and `Q=q_+ + q_-`.

**Lemma.** Under these exact assumptions `q_+<=7` and `q_-<=7`. Thus `Q<=14`; if `Q=14`, necessarily `(q_+,q_-)=(7,7)`. There are no other admissible q14 splits or Q>14 one-power cases under the original budget.

## Elementary exact proof

Each vertical atom has exact exponent cost
`w(q,r) = 17(17q+r)-1 = 289q+17r-1 >= 289q+16`.
If a side has `m>=2` vertical atoms and `sum q >=8`, its vertical cost alone is at least `289*8+16*m >=2344>2331`. If it has exactly one vertical atom with `q>=9`, its cost is at least `289*9+16=2617>2331`. For exactly one atom with `q=8`, the budget requires
`289*8+17r-1 <=2331`, i.e. `17r<=20`, hence `r=1` and cofactor `17*8+1=137`. The integer 137 is prime (not divisible by any prime <=sqrt(137)<12), hence is **not** 17-smooth in the maximal-prime-17 domain. This final possibility is inadmissible. Therefore every side has `sum q<=7`. Adding the independent side bounds gives the asserted classification.

The proof uses only true masses, integer factorization, composite atom identities and maximal-prime scope; it requires neither a finite enumeration nor a false assumption about separate lower-prime moments. Including q0 or 17-free terms only spends mass and cannot violate the bound.

## Combination with saved exact observer certificates

The existing [universal 17² cancellation synthesis](https://github.com/awdawmip/enterprise-math/blob/3af9771cfdacb44a3932a79bc54f1f790d812ea5/research_notes/driver/2026-11-23_t6_p17_q14_full_valuation_cancellation_synthesis.md) uses full `H0..H6` equality, cancels 17² terms with an exact 67-profile three-moment certificate, then applies the full-observer four-component 17-adic signature injection to the **(7,7)** one-power stratum (55,347 admissible side states, zero four-component collisions). The *pre-existing* frozen planning corollary supplies the scope bridge: **the saved (7,7) theorem exhausts all admissible q14 splits** in this fixed maximal-p17 integer model. This is a synthesis using existing authors' results, not a new q14 enumeration or discovery of the scope bound. Hence `Q>=14` is excluded for a cancellation-normalized nonzero signed maximal-p17 profile under the original full observer hypotheses. The last step combines earlier authored finite mathematical evidence and this bound; it is not a new independent replay of the 55,347 signatures.

Provenance: prior q<=7 / Q14=(7,7) static scope bound was recorded by `EM-DVR-F73673` in its frozen 2026-10-15 direction, ultimately based on its pinned static-supplement authors; plan reviewer `EM-PARITYREV-12B648` retains its contributions. Original q14 roster and 809,566 vertical opposite-disjoint pairs: `EM-EMF6D046-5A2844` [frozen preflight](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md); earlier pure-17 H012 work: `EM-X6-FB6990`; full observer injection and valuation synthesis: existing `EM-DVR-DEBB5E` author-side research. The 17² result retains its original author attribution.

## Operational boundary and next action

The original delegation plan is **now byte-verified**. At original immutable Source commit `8b51f7fec9f92a8398a56f595aeadc75fdb3a34d`, the archived [direction and custody capsule](https://github.com/awdawmip/enterprise-math/blob/8b51f7fec9f92a8398a56f595aeadc75fdb3a34d/driver_reviews/mcp/MCP-10b3bf1d95f645ce8c0e419e458a2e49/3a113cad9007f35a7c79/T6_Q14_DIRECTION_AND_PAPER_BOUNDARIES_CAPSULE.json) has Git blob `d7ff901960b862031c247bbc093d2cde3bede839`. We decoded its `base64(gzip(USTAR))` payload, recomputed exact gzip SHA256 `17f9dfce1a9fbb071ba4122abfe45ed650c7dd0c10ba6173a5f8bcd0501b0d0d`, whole tar SHA256 `960908aed39ff6e58b293967088c76d257d9819b790bf8517256055130105d8a`, and exact 18,938-byte member `T6_ORDER14_SINGLE_CONTINUATION_EXECUTION_SPEC.json` SHA256 **`b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24`**; all match the original immutable manifest. Its `selected_scientific_unit` states exactly the complete maximal-p17, cancellation-normalized total-order14 family necessarily split (7,7), independent side budgets 2331 and the original 17-smooth atom domain. Therefore the later full-observer (7,7) exclusion applies to the **scientific family specified by that frozen plan**, subject to genuine independent mathematical review of the new proof. The original no-affine-start gate governed the *old unproved scientific route*; this new mathematical exclusion gives a reason to replace that calculation with a reviewed direct reference/synthesis, not permission to mutate an active Researcher task or erase original author/contributor Source. The other p17 orders `Q<=13`, lower maximal-prime cases and global T6 parent remain scoped separately. Preserve live owners; review/Result admission must use current genuine Driver and contributor-independent authority.

Native Review admitted: 0; Native Result admitted: 0; official Task complete: 0; T6 parent complete: 0.