# D25 original216: all-prime quadratic-twist hypothesis and a sharp p^4 counterexample

Date: 2026-11-07 (Asia/Hong_Kong). This is an **author-side finite computational discovery with an exact special-case counterexample**, not a general all-prime theorem or a Source Result. Active research task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`. The CONTROL_PLANE_MAINTENANCE conversation is excluded. Parent accepted CM0/UR and previously proven R/K bridge remain consumed, not reproduced.

## Smallest newly tested mathematical unit

Retain the **original unchanged 216 object**
[
a_k=rac{(2k)!(3k)!}{216^k(k!)^5}
=rac{inom{2k}{k}^2inom{3k}{k}}{216^k},
qquad
W_p=sum_{k=0}^{p-1}(6k+1)a_kinmathbb Z_{(p)}.
]
For every prime `p>3`, `216` is a p-unit. Its exact term recurrence is
[
a_0=1,quad
a_{k+1}=a_krac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}quad (0le k<p-1).
]
This supplies two independent exact integer algorithms: a modular term recurrence and the factorial/binomial coefficient expression. All reductions are integer arithmetic modulo `p^3`.

**Finite exhaustive certificate (PROVED FOR DECLARED FINITE SET):** For every prime `5<=p<10000`,
[
oxed{W_pequiv pleft(rac{-3}{p}ight)pmod{p^3}.}
]
The sieve enumerated **1227** primes, partitioned into **611** `p≡1 (mod3)` and **616** `p≡2 (mod3)`. A modular recurrence checked every prime: **0 failed**. For all **77** primes `p<=401`, independently recomputed the entire sum using `binom(2k,k)^2 binom(3k,k)`: **0 discrepancies**. The script used is `research_notes/portable_direct/d25_allprime_twist_verify_20261107.py`; source exact bytes were compiled and executed locally. No uncertainty or floating point enters the computation.

The existing frozen target `p≡13,19 (mod24)` lies in the positive-character branch. The 616 negative-character primes add a **genuinely distinct candidate branch** for a common hypergeometric proof, rather than another evaluation of the already tested positive target. The extension to **all primes p>3** remains **CONJECTURE / NOT_PROVED**:
[
W_pstackrel{?}{equiv}pleft(rac{-3}{p}ight)pmod{p^3}.
]
Here `(-3/p)=+1` iff `p≡1 (mod3)`, and `-1` iff `p≡2 (mod3)`.

## Exact sharpness witness (PROVED SINGLE CASE)

The tempting blanket improvement to modulus `p^4` is **false**, already at `p=7`. Direct exact term recurrence modulo `7^4=2401` gives
[
 W_7equiv350=7+7^3pmod{7^4}.
]
A complete independent residue trace for `k=0,...,6`, listing `(k,(6k+1)a_kmod2401)`, is
`(0,1),(1,2268),(2,706),(3,903),(4,1617),(5,343),(6,1715)`;
their sum equals `350 mod2401`. Thus
[
rac{W_7-7}{7^3}equiv1pmod7.
]
This proves the proposed **universal p^4 strengthening** does not hold; it does not constrain stronger bounds on special prime families.

Additional p^4 residual observers `(W_p-p(-3/p))/p^3 modp`: `p=11 ->2`, `p=13 ->9`, `p=19 ->12`, `p=31 ->22`, `p=373 ->228`; these are finite observations.

## BRC observer and next exact action

Use the existing BRC provenance-preserving residual carrier: labelled coefficient `(p,k,a_k,v_p(a_k))`, operation `sum (6k+1)*a_k`, scalar modulus-p^3 readout, with optional distinct modulus-p^4 residual. The character `(-3/p)` is the tested branch label, not a substitute for ordered coefficient provenance. Reuse resolution: **COMPOSE_APPLIED** (existing signed/valuation observer), no new BRC tool family.

Next scientific unit: seek a parameter-deformed finite WZ / creative-microscoping certificate for the **original signed 216 sum** whose specialization yields `p(-3/p) mod p^3`; compare the `p≡1` branch to the frozen `Delta_p-R_p=(W_p-p)/p^2` identity, while the `p≡2` branch is kept source-distinct and outside the original accepted frozen target. Test any proposed exact certificate at `p=7,11,19,373`; `p=7` rejects a false universal p^4 upgrade.

Native Source: original target_request_id `onhour11-20261106-1400-exact-research-lane-continuation`; this run's receipt read failed with `BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false`. Site at 2026-11-07T01:02Z: `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. Native session/CLAIM/run and Result **NOT_VERIFIED**; `REGISTER_PENDING / SYNC_DEBT`. Exact Source continuation and old request receipt still require the dedicated Site-bound client/version/credential approval. The original p373 native H0/B0/Frobenius/κ independent experiment remains separately tracked in #1559, **NOT EXECUTED**. No scheduler or notification settings were changed.
