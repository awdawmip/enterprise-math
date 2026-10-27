# Stage196 — exact all-real optimum for an external N14 ternary IID problem

Date 2026-10-27. Status: AUTHOR_EXACT / PORTABLE_RESEARCH / UNREVIEWED / NOT_ADMITTED. The result is not a native P000 X6 or three-dimensional-slice dynamics theorem.

## Scientific inputs and provenance

Frozen GLOBAL_KNOWLEDGE_V1 main: 2efeb9799e7f61ceae87dec194dfb74b17310a86. Frozen Enterprise Math initial main: bdee30996b0cddf2b0248ca5afb4c8445fba2b75. P000 original blob: 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, matching the startup projection. ACTIVE worldview, BRC method scope, current task-research and portable-operations contracts were read. The immediate author-level predecessor is Stage195 at commit 7750603ec81a52459c7228eeb01a6ef352956dbf, including NEXT_TASK_PACKET_196.md; no mathematical admission is inherited.

Each IID observation lies in {0,1,2}. P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6); maximum observation depth N=14. Policies may randomize based on every complete ordered history and stop by N. Set eP=P(report Q), eQ=Q(report P), tP=E_P[T], tQ=E_Q[T], and V14(alpha)=min(max(tP,tQ): eP,eQ<=alpha).

## Exact full-real theorem

Define

- alpha195 = 1849072934531492153/5258930030792146944;
- V195 = 1153307972138565565/109561042308169728;
- Delta196 = 948828125/53496602689536;
- alpha196 = 1849166208131492153/5258930030792146944;
- V196 = 1152740427818565565/109561042308169728.

For EVERY REAL delta in [0,Delta196], including irrational values,

    V14(alpha195+delta) = V195-(506736/1735)*delta.

For every real alpha>alpha196, the **fixed Stage196 Bellman supporting line**, H196-(506736/1735)*alpha, lies strictly below V14(alpha). This does NOT identify the post-alpha196 value-function segment.

## Universal Bellman proof

The sufficient count state is s=(n,a,b) recording total symbols n and counts of 0 and 1, and ell(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. There are sum_{n=0}^{14} (n+1)(n+2)/2 = 680 states. Fix positive multipliers K196=L196=253368/1735 and

    H196=168137908605541983707/1485065690661519360.

With h at depth 14 terminal, perform finite exact rational backward induction:

    h(s)=min{ K196*ell(s) [report P],
              L196 [report Q],
              1+sum_i P_i*h(child(s,i)) [continue, only n<14] }.

This yields h(root)=H196; 1238 strictly positive action gaps, minimum gap 9719/249840, no negative gap, and precisely two ties: U=(10,2,2), actions Q/C; Z=(14,0,0), actions P/Q. The conditional suffix law is identical among ordered prefixes having the same counts, so the backward argument is also universal over arbitrary full-history randomized policies. Iterating the conditional Bellman inequality gives

    tP + K196*eQ + L196*eP >= H196.

Thus V14(alpha)>=H196-(K196+L196)*alpha for ALL real alpha because K,L>0, eP,eQ<=alpha, and max(tP,tQ)>=tP.

## Exact primal attaining continuum

Outside U,Z choose the unique Bellman-minimizing action. At U report Q with probability u, else continue; at Z report P with probability z, else Q. These choices cannot be in a common ancestor chain: U has two observed zeros but Z has no zero, and counts never decrease; Z is terminal, while U has depth 10. Hence the four observables O=(eP,eQ,tP,tQ) have an exact bilinear mixed coefficient identically zero and obey

    O(u,z)=B+u*DU+z*DZ,

where

    B = (
      309449599034352403/876488338465357824,
      56196541591091/160489808068608,
      1153307972138565565/109561042308169728,
      137455146584591/13374150672384)

    DU = (
      15859375/110075314176,
      -45390625/417942208512,
      -213828125/41278242816,
      -32265625/3869835264)

    DZ = (
      -6103515625/78364164096,
      6103515625/78364164096,
      0,0).

Solving eP=eQ gives

    z(u)=1524931934924453/81920000000000000+(259539/160000000)*u.

For every real u in [0,1], 0<z(0)<z(1)=1657815902924453/81920000000000000<1; both coins are valid. At u=0, this exact z equals the Stage195 terminal coin and yields eP=eQ=alpha195, tP=V195. At u=1 the output is eP=eQ=alpha196, tP=V196.

The common-error increment is Delta196>0; the tP increment is -213828125/41278242816<0 and the exact ratio of opposite increments is 506736/1735=K+L. The tP-tQ gap is positive at BOTH endpoints:

    u=0: 3030601257510677/12173449145352192;
    u=1: 3069039657510677/12173449145352192.

The gap is affine, so tP>tQ throughout. Every chosen action is Bellman-minimizing and saturates the dual bound. For any real delta in the specified interval set u=delta/Delta196, z=z(u). Therefore the displayed formula is the exact optimum for the WHOLE interval, not a finite grid.

## Strict right support

A full-history finite-horizon behavioral strategy belongs to a finite product of compact simplices; error and time functionals are continuous, so any nonempty alpha-feasible set admits a minimizer. Equality with the fixed line for alpha>alpha196 requires eP=eQ=alpha (positive K,L), max(tP,tQ)=tP, and equality in every positive-reach-probability Bellman action. Hence all strict-gap actions are forbidden and all non-tie actions must be the unique minimizer.

The 420 first-hit ordered U histories all have identical P and Q prefix mass (the same count state), and their IID optimal suffix laws agree. Averaging their potentially history-dependent U coins preserves the four requested observables. The sole Z history is terminal. U and Z cones are disjoint, so averaging also preserves joint behavior. Thus any equality policy reduces for this observer to O(u,z) for u,z in [0,1]. Equal errors force z=z(u), and then the common error is at most alpha196 (strictly increasing u). This contradicts alpha>alpha196. Compact attainment proves strictness, not merely nonattainment.

## Independent exact verification and BRC semantics

Actual local executed source: VERIFY_STAGE196_EXECUTED.py. Algorithm 1 uses Fraction-based Bellman and deterministic-corner suffix DP. Algorithm 2 independently traverses full unmerged ordered histories using P integer weights (3,1,20)/24 and Q weights (2,2,20)/24, scaling terminal contributions to denominator 24^14. All four deterministic corner observables agree EXACTLY. Per-corner DFS node counts at (u,z)=00/01/10/11: 132142/132142/123322/123322, total 510928. Each corner reaches U in 420 distinct ordered histories, Z in 1, with zero U/Z ancestral intersections. Executed output: STAGE196_AUTHOR_EXACT_FULL_REAL_PASS. Full rational certificate, original executed code and stdout are in the accompanying portable package; GitHub reference reproducibility code does not by itself establish remote execution.

BRC's adequate positive-rational carrier preserves ordered provenance, nonnegative branch multiplicity, and separate P/Q masses. The observer is exactly (eP,eQ,tP,tQ) at horizon 14 for this IID law and future observations. Count compression is certified only for these observables and future operations; not for arbitrary native X6 paths, phase/signed amplitudes, physical fields or infinite-scale effects.

## Stage197 new dual-only candidate

Saturate U=Q at the right endpoint, lower both K and L along (-1,-1). The U-continuation gap opens at positive rate 1735/186624. First closure step is 25191648/5692535 at W=(11,4,3), C/Q. The resulting exact dual values are

    K197=L197=464616/3281;
    H197=9895037491722567552173/89867444953276219392.

Fresh 680-state Bellman scan gives only W Q/C and Z P/Q ties, 1238 positive gaps, minimum positive gap 28229681/4898506752. Scan executed marker STAGE197_DUAL_SCAN_PASS. Stage197 primal all-real interval has **not** been proved. Next: compute W/Z corners via suffix DP plus independent ordered DFS; establish balanced legal coins, Stage196 contact, tP>=tQ, support equality and right-endpoint strictness; return exact rational obstruction if any condition fails.

## Permissions and claim strength

GitHub authenticated as awdawmip and can persist author materials. Native em_status returned research_authority_granted=false; em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active native owner and CLAIM are therefore unverified. A separately registered local research-activity record is not a Source session, formal CLAIM, frozen Result, independent review or mathematical admission. This is author-level portable evidence only.
