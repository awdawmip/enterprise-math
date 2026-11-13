# Stage254 — Exact adjacent Bellman contact region (external N=12 IID)

**2026-10-28. AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** External ternary IID auxiliary model, not a native P000-X6 heartbeat theorem. Parent: Stage253 research commit e4b91f62e61a43ad76c6fb7737e4936c6ef4e2a3, Draft PR #1571.

## Model, exact support, and theorem

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=12. Arbitrary full ordered-history randomized stopping/classification policies have four observers (eP,eQ,tP,tQ): eP=Pr_P(declare Q), eQ=Pr_Q(declare P), and expected stopping depths under P/Q. For real caps a,b in [0,1], V12(a,b) is the minimum of max(tP,tQ) with eP<=a and eQ<=b, or +infinity if infeasible.

The exact new one-sided Bellman support has equal error multipliers and time weights (1,0):

    K=1310563224/20009183
    H=204301839860512073/3629636342682624

Four-observer vectors (eP,eQ,tP,tQ):

    w=(969734737/2902376448,
       1932641711/4353564672,
       1932641711/362797056,
       1932641711/362797056)

    u=(17629541/6879707136,
      -58513051/11609505792,
       418652141/2579890176,
       13723291/107495424)

    v=(-244140625/2176782336,
        244140625/2176782336,
        0,0)

    D=u_eP*v_eQ-u_eQ*v_eP
     =-112356252197265625/404341874203444641792 < 0

Let R254 be the rational parallelogram of all cap pairs (a,b)=(w_eP,w_eQ)+x(u_eP,u_eQ)+y(v_eP,v_eQ) with real 0<=x,y<=1. R254 lies strictly inside [0,1]^2 and has positive area |D|.

**All-real maximal-contact theorem.** For every real cap pair (a,b) in [0,1]^2,

    V12(a,b)=H-K*(a+b)  IF AND ONLY IF  (a,b) belongs to R254.

This applies to all full ordered-history randomized policies, including irrational coins. R254 is an exact nonzero-area region adjacent to the Stage253 contact parallelogram R253, not merely a fit to finite numerical samples.

At the Stage253 feasible exterior point

    a*=195427979423/696570347520
    b*=43104161797/87071293440

both caps are strictly interior to R254. The exact global optimum is

    V12(a*,b*)=3186354511333424681/580741814829219840
              approximately 5.486697237860242.

The optimal randomized actions are A=(1,0,0): continue with x=6790947364/6903168135, otherwise declare P; B=(0,0,12): declare P with y=5752909748711/11505280225000, otherwise declare Q; elsewhere choose the unique Bellman-minimizing action. The four exact observers are

    eP=195427979423/696570347520
    eQ=43104161797/87071293440
    tP=3186354511333424681/580741814829219840
    tQ=9103920614225559569/1669632717634007040.

The previous Stage253 affine bound is strictly weaker here by the exact positive amount 229137734375/9679030247153664.

## Proof with all load-bearing obligations

**1. Four-observer full-history quotient.** At an ordered history h with counts s=(i,j,k), the positive source likelihood ratio is Q(h)/P(h)=L(s)=(2/3)^i*2^j. Aggregate P-weighted action flows over all histories with count s; corresponding Q flows are exactly L(s) times the P flows. Normalize the former to obtain a randomized count policy. IID successors propagate both source flows correctly, retaining exactly eP,eQ,tP,tQ and all future IID steps up to N=12. Conversely every count policy is a full-history policy. Thus the four-observer feasible sets coincide for this declared finite-IID scope. This does not imply preservation of native X6 histories or arbitrary future operations.

**2. Exact global Bellman certificate.** For fixed K>0, the P-normalized cost tP+K(eP+eQ) has value recurrence

    H(s)=min { K*L(s)  [declare P],
               K       [declare Q],
               1+sum_z P(z)*H(s+e_z) [continue if |s|<12] }.

At A=(1,0,0), P-stop cost is 2K/3 and continuation cost is

    418652141/322486272 + (15019129847/23219011584)*K.

Equality produces K=1310563224/20009183. Exact Fraction enumeration of ALL 455 count states verifies root value H above, precisely two ties A:(P,C) and B=(0,0,12):(P,Q), plus 817 strict positive alternative-action gaps. Consequently any full-history policy satisfies

    max(tP,tQ) >= tP >= H-K*(eP+eQ) >= H-K*(a+b).

**3. Two lawful coins and complete error-plane coverage.** At A continue with probability x and otherwise P; at B declare P with probability y and otherwise Q; elsewhere use the unique Bellman minimizer. A lies on histories beginning with symbol 0; B lies on the all-symbol-2 length-12 history, so no path visits both. Exact P/Q suffix recursions yield (eP,eQ,tP,tQ)=w+xu+yv for every real 0<=x,y<=1, without an xy interaction term. Since D!=0, every cap pair in R254 uniquely determines lawful coins and saturates both error caps.

**4. Time dominance including its equality edge.** Throughout the lawful two-coin square,

    tP-tQ = x * 89293157/2579890176 >= 0.

It is positive for x>0 and zero at x=0. Therefore max(tP,tQ)=tP, and the all-Bellman-minimizing strategy reaches H-K*(a+b), proving sufficiency everywhere in R254.

**5. Converse.** The finite ordered-history randomized policy space is compact; the cap-feasible subset is closed. Equality to the global affine lower bound forces both errors to saturate (K>0) and forces every reached positive-mass action to minimize the exact Bellman recurrence. Apply the proved source-labelled count reduction; the exhaustive action-tie list leaves exactly the legal two-coin family above. Therefore equality forces the cap pair into R254. Outside R254 any feasible cap pair has a strict positive gap from this affine bound by attained minimum, and an infeasible pair has V=+infinity. This establishes the if-and-only-if theorem over ALL real caps.

**6. Exact first adjacency.** Stage253's old W vector is

    W_OLD=(62539020775/185752092672,
           15285594535/34828517376,
           127456938773/23219011584,
           15831662545/2902376448).

Exact calculation gives w+u=W_OLD, and Stage253 and Stage254 share the identical v direction. Thus the entire x254=1 edge equals the x253=0 edge with matching y and all four observer coordinates. Along this edge S=eP+eQ=432186574885/557256278016, and the old/new affine Bellman supports agree. On R253 the total error is S minus 561103855/139314069504 times the old x, whereas on R254 it is S plus 460211209/185752092672 times (1-x). Hence R253 and R254 intersect in exactly this full shared edge and have disjoint interiors. In particular the new face is genuinely adjacent.

**7. Exact feasible witness beyond the NEW x=0 edge.** The formal invalid coins x=-1/100,y=1/2 give outside caps

    a_ext=15492478957579/55725627801600
    b_ext=580533802651/1160950579200.

These are strictly outside R254, but feasible: with probability eta=1427992821/15493906950400 immediately declare P at depth zero; otherwise use the lawful Stage254 coin policy x=0,y=1/2. This yields

    eP=a_ext
    eQ=15495334943221/30987813900800 < b_ext
    Q-cap slack=12137690822080267/2810571913771529011200
    tP=tQ=29941411040206974977669/5621143827543058022400.

Thus the next support transition is real, not an infeasibility artifact. Its exact optimum remains open for Stage255.

## Executed evidence and project boundary

Executed Python stdlib Fraction program STAGE254_EXACT_ADJACENT.py checks 455 Bellman states, 2 ties and 817 strictly positive gaps. Six separate unmerged ordered-history observer evaluations (four vertices, target, exterior mixture) visited 717 DFS nodes and 484 terminal branches, retaining P and Q positive masses separately, both total masses equal to 1, all four observers and stopping depths. Actual execution returned STAGE254_ADJACENT_EXACT_AUTHOR_PASS. The program and a selected stdout record are preserved beside this proof. Exploratory floating LP merely selected the candidate face; it is not a theorem premise.

Frozen verified input snapshots: GLOBAL_KNOWLEDGE_V1 main@84722f01d19471f6debb5cf2ebf615a6e5c1436f, Enterprise Math main@56566e4494d35ba3df4b645e0083a9d4cf05cb9d, Stage253 parent commit e4b91f62e61a43ad76c6fb7737e4936c6ef4e2a3. P000 ACTIVE and the six-native-X6 plus one time, three-dimensional-slice, source/joint-relation preservation and portable research contracts were read. BRC use is source-positive-mass observer preservation, not execution of native-heartbeat BRC software. At this read the native service reported research_authority_granted=false, upstream CODE_REVIEW_REQUIRED and active-job quota 5/5. No Source CLAIM, Result, independent Driver mathematical acceptance or X6 theorem transfer is represented.

**Next Stage255:** solve exactly the feasible (a_ext,b_ext) outside new R254, allowing both time weights and asymmetric error multipliers if mathematically needed; derive its next contact region, primal/dual certificates, ordered P/Q verification and a new successor packet.
