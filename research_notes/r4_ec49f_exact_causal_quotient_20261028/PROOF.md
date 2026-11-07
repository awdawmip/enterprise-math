# EC49F — exact causal likelihood-ratio quotient and rational occupancy certificate

**2026-10-28 / TASK_RESEARCH author-side portable study.** Status: `AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. This is a finite, strictly positive, source-neutral **auxiliary weighted-BRC observation model**, not a native signed/phase BRC computation or an X6 heartbeat evolution. It continues immutable EC49E (`4cc5c0407d499562b7f3039a51454c53dc438c82`) without replacing its proof or Owner/Claim.

## 1. Exact theorem: a causally observable two-source quotient

Let two probability laws P,Q have strictly positive rational masses on the leaves of a finite rooted observation tree with stages t=1,...,H. At an internal prefix h, a source-neutral behavioral observer may **reject**, **accept**, or **continue** to obtain the next observation and advance the auxiliary clock by one. At the final stage it must accept or reject. P and Q specify the observation law **under forced continuation**; actions do not change those laws other than stopping the current path. Full-history observers may condition on all previously seen labels, without a persistent hidden random register. Define the raw four-dimensional region

\[S=\{(\alpha,\beta,E_PT,E_QT):\pi\text{ any legal source-neutral behavioral policy}\},\]
where \(\alpha=P_\pi(\text{accept})\), \(\beta=Q_\pi(\text{accept})\), and T is the stage of stopping.

Let \(P_t(h),Q_t(h)>0\) be the exact forced-continuation prefix masses, \(L(h)=P_t(h)/Q_t(h)\), and \(\phi_t:\mathcal H_t\to\mathcal S_t\) a finite-stage compression. **Assume all of the following:**

1. Each state s=φ_t(h) has a fixed stage t, the same available actions, and a single **complete prefix** ratio \(r_s=L(h)\). In particular, no substitute ratio computed only from an already-collapsed current symbol is silently inserted.
2. Every h in state s has the same next-state law under Q **conditional on continuing**: for every s' at t+1,
   \[K_Q(s,s')=\sum_{h':\,h'\succ h,\,\phi_{t+1}(h')=s'}\!Q_{t+1}(h')/Q_t(h),\]
   where the sum ranges over immediate child prefixes. (Each path's next observation is included exactly once.) Terminal classes have no continuation. The analogous P kernels then agree automatically because \(P_t(h)=r_sQ_t(h)\) and \(P_{t+1}(h')=r_{s'}Q_{t+1}(h')\):
   \[\boxed{K_P(s,s')=(r_{s'}/r_s)K_Q(s,s').}\]
3. The compact controller is actually entitled to observe the class s at the current stage: the class is either a declared current readout or can be updated causally from its previous class, its action and its declared next observation. **Providing s as an unrequested new oracle is not an operational compression.** The full-history controller can of course evaluate φ_t.

**Theorem EC49F-Q.** Under (1)–(3), the **entire raw** regions of the full-history observer and the compressed φ-state observer coincide for arbitrary *real* behavioral randomization, including all four coordinates simultaneously: \(S_{full}=S_{\phi}\). The common region is the projection of an explicit rational linear occupancy polytope and therefore is a rational convex polytope. In this class, **each rational attainable four-vector admits a fully rational source-neutral compressed policy**; an irrational-only rational target is impossible.

**Proof (constructive, all real strategies).** For a full-history policy π, write \(v_\pi(h)\) for the conditional probability that decisions along h have continued to stage t. Because actions use the same source-neutral probabilities under both hypotheses, v(h) is the same multiplicative factor for P and Q along any exact history. Let \(x_s=\sum_{\phi(h)=s}Q_t(h)v(h)\) and \(u_{s,a}=\sum_{\phi(h)=s}Q_t(h)v(h)\pi(a\mid h)\). Set compressed \(\bar\pi(a\mid s)=u_{s,a}/x_s\) when \(x_s>0\); choose any legal distribution on an unreachable state. This is **one** policy, not one independently fitted for P and another for Q. Condition (1) gives P-alive mass exactly r_s x_s and P-action flow r_s u_{s,a}. Condition (2) gives the next Q-alive flow \(x_{s'}=\sum_s u_{s,continue}K_Q(s,s')\); the P flow is simultaneously consistent by the boxed formula. Induction on t gives identical state/action flows under both sources for π and \(\bar\pi\). Since stop at stage t contributes t times its source mass and acceptance contributes its source accept mass, all four coordinates agree. Conversely every φ-policy is a full-history policy by (3), so the raw regions are equal. Notice that the proof **does not** infer arbitrary joint-event fidelity from equality of marginal LR spectra.

For the linear description take nonnegative Q-occupancy variables \(x_s,u_{s,a}\) and the exact equations

\[x_s=\sum_a u_{s,a},\qquad x_{s'}=\sum_s u_{s,continue}K_Q(s,s')\ (t\ge1),\]
with initial \(x_s=\sum_{h:\phi_1(h)=s}Q_1(h)\). At terminal stages u_continue=0. The output map is

\[\begin{aligned}
\beta&=\sum_s u_{s,accept}, & \alpha&=\sum_s r_s u_{s,accept},\\
E_QT&=\sum_s t(s)\big(u_{s,accept}+u_{s,reject}\big),&
E_PT&=\sum_s t(s)r_s\big(u_{s,accept}+u_{s,reject}\big).
\end{aligned}\]

Any feasible flow defines a legal behavioral policy by u/x; the preceding induction proves its output. All coefficients are rational. A nonempty rational polyhedron intersected with rational target equalities contains a rational point (equivalently solve the finite rational linear feasibility system), and u/x is rational at all positive-occupancy states; choose rational decisions at zero-occupancy states. Thus no rational four-vector in this subclass requires irrational behavioral choices. Convexity and rational-polytope status follow from linear projection of the finite bounded occupancy polytope. QED.

**Boundary of the theorem.** It concerns the stated stopping/continue observation language, the *complete prefix likelihood-ratio* class, source-neutral decisions and unit stage clock. For action-dependent sensing/costs, replace the one continue kernel by a separately equal joint action-conditioned kernel for each action and preserve the exact immediate source-indexed output contributions. Condition (3) remains essential. The theorem is a sufficient lossless criterion, **not** an equivalence or necessary condition for all possible task-specific four-vector compressions; dominated alternate paths can mask local kernel differences (EC49D).

## 2. Exact bottom-up computation and its scope

At stage H, group all full histories with identical `(stage, complete_prefix_LR)`; they have the same allowed terminal decisions. Inductively at t=H−1,...,1 group histories with identical `(stage, complete_prefix_LR, distribution of Q over the already computed successor classes under continue)`. All groups preserve the P kernel by the boxed relation. This is the coarsest partition among partitions **stable under these exact LR and successor-Q-kernel requirements**: a competing stable partition must respect the terminal tags, and induction forces its earlier blocks to refine the computed blocks. This *does not claim* a minimum number of memory states among every four-vector-equivalent controller; nor does the algorithm guarantee causal readout implementability. Check condition (3) separately on the declared observation interface.

The finite algorithm uses exact rational equalities and can stop at a precisely exhibited differing conditional kernel, instead of approximating a tiny information residual away.

## 3. Strictly positive eight-leaf **safe** instance: 14 histories → 6 quotient states

Let W∈{0,1}, with κ_0=1/3 and κ_1=2/3, source-neutral and independent of both future readings. Given P or Q, Y1 and Y2 are independent binary observations with

\[P(Y_i=1)=3/4,\quad Q(Y_i=1)=1/4,\quad i=1,2.\]

For each of the eight labeled leaves (w,a,b), define **unconditional** positive rational masses
\[P(w,a,b)=\kappa_w p(a)p(b),\qquad Q(w,a,b)=\kappa_w q(a)q(b),\]
where p(1)=3/4,p(0)=1/4 and q(1)=1/4,q(0)=3/4. The fine observer can use full history W,Y1,Y2; the coarse interface reports only stage and **complete LR**, with at stage 2 Y1 equivalently readable from LR. It supports stop/continue at T1,T2, and terminal acceptance at T3. No W is needed for the coarse controller.

At T1 complete LR is 1, at T2 it is 3 for Y1=1 and 1/3 for Y1=0. At T3 it is 9 for Y1=Y2=1, 1 for mixed observations, and 1/9 for Y1=Y2=0. Thus exactly **one**, **two** and **three** classes suffice at T1,T2,T3, respectively. For each value of the current complete LR, both W histories have identical Q distributions over next LR classes. Explicitly:

- T1: next LR=3 with Q-probability 1/4; LR=1/3 with Q-probability 3/4.
- T2 LR=3: next LR=9 with Q-probability 1/4; LR=1 with Q-probability 3/4.
- T2 LR=1/3: next LR=1 with Q-probability 1/4; LR=1/9 with Q-probability 3/4.

The stage+LR labels are causally readable and hence (3) holds. Theorem EC49F-Q applies: **the entire four-dimensional raw region is identical for a 14-node full-history tree and this six-class quotient**. No convexification has been used as an approximation.

To show a genuinely W-dependent random controller is covered, take the precise probabilities listed in `VERIFY.py` (W-specific T1 continue, W- and Y1-specific T2 continue and terminal acceptance). The Q-flow compilation returns a single compact strategy and exactly the observation

\[\boxed{O=(377/576,\;329/576,\;25/12,\;73/36).}\]

For this instance the compiler's T1 compact `(reject,accept,continue)` probabilities are `(1/9,2/9,2/3)`, T2 are `(1/6,1/6,2/3)` at LR=3 and `(3/16,5/16,1/2)` at LR=1/3. The full terminal probabilities are in `EXACT_REPORT.json`. Direct two-source evaluation confirms equality coordinate by coordinate.

## 4. EC49E eight-leaf **obstruction**: individual marginal spectra are insufficient

Reusing the exact 8-leaf masses and source pin in EC49E, the bottom-up **action-conditioned** signature has 5 terminal LR classes, 4 classes at T2, and 2 classes at T1. In particular the two histories (W=0,Y1=1) and (W=1,Y1=1) have the same complete *prefix* LR=3 but their Q distributions over *terminal* LR are:

\[\begin{array}{c|ccc}
 & LR=1 & LR=7/2 & LR=11\\\hline
 W=0,Y1=1 & 1/5 & 4/5 & 0\\
 W=1,Y1=1 & 4/5 & 0 & 1/5
\end{array}\]

so their total-variation distance equals \(4/5\). For Y1=0, the corresponding terminal LR distributions have TV distance \(14/15\) (see `EXACT_REPORT.json`). No quotient respecting the action-conditioned kernel can merge W at T2 for either Y1 value. The computed T1 quotient also splits W. **Crucially:** if W is actually hidden, these separate T1 classes are *not* part of the allowed coarse current readout; condition (3) fails for that hypothetical coarse quotient. This accurately locates the causal-memory/readout deficit instead of pretending the algorithm restored W for free.

The earlier EC49E linear four-vector separator at cost c=1/8 has \(V_{coarse}=0\) and \(V_{fine}=3/80\). The new exact kernel audit identifies the specific pair of missing predictive distinctions, and the previous support proof supplies the actual observable-region separation. The **two individual marginal** LR spectra may match while the **conditional second-stage** LR kernel fails.

## 5. Verification coverage and unresolved work

`VERIFY.py` uses Python standard-library `fractions.Fraction`. It checks every leaf's positive source mass and normalization, all prefix LRs, exact Q and induced P kernels, the causal stage/LR readout of the safe quotient, and the nonimplementable W split in EC49E. It checks all **729** deterministic T1/T2 action patterns crossed with **eight explicitly specified terminal masks** (=**5,832** complete deterministic policies), plus **1,000** seeded rational random full-history policies; each full-history four-vector is reconstructed exactly in the safe quotient. These finite checks support the worked instances; the all-real policy theorem is the proof in §1, not an extrapolation from tested samples. Earlier EC49E support equality is reused at its exact proven scope.

The exact Q-kernel quotient gives a **sufficient** native-memory *design criterion*, not a proof that an observed weighted-BRC branch is a physical X6 state or that native signed amplitudes can be collapsed. The W-history carrier is an auxiliary relationship/provenance coordinate, not another native spatial axis. The clock T=1,2,3 is an experiment-decision counter and not a calibrated heartbeat interval. P000 and the ACTIVE X6 discrete worldview stay unchanged. An X6 transfer requires an explicit typed native state embedding, readout contract, causal action algebra, signed/phase BRC kernel and a future-operation preservation proof.

**Next EC49G:** investigate quotient conditions for **cost-sensitive action-dependent acquisition** (different sensors, adaptive schedules, source-indexed time increments), with a certified counterexample when preserving only action-marginal Q kernels and not their causal updates. Independently, the irrational-only rational target problem is now **restricted to non-lumpable / non-LP subclasses**; search the smallest source-neutral non-Markov rational model with a genuinely nonpolyhedral raw region and a rational point requiring irrational control, or prove further rational witnesses under a weaker hypothesis.