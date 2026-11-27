# Stage202 — complete exact all-real optimum for external N14 ternary IID

Status, 2026-10-27: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Scientific parent is Stage201 proof on Draft PR #1571 at commit feb4b102a0d8796cb47723baf6024cb640314c4d. GLOBAL_KNOWLEDGE_V1 pinned main@f4ef844a208d4774467436397c4ee4b0481b7ba6; Enterprise Math control-source main@d8b1a8272420500b67ddc04033ca9577f7c1f3f8; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc agrees with P000 startup projection.

## Exact model and theorem

Horizon N=14, observation alphabet {0,1,2}, IID probability vectors P=(3,1,20)/24, Q=(2,2,20)/24. Allow arbitrary randomized stopping/reporting rules on the entire ordered observation history. Define eP=P(report Q), eQ=Q(report P), tP=E_P T, tQ=E_Q T, and V14(alpha)=min_(eP,eQ<=alpha) max(tP,tQ).

Stage201 proved the contact alpha201=3705289910272792345/10517860061584293888 and V201=2265238509513884573/219122084616339456.

**Theorem (all real parameters).** For every real delta in [0,2316540625/3343537668096],

    V14(alpha201+delta) = V201 - (188727102/741293)*delta.

The endpoint is alpha202=3712577116979992345/10517860061584293888 and V202=2226587199024284573/219122084616339456. For all feasible alpha>alpha202, the *fixed Stage202 Bellman supporting line* lies strictly below V14(alpha). Strict-right support refers to this one line, not to all successor optimum segments.

## Dual lower bound, including arbitrary ordered histories

For a count state s=(n,a,b), a counts symbol 0 and b counts symbol 1. Every ordered prefix with this count has likelihood ratio Q/P=2^(a+b)/3^a and identical conditional IID suffix laws. Under P define the Bellman cost to report P as K*(Q/P), report Q as L, or continue as 1+sum_i P_i*h(child_i(s)), where continuation is available only if n<14.

For K=L=94363551/741293 the exact rational root value is

    H202=18568821153724089963922211/185638477110285856407552.

An exhaustive Fraction Bellman recursion over the complete 680 count states gives exactly 1238 strictly positive action gaps, smallest 16319029/1441073592. Exactly two tie states exist:

- B=(6,0,1): report Q versus continue.
- Z=(14,0,0): terminal report P versus report Q.

At all other states the Bellman-minimizing action is unique. Conditional backward induction applied separately to **each actual full ordered prefix**, not only to a count-state Markov rule, implies for any randomized history-dependent policy

    tP + K*eQ + L*eP >= H202.

Thus if both errors are at most alpha,

    V14(alpha) >= H202 - (188727102/741293)*alpha.

This is the precise universal lower bound. All finite count-state compression here is justified by the IID suffix observer and constant P/Q likelihood ratio on its fibers.

## Exact primal construction and BRC full-history check

At all states outside B and Z use the unique Bellman-minimal action. At B choose report Q with probability b and continue with 1-b. At Z choose report P with probability z and report Q with 1-z. Let O(b,z)=(eP,eQ,tP,tQ).

For each of (b,z) in {(0,0),(0,1),(1,0),(1,1)}, an exact Fraction suffix DP was checked against an independent full, unmerged **ordered-history** DFS using two integer path masses (P weights 3,1,20 and Q weights 2,2,20; terminal denominator 24^14). Every corner and each of four observer components matched. certificate202.json lists exact corner rational vectors. In particular,

    O00 = (
      627135530211198899/1752976676930715648,
      111321003395947/320979616137216,
      2265238509513884573/219122084616339456,
      267017230439735/26748301344768).

The affine differences are

    DB = (
       1101221875/185752092672,
      -3797228125/835884417024,
      -32765121875/185752092672,
      -20333265625/69657034752);

    DZ = (
      -6103515625/78364164096,
       6103515625/78364164096, 0, 0).

The mixed difference O11-O10-O01+O00 equals (0,0,0,0) **exactly**. This has a direct structural explanation: B has one observed type-1 symbol whereas Z has zero. Monotone counts mean B cannot precede Z, while Z is already terminal and cannot precede B. Hence neither randomized tie is an ancestor of the other, so their behavioral probability effects are disjoint. Accordingly O(b,z)=O00+b*DB+z*DZ for all real (b,z) in [0,1]^2.

Setting eP=eQ yields the **exact** balancing law

    z(b) =
        57523270994401049/819200000000000000
        + (3361047/50000000)*b.

The endpoint probabilities are z(0)=57523270994401049/819200000000000000 and z(1)=112590665042401049/819200000000000000, both strictly between 0 and 1. Every b in [0,1] is therefore legal. Along this arc the common error increases strictly and affinely from alpha201 to alpha202, by delta_alpha=2316540625/3343537668096.

Moreover, tP-tQ equals 77833357751575453/219122084616339456 at b=0 and 103144970269975453/219122084616339456 at b=1. Both are strictly positive; their affine interpolation remains positive throughout. The chosen actions have Bellman slack zero, so the primal gives max(tP,tQ)=tP=H202-K*(eP+eQ)=H202-2K*alpha. For **every real delta** in the theorem choose b=delta/delta_alpha and z=z(b). This constructs a legal policy exactly attaining the universal lower bound, proving the full-real identity including irrational values.

## Strict-right fixed supporting line

The randomized full-history behavioral strategy space of a finite horizon is a finite product of compact simplexes. Observer outputs are continuous; whenever constrained policies exist, the infimum is attained. Suppose alpha>alpha202 achieves equality V14(alpha)=H202-2K*alpha. The chain

    max(tP,tQ) >= tP >= H202-K*(eP+eQ) >= H202-2K*alpha

must have equality at every step: in particular eP=eQ=alpha (since K>0) and all P-positive reached prefixes have Bellman slack zero. At states other than B,Z, every minimizing action is unique. At B, every ordered prefix with this count has identical IID suffix distribution and the same likelihood ratio, so averaging coins across arrived histories has the same four-component observer as one effective b in [0,1]. Z is a single terminal all-type-2 prefix with coin z. Their tie cones are disjoint; all such zero-slack policies have four-vector O(b,z)=O00+b*DB+z*DZ.

The equal-error constraint forces z(b) above, and for legal b in [0,1] its common error cannot exceed alpha202. This contradicts eP=eQ=alpha>alpha202, so the fixed supporting line is strictly below the attained optimum beyond the endpoint.

## Exact execution evidence and scientific boundary

Executed local author checker verify_stage202.py using Fraction Bellman and an independently implemented positive-integer P/Q ordered DFS. DFS calls at the four corners: 98494, 98494, 96406, 96406 = **389800** total. Per corner: B first-arrival paths 6, Z first-arrival paths 1, joint visits zero. Every four-component observation agrees between the two algorithms. All exact dual gaps, endpoints, coin law, error equality and P-time dominance checked. Local stdout: STAGE202_AUTHOR_EXACT_PASS 389800. Separate exact Stage203 directional candidate scanner also executed: STAGE203_DUAL_SCAN_PASS. The GitHub REPRO_STAGE202.py script is a consumable executable reference and Git blob readback proves storage, not remote program execution. Raw original executed source and logs are retained in the run's accompanying local research bundle.

BRC type: retain ordered branch identity, multiplicity/provenance and separate **positive** P/Q integer-weight carrier; only then project to the four stated finite IID observer values. This does not encode signed/phase cancellation, native X6 residuals, three-dimensional slice dynamics, or P000 physical transfer. P000, independent review, current task ownership and Source Result admission remain separate.

## Stage203 next scientific question

A separate exact directional scan from the Stage202 b=1, z-policy found **dual-only** K203=L203=17496/139 and H203=188497771183924373447/1903623110104449024. Bellman ties: T=(13,6,4) Q/C and Z=(14,0,0) P/Q, 680 states, 1238 positive gaps, minimum 16319029/830103552. Stage203 primal matching has not yet been proved. The next independent unit is its four-corner full-history rational observations, possible mixed term, equal-error coin law, legal interval, P-time dominance and new all-real support theorem or exact obstruction. See NEXT_TASK_PACKET_203.md.
