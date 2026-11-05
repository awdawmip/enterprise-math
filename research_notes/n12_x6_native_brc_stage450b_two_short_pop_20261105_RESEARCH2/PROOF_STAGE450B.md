# Stage450-B — exact future quotient for P: two POP, Q: one POP

Date: 2026-11-05. Status: AUTHOR-SIDE PROOF / EXECUTED EXACT INTEGER TESTS / UNREVIEWED / NOT ADMITTED.

Parent: Stage449-B at commit f7418907ccb99a80334e6ef66602522219b910e8; scientific input pins unchanged from parent: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative routing read separately under RESEARCH_CONTINUATION_PROTOCOL. Native X6 signed six-axis primitive directions are D={+E1,-E1,...,+E6,-E6}; the initial A/B restriction is a family within X6, not a different native space.

## Definitions and exact hypothesis

3<=m<n. Ordered original words P,Q have lengths m,n. All original letters are A=+E1 or B=-E1, both initial and final letters are A, B defects occur only internally and never consecutively. Defect counts kP,kQ and the entire initial observer O=(m,n,Vp,Vq,Jp,Jq,K) are fixed, where V are signed six-component endpoints, J are complete directed native-adjacency histograms, and K is positionwise equality count in the overlap. Equivalently d=m-K is fixed once m,n,kP,kQ are fixed.

The future operation language allows P up to TWO POP and r>=0 APPEND, Q up to ONE POP and any nonnegative number of APPEND; allowed legal interleavings are arbitrary. APPEND labels range over all 12 native directions. Equal future traces mean equal full observers after each identically labelled legal action prefix. Any POP of an appended letter consumes the same source's POP budget. Initial m>=3 makes all original POP operations legal.

## Theorem 450.1 — exact minimal future repair

Set h=min(n-1,m+r) and use one-based original indices. Define

R450(P,Q)=(P_(m-2),P_(m-1),Q_(n-1), Q_(m-1),Q_m,...,Q_h),

with repeated Q slots recorded only once. For any two original histories H,H' within one O-fiber:

H ~ H'  if and only if  R450(H)=R450(H').

**Sufficiency.** An original P POP first removes edge (P_(m-1),A); a second original P POP removes (P_(m-2),P_(m-1)). The original Q POP removes (Q_(n-1),A). Every other POP deletes an edge whose appended direction is in the labelled future; every APPEND adds a labelled edge. Thus all V and J updates follow from O,R450 and the operations. Original overlap matches removed at indices m and m-1 have values [A=Q_m] and [P_(m-1)=Q_(m-1)] respectively. After P APPEND, the newly compared original Q slots are m+1 through at most h (or Q_n=A, known); a Q original POP can only replace its terminal original A by a labelled future letter. All other compared letters belong to known original P slots, the key, or labelled APPEND history. Consequently K too is determined after every legal prefix, proving full observer descent through R450.

**Necessity.** Differing P_(m-1) gives a differing J edge after the first P POP. With this slot equal, differing P_(m-2) gives a differing J edge after two P POP. Differing Q_(n-1) gives a differing Q edge after one Q POP. With the P pair equal, differing Q_m and Q_(m-1) respectively give different K losses after one or two P POPs. For each m<i<=h, keep Q unchanged and APPEND i-m native letters to P, choosing the last one A: the final K increment is [Q_i=A]. For a first differing window letter all previous increments agree; hence the two future traces differ. These cases cover every differing key. This is a fibrewise characterization: some coordinates may be fixed on a particular O-fiber, automatically reducing its supported key set. QED.

## Theorem 450.2 — polynomial exact support and BRC population

Write alpha=P_(m-2), beta=P_(m-1), gamma=Q_(n-1), qprev=Q_(m-1). Let the word w=Q_m...Q_h have first letter q0, last letter v, and s B letters, with ell=h-m.

Define T(alpha,beta,qprev,b,e) as the number of legal paired prefixes through position m-1: P has exactly kP defects; Q has b defects, e position mismatches, P predecessor pair alpha,beta and Q last direction qprev. The original P_m=A and the prescribed q0 add exactly q0 to the mismatch count.

Define W(qprev,q0,s,v) as the number of legal distinct words w of length ell+1 with q0 first, v last, s B's, and no consecutive B including the boundary qprev. Define U(v,gamma,R) as the number of legal Q completions at h+1,...,n with R B's, Q_n=A and Q_(n-1)=gamma (including the boundary with v).

For each exact key (alpha,beta,gamma,qprev,w), its integer population is

M(alpha,beta,gamma,qprev,w)
 = sum_b T(alpha,beta,qprev,b,d-q0) U(v,gamma,kQ-b-s).

This is a bijective split into prefix / visible window / completion. M depends on w only via (q0,s,v), qprev and the other three key bits. Hence the exact number of supported future classes is

qF = sum_(alpha,beta,gamma,qprev,q0,s,v) W(qprev,q0,s,v) [M>0].

The total original historical population is sum W*M. Computing T,W,U and these sums uses exact nonnegative integer arithmetic, preserving both Boolean support and multiplicity. The dynamic programming implementation gives a conservative polynomial bound O(n*(H+(kQ+1)^2+n)) integer arithmetic operations, where H=8(kP+1)(kQ+1)(d+1), n=max(m,n). Integers have O(m+n) bits since the history count is <=2^(m+n). Memory is polynomial. Full original history I/O costs Omega(m+n).

For implicit class lexicographic rank/unrank, fix the bits of (alpha,beta,gamma,qprev,w) from left to right. A prefix-conditioned W recurrence returns the exact number of supported completions by (q0,s,v), retaining T,U. Counting 0-branch support before a 1-branch yields the rank; inverse branch selection yields unrank. This uses O(n) support-oracle calls, each polynomial. To recover an original (P,Q) within a class, condition T and U on successive original bits and use exact integer population counts in lexicographic arithmetic coding. The companion full local verifier additionally exercised this construction (80 history pairs and 6076 class ranks), while the published portable checker concentrates on theorem and population checks.

## Executed verification

The accompanying Python standard-library executable reproduces the following exact results: full 12-direction future signature checks across 5 families, 11 full-O fibers, 40 histories, 74 history pairs and 40,560 cached future states. Exact transfer-vs-direct-history checks: 1,708 parameter/fiber instances, 15,804 histories and 6,076 population/class checks. Larger (m,n,kP,kQ,d,r)=(64,80,15,17,1,12): |F|=5,061,384,194,832,966 and qF=1,046, from 9,168 prefix DP transitions. The fixed class index uses ceil(log2(1046))=11 bits. The printed evidence JSON contains actual local execution output; it is not a native Source Result or Driver acceptance.

BRC carrier: original ordered pair and joint observer O; repair key is Boolean support-class identity, M gives exact positive integer population; class internal ordering retains provenance needed for reconstruction. The quotient is certified for the declared operation language, not substituted for the raw path before reconstruction.

## Next open problem

Stage451-B: investigate P and Q each with up to two POPs, full 12-direction APPEND and arbitrary interleavings. Test whether adding Q_(n-2) and a possibly shifted shorter-source alignment window makes a sufficient and necessary repair. Supply independent full-future distinguishing witnesses for all proposed coordinates, exact integer support/population recurrences, and a complexity account. Preserve the existing P000/science pins and native ownership/admission boundaries.
