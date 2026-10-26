# R4-EC39 — Predictive states do not guarantee exact co-adapted source overlap

Status: AUTHOR_SIDE_PROOF_AND_EXACT_CHECK, not native X6 dynamics, formal Task Result or independent mathematical acceptance.

## Frozen authority and scientific source

GLOBAL_KNOWLEDGE_V1 canonical snapshot: awdawmip/chatgpt-global-knowledge@35005f59b5c1065b74ee44e1a4f5a7ae05821bd9. The 00_BOOTSTRAP.md, OPERATING_MANUAL.md, active P000, worldview, mathematical and code rules and BRC/RA policy were read at this one pin. Enterprise Math project main was fixed at b24c47d54e79e9171baff05fd8950db1240d1a33, reading the portable research protocol, P000, heartbeat and joint-relation preservation contract. Existing sources: R4-EC37 co-adapted Bellman exact transportation formula, immutable 0a7e1d0baebfc648460c58cdc8b6fd99b675fe62; R4-EC38 arbitrarily conservative hidden-state bound, immutable 1757dfcdcc1bd9dd069e0fb2d0e1e70b708b33a0.

The GitHub connected identity was awdawmip with repository push/admin rights. Native owner lookup returned CONTROL_QUOTA. Native session creation returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. A native Task owner, CLAIM, Researcher session, Result and Driver authority could NOT be established. This is a provenance-preserving *independent author-side draft* and makes no claim on another owner's research.

BRC reuse: REUSE_APPLIED to finite positive-integer microscopic source-branch mass, labelled provenance, source-word count, exact total variation and the EC37 Bellman recurrence. This model is *auxiliary*. Source labels and temporal operation indices are not extra native spatial axes. The P000 6D X6 + separately typed time worldview is assumed as a research frame, but no heartbeat update, 3D slice selector, third-coordinate interpretation or native observer bridge is supplied.

## Theorem EC39.1: exact two-step overlap and adapted survival

Let A,B be finite alphabets. Two time-inhomogeneous unifilar labelled positive-source models P and Q have the same integer microscopic outgoing branch total M. Let k_a and ell_a be the respective counts of initial label a, with sum_a k_a = sum_a ell_a = M. Every initial microbranch with the same visible a leads to the SAME successor state within its model; thus the current state after an observed prefix a is uniquely known. From that state, let r_ab,s_ab be the respective integer branch counts for the next label b, with sum_b r_ab = sum_b s_ab = M. Every existing microbranch is a distinct positive source; a zero entry simply means no edge.

The complete word-specific counts are C_P(ab)=k_a r_ab and C_Q(ab)=ell_a s_ab (each model totals M^2). For the full length-two word observer with no terminal port and universal successor relation, define O=1-TV(P_2,Q_2), the *true* word-law overlap, and H, the highest entire-word agreement probability under EC37's **co-adapted state-pair joint-kernel-preserving transportation coupling**. Then

M^2 O = SUM_(a,b) min(k_a r_ab, ell_a s_ab).

M^2 H = SUM_a min(k_a,ell_a) SUM_b min(r_ab,s_ab).

Consequently TV(P_2,Q_2)=1-O <= 1-H. Their exact nonnegative gap is

M^2 (O-H) = SUM_(a,b) [min(k_a r_ab,ell_a s_ab) - min(k_a,ell_a) min(r_ab,s_ab)].

Proof: The first line is the elementary finite-measure maximal-overlap identity applied to M^2 equiprobable microscopic source histories. At the first step the joint distribution of initial labels can place at most min(k_a,ell_a)/M on equal label a. Every one of these separate maxima is achievable simultaneously by maximal first-step coupling, because the unmatched residual supports are disjoint. Conditional on this matched a, the two successor states are uniquely given by a. The optimal second-step match chance is SUM_b min(r_ab,s_ab)/M by the exact finite-label coupling theorem. Maximizing each nonnegative equal-label contribution therefore yields the H formula. Termwise min(xy,uv) >= min(x,u)min(y,v) for nonnegative values, giving the last inequality. QED.

## Theorem EC39.2: necessary and sufficient **two-step** exactness

For a fixed initial label a with k_a > ell_a > 0, its contribution to O-H is positive if and only if there exists some b with 0<r_ab<s_ab. Symmetrically, if ell_a>k_a>0, the contribution is positive if and only if some b has 0<s_ab<r_ab. If k_a=ell_a or min(k_a,ell_a)=0, the contribution is zero. Thus O=H iff no such witness exists for any a.

Proof: For k>ell>0, when r>=s the two expressions min(kr,ell s) and ell min(r,s) are both ell s. When r=s they coincide, and when r=0 both vanish. When 0<r<s, BOTH kr and ell s are strictly larger than ell r, hence their minimum exceeds ell r. Summing nonnegative terms proves necessity and sufficiency. Exchange P,Q for the symmetric case. QED.

Full-support corollary: If all conditional label counts are strictly positive for both models on the same finite second-label alphabet, O=H iff every a with k_a != ell_a and both positive has IDENTICAL conditional rows (r_ab)_b=(s_ab)_b. Nonidentical positive rows of equal total M have entries in both strict directions, triggering the criterion. Thus a predictive/unifilar quotient alone cannot guarantee an exact strong-causal overlap certificate when initial prefix masses disagree.

## Smallest clean two-model witness with both first labels present

Let M=3, first labels 0,1. The exact integers are:

- P: initial counts k=(2,1); following label 0 the next-label row is r_0=(1,2), and following label 1 r_1=(3,0).
- Q: initial counts ell=(1,2); following label 0 s_0=(0,3), and following label 1 s_1=(3,0).

Each first-step label determines its successor state, without any unresolved hidden branch choice. Two-step word counts:

| word | P | Q | min |
| --- | ---: | ---: | ---: |
| 00 | 2 | 0 | 0 |
| 01 | 4 | 3 | 3 |
| 10 | 3 | 6 | 3 |
| 11 | 0 | 0 | 0 |

Hence O=6/9=2/3 and actual TV=1/3. The adapted survival is H=[min(2,1)minsum((1,2),(0,3))+min(1,2)minsum((3,0),(3,0))]/9=(2+3)/9=5/9. Therefore the **optimal** EC37 co-adapted upper bound is 1-H=4/9, and its strictly positive conservative gap is 1/9.

An unconstrained maximal coupling of completed words may bias which microscopic futures form the matched subpopulation. The co-adapted conditional row law on both coupled present states may not be changed by such conditioning. The gap here is due to nonanticipativity and prefix mass imbalance, *not* hidden-state ambiguity.

Persistence: from step 3 onwards let both models emit only visible X through M microscopic branches returning to a common absorbing state. All length-two word counts are multiplied by M^(n-2) and X^(n-2) is appended. Thus for EVERY n>=2, actual TV=1/3, best co-adapted bound=4/9, and gap=1/9, by exact algebra.

Full-support witness: M=5, k=(3,2), ell=(2,3), r_0=(1,4), s_0=(2,3), r_1=s_1=(2,3). All displayed label counts are positive; O=19/25, H=18/25, and gap=1/25. Zeros are not needed for strict conservatism.

## Exact finite evidence

The actually run Python file EC39_verify.py enumerated all 184,819 binary-alphabet two-step models for M=1..6; exact integer overlap, nonnegative gap, iff criterion and independent binary transportation extreme-point calculations passed. 20,515 checked models satisfied the positive-support corollary premises. An independent Node BigInt-safe-in-range integer verifier EC39_GITHUB_VERIFY.js actually ran 67,170 models for M=1..5 and separately checked both witnesses and the exact initial transport optimum. Its saved report EC39_GITHUB_REPORT.json is the actual program output, status PASS. The exhaustive enumeration is only a finite software check; the formulas and all-n persistence are proved above.

## What remains unresolved

This is a complete two-step theorem for time-inhomogeneous unifilar positive-integer microbranch kernels; it does NOT establish the analogous if-and-only-if for arbitrary horizons, general hidden/non-unifilar source models, extra terminal ports, or microscopic branch-ID observers. The native P000 fixed heartbeat program is unspecified and no true X6 native-source or time attribution was tested.

Next EC40: derive an all-horizon observer-predictive BRC overlap recursion with explicit prefix imbalance and retained conditional future law; characterize exactly when the unrestricted full-word maximal coupling admits an EC37 state-pair co-adapted realization. Prove a compositional criterion or construct the minimal higher-order obstruction; only then consider native X6 transfer after source-branch and 3D slice mappings exist.

Activity class: source-tracked author contribution, native session/owner UNKNOWN, independent Driver NOT DONE, canonical mathematical acceptance NOT DONE.
