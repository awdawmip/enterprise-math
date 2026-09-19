# BRC-Shor: first-window wheel counting, negative-certificate reuse, and Drive handoff

Event-ID: brc-shor-wheel-first-window-20260919-6EF011
Researcher-ID: EM-DIRECT-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE; elementary derivations and same-author checks, not independent review, Lean, Working Truth or Foundation admission.
Source read: enterprise-math@a06a465e3bd932981794feb60c8a7aa937ca72f6. Prior frontier: BRC_SHOR_SCHEDULE_PRIMARY_LIFT_20260919_6EF011.md at e6a634ed40dc6cc3d2abf8645db77331d5bfd208. Inherited local reproducer commit b732a51c2efac420dedbfb47f8c7fd08b2e3a5e3.

## Proved observation contract

Retain original N,a and the inherited known-factored saturated exponent M. Put b=a^M and s=ord_N(b). Saturation proves that s is coprime to the selected small primes; no factor/order oracle supplies this promise. The exact inherited restoration returns ord_N(a) from exact s and the retained original input. This continuation fixes the primary threshold at31 and adapts only the wheel and search width, not an optimal arbitrary prime mask.

For a wheel W formed from selected primes, define

K^W_Q = Q + 2 sum_{1<=d<Q,gcd(d,W)=1} (Q-d)[b^d=1 mod N].

Under gcd(s,W)=1, K^W_Q=Q iff Q<=s: before s there is no positive return; after s the term d=s survives with positive weight. At the first detecting dyadic Q, Q/2<=s<Q, so s is the only positive returning difference. Thus K^W_Q=K_Q=3Q-2s and s=(3Q-K^W_Q)/2. The filter preserves this terminal collision observer, not arbitrary later-window K or Fourier probabilities. Counterexample: N11,b3,s5,W6,Q16 gives full K52 but filtered K38. Without the coprime promise, order6 and wheel2 lose every positive return.

If the same b has no return through H, then H<s. A baby prefix 0<=j<B with B<=H+1<=s is injective: equal powers at distinct indices would give a return with smaller exponent. Therefore the old residue-keyed count/first-moment carrier safely specializes to residue->j for this prefix. This is a proved singleton fiber, not unlicensed loss of multiplicity.

For B=kW, write d=iB-j, 0<=j<B. Then gcd(d,W)=gcd(j,W). Store only permitted baby exponents j, match b^(iB) against their powers, and add Q-d only for H<d<Q. A previously empty dyadic window makes the old prefix contribution exactly zero; only the new shell is needed. If W grows by divisibility while b stays fixed, filter and extend the existing table without recalculating retained powers. Gap powering avoids generating every skipped exponent. A first-hit variant returns the same exact order without computing the intermediate mass.

The leading cold work proxy is k*phi(W)+Q/(kW). Construction of the wheel, powering gaps, old-table scans, dictionaries and restoration are charged. The planner searches a small specified set, not all widths or prime subsets. W is capped at2310, so the shipped code has only finite-factor savings, not a new asymptotic o(sqrt(s)) guarantee. The budget bounds baby entries at65536 and giant queries per stage at twice that; equal entry caps are not equal byte budgets.

## Negative evidence cannot be copied across a changed base

If ord(b)>H and the base becomes b^E, then ord(b^E)=ord(b)/gcd(ord(b),E)>H/E. Only floor(H/E) is a generally valid inherited no-return bound. Example: modulo11, b2 has order10 and no return through7; b^2=4 has order5. Keeping H7 would skip the answer; H3 is safe. The implemented cache keeps b fixed. More precise transport requires additional certified information; it is not assumed. A separate bounded check covered44850 r,E,H instances.

## Actual BRC reuse and classical prior art

The branch population is ordered modular-power path pairs; positive multiplicities, residue/exponent associations, original input and restoration provenance remain typed. T0 residue-keyed composition is specialized to certified singleton prefixes. P023 fiber-constancy/future-compatibility is COMPOSE_APPLIED to the first-window filter, same-base negative evidence and its failed base-change transfer. The inherited mask and primary restoration code is REUSE_EXECUTED unchanged. This is an application/observer specialization, not a new top-level family; the affine28-entry moment carrier is not an occupancy oracle.

Sutherland, Order Computations in Generic Groups (MIT,2007), Algorithm4.1 already combines a smoothness-removing exponent, coprime baby steps and order restoration; Algorithm4.2 already performs incremental primorial steps. Chapter5's multi-stage sieve addresses changing the smoothness threshold. Primary source: https://math.mit.edu/~drew/sutherland-phd.pdf ; errata: https://math.mit.edu/~drew/ThesisErrata.html . This corrects the potential overstatement that adaptive prime scheduling itself is an unoccupied direction. The local wheel first-hit comparator is not a complete implementation of the optimized Algorithms4.2/5.1. No general-algorithm novelty, polynomial Shor simulation or record is claimed.

## Executed checks and measured limits

PASS:10406 first-window identities,51052 coefficient-shell checks,20612 complete original-order runs,15459 incremental-equivalence runs,1089 larger random unit inputs,19 planner checks,7 invalid-input cases,1 resource failure. The new candidate AST has no float/complex literal, true division or SymPy import. Checks are same-author distinct computational paths, not independent review or full-project/Lean verification.

Frozen comparison:23 inherited selected inputs plus12 new seeded balanced semiprimes around24/32/36/40bits; seed2026091913;6 methods;3 repetitions;fixed primary bound31/cap65536. The55 complete per-process pilot rows are preserved and excluded after transport overhead interrupted that approach. The disclosed amendment uses candidate-only interpreter batches, with reference factoring in a separate postcheck process. Candidate setup, masking, planning, search, restoration and final checking are timed. GC before each run, rotated order, no CPU pinning. Incomplete interrupted rows are not counted.

630 definitive runs:567 exact original-order successes,63 explicit budget exhaustions; all successful outputs pass postchecks and7158 stage checks. On31 successful paired inputs, inherited conditioned collision/new incremental weighted median ratio2.473750, new faster31/slower0. Against inherited conditioned Shanks,16/15 and median1.114758. On12 fresh inputs, collision comparison12/0 and median2.123592; Shanks comparison6/6 and median1.034167. Against cold rebuilt wheel count,32/0 and median1.396303. Against incremental W1,21/10 and median1.302053. Against local wheel first-hit,11/21 and median0.964420. Ratios are medians of per-input median-time ratios, not population guarantees. No stable win over the stronger classical same-output route was established.

Example N1000036000099,a5: original order166672333344, residual157833649. Median milliseconds: old conditioned collision31.484592; old conditioned Shanks12.305924; cold wheel12.815782; incremental wheel8.919520; wheel first-hit8.104052; incremental W1 15.259021. Peak collision entries16384 become9458 in the incremental run. Rough example N6186937,a2 has r=s1545469 and Shanks1.018055ms versus wheel0.868356ms. Counterexamples: fresh N697798516999,a2 gives0.934752 versus0.980259ms; constructed N1002772198720536577,a3 gives0.441689 versus0.572551ms. N1000000016000000063 and N18446743979220271189 exhaust the current budget in all six methods; no general64bit success.

## Verified complete executable handoff

The user explicitly requested Google Drive synchronization. New full standalone Git bundle: BRC_Shor_wheel_20260919.bundle,201315 bytes; HEAD121213c2e507d0ebc59d3082c729e826b7263939, descended from the prior reproducer. This is not the complete enterprise-math repository. It includes prior executable sources plus this continuation's proof, code, frozen plan, all raw definitive/pilot rows and checks.

Drive file: https://drive.google.com/file/d/1rT8sNly8WpNvQ81FMa_ld640w3lFnnuQ/view
Folder: EnterpriseMath-Handoffs,1IJ8iAXY5laK1lj-Y4NGWKEOdLofieHLa.
SHA256:0593334fc8d9b85065e2cf279f87c7c53b855dcff4b0a5d77dd1a763a771058e.
MD5:afcae00cc7272f9a6bcd76aeea470aa1.

Google_Drive.upload_file returned success; metadata confirmed201315bytes and not-shared status. Google_Drive.fetch returned the complete raw file; runtime-mounted readback was compared byte-for-byte and matched. Git bundle verification, fresh clone/fsck,47 file-hash checks and rerun new tests passed; worktrees clean. No prior blocked GitHub code request was retried. Full code is durable on Drive, not asserted to be committed to the enterprise-math GitHub repository.

## Resume, not rediscover

Preserve the verified observer/lower-bound contracts, explicit failures and calibration. Next nonduplicate unit: implement or reuse a faithful classical multi-stage-sieve reference with typed bound transport, then isolate any BRC-specific additional observable capability under the same original-order output and complete cost accounting. Optimal arbitrary mask selection, cheap unknown-five-position localization and general polynomial classical Shor simulation remain unestablished. Persisted notes and Drive publication do not grant theorem acceptance or close those parent scientific questions.
