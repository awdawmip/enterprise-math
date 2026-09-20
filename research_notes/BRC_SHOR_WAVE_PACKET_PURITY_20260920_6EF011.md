# BRC-Shor: wave-packet full-output readout and purity-rank certificates

Event-ID: brc-shor-wave-packet-purity-20260920-6EF011
Researcher-ID: EM-DIRECT-6EF011
Research-Activity-ID: RA-6EF011C2E75C4A799606AFEA
Status: RESEARCH_CANDIDATE; same-author derivations and executable checks, no independent review, Lean, Working Truth or Foundation admission.
Source read: enterprise-math@a91c12e6c2f446a1bd4defc92f70c690cc96848e. Inherited standalone head c0bc60cff6dcbf3746e7a4d5609dc021c138737d.

## Result and crucial cost boundary

The wave-first direction now has an approximate COMPLETE FIRST-REGISTER OUTPUT sampler with deterministic total-variation control, not only marginals or completed prefixes. However its public N,a,m entrypoint FIRST invokes the inherited exact classical conditioned-order backend, with all prime selection, modular powering, residual search and order restoration charged. It then samples wave packets. It is not a faster order-finder or a general classical Shor speedup. The cases whose orders exceed the budget still have no output samples.

For r=ord_N(a), spectral decomposition of U|y>=|ay mod N> and the orthonormal eigenmode expansion of |1> give

    P(k)=(1/r) sum_(j<r) F_(Q,j/r)(k),
    F_(Q,theta)(k)=|Q^(-1) sum_(x<Q) exp(2*pi*i*x*(theta-k/Q))|^2.

A sample needs one uniform j and its packet, not a list of all r modes or Q states. This is standard phase estimation, not a novel general identity. It is valid for uniform exponent input, unit a, ideal QFT, numeric output labels and UNCONDITIONED second register. It does not preserve arbitrary future joint-register operations. Incorrectly substituting a returning multiple R for minimal r is fatal: N15,a2,Q256,r4 versus R8 gives TV=1/2 despite a^R=1.

## Wave residual bound and total readout

Round j/r to its nearest dyadic phase u/S, S=2^p. Unitarity and the whole normalized-wave norm bound give measurement TV<=4Q/S. Around the nearest Fourier bin, retain offsets -J..J on the circle. The squared Dirichlet-kernel bound gives omitted mass<=1/(2J-1); the nearest bin has mass>=4/pi^2>1/4. Thus every packet has a universal retained-mass floor, unlike rare prefixes of the final mixed law.

Use inherited stage6 Dyadic unchanged. For a non-grid phase, F(k)=|1-z^Q|^2/(Q^2|1-z|^2). All bins share the numerator, and denominator phases advance by one unit-root multiplication. Outward integer intervals at grid2^b enclose every probability; midpoint integer weights differ by at most2^(-b). Normalizing K retained weights contributes TV<=4K/2^b. Hence

    TV(P,P_tilde)<=4Q/2^p+1/(2J-1)+4K/2^b,

with zero tail for complete small supports. J=ceil(2/epsilon)+1, p=m+ceil(log2(16/epsilon)), b>=ceil(log2(16K/epsilon)) make this smaller than epsilon. At epsilon1/64, J129,K259,p=m+10,b19 give actual uniform bound329219/33685504 (about0.0097733138).

A conservative working precision W=2b+20p+6K+2ceil(log2(p+1))+128 is resource-checked BEFORE any random phase is selected. The proof bounds half-angle root errors by4(p+1)2^(-W/2), each complex multiplication error by8 times its predecessor, computation depth by2p+K, and nonzero squared-chord denominators below by16/2^(2p). Every supported plan consequently has positive denominator enclosures and final endpoint width<=2 for every phase. No phase-dependent precision rejection or selective retry is part of the mathematical sampler. Unexpected implementation failures invalidate a whole batch. Default integer randomness is SystemRandom; seeded PRNGs are reproducibility, not an IID proof. The error bound concerns the one-draw probability law, not a finite histogram; s independent draws have product-law error at most s times the one-draw bound.

Readout uses O(p+K) root/interval operations at the explicitly charged O(b+p+K) bit precision, polynomial in m,log r,1/epsilon after order recovery. This resolves the rare-prefix normalization bottleneck at known spectral grid, not how to discover that grid cheaply. The full proof is in stage10/PROOF.md of the delivered reproducer.

## Reusing collision mass as a wave-compression diagnostic

Group the pre-QFT pure state by modular output with fibre sizes n_y. Its Schmidt probabilities across exponent/output registers are n_y/Q, so

    Tr(rho^2)=K_Q/Q^2,
    inverse purity=Q^2/K_Q.

The original inverse-collision quantity is exactly an effective Schmidt-mode count. Writing Q=q*r+w, the best squared overlap of any normalized Schmidt-rank-D pure approximation is

    [D' q+min(D',w)]/Q, D'=min(D,r,Q).

This is a restriction on one whole-state approximation interface, not a general sampling lower bound or a bound for every tensor ordering/implicit representation.

Without an order input, a genuine K_W=W certificate proves r>=W and therefore F_D<=min(1,D*ceil(Q/W)/Q). On N18446743979220271189,a2,Q2^128,W2^16,D1024, the unchanged collision engine uses256 residue keys,511 modular multiplications and one inverse to certify F_D<=1/64. It does not compute the full-Q collision coefficient or solve the full order. This explains why small-mode pure-state truncation can fail while final-output spectral mixture sampling is compact after its parameters are known.

## Executed evidence

Checks passed:966 spectral-mixture/direct modular-fibre comparisons;6762 exact Schmidt-mass checks;534 order-blind purity/rank certificates;336 tail checks;240 exhaustive bounded dyadic-phase precision checks;183 component packets and5 complete approximate-output-law comparisons;75 high-precision probability enclosures through128-bit registers;12 large-r readout-only cases;20000 integer sample support checks;6 factor-blind end-to-end inputs; explicit order/resource/invalid-input and wrong-period-multiple witnesses. Candidate AST contains no float/complex literal or true division and imports no reference factorizer. Same author, not independent review or full-project/Lean validation.

Complete-law TV measured by independent direct modular-fibre Fourier arrays (verification only): N15,a2,m8:0; N21,a2,m8,epsilon1/16:0.00377055; N23,a2,m10,epsilon1/64:0.001024514; N71,a2,m10,epsilon1/16:0.00352253; N509,a16,m12,epsilon1/8:0.00803714. Each is below its reported bound. A20000-draw seeded histogram for N23 has TV0.0262967 to truth; this is sampling fluctuation, not a contradiction of the smaller probability-law bound.

The plan was frozen before timing:8 inputs*3 repetitions*4 requested samples, plus3 one-sample521-bit structured stress runs.27 completed records:21 successful batches,75 full output samples,6 explicit order-budget failures. GC before repeats, no CPU pinning, serial runs; reference minimality checks only after candidates. One tool timeout preserved26 completed records; only the missing unfinished repetition was restarted.

Median costs, milliseconds, order preprocessing / one full sample readout:
- N23,a2,m10:0.068921 /58.031703.
- N509,a16,m21:0.101269 /71.138132.
- N1000036000099,a5,m80:12.708653 /172.672037; exact r166672333344.
- N1002772198720536577,a3,m120:0.464283 /252.955353; structured NTT-prime product, r478159044608.
- N2^521-1,a2,m1042:3.154632 /7912.824828; evident small order521, NOT a hard factoring benchmark.

Non-grid packets retain259 output positions, not Q entries. The521-bit stress uses22782-bit conservative working precision. N1000000016000000063 and N18446743979220271189, both base2 with the fixed B31 and65536-key cap, fail at order recovery in all3 repeats; no quantum-style speedup or general64-bit success is asserted. Packet readout is deliberately conservative and no fastest-sampler claim is made.

## Reuse and next unit

REUSE_EXECUTED: inherited conditioned_order, collision_mass and directed Dyadic arithmetic unchanged. COMPOSE_APPLIED: P023 observer-scoped collapse, T0_BRC multiplicity/action semantics and finite-character spectral readout. Equal spectral mixture is permitted only for the stated traced-output observer; no identification of orthogonal physical labels or arbitrary positive-mass interference is used. This is an application extension, not a new admitted global family. P000 is unchanged.

Primary context: IBM Quantum Learning Phase-estimation and factoring; Shor quant-ph/9508027; Wang-Hill-Hollenberg arXiv1501.07644; Dang-Hill-Hollenberg Quantum3,116(2019); Sutherland Order Computations in Generic Groups(2007). Spectral decomposition, QPE tails, Schmidt approximation and generic order methods are prior art. Bounded repository search is not a novelty proof.

Next unresolved unit: construct or sample a sufficient spectral measure WITHOUT first supplying/computing the exact period and without hiding comparable work in a compact operator contraction. Use the current full-output sampler as a positive baseline and the order-blind purity certificate to reject unsuitable low-rank whole-state proposals. Preserve the exact small-denominator and prior phase/provenance witnesses.

Full executable history and raw evidence are delivered in the user-requested Google Drive Git bundle. The bundle is a standalone reproducer, not the complete Enterprise Math repository. Previously blocked GitHub code payloads are not retried; this note is text evidence. Actual upload/hash/readback are recorded separately after delivery.
