# RP14-PATH-BUDGET: online directional-error budgets without output-tree enumeration

Progress-Event-ID: RP14-PATH-BUDGET-C971348E-20260928
Date: 2026-09-28 Asia/Taipei
Status: AUTHOR_DERIVATION / LOCAL_EXECUTION_UNAVAILABLE / UNREVIEWED / NOT_ADMITTED
Global read snapshot: 8ed0845abd58a3cfc63aef1f6a8d26f94cff2bbf
EM intake: 643a098b7ae08a4fb88c1c8f4f7e65502a7904f2
Publication preflight: 1a54a242a7c04ff47d19eef953308a805b139f5d
Scientific parent: RP13-BRANCH-NORM attachment/runtime, not a new formal Result.

## 0. Actual source and execution status

The full attached RP13_BRANCH_NORM_研究报告.md and RP13_BRANCH_NORM_Proof.md and the relevant delivery ranges were read through Files in this turn. Their source explicitly states that RP5 already implemented conditional normalization and the mass-weighted hybrid bound. RP13 applied them to the no-work-pruning18-coordinate replica carrier, computed full finite laws, and left adaptive caps unimplemented. We consume that frontier; the generic hybrid bound is NOT a new RP14 theorem.

Parent archive: BRC_RidgePrecision_RP13_BRANCH_NORM_RUN_20260928.zip; recorded size45725980; recorded SHA25629d4fa91081b334273683db2ca46735c03cea53fb583b4eaf6bd2ef3dcb7b9a3. These are parent delivery metadata, NOT a new byte verification. Parent frozen engine SHA2564b1ff066eba0a6debad4369eb751a8712c6ad2385bb27f848a02e72aec63d28c. Original positive BRC vendor SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26.

The current container, analysis Python, and visible Python calls all returned ClientError. No archive extraction, new BRC numerical execution, probability enumeration, Monte Carlo experiment, runtime benchmark, local file hash, or new executable package succeeded in this turn. Results below are explicit algebraic derivations and an interface counterexample, not numerical BRC-Shor measurements. The new controller has NOT been implemented or formally verified. Source publication preserves a resumable proof, not acceptance.

P000 is unchanged. All formulas use the inherited complete signed BRC carrier and its positive diagonal W18 metric, including complete work labels, exact dyadic exponents, actual b12 gates and their order. No new ideal phase, trigonometric reference, known order/factor input, independent-row normalization, hidden-label collapse, or physical realization of conditional normalization is introduced. Source bank evidence currently covers the declared levels through18; a general formula does not certify untested wider banks.

## 1. Chosen question and fixed observer

Can the RP13 conditional-normalization sampler choose lower or higher mantissa caps from observed local error while certifying a prescribed final OUTPUT total-variation budget, without generating the entire tree of output histories or an accurate-reference distribution?

Let x_h be the full conditional field at bit history h; the exact next actual BRC instrument produces raw fields a_hb with A_hb=Q_W(a_hb). M_h=Q_W(x_h), p_hb=A_hb/M_h, and sum_b p_hb=1. Quantize only the selected whole child field, preserving every work row and all18 representative components of each row. Do not draw a survival coin. The next bit normalizes by the ACTUAL current field mass. This is RP13's L-type conditional target, not the R survival-conditioned target.

The precision policy and its budget state must be deterministic functions of the fixed input, bank, visible history and full conditional field. They must not depend on a private latent work label, cache visitation order, success mask, later factor verification or previous independent attempts. At a fixed policy these data define one unambiguous history tree. If budget/configuration differs, cache identities must distinguish it.

For a nonzero raw child a and nonzero candidate q, set A=Q_W(a), C=Q_W(q), J=J_W(a,q). The normalized full-field direction error is

    gamma(a,q)^2 = 1-J^2/(AC).

This is a quotient of the inherited full BRC observer, not the norm of one work row. A zero-probability child is never sampled and requires no division. The terminal boundary is not quantized and receives zero error charge.

## 2. A remainder identity separates direction from radial mass loss

Write e=a-q, E=Q_W(e), B=J_W(q,e), and C=Q_W(q). Then

    A=C+2B+E,       J=C+B,
    AC-J^2=CE-B^2,
    gamma^2=(CE-B^2)/(AC).

All pairings sum over the same COMPLETE work-field carrier with the true exponents. For toward-zero truncation B>=0, but the identity itself only requires the inner-product algebra. Cauchy-Schwarz gives CE-B^2>=0.

The identity decomposes the discarded part into a component parallel to q and a perpendicular component:

    E - B^2/C = A gamma^2.

If e is a common scalar multiple of the WHOLE q, the directional error is zero even when norm loss is nonzero. Conversely, changing different work rows by different factors need not be radial and must not be normalized away. This is the precise task-level reason to avoid charging all norm loss as directional error.

An implementation MAY form E and B from discarded integer remainders rather than separately squaring two nearly equal full totals. It still needs common exact exponent handling, A/C, and complete work-label coverage. No runtime or bit-length improvement for this rearrangement has been executed or claimed.

## 3. More retained bits need not monotonically reduce directional error

Use the legal18-carrier subspace spanned by modes0 and1, each with W weight1, all other entries zero. Let the raw full field consist of one row

    a=11 e0+5 e1.

This is an ALGEBRAIC INTERFACE example, not asserted to occur on a standard BRC-Shor path, and it was not run through a new BRC observer. Its values follow directly by applying inherited Q(e0)=Q(e1)=1 and J(e0,e1)=0.

The inherited common-shift toward-zero quantizer gives physical rows

    K2: q2=8 e0+4 e1,      K3: q3=10 e0+4 e1.

The raw norm is A=146. For K2, C2=80,J2=108,E2=10; for K3,C3=116,J3=130,E3=2. Thus

    gamma2^2=1/730,
    gamma3^2=9/4234 > 1/730.

The ordinary error decreases from10 to2, while normalized directional error INCREASES. Therefore a precision search must not binary-search K under an assumed monotonicity of gamma. An ordered finite candidate scan with exact acceptance tests is safe; so is a certified all-input bound. A failing K does not prove all smaller K fail, and a passing K does not prove every larger K passes.

Every higher-K candidate must be obtained from the SAME original raw child a, not by padding or requantizing an already truncated q. Lost low bits do not return when a cap is raised. Holding a while testing candidates is a real temporary-memory cost.

## 4. The inherited hybrid interface, expressed as an expectation

Let pi denote a fixed deterministic adaptive policy and L_pi its output law. P_* is the law from the same initial field and the same actual b12 gates with no state quantization. RP13/RP5's hybrid argument extends to this policy: compare algorithms with the first i approximate boundaries and an EXACT common suffix. Their prefixes, next-bit probabilities and policy budget metadata agree up to the replacement under comparison. After the replacement both suffixes are the same exact instrument, so its readout contracts the normalized full-field direction distance.

Consequently, with s=t-1 nonterminal boundaries,

    TV(L_pi,P_*) <= sum_i sum_|h|=i L_pi(h) gamma_h
                  = E_(k~L_pi)[ sum_h on path k gamma_h ].

This uses the policy's own approximate-prefix probabilities, not unknown exact-prefix probabilities. It does NOT assume nonlinear truncation contracts arbitrary pairs of approximate states. The task is now to bound the expectation by a runtime invariant instead of enumerating all h.

## 5. Pathwise budget theorem and a finite dyadic controller

Suppose a nonnegative certified charge u_h>=gamma_h is assigned at each approximate boundary. If the policy ensures, for EVERY positive-probability root-to-leaf path,

    sum_h u_h <= epsilon,

then immediately

    TV(L_pi,P_*) <= epsilon.

A single observed path staying within budget does NOT prove this condition. The guarantee follows from the universal controller invariant plus its local certificates; finite tests only validate an implementation of that invariant.

Concrete reference controller, specified but not executed:

1. Choose dyadic accounting unit rho=2^-P, P>=0, and integer initial credit B0=floor(epsilon/rho). The certified total is B0*rho<=epsilon. This is an error-accounting resolution, not a BRC gate precision.
2. At a selected raw child, let m be the number of nonterminal compression boundaries still including the current one. Let U=floor(B/m). Search the PREDECLARED ordered cap list, e.g.8,10,12,16,20,24,32. All candidates are recomputed from raw a.
3. For each q, compute the full BRC A,C,J and Delta=AC-J^2. A/C must be positive; Delta must be nonnegative. Accept only if

       Delta * 2^(2P) <= U^2 A C.

   Denominators are cleared with positive exact factors. No floating square root or guessed direction is used.
4. For the accepted q, let b be the smallest integer in[0,U] such that

       Delta * 2^(2P) <= b^2 A C.

   A bounded integer search gives a certified upward-rounded charge b*rho. Update B <- B-b, continue with q, and decrement m. There is no random acceptance/rejection at this budgeting step.
5. If no candidate passes, return raw a exactly and charge0. If U=0, exact q=a always supplies this path. The finite cap list plus exact fallback terminates for every finite input, but exact fallback means no hard upper bound on all stored mantissas.
6. At the terminal boundary do not quantize and do not charge.

Because b*rho>=gamma and B never becomes negative, induction gives sum gamma<=sum b*rho<=B0*rho on every path. Cheap stages with b=0 leave all credit for later; small actual charges preserve more future credit than charging the full allowance U. The current remaining allowance is recomputed, not spent merely because it was reserved. Budget never resets inside one output sample. Independent output samples restart with the SAME fixed configured policy.

An all-input shortcut can bypass actual angle evaluation when the inherited bound already proves safety: gamma<=5*2^(1-K). If its upward-rounded charge is <=U, accept with that conservative charge; an audit may still evaluate the exact angle. For rational tolerance tau>0, K with24*2^(2(1-K))<=tau^2 is another sufficient certificate. The runtime scans, root-comparison cost, full-field metrics and cached next-step mass must be measured; this theorem supplies no free certificate.

## 6. Probability-weighted reserve theorem allows rare branches more error

Pathwise caps are sufficient, not necessary. A more general local certificate attaches a finite nonnegative reserve V(h) to every positive-probability prefix. If V(empty)<=epsilon and at every raw binary split

    sum_b p_hb [u_hb + V(hb)] <= V(h),
    gamma_hb <= u_hb,

with terminal reserve nonnegative, then

    E_(L_pi) sum_h gamma_h <= epsilon,
    TV(L_pi,P_*) <= epsilon.

Proof: multiply each local inequality by L_pi(h), sum across a depth, and telescope. Expected charged error plus expected remaining reserve is nonincreasing. This is an explicit conditional-expectation identity, not an assumed martingale or evidence from one walk.

One completely specified allocation needs no future tree. Set a=epsilon/s, reserve m*a when m compression boundaries remain. For p_hb>0 assign

    tau_hb=min(1, a/(2p_hb)).

Choose q with gamma<=tau_hb, using the same exact test/fallback, and set the child's reserve to(m-1)*a. The inequality follows since p_hb*tau_hb<=a/2. Zero-probability children are skipped. Only the actually selected raw child needs quantizing; the policy's mathematical all-input guarantee covers the unvisited alternative. Probabilities are computed BEFORE candidate quantization, with original actual gates unchanged. Broader deterministic allocations theta_b>=0, sum theta_b<=1 may replace1/2.

This permits an individual rare branch to have directional error exceeding the per-round average allocation, WITHOUT dropping that branch. It does not guarantee cheaper execution: the likely branch can receive a tighter allowance, and its cost may dominate. This probability-weighted controller is a DIFFERENT configured approximate law from the pathwise-debit controller. No expected-cost optimality is claimed, and a local small p does not by itself bound a whole-output failure probability.

## 7. What can be certified, and what cannot be recovered

For any FIXED exact factor-verification event G,

    |L_pi(G)-P_*(G)| <= epsilon.

This is an absolute event-probability bound, not1-epsilon factoring success. It is relative to the SAME b12 bank. Comparing to old21/Q16 additionally requires that target's independent same-bank bound. For the already-declared18-coordinate/active21 scope through t18, a sufficient old-Q16 bound is(t-1)*5/32768. A theoretical epsilon=1/1000 at t18 therefore yields the triangle bound

    epsilon+85/32768 < 1/250.

This is a symbolic budget illustration, not a new execution or a statement about required mantissa K. B12-versus-b64/ideal gate error remains separate.

Adaptive precision cannot repair unknown error committed before its current checkpoint. An RP13 low-precision field used mid-run is not an exact reset with zero spent budget. Start from the same initial state with the new ledger, or inherit an independently valid prior-error charge.

A bound on one output sample is not automatically the same bound for an entire until-factor transcript. For at most M independent restarted samples, product coupling and data processing give transcript TV<=min(1,M*epsilon). Without a fixed M, no identical uniform transcript bound is claimed. With independent identically configured attempts of mean cost c and per-attempt true-factor probability p>0, the renewal equation gives expected cost until success c/p (even when current cost and success are correlated). This must include failed outputs, recomputation, metrics and initialization according to the chosen reset model. No sample-success count or local cap saving in this turn establishes an improvement of c/p.

## 8. Preserved implementation boundaries

- Do not normalize work rows independently; compute A,C,J over the complete conditional field and common exact scales.
- Do not erase low-mass labels, discard signed interference or turn positive mass into amplitude.
- Do not alter the actual gate bank/temporal order/factor verifier to meet the budget.
- A computational exact fallback retains a without a new random survival coin. It is not RP13-R rejection and does not select outputs by success.
- Cache clearing changes recomputation only. Policy config, accounting scale and budget state belong in scientific identity where they affect q.
- More bits are not assumed to improve projective error monotonically; do not binary-search K on that premise.
- Temporary raw fields, exact scalar products, accounting integers and probabilities are charged separately from retained mantissas.
- The universal budget proof avoids enumeration of OUTPUT HISTORIES, not the current explicit WORK FIELD. No cheap arbitrary row oracle or polynomial classical Shor conclusion follows.
- No claim of physical nonlinear normalization, ideal-QFT fidelity, formal admission or independent review.

## 9. Finite acceptance packet; all items below remain unexecuted

First bind to the unmodified RP13 runtime and original positive BRC observer. Implement the pathwise integer-debit controller as a new module, preserving every parent file. Set a declared epsilon, P, candidate list, exact fallback and raw-field retry semantics before collecting data. Verify zero branches, signs/exponents, Delta>=0, integer charge upper bounds, exhausted budget, forced exact fallback, policy determinism under cache/query order, and the symbolic11/5 nonmonotonic witness through the actual BRC observer.

On the three existing RP13 diagnostic inputs (21,2,12),(35,2,12),(77,2,10), treat old laws as reference sources, not new discovery. Enumerate the NEW policy once to cross-check every path budget, the expectation identity and actual TV<=epsilon. Then run new predetermined sampling inputs/seeds without generating their reference trees. Report cap histogram, exact-fallback fraction, full-field/certificate costs, peak retained and temporary bits, cold preparation, all capped failures and time per verified factor. Same seed need not mean same path across different laws. Compare fixed8/12/16 to pathwise and weighted controllers as distinct targets.

A negative speed result is retained. Universal error safety alone is not enough to replace the fastest inherited implementation. Low epsilon may force nearly accurate paths; finite fallback and error proof are not a complexity theorem.

## 10. Source, control and persistence

This turn's native status request is Issue2568, request_id status-rp14-budget-c971348e-20260928-01, logical conversation chat-stage101-c971348e64294a5882dfc50fcc8217f1. Matched response reports transport version0.6.8, existing session MCP-96f924f41c514d25a77e39b46abe2044 and original start_request_id stage101-session-c971348e-02, research_authority_granted=false. No new identity, RA, CLAIM, formal run/Result or independent acceptance is asserted. Activity/native-start prerequisite remains separate from this authorized portable derivation.

Current Sources consumed: RP13 report/proof/delivery; current global bootstrap/manual/P000/project router; current EM BRC-only and portable-research contracts. Parent stored numerical results are NOT new RP14 executions. Public primary source checked only at abstract level: Zulehner et al., arXiv2002.04904, Approximation of Quantum States Using Decision Diagrams; Yan et al., arXiv2507.04335. Their approximation/fidelity work is prior art; no global novelty or transferred complexity guarantee is claimed. This turn's specific contribution is the full-field remainder identity, nonmonotone cap witness, a finite integer path-credit controller with all-history implication, and the probability-weighted reserve alternative, applied to the inherited conditional BRC observer.

The local execution failure does not prevent recording a proof. This artifact is LOCAL_VALIDATION_PENDING: there is no new source hash, BRC run receipt, probability law or timing package. Google Drive mirror and actual post-publication readback are recorded separately rather than anticipated here. Do not rewrite or delete earlier evidence/pending records merely because this note exists.
