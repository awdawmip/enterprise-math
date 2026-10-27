# Stage198 — exact N14 ternary-IID full-real interval (author-level)
STATUS: PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM.

## Frozen sources and scope
Global canonical-main read: c8ee414d4fc77e812e9a272fbbbfe183abe39c1e; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc verified against P000_STARTUP projection. Enterprise Math read: main@4f9653b3b03cd94f69c6a914a02cf757ea06720f. Parent author proof: Stage197 immutable science commit 51f7dc0f789154da4894044754ce729af851c811. The mathematical statement is entirely for an external finite IID helper, not native X6/three-dimensional slice/physical heartbeat dynamics. Protected P000 and ACTIVE worldview are unchanged.

Independent observations in {0,1,2} under P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), stopping by time 14. Full ordered-history randomized stopping and decisions P/Q allowed. Let eP=P(report Q), eQ=Q(report P), tP=E_P T, tQ=E_Q T, V14(alpha)=min_{eP,eQ<=alpha} max(tP,tQ).

## Theorem
Let alpha197=1849166467986692153/5258930030792146944, V197=1152738894585765565/109561042308169728. For EVERY REAL delta in the closed interval
0 <= delta <= 1957556675/328683126924509184,
V14(alpha197+delta)=V197-(110347073712/391511335) delta.
New endpoint alpha198=1849166499307598953/5258930030792146944 and V198=1152738710673976045/109561042308169728. For alpha>alpha198 the *fixed* Stage198 supporting line H-(K+L)alpha is strictly below V14(alpha). No assertion about the next true piece beyond that endpoint.

## Dual inequality, all possible ordered-history policies
A counting state s=(n,a,b) counts observations 0 and 1; Q/P likelihood ratio is ell(s)=2^(a+b)/3^a. Set K=L=55173536856/391511335 and h(s)=min{K*ell(s), L, 1+sum_i P_i*h(child(s,i))} for n<14, terminal h=min{K*ell,L}. Exact Fraction Bellman induction over 680 states gives H=h(0,0,0)=1175588567905831666473706183/10723597484515752903966720. Exactly 1238 strictly positive action gaps have minimum 28229681/4698136020. The ONLY ties are A=(8,5,2) with actions P/continue and Z=(14,0,0) with actions P/Q. Given either hypothesis, IID suffix law is determined at every ordered prefix; induction applies to history-dependent actions. Thus for every allowed strategy:
tP+K*eQ+L*eP >= H,
hence V14(alpha) >= H-(K+L)*alpha.

## Attaining strategies and exact four-dimensional certificate
At all non-tied states use the unique Bellman action. At A report P with probability r and otherwise continue. At terminal Z report P with probability z and Q otherwise. A contains five zeros; Z contains zero zeros, hence A can never be an ancestor of Z. Z is terminal and cannot precede A. The randomization mixed term vanishes exactly, not approximately.

The exact observations O=(eP,eQ,tP,tQ) are O(r,z)=B+r*DA+z*DZ with
B=(309576157127952403/876488338465357824,56179076941091/160489808068608,1152738894585765565/109561042308169728,137343361034591/13374150672384);
DA=(-7741445/225434243432448,927865/20061226008576,-47302415/28179280429056,-1683065/1671768834048);
DZ=(-6103515625/78364164096,6103515625/78364164096,0,0); mixed=(0,0,0,0).

Solving eP=eQ exactly gives
z(r)=1658094956204453/81920000000000000-(2648916697/5120000000000000)*r.
For all REAL 0<=r<=1, 0<z(1)=1658052573537301/81920000000000000<z(0)=1658094956204453/81920000000000000<1. Both error rates are equal and increase linearly from alpha197 at r=0 to alpha198 at r=1. The time differences tP-tQ at endpoints are respectively 9207360330132031/36520347436056576 and 27622007379954413/109561042308169728, both positive; affine interpolation preserves strict positivity. For both endpoints and hence the whole interval, tP+K*eQ+L*eP=H. Choosing r=delta/(alpha198-alpha197) saturates the dual inequality for every real delta, proving the theorem.

## Strict-right boundary
In the finite 14-step history tree, randomized behavioral policies form a finite product of compact simplexes; risks are continuous and minima on nonempty feasible sets attained. Equality with H-(K+L)alpha would require max(tP,tQ)=tP and eP=eQ=alpha (K,L>0) and Bellman-minimizing actions at every positive-mass history. Non-ties are uniquely determined. At a tied count state every distinct ordered arrival has the same P/Q history mass and the same IID continuation law, so arbitrary history-specific coins can be averaged to a single r or z without changing the four observations. The two tie cones are not nested; all support-line equality strategies reduce to O(r,z), and balancing the two errors forces z=z(r). Its maximum shared error rate is alpha198. Therefore alpha>alpha198 cannot attain the same support line.

## Computation, BRC and remaining scope
Executed exact rational suffix DP and unmerged integer-weight ordered-history DFS agree at all four deterministic (r,z) corners. Ordered calls: 107482,107482,104410,104410; 423784 total. First-arrival ordered paths at A:32; at Z:1; intersection:0. The executed main checker printed STAGE198_AUTHOR_EXACT_FULL_REAL_PASS. A second non-importing reference implementation printed STAGE198_INDEPENDENT_EXACT_PASS 423784 ordered DFS nodes. The exact reference script and certificate accompany this source; full executed originals, logs, Stage199 scanner, and SHA256 manifest are in conversation artifact EM_STAGE198_AUTHOR_EXACT_PORTABLE_20261027.tar.xz.

The BRC observer retains ordered path provenance, integer multiplicity, positive P branch weights (3,1,20), positive Q weights (2,2,20) and terminal denominator 24^14. These masses are not signed/phase-cancelling amplitudes. Count compression is proven sufficient for the declared finite IID Bellman observer only, not for hidden native residual dynamics or unlimited future operations.

Stage199 DUAL candidate only: K=L=213288424/1523041; H=13641932749948792109334011/125149469578557848027136; ties (7,0,1) Q/C and (14,0,0) P/Q; original all-real interval remains unproved. Native em_status v0.6.11 reported research_authority_granted=false; the attempted em_control_tasks reported CONTROL_QUOTA. Active owner not authoritatively confirmed. No native CLAIM/Result/independent Driver admission.