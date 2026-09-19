# BRC-Shor: interval observers and guarded conditioning

Event-ID: brc-shor-interval-conditioning-20260920-6EF011
Researcher-ID: EM-DIRECT-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE, same-author derivations and finite checks; no independent review, Lean or admission.
Source read: enterprise-math@a888bcdfd0a9714489eb5f368b3356a0ff321fb1. Inherited standalone head5831ae8bed5af3da68dffac28a919ed677fc1c70.

## Exact scope and result

Uniform exponent input, unit a modulo N, Q=2^m, ideal QFT, unconditioned second register and numeric output K. Reuse unchanged stage7 character oracle Q*chi(d)=(Q-d)[a^d=1]+d[a^(Q-d)=1] for0<d<Q.

A leading t-bit prefix is one interval I=[l,l+R), not t separately multiplied bit indicators. Its coefficient is c_I(d)=exp(-2*pi*i*d*l/Q)*sum_{j<R}exp(-2*pi*i*d*j/Q)/Q; Pr(I)=R/Q+sum_{d!=0}c_I(d)chi(d). With v=min(d,Q-d), |c_I(d)|<=min(R/Q,1/(2v)). The latter bound follows from the geometric series and sin(pi*v/Q)>=2v/Q.

Sample m equal tickets: one Nyquist frequency Q/2; one for each signed shell2^h<=v<2^(h+1), h0..m-2. Inside shell h the reciprocal probability is m*2^(h+1). Hence |c_I/q|<=m. No Q-entry support is enumerated. The real signed estimator has known DC R/Q and envelope A<=m, independent of the number of prefix bits. For dyadic R=2^s<Q, two tickets for signed1<=v<Q/R, s-1 shell tickets, and one Nyquist ticket give A=s+2 when smaller. Singleton intervals use flat frequency draws with A=1. This removes the product-of-one-bit-envelope penalty, not the cost of exponentially fine probability accuracy.

A fixed list of interval probabilities has additive probe complexity O(A^2/alpha^2*log(k/delta)), plus polynomial-precision phase/modular-power costs. This does not compute all2^t cells at once or provide a full Shor sampler.

## Deterministic parent-mass floor without an order input

For proof only let r=ord_N(a). The output is the equal mixture of r phase-estimation laws, P(k)=sum_{j<r}|sum_{x<Q}exp(2*pi*i*x*(j/r-k/Q))|^2/(r*Q^2). Each phase puts at least4/pi^2>1/4 on its nearest integer Fourier bin. A length-R interval receives at least floor(rR/Q) nearest phase-grid points, with a consistent half-open tie rule. Thus Pr(I)>=floor(rR/Q)/(4r)>=(R/Q-1/r)/4.

If an actual no-return certificate establishes r>=R0, then Pr(I)>=max(0,(R/Q-1/R0)/4). The production helper computes inherited collision_mass(N,a,W); K_W=W certifies R0=W. Otherwise it retains only R0=1, not an invented order. The certificate's work is charged. An interval containing zero also has Pr(I)>=P(0)>=1/(N-1). A tiny positive bound does not imply cheap conditional estimation.

Example N71,a2,W32:6 baby+5 giant multiplications, one inverse, K32=32. Every three-leading-bit prefix then has mass>=3/128, without knowing the actual order.

## Guarded conditional generation

For child masses x in[l0,u0], y in[l1,u1], refine lower bounds with a verified parent floor lambda. If no positive denominator is established, return PARENT_MASS_UNRESOLVED. Otherwise x/(x+y) lies between l0/(l0+u1) and u0/(u0+l1), with endpoints0/1 for zero child lower bounds. Inconsistency against the deterministic floor is reported. Child correlation is not erased or replaced by independent bit samples.

Conditional accuracy eta generally requires child additive error O(eta*lambda), giving a sufficient probe bound O(A^2/(eta^2*lambda^2)*log(1/delta)) for this estimator. This is not a general lower bound. Additive boxes alone cannot determine the conditional: (p,0) and(0,p) fit the same[0,p]^2 and same parent totalp but have opposite conditionals.

Reuse stage6.Dyadic unchanged for outward integer phase enclosures. Fractions are exact; the new candidate has no float/complex literal or true-division operator. Each rounded probe has error<=2^(-bits). Statistical radii combine Hoeffding and the inherited Maurer-Pontil empirical Bernstein inequality; IID and fixed sample counts are assumptions, not guaranteed by a fixed PRNG seed.

The bounded sequential prototype reserves delta/(maximum_depth*declared_looks) per possible attempt, uses fresh draws at each history and predeclared fixed budgets, and stops with a saved partial prefix when precision fails. Finite conditional union bounds cover the adaptive history. It NEVER discards failed paths and retries until success. Completed-only outputs are not certified: even a fair first bit followed by abort on all bit1 paths leaves only bit0 among completions. A complete-law TV theorem additionally needs an abort-probability bound or an always-resolving implementation. The code reports these missing guarantees explicitly.

## Executed evidence and limits

All new finite checks passed:45 proposal normalizations,8149 envelope checks,160 high-precision phase endpoints through128-bit registers,20 exhaustive expectations,7060 nearest-grid counts,7060 interval floors,870 factor-blind negative certificates,19998 rational ratio boxes,18/18 observed seeded coverage trials,9 invalid/resource checks, integer-only AST and a postselection counterexample. The initial100-digit reference was insufficient at64/128bits; recalculation at200+4m digits verified the original candidate intervals. Final timings were rerun after replacing exact Fraction division syntax with explicit constructors; preliminary runs are preserved separately.

Frozen definitive plan:53 runs=36 main+2 higher-budget diagnostics+12 representation comparisons+3 sequential paths. At65536 probes and conditional-radius target0.05, main results were3 target met,27 precision exhausted,6 parent mass unresolved. All78 available reference mass comparisons and64 conditional comparisons covered reference values; full128-bit laws were NOT computed. Same author, no independent review or full-project/Lean checks.

At262144 probes, N23,a2,m10,prefix00 has true next-zero probability0.6662514349303774 and estimate0.6682223119735466 with interval[0.6441215064586865,0.6923231174884069], elapsed371974062ns. N509,a16,m21,prefix000 reaches interval[0.45489476603415085,0.553610725856599] around true0.5000000350366489 in2845741503ns; it is a structured prime-input diagnostic.

For two requested four-leading-bit cell masses, N23: interval envelope8 versus prior per-bit495, median143290673ns versus806809681ns, radii0.0165083 versus0.710908. N509: envelopes19 versus10972.5, median781937975ns versus1137808712ns, radii0.0206925 versus11.9671(no useful old accuracy). The predecessor also computes all16 cells, so this is an application-level comparison, not equal-work benchmarking or a best-classical claim.

With separately declared conditional target0.1, three sequential paths reached6,4,3 of6 requested bits on N23,N71,N509; only N23 completed(prefix101110). No completed-only distribution guarantee is claimed. Rare-positive N23,a2,m10,prefix00000001 has parent mass about3.4782440390e-6; all main attempts refuse to normalize. The N15,a2,m10,prefix0001 zero-mass witness also refuses.

## Reuse, prior art and continuation

T0_BRC cyclic counts/provenance REUSE_APPLIED; inherited character oracle and directed intervals REUSE_EXECUTED; P023 observer-specific quotient/repair COMPOSE_APPLIED. Both child masses, interval location and parent evidence are retained for the split/normalize future operation. Signed Fourier payloads are not positive BRC branch weights. This is an application extension, not a new admitted global family.

Primary references: Van den Nest arXiv0911.1624, Maurer-Pontil arXiv0907.3740, Shor quant-ph/9508027. Fourier interval formulas, nearest-phase estimates and confidence/ratio tools are not claimed globally novel. A bounded current repository search is not a novelty proof.

Next unresolved unit: a direct conditional/relative-error arithmetic observer or costed structural jump avoiding inverse-parent-mass amplification. The present result removes one representation penalty but does not establish complete classical Shor simulation or improved general order finding.

Full proof, code, final raw runs and inherited histories are delivered in the separately verified Google Drive Git bundle. It is a standalone reproducer, not the whole Enterprise Math repository. Previously blocked GitHub code payloads are not retried; this file is text evidence. Upload hashes and observed readback are recorded in PUBLICATION_EVIDENCE.json after delivery.
