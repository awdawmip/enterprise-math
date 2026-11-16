# R5: exact two-stage seedless-LR observation hexagon and its largest centered square

Date: 2026-11-06 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen scientific inputs and model scope

Keep the existing task's scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. The exact strictly-positive four-stage P/Q experiment has delta=1/4. Reuse the previously verified stop-mass/likelihood-ratio conventions in EM 57f7d654e5dd002567e0b0d333937e6e38f3b4cb and the immediate predecessor EM 912ad9184613cf615ca3a73bb40129c1e6f8ba6f. This is an exact finite BRC branch/observer calculation, typed as an external P/Q probability test, not native six-dimensional geometry.

For stopped likelihood-ratio key r=dP/dQ, M_r is its stopped Q mass and t_r the shared seedless-LR probability of declaring P. The error and time observers are

    e_Q = sum_r M_r t_r,
    e_P = 1 - sum_r r M_r t_r,
    T_Q = E_Q[tau],  T_P = E_P[tau].

Observer scope is these four coordinates and the two-stage stopping/declaration subfamily. Full stopped-ratio masses are retained. This projection does not assert equivalence under later operations on hidden histories.

## Exact two-stage LR construction

Set time-1 continuation probability to g=7/8 and stop at time 2 on either history (u_0=u_1=0; all later continued masses vanish). The P/Q time-2 branch ratios from the frozen tree are 3/4 and 5/4, each with conditional Q probability 1/2. Thus stopped Q masses are exactly:

    ratio r:       3/4      1       5/4
    mass M_r:      7/16     1/8     7/16.

Both total mass and the first LR moment equal 1; T_Q=T_P=1+7/8=15/8.

**Theorem 1 (entire exact hexagon).** All genuine seedless-LR policies of this fixed stopping family, allowing its three shared declaration probabilities to vary independently in [0,1], have exactly the following error image on the time fiber T_P=T_Q=15/8:

    H = {(e_P,e_Q) in R^2 :
         3 <= 4 e_P + 3 e_Q <= 4,
         4 <= 4 e_P + 5 e_Q <= 5,
         57/64 <= e_P + e_Q <= 71/64}.

The six counterclockwise vertices are

    (0,1), (21/64,9/16), (29/64,7/16),
    (1,0), (43/64,7/16), (35/64,9/16).

**Proof.** The cube t=(t_3/4,t_1,t_5/4) in [0,1]^3 maps affinely to the error pair. Its image is the convex hull of the eight deterministic t in {0,1}^3. Exact substitution yields the six vertices listed; the remaining two points lie inside the convex hull. The six edge equations give the three displayed double inequalities. Hence their intersection is the complete image for all real declaration probabilities.

**Theorem 2 (sharp centered square).** Every real pair

    e_P = 1/2+c, e_Q = 1/2+d,
    |c| <= h, |d| <= h, h = 7/128 = 0.0546875

is in H and thus in O4(seedless LR) and O4(FULL_HIST) of the frozen four-stage model. This is the largest centered axis-aligned square within this exact two-stage subfamily.

**Universal explicit inverse.** For every real c,d in the square set

    t_3/4 = 1/2 + (32/7)(c+d),
    t_1   = 1/2 + 8d,
    t_5/4 = 1/2 - (32/7)(c+d).

As |c+d| <= 7/64, the outer probabilities are in [0,1]; t_1 is in [1/16,15/16]. Substitution gives e_Q=1/2+d and e_P=1/2+c. All repeated stopped-ratio occurrences share one declaration probability (in this policy the time-1 key is 1; time-2 keys are 3/4,5/4).

**Sharpness within the family.** The exact identity

    e_P + e_Q - 1 = (7/64)(t_3/4-t_5/4)

gives |e_P+e_Q-1|<=7/64. A centered square of half-side h' contains its top-right corner with e_P+e_Q-1=2h'; therefore h'<=7/128. Our inverse attains equality.

## Relation to the verified frontier

The immediate predecessor's sharp fixed-flow/two-extreme-key subfamily had h_old=287903/10672000. The new family changes stopping-flow regime and uses keys 3/4, 1, 5/4. Its larger square has exact enlargement factor

    (7/128)/(287903/10672000) = 83375/41129 > 2.

This preserves the predecessor's optimality assertion in its own restricted model. The new deliverable includes the complete 6-vertex hexagon and a real-valued explicit inverse.

## Verification, evidence and status

Python standard-library fractions.Fraction code in VERIFY.py was executed. EXACT_OUTPUT.txt contains real stdout from 8 deterministic decision vectors, 1089 rational target grid checks, exact P/Q normalization, times, polygon vertices and factor. Analytic identities above prove universal real-square coverage and sharpness in the selected stopping family. No independent mathematical review/admission has occurred.

GitHub account observed: awdawmip. Native session request r5s11-20261106-144132-session returned FAILED/Error; task inventory request r5s11-20261106-144132-tasks showed WAITING_RESOURCE/EVENT_COLLECTION_IO. Formal R5 owner/CLAIM remains unconfirmed; this note is an independent author-side research artifact.

## Next discriminating unit

At fixed T_P=T_Q=15/8, search for an exact rational FULL_HIST observation outside this two-stage hexagon and test it against *all* four-stage seedless-LR flows via full seven-variable K(W) and its quadratic residual. A point outside the two-stage family is only a subfamily-separation witness; global image separation requires a global LR infeasibility certificate. Frozen scientific pins, source exposure history and the formal owner/claim boundary remain unchanged.
