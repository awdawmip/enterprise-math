# R4-EC31 — Observer-scoped source-memory quotient and nonvanishing relative defect

**2026-10-26 · Author-side exact derivation + integer verification. NOT a native heartbeat Result, an independently reviewed theorem, or an accepted Foundation promotion.**

## Frozen authority and BRC carrier

Account Global Knowledge: awdawmip/chatgpt-global-knowledge main@90a2dbab9e17c77b3a4c74bea4785e6f0e240321 (GLOBAL_KNOWLEDGE_V1), including both normative entrypoints, ACTIVE worldview, P000, mathematical/code/BRC and activity rules. Project: awdawmip/enterprise-math main@49f0bdada7acc91157a9967b5d6374219cd9de25, P000 X6 V5, joint-relation observer contract, weighted-BRC foundation, heartbeat BRC-only route and docs/PORTABLE_RESEARCH_PROTOCOL.md. The predecessor is the *exact* R4-EC30 author-side source commit 9042dd74fd97d06d218e9c9818da8da7bf69ba1b (and EC29 commit 1f112b4352e7162ed7afc67f8a6d32eae75530b6). Their conclusions remain author-side, not independently admitted.

GitHub user awdawmip has administrative Source access. Native owner/task lookup returned CONTROL_QUOTA, so the live owner, session and CLAIM are unverified. The work below is a separately scoped author-side positive BRC result, not an adoption of anyone's active task.

The exact carrier is EC29's *invented*, not physically implemented, positive source-labelled path model in a selected three-axis sub-torsor of the six-dimensional signed-X6 Cell chart, starting at an arbitrary chosen Cell anchor. The steps are A=+E1, B=+E2, C=+E3, with E4/E5/E6 unchanged; C has labels C0 and C1 if and only if immediately preceded by A, and otherwise only label C0. The memory bit q is one exactly when the last preceding letter was A. Positive-source alternatives add counts and ordered concatenation multiplies them, retaining branch multiplicity. The third selected coordinate is the C-step count, not an omitted native dimension. Step length h is **operation depth, not heartbeat time**. The raw signed six-coordinate displacement is not an encoded final Cell address. This model has no physical phases or signed cancellations.

For an undecorated future word w, let ac(w) count adjacent AC occurrences. EC30 proved the exact multiplicity law N_0(w)=2^ac(w) and N_1(w)=N_0(w)(1+1_{w begins C}), valid for all finite words, including the empty word.

## Theorem A — exact future-language quotient criterion

Fix a finite future length h, an admissible language L contained in {A,B,C}^h, and rational nonnegative word-observation weights theta(w). Define O_q(L)=sum_{w in L} theta(w) N_q(w).

Then, exactly,
 
O_1(L)-O_0(L) = sum_{w in L, w begins C} theta(w) 2^ac(w) >= 0.

Consequently q=0 and q=1 may be identified for *this observer and future language* if and only if every admissible first-C word has weight zero. For a vector of endpoint/grade/word observers, the criterion must hold on **each** observation fiber; a coarse total with positive weights cannot hide an unequal fiber through cancellation. For any collection of horizons, apply the condition coefficientwise. A statement about one horizon does not imply unbounded-horizon preservation.

**Proof.** Upon the first A or B both initial states have the same successor memory, and all subsequent source-labelled continuations coincide. If the first letter is C, starting in q=1 creates exactly one additional first-C source-labelled choice; thereafter the two successor memories coincide. Hence the multiplicities are identical for A/B-first words and differ by N_0(w)>0 for C-first words. Multiply by theta(w)>=0 and sum. There can be no cancellation; the defect is zero exactly under the stated condition. QED.

This refines EC29's globally necessary one-bit repair: if a genuinely specified operation language excludes all initial C steps, the bit can be forgotten **for that scoped observer** without losing future source *counts*. It does not recover the full source-label histories, signatures under larger future languages, native fields or physical amplitudes.

## Theorem B — sharp, uniform-in-horizon relative defect

Weight every A, B, C primitive operation by a fixed *strictly positive rational* x, y, z, respectively, independently of its C0/C1 label. Let T_{q,h} be the sum of positive source-labelled weights of all future words of exact length h, beginning from initial memory q. Set:

s=x+y+z>0, p=xz>0, H_h=T_{0,h}, D_h=T_{1,h}-T_{0,h}.

The exact BRC marked-AC atom bijection from EC29, with positive word weights retained, gives formal series identities:

F_0(t)=sum_{h>=0}H_h t^h=1/(1-s t-p t^2),

F_1(t)-F_0(t)=sum_{h>=0}D_h t^h=z t/(1-s t-p t^2).

Thus H_0=1, H_1=s, H_h=s H_{h-1}+p H_{h-2} (h>=2), D_0=0 and D_h=z H_{h-1} (h>=1).

For h>=1 define the *true-q=1-mass fraction* omitted when the bit is forgotten:

epsilon_h=D_h/T_{1,h}=z H_{h-1}/(H_h+z H_{h-1}).

**Universal sharp bounds for every finite h>=1:**

z s/(s^2+p+z s) <= epsilon_h <= z/(s+z).

The upper bound is attained at h=1 and the lower bound at h=2. These are exact rational bounds for rational x,y,z and do not weaken as the future horizon grows.

**Asymptotic theorem:** Let lambda_+=(s+sqrt(s^2+4p))/2 be the unique positive root of lambda^2-s lambda-p=0. Then

lim_{h->infty} epsilon_h = z/(lambda_+ + z)>0.

**Proof.** Every labelled source word uniquely corresponds to a sequence of A, B, C single-letter atoms and distinguished double-letter AC atoms, where a distinguished AC means selection of the extra C1 label. The free ordered atom generating function is exactly F_0; a q=1 history supplies one extra first-C-labelled branch, hence F_1-F_0=tzF_0. These are identities in the positive rational formal-power-series BRC semiring, with no negative source weights.

Put r_h=H_{h-1}/H_h>0. The recurrence implies r_1=1/s, r_2=s/(s^2+p), and r_{h+1}=f(r_h) where f(r)=1/(s+p r). Since f is decreasing, f(r_1)=r_2 and f(r_2)<=r_1; consequently the entire closed interval [r_2,r_1] is invariant. By induction, r_2<=r_h<=r_1. The strictly increasing rational map g(r)=zr/(1+zr) sends these endpoints to the stated sharp bounds for epsilon_h.

Furthermore |f'(r)|=p/(s+p r)^2 <=p/s^2<1 (because x,z>0 and s=x+y+z). This is a contraction on the invariant interval. Its unique positive fixed point solves p r^2+s r=1, namely r=1/lambda_+. Taking limits under g yields z/(lambda_++z)>0. QED.

For the original unit-weight source model x=y=z=1, s=3,p=1, so:

**3/13 <= epsilon_h <= 1/4 for every h>=1**,

and lim epsilon_h=2/(5+sqrt(13))=(5-sqrt(13))/6.

Thus for this **aggregate all-future-words at fixed depth** observer, at least 3/13 of the q=1 positive source mass is missed at every nonempty depth when the historical bit is incorrectly dropped. The algebraic root is a derived recurrence readout, not a calibrated physical heartbeat frequency or time.

## Theorem C — endpoint-conditioned fraction can vanish

When retaining the endpoint (a,b,c) instead of aggregating all operation words, EC30's exact BRC defect is Delta W(a,b,c)=W(a,b,c-1) if c>=1, zero otherwise.

For any integer m>=0, endpoint (m,0,1) has W_0=2m+1, W_1=2m+2 and Delta W=1. Hence the endpoint-relative lost fraction equals 1/(2m+2), tending to zero as m grows. Conversely at endpoint (0,0,c), c>=1, the unique future word C^c has W_0=1 and W_1=2, so relative loss equals 1/2. When c=0 it equals zero.

**Proof.** At (m,0,1) the C can occur first (one labelled source) or after one of m As (two labelled sources for each placement), yielding 1+2m. Initial q=1 creates one additional labelled choice on the C-first word, yielding 2m+2. At (0,0,c), only C^c occurs; the extra initial source choice doubles the first C and none thereafter. QED.

**Observer distinction:** Theorem B's uniform aggregate lower bound is not an endpoint-uniform lower bound. There is no strictly positive lower bound on endpoint-relative error over *all* endpoints with c>=1. Endpoint support, positive count and normalized relative defect are different BRC observer types.

## Verification, method and remaining work

Actual local execution: EC31_verify.py, Python arbitrary integers and exact Fraction comparisons, four positive integer weight triples (1,1,1), (2,1,3), (1,4,2), (3,2,5); automata h=0..36 and independent per-word positive source counting for every word through h=8. Reported checks: 148 automaton depth cases, 144 rational bound checks, 39,364 word/initial-state signature checks, 101 endpoint-family checks; all PASS. The universal proofs above are not extrapolated from those finite tests. The program is source-blob-identical to the executed copy; EC31_REPORT.json summarizes the run and can be regenerated with the executable.

BRC method resolution: REUSE_APPLIED to EC29's exact marked-AC/path-N-BRC carrier and endpoint theorem; COMPOSE_APPLIED to EC30's source-memory defect; EXTEND_EXISTING_TOOL via a future-language certificate and sharp relative-error bounds. No numerical pi, classical trigonometry, matrix propagator, phase surrogate or physical residual experiment was executed.

**Native limitation:** At the frozen project source, definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json still has fixed_heartbeat_program=null. The real source-labelled heartbeat update, independent physical time model, complete valid native crystal packet/slice representation, source-fibre preservation and EC27-to-X6 bridge have not been established. Thus EC31 is a theorem *within the declared invented positive-source BRC path model*, not a native X6 heartbeat theorem.

**Precise successor (EC32):** Obtain the current actually authorized native source-labelled update and its selected three-dimensional slice, time semantics, grade and future-language definition. Compare all source fibres and update-commutation at depths 2 and 3; apply Theorem A separately to each native observation class. Without a specified native transition, preserve NATIVE_LIFT_UNPROVED and seek the minimal missing transition/source rule rather than inferring it from auxiliary path counts.
