# RP7: signed family projection, block resampling, and an antipodal obstruction

Progress-Event-ID: RP7-C971348E-SIGNED-BLOCK-01
Date: 2026-09-27 Asia/Taipei
Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED / NOT_EXECUTED
Global read snapshot: 60bd7d5591e518cef2c7df6098530c059b95690e
EM intake: b782ba42244dd87f00d69d056691985c0b64a957
Semantic predecessor: RP6 scientific source 4c5707594ae41d184cbb3374b0fb19d43e09f27b; published note c2870c60795a682666f6670f5abc0d2c5cd64883, research_notes/HEARTBEAT_RP6_VALUE_FAMILIES_4C570759_20260927.md.

This is a new proof manuscript, not an executed RP7 implementation or a new benchmark. Container, private Python and visible Python calls all returned ClientError before producing results. No RP6 package rehash, new core receipt, simulation, timing, ZIP or local source validation is claimed. The actual attached RP6_Proof.md was read through Files. Its inherited quadratic-norm and ordered-instrument contracts are hypotheses here, not newly independently verified facts. P000 and the BRC-only constraint are unchanged. The proof uses the inherited signed BRC linear extension and its quadratic identities; it introduces no trigonometric or ideal-QFT reference calculation.

## 1. Target and signed projection

Fix the declared real 61-mode BRC bank and its normalized, norm-preserving actual feedback T_h. For a history h, the raw child field is

    a_hb(w) = [u_h(w) + (-1)^b T_h u_h(P_i^-1 w)] / 2.

Its exact dyadic scales, all signs, labels and temporal order are retained. The two children together preserve the squared norm. At each nonterminal boundary choose a deterministic disjoint partition of the carrier into finite blocks C. The partition and signs may depend on the complete raw child as a mathematical function of h,b, but must NOT depend on the private sampled label or query order. Any cost of finding that partition is charged. A locally computable fixed-block specialization is given below.

Let m=|C|, choose signs sigma_w in {+1,-1}, and define

    mu_C = (1/m) sum_(w in C) sigma_w a_hb(w),
    (Pi a)(w) = sigma_w mu_C.

For a chosen partition/sign pattern, Pi is an orthogonal projection in the inherited quadratic-norm algebra. This is algebraic state-space orthogonality, not a redefinition of the native spatial angle. Require m to be a power of two when using only the current dyadic carrier.

Put A_C=sum_C ||a(w)||^2, B_C=m||mu_C||^2, and L_C=A_C-B_C. Expanding the signed sums gives

    L_C = sum_C ||a(w)-sigma_w mu_C||^2 >= 0.

Thus every work-label identity remains in the representation; only the within-block detail is approximated. It is not a lossless codec of those omitted details. A mean can increase an individual row norm even while the block norm decreases.

Apply the original toward-zero row quantizer to the shared mean:

    q_C=Q_K(mu_C),   u_hb(w)=sigma_w q_C.

Singletons use Q_K directly. Terminal children are neither projected nor quantized. This defines a NEW approximate target, not RP6 exact sharing and not a permitted relocation of Q across temporal boundaries. Projection followed by Q occurs at the same declared nonterminal boundary. Q is odd, so the resulting field remains in the range of Pi. For a nonzero block, a relative projection budget L_C<=beta_i A_C with beta_i<1 prevents a zero mean. The inherited quantizer preserves a nonzero row's largest coordinate.

## 2. Orthogonal error accounting survives individual row growth

Let A be a full raw child, X=Pi A, Y=Q_K X with the shared-value implementation above. The residual A-X is orthogonal to the projection range, and X-Y lies in that range. Consequently

    ||A-Y||^2 = ||A-X||^2 + ||X-Y||^2.

The inherited toward-zero quantizer obeys ||X-Y||<=rho_i||X|| and ||Y||<=||X||, with rho_i=8*2^(1-K_i). Coordinatewise magnitude decrease applies to X->Y, not to A->Y. It implies

    ||A-Y||^2 <= ||A||^2-||Y||^2.

If each block has L_C/A_C<=beta_i, and rho_i<1, then

    ||A-Y||^2 <= tau_i^2 ||A||^2,
    tau_i^2 = beta_i + rho_i^2(1-beta_i),
    ||Y||^2 >= (1-rho_i)^2(1-beta_i)||A||^2.

The quadratic combination is tighter than simply adding sqrt(beta_i) and rho_i. These facts also hold for partitions selected from A: they are pointwise projection identities, and require no false assertion that the adaptive projection map is globally Lipschitz.

For pairs x,y, choose sigma=+1 when J(x,y)>=0, else -1, with a deterministic zero tie. Then

    mu=(x+sigma*y)/2, d=(x-sigma*y)/2,
    x=mu+d, y=sigma*(mu-d),
    ||x||^2+||y||^2 = 2||mu||^2+2||d||^2,
    lambda = L/A = [A-2|J(x,y)|]/(2A) in [0,1/2].

Merge only if lambda<=beta; otherwise use two singleton blocks. All decisions can compare exact BRC norm/pairing quantities without computing a square root. Different exponents must be aligned exactly. An entirely zero pair is explicitly zero. For beta<1/2, a pair with exactly one nonzero row never merges, so this paired scheme does not populate a previously zero partner. A nonzero merged pair remains nonzero after Q.

## 3. The needed sampling correction is block acceptance PLUS relabelling

The inherited two-row walker proposal and local bit selection imply the following unnormalized law before compression: live mass at (h,b,z) is ||a_hb(z)||^2. Indeed proposal mass is S(z)/2 and the local bit probability is 2||a_hb(z)||^2/S(z).

Let C be the deterministic block containing z. Obtain all quantities needed for that block, including A_C and q_C. Accept with

    alpha_C = m||q_C||^2 / A_C <= 1.

On rejection, end the WHOLE trial and restart from the original initial state using fresh draws. On acceptance, replace the private work label by a fresh uniform member z' of C. The sign sigma_z' remains in the row function; it is not erased by uniform label sampling. For singleton blocks no relabelling draw is needed.

For each z' in C the surviving mass is exactly

    sum_(z in C) ||a(z)||^2 * [m||q_C||^2/A_C] * [1/m]
      = ||q_C||^2 = ||u_hb(z')||^2.

This proves induction of the complete surviving history/work law. Accepted terminal samples therefore have joint law ||u_h(w)||^2/Z, where Z is the full-trial survival probability. The algorithm need not compute global Z or the norm of the entire work field online. It DOES need the whole requested block and its norm. Zero-mass cases are not divided by; impossible local branches cannot contribute accepted mass. Random exhaustion is not success.

Symbolic failure witness: x=e0,y=3e0, merged without a small-beta restriction, give mu=2e0. Old rowwise acceptance at x would be 4>1. Block acceptance is 8/10=4/5, followed by uniform relabelling. Accepting by 4/5 but retaining the old label would keep probabilities 1/10,9/10 instead of the required 1/2,1/2. This is an algebraic interface witness, not a newly executed BRC experiment or a claimed reached Shor prefix. A strict beta may reject this particular merge.

Generic rejection sampling and resampling are not claimed as novel. The result here is the explicitly proved transfer kernel for this signed-family approximate BRC target. A full-field branch sampler can instead use its total child acceptance, but must likewise not claim a preserved latent-label invariant without the appropriate redistribution.

## 4. Global output and retry guarantees

Let V_i be the untruncated family over all classical histories, with norm one, and U_i the raw family under this target. The common history-controlled BRC instrument L_i is an isometry. With E_i=||L_i U_i-U_(i+1)||^2 and D_i=||U_i||^2-||U_(i+1)||^2, section 2 gives E_i<=D_i and E_i<=tau_i^2||U_i||^2. The hybrid triangle inequality gives

    ||V_t-U_t|| <= sum_(i=1)^(t-1) tau_i.

For unit V and nonzero U, pure-state trace distance between V and U/||U|| is the distance from V to the line of U, hence at most ||V-U||. Measurement yields

    TV(P_RP7,P_exact_same_bank) <= min(1,sum_i tau_i),
    Z >= product_i [(1-rho_i)^2(1-beta_i)].

Also TV<=min(1,sqrt((t-1)(1-Z))). This last bound needs ensemble Z, not the loss observed on one sampled path. Deterministic per-block checks enforcing the declared beta_i for EVERY possible input suffice for the uniform bound; a finite list of small observed losses does not.

For the unchanged exact factor-verifier success event G and p0=P_exact_same_bank(G), accepted success is at least (p0-epsilon)_+ when sum tau_i<=epsilon. Per-trial true-factor probability is at least Z_lower*(p0-epsilon)_+. Under iid reset attempts of finite expected cost, expected cost to a verified factor is E[C_trial]/P(trial returns a factor), not cost per accepted output. Gate-bank error to b64/ideal is separate. No positive generic p0 or factoring complexity improvement follows from this theorem.

A symbolic dyadic budget example: t=16,K=16,beta_i=2^-22. Then rho=1/4096 and tau^2=5/2^24-1/2^46<5/2^24, hence

    TV < 15*sqrt(5)/4096 < 135/16384 < 1/100.

Moreover Z>=(4095/4096)^30*(1-2^-22)^15 >= 1-30/4096-15/2^22 > 99/100. This is a proved sufficient budget, NOT a measured distribution, a claim of 99% factoring success, or evidence that any nontrivial merge passes this tight budget. It adds state approximation error only relative to the same declared bank.

## 5. A locally addressable pair, and why its apparent advantage fails on useful bases

For odd N, the involution J(w)=-w mod N pairs unit labels without needing factors or order. It commutes with every scheduled modular multiplication. Define F_h(w)=(u_h(w),u_h(-w)). A raw pair query at the next level requires only F_h(w) and F_h(P_i^-1 w), because P_i^-1(-w)=-P_i^-1(w). Apply the pair rule of section 2, including the deterministic split when its budget fails. Exchanging w and -w swaps the result: J(x,y) and lambda are symmetric, the tie convention is fixed, and Q is odd. Query order and cache orientation therefore do not change the row function.

This gives a complete symbolic two-parent PAIR recurrence without a full-field scan or a free clustering oracle. Its unshared depth-i recursion remains at most 2^(i+1)-1 pair visits, with up to twice the internal row action per visit, plus norms, certification, random draws and caches. It does not establish cheap queries.

There is a sharper obstruction. Write H=<a> in the unit group. If -1 is not in H, the unmodified instrument's support lies in H, and each pair {w,-w} contains at most one nonzero row. Such a pair has lambda=1/2, so any beta<1/2 refuses its merge. Singleton Q cannot expand support. Induction shows that this particular pairing merges NO nonzero rows at ANY history, not merely the tested prefixes.

In particular, if r=ord_N(a) is even and a^(r/2) is not -1 mod N, then -1 is not in H: a cyclic even-order group has the unique order-two element a^(r/2). These are precisely the usual favorable order-to-factor conditions (a^(r/2) cannot be +1 by minimality of r). Thus this cheapest commuting antipodal pairing gives no compression on that important class of bases. No value of r is needed as an online input to state or prove the obstruction. The claim is about standard order-based extraction, not every possible heuristic factor verifier.

Replacing -1 by a known multiplier c with c^2=1 and c not congruent to +/-1 would already yield a nontrivial factor gcd(c-1,N) for odd N. This blocks treating discovery of a better involutive MULTIPLIER as a free step. It does not rule out other deterministic partitions, time-dependent families, or non-multiplier structures.

For arbitrary predefined m-label blocks, computing all child rows can require up to 2m parent-row queries. Without a proven closure/sharing rule this can give a (2m)^i recursive upper bound. Scanning and grouping a full field avoids that recursion only by paying the full support cost. The block-resampling proof solves a correctness obstacle, not this remaining complexity obstacle.

## 6. Implementable contract and next bounded unit

PAIR_COMPRESS(x,y,K,beta): validate full carriers and common coordinate semantics; compute exact A and signed J; zero-total returns two explicit zeros; choose the fixed sign; compare A-2|J| with 2*beta*A; if the budget fails return separate Q_K(x),Q_K(y) and singleton metadata; otherwise return Q_K((x+sigma*y)/2), its signed partner, and exact A,B,C,L certificates. One may decode all labels; no omitted ordinary memo key denotes zero.

BLOCK_TRANSFER(h,b,z): resolve the SAME deterministic partition used by row queries; obtain the complete block; accept by retained block mass/raw block mass; on acceptance redraw the label using the retained block's conditional mass (uniform for signed equal-value blocks); on rejection terminate the trial. Never retry locally while keeping an uncorrected work label.

Next execution unit: implement only these operations using the pinned actual signed BRC/Dyad interfaces; verify projection/error identities and an exhaustive small live-history/work law against a full-field reference of this NEW target. Include unequal row masses, opposite signs, differing exponents, a zero partner, ties, budget refusal, query-order and random-exhaustion checks. Demonstrate the antipodal no-merge theorem rather than selecting it as a purported performance winner. Then test a declared non-antipodal grouping and charge all grouping, raw-row queries, rejection, label-resampling and factor-verification costs. No such execution is reported here.

Do not repeat RP6 exact interning or its benchmark as new progress. No new benchmark counts, speedups, local source commits, scientific bundles, core-call traces or independent review have been produced in this turn. Runtime validation is pending. Existing native session authority remains unverified; this note creates no RA, CLAIM, run or Result.

## 7. Sources and scope of outside reading

The actual attached RP6_Proof.md, especially sections 1-3 and its final approximate-family question, is the mathematical intake. Published source: https://github.com/awdawmip/enterprise-math/blob/c2870c60795a682666f6670f5abc0d2c5cd64883/research_notes/HEARTBEAT_RP6_VALUE_FAMILIES_4C570759_20260927.md . RP3/RP5 contracts are inherited only at the stated scope.

Primary outside abstracts/publication metadata consulted: Bravyi-Gosset-Liu, https://arxiv.org/abs/2112.08499 ; Zulehner-Hillmich-Markov-Wille, Approximation of Quantum States Using Decision Diagrams, https://arxiv.org/abs/2002.04904 ; Shor, https://arxiv.org/abs/quant-ph/9508027 . Approximate compressed simulation and amplitude-query sampling have prior art. The displayed signed-block transfer, budget and antipodal proofs are derived here; they are not attributed verbatim to these abstracts, and full-text novelty completeness is not claimed.
