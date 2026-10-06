# Euler routing: variable memory, state feedback and robust observer bounds

Status: PROVISIONAL MODEL THEOREMS AND EXACT BRC CERTIFICATES / NOT FORMALLY ADMITTED.
Date: 2026-10-07 (Asia/Tokyo). Same-conversation continuation, not independent replication.
Global read snapshot: 51a83acfc90f6b6b18c572f3840f1754c6766a99.
Source read snapshot: 4eaa6d696b000ca522add69bfb5f1d748e4b9ead.
Prior mathematical frontier: fb325f11e26e6438f442312fd872c409b07f6c8c, research_notes/chatgpt_direct/20261005_EULER_MEMORY_KERNEL_SAFE_TRUNCATION.md, blob 044f35ec1ccea5a6b6e51412aff853d17fc5d6e8.
Logical conversation: chatgpt-heartbeat-euler-20261004-layer-01; not platform-attested.
Research activity: UNVERIFIED / REGISTER_PENDING; no borrowed identity or CLAIM.

## Scope and executed reuse

This unit studies the existing LOCAL three-channel contact, not the shared-field 35-state process. It does not change P000, six native spatial axes, independent time, or three-dimensional slice typing. Channel labels, routing signs and contact counts are not native spatial coordinates or calibrated heartbeat times. The rate rules below are candidate assumptions, not derived native forces.

The previous evidence archive has SHA256 67b7852db3f329dcc1195139c49b73155cd310837d1509f4f6bc96e023e14c38; all 68 manifest entries matched. Unchanged brc_memory_kernel.py (SHA256 6cdfd12ddf6b6b27de711c61156250506b6a37bca56e9f7ff11531d6e77dd628) imports unchanged brc_route_memory.py (SHA256 ce182a5861982d0e43120aeb15da06cf02c774300730975330a85ea86f3c979e). Every positive transition executes its existing contact function and the source CWM bodies. The current source brc_weighted.py blob remains 3f205696709e847909958a153f8fe10d3f6b70f0. Explicit paths retain binary triples, routing signs, positive CWM, root, choices and history. Histogram updates use the proved full-state key and actual CWM serial/merge calls.

Reuse: REUSE_EXECUTED for those kernels and their exact phase interface; EXTEND_EXISTING_TOOL for variable-rate observer certificates and PRE-contact rate selection. No new top-level BRC family is claimed. No numerical pi, trigonometry, square root, matrix exponential, Taylor/Pade/Cayley or alternative world propagator is executed. Rational observer recurrences are proved readout interfaces, not positive populations or Cell addresses.

Write omega=alpha^4, alpha^4-alpha^2+1=0. Then omega^2+omega+1=0 and omega^2=-alpha^2. For a binary triple x=(a,b,f), zeta(x)=a+omega*b+omega^2*f. P(x)=(f,a,b) multiplies this observer by omega; P^-1 multiplies it by omega^2. The unchanged contact uses the current sign, then keeps it with weight p or reverses it with weight 1-p. This ordering matters.

## 1. A prescribed common schedule is not a state-dependent rate

First let p_n be a prescribed common rational rate at contact n, shared by every branch. Put k_n=2p_n-1, ell=(omega-omega^2)/2, and let u_n,v_n be the unnormalized sign-conditioned phase sums. Set z_n=u_n+v_n and d_n=u_n-v_n. The existing BRC laws give

z_(n+1)=-z_n/2+ell*d_n,
d_(n+1)=k_n*(ell*z_n-d_n/2), ell^2=-3/4.

Elimination gives the exact nonautonomous recurrence

z_(n+2)=-p_n*z_(n+1)+(1-2p_n)*z_n.

It uses p_n, not p_(n+1): the rate chosen after one collision affects the next collision. Define G(n,j)=product over r=j,...,n-1 of (-k_r/2), with an empty product equal to one. Direct iteration gives

z_(n+1)=-z_n/2+G(n,0)*ell*d_0
 -(3/4)*sum over j=0,...,n-1 of k_j*G(n,j+1)*z_j.

Thus time-dependent memory contains products of the actual intervening rates. Replacing them by a power of an averaged rate is not justified. The identity does not require stationarity, independent initial preparation, or a constant parameter. If the schedule is computed from an aggregate state, an approximation must use the SAME schedule for this comparison; recomputing a different feedback schedule is outside this result.

## 2. All-future finite-window bound for arbitrary common switching

Assume total positive weight one and |k_n|<=K<1/2. Keep the initial term G(n,0)*ell*d_0 exactly, retain only the m most recent history corrections, and use approximate past outputs recursively. Each exact phase coefficient has absolute value at most one, since its four coefficients are (a-b,0,b-f,0) branchwise.

With q=K/2, the omitted one-step tail is at most delta_m=3K*q^m/(4-2K). The retained absolute feedback sum is at most a_m=1/2+3K*(1-q^m)/(4-2K)<1. Induction from zero initial error gives

sup_n ||z_n-ztilde_n||_infinity <= delta_m/(1-a_m)
 =3K*(K/2)^m / (2-4K+3K*(K/2)^m).

This includes propagated approximation error, not only a tail evaluated on exact history. K<1/2 is a sufficient condition for this proof, not an asserted necessity for every stable law.

In particular, arbitrary common switching inside 7/16<=p_n<=9/16 gives K=1/8 and the bounds

m=0,1,2,3,4: 1/5, 1/65, 1/1025, 1/16385, 1/262145.

Two retained corrections therefore suffice for coefficient tolerance 1/1000 within this schedule contract. The actual finite-window implementation stores the current coefficient tuple, at most m lag/coefficient pairs, and an initial-memory tuple. Fixed slots do not imply bounded rational bit length. At K=1/15 the formula reduces to the previous constant-case bound; that earlier theorem is not claimed anew.

## 3. An exact obstruction when the rate is selected by the occupied channel

Now restrict to unit-count triples e_A,e_B,e_f. Choose the rate from the PRE-contact occupied channel: p_A,p_B,p_f. It is the same for both signs at that channel. The new extension merely passes this selected rate to the unchanged contact function. There is no reset of the triple or manual change of its phase.

Start with weight 1/6 in each of the six channel/sign states. Then z_0=z_1=d_0=0. However, summing the actual sign-conditioned contributions gives

z_2=-(p_A+omega*p_B+omega^2*p_f)/2.

For rational rates this is zero iff p_A=p_B=p_f. Hence the previous homogeneous two-phase closure cannot hold for ALL preparations under a nonconstant pre-channel rate map: a zero pair (z,d) generates a nonzero next pair. This does not forbid an affine or enlarged-state representation.

Take p_A=p_B=1/2 and p_f=9/16. The law remains symmetric under interchanging the two recipients and reversing the routing sign. Its rates lie in the SAME interval used in section 2. Nevertheless

z_0=z_1=0, z_2=-omega^2/32=alpha^2/32.

Under ANY prescribed common rate schedule, the uniform six-state preparation remains uniform and has zero phase forever. Under the state-dependent law it does not. The interval-only common-schedule bound must not be transferred to this different action.

## 4. Stable nonzero phase, with a closed formula

More generally take p_A=p_B=a, p_f=b, with 0<a,b<1. Recipient-exchange symmetry permits joint masses in the order (A+,A-,B+,B-,f+,f-) of the form (x,y,y,x,z,z), x+y+z=1/2. One actual contact gives

x'=(1-a)*x+b*z, y'=a*x+(1-b)*z, z'=y.

These are positive endpoint-mass identities, not substituted numerical evolution. The stationary joint masses are

(b,a,a,b,a,a) / [2(b+2a)].

Its channel masses are ((a+b)/(2(b+2a)),(a+b)/(2(b+2a)),a/(b+2a)); its sign marginal is exactly fair. Its phase is

zeta_star=(a-b)*omega^2/[2(b+2a)].

The six-state support reaches every state from every state in three contacts whenever all rates are interior. If eta=min(a,1-a,b,1-b), every three-contact transition is at least eta^3. Splitting off 6eta^3 times the uniform kernel contracts the total-variation distance of two distributions by at most 1-6eta^3 per block. Thus the displayed stationary distribution is unique and globally attracting. For (a,b)=(1/2,9/16), a sufficient factor is 1019/2048 per three contacts. This is a mathematical contraction of endpoint distributions, not physical energy loss.

For any recipient-symmetric initial population of total weight one, the phase satisfies the exact AFFINE recurrence

zeta_(n+2)=-a*zeta_(n+1)+(1-a-b)*zeta_n+(a-b)*omega^2/2.

Proof: zeta_n=(3z_n-1/2)*omega^2 and z_(n+2)=a/2-a*z_(n+1)+(1-a-b)*z_n. Substitution gives the formula. It is not asserted for arbitrary nonsymmetric preparations.

For the uniform initial preparation and (a,b)=(1/2,9/16), this becomes

zeta_(n+2)=-zeta_(n+1)/2-zeta_n/16+alpha^2/32,
zeta_n=(alpha^2/50)*[1+(5n-1)*(-1/4)^n].

The first values are 0,0,alpha^2/32,alpha^2/64,11alpha^2/512,5alpha^2/256. The stationary joint masses are (9,8,8,9,8,8)/50 and the limiting phase is alpha^2/50, not zero. The repeated factor (lambda+1/4)^2 explains the linear prefactor in n. This is an exact candidate-state-feedback bias, not a finite-history truncation or rounding error. No physical gate/force law has been derived by assigning these rates.

## 5. Exact omitted correlation term and a robust replacement contract

Keep the nominal rate p0=8/15. In a true positive joint population allow a branch-specific rate p_n(path), with the same contact/sign-update ordering. Define

F_n=ell*sum_paths w*[2p_n(path)-2p0]*chi*zeta(P^chi x).

Then the exact TRUE phase obeys

zeta_(n+2)=-p0*zeta_(n+1)+(1-2p0)*zeta_n+F_n.

If p0 is instead chosen at that step as the branch-weighted mean, the analogous term is a covariance between rate and the sign-weighted post-collision phase. Zero mean rate deviation does not imply zero covariance. The original six-state histogram is sufficient for a policy depending only on its state key; hidden field/history-dependent policies require those data too.

For any normalized positive mixture of the eight binary triples, ||ell*zeta(P^chi x)||_infinity<=1 branchwise. Hence |p_n(path)-8/15|<=epsilon implies ||F_n||_infinity<=2epsilon. Compare to the nominal constant-rate BRC evolution from the SAME initial joint population. Initial phase errors e_0=e_1=0, and

e_(n+2)=-(8/15)e_(n+1)-(1/15)e_n+F_n.

The already-proved nominal impulse gains are g_r=(15/2)[(-1/5)^r-(-1/3)^r], r>=1. Their absolute sum is (15/2)(1/2-1/4)=15/8. The finite convolution with actual F_j therefore gives the new uniform bound

sup_n ||e_n||_infinity <= (15/4)*epsilon.

It allows arbitrary temporal and state-rate correlation subject to the bound, and is sufficient rather than claimed sharp over all realizable policies. It preserves the nominal contact law; unrelated interventions are outside the comparison.

Combining with the previous m-lag observer at the nominal rate gives

sup_n ||zeta_true,n-zeta_approx,n||_infinity
 <= (15/4)*epsilon + 3/(26*30^m+3).

Thus epsilon=1/10000 and m=2 guarantee an error below 1/1000. Increasing history length only reduces the second term; it cannot by itself remove uncertainty in the update rule. All bounds scale with total positive weight W. Input measurement errors, altered phase observers and new physical actions need separate contracts.

## 6. Validation and limits

Final suite: 155605 exact assertions, including 68 prior-manifest checks. Coverage: all 16 binary channel/sign atoms; all 64 six-contact schedules over the interval endpoints plus two schedules using rates 0 and 1 for identity-only checks; all 63 nonempty normalized unit-sector supports under four common schedules through 32 contacts; 27 pre-channel rate maps; 25 symmetric parameter pairs; three recipient-symmetric initial orbits through 16 contacts; a 48-contact bias trace; three uncertain/state-dependent policy families on all 63 supports; explicit labelled/whole-state CWM agreement and 2044 inverse-channel checks through eight contacts.

Actual existing source calls: cwm_edge 468696, cwm_propagate 619816, cwm_recoalesce 341150. New state-policy adapter rows: 49046. These are assertion/call counts, not independent experiments. The preliminary 154430-assertion stage preceded the affine closed-form proof; final revalidation is not a second replication. No prior research suite was rerun as new science. One shell redirection failed before Python ran because a log directory was absent; it was corrected and recorded. The final process exited zero; the unrelated terminal warning is retained.

New brc_variable_memory.py SHA256 0c0da19d37971bdebfffdf884b4fae8691f94498070c5e6c43ae5c0e7fbecb49.
New check_variable_memory.py SHA256 5bb99e16e82cef9fcf364f5ed65c47a93c488bb796f84fe3c86a51aa5cba17eb.
Run python check_variable_memory.py from the conversation evidence package using Python3.10+ and the standard library. Complete code, exact prior dependencies, logs, traces and manifest are in the attachment. Source stores this proof and verification frontier; it does not claim every execution-package byte is newly stored there.

General exact Markov aggregation has established literature: Jacobi and Goernerup, arXiv:0710.1986v2, and Sonnentag, arXiv:2507.11157v1. Only their public primary-source abstracts were read for background attribution; no theorem from an unread full paper or literature-wide novelty claim is used. Dedicated literature capability metadata was inspected, but no unexposed provider operation was invented or claimed executed.

Current control status request #2759 (status-20261007-euler-variable-memory-18) still exposes the service-local pointer MCP-74124c48a87440a6b56f5f440f7e9493 from the earlier failed registration. Its Source session record at the current pin again returned404. No duplicate registration, rejected-prerequisite replay, CLAIM, new role identity, independent review, accepted Result or successful final guard is claimed. Earlier safety-blocked payloads were not retried.

Completed unit: nonautonomous memory products and robust truncation; pre-channel feedback obstruction; symmetric nonzero stationary phase and exact transient; correlation-source equation and combined all-future uncertainty/truncation bound. The next scientific gap is to supply an actual sourced incoming-field law that determines these conditional rates, or to add its evolving state and verify a joint closure. More history alone cannot identify that law. Local observer results do not automatically transfer to the earlier shared-field world or physical time/energy.
