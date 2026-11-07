# EC49N — Uniform-menu action coding versus sensor-destroying actions

**Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. Independent author-side portable research; not native CLAIM, Result, independent Driver admission, signed BRC or X6 theorem.
**Local identity:** R4-AUTO11-EC49N-20261028-2325-LOCAL. Native Researcher/Owner is unverified (gateway returned authority_granted=false; active-task query returned CONTROL_QUOTA).
**Frozen canonical inputs:** GLOBAL_KNOWLEDGE_V1 main@05b476005671b3ac9f4cfff09ff08db977cc9e42; Enterprise Math main@35b25780e54fb34378f305e2b3bd06fe7f782f92. Canonical P000 projection matches original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Current ACTIVE worldview and P000 remain unchanged.
**Predecessor:** EC49M PR #1648 at immutable f8078636e0f91632a8bc2394a344238de40b6d51. This deliberately removes calibrations, uses identical first-action menus for both W histories and allows early termination/acceptance.

## Model — two strictly positive source-labelled probability branches

Two statistical source measures P,Q have P(W=U)=P(W=V)=Q(W=U)=Q(W=V)=1/2. Each source samples two binary *potential* signals (Y0,Y1), conditionally independent given W; only the selected Y_A may be observed. Exact selected-signal probabilities:

| W | P(Y0=1|W) | Q(Y0=1|W) | P(Y1=1|W) distorted | Q(Y1=1|W) distorted |
|---|---:|---:|---:|---:|
| U | 1/4 | 3/4 | 1/2 | 1/2 |
| V | 3/4 | 1/4 | 1/2 | 1/2 |

The distorted model uses the displayed Y1=1/2 columns. The neutral comparison instead sets each source's Y1 conditional law equal to *its own Y0 conditional law*, at every W. Each model/source has eight strictly positive rational joint atoms (W,Y0,Y1) of mass (1/2)Pr(Y0|W)Pr(Y1|W).

Identical legal operations for both W histories and both observer classes: initially, after W, ACCEPT or REJECT at cost T=0, or choose A=0 or A=1, adding 1 to T. After A, ACCEPT or REJECT with no sensor, or BUY selected sensor Y_A adding 1 to T. After BUY, accept/reject based on observed Y_A. All decisions may use arbitrary *real* fresh source-independent behavioral probabilities; full observer retains W and own A, compressed observer retains own A but forgets external W. Observation target is the original raw four-vector O=(P(accept),Q(accept),E_P T,E_Q T); T is an auxiliary decision cost, not native time. W and joint potential signals are retained as source-labelled Weighted-BRC positive masses prior to the declared forgetting quotient.

## Theorem A — exact uniform-menu memory loss despite unrestricted early acceptance

**Statement.** For distorted actions, over every permitted real behavioral policy, the sharp support values of L(O)=alpha-beta are:

- sup L over compressed histories remembering A: **1/4**;
- sup L over full W histories: **1/2**.

Therefore a full-memory original four-vector lies outside even the convex hull of the compressed four-region, with *sharp support gap 1/4*. One additional external W bit is sufficient and necessary for full four-region preservation in this exact fixed protocol, keeping own A.

**Proof.** Let p_U,p_V be the probabilities of choosing A=0 after W=U,V, respectively. These are any numbers in [0,1] and already allow any competing first-stage early accept/reject/A1 probabilities. Initial W is source-neutral, so any initial accept/reject has P-Q acceptance difference zero. P(A=a)=Q(A=a) because source-independent action selection operates on W with equal P/Q W masses; therefore any pre-buy acceptance after A also contributes zero. All A=1 selected outcomes are source-neutral fair bits under both sources, hence acceptance conditional on A1,Y1 cannot affect alpha-beta.

For the only informative retained action A=0, source-labelled summation yields
P(A0,Y0=0)-Q(A0,Y0=0)=(p_U-p_V)/4=:d,
P(A0,Y0=1)-Q(A0,Y0=1)=-d.
The compressed BUY probability b0 is the same after A0 whether W=U or V; terminal accept probabilities r00,r01 are shared by the corresponding (A0,Y0) cells. Hence *for all real policies*
alpha-beta=b0*d*(r00-r01) ≤ |d| ≤ 1/4.
The pure compressed policy U→A0, V→A1; BUY iff A0; accept iff A0 and Y0=0 has O=(3/8,1/8,3/2,3/2), reaching L=1/4.

For full recall, initial/early accept and A1 all have zero P-Q advantage. For each W, buying Y0 can contribute at most the positive part of its two source-labelled outcome differences, equal to 1/4. Summing over U and V gives L≤1/2 for *every* full policy, including real randomization. The pure full strategy choose A0 and BUY after both W, accept exactly (U,Y0=0) or (V,Y0=1), yields O=(3/4,1/4,2,2) and L=1/2. The strict linear support certificate excludes this full four-vector from conv(S_compressed). Retaining W as one binary external memory bit lets the compact controller exactly reproduce all full conditional decisions and four outcomes; zero extra bits fail by the separator, so one is minimal for the declared full raw four-observable target. Both histories have exactly the same first-action menu; no calibration branches are present.

## Theorem B — neutral own actions are an exact external-history code

**Statement.** In the neutral-action comparison, S_compressed=S_full as *raw four-dimensional sets* for all real source-independent fresh behavioral policies, even with early acceptance before any sensor purchase. Moreover, every rational four-vector in this common region is reachable by a *fully rational fresh behavioral compact policy*.

**Proof.** Because A0 and A1 have equal conditional selected-signal laws given each W under each source, equal action cost and the same downstream interface, replace any full policy's first action upon continuation by the deterministic code U→A0, V→A1. Keep its W-dependent initial ACCEPT/REJECT/continue probabilities. After the new coded A, the controller knows which W occurred. For that W, average the old full policy's random A and downstream early-accept/reject/BUY probabilities, and after BUY and observed Y average its terminal acceptance over original pre-Y action choices that led to BUY. These averages are source-independent because the original controlled action probabilities are source-independent and both actions have the *same selected Y law for each W and source*. Thus the new compact fresh-behavioral policy gives the same probability distribution of (accept,T) under P and under Q. This is distributional observer equivalence, not literal identity of the unused potential Y variables. Full recall can simulate compact policies, proving both inclusions.

For the rational claim, full perfect recall has a finite list of deterministic complete plans whose four-vectors are rational. A rational vector in their convex hull has a rational nonnegative solution of the finite rational linear feasibility system. Perfect-recall mixed-to-behavioral conversion yields rational full behavioral probabilities; the explicit code/averaging uses only rational sums and conditionals, hence rational compact behavioral probabilities. A rational-target/irrational-only parameter obstruction cannot exist *for this exact neutral-action interface*. This does not settle the corresponding question for the distorted-action interface.

**Sufficient generalization.** If a finite W set of size m has at least m interchangeable action labels available on every W history; each label has identical conditional future observation kernels under both sources, equal costs and identical continuation menus; and the four-vector ignores the action name, then encode W injectively in the first chosen action and obtain the same raw-region equality. The distorted case is a strict counterexample if one omits the equal-kernel premise.

## Exact verifier, evidential strength and remaining obligations

Executed standard-library Fraction checker VERIFY.py generates EXACT_REPORT.json. For *each* model it exhaustively evaluates 2,304 compact deterministic policies: 4 initial choices per W × 3 post-action choices per A × 2^4 terminal maps. For full recall it exhaustively evaluates 196 distinct *induced* deterministic outcome plans (14 choices per W, two W): each W has ACCEPT/REJECT or A0/A1 followed by early ACCEPT, early REJECT, or BUY and four binary terminal accept patterns. This is 5,000 enumerated deterministic policies across both model variants, explicitly not all syntactically redundant full plans at unreached nodes. Exact masses, normalization, all four observables, two separating witness vectors, and support maxima are checked. The continuum statements are proved by the displayed real-variable inequalities and explicit controller compilation, not inferred from enumeration.

The distorted model's pure four-vectors number 35 compressed, 37 full; supports are 1/4 and 1/2. The neutral model has 29 distinct pure four-vectors for both policy classes, verified to be the *same set*; its raw-set equivalence relies on the constructive theorem. This is a finite strictly positive **auxiliary probability** BRC model; no signed cancellation, X6 physical state/address, three-dimensional slice, native rotation, physical heartbeat time or X6 interface is proved. General multi-stage action-dependent sufficiency, the rational target question in a distorted forgetting controller, independent replication and native typed transport remain open. External POMDP/Blackwell/Kuhn theory is background, not a novelty-priority claim.

Next EC49O: three or more W histories, two adaptive priced sensors; characterize controlled W coding, minimal causal external memory and any rational-only-realization obstruction with all pre/post terminal decisions admitted.