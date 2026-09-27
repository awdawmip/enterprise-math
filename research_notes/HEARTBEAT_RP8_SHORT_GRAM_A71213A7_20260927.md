# RP8: short nonorthogonal BRC frames, norm repair and measured payload limits

Progress-Event-ID: RP8-C971348E-A71213A7
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read snapshot: 7a639845946cb5f8edfa22d3d5d0d47a44f6080e
EM intake: 2e81851d62c869a20b47ae083a24dde1a4c0420c
Publication preflight: 88c799356c4d11890625c688ef4fffaeb3e26fb3
Scientific parent: d2d2c685a89598e2c729885ae1bd921a2d328d1b (RP7)
Scientific commit: a71213a79dade92425515c854636a695bfd05d78

This additive portable note is not a formal Task/Result, independent review, Foundation promotion or parent-objective closure. P000 is unchanged. All3155 parent Git files and2324 inherited runtime files remain byte-identical. Actual b12 BRC gates, complete61 signed modes, accurate dyadic exponents, all work-label incidence, temporal feedback and original nonterminal Q_K boundaries are retained. Main K16; coefficient block16 and radial20; final relative compression tolerance theta=1/8192. No new classical phase/reference calculation, raised gate precision or known-order/factor tuning is used.

## 1. Short bases and an explicit Gram metric

Instead of storing the previous143-bit orthogonalized vectors, use selected original16-bit full-mode rows as a nonorthogonal frame B. Obtain G_ij=J(f_i,f_j) through the inherited signed BRC pairing. Positive exact Schur pivots and G*G_inverse=I certify the finite coefficient solve. For complete x, set R=Q(x), b_i=J(f_i,x), c=G_inverse*b. Then

    Eperp=R-b^T c>=0,
    Q(x-Bd)=Eperp+(c-d)^T G(c-d).

The off-diagonal metric terms cannot be erased. Independent inward coefficient rounding has error bound delta^2 sum_ij |G_ij c_i c_j|. The resulting row-dependent cancellation ratio is NOT called a condition number. The improved codec rounds coefficients with a common exact binary exponent WITHIN each label, evaluates the exact quadratic error, and records each label's scale separately. It does not independently normalize rows and erase relative strengths.

A real BRC-norm interface counterexample uses padded f1=(16,0), f2=(16,1), c=(1,-15/16). Original x=(1,-15/16) has Q=481/256. Inward two-bit coefficient rounding gives d=(1,-3/4), y=(4,-3/4), Q=265/16. Thus individual coefficient magnitudes decreasing does not imply whole-row norm contraction.

## 2. Radial correction and sampling theorem

For candidate y=Bd let A=Q(y), j=J(x,y). If A=0 or j<=0, retain x exactly. Otherwise choose lambda*=min(1,j/A); preserve1 exactly or round the smaller value inward to20 significant dyadic bits. Set z=lambda*y. Since lambda*A<=j,

    Q(z)<=Q(x),
    0<=Q(x-z)<=Q(x)-Q(z).

When lambda*<1 it is the exact least-squares projection onto the line of y; the added radial quantization error is at most delta_radial^2 Q(x). Return z ONLY if the full exact error Q(x-z)<=theta^2 Q(x), otherwise escape to x. Passing nonzero rows stay nonzero. Store lambda losslessly as1-deficit, a codec change not an extra approximation. Each coefficient record remains bound to its complete basis.

The deterministic complete child first runs the original Q_K, then this checked frame codec. Fit depends on the complete history field with fixed tie rules, never private walker or request order. The actual new full-field sampler uses the original raw-bit probabilities and the whole-child acceptance ratio Q(new child)/Q(raw child)<=1. Rejection ends the WHOLE attempt. Induction gives the exact surviving raw target and its normalized accepted law. This is an explicitly new approximate target, not the RP6 law, not a cheap point oracle.

Let s=t-1, rho=8*2^(1-K). For theta,rho<1,

    TV(P_RP8,P_exact_same_b12)<=min(1,s*(rho+theta)),
    survival Z>=((1-rho)*(1-theta))^(2s),
    TV(P_RP8,P_RP6_K16)<=min(1,s*(2rho+theta)).

These follow by norm-error accumulation relative to the SAME linear BRC instrument, not an assumed Lipschitz property of the old nonlinear quantizer. At t16,K16,theta1/8192 the two TV bounds are45/8192 and75/8192<.01. Theta is the total NEW compression tolerance, not RP7's angular eta1/16384. Bank-versus64/ideal error is separate. An absolute .01 budget is one percentage point, not99% factoring success. Rank/fitting/query costs are not bounded by these error results.

## 3. Actual local payloads and unfavorable cases

Original checkpoints: N143a2t16 at the alternating01 history of length15 (30rows), and N253a2t16 at history(1,0,0,1,1,0,1) (55rows). Initial32 basis/precision alternatives produced1360 row certificates; a declared common-exponent follow-on added10 alternatives and425 certificates. This is42 alternatives on the SAME85 distinct rows, not1785 independent samples. Twelve-bit shortened orthogonal bases did not meet the tolerance and fell back; failures are retained.

Selected original-pivot/common-exponent16/radial20 results:

|Checkpoint|Rank|Original integer payload|Basis+coefficients|Explicit Gram|Total including Gram|
|---|---:|---:|---:|---:|---:|
|N143,30rows|8|7902bits|5097bits|2198bits|7295bits|
|N253,55rows|7|10502bits|6972bits|1647bits|8619bits|

The basis/coeff splits are2057+3040 and1301+5671. All rows pass theta. Maximum relative squared error is8.552674410011568e-9 and4.009269726667644e-9. N253 has four actual raw coefficient-rounding norm increases, each repaired by lambda. Its final total norm ratio is.9999661607008233 and next-bit p0 difference is1.57559371264155e-6. N143 p0 difference is exactly0 at this observation. Basis integers are at most16bits, but decoded N253 rows still reach52bits.

This payload counts one sign bit plus absolute integer bit length, even for zero, and exact exponents. Explicit Gram rational entries include denominator1. Labels, containers, tags and certificates are excluded on BOTH sides. It is NOT a packed-file or RSS measurement. Gram inverse retained during fitting would add19519bits atN143 and14013bits atN253; peak runtime memory is not proved smaller. Full validation evidence is substantially larger than the encoded scientific state.

Two separately prescribed fresh prefixes also pass but have NO total payload advantage: N209a2t16,h=(1,0,1,1,0,1,0,0),45rows/rank8 gives original8698 versus8756 including Gram; N221a2t16,h=(0,1,1,0,1,0,0,1),3rows/rank3 gives709 versus1035. Their histories are deterministic test inputs, not high-probability sampling claims. Basis compression opportunity is not guaranteed.

## 4. Exact Gram observation and timing with fitting charged

For V=TB from the ACTUAL ordered feedback and H=B^T V, coefficient vectors include exact radial scalars. With actual modular permutation P,

    M=sum_w c_w^T G c_w,
    C=sum_w c_(P w)^T H c_w,
    p0=(M+C)/(2M).

All signed cross-terms and label incidence remain. The new Gram observer exactly matches full decoding of the SAME projected field. Transformed Gram conservation and512 complete raw child rows were checked. A subsequent coordinatewise Q_K can leave the span; no general closed low-rank evolution is claimed.

Seven rotated/reversed repetitions per original checkpoint, three observation methods, give42 observation calls on TWO states. New program setup and TB/H construction are included; bank construction, I/O and result comparison are excluded. Inverse/coefficient/certificate fitting is measured afresh separately; the original RP7 pivot-discovery cost is NOT included. Medians in seconds:

|N|Original full|Projected decoded full|Projected Gram|Fit plus Gram|
|---|---:|---:|---:|---:|
|143|.066151412|.080645396|.070702312|.173655715|
|253|.158452407|.188739757|.155368411|.322129748|

Fit medians alone are.099086321 and.155302937; the last column is the median of per-repeat sums, not a sum of separate medians. The bare metric observer can be cheaper than full decoding, but overall encoding plus observation is slower. There is no new cold-process, until-factor, universal speedup or comparison against every old optimized implementation.

## 5. Complete new laws, sample replay and safety

The frame compressor was integrated after EVERY original nonterminal boundary in a complete-field whole-trial sampler. N21a2t6 andN33a5t6 yield two new full laws,128 terminal probabilities and252 child mass/acceptance identities. Every accepted law is exactly normalized/nonnegative. TV to RP6 K16 is7.571955921213148e-6 and4.488578095778468e-6; TV to untruncated samebank is2.076648478963908e-5 and1.3161956821685512e-5. Surviving-factor probabilities are.287769554500575 and.29082181173991256; corresponding K16 references.28777228400361754 and.29082263637007255. Survival Z is.9999462665009574 and.9999458492473645. These are reduced t6 diagnostic widths, not default-width performance guarantees; exact fractions and full fields are retained.

Four new defaultt16 sample settings (N143/N253, two seeds each, base202609271100000+case_index*10000+j) each replay once: eight executions but only four distinct settings. Complete attempts/certificates/random tape/RNG match. One N253 sample returns verified11 and23; no success-frequency conclusion is drawn and no sampling timing superiority is claimed.

Twelve invalid-input rejections, singular/asymmetric/negative metric controls, signs, exponent-1000, frozen-basis request-order consistency and nonorthogonal norm witnesses pass. The first two safety processes hit45-second tool limits with no complete report; scripts and logs are kept. Early inverse-only timeout attribution was corrected after dense positive-norm witness costs were exposed; no complete per-call profile is claimed. Final positive BRC norm witnesses omit only ZERO GRAPH EDGES, retain coordinate indices/full scientific vectors, and execute the original two-edge BRC observer. This is not deletion of61-mode scientific state. Hot norms/pairings use the unchanged inherited signed direct-sum extension, not one rebuilt positive graph per scalar operation.

Separate retained process core-call counts: local22438, block7874, observation16372, full-target14600, final-safety2629. They are execution receipts, not independent samples. Local, independent-extraction and cloud-extraction smoke separately use5646 core calls each. A packaging draft accidentally indexed10 pyc files; the local unpublished index was rebuilt from RP7. The final scientific diff is exactly90 new authorized files, with3155 parents unchanged; no benchmark evidence or scientific source was removed.

## 6. Artifacts and actual Drive recovery

Entrypoint START_HERE_RP8.md. Independent run ZIP BRC_RidgePrecision_RP8_RUN_20260927.zip:33494271bytes, SHA256c6bd241717b256e36283151dc7a5216c3b440ccec01637fb31bfae819c7f61d3. It has2414 payload files,2324 inherited plus90 new, and runs without a parent bundle; it is NOT the complete historical Git/large-evidence archive. New manifest contains89 hashes plus itself.
Delta BRC_RidgePrecision_RP8_20260927_delta.bundle:2635302bytes, SHA256d0e37cae4f90629c64b576801d0ac3f327f766977554a1b3e3eb58fed8f47888. Requires RP7d2d2c685, NOT standalone. No new full-history bundle is claimed. Local Git ancestry was restored from already hash-verified RP5 full bundle and RP6/RP7 deltas, never remote container Git transport.

Drive root19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP; new folder1kuU8dq9ex7jS199c1_EY6QADOG3Iutqf, RP8_短非正交基与Gram校正_20260927_a71213a7. ZIP file1fm-e34kV8ioCTDHj2uacWV6NHQgOiyKX actually uploaded, metadata read, fully downloaded/hash checked and extracted to a NEW directory. All2324 parent pins and89 new hashes passed, followed by actual smoke: all55 coefficient/Gram/radial/error/p0 certificates, positive BRC norm witness, complete64-probability N21 law with transition fields, and N253 full attempt/tape/RNG/factor replay. Cloud smoke used5646 actual core calls. This is author recovery, not independent scientific replication.

Delta file1DRA46-yOrTa-eUE0QQMED_pUXUcrG5-R was uploaded, downloaded, size/hash checked and git-bundle verified against the parent; no separate delta-chain scientific smoke. Readable report1mzmtOi89j-OQCp2DifIULfIJKUy_gked, proof1nSEy53MccBr0QFnJP2tCf2E0UAi7PJtj, results1TYtpV2HHBWyH3Q283Yhs3WyCaqEv4gfA, entry1f__qGTRA1sLsSjYa8XZlkLNqN0vLNwci uploaded with directory metadata readback; their bytes are covered by the downloaded ZIP manifest. No permissions or schedules changed. Final delivery receipt is separate, with no self-hash recursion or bearer URLs.

Original vendor remains bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py, blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. Primary literature checked only at abstract/metadata level: Yan et al.arXiv2507.04335 and Bravyi-Gosset-Liu2112.08499. No worldwide novelty of Gram projection/compression or full-text prior-art completeness claimed.

## 7. Control and precise next frontier

Same logical conversation chat-stage101-c971348e64294a5882dfc50fcc8217f1, old start stage101-session-c971348e-02. Recovery2539 succeeded only as local pointer read, source_authority_verified=false, no runs/claims/staging. PRE_FINAL2540 actually REJECTED/PREREQUISITE_NOT_SUCCEEDED, request_sha256e9f368f16329074e471e17604b491d722870f106ebf4f05e0d287fe373327365. No new identity, RA, CLAIM, run/Result, final_allowed or independent admission is asserted. Persistence and cloud checks are not native registration.

Completed units not to repeat as discovery: radial Gram compressor proof and executed witness,42 local alternatives, explicit payload/inverse accounting, two extra prefixes, exact Gram observation, seven-repeat local costs, two complete new laws, four sample replays and cloud recovery. Next: reuse/transport the short frame through actual ordered operations, update it only when the original Q boundary produces a certified out-of-span residual, and charge refitting and metric maintenance. Do not treat a one-checkpoint saving as generic small rank, cheap membership, useful-ridge locator, polynomial classical Shor or hardware/physics advantage. Parent research remains open.
