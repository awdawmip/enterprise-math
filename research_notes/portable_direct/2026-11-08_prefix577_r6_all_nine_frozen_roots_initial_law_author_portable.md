# PREFIX577-R6 — Nine frozen roots share one 79-dimensional symmetry-preserving initial-law polytope; sharp horizons 5/4/3

Date: 2026-11-08 UTC. Evidence: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Neutral author-side mathematical publication, not a Source CLAIM, Result, checkpoint, Driver review or mathematical admission.

Frozen native scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Original native kernel blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41. Exact scope: 96 native original ports, six distinct labeled actions per port, full joint rewards (R1,R2,R3,R4,R5,R6,K), all finite path lengths, and the model's nine explicitly frozen root vectors 0, ±e1, ±e2, ±e3, ±e4. Path length is an ordered action count, not a physical-time calibration.

Predecessor reused, not re-claimed: 51-class full-label row-equitable quotient and rank49 class responses at immutable Git blob 311caef8c2a7f651f29a8248ad21c23458a22e5c. Zero-root initial-law classification and sharp five-step test were already established and preserved in immutable commit 4f276f8b11b75c0a1e4864dd0f0449ca4a88ae0f (blob 8df01c2b210a4785b1baa5fd6ab19bae6eb86f40).

## Theorem 1: root-independent complete invariant initial-law polytope

For every root r in the exact nine-element frozen set and every real probability vector μ on the 96 original ports, the complete seven-variable length-n path-law generating polynomial is invariant under exchanging only R5 and R6 **for all n>=0 if and only if** the same sixteen disjoint native-port block-mass balances hold:

| # | A ports | B ports |
|---:|---|---|
| 1 | 20,21 | 44,45 |
| 2 | 16,17 | 40,41 |
| 3 | 88,89 | 64,65 |
| 4 | 92,93 | 68,69 |
| 5 | 18,19 | 66,67 |
| 6 | 22,23 | 70,71 |
| 7 | 90,91 | 42,43 |
| 8 | 94,95 | 46,47 |
| 9 | 34,35 | 82,83 |
| 10 | 38,39 | 86,87 |
| 11 | 62,63 | 14,15 |
| 12 | 58,59 | 10,11 |
| 13 | 54,55 | 78,79 |
| 14 | 50,51 | 74,75 |
| 15 | 26,27 | 2,3 |
| 16 | 6,7 | 30,31 |

Each balance means sum(μu for u in A) equals sum(μu for u in B). The other 32 ports are individually symmetric. The resulting initial-law polytope for **every one of the nine roots** has affine dimension **79** and exactly **96 extreme points**: 32 single-port Dirac laws and 64 equally weighted cross-block two-port laws. For example, the original native one-port law μ=δ0 preserves the complete swap law at **every path depth for every pinned root**.

## Theorem 2: exact root-dependent minimum finite observation horizon

For each root, all-depth symmetry for any starting probability vector is equivalent to checking every length n=0,...,H(r), with the following **sharp** H:

| Frozen root | Sharp H | Exact 16x16 integer minor modulo prime 1000000007 |
|---|---:|---:|
| 0 | 5 | 681390811 |
| -e1 | 4 | 560463606 |
| +e1 | 4 | 725563230 |
| -e2 | 4 | 159304598 |
| +e2 | 4 | 159304598 |
| -e3 | 3 | 640115905 |
| +e3 | 3 | 359884102 |
| -e4 | 3 | 640115905 |
| +e4 | 3 | 359884102 |

Every displayed residue is nonzero, certifying Q-linear independence of the sixteen rooted full-observer response families within the stated horizon. For **each of all nine roots**, a separately constructed positive equal-weight original-port initial law is verified by **direct integer path counting on the 96-state original native graph**, symmetric at n=0,...,H-1 and asymmetric at n=H. Thus the upper bounds and lower bounds are both exact.

A concrete sharpness witness: at root -e3, uniform initial support {18,42,86,62} is coefficientwise symmetric at n=0,1,2; at n=3, monomial seven-observer vector (0,1,0,1,0,1,0) has 64 labeled paths and its fifth/sixth-swapped vector (0,1,0,1,1,0,0) has 56, among 4*6^3=864 paths. Exact probability discrepancy = 1/108.

## Proof: all-depth row-equitable transfer and finite integer certificate

For each rooted kernel, take the tagged union of normal and fifth/sixth-swapped 96-state native automata. Refine 192 tagged states by exact multiset of (full seven-variable increment, successor class) preserving six parallel labeled actions. Each of nine cases gives exactly the **same 51 tagged-state classes as zero root**, up to harmless renumbering, and equal original/swapped class multiplicities. The resulting rooted quotient has seven-coordinate monomial-labeled transition operators B_(r,w).

The two predecessor zero-root class-row vectors v0=e40-e41-e46+e48 and v1=e40-e42-e46+e50 satisfy **entrywise exact integer** v0^T B_(r,w)=v1^T B_(r,w)=0 for **every distinct action monomial w of every one of nine roots**, and v0^T 1=v1^T 1=0. Consequently for each root and every n the class-response relations q40-q41-q46+q48=0 and q40-q42-q46+q50=0 hold. Their difference combines the exceptional port pairs to produce the same last mass-balance block.

The complete all-depth discrepancy therefore factors exactly as sum over sixteen blocks of (μ(A)-μ(B))*H_(r,block)(n), where H is a full seven-variable rooted response polynomial family. Thus 16 balances always suffice. An explicitly selected 16x16 integer coefficient minor from n<=H(r) is nonzero modulo 1000000007 for each root, proving necessity and finite-horizon sufficiency; separate **positive native-port distributions** with direct counted asymmetric coefficients at n=H prove minimality. This is a certificate over integers and a declared finite state model, not floating-point extrapolation or a result about arbitrary roots.

## Exact reproducibility and Source state

Stdlib-only executor: prefix577_r6_all_nine_root_initial_symmetry.py with pinned frozen_native_kernel_prefix577.py and previous zero-root certificate. Nine-root 51,811-byte JSON certificate SHA-256 **3cffe128c7110a3355a8bd65565cab09b186269cb7519f5d61e1b742049b1f55**; zero-root input certificate SHA-256 **215f02c55b6815a613cb3a78739474bb040da7ac08d8806b07234dbaab58c0ea**. Clean ZIP extraction and rerun reproduced the nine-root certificate byte-for-byte. Nine-file conversation-local ZIP SHA-256 **9e7d2943306433625803d21359d98962b9f9f1aaf8fbf4659815cfe2e9145947**; ZIP is not represented as a Source upload or GitHub blob. The detailed expanded theorem contains all exact witness supports and verifier semantics.

As observed 2026-11-08 ~06:45 UTC, native em_status read returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; Site is CONFIGURED_NOT_LIVE_VERIFIED with backend_connected=false and research_authority_granted=false. No native session, CLAIM, OPEN, checkpoint, freeze or independent review was issued by this author note.

Original UR V2 obligation is separately preserved: restore the actual 94,687-byte four-file object with SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76, then only authorized native writer/provenance/checkpoint. Four old predecessor historical evidence files do not substitute for the exact original Bundle. Actual own recovery_status/original request receipts/exact Source continuation must precede formal task mutation, with completed_units=[] for CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS.

Next scientific question: find a typed symbolic root-parameterized coboundary condition preserving the full-label annihilator and the 16-block initial law; test one specifically selected native root outside the nine as a separately scoped hypothesis, not an inferred extension.
