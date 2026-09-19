# BRC-Shor: exponent scheduling with exact original-order restoration

Event-ID: brc-shor-schedule-primary-lift-20260919-6EF011
Researcher-ID: EM-DIRECT-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE; proved elementary derivations and same-author finite checks; no independent review, Lean, Working Truth or Foundation admission.
Read source: enterprise-math@a6ef14fdc1dec284f9ca40875ae3acfb85e1b4b7. Inherited source: research_notes/BRC_SHOR_PARTIAL_RETURN_BLOCK_20260919_6EF011.md at 508269b7249af374b24832a23e6b2c347a35ce9e.

## Main result: return to the complete-order objective

Let a be a unit modulo N, r=ord_N(a), and let M>=1 have a known factorization chosen without knowing factors of N or r. Compute b=a^M mod N and its EXACT order s. Then s=r/gcd(r,M), s divides r, and ord_N(a^s)=r/s=gcd(r,M), which divides M. Thus the missing part is a known-factorization order problem. No factorization of N or s is needed.

Write M=product L_i, L_i=ell_i^e_i, and x=a^s. For y_i=x^(M/L_i), the order is ell_i^alpha_i with alpha_i=v_ell_i(ord(x)). Repeated ell_i-th powering until first identity determines alpha_i exactly. Hence r=s*product ell_i^alpha_i. A balanced product tree obtains every y_i: a node of product U*V and residue z sends z^V to its U child and z^U to its V child. This proves both the representation and its executable evaluation procedure.

The general law does NOT require gcd(s,M)=1: N=17,a=2,M=2 has r=8,s=4 and ord(a^s)=2. Conversely s must be exact: supplying the false nonminimal s=16 gives a nonminimal output16 that still passes a^16=1. Production uses exact reduced-order search; final modular equality alone is not a minimality certificate.

## Factor-blind saturated schedule and cost

Fix B before learning factors/orders. For each prime ell<=B choose the largest ell^e<=N-1, entirely with integer operations, and multiply these powers to obtain M. Since r<N, M contains every selected primary part of r. Therefore s is exactly the B-rough part of r, while the recovery returns its B-smooth part.

The original collision backend is reused unchanged: double Q until K_Q(b)>Q, then s=(3Q-K_Q(b))/2. A conventional dyadic Shanks backend was also tested as a same-output baseline. All sieving, exponent construction, powering, reduced search, recovery and final checking are timed. With k selected primes and L=bit_length(M), the mask/product-tree/leaf recovery uses O(L log(k+1)+log N) binary modular-power work beyond the prime sieve/integer products. Residual search remains O(sqrt(s)) group operations. L<=k log2(N); bit costs and nonconstant memory must be charged. Mostly rough orders may receive no benefit.

## BRC/P023 reuse and failed quotient

The retained population is modular-power branches with residue-keyed count/first moment; the new observer is K_Q(b), followed by exact restoration of ord(a). T0_BRC coefficient and prior block/gcd interfaces are REUSE_EXECUTED through unchanged delivered engines. P023 fiber-constancy/repair is COMPOSE_APPLIED: the map a->a^M is not sufficient for original-order observation, but retaining original a,N, factored M and exact reduced-order provenance is sufficient by the recovery law. This extends the application, not a new BRC family or the affine 28-entry occupancy interface.

Explicit witness: at N=15,M=4, a=2 and a=4 both project to1, although original orders are4 and2. Throwing away a cannot be repaired from b alone. Bounded repository pminus1/Pollard searches had no hits; this does not prove novelty or absence of all reusable methods.

## A factor exit can be erased and then restored

Ordinary M=lcm(1,...,B) is Pollard p-1 type preprocessing. At N=91,a=18, original local orders are3 and4; M=12 makes b=1. Naive transformed partial-return search loses the original factor7 exit. Retain a and M: s=1; a^3=8 mod91 has order4 and a^4=53 has order3. Their gcds with1 removed give7 and13; original order is12.

The repaired factor wrapper uses the same recovery for projected identity or for an exact transformed SYNCHRONIZED_RETURN supplied by the prior block engine. It returns FACTOR, BUDGET_EXHAUSTED or RESTORED_ORDER_NO_FACTOR, never a primality claim. The previous square-free fixed-base obstruction for equal ORIGINAL local orders remains intact.

For N=pq with distinct odd primes and a uniform original unit, let u=(p-1)/gcd(p-1,M), v=(q-1)/gcd(q-1,M). Powering gives independent uniform image-subgroup elements. Counting phi(d) elements of order d gives projected synchrony probability sum_{d|gcd(u,v)}phi(d)^2/(u*v). It may equal1. For p=7,q=13 and M=1,2,6,12 the exact probabilities are5/36,5/18,1/2,1. This concerns the naive projected exit before restoration. The old untransformed <=1/4 synchrony bound cannot be reused after changing the sampling distribution.

## Executed checks and same-output measurements

All passed: 7805 direct BSGS unit cases;31220 saturated original-order recoveries;93498 primary leaf-order checks;7805 arbitrary-mask recoveries;270 exact probability cases with56568 unit evaluations;3928 naive scheduled-factor cases;15608 repaired-factor cases. The repair suite recovered9580 original orders and4070 factor exits lost by its tested naive schedule. These are bounded test counts, not general success probabilities. Three candidate/dependency AST audits found no float/complex literal, true division or SymPy import. Five invalid-input cases and one explicit resource failure passed. Same assistant authored and ran all checks; no independent review or full-repository/Lean validation.

Benchmark plan frozen before timing: seed2026091905;12 seeded balanced semiprimes around24/32/36/40bits,4 constructed safe-prime pairs,7 named/constructed cases. B values7,31,127; max_baby_steps524288. Raw backends above40bits NOT RUN by a predeclared rule. Candidate worker loads no reference factorizer; SymPy1.14.0 postchecks run afterward. Three repetitions, GC before each, rotated method order, no CPU pinning.396 completed runs:375 exact original-order successes,21 explicit budget exhaustions. One tool timeout interrupted an unfinished repetition; saved complete rows were preserved and the unfinished repetition was restarted, not counted.

Fixed B31 versus raw Shanks,20 paired successes:17 faster,3 slower; median paired raw/new ratio4.805124366969568. Fixed B31 versus raw collision:19 faster,1 slower; median ratio6.898336146877507. These are selected finite sample summaries, not statistically robust or best-classical comparisons.

N=1000036000099,a=5: original r166672333344, reduced s157833649, recovered part1056=2^5*3*11. Old/new collision median ns1040122514/29733513; old/new Shanks392128712/10773813. Collision peak residue keys524288->16384. Mask423bits;40 preprocessing/restoration/checking modular-power calls included.

Strong selected example N=56708047307,a=2: r28353785460,s16279; old/new Shanks170114749/368563ns. Counterexample N=6186937,a=2: r=s1545469; old/new Shanks859651/1000833ns, so the new work is overhead. Increasing B is not monotonically faster.

Constructed NTT-prime product N=1002772198720536577,a=3: r478159044608,s479; conditioned Shanks419380ns. Raw >40bit run was not performed, so no raw speedup ratio is asserted. N=1000000016000000063,a=2: B7/B31 exhausted, B127 recovered r62500000875000003 in392451252ns median. N=18446743979220271189,a=2 exhausted all tested bounds. No general64bit success claim.

## Prior art and continuation

Classical prior art: SageMath generic group documentation (order_from_multiple, order_from_bounds); Sutherland, Order Computations in Generic Groups; Bostan-Yurkevich arXiv:2012.08656; Zralek arXiv:0707.4102. Cyclic primary decomposition, known-factored-annihilator recovery, Pollard p-1 and BSGS are not claimed as new. No polynomial classical Shor simulation, general factoring record or new worst-case order bound is established.

Next unresolved unit: choose profitable prime/exponent branches from observable arithmetic evidence, without oracle knowledge of r, and certify that saved work exceeds selection/restoration cost; compare against smoothness-aware generic algorithms rather than only raw BSGS. Preserve rough-order failures and the unresolved unknown-five-position localization problem; do not repeat completed proofs/tests.

## Persistence limit

This text is the remotely publishable proof/experiment checkpoint. The previous block_engine.py upload block was NOT retried, encoded or rerouted. Full runnable code, frozen plan and raw runs remain in the local delivered reproducer bundle. Complete remote executable publication remains pending; this note does not establish that all code was committed.
