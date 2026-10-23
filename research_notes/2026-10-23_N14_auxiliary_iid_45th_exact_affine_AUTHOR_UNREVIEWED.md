# N=14 auxiliary iid BRC sequential test — 45th exact affine interval (AUTHOR-LEVEL, UNREVIEWED)

Date: 2026-10-23. **Scope**: finite horizon N=14 three-symbol iid sequential hypothesis testing **only**. This research note is a durable author artifact, **not** a formal Enterprise Math Task Result, native CLAIM, independent Research Driver review, Working Truth, Foundation acceptance, P000 proof or native BRC/X6/Heartbeat correspondence. Keep the 44th exact author certificate as a mathematical dependency, not an independent acceptance.

## Precise question and model

Under P=(3,1,20)/24 and Q=(2,2,20)/24, an arbitrary randomized stopping rule may stop by time 14 and decide P or Q, with ordered-history dependence. Let E_P=P(decide Q), E_Q=Q(decide P), T_P=E_P[stopping time], T_Q=E_Q[stopping time]. Define V_14(alpha)=inf_{E_P,E_Q<=alpha} max(T_P,T_Q). At count state (n,a,b), n=length and a,b are the numbers of symbols 0 and 1; L=Q(prefix)/P(prefix)=2^(a+b)/3^a.

From the 44th author certificate: alpha44=5171815348217925797/14900301753911083008, V44=193782614607902809/14551075931553792; the equilibrium early-Q probability at B=(12,0,1) is s44=26391957913028113/41779200000000000. The 44th stop set includes early-Q at (4,0,3); the inherited certificate is not source-reviewed. Its original archived ZIP SHA256 was fe37f9c714d83dbca6426a3d4c3ffb5cab36e3d8434cd5c389b44e405ffa417a.

## Main author-level theorem

Let K45=1320948/47, lambda_P=1177560/47 (=72+8*K45/9), lambda_Q=1320948/47, Gamma45=2498508/47, and eta45=1615625/538928738205696. For every rational or real delta with 0<=delta<=eta45,

  V_14(alpha44+delta) = V44 - (2498508/47)*delta.

Its **45th exact endpoint** is

  alpha45 = 5171815392886725797/14900301753911083008
  V_14(alpha45) = 193780295680165309/14551075931553792
  approx V_14(alpha45)=13.317248607022634.

Beyond alpha45 this particular supporting affine line cannot still be attained by any feasible rule. The statement DOES NOT claim subsequent intervals are absent.

## Global finite Bellman dual bound

For the Lagrangian T_P + lambda_P E_P + lambda_Q E_Q, use P as reference measure and recurrence

  D[n,a,b] = min( lambda_Q*2^(a+b)/3^a,
                  lambda_P,
                  1 + P0*D[n+1,a+1,b] + P1*D[n+1,a,b+1] + P2*D[n+1,a,b] ),

omitting the continue term when n=14. The first term is early decision P (Q error), the second is early decision Q (P error). Exact Fraction dynamic programming finds 680 finite count states and checks 1240 nonselected action differences: 1238 strictly positive, exactly two zero differences:

  A=(11,6,1): continue = decide P
  B=(12,0,1): continue = decide Q.

At the root D[0,0,0] = 190163946937075330788271/10298737976967954432 = V44 + Gamma45*alpha44. Thus ANY randomized, even full-history-based rule satisfies max(T_P,T_Q)>=T_P>=Droot-lambda_P*E_P-lambda_Q*E_Q >= V44+Gamma45*alpha44-Gamma45*alpha. This is a global certificate, not just a local strategy comparison.

## Ordered-history reachability and conditional exact suffixes

A has nominal binomial count 11!/(6!1!4!)=2310 ordered histories. Evaluate the *first* stopping decision under all inherited earlier rules, rather than conflating count states with live prefixes. Exactly 1980 are live, 330 already stopped; the stopped counts by ancestor state are (6,6,0):5, (7,6,0):24, (8,6,0):63, (9,6,0):112, (10,6,0):126. Forward propagation of live P and Q weight independently gives:

  p_A=34375/226492416 ; q_A=34375/1289945088.

If we continue at A, enumerating every one of the 27 ordered three-symbol suffixes gives conditional vector (P-error,Q-error,P-further-samples,Q-further-samples)

  (cP_A,cQ_A,tP_A,tQ_A) = (1/13824,1727/1728,601/576,157/144).

B has 12 live ordered prefixes and

  p_B=48828125/725594112 ; q_B=48828125/362797056,
  (cP_B,cQ_B,tP_B,tQ_B)=(63/64,1/144,9/8,13/12),

as checked by all nine two-symbol suffixes. Dummy suffixes after stopping are integrated at their full measure (never multiply an already stopped prefix's probability by the number of remaining words).

The branch source with its order/weights/first-stop status matters: nominal A count 2310 alone is an UNSAFE quotient that would incorrectly retain 330 dead branches. This is an actual positive-rational, labeled-provenance BRC observer application, not a claim of native signed/phase cancellation.

## Primal construction and equality

Choose early P at A with probability u in [0,1], and choose early Q at B with probability s; all other inherited actions remain fixed.

Set
  D=p_A*cP_A=34375/3131031158784;
  W=q_A*(1-cQ_A)=34375/2229025112064;
  E=p_B*(1-cP_B)=48828125/46438023168;
  H=q_B*cQ_B=48828125/52242776064.

Increment u changes (E_P,E_Q) by (-D*u,+W*u). Increment Delta_s changes (E_P,E_Q) by (+E*Delta_s,-H*Delta_s). Therefore balance both error sides uniquely by

  s=s44+h45*u;   h45=(D+W)/(E+H)=57849/4352000000.

For all u in [0,1], 0<s<1. Both errors then satisfy

  E_P=E_Q=alpha44+eta45*u,
  eta45=-D+h45*E=W-h45*H=1615625/538928738205696.

The P-expectation decrement is
  T_P(u)-T_P(0) = -(p_A*tP_A+h45*p_B*tP_B)*u
                 = -2385728125/14970242727936*u = -Gamma45*eta45*u;

and the Q-expectation decrement is
  T_Q(u)-T_Q(0) = -12526971875/404196553654272*u.

Both T_P(0)>=T_Q(0) and T_P(1)>=T_Q(1), the latter by exact difference
  T_P(1)-T_Q(1)=1805488840366522333/3725075438477770752 > 0.
Both expectations depend affinely on u, hence T_P>=T_Q for the whole interval. The constructed strategy attains the global dual bound at alpha=alpha44+eta45*u, proving the theorem.

## Sharpness beyond the endpoint

Equality with the positive Bellman multipliers forces all actions other than the two exact zero-gap ties to be excluded on positive-probability reachable states. A and B are prefix-incomparable: A has a=6; B has a=0 with longer length. Even if the policy chooses different mixing for different ordered histories at one count state, all those histories have the *same* Q/P likelihood ratio, so they can be collapsed to one effective u at A and one effective s at B for these four observables. Since both positive-lambda error constraints must be tight, the two error changes enforce s=s44+h45*u. The only possible common error is alpha44+eta45*u; u<=1 implies alpha<=alpha45. Thus equality on the old supporting affine line is impossible for alpha>alpha45.

## Exact checker and independent-author crosscheck

Main author verifier used Python fractions.Fraction, enumerating 680 reachable count states, 1240 Bellman alternatives, 2310 nominal A histories and 27 A suffixes, checking also forward joint path-mass propagation and five randomization values u in {0,1/4,1/2,3/4,1}. Second author-side checker independently recomputes the four extreme-parameter absorption distributions and backpropagates the Bellman minima, without importing the main verifier; shares the inherited 44th author source and research context. Fresh ZIP extraction rerun and manifest checks regenerated an identical certificate. Distinguish this from a genuinely independent Driver review.

Local complete reproducible bundle: EM_R5_BRC_N14_FORTYFIFTH_POSTCRITICAL_AFFINE_20261023.zip
SHA256: 3be1ebc238e7d464117d6e054bc7d222c07fbb5407ab1916c9f00373cc9317e8.
Contents: PROOF.zh-CN.md, PROOF.en.md, verify_n14_fortyfifth.py, verify_n14_fortyfifth_crosscheck.py, certificate_n14_fortyfifth_affine.json, inherited_certificate_n14_fortyfourth_affine.json, logs, provenance, SHA manifest and next task.

Mathematical status: AUTHOR_PROVED_EXACT_FINITE_AUXILIARY_MODEL / TWO_AUTHOR_IMPLEMENTATIONS_REPLAY_PASS / INDEPENDENT_DRIVER_UNREVIEWED / NATIVE_TRANSFER_UNPROVED.

## Next smallest unfinished unit

Candidate K46=15422430942/577175, proposed next tie A46=(8,7,1) with continue=decide P and B still continue=decide Q. This is a **dual candidate only**, not a proven 46th interval. Compute A46 live ordered-history count and P/Q masses under the *complete* 45th endpoint stopped tree, suffix risk/length tuple, balance compensation at B, first admissible u range, next endpoint, and the global Bellman dual/root/sharpness certificate. Use exact rational arithmetic and retain provenance.

## Fixed authority pins and publication boundary

Account knowledge fixed for this research computation: awdawmip/chatgpt-global-knowledge main@c0063368858bfea93f5bda62c8f43039d03a1f0e (GLOBAL_KNOWLEDGE_V1).
Starting project Source: awdawmip/enterprise-math main@2f8b170c87f643c4f1291f8aacf975520a0c7d1a.
P000 startup projection verified against original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
Authenticated GitHub connector: awdawmip. Direct native em_control_tasks reported CONTROL_QUOTA; gateway research_authority_granted=false; owner and formal CLAIM unverified. Persist this as an explicit **unreviewed research note only**. Source registration activity: research_activity_records/RA-R5N14-20261023-RESEARCH5-T11.json. No assertion of full formal task/result admission.
