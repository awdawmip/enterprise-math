# R263 — Global seven-way provenance saturation inside one affine-effect fiber

2026-10-24 | Author-side exact proof and exact finite verification. UNREVIEWED; NOT ADMITTED; no native execution session or CLAIM.

## Frozen authority, provenance, and model boundary

GLOBAL_KNOWLEDGE_V1 canonical main: 7ed68d9c321685e609fe1ac2800af7c3592de4e1. P000 ACTIVE_LOCKED original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, matching its startup projection. Enterprise Math canonical main at derivation: 238626c2bb75a51b843c3cb3e1af56c60a30e530. Read the account bootstrap/manual, Task research role, ACTIVE worldview, native-X6 companion, portable protocol, applicable math/BRC/code policies. Direct model predecessors: R260 commit 2f45730d1bf1064b9072ad4e57ade3f0e285d112 and R262 commit c446659ec353ad6e8d65591f6d882521ff674ac2. Predecessors are author drafts, not accepted theorems.

Scope: formal positive-weight toy BRC with six *formal* affine-coordinate slots. This does not establish legal native P000 six-axis rotations, force dynamics, final Cell addresses or the physical heartbeat time law. The depth m is a count of serial abstract operations. No use of classical trigonometric or numerical heartbeat substitutes. R193's actual source-label/time-port semantics remain unverified.

## Defined BRC model

Initial control/history/effect state (q,r,eps,k)=(0,0,+1,0). q in {0,1,2}; source selector a in {0,1}. DFA r=0 denotes no 00 found and last symbol not zero; r=1 denotes no 00 found and last symbol zero; r=2 denotes 00 already found. The update of r on a=0 is (1,2,2), and on a=1 is (0,0,2).

Positive weight for each raw branch is 1. The q-transition/affine edge (q',eta,b) is:

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

The formal full six-slot affine effect is F_(eps,k)(z)=(eps*z1+k,eps*z2,z3,z4,z5,z6), and chronological composition is F_(eps,k) THEN F_(eta,b)=F_(eta*eps,eta*k+b). It is a defined algebraic surrogate, not verified native physical evolution.

The seven reachable joint control states in canonical table order are S=((0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)). Observable terminal query is (q,h) where h=1 iff r=2. The full effect (eps,k) may additionally be read. Permitted futures repeat the same *nondiscriminating* positive binary choice packet; observers do not choose the individual selector.

## Theorem 1: universal simultaneous fiber saturation

For EVERY integer m >= 8, there exists ONE full affine effect g_m such that all seven distinct (q,r) in S occur with POSITIVE original-history multiplicity and with that SAME g_m at the SAME depth m, from the common initial state. The least possible depth is exactly 8.

Proof, base certificate: the following table gives, for each j, an affine effect shared by seven length-j raw words; every word belongs to the matching terminal (q,r) column.

| j | (eps_j,k_j) | (0,0) | (0,2) | (1,1) | (1,2) | (2,0) | (2,1) | (2,2) |
|---|---|---|---|---|---|---|---|---|
| 8 | (+1,0) | 01010101 | 00001100 | 01010110 | 00000100 | 01101011 | 10101010 | 00001010 |
| 9 | (-1,-1) | 110101101 | 000001000 | 101010110 | 000001110 | 101101011 | 010101010 | 000000011 |
| 10 | (-1,0) | 1011010101 | 0000000101 | 1011010110 | 0000000110 | 1011101011 | 0101011010 | 0000000011 |

Direct composition of the declared edge law verifies all 21 base words. The EXACT positive multiplicity vectors in this column order are:
- depth 8, common effect (+1,0): (1,6,1,9,1,1,16), total 35;
- depth 9, common effect (-1,-1): (1,19,2,20,3,1,28), total 74;
- depth 10, common effect (-1,0): (2,38,3,29,4,1,49), total 126.

The three-symbol prefix p=101 starts at (q,r)=(0,0), returns to that same joint state, and has effect (+1,-1). Hence p^h returns to (0,0) with effect (+1,-h). For any m>=8 set j=8+((m-8) mod 3) and h=(m-j)/3. Prepending p^h to every one of the seven j-witnesses preserves all seven terminal (q,r) outcomes. Since the seven j-witnesses share (eps_j,k_j), the resulting m-words share the effect

g_m=(eps_j, k_j - eps_j*h)

by the chronological THEN law. Each remains a distinct positive-weight raw history. This establishes the claim for ALL finite m>=8 by an explicit construction; finite tests are not substituted for the proof.

For m=0,1,...,7 exact exhaustive evaluation of ALL binary words, respectively 1,2,4,8,16,32,64,128 words, yields the maximum number of joint (q,r) outcomes sharing a single (eps,k) at that depth equal to (1,1,1,3,4,4,5,6). This exhausts the declared finite domains, so no such full seven-way fiber exists before m=8. The displayed m=8 witnesses attain seven. QED.

## Theorem 2: effect-aware deterministic pathwise information lower bound

Consider a per-history deterministic memory codec whose future evolution and readout use only its stored nonspatial codeword, the exact accumulated affine effect (preserved, not overwritten as an encoding side channel), the step count, and the same future packet. Require exact current and all-future observations of (q,h) per raw positive history. The model may inspect the FULL effect.

At each depth m>=8, take the seven constructed histories with identical step count and effect. They cannot be assigned the same codeword in any pair. If q differs, the current q-output distinguishes the pair. If q agrees and one history has r=2, its current Boolean h differs. The only pair with identical current (q,h) is (q,r)=(2,0) versus (2,1). Under ONE further nondiscriminating packet, selector a=0 transitions respectively to (q=1,h=0) and (q=1,h=1); selector a=1 transitions in both cases to (q=2,h=0). The two next-step positive output count vectors thus differ. Equal codeword, effect and time would imply identical futures, a contradiction.

Consequently at each m>=8 at least SEVEN simultaneously distinguishable memory codewords are necessary even when exact accumulated affine effects are visible. This is stronger than adding separate lower bounds from different effect fibers: ONE single shared fiber gives the witness. QED.

Strict boundary: This only proves the deterministic PER-HISTORY lower bound under the specified future-readout contract; it does not rule out a <7-dimensional unrestricted time-homogeneous weighted AGGREGATE model with effect-dependent linear readout or nonlinear decoding. R262's separate Hankel lower bound requires effect-INDEPENDENT fixed linear readout. Never transfer either claim beyond its representation class.

## Verification

Python author-side exact enumerator checks each word to depth 10, the first globally saturated depth, base witnesses, positive counts, and constructed prefixes to m=180. Independently implemented C++17 enumerates all words to depth 10, checks all 21 witnesses and the same bounded prefix family. Both PASS. The all-depth part is proved above by the reset composition identity, not inferred from m<=180.

Code: R263_verify_global_fiber.py and R263_independent.cpp. Structured certificate: R263_AUTHOR_REPORT.json. Local verification package includes additional exact source and SHA-256 manifest. Neither code execution is the original Enterprise Math Source module.

## Actual owner/authorization and outstanding scientific work

The native control-task inventory returned CONTROL_QUOTA. A fresh service-issued RESEARCHER session start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Thus actual live owner, canonical CLAIM, research RA, authenticated Result, and independent Driver judgment remain UNVERIFIED. This GitHub research branch is author-side durable evidence, not a Source-native task or mathematical admission.

R264 exact next question: Specify effect-dependent linear readout and affine-carrier constraints, then test whether the FULL joint weighted histogram H_m(q,h,eps,k) can be represented by fewer than seven *aggregate* control states. An explicit positive 6-state model or a valid effect-filtered Hankel/semimodule certificate would discriminate the alternatives. Separately obtain R193's genuine source/time-port contract and execute source-pinned native ControlPacket/EffectHistogram before claiming any X6 physical transfer.
