# R5: local ray compatibility, exposed-face lift, and a four-dimensional global separator

Date 2026-11-01. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is an auxiliary finite two-law stopping-process result, not a native X6 proof and not a solution to the original four-observer mother problem.

## Frozen provenance

GLOBAL_KNOWLEDGE_V1 canonical main @ 80dd2098421b56b9f31183b6fa53fb9144fcec82: read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, Enterprise Math project router, P000_STARTUP.json, original P000_REALITY_FOUNDATION.json, ACTIVE worldview; original P000 blob = projection's canonical_blob_sha1 = 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Enterprise Math main @ a673d9c9852957727a17317b223423451f48f6a1: AGENTS.md, current autonomous and portable research protocols. Previous PR #1663 author-side source: 2ff5a2afc12b5876d5e68e1a4ba99fe10b4565c8 and its RESEARCH/NEXT_TASK in research_notes/brc_r5_two_merger_source_sensitive_20261101_t0942. P000 and worldview unchanged. Native status research_authority_granted=false, executor_binding_configured=false, active quota=5/5; bounded owner query returned CONTROL_QUOTA, so no verified current active owner/CLAIM/Result/review.

## Theorem 1 — exact fixed-upstream, all-real local compatibility classification

In a finite acyclic stopping process, fix one last shared LR decision key k, its finite incoming full-history labels h, the upstream reaching weights under both P and Q, and every other policy decision. Assume fresh conditional action randomization and that k is not revisited within a trajectory. Let D_h in R^d denote the entire weighted observation-vector difference for CONTINUE versus STOP at h, including the source-tagged P/Q masses and all downstream consequences. FULL chooses independent continuation probabilities a_h in [0,1], LR one shared a in [0,1]. Then their actual observation images restricted to this fiber are exactly

    K_FULL = O_0 + sum_h [0,D_h],
    K_LR   = O_0 + [0,sum_h D_h].

For every real signed objective w in R^d, the support gap is

    G(w) = sum_h max(0,w·D_h) - max(0,sum_h w·D_h) >= 0.

G(w)=0 for every real w if and only if all nonzero D_h lie on a common nonnegative ray; the all-zero and one-nonzero cases count as compatible. If compatible, the actual real behavioral images, not only the convex hulls, coincide within the frozen fiber.

Proof: Independent FULL actions trace the Minkowski sum of segments; common LR action traces one segment. Support functions of Minkowski sums add. If D_h=lambda_h v, lambda_h>=0, both sets are the same segment [O_0,O_0+(sum lambda_h)v]. Conversely, two nonzero vectors that are not positively collinear admit a linear functional w taking strictly opposite signs: solve prescribed values on two linearly independent vectors, or choose a sign on a common line for opposite vectors. Then the sum of positive w·D_h exceeds max(0,sum w·D_h), a contradiction. QED.

This condition is frozen-upstream/frozen-suffix, not global. In particular changing upstream actions can change the reaching weights, and local compatibility is not global convex-hull equality. A source-aggregated Q/P mass is insufficient to infer fine-port predictive lumpability.

## Theorem 2 — exact common exposed-face lift

Let E_FULL and E_LR be finite deterministic-policy observation vectors in R^d, with K_LR=conv E_LR contained in K_FULL=conv E_FULL (valid for the stated finite acyclic no-repeated-key model by multi-affinity). Suppose rational covectors a,w have a common exposed maximum

    M=max_{E_FULL} a·v=max_{E_LR} a·v.

Set F_LR={v in E_LR:a·v=M}. Suppose a FULL deterministic witness v* has a·v*=M and g=w·v* - max_{F_LR}w·v>0. Let delta=min_{E_LR\F_LR}(M-a·v)>0 when off-face LR vertices exist, and B=max_{E_LR}w·v - min_{E_LR}w·v. Every rational epsilon>0 with epsilon B<delta yields

    h_FULL(a+epsilon w)-h_LR(a+epsilon w) >= epsilon g>0.

If no off-face LR vertex exists or B=0, any positive epsilon works.

Proof: An off-face LR vertex loses at least delta on a, while its w-gain over any on-face LR vertex is no more than B; hence epsilon B<delta keeps all LR maximizers on F_LR. Their support is M+epsilon max_{F_LR} w·v. The FULL witness attains M+epsilon(max_{F_LR}w·v+g), proving the bound. QED.

The practical upstream-exposure obligation is therefore a common face of the COMPLETE full-model and LR-model polytopes, not a face of a fixed upstream submodel. The researcher must check every LR alternative on that face; a local sign defect alone need not survive global upstream re-optimization. Repeated-key non-multi-affine models require a different margin argument.

## Complete exact counterexample: last collision lossless, global convex hulls different

Nature chooses hidden S=A,B, each prior 1/2 under both P and Q. At t=1 FULL can condition on S; LR only observes (time, exact full labelled-path likelihood ratio)=(1,1). Stopping yields binary response 0 at time 1. Continuing draws a binary U, with

    source     P(low|S)    Q(low|S)    t=3 LR(low)    t=3 LR(high)
    A          1/8         1/4         1/2            7/6
    B          1/4         1/2         1/2            3/2

All kernels are strictly positive. At t=3 STOP yields response 0, time 3; CONTINUE gives terminal t=4 and categorical W=(0,alpha,beta), with binary response 0 for W=0 and 1 otherwise. The strictly positive conditional distributions are:

    S,U        P(W=0,alpha,beta)       Q(W=0,alpha,beta)
    A,low      (1/2,1/3,1/6)           (1/2,1/3,1/6)
    B,low      (1/2,1/6,1/3)           (1/2,1/6,1/3)
    A,high     (1/4,3/8,3/8)           (3/4,1/8,1/8)
    B,high     (3/4,1/8,1/8)           (1/4,3/8,3/8)

FULL keys (cA,cB,lA,hA,lB,hB); LR keys (c,l,hA,hB), with c at time 1 and l shared for both low-labelled histories at t=3. No key is revisited along a path. Observation is O=(eP,eQ,TP,TQ), where eP=P(binary response 1), eQ=Q(binary response 0), and T is expected stopping time under its own law.

At the late shared low key, the weighted continue-minus-stop vectors are

    D_A=(1/32,-1/16,1/16,1/8),
    D_B=(1/16,-1/8,1/8,1/4)=2D_A.

For any real FULL cA,cB,lA,lB in [0,1] and arbitrary other actions, set

    l=(cA*lA + 2*cB*lB)/(cA+2*cB)

when denominator>0, else l=0. Substituting the single shared low action l for lA,lB leaves all FOUR observer coordinates EXACTLY unchanged. Yet fine terminal distribution at this low key differs between A and B (e.g. alpha probabilities 1/3 versus 1/6 under both P and Q). The quotient is safe for these four observers, NOT for an observer retaining alpha/beta port identity.

Despite this local repair, the global four-observer hulls differ. In J=5eP-TP the baseline immediate-stop value is -1. Continuing source A at time 1 costs -1 in P-time and permits positive terminal increments 3/32 (low) and 77/64 (high), net 19/64. Continuing B costs -1 and its best increments are 3/16 (low) and 3/32 (high), net -46/64. FULL chooses source A only:

    max_FULL J = -45/64.

LR must continue A and B together at time 1: with all terminal keys optimized its maximum gain after the shared first action is -2 + 101/64 = -27/64<0, so LR instead stops at time 1:

    max_LR J = -1;  gap = 19/64 > 0.

FULL policy (1,0,1,1,0,0) yields O=(23/64,27/32,5/2,5/2). Its L-infinity distance from the LR convex hull is at least (19/64)/(5+1)=19/384.

LR has full affine rank four. The five deterministic LR policies (c,l,hA,hB) 0000,1000,1001,1010,1100 have, respectively, observer rows:

    (0,1,1,1)
    (0,1,3,3)
    (3/32,13/16,27/8,13/4)
    (21/64,29/32,55/16,27/8)
    (3/32,13/16,51/16,27/8)

The determinant of the last four vectors minus the first is exactly 135/4096 != 0. Thus LAST-KEY LOCAL RAY + NONLUMPABLE FINE PORTS + LR RANK4 does NOT imply global hull equality: an earlier LR source collision contains the obstruction.

## Evidence, BRC typing, scope, next question

The accompanying standalone Python Fraction verifier was actually run locally with final marker PASS_EXACT_R5_LAST_COLLISION_RAY_NOT_GLOBAL_HULL. It checks strict positivity and P/Q normalizations, exact time/LR keys, unequal fine W ports, exact low ray, all 64 deterministic FULL local repairs, all 16 LR and 64 FULL support values, full witness, and rank-four determinant. The all-real geometric theorems have analytic proofs above; enumeration is a complete finite-model check only, not an extrapolation to all topologies. No Lean check, external novelty search, independence review, native X6 embedding, or physical experiment is claimed.

BRC interface: preserve the positive source-labelled serial/alternative P/Q path-flow carrier (S,U,W,law,time,branch), and only then project to (eP,eQ,TP,TQ). The signed difference D and signed objective J operate on the observer side; they are not positive mass or a new BRC primitive. The alpha/beta residual demonstrates why provenance must be retained for finer future observers.

Next: classify earliest-key exposed faces after last-key repairs in a two-merger model. Find complete all-signed rational FULL->LR convex certificates (at most five LR vertices per FULL vertex) for a full-rank candidate, or a rigorous signed separator. Only after global convex-hull equality test real behavioral image nonmembership. Mother problem OPEN.
