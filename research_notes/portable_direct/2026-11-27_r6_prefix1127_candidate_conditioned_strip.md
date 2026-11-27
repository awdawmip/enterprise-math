# PREFIX-1127 -- Candidate-conditioned BRC strip exclusion

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / CONDITIONAL_STAGE46_APPLICATION / NOT_REVIEWED.
Researcher EM-DIRECT-780BBE / TASK_RESEARCH; same activity RA-0ABD84561C86E53067DB0322. Original own registration r6-20261123-2358-session-start-own-v1 re-read SUCCEEDED. Owner request r6-20261127-1354-leased-observe SUCCEEDED/error=null, as_of 2026-11-27T05:54:53.177884Z, Source dc686c247bdc0dab857eca322648ec2231e30cb3, LEASED tasks=[] and next_cursor=null. No new claim or shared Task mutation.

## Inputs and scope

Continue PREFIX-1126 at 32bf421acedb4bed2737e0ed1cca9661bc2ee7a5:research_notes/portable_direct/2026-11-27_r6_prefix1126_anchor_recovery_joint_certificate.md. Reuse compact signed shared anchor at 843db46cfabef3bc3e62a266ba11d1be224291ba:research_notes/portable_direct/2026-11-27_r6_prefix1126_anchor_compact.json (SHA256 90d2891844e2db432af6efb66be7325f914f1934ad553d7d6e61cf9182cc88ff). Reuse original 8800 jets at 897771dcc60212121f1e222bf139da189cce0078:research_notes/portable_direct/2026-11-27_r6_prefix1117_root_8800_result.json. Frozen P000 V5, joint observer, X6/time and residual fidelity read at f42f2906d77f24085c123f3ccfe9667d41caa96d; current account canonical entry blobs verified at 1a96733e514890ce6222a05f692659b2f280ed4f. Preserve signed reversal -5, 5q cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Scalar spectral readouts and integer relation coordinates are auxiliary observers of the inherited signed X6 carrier, not new native spatial axes or time. No classical reference calculation or new native CT enumeration. Inherited carrier correspondence, root isolation, boundary theorem, and 8400/8800 command-exit uncertainty remain conditions.

## 1. A fixed signed observer strip for candidate families

Write f(m)=rho*m+c+d/m and |f(m)-j|<=E/m^2, E=400000. For two such observations in [L,2L), qj-pm=h is the primitive line with gcd(p,q)=1, q>0. The signed pair bounds from PREFIX-1123 and the inherited exclusion of q<q0=544447235321021556325566186117974922693 imply, for every L>=L0=10^90, rho in [p/q,p/q+K/L0^2], c in [h/q-H/L0,h/q], where K=d_u+2E/q0 and H=2d_u+4E/q0. In particular these bounds apply to all later windows at once. Intersect these intervals with the frozen 9600 rho,c boxes. From rho=36/t_*^2-1 obtain an enclosing candidate root interval J by monotone inversion and exact outward integer square root; intersect J with the certified root interval T.

Let F(t_*)=0, F'(T) contained in A<0 and c=alpha(t_*)+beta(t_*) F''(t_*)/F'(t_*), as in PREFIX-1124. Put G(t)=beta(t)F''(t)+(alpha(t)-c0)F'(t). Here c0 is the midpoint of the frozen c box. Then G(t_*)=(c-c0)F'(t_*). For a fixed rational x in T, the shared anchor gives (F(x),G(x)) in (f,g)+sum_j [-1,1](u_j,v_j), with signed common anchor columns, coefficient representation and point/tail payments all included. For any fixed rational s put Q_s=G-sF. Its point enclosure is B_s=[g-sf-W_s,g-sf+W_s], W_s=sum_j |v_j-su_j|. A derivative interval D_s containing G'(T)-sF'(T) is computed using the frozen jets and product rule. The mean-value theorem proves the necessary condition

    (B_s + (J-x)*D_s) intersects ((C_candidate-c0)*A).

If the intervals are disjoint, that entire primitive integer line is excluded for all L>=L0. All interval products here are enclosing products; no independence of the true F,G or anchor columns is asserted. The same reference x and signed column s work for many different candidates. This extends the root-conditioned support method of PREFIX-1125 by conditioning on the candidate slope and intercept simultaneously, not merely optimizing unconditional marginal parameter widths. The proof only needs a strict separating direction, not optimality of a numerical optimizer. A remaining candidate is not an existence certificate.

## 2. First actual exclusion of the previous sharp independent-box witness

At the old minimal q,p,h of PREFIX-1126, set c0=h/q and restrict the root interval as above. Recompute the shared F,G point columns at its midpoint using the saved N=300 basis reconstruction and compact anchor. Transfer along the common displacement with a shared mean derivative column and two explicitly paid axis radii: for delta in [-r,r], derivative intervals A and D, use (r*mid(A),r*mid(D)) and axis payments r*rad(A), r*rad(D). This contains the exact integrated derivative pair. Slice the resulting zonotope at F=0 with the finite support slopes v_j/u_j (plus 0). The resulting G interval lies in [-9.178784634e-81,-8.587964193e-81] (display approximations, exact endpoints in candidate_joint_result.json), while required G is nonnegative because c<=h/q and F'<0. The previous minimal line is strictly excluded. It had an exact substitute-parameter witness inside the independent boxes, so this is a genuine use of previously unconsumed joint anchor information, without any new anchor precision.

## 3. Actual batch exclusion from the same frozen compact anchor

Use x=mid(T) (exact rational), c0=mid(C). Reconstruct six signed Frobenius observation polynomials, evaluate F,G with the inherited 10^180 directed Horner grid and product-rule tails. Retain the original six shared weighted anchor columns and six rounding columns. Round centers and columns down at 10^-180 and pay the absolute rounding error in two axis columns. No anchor moments or inverse matrix recomputed. Derivative interval uses the same frozen 8800 first/second/third jets with alpha,beta and their derivatives evaluated on T. Use s equal to the slope v_1/u_1 of the dominant shared anchor column; it is approximately -23.26976977956. This cancellation is exact for that point column. All 588 exclusions already follow from that one direction. Full raw inputs, joint column values and per-line rational margins are in batch_joint_result.json (local evidence archive).

For a small standalone certificate use s=-11634884889781635619562764508733/500000000000000000000000000000. Direct outward comparison against the actual computed columns and derivative rectangle verifies:

    B_s = [-29563782680394916876739371429,29518261340403151337066718651]/10^110;
    D_s = [1627485539561293395435538730916079508360030,1627485539561293395435538730916079508360031]/10^30;
    A   = [-9569233600936582651958077026760045106905,-9569233600936582651958077026760045106904]/10^30.

The compact certificate and exact R,C,T,d,x,c0 inputs are embedded in prefix1127_verify.py, published as 5de6c6fc91b7dbf9679b5665047f8f168c5d959b:research_notes/portable_direct/2026-11-27_r6_prefix1127_joint_strip_verify.py. It is an independent finite exclusion checker given the BRC-derived enclosures; reconstruction of those enclosures is supplied by candidate_joint.py and batch_joint.py. The latter two use the prior execution archive files with the original basenames.

For q0<=q<=Q=2*10^59 use the unimodular V from PREFIX-1126. The transformed integer ranges are [-5,4],[-33,31],[-30,12]; each range encloses all q*(a+b*(p/q)+c*(h/q)) by multiaffine corner evaluation on the allowed intervals. Original scan uses 430 coordinate pairs with exact third-coordinate bounds; independent pure-Python checker enumerates all 27950 points in the enclosing integer box and filters original inequalities. Both recover 595 primitive integer lines, 295 strictly below required G interval, 293 strictly above, 7 remaining. Every one of the 588 excluded lines has strict separation >4.652e-81 even with compact outward rounding. No random sampling, no reliance on LLL optimality. All three executions completed exit 0. Minimum remaining denominator is

    q_new=103227297686501849015849101643201302351892157120286900838987.

The associated p,h are 2213197052946740996166259278782039385919137025347310577185541 and 10234058597391047904845116101931309635401605626827898293341334. All seven lines are printed by the standalone verifier and retained in the raw batch result. Since q_new<Q, excluded q below q0 by inherited theorem and above Q already larger, every true pair in every [L,2L) with L>=10^90 has b-a>=q>=q_new. This improves the prior lower bound by about 15.10058547. Use sharp curvature q^2<4EL/d from PREFIX-1121 and previous smaller-window exclusion to obtain first not-excluded dyadic triple window

    L3=114674930799503575580541044765104347039828249458414056186879441969346143804424240403500927655506284327731200000000

and first not-excluded dyadic square-root-gap pair window

    L2=15030672529752532658492675819451756975204368313013247172526662217806137760733494038167673589662519699404383846400000000.

These are approximately 1.146749308e113 and 1.503067253e118, each 256 times the prior dyadic boundary. They are exclusion bounds, not newly established sharpness or actual occurrence. The single endpoint ambiguity from PREFIX-1126 remains; continuous integer endpoint certification still ends just before m=47247757565973207955345875119021762026915609.

## 4. Reproduction and evidence

The three exact executed programs are published at: 8a9c2449673d8a949cd8566980a11703b84c22ce:research_notes/portable_direct/2026-11-27_r6_prefix1127_candidate_joint.py; d9b7611b6851cc9fc76c323ab63e8bd0be29c333:research_notes/portable_direct/2026-11-27_r6_prefix1127_batch_joint.py; verifier above. Each remote blob was matched to the actual local executed file. The actual complete execution evidence archive PREFIX-1127-execution-evidence.zip retains these programs, prior needed frozen inputs, exact raw result JSON, independent output and checksums. Local archive is distinguished from remote publication. File SHA256:

- candidate_joint.py 39f16200aa45d0cfff55d65962db6c45dfd92c2440f59af565328f9902dd7b14
- batch_joint.py 321477a1c415137fba549585c4a86a75405883d1cd2fc2b04b7e408428e95eff
- candidate_joint_result.json ed8f4c4196d82939e0d2b34216cd996be8230b4e58c2216cc34b5bf0add2eabf
- batch_joint_result.json d450c82e81912f6bbf8d386550c0eb844bf242d00328955891d5901eea4b7a99
- prefix1127_verify.py 20ae084c4f4c8adb38ee38d2ab50e615d2a29352a0a259b3dbf90c9df916c9b0
- prefix1127_verify.log 984a87683dbd87a7bc6aa51cd34b497646c411432499193b5a246f4df9e31ef9

Run python candidate_joint.py, python batch_joint.py, python prefix1127_verify.py from the evidence directory. The first two use SymPy and previous frozen signed-basis reconstruction; the final checker uses only the standard library. No new high-order anchor, no new native CT enumeration. Independent mathematical review and Activity observation audit remain pending.

## Next

The seven surviving lines may be tested by conditioning additional shared anchor/jet directions, in particular the first surviving line. Determine the information limit of the full joint relaxation instead of merely the independent parameter boxes. The single endpoint ambiguity and unbounded single-anomaly separation remain open; do not redo the 9600 anchor. Mother B_fix,odd(32) and exact zero remain open.
