# Euler feedback: finite reversible microstates, exact horizon cost and safe quotients

Status: PROVISIONAL MODEL THEOREMS AND EXACT BRC CERTIFICATES; NOT FORMALLY ADMITTED.
Date: 2026-10-07 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: e94f40eef06dc27555c084adfc308518c34419cc.
Source read snapshot: 762dc5c1d86bee0a63858686866c9df36a13c147.
Prior frontier: 36d1e43e67db9011ed5692789a84cf373c20fe40, research_notes/chatgpt_direct/20261007_EULER_VARIABLE_MEMORY_STATE_FEEDBACK.md, blob bb375b97413dfee0f10ecd298e8bbfc05e51f050.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Activity: UNVERIFIED / REGISTER_PENDING. No old identity, CLAIM or theorem admission is borrowed.

## 1. Scope and executed reuse

This unit concerns the prior LOCAL unit-count three-channel/sign model, not physical X6 motion or the earlier shared-field 35-state system. The six coarse states are ordered A+, A-, B+, B-, f+, f-. Recipient exchange swaps indices 0/3, 1/2 and 4/5. The exact unchanged collision is P(a,b,f)=(f,a,b), or its inverse according to the current sign; only then is the next sign retained or reversed. The prior PRE-channel rates are (1/2,1/2,9/16).

All dynamics here execute the unchanged brc_route_memory.contact and positive CWM bodies through the previous brc_variable_memory interface. The previous archive SHA256 is b2df5cbd485ad5731323b8649a00cbac9c93d330ab44553e2c126886c51553a5; all 80 manifest entries matched. brc_variable_memory.py SHA256 is 0c0da19d37971bdebfffdf884b4fae8691f94498070c5e6c43ae5c0e7fbecb49; the underlying route module SHA256 is ce182a5861982d0e43120aeb15da06cf02c774300730975330a85ea86f3c979e. The current source brc_weighted.py blob remains 3f205696709e847909958a153f8fe10d3f6b70f0. Existing source bodies, not a replacement numerical propagator, carry every positive path transition.

Reuse: REUSE_EXECUTED for contact, positive weights and phase; EXTEND_EXISTING_TOOL for an explicit finite internal microstate. This is an inverse construction from a given transition law, not a derivation of that law from native forces. Sorting/matching conventions below are declared model data. Internal tickets, channel/sign states and contact counts are not spatial dimensions, Cell addresses or physical clock readings. P000 and source residual-fidelity constraints remain unchanged. No numerical pi, trigonometry, roots, matrix exponential or other classical reference propagation was used. Finite graph and denominator computations audit BRC-generated histories.

## 2. A one-contact microscopic realization has a sharp counting constraint

Let K be the existing six-state endpoint transition matrix, with rows indexed by the source state. Its nonzero entries, obtained by actual BRC contact, are:

0 -> 2,3 with weights 1/2,1/2;
1 -> 5,4 with weights 1/2,1/2;
2 -> 4,5 with weights 1/2,1/2;
3 -> 1,0 with weights 1/2,1/2;
4 -> 0,1 with weights 9/16,7/16;
5 -> 3,2 with weights 9/16,7/16.

The prior unique stationary distribution is pi=(9,8,8,9,8,8)/50.

Declare the microscopic realization contract: a finite set Omega, a permutation T of Omega, a projection q onto all six states, and uniform preparation within each fiber Omega_x=q^-1(x). Its one-contact projected probabilities must equal K for every initial x. Put d_x=|Omega_x| and N=|Omega|. Then the integer transition count from x to y is d_x K_xy. Since T is a permutation, counting arrivals gives dK=d. Uniqueness of pi forces d=k(9,8,8,9,8,8), N=50k, with integer k. The field departure count 8k*(9/16)=9k/2 requires k even. Therefore N is a multiple of 100, and N=100 is achievable.

Equal-sized fibers are impossible under this contract: the column sums of K are (17/16,15/16,15/16,17/16,1,1), not all one. This is not a prohibition on unequal microscopic weights, nonuniform environment preparation or open-system dynamics.

At the minimum, d=(18,16,16,18,16,16), and all twelve nonzero edge counts are integers. For example, 18 A+ microstates divide 9/9 between B+/B-, while 16 f+ microstates divide 9/7 between A+/A-. Thus a deterministic internal choice can reproduce the prescribed fractions for one freshly prepared contact. The fractions were the design target; their physical origin remains unknown.

## 3. Explicit symmetric reversible construction and a differing future

For one contact use one ticket (x,y,j) for each of the d_x K_xy copies of a directed edge x->y. At each vertex v, incoming and outgoing ticket counts agree. Match their sorted lists bijectively. Do this at one vertex from each recipient-reflection pair, and obtain the partner matching by reflection. A ticket entering v maps to the matched ticket leaving v. This defines a permutation commuting with recipient reflection. The observed current state is the source of the current ticket.

Every microscopic step uses the old contact with persistence 0 or 1 selected by the next ticket; its binary-channel update, positive weight and provenance are checked. The hidden update is the matching permutation, not a manual phase change. All 100 states are covered. The specified sorted matching has 23 cycles of length four and one of length eight. Cycle/history return does not reset elapsed time or audit records.

Prepare each coarse state with weight 1/6 and distribute it uniformly across its own fiber. Then each of the 18-member fibers has microscopic weights 1/108, while each 16-member fiber has weights 1/96. This is not the uniform measure on Omega. Both the microscopic model and the old Markov rule start with the same full six-state marginal.

Write omega=alpha^4, alpha^4-alpha^2+1=0, and observe zeta=a+omega*b+omega^2*f. The microscopic phase repeats exactly:

zeta_0,zeta_1,zeta_2,zeta_3 = 0,0,alpha^2/32,alpha^2/32,
followed by the same four values.

The old feedback law instead has initial phases 0,0,alpha^2/32,alpha^2/64,11alpha^2/512,... and converges to alpha^2/50. Its full six-state distribution already differs at contact two, though the phase still agrees there. The first phase discrepancy is at contact three. The four-period claim follows from the full eight-period permutation together with the verified four-period prepared endpoint distribution. The microscopic phase average on this prepared orbit is alpha^2/64, not alpha^2/50.

Uniform weight 1/100 on all microstates IS stationary under the permutation. Its coarse weights are pi and its phase is exactly alpha^2/50 at every time. This gives a precise multiplicity interpretation of the nonzero centroid: channel multiplicities are 34,34,32. A stationary uniform microscopic ensemble does not make that centroid globally attracting. Which invariant microscopic components are populated matters.

## 4. Exact agreement for H contacts has a sharp finite resource law

Strengthen the contract: from uniform preparation in each fiber, reproduce the entire ordered joint law of H future coarse states for every initial coarse state, not merely the final phase or one-time marginals. Under global microscopic uniform preparation the initial coarse law is pi. Every stationary word w=(x_0,...,x_H) therefore has probability

p(w)=pi_x0 K_x0x1 ... K_x(H-1)xH,

and N p(w) must be an integer. Hence the lcm of all these denominators divides N.

For this particular K the lcm is exactly

N_(2k)=25*2^(5k-2), for k>=1;
N_(2k+1)=100*32^k, for k>=0.

Thus H=1,2,3,4,5,6,7,8,9,10 require at least
100,200,3200,6400,102400,204800,3276800,6553600,104857600,209715200
uniform microscopic states, respectively.

Proof of the exact denominator: let v count field-channel departures among the H steps. Each contributes an odd numerator over 16; every other departure contributes 1/2. If x_0 is A+ or B-, its stationary weight is 9/50, so the word denominator is 25*2^(H+3v+1). Such a start cannot reach a field departure until step index two, so v<=floor((H-1)/2). For other starts the stationary weight is 4/25, and the denominator divides 25*2^max(H+3v-2,0), with v<=ceil(H/2). These yield the same displayed bound for each parity. The allowed alternating word f+,A-,f+,A-,... attains it: its transition numerators are 7 and 1, and no factor five or two can cancel the maximum denominator.

Sharp construction for any H: use overlap vertices (x_0,...,x_(H-1)) and directed edges w from its prefix to its suffix, with multiplicity N_H p(w). Stationarity balances incoming and outgoing counts at every overlap vertex. Match tickets as above. The resulting permutation preserves the overlap, so its first H+1 observed symbols are exactly the stored word. Uniform preparation in a fiber gives the required conditional word law. Recipient reflection has no fixed overlap vertex, so matching reflected pairs ensures symmetry without increasing N_H. The implementation constructs the minimum at H=1,2,3; denominator and sharp-word certificates were executed through H=10. The general conclusion has the preceding proof, not an extrapolation from these tests.

This is a sharp minimum only for the stated uniform-counting, reversible, full-word contract. It is not a universal physical memory bound, a lower bound for arbitrary weighted hidden preparations, or a phase-prediction storage bound.

Even without equal weights, a fixed known coarse start with D deterministic hidden states can generate at most D different H-step words. The stochastic model has 2^H positive words, so exact full-word reproduction requires D>=2^H. For total-variation error at most delta, every word has probability at most beta_H=(9/32)^floor(H/2)*(9/16)^(H mod2), since consecutive field departures are impossible. Missing support gives TV>=1-D beta_H, hence D>=(1-delta)/beta_H. These statements concern complete path laws, not the small phase-only recurrences already available.

## 5. What an implicit reset changes

Let C project a microscopic measure to coarse states, U distribute each coarse weight uniformly within its fiber, and E=UC. Then CU=I and the one-contact coarse rule is K=C T U. Closed microscopic evolution is C T^n U, not generally K^n. Reapplying the conditional uniformization after each contact gives C(ET)^n U=K^n.

Uniformization is an additional positive branching operation. It is not the same thing as leaving an unobserved internal state unchanged, and it is not an invertible update on the reduced ticket state. The implementation retains the source/audit records of these reset choices. Its endpoint masses match the old Markov law; its branch counts need not match that law's two-way branching counts.

In signed observer coordinates, rho=U mu+eta with C eta=0 gives mu_next=K mu+C T eta. The closure defect is the transported within-fiber correlation. This applies the already established memory principle to an explicit finite microscopic realization, rather than naming an unexplained error.

The actual reset implementation and a whole-microstate CWM quotient were tested through twelve contacts against the unchanged feedback rule. No physical mechanism or cost of resetting is assumed free. A larger initially prepared environment can postpone the mismatch without an explicit reset, at the horizon-dependent resources in section 4.

## 6. Counting atoms and minimum predictive states are different

For the specified 100-state matching, all microscopic orbits divide eight. Two states have identical future coarse observations iff their eight-symbol traces agree. There are exactly 20 such classes: eight classes of multiplicity eight, four classes of multiplicity seven, and eight classes of multiplicity one. Their future transition is deterministic and closed. All 190 class pairs differ somewhere in their eight-symbol trace, so 20 is the minimum deterministic predictive quotient of THIS microscopic rule for exact coarse-state observations. It is not a minimum over all microscopic realizations.

The original count 100 remains 8*8+4*7+8*1. It is not legitimate to replace these classes by twenty equal-weight states. Keeping class multiplicities and using actual CWM addition preserves path count, total weight and largest individual path weight for the declared history-blind future. The quotient was checked against explicit microscopic paths. Source-sensitive or ticket-sensitive controls require a new equivalence test.

This does not conflict with section 4: that theorem counts equal-weight underlying states while this quotient stores unequal multiplicities. Nor does it invalidate earlier two-coefficient or finite-memory phase predictors, which answer a narrower observation question.

## 7. Evidence, prior work and remaining native obligation

Final suite: 73,012 exact assertions, including 80 prior-manifest integrity checks. Coverage includes BRC-generated stationary histories through H=10; maximum-word and lcm certificates; all microscopic states of the minimum H=1,2,3 constructions; overlap words, inverse, source identity, count conservation and recipient symmetry; all six initial fibers; the four-period counterexample and stationary centroid; explicit/whole-state CWM equivalence; reset comparisons; the complete 20-class predictive quotient. Actual source calls: cwm_edge 70,742, cwm_propagate 87,110, cwm_recoalesce 32,481; existing contact 29,898. The preliminary 72,631-check stage preceded the predictive-quotient unit, not independent replication. Both suite processes exited zero; an unrelated terminal warning is retained. No prior research suite was replayed as new progress.

General deterministic environmental dilation and exact aggregation have prior literature: M. Gregoratti, Classical dilations a la Quantum Probability of Markov evolutions in discrete time, arXiv:math/0702690 (primary search abstract and SIAM abstract); B. Geiger and C. Temmel, Lumpings of Markov chains, entropy rate preservation, and higher-order lumpability, arXiv:1212.4375v6 (official abstract). No unread full-paper theorem is used to justify the new counts, and no literature-wide novelty is claimed.

The supplied code and certificates give a finite inverse model of the prescribed conditional rates, not their native origin. An actual incoming field must supply both the admissible microscopic relations and their preparation/continued updating. Matching one contact, matching finitely many full histories, predicting only Euler phase, and deriving a physical force law are different achievements.

Current own status request: private bridge #2827, status-20261007-euler-microstate-lift-19. Its successful status receipt still identifies the same service-local session pointer from the earlier failed registration; status alone supplies no Source-bound activity or mathematical authority. No duplicate registration, rejected-prerequisite replay, new role identity, CLAIM, review or successful final gate is asserted. Earlier safety-blocked payloads were not retried. Project storage and this attachment are scientific continuity, not formal admission.

Next precise gap: test a sourced native incoming-channel structure against the microscopic multiplicity and history requirements, without fitting its hidden multiplicities solely to the target K. For a finite-resolution field, a reduced phase-only or finite-horizon error contract may be appropriate; full independent history reproduction must not be silently assumed.
