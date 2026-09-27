# RP11-CLOSED: executed common b12 invariant carrier and measured coefficient precision costs

Progress-Event-ID: RP11-CLOSED-C971348E-120A8CD5
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Started: 2026-09-27 Asia/Taipei; recovery/publication crossed to 2026-09-28.
Global read snapshot: 96b9afcb305aaf0f3a5599d5c75115411031b09c
Project control intake: c4dc4719ea3900e60086aa451425a3641d4f47b7
Parent: RP9 standalone run ZIP, 54755655 bytes, SHA256 5462e1f52e3ab7a79aa2bbb231b67efe22bbbf66528985a5f1990b6796ee13bd.
Scientific implementation: rp11_closed/engine.py SHA256 120a8cd500711ac1b6a675e167a87547c6834e3370fe99b04ff0e5347f48430e.
This is the CLOSED implementation, not another dialogue's RP11 residual-channel proof.

## Actual scientific increment

The previously symbolic common-invariant-space route has been executed for the inherited ACTUAL b12 bank through level16. P000, full61 signed internal semantics, exact dyadic exponents, modular work labels, gate order, original factor verifier and operator bank are unchanged. No classical phase, ideal-QFT reference, raised bank precision or known order/factor input was introduced. All2406 RP9 payload files remain byte-identical.

The natural integer basis E=(e0,e1,primitive_tail4,...,primitive_tail14) has rank13, positive BRC Gram G, and maximum basis entry length7 bits. Levels14/15/16 happen to have identical complete z at this bank precision; identities and schedule are retained. The full active coordinate union is0..20 (21 coordinates). The other40 coordinates are exact zeros from the standard initial state even under original coordinate Q16.

For every one of15 actual gates, forward/inverse complete images of13 basis vectors agree with the inherited61-mode action:390 images and5070 Gram equalities. TE=EM_T and M_T^T G M_T=G. T2 e0 supplies e1; each actual T_m e0 for m4..14 supplies its nonzero independent residual tail after subtracting e0/e1 components. Hence13 is the MINIMAL common LINEAR invariant dimension for this full bank and initial e0, not a universal state count or a statement about arbitrary bank precision/control width/nonlinear quantizers. Complete matrices, rank residuals and11 generation witnesses are stored.

The canonical coefficient recurrence never refits rows or calls LDL/inverse in the hot path. Setup still uses and retains small verification factors; no total-memory elimination is claimed. Norm/inner products use the explicitly verified Gram quotient of the inherited signed direct-sum BRC observer.91 dedicated Gram witness requests pass through the original positive BRC path interface, with22 new core graph calls after cache reuse; no graph call per every hot score is claimed.

An actually reachable Q16 counterexample at N21/a2/t8, history(1,0,0), work4 has squared distance outside the13-space
105498504521/67543913720854544908288, relative squared distance
210997009042/368042005824333041099>0.
Thus13-coordinate truncation is a NEW approximate target. The21-coordinate zero-padding quotient is exactly the old Q16 target.

## Precision contracts and finite laws

Adaptive coordinate quantization tries common mantissa caps6,8,...,32, with eta=2^-14 (also eta=2^-8 in diagnostics), exact G error tests and a24-significant-bit inward radial correction. For candidate d, R=c^TGc,A=c^TGd,Y=d^TGd, choose0<alpha<=min(1,A/Y). Only return alpha*d if
0<=R-2alpha*A+alpha^2*Y<=eta^2*R and norm does not increase; otherwise try the next candidate or retain the original coefficient row. No nonzero input label is intentionally erased. Products may reach48 stored bits in these sample paths; eta is not a mantissa-width guarantee.

After the primary negative benchmark, a separately frozen amendment uses one-pass quantization. Set eps=eta/4 and B_G=sum|Gij|=319501. Choose the largest positive integer shift s with B_G*2^(2s)<=eps^2*n^TGn; truncate n toward zero, then multiply by exact1-eps, unless unchanged. This gives relative norm error at most2eps+eps^2<eta and norm contraction without repeated candidate Gram tests. Exact error and decoded-row checks remain. The observed retained peak is43 bits. It is a separately defined target, not an implementation-equivalent optimization of adaptive quantization.

Each row satisfies error or exact fallback, every history is included in the scope, and whole-attempt mass correction is used: rejection restarts the entire trial. Against the untruncated SAME b12 instrument,
TV<=min(1,sum eta_i), Z>=product(1-eta_i)^2.
For t16 and eta2^-14 the triangle bound to the original K16 target is75/16384<1/200. This bounds possible absolute event-probability loss, not99.5% factor success. Bank-versus64/ideal error and work-label/query complexity remain separate.

Complete diagnostics use only (21,2,8),(33,5,8),(77,2,8), below default factorization widths. Main18 laws include representation-equivalent pairs61/13 exact and61/21 K16; one-pass adds3 laws. Total21 normalized laws,5376 terminal entries,10710 branch identities,27935 row quantization certificates. Same-target complete-row comparisons34302. A separate real SparseField parent check covered252 branches and1479 nonzero output rows. These are not21 independent scientific inputs.

For N21/33/77 respectively, exact same-bank factor-event probabilities:
0.3227344752467301 / 0.36372283509018044 / 0.1288089092061766.
Adaptive eta14:
0.3227291424801835 / 0.3637209603348087 / 0.1288090236961834.
Adaptive TVs to exact:
1.2384094144372279e-5 / 8.487528740285645e-6 / 7.2062780151302494e-6.
One-pass TVs:
3.2300067780636897e-5 / 2.347502787195406e-5 / 1.1653546400049665e-5.
All displayed decimals derive from stored exact fractions. No success mask enters state evolution.

## Interleaved benchmarks: no hidden speed claim

Primary cases N143/221/253,a2,t16, eight seeds per case, three methods and three rotated/reversed repetitions:216 executions,24 different case/seed pairs. Median seconds per8 outputs, full61-K16 / active21-K16 / adaptive13-eta14:
143:1.205563068 / 1.012195887 / 2.232124454
221:0.360044662 / 0.324597115 / 0.607641574
253:6.313948588 / 5.740889614 / 9.236052344.
The21 quotient saves9.08%-16.04% on these batches with identical full scientific traces, random requests and RNG. This is zero-coordinate removal, NOT a new precision reduction. Adaptive13 is slower.

Amendment uses12 different NEW case/seed pairs, four per case, same three repetitions:108 executions. Median seconds per4 outputs, active21 / adaptive13 / onepass13:
143:0.550592376 / 1.068346751 / 0.619542063
221:0.148461971 / 0.266275282 / 0.173484944
253:2.950424711 / 4.666214276 / 3.084199021.
One-pass is33.9%-42.0% faster than adaptive13 on these fixed batches, but still4.5%-16.9% slower than active21. New targets can consume different random paths and yield different factor counts; no paired pathwise advantage against21 or expected time-to-factor theorem is claimed.

Timers include per-sample program/engine setup, explicit field traversal, candidate checks, whole-trial corrections, exact postprocessing and event capture. Bank/common-space preparation, comparisons, encoding/I/O excluded. Actual initial bank construction observation6.117922793s and1233 core calls is separate, not a cold benchmark. Not compared with every older suffix/checkpoint optimization; not process RSS or total-memory reduction.324 timed executions represent36 distinct case/seed pairs, not324 independent inputs. All unfavorable observations retained. Timed modules froze before their respective measurements.

## Artifacts, recovery and actual cloud mirror

Standalone archive BRC_RidgePrecision_RP11_CLOSED_RUN_20260927.zip:
79151427 bytes; SHA256 2c262feaff7663023f2723233a50db3c7e1625e0b16b8e0990707722531ce211.
2546 payloads=2406 unchanged parent files+140 new files (139 manifest entries plus manifest).
Entry RP9_Run/rp11_closed/START_HERE.md. Contains full current evidence and parent runtime, not complete Git history. No new full-history bundle or code commit is claimed.

Source workspace, fresh local ZIP extraction and newly downloaded Drive extraction each actually replayed390 gate images/5070Gram entries/minimality,15 named safety checks,48 additional row-budget checks, two complete N21/t8 laws with transition certificates and the first N143 sample for each primary method. Each process used2698 original core calls. Fresh/cloud extraction also checked all2406 parent pins and139 new hashes. This is author recovery, not independent scientific replication. All three full-case laws and every benchmark were NOT repeated in every smoke.

Main process final core count372465; earlier CORE snapshots are cumulative prefixes and must not be summed. Failed development API calls, verifier RNG-adapter error, results-display/assembly errors and the one-pass filename correction are retained; fixed prior to delivery without changing timed scientific modules.

Drive folder1z8hy1SdsOkvTZ2FpM6Oy2d1mYQb0tjNO under root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP.
Runtime file1cJr0qHtNj8ExHa1tMtfirumOiAc9Dfes actually uploaded, metadata-read, downloaded, full size/SHA checked and newly extracted for the smoke above.
Report1ETypEajer2LzjrpVv_E__CEoCfcKhsnS; proof1d5OCgYNiFZKVChcwleNNZPtabrkP9_Kf; results1S2dOeMUHGSRMItYfvVeNa8MMt0_0G11e; bank certificate15DuL_1qUkSk9wRKSJSPfhokDIVd6BT3T; entry1YT4JabOCOtRKBsJH3RXntHqAKvGnvmka. Readable bytes are included in the verified archive. No permissions/schedules changed.

Existing RP8/RP9 attachment-version backups were discovered in folder1hz6_Oc5L2_x_gp7OSGKgcCBz6JZSoRbw, not newly uploaded by this turn. Both were downloaded and fully matched:
RP8 file1W7RlQDmxmreiaFmQB_Y0f22a4xJc-OhB,35840220 bytes,SHA d680a1d633f32df579ee8fa27e3281b6a98d1cb72d82ad36a66ae4ab516d94a0;
RP9 file1h76_iUbDx3uJMfiYODB-4t0z44RDX--c,54755655 bytes,SHA5462e1f52e3ab7a79aa2bbb231b67efe22bbbf66528985a5f1990b6796ee13bd.
Old pending records are preserved as historical facts. No claim that this turn independently reran all old experiments or created those uploads.

Vendor: bc7babbb9e890f6d5a7094430a5fbdccf66c77ad, src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26.
Primary abstracts only: arXiv1406.7069v2 and2112.08499v2. Invariant-subspace reduction, Gram identities and rejection sampling are prior art; no worldwide novelty or transferred complexity claim.

## Control and continuation

Same logical conversation chat-stage101-c971348e64294a5882dfc50fcc8217f1, original start stage101-session-c971348e-02.
Recovery2558 is local-pointer SUCCEEDED only, source_authority_verified=false and no runs/claims/staging.
PRE_FINAL2559 submitted with truthful nonterminal parent liveness; actual result recorded in separate delivery.
No new RA/CLAIM/formal run/Result, independent review or final_allowed is asserted. Publication/backup do not confer native authorization.

Completed: common13 minimality/quotient,21-coordinate exact baseline, actual original-Q16 escape witness, two new coefficient quantizers, complete finite laws, both declared benchmarks and cloud recovery. Do not repeat them as discovery.
Next: reduce the fixed-G certification/bit cost without reinstating per-row fitting, e.g. a short sparse metric coordinate with a proved rounding contract; compare to the actual21-coordinate baseline, including preparation, state bits, labels and time to a verified factor. No general cheap row oracle, polynomial classical Shor or physical/hardware advantage is established. Parent research remains open.
