# R4-EC32 — A finite BRC source-bridge certificate and a sharp obstruction to shallow-depth inference

Date: 2026-10-26, Asia/Shanghai. **Status: AUTHOR-SIDE EXACT MATHEMATICS / UNREVIEWED / NOT_ADMITTED.** No native Enterprise Math Result, CLAIM or independent Driver decision is asserted.

## Frozen source and predecessor

- Account canonical snapshot: awdawmip/chatgpt-global-knowledge main@40ae4bf39f84a1ad1b122a824019ef562a5e4bc1 (GLOBAL_KNOWLEDGE_V1), including 00_BOOTSTRAP.md, OPERATING_MANUAL.md, project bootstrap, P000_REALITY_FOUNDATION.json, P000_STARTUP.json, ACTIVE 我眼中的世界.md, mathematical/code/BRC research policy and activity route.
- Project source: awdawmip/enterprise-math main@e27e64dfe4803804ff84c9ca75d83da4cc38459b, including AGENTS.md, HEARTBEAT_WORLD_NATIVE_X6_TIME, joint-observer preservation, heartbeat BRC-only constraint, control authority and PORTABLE_RESEARCH_PROTOCOL.
- Immediate predecessor: R4-EC31 at commit 67817ffc5bee062c2c0799912b2acaac2ec3be6d, path research_notes/r4_ec31_observer_relative_defect_20261026/EC31_OBSERVER_SCOPE_AND_RELATIVE_DEFECT.md. EC29 and EC30 provide the positive-source history-bit carrier.
- Authenticated GitHub connection: awdawmip (administrative access to the project repo). Native task/owner read returned CONTROL_QUOTA; Sites configuration read returned static_machine_readonly and write_relay_enabled=false, not native research authorization. Active task owner, native session and formal CLAIM remain UNKNOWN; source-side Research Activity registration is REGISTER_PENDING.

## Exact scientific scope and BRC law

This paper concerns **finite positive-source ordered-word BRC**, not a verified physical heartbeat program. Its alphabet is Σ={A,B,C}. Each letter is an elementary test step along native X6 axes +E1, +E2, +E3 respectively, in an explicitly restricted three-dimensional slice of six-dimensional discrete Cell space. The selected third coordinate counts C. The other three displacement components remain fixed relative to a chosen anchor; this is not a claim about an absolute six-field Cell address or preservation of a true native X6 slice under an unknown update. Word length means operation depth, not independent physical time. Grade can be B-count.

The carrier retains individual labelled alternative sources, positive branch multiplicities, ordered composition, initial residual/history state, a future-operation word and an exact source-count observer. Given a finite residual state set of cardinality n, represent each allowed letter by a nonnegative rational matrix M_a of dimension n. Its (i,j) entry is the **sum of positive contributions from distinct source-labelled transitions i→j for that letter**, without deleting multiplicity. With initial row α and terminal column β,

    f(w)=α M_{w1} M_{w2} ... M_{wk} β,   f(empty)=αβ.

Positive alternatives add; ordered serial steps multiply. This precise representation is a BRC source-count observer, not a signed-amplitude or complex-phase model. Equality of these f(w) values for all words ensures equality of any common fixed word-sum endpoint/grade observer; it does NOT itself establish a bijection of provenance labels or exact native joint state.

## Theorem A: a finite equivalence certificate for all future word counts

**Theorem.** Let F and G be two finite positive-source BRC word-count observers over the same declared alphabet, with respectively m and n fully specified, closed residual states and exact initial/terminal observers. If

    F(w)=G(w) for every word w of length at most m+n−1,

then F(w)=G(w) for every finite future-operation word w. The empty word is included in the initial test. Rational weights are allowed.

**Proof.** Work only in an algebraic comparison vector space of dimension d=m+n. Put

    α*=(α_F,−α_G);
    M*_a=diag(M^F_a,M^G_a);
    β*=(β_F,β_G)^T.

The comparison scalar α*M*_wβ* equals F(w)−G(w). The minus sign here subtracts *two already computed positive-source counts*; it never denotes a negative source branch or a physical cancellation.

Define V_k=span over Q of rows α*M*_w for |w|≤k. These spaces ascend, their dimensions never exceed d, and V_0 has dimension one unless α*=0. If V_k=V_(k+1), multiplication of V_k by each M*_a stays in V_k, so it remains equal to every later reachable space. Every strict growth increases dimension at least one, hence stabilization occurs no later than k=d−1. Therefore V_(d−1) spans every reachable row. The assumed vanishing of all differences for |w|≤d−1 says that every spanning row is annihilated by β*. By linearity, every reachable row is annihilated, so F(w)=G(w) for all w. When α*=0 the claim is immediate. QED.

**Exact compact certificate.** Instead of enumerating exponentially many words, start from α*, multiply every retained independent row by every M*_a, and insert a new row only when it is linearly independent over Q. Stop at closure. All possible future comparison rows are in this finite reachable span. Annihilation of the resulting rational row basis by β* certifies equality of **all** future word-count observations. If the reachable rank is r, basis witness depths can be bounded by r−1, sharpening the universal m+n−1 cutoff. EC32_verify.py executes that construction with exact Fraction elimination.

### Explicit EC29 two-state BRC interface

Use states ordered q=0,1, where q records whether the previous operation was A. In the declared EC29 positive-source model C has two distinct source-labelled choices when q=1, one otherwise; A and B always have one choice. Its matrices are

              [0 1]             [1 0]             [1 0]
    M_A =     [0 1]   M_B =     [1 0]   M_C =     [2 0]

    α(q=0)=[1 0],   α(q=1)=[0 1],   β=[1 1]^T.

Thus a genuinely established finite native-X6 source observer having at most n full residual states and precisely the same allowed operation alphabet and terminal count could be compared with this two-state model by checking every exact word of length ≤n+1. For native n=2 this finite test reaches depth 3. This is only a **conditional mathematical test recipe**: it assumes full native transition closure, correct branch-weighted readout, residual state capacity, selected X6 slice, third coordinate, grade and operation/time typing. Comparing depths 2 and 3 without proving these hypotheses grants no unbounded-horizon source lift.

A stricter **source-fibre** lift needs a compositional label-respecting bijection or a suitable future-observer-preserving relation at every transition, including source identities, residual state, allowed continuation and readout. Scalar matrix equality is necessary for the chosen scalar observer, not sufficient for labelled fibre equivalence.

## Theorem B: no dimension-free finite-depth test, and the cutoff is sharp

**Theorem.** For every integer H≥1 there exist two explicit positive-source BRC path systems using identical operation letters, identical selected X6-axis displacements, identical word endpoints, grades and operation depths, that have **equal exact source count for every word of length ≤H**, but unequal counts for one word of length H+1.

**Construction.** Model U has one residual state and one source-labelled transition for each of A,B,C. Its word count is U(w)=1 for every w.

Model V_H retains H+1 states r=0,1,...,H, recording the consecutive trailing A-run length, capped at H. From state r, letter A moves to min(H,r+1) with multiplicity one; B moves to 0 with multiplicity one; C moves to 0 and has multiplicity **two** if r=H, otherwise one. The two C choices, when they exist, have distinct positive source labels. The initial state is r=0, and all terminal states contribute one.

A doubled C needs at least H preceding As, so every word w with |w|≤H has V_H(w)=1=U(w). However the exact operation word A^H C has length H+1 and satisfies

    V_H(A^H C)=2;    U(A^H C)=1.

The two source systems change only source branch labels, not the ordered geometric test steps, endpoints or grade. This supplies a counterexample to the claim that any fixed shallow-depth check, including only depths 2 and 3, guarantees an all-depth lift **without a proven residual-state bound or a commuting structural bridge**. The counterexample is an invented source-labelled path rule, not an actual P000 heartbeat transition and not an objection to EC27 auxiliary unimodality.

**Sharpness.** Here the dimensions are m=1 for U and n=H+1 for V_H. The general cutoff in Theorem A is m+n−1=H+1, and the earliest disagreement occurs at exactly that length. Thus the general finite cutoff cannot be reduced for these state dimensions. The combined reachable comparison rank must equal H+2, since any smaller rank would yield an all-word equivalence certificate from the agreement through depth H, contradicting the explicit difference. QED.

## Actual computation and evidence

The remote executable EC32_verify.py implements positive integer source-transition matrices, an independent combinatorial word-scan source-multiplicity evaluator, exact comparison-row rational span, and a two-state permuted-encoding equality test. Its generated EC32_REPORT.json records:

- EC29 comparison with an independently permuted two-state encoding: 3,280 words per initial q state, 6,560 exact word checks, and a closed rational comparison basis of rank 2 proving the permuted two-state observer equivalent for **all** future words.
- H=1,...,8 delayed-branch systems: every word of length 0,...,H exhaustively matched to the one-state baseline; each A^H C gave exact 2-versus-1 counts; 14,764 such aggregate checked words/witnesses. The comparison rank at H is H+2, and its first nonzero basis witness has length H+1. For H=8, the witness is AAAAAAAAC, word length 9, comparison rank 10.
- All checks use CPython standard-library arbitrary integers and exact Fraction, not floating-point fitting. Both universal theorems follow from proofs, not extrapolation from H≤8.

Locally executed source SHA256: 604233139ed6fd2e2db491de3f661b37ae0af98d0e1fecf38c180e561d3f983d. Locally generated report SHA256: ca4851630b8b37652c37b2286fbb2fca9761fb6d3f019105b228b865c70e1f5f. The code and report were published and read back from the same GitHub research branch with the expected Git blob SHAs; their remote file URLs are separately reported. A separate local expanded explanatory proof and clean-extraction cold-start verification are in the EC32 evidence ZIP.

BRC methodological disposition: REUSE_APPLIED to EC29's labelled positive-source path semiring and EC30/EC31's future-word observation law; COMPOSE_APPLIED for state-memory fibre discipline; EXTEND_EXISTING_TOOL for rational reachable-span equivalence certificates and sharp delayed-branch obstruction. No classical propagator, trigonometric computation, physics residual simulation, complex-source cancellation or higher-precision surrogate was executed.

## Actual native limitation, honest handoff and next question

The pinned P000 and current X6 source leave fixed_heartbeat_program=null. An actual authorized source-labelled native-X6 heartbeat update, source-fibre rule, complete slice embedding and time/grade observation have not been supplied in the inspected sources. The required source-labelled native automaton and its residual dimension cannot be constructed from spatial axis names alone. Thus there is **no completed native heartbeat bridge, physical attribution or all-X6 theorem**.

Current classification: author-side proved mathematical statements with exact local evidence, GitHub draft research branch, native owner/CLAIM unknown, no native Result, independent Driver review or mathematical admission. Research Activity official registration and Guard remain pending; a GitHub commit is evidence persistence, not role authorization.

**Next executable scientific unit:** obtain the exact authorized native X6 source-labelled transition and its allowed future words, with six-dimensional Cell identity, selected three-dimensional slice/third coordinate, retained historical residual, separately typed time, grade and readout. Prove a finite residual dimension bound n or a label-preserving transition simulation. If finite, instantiate the native weighted matrices and run the all-word certificate through n+1, or prove the rational reachable-span/intertwining relation directly. Independently check source labels and fibre multiplicities. Use V_H as an adversarial control against unjustified shallow-depth inferences.

Provenance preservation, evidence storage and scientific admission remain distinct; future work should continue from the highest actually verified immutable source rather than treating author-side notes as accepted foundation.
