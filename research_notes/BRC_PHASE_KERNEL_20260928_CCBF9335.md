# Source-bound BRC phase kernel v0.1

Progress-Event-ID: BRC-PHASE-KERNEL-CCBF9335-20260928
Date: 2026-09-28
Status: AUTHOR_DERIVED_AND_FINITE_EXECUTED / CANDIDATE_EXTENSION / UNREVIEWED / NOT_ADMITTED
Researcher-ID: EM-DIRECT-CCBF9335
Research-Activity-ID: RA-CCBF9335770F4460A2F947CFA000114F
Session: local-chat-brc-phase-ccbf9335770f4460a2f947cfa000114f (local writer key, not platform authentication)
Global read: awdawmip/chatgpt-global-knowledge@8ed0845abd58a3cfc63aef1f6a8d26f94cff2bbf
Scientific source read: awdawmip/enterprise-math@643a098b7ae08a4fb88c1c8f4f7e65502a7904f2
Publication preflight main: 40f9d6781a82eb50d65dcb7dae8b84299473bf93

## Objective and actual interface

Replace angle -> transcendental values -> propagation by sourced BRC word -> certified integer recurrence -> declared observation. No pi, trigonometric evaluation, square root, matrix exponential, Taylor, Pade or Cayley reference is executed. This is not yet an arbitrary-angle compiler or a universal replacement for classical geometry.

Actual positive core: src/enterprise_math/brc_weighted_recurrent.py:recurrent_mass_power at the scientific source read. Exact copied source: 10087 bytes, Git blob 4e6b3132580e3cd70a20a0d8bd4d28792b961afb, SHA256 7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26. Both hashes are checked before each Engine run.

The core handles nonnegative rational total walk mass. A signed edge q is lifted to positive states (port,parity), weight abs(q), toggling parity exactly when q is negative. Initial origin and ordered edge-id words give path provenance. The endpoint signed observer is positive_mass minus negative_mass. For each finite path, weight and parity equal the product of the original signed edge coefficients; summing proves intertwining for every declared signed-linear continuation. This explicit extension is not an already admitted signed feature of the positive core, nor a novelty claim for the sign-cover construction.

Producer calls really execute the positive core; bilinear coefficients use two-edge BRC paths. Common-denominator division is a typed, separately logged observer. Receipts preserve edge rules, positive/negative endpoints, word/depth, inputs, outputs, source and scope. Generative path descriptions are retained instead of enumerating all paths. Signed endpoint aggregation is not faithful to arbitrary history or positive-mass observers, so those are not silently included in its scope.

## Concrete candidate word and exact theorem

Reuse the candidate junction 2J-3I from research_notes/heartbeat_outward/20260927_9F026E/IMPLICIT_CAUSAL_FRONTIER_CHECKPOINT.md at the scientific source read, blob 664d3d973c45dfa7cc8591564d08f11b5ebb99ed. Its native force-law status remains unproved.

Three ports e0,e1,e2: D sends a port to itself with coefficient -1/3 and to each other port with coefficient 2/3. Z preserves the sign at port0 and flips it at ports1,2. Execute D then Z, denoted W=ZD. Since J^2=3J, (2J-3I)^2=9I; thus D and Z are involutions preserving this candidate's algebraic response norm. Reverse operation executes Z then D.

With u=e1+e2, the response plane span(e0,u) is invariant. The edge sums on (a,b,b) are ((-a+4b)/3,(-2a-b)/3,(-2a-b)/3). Define

    A0=1, B0=0, D0=1;
    A(n+1)=-A(n)+4B(n);
    B(n+1)=-2A(n)-B(n);
    D(n+1)=3D(n).

Induction gives W^n e0=(A(n),B(n),B(n))/D(n), for every n>=0. The producer evaluates this recurrence through a signed-edge BRC graph, not through trigonometric seeds. The exact identity

    (-A+4B)^2+2(-2A-B)^2=9(A^2+2B^2)

proves A(n)^2+2B(n)^2=D(n)^2. Define K e0=u and K u=-2e0. Then K^2=-2I on that plane, and W^n=(A(n)I+B(n)K)/D(n). Two same-word triples compose as

    (A,B,D) * (C,E,F) = (AC-2BE, AE+BC, DF).

Inversion changes B to -B. These identities replace the phase-composition role of trigonometric coordinates for this declared word. They do not identify B/D with the ordinary sine of an arbitrary external angle.

First executed triples n=0,1,2,3,4 are (1,0,1),(-1,-2,3),(-7,4,9),(23,10,27),(17,-56,81).

## Residual and cost boundaries

W e0=(-1,-2,-2)/3 and W^-1 e0=(-1,2,2)/3 have the same present first-port value -1/3. Applying one further W gives first-port values -7/9 and 1 respectively. The orientation component cannot be deleted under this allowed future. The raw positive cover mass is (5/3)^n, distinct from the signed response norm 1; neither is declared physical mass or energy.

The complementary line e1-e2 is fixed. For arbitrary input, let alpha=x0, beta=(x1+x2)/2, gamma=(x1-x2)/2. The full symbolic output is (alpha',beta'+gamma,beta'-gamma), where alpha'=(A alpha-2B beta)/D and beta'=(B alpha+A beta)/D. Compact full-input API is not implemented; raw full-space tests retain and check the complement. The global annihilator is (W-I)(3W^2+2W+3I)=0. Using only its quadratic factor outside the response plane is invalid. Different words need not commute; an explicit port-permutation control demonstrates this.

A(n+2)=-2A(n+1)-9A(n), A0=1,A1=-1. Modulo3 gives A(n)=-1 mod3 for every n>=1, so A(n)/3^n has exact denominator 3^n. Therefore W has no positive finite period and explicit exact output needs Theta(n) denominator bits. Fewer algebraic compositions do not establish reduced bit complexity or wall-clock time. The dense positive-cover engine is a validation baseline, not a performance claim.

Ports, sign-cover states, invariant-response coordinates and recurrence index n are not P000 spatial dimensions or physical heartbeat time. Six native axes, 120-degree native orthogonality and independent time are unchanged. This is an algorithmic candidate with an explicit norm observer, not a derived native force law, quantum device or Shor speedup.

## Executed coverage

Each complete run passed 156 named checks, with 203 actual positive BRC core calls and 34 common-scale observer calls. Tests cover n=0..16; raw word versus integer pair; separately compiled scalar recurrence; norm, inverse, exact denominator, positive-mass law; eight composition pairs; fixed complement; full cubic relation; direction alias; noncommuting words; malformed input rejection; producer forbidden-call AST check.

The second full local run and a third run from a fresh ZIP extraction reproduced both RESULTS.json and the complete compressed BRC ledger byte-for-byte. Manifest checks passed. These are same-producer replays, not independent peer review or formal proof-assistant validation. No arbitrary-angle compilation, full Stage100 rerun, Shor circuit, low-precision experiment, timing comparison or physical validation was performed.

## Generalization and approximation: proved conditions, not executed extension

For a sourced operator T and declared input/future/observer scope, prove an annihilating polynomial mu(T)|V=0 before reducing powers modulo mu. Include coefficient growth, finding the certificate, full-state complements and observation costs. This is standard linear-recurrence algebra; the contribution here is the source-bound BRC interpretation, explicit scope and executed example. Stage100's actual-root normal form remains prior project work and is not replaced or claimed anew.

If exact W is isometric and per-step state rounding errors are bounded by eta_j, accumulated error is at most their sum. For a rounded operator only known to differ by eta, the generic n-step bound is (1+eta)^n-1; n*eta requires both operators to be isometries. Winner selection with certified value error epsilon is preserved by a gap exceeding 2epsilon. This does not certify an entire sampling law or Shor continued-fraction success. Low-resolution execution is the next research unit, not a result of this run.

Primary-source context: AMD CORDIC6.0 official documentation; NIST DLMF18.9 and4.21; Bostan and Mori, arXiv:2008.08822 (abstract/arithmetic-complexity scope); Wildberger, arXiv:0806.3481 and author's UNSW overview (abstract/overview scope). No full-paper reading or priority claim is inferred from these scopes. Full URLs are retained in the package PROOF.md.

## Durable evidence

Archive: BRC_Phase_Kernel_v01_20260928.zip, 13 files, 43224 bytes.
SHA256: 61f19905d469bd544a46e13dd23d7095254d408afc6dfd45df3371a143a8a59f.
Drive: https://drive.google.com/file/d/1nQpUKt34nqgxP0yPjNHQ1twCz0lVZYB5/view?usp=drivesdk
Parent: 19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP (existing research-material folder).
Upload succeeded and metadata confirmed ID, name, parent and43224bytes. No remote redownload hash was verified.

RESULTS.json SHA256 c9fbdb04a5177ba2444e881ad9084429ec8b6019f28fe3481e10845cf7345e8c.
BRC_LEDGER.jsonl.gz SHA256 54c979b6befb48c4d53302b4b3bbaaeea7cfe4a6d416174e5e2c68b7546b2748.
PROOF.md SHA256 70e1b81b580a01e79c21ae0d083954a1e00bffe35a476e2bcb16b31da9da45a0.
Run: python run.py --out fresh-results from the extracted brc_phase_kernel directory.

Activity registration was created at1a54a242a7c04ff47d19eef953308a805b139f5d and read back at blob49d636e799217a53025a7582a5d4358e6d14f42b. The archive contains that initial registration, not a later activity-checkpoint binding. This source note does not claim a formal Task, CLAIM, Review, mathematical admission or a successful runtime pre-final guard. No schedule, worldview, earlier evidence or another writer's source is changed.

Global-Knowledge-Sync: main@8ed0845 / GLOBAL_KNOWLEDGE_V1
