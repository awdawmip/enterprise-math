# Stage255 — Exact Bellman support across Stage254 x=0/equal-time edge

Parent evidence: Stage254 exact author proof and Fraction checker in existing Enterprise Math Draft PR #1571; the predecessor Stage253 is already complete in that same branch. Do not reprove either result merely to resume.

**Question.** With P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12, arbitrary full-history randomized stopping/classification, minimize max(tP,tQ) for separate errors eP<=a and eQ<=b. At exact caps

    a=15492478957579/55725627801600
    b=580533802651/1160950579200

Stage254 proves this point is strictly outside its maximal affine contact region R254 (formal x=-1/100,y=1/2) but FEASIBLE. Witness: with probability eta=1427992821/15493906950400 immediately declare P; otherwise follow the Stage254 x=0,y=1/2 policy. Exact eP=a, eQ=15495334943221/30987813900800<b, both stopping times equal. Exact V12(a,b) is not yet established.

**Hard output.** Find a matching rational policy and a *globally valid* Bellman dual with thetaP,thetaQ>=0, thetaP+thetaQ=1 and lambdaP,lambdaQ>=0:

    H(s)=min {lambdaQ*L(s), lambdaP,
              thetaP+thetaQ*L(s)+sum_z P_z H(s+e_z)}.

Enumerate/check all 455 states, all ties and positive gaps exactly. Give rational four-observer primal values, prove both caps and max-time support, confirm exact primal/dual equality, and independently check unmerged ordered P/Q source masses and decision/stopping depth. Prefer the full adjacent all-real region. The Stage254 x=0 boundary has tP=tQ so an interior theta is plausible but unproven; do not assume it.

**Research scope/authority.** This is external IID error-parameter geometry, not a native P000 plane; the only proved sufficient quotient is for the four declared IID observers and future IID steps to N=12. Preserve BRC positive sources and P000/ACTIVE terminology. Current native research_authority_granted=false, source CODE_REVIEW_REQUIRED; read current owner/authority before formal transition. Publication to the PR is author provenance, not a native CLAIM/Result/Driver acceptance. Keep frozen source pins and publish exact verification and next question to the same PR.
