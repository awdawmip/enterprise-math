# Stage157 — exact full-real N14 auxiliary optimum

Evidence class: AUTHOR exact rational computation-assisted proof, NOT native Source Result, CLAIM, independent Driver review, Lean, or P000-native transfer.

## Frozen authority and model

GLOBAL_KNOWLEDGE_V1 canonical-main pin: c98c19a23c5dca566b7fe42c933c00b39be93532. P000 STARTUP projection matches original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Enterprise Math initial main a49fa11820c4613a585bbbf3f4411a2c0ee40df3; Stage156 source read at immutable 1b668c2a75e973a38fbf999bb97f559a769cdc40. Portable research protocol read at source main.

This is an EXTERNAL auxiliary model: 14 iid ternary observations, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). The minimization ranges over EVERY complete ordered-history dependent randomized stop/decision policy. Observations: eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha.

## Exact theorem, entire real segment

With alpha156=7319074368089652265/21035720123168587776, V156=5285134543382516317/438244169232678912 and

  eta157=34752911724120248905/842080912250561737261056,

for ALL REAL 0<=delta<=eta157,

  V14(alpha156+delta)=V156-(6685200/10529)*delta.

The new exact endpoint is

  alpha157=763084945158127578305/2192919042319171190784,
  V157=3298586218925748578843/274114880289896398848.

The SAME supporting affine line is strictly below V14(alpha) for alpha>alpha157.

## Proof I: universal Bellman support

States s=(n,a,b), with a,b the first two symbol counts and n<=14, have likelihood ratio Q/P=2^(a+b)/3^a. Let k=3342600/10529 and, backwards from n=14, set

  H(s)=min{ k*Q/P(s) [decide P], k [decide Q],
            1+sum_i P_i H(child_i(s)) [continue if n<14] }.

The exact Fraction verifier evaluates all 680 count states, finds exactly TWO nontrivial action ties J=(10,2,0), P versus continue, and T=(14,0,0), P versus Q. All 1238 other nonminimal action gaps are positive; minimum 232231247/11789784576, and no negative gaps. H(root)=16797051003483763023587/72098013403919941632.

For an arbitrary ordered-history-dependent policy, the Bellman inequality gives

  H(root)<=tP+k*eP+k*eQ<=max(tP,tQ)+2*k*alpha.

This establishes V14(alpha)>=H(root)-(6685200/10529)*alpha WITHOUT imposing count-based policy restrictions. The previous Stage156 exact-ray result identifies k as the next dual closure; the above present full 680-state check independently validates the candidate.

## Proof II: branch-preserving exact observers

Preserve all ordered positive P/Q branch weights until an iid observer-specific quotient is justified. Under strict Bellman minimizers outside ties, exactly 45 distinct first-hit histories reach J with P mass 1953125/11943936 and Q mass 1953125/26873856. Exactly one first-hit history reaches T, the all-symbol-2 path, with identical P and Q mass 6103515625/78364164096. The two first-hit cones are disjoint: J includes two symbol-0 observations while the terminal T path contains zero.

Let j=probability of deciding P at J (otherwise continue) and x=probability of deciding P at T (otherwise Q). All other histories take strict minimizers. In the coordinate order (eP,eQ,tP,tQ) the observer vector is

  M(j,x)=M00+j*dJ+x*dT,

with

  M00=(1220395842171464035/3505953353861431296,
       223259694920365/641959232274432,
       5285134543382516317/438244169232678912,
       619867204468061/53496602689536),

  dJ=(-3201171875/3962711310336,
       771484375/557256278016,
       -30224609375/165112971264,
       -4150390625/46438023168),

  dT=(-6103515625/78364164096,
       6103515625/78364164096,0,0).

The four-corner mixed observer vector M11-M10-M01+M00 is (0,0,0,0), exactly. An exact-rational suffix recursion on the Bellman count DAG and separate unmerged integer likelihood-weight DFS agree independently for ALL four deterministic corners. The latter performs 465880+465880+464800+464800=1861360 ordered-node visits. Individual first-hit P/Q masses and all four observers agree.

## Proof III: primal attainment on all real alpha

The equality eP=eQ is equivalent EXACTLY to

  j(x)=660136987826389/4611571200000000
       -(25600000/360279)*x.

The entire feasible subset of the equality line in [0,1]^2 is

  0<=x<=660136987826389/327680000000000000.

At its left (x maximal) endpoint j=0 and (alpha,tP)=(alpha156,V156). At its right (x=0) endpoint j=660136987826389/4611571200000000, and (alpha,tP)=(alpha157,V157). Common error increases strictly affinely as x decreases by eta157. The two tP-tQ gaps are strictly positive:

  left  69060801460053535/146081389744226304;
  right 251826953459549368715/548229760579792797696.

Affine interpolation keeps tP>tQ throughout. Both endpoints satisfy the exact equality

  tP+k*(eP+eQ)=H(root).

Affineness gives the equality for EVERY REAL x within the interval, and all corresponding real alpha. Such randomized policies attain the universal dual lower bound. Therefore they achieve the exact global V14 formula and slope 2k=6685200/10529, not merely rational-grid interpolation.

## Proof IV: the right endpoint is sharp for the same support

The finite set of complete ordered histories yields a compact cube of behavioral randomized policies; all observers are continuous, so V14 is attained. Were equality to the same dual affine support achieved for alpha>alpha157, positivity k>0 would force eP=eQ=alpha, tP>=tQ and Bellman-minimizing actions at each reached positive-mass history. Strict positivity of the other 1238 gaps restricts randomization to J and T. At all distinct J ordered first-hit prefixes, the same iid suffix and same Q/P ratio allow the history-dependent J coins to be averaged to one effective j for EXACTLY the four stated observers; both measures induce the same relative first-hit weights for fixed counts. The T history is unique and the J and T cones are disjoint. Every equality-policy observer is therefore M(j,x) for j,x in [0,1]. Equality eP=eQ gives the displayed j(x), and its maximal common error is exactly alpha157 (x=0). This contradicts alpha>alpha157. Thus the same dual line is strict to the right.

## Evidence and boundary

Reproduction: VERIFY_STAGE157.py (Python standard library Fraction) writes certificate157.json. Checked: all 680 Bellman states; 1238 positive gaps; zero negative gaps; two specified ties; exact first-hit counts and masses; 4 deterministic corners cross-checked by two mathematically distinct author implementations; zero mixed difference; exact Stage156 left endpoint, Stage157 right endpoint, positive time dominance and dual equality. Local run completed with STAGE157_FULL_REAL_AUTHOR_PROOF_CHECK_PASS. Mathematical status AUTHOR exact; no independently activated reviewer or native CLAIМ, Result, Lean or source admission. The iid BRC order/provenance carrier is observer-specific and does not establish an X6 native update or remove phase/source residues.

Current authenticated GitHub user awdawmip; native task listing returned CONTROL_QUOTA; native researcher session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Real active native owner remains UNVERIFIED. Local research activity RA-R2-20261026T1142-B742E1 is bookkeeping, not an authorized CLAIM.

## Next scientific question (Stage158)

At alpha157, j is interior whereas T's P coin is at x=0. Scan the next exact dual deformation after k157=3342600/10529, preserving J's P/continue tie and making the terminal T action strictly Q. Find the first other Bellman gap closure (or prove the proposed one-dimensional ray cannot continue) and then determine complete-history primal attainability, the next all-real segment and its sharp right endpoint. Keep source/model and BRC/P000 type distinctions frozen.
