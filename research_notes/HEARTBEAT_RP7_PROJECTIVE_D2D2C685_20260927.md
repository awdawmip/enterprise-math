# RP7: executed projective sharing, a line-cover obstruction, and a local subspace certificate

Progress-Event-ID: RP7-C971348E-D2D2C685
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: e133955493b680940a46d1795bfb059cee145f00
EM control intake: a99ad446f853f0103ca763459de007a13680ba76
Publication preflight: c3da1bfbe93f127c514f3fd22e4c2b125962e37b
Scientific parent: 4c5707594ae41d184cbb3374b0fb19d43e09f27b (RP6)
Scientific commit: d2d2c685a89598e2c729885ae1bd921a2d328d1b

This portable author note does not assert a formal Task/Result, independent review, Foundation promotion or parent-objective closure. The preceding chat RP7 was a symbolic draft only. This turn implemented it and continued to finite line/subspace certificates. P000 is unchanged. Actual b12 BRC gates, 61 complete signed internal modes, exact dyadic exponents, work labels, temporal feedback and original nonterminal Q_K boundaries are retained. There is no new classical phase/reference calculation, raised bank precision, or known-order/factor tuning. All3082 parent Git-tracked files and2251 inherited compact-runtime files remain byte-identical.

## 1. Executed projector and its scope

At each nonterminal child, run the original Q_K first, with K16. Fit at most eight candidate directions from complete rows in ascending work-label order, using the declared exact Gram threshold; freeze the dictionary before assigning rows. Fits use the full current field, not the private latent trajectory or query request order. Failed matches remain exact escape rows; no nonzero input work label is deliberately deleted. Direction selection/scoring/storage are charged.

For row r and nonzero direction f let R=Q(r), kappa=Q(f), j=J(f,r), c=j/kappa. Match only if kappa*R-j² <= eta²*kappa*R. Truncate c toward zero to L15 significant dyadic bits, retaining sign and exact exponent; call it d, with delta=2^(1-L). Store d*f. Exact local identities give:
Q(d*f)<=Q(r);
Q(r-d*f)=Q(r)-j²/kappa+kappa*(c-d)²;
Q(r-d*f)/Q(r)<=sigma²=eta²+(1-eta²)*delta².
The error is also no greater than Q(r)-Q(d*f). Fallback rows have zero added sharing error. Decoded products can require K+L bits; K does not bound all resources.

A complete child has acceptance probability Q(new child)/Q(raw child)<=1. The actual implementation sums complete field masses, chooses the original conditional bit, and rejects the WHOLE attempt if its correction fails. Its surviving law is the specified new raw target divided by its survival Z. This is not a claim of a cheap point oracle. A second packed evaluator applies the actual ordered word once per direction and scales each label while preserving incidence and every Q boundary; the two implementations have the same target.

Set rho=8*2^(1-K), s=t-1. Against the untruncated SAME b12 instrument, TV <= min(1,s*(rho+sigma)); survival Z >= [(1-rho)²*(1-eta²)*(1-delta)²]^s. At t16,K16,L15,eta=2^-14, a rational bound to the exact same-bank reference is45/8192 and a triangle bound to the RP6 K16 reference is75/8192<0.01. These are sufficient bounds, not measured factor success or bank-versus64/ideal error. Empty dictionaries also satisfy them without delivering compression.

Hot Q/J use the unchanged inherited signed direct-sum BRC extension. Dedicated local and orthogonal-projection witnesses separately run the original positive BRC norm observer. No new positive graph per every hot score is claimed.

## 2. Full finite checks and actual performance

The frozen primary plan uses N21/a2/t6 and N33/a5/t6, eta1/16384 and1/256, K16/L15, budget8. Four normalized target laws contain256 terminal probabilities,504 full/packed transition comparisons and24192 complete-carrier row checks. Each eta pair happens to yield the same law at that input. There are zero angular changes; the N21 full tree has two coefficient-only changes and N33 has three. TV to the K16 baseline is1.0589608072384344e-5 and5.142400348200831e-6; TV to the exact same-bank reference is6.14919030639507e-6 and5.055045776915892e-6. Exact fractions, raw fields and all correction certificates are retained. These reduced t6 cases do not establish general compressibility.

Safety includes3213 scalar-rounding checks,13 named input/sign/exponent/dictionary/exhaustion checks,12 actual-gate linearity checks, and four selected local norm/polarization witness records. The existing operator bank was actually constructed/verified; an observed development build took4.164s and1233 core calls, excluded from the hot timings.

New primary benchmark cases143/221/253,a2,t16,K16, eight seeds each, base202609271000000+case_index*10000+j. Three rotated/reversed method repetitions:216 executions and24 distinct case/seed pairs. Median seconds per eight outputs:

|N|Inherited no-prune baseline|New projected full-field|New projected packed|
|---|---:|---:|---:|
|143|0.797269095|1.167197655|1.309135976|
|221|0.236085068|0.305269582|0.317880250|
|253|4.211211180|4.911919450|5.342190528|

All new-target full/packed records match exactly, including attempts, events, random requests and RNG state, across all repetitions. N143 andN253 also match the common baseline scientific/random trace. N221 has60 coefficient-only changes and three different baseline trajectories (seed indices2,4,7); the baseline comparison is NOT wholly pathwise paired. Every primary case has zero changes of direction under the implemented dictionary. Equal factor counts2/3/3 per eight outputs are not exact success probabilities. The new implementations are slower in all three cases; none replaces the faster path.

Timers include program/engine setup, dictionary construction, scoring/certification, all attempts, factor verification and event collection. Bank construction/imports, comparisons, result encoding and I/O are excluded. No cold-process or time-to-verified-factor advantage, nor ranking against every earlier optimized implementation, is claimed. Per first repetition total input labels/directions are1680/1552,455/327,4904/4346; fitting-plus-assignment pairing counts are12590,1357,36577. Repetitions are not independent mathematical samples.

The early commentary that all three cases had no changed rows was corrected after the full N221 tape audit. The overly strong baseline trace assertion and a local rank7 result-assembly NameError are preserved in evidence. Complete corrected local checks reran; engine.py and run.py remained frozen after primary timing.

## 3. New pairwise obstruction to arbitrary one-direction sharing

For two nonzero rows x,y, if each can approximate some scalar multiple of the SAME arbitrary direction with relative norm error at most eta, eta²<1/2, then:
J(x,y)² >= (1-2eta²)² Q(x)Q(y).
Choose signs so their normalized components along that direction agree; Cauchy-Schwarz on the orthogonal residuals gives the bound1-2eta². No trigonometric numerical input is used. Its strict contrapositive excludes even an optimally chosen common direction, not only the implemented dictionary. A pairwise-incompatible clique of q rows therefore needs at least q separate lines at this pointwise tolerance. This is not a lower bound on every task observable or a multi-vector subspace.

A predeclared follow-on examines the first two stored baseline sample paths of N143 andN253:60 layers and34252 exact complete-row Gram pairs. It preserves all fields and pair gaps. The deterministic maximum strict-clique records are:
- N143, history(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0):30 labels,30 exact rays, clique sizes30/18/4 at eta1/16384,1/256,1/16.
- N253, history(1,0,0,1,1,0,1):55 labels,55 exact rays, clique sizes55/55/21 at those thresholds.
Thus the latter checkpoint cannot be represented by fewer than55 one-dimensional families under uniform eta2^-14, regardless of representative fitting. These are actual selected recorded prefixes, not a probability-mass or whole-program lower bound.

## 4. Several shared basis vectors behave differently

For an orthogonal full-mode basis f_1,...,f_d define c_i=J(r,f_i)/Q(f_i), truncate each coefficient inward to d_i, and z=sum d_i f_i. If projection residual Eperp<=eta²Q(r), then:
Q(z)<=Q(r);
Q(r-z)=Eperp+sum Q(f_i)*(c_i-d_i)²
       <=[eta²+(1-eta²)*delta²]Q(r).
Again the error does not exceed norm loss. Orthogonality removes cross-terms, so this bound has no extra basis-rank factor. This extends the symbolic sampling contract when all rows pass or escape exactly; it is NOT an executed multibasis full sampler.

Using exact inherited BRC Gram pairings, fraction-free orthogonalization and verified integer rescaling, at most eight directions were constructed on the two deterministic records above. Pivots maximize relative residual with ascending-label ties. Basis construction is charged, not treated as free. These are61-mode algebraic directions, not new native spatial axes.

N253's55 rows admit a seven-dimensional subspace with maximum relative squared projection residual1.8820304673805516e-9 < 2^-28. N143 still has7.759713502783459e-9 > 2^-28 at rank8; no strict rank<=8 sufficiency is claimed there.

The N253 rank7/L15 projection was then ACTUALLY executed on all55 complete rows with exponents, and through the next original BRC observation. Every row passes the exact error/norm-loss/nonzero tests. Maximum relative squared TOTAL error is3.48311802251093e-9; total squared-norm ratio is0.9999595892801146; the absolute next-bit p0 difference is2.0213475712855497e-8. Full exact coefficients, Gram entries, fields and probabilities are retained.

This is not yet useful memory compression. Basis integers reach143 bits; decoded projected rows reach176 bits. Under one sign bit plus abs(bit_length) per stored integer, even zero, counting exponents:
original field10502 bits;
basis8665 bits;
coefficients/exponents8493 bits;
compressed total17158 bits.
Labels, Python objects, headers and certificates are excluded on both sides. Although raw vector/coefficient slots fall3355 to812, bit payload INCREASES. No multibasis end-to-end speed or success claim is made.

## 5. Source integrity, runtime evidence and actual Drive roundtrip

Original vendor: bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26.
The RP6 runtime ZIP was hash-verified before extraction. Local Git ancestry was independently recovered from the verified RP5 full bundle plus RP6 delta; no remote container Git transport was used. Parent3082 Git files and2251 runtime pins are unchanged. New scientific files:73, comprising72 manifest entries and the manifest itself. Timed sources engine.py/run.py are separately pinned and unchanged.

The final main-process core snapshot contains256973 records. Earlier snapshots are cumulative prefixes, NOT additive independent executions. Local, independent-extraction and cloud-extraction smoke each separately constructs the bank and uses3004 actual core calls.

Standalone compact ZIP BRC_RidgePrecision_RP7_RUN_20260927.zip:
30843376 bytes; SHA2565468c3c54f165ab50a9be65514e757775cd77120c0291b28e8a2654f0b74a6d8;2324 payload files. It runs without a parent bundle but does not include complete historical Git/large evidence. Entry START_HERE_RP7.md.
Delta BRC_RidgePrecision_RP7_20260927_delta.bundle:
2495201 bytes; SHA2561bce02447a5c994c55a574823c6573089750ca24acc5b19fb9039fafe520a043. Requires RP6 parent4c570759, NOT standalone. No new full-history bundle is claimed.

Drive root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP; folder1CvNS9oJGvxzcX6_nn9z3gxZJ4sHmpwtM (RP7_共享方向与子空间证书_20260927_d2d2c685).
ZIP file1ZHd3W4rpx-zEhP99yRLQFMR1rjQafaPc was uploaded, metadata-read, downloaded, fully size/hash checked and extracted to a NEW directory. All2251 parent pins/72 new hashes passed, then actual smoke recomputed the full21/t6 strict law and transition-row certificates, replayed143/t16 full/packed attempts/tape/RNG, and reproduced every coefficient/error/next-bit result for the55-row rank7 checkpoint. These are author recovery checks, not independent scientific replication.
Delta file1NkX13R67OLtCeJLdDYLmMt21x71eaLif was uploaded, downloaded, size/hash checked and git-bundle verified; no additional delta-chain smoke is claimed.
Readable report1kVv2g-ElrGR7YU0G33MvvTWOlnNx3c5G, proof1igturL5Um8y93YPXsOVjLcmNgeJCMLtQ, results1hAaZkQ-9oBq62uAAdzKahmPb37MApTia and entry16uQH4OMpyvvPB53nbTCuhJkxMuY4WAgN were uploaded and folder metadata read back; their full bytes are covered by the downloaded ZIP. No permissions or schedule changes; no bearer URLs stored. The final delivery receipt is outside the package to avoid self-hash recursion.

## 6. Control, antecedents and precise continuation

Same logical conversation: chat-stage101-c971348e64294a5882dfc50fcc8217f1. Recovery2537 succeeded only as local pointer read; source_authority_verified=false and no runs/claims/staging. PRE_FINAL2538 returned REJECTED/PREREQUISITE_NOT_SUCCEEDED, request_sha256041fb6a495f32acff99e892b3d2f11a8904dc5eb62cdb6e52455ba818baedc22. No new identity, RA, CLAIM, formal run/Result, independent admission or final_allowed is asserted. Persistence and cloud byte checks are distinct from native authorization.

Primary abstracts checked: BGL arXiv2112.08499 and Yan et al.arXiv2507.04335. Projection, orthogonalization and similar-structure replacement are not claimed as worldwide novelty; no full-text novelty-completeness review was performed.

Completed units not to repeat as discovery: prior single-ray draft now implemented, four complete target laws, frozen216 executions, corrected baseline pairing audit,60-layer Gram census, selected orthogonal subspace certificates, actual55-row projection/next-bit check, and cloud recovery.
Next: a short NONORTHOGONAL basis with an explicit BRC Gram metric, conditioning-aware coefficient approximation and certified norm/error handling. Do not hide large coefficients or fitting/incidence costs, or treat a one-checkpoint7-dimensional certificate as a complete low-cost sampler. General cheap query complexity, useful-ridge location, polynomial classical Shor and hardware/physics advantages remain unestablished.
