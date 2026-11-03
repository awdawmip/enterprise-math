# Stage407-B: Exact finite future tests and inverse-Q-tail memory compression

Date: 2026-11-03 Asia/Shanghai. Research2, continuation of Stage406-B commit 564f061a24866959a13c99185009ffb531104f4a, Draft PR #1736. Classification: PORTABLE_AUTHOR_THEOREM / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative reads: global d618983a96000de251901eb2cf0d1e1fa4298315; Enterprise Math e90b07741a38a412ecf9fe161052ecd2353e5736. P000 and ACTIVE worldview unchanged.

## 1. Typed model and mother objective

D consists of the twelve signed native X6 steps ±E_i, 1<=i<=6, with inverse steps on the same axis. P and Q are initially equal-length ordered histories, not independent lower-dimensional spaces. Current full observer O gives lengths, signed X6 endpoints, directed adjacent-pair histograms J_P and J_Q, absolute-index match count K=sum_{i<=min(lengths)}[P_i=Q_i], endpoint-derived native BRC counts and positive weights, and any nonzero scalar direction-local products. Operations: any APP(a,b), at most one POP_Q deleting Q's last step, and at most one CANCEL deleting the last two steps of BOTH sources when both terminal pairs are inverse. Each intermediate observation and enabledness is visible.

Two histories on one current-observation fiber are future equivalent when all common legal finite operation traces have matching intermediate observations and matching enabledness. The Stage406-B raw suffix key (P3,Q4) is sufficient, with the entire shorter word retained when needed. We seek its *exact* per-fiber minimal quotient.

## 2. The four-APP shielding lemma and finite complete tests

Lemma 407.1. Suppose two compared states have equal full current observers, the same lengths and P-length minus Q-length in {0,1}, and execute the same four consecutive paired APP operations. If the observers match at all four intermediate points, every further allowed operation trace with at most one remaining POP_Q and one remaining CANCEL is observer-identical.

Proof. One CANCEL deletes at most two P and two Q terminal steps, and one POP_Q deletes at most one additional Q step. Thus after four APPs at least two appended P letters and one appended Q letter survive any later deletions; no prior original letter or prior original adjacency edge can be removed. The first APP adds exactly the boundary edges (last P,a1) and (last Q,b1) to their respective directed histograms. Equality of the pre-APP and first post-APP histograms therefore forces equality of any existing original terminal labels in the two compared histories. Subsequent endpoint, ordered adjacency and direction-local multiplicative changes involve only their common appended suffixes. For K, the old overlap is retained; new comparisons involve common appended letters, except when P was exactly one step longer than Q, where Q's first appended letter is compared with P's old terminal letter, already shown equal. All later enabledness is decided by common appended terminal letters. Induction over later operations proves the assertion. Empty old words are covered by omitting their boundary edges.

Theorem 407.2 (complete bounded test language). Two initially equal-observer histories are future equivalent if and only if they have equal outputs and enabledness on every legal action trace with at most one POP_Q, one CANCEL and no four consecutive APPs. Every such trace has at most nine APPs (three APP blocks with at most three each) and two destructive steps: total length <=11. The statement holds over all twelve signed X6 directions and any finite original length.

Proof. Necessity is immediate. If an arbitrary trace distinguishes, truncate at its earliest mismatch. A preceding block of four consecutive APPs cannot occur: equality through that block would invoke Lemma 407.1 and rule out all later mismatches. Hence this first distinguishing prefix itself belongs to the bounded reduced language.

Algorithmic consequence. Enumerate feasible Stage406-B suffix keys using the Stage402/404 coupled residual-Euler directed-edge-count and K dynamic program, without listing all complete word pairs. For each key, compute the exact observer/enabledness trace signature for all reduced action words; Stage406-B's reconstruction makes these signatures functions of O and the retained key. Equality of signatures is exactly future equivalence, and q distinct signatures require ceil(log2 q) fixed code bits. There are at most 12^7 candidate raw keys. With the twelve-direction alphabet fixed, the reduced test enumeration has a huge but length-independent finite bound. The feasibility DP is polynomial in the *numeric* histogram counts at fixed alphabet size, and is pseudopolynomial relative to their binary encoding; no polynomial bit-complexity assertion is made.

## 3. A complete three-element fiber whose inverse Q tails compress

Let A=+E1 and B=-E1. Fix
P=AAAAAA;
Q0=AABABA;
Q1=ABAABA;
Q2=ABABAA.

All three pairs have six steps per source, endpoint P=6E1 and Q=2E1, J_P(AA)=5, J_Q(AA)=1, J_Q(AB)=2, J_Q(BA)=2 with all other counts zero, and K=4. The Q word has four A and two B. Products of any nonzero scalar direction-local factors therefore agree. Both Q0 and Q1 have terminal inverse pair BA.

Lemma 407.3 (fiber completeness). The above three pairs are the complete observation fiber, even over the full twelve-step alphabet. P's five AA adjacency edges force P=A^6. Q's given edge multiset forces a walk on A,B beginning and ending A, containing exactly two isolated B letters and one AA edge; the extra AA adjacency may occur in exactly one of the three A-runs. These are Q0,Q1,Q2. The executed sparse Euler/K residual-edge DP independently returns the three four-step terminal keys BABA, AABA, ABAA, with count one each; a direct exhaustive two-letter six-step enumeration agrees.

Theorem 407.4 (exact minimum). The future equivalence classes on this full fiber are {Q0,Q1} and {Q2}. Thus the raw Stage406-B suffix representation has three distinct states but the exact minimum has two; fixed-length binary memory falls from 2 bits to 1 bit.

Proof of Q0~Q1 over all 12 append directions. For r=0,1,2 deleted original Q letters, the Q-prefix pairs are:
r=0: AABABA / ABAABA (last two BA, each four A);
r=1: AABAB / ABAAB (last two AB, each three A);
r=2: AABA / ABAA (last two BA, each three A).
Each row has identical length, signed endpoint, complete directed adjacency J, and terminal pair. P's original prefix remains A-only with length at least five. Indeed an original-P-touching CANCEL cannot erase two P originals because its original terminal pair is AA; to be enabled it must have a newly appended B and then removes that B plus only the original terminal A. At most two original Q letters can disappear. If CANCEL removes two Q originals while P carries its necessary appended B, the paired APP also put a letter on Q and the unique POP_Q must remove that appended Q letter; no POP is left to erase another original. In all remaining POP/CANCEL orders, one CANCEL and one POP remove at most two Q originals. Therefore only the three listed Q original prefixes can occur.

Induct on the common action trace, separating surviving original prefixes from the common appended suffixes. Equal row-wise endpoint/J/last-two summaries, and equal P original summaries, imply equal enabledness and per-source observations. For synchronous K, every original P direction is A. Against an original Q prefix of length 4,5,6, both versions give respectively 3,3,4 A matches. When P has lost its sixth original A, any still-present Q original at position six is the common symbol A; all other comparisons between an original and appended segment use P's common A or common appended letters. Consequently K is also equal at each intermediate step, including shifted alignment after POP. The same induction works for arbitrary appended directions outside {A,B}. Endpoint/length-derived BRC readings and nonzero scalar direction factors update equally. This proves Q0~Q1 for every finite future trace.

Distinguish Q2 by the immediate legal POP_Q operation: Q0,Q1 lose a terminal BA directed edge, whereas Q2 loses AA. Their new directed histograms differ; hence Q2 is a necessary separate state. This exhausts the complete fiber.

## 4. Exact executed integer evidence and limits

REPRO_STAGE407B_MIN.py was executed twice with byte-identical stdout in REPRO_STAGE407B_MIN_EXECUTED.json. It independently computes sparse Euler remainder/key counts and brute two-letter word enumeration, runs a complete two-letter reduced-trace comparison (four-APP shielding is proved above), and evaluates the native all-twelve-direction length-six integer BRC recurrence
N_{n+1}(z)=sum_{d in D} N_n(z-d); W_{n+1}(z)=sum_{d in D}w(d)W_n(z-d).
Weights: w(A)=2,w(B)=3,w(other)=1.
Results: N6(6E1)=1,W6(6E1)=64; N6(2E1)=4665,W6(2E1)=32760. These BRC quantities count all endpoint walks and are distinct from the adjacency-restricted 3-element fiber. Q0/Q1 finite exhaustive test uses 86,273 paired states and 90,355 transition checks; both comparisons with Q2 separate by POP. The full-12-alphabet future equivalence claim follows from the case-analysis proof, not from the two-letter BFS.

Reuse: native twelve-direction positive-weight BRC recurrence REUSE_APPLIED; directed residual Euler plus coupled K transfer from Stages399/402/404 COMPOSE_APPLIED. Preserve source identity, ordered edges, K, branch count versus positive weight and signed factors.

## 5. Next question and authority

Stage408-B: reduce the 11-action complete test bound to a smaller set of symbolic eraser skeletons, retaining exact K after one-source POP and quantifying binary versus numeric-length complexity. Expand the exact Euler/K feasibility-to-minimization composition on a larger fiber without listing full word pairs. No independent Driver review is asserted. For this run, native owner listing returned CONTROL_QUOTA, and service status returned BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false. GitHub author-side proof is not a native CLAIM, Source Result or mathematical admission.
