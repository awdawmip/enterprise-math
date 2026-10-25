# D25/LIFT — original W: sharp p³ stopping ranks and sign-class scan to 100,000

**2026-10-26 · TASK_RESEARCH portable author evidence · UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_BENCHMARK / SOURCE_CHECKPOINT_PENDING.** Logical conversation: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance, not the distinct chatgpt-research-hourly-enterprise-math-20260923).

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged**.

## Exact original summand, not a replacement benchmark

For every prime p>3, define the originally frozen weighted value

\[
W_p=\sum_{n=0}^{p-1}(6n+1)A_n,\qquad
A_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=\frac{(2n)!(3n)!}{216^n(n!)^5}
=\frac{\binom{2n}n^2\binom{3n}n}{216^n}.
\]

The rational equalities are exact. This note **consumes, without re-credit**, the original source-alignment certificate 2037e50b362a0b92e61d4250dcb1593e58899ea8: for D25 target p≡13,19 mod24, the frozen native observer satisfies Delta_p−R_p^(Source) ≡ (W_p−p)/p² modulo p, subject to already accepted CM0 and UR. That source alignment is an equivalence, **not** a proof of vanishing. It also consumes previous portable sign-class code 28d5bc565f0f00db4c71e312b7676eef1fb929eb (finite scan through 5,000); those earlier results are not claimed new.

## New theorem: all-prime sharp rank cutoff, both mod-6 branches

For 0≤n<p, all denominators of A_n are p-units. The three numerator arithmetic progressions (2k+1),(3k+1),(3k+2), indexed 0≤k<n, each hit a p-multiple **at most once**, since each step is invertible modulo p and n<p. Therefore their three first-hit indicators give the exact p-adic valuation:

If p=6m+1, the first-hit indices in the order (2k+1),(3k+1),(3k+2) are (3m,2m,4m). Thus

\[
\boxed{v_p(A_n)=\mathbf1_{n\ge2m+1}+\mathbf1_{n\ge3m+1}+\mathbf1_{n\ge4m+1}.}
\]

Consequently A_n≡0 mod p³ for n≥4m+1. The **last surviving weighted term** n=4m has valuation exactly 2 because (6n+1)=4p−3 is a p-unit.

If p=6m+5, the first-hit indices are (3m+2,4m+3,2m+1). Thus

\[
\boxed{v_p(A_n)=\mathbf1_{n\ge2m+2}+\mathbf1_{n\ge3m+3}+\mathbf1_{n\ge4m+4}.}
\]

Consequently A_n≡0 mod p³ for n≥4m+4. The **last surviving weighted term** n=4m+3 has valuation exactly 2 because (6n+1)=4p−1 is a p-unit. These assertions hold for all p≥5 (including m=0, p=5). Proof: the first-hit index computation plus p-unit denominators proves the valuation formula; the final rank/weight computation proves termwise sharpness. No observed supercongruence or unproved CM assumption enters the proof.

This licenses a *separately declared* exact precision shortening, but the scanner below still computes **the full original n=0,...,p−1 series** to avoid redefining the frozen benchmark.

## New exact finite evidence (not an all-prime LIFT proof)

Direct integer-only original Pochhammer recurrence scan, all primes 5≤p≤100,000, modulus p³:

\[
\boxed{W_p\stackrel{\rm observed}{\equiv} p\,\chi_{-3}(p)\pmod{p^3},\quad
\chi_{-3}(p)=+1\ \text{for}\ p\equiv1\pmod6,\quad
-1\ \text{for}\ p\equiv5\pmod6.}
\]

All **9,590 primes** passed, zero mismatches: 4,784 in class 1 mod6, 4,806 in class 5 mod6. There are 8,923 tested primes *above* the earlier 5,000 bound (the previously tested 19,963 is not a new first observation). Max checked prime 99,991. Residue-class counts p mod24: 1→1181, 5→1206, 7→1205, 11→1203, 13→1193, 17→1203, 19→1205, 23→1194.

Witnesses: p=5: W≡120=−5 (mod125); p=7:7; p=11:1320=−11 (mod1331); p=13:13; p=19:19; p=101:1030200=−101 (mod101³); p=19,963:19,963; p=99,991:99,991 (respective mod p³). Already p=5 **refutes the naive extension** W_p≡+p to all primes, not the actual D25 inert-class statement.

Two distinct executed algorithms: adjacent-term recurrence in C++ and exact factorial expression independently in Python (not using the recurrence). Factorial crosschecks PASS for p=5,7,11,13,19,37,101,1009,19963,99991; direct independent exact rational arithmetic also matched p=5,7,11,13. The 9,590-row deterministic CSV has SHA-256 ea9f2c43e9e741fd79a2485117c71df0217eb0d1242874e2d6f49668ead21ab2; stdout SHA-256 a75d2a5533afc3641a6f05c9f782a11fe21f79f5ffecb413b336d8c8f2df259f.

Companion full re-executable original scan: research_notes/portable_direct/20261026_onhour_d25_original_W_sign_100k_scan.cpp (commit 4fff3b6948710e20fbe5cefc8e88143e6c6c4f17).
Independent factorial crosscheck: research_notes/portable_direct/20261026_onhour_d25_original_W_sign_factorial_crosscheck.py (commit 17761e51e38d54da60db5b675fcca1c33ad58635).
This computation is an **exact finite numeric certificate** and falsifier, NOT a proof for all primes or independent review. Literature novelty is NOT established.

## BRC / mathematical observer type and safe quotient

**COMPOSE_APPLIED:** retain for every original rank the tuple (n; first-hit branch indicators for 1/2,1/3,2/3; weighted residue (6n+1)A_n mod p³), as well as p and p-local arithmetic provenance. Rank update n→n+1 propagates valuation and residue before weighted finite sum. The valuation indicators alone suffice to decide which terms can be removed modulo p³, **but do not preserve signed residue cancellation**; dropping the residue or quotienting directly to positive total mass loses the original observer. This is p-adic auxiliary mathematics, **not** native Enterprise X6 geometry, and makes no P000-worldview change.

## Exact recovery and unresolved native obligations

Authenticated onhour-lane own recovery request research-onhour-20261026-0701-recovery-v1 (GitHub bridge Issue #6467) returned ACTIVE Researcher service session MCP-de3e5bafb24f43f4a5e6285e7601676a, pending=[], runs=[], unopened_claims=[], unpublished_uploads=[], has_more=false, execution_authorized=false, source_authority_verified=false. This projection is NOT Source ownership. Historic independent three-file UR staging was preserved as a neutral immutable archive in the old session; #6468 confirms successful original preservation (3 files, 11,301 UTF-8 bytes, source commit 1696ffd389976f17fee942e905d466e8e92c0148), #6471 + #6474 read both immutable manifest pages to completion and verified SHA256 1c872ed766a761e11d99fac7aa73f228b4f49b90dd14e04172468e079b199381. Archive disposition SD-d7c23e7984c2ddaac60a preserves prior source, is NOT task input or native Source checkpoint, and is not merged into accepted UR Result.

Direct read-only Sites continuation returned CONTROL_QUOTA. Separate original ordinary-bridge continuation request research-onhour-20261026-0701-d25-continuation-v1, Issue #6469, has **adapter_status=REJECTED, bridge_receipt=null, error=PREREQUISITE_NOT_SUCCEEDED**; no native continuation result is implied. This is not NO_DISPATCH and is not permission to copy the active separate hourly Researcher identity. Control support #1558 concerns the independently known checkpoint-claimant/predecessor mismatch, while the specific onhour bridge prerequisite is an additional bounded diagnostic. Never replay an unknown mutation. **No onhour CLAIM/open/run/Source checkpoint/Result/independent review has been established this turn.**

Mother goal OPEN: original native H0/B0, divided-power [X]U mod p², kappa, Frobenius direction/normalization and independent review still require native evidence with frozen inputs and genuine execution authority. The full 100k scalar scan is NOT a substitute. Next smallest scientific action: derive an actual signed/endpoint-faithful proof (or a falsifier) for the stronger observed pχ(-3) relation while retaining the frozen D25 Delta_p−R_p target and original finite cutoff; next authorization-dependent action: repair/reconcile the exact onhour continuation prerequisite, win own claim and open, execute original native benchmark, publish Source checkpoint with immutable readback. This GitHub artifact is **author-side portable evidence only**. Existing research automation frequency, phase, enabled status and notifications unchanged.
