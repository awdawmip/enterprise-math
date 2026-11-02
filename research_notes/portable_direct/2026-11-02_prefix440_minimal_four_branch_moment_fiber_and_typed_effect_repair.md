# PREFIX-440 — Constant-four-branch X6 moment fiber and typed BRC effect repair

Date: 2026-11-02 (Asia/Shanghai). AUTHOR-SIDE ANALYTIC PROOF + EXECUTED EXACT INTEGER CERTIFICATE; UNREVIEWED / NOT_ADMITTED. Frozen scientific inputs: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Current API read snapshot: enterprise-math main@2257276362a3c515c128472b6c7c922d2bca3040. Current account rules read snapshot: chatgpt-global-knowledge main@e4645d03399b0f779ff16f12d393b8909c27b6ce. Frontier: PREFIX-439, blob 18eb11a384803e6c0de6b0334ddf0adac36f4a3e. Mathematical model is the chosen-chart, signed-step X6 path family; step count n is not a physical heartbeat period.

## Model

Choose one native X6 Cell as a chart reference, within the full six-axis torsor. A signed length-n word using only ±e1 has k negative steps, endpoint x_k=(n-2k)e1, with binomial(n,k) distinct ordered realizations. A positive integer path bag μ is recorded as endpoint counts. Write M_d(μ)=sum_k μ_k (n-2k)^d. The full six-coordinate homogeneous second-moment Gram matrix of this family is determined by M_0,M_1,M_2 because the remaining five coordinate components vanish. Current observers: exact endpoint counts, endpoint polynomial observers, signed step-history parity, and typed control Port labels.

## Theorem A: first moment-fiber threshold is n=3

For every fixed n, the map from nonnegative rational endpoint histograms supported on {n-2k: 0≤k≤n} to (M0,M1,M2) is injective if and only if n≤2.

Proof. For n≤2, the moment Vandermonde matrix has n+1 distinct columns and full column rank. For n=3, the rank-three matrix has exactly one kernel direction (1,-3,3,-1), since the third finite-difference stencil annihilates polynomials of degree ≤2. Its positive/negative parts are legal endpoint histograms: E3={3:1,-1:3}, O3={1:3,-3:1}. Each is realized by four distinct native words of length three. Both yield (M0,M1,M2)=(4,0,12), whereas M3(E3)=24 and M3(O3)=-24. For every n>3 use the four consecutive reachable positions n,n-2,n-4,n-6 with the same signed kernel. Nonnegative realizations follow from Theorem B. QED.

## Theorem B: four branches per ensemble suffice for every n≥3

For each integer n≥3, choose one distinct word with k=0 and three with k=2, giving E'_n={n:1,n-4:3}. Choose three distinct words with k=1 and one with k=3, giving O'_n={n-2:3,n-6:1}. These eight source paths exist because binomial(n,1)≥3, binomial(n,2)≥3, binomial(n,3)≥1. They all have precisely n signed native steps.

For d=0,1,2,
M_d(E'_n)=M_d(O'_n).
At d=3,
M3(E'_n)-M3(O'_n)=n^3+3(n-4)^3-3(n-2)^3-(n-6)^3=48.
This follows from the exact finite-difference identity (1,-3,3,-1) at step spacing two. It holds for every n, not only tested lengths. Thus the earlier PREFIX-438 full even/odd families, each of size 2^(n-1), have a constant-four-branch-per-ensemble obstruction witness for all n≥3. Each explicit word still takes O(n) symbols to specify; the BRC endpoint histogram has two atoms per ensemble.

## Theorem C: exact terminal observer condition at n=3

Let L_f(μ)=sum_{k=0}^3 μ_k f(3-2k), for any specified scalar endpoint observer f. For all nonnegative rational μ supported on {3,1,-1,-3}, this observer factors through (M0,M1,M2) iff
f(3)-3f(1)+3f(-1)-f(-3)=0.
Proof: the moment map kernel is exactly span(1,-3,3,-1), and factorization is equivalent to orthogonality to this kernel. Necessity holds on the nonnegative cone by E3 and O3. Sufficiency follows by row-space/kernel duality. QED.

The terminal parity observer f(x)=1 if (3-x)/2 is even and 0 otherwise gives 4 on E3 versus 0 on O3. Every terminal endpoint observer at n=3 is recoverable with one additional independent scalar, e.g. M3, since the four-row Vandermonde matrix is invertible. One such scalar is necessary and sufficient for the four-endpoint linear moment representation; this does not assert a universally sufficient four-number carrier for arbitrary future actions.

## Theorem D: what exact EffectHistogram coalescence preserves

For a legal signed X6 path of length n and total displacement x=(x1,...,x6), let a_j,b_j be its positive/negative step counts on axis j, and r_j=b_j mod 2. Since n=sum(a_j+b_j) and sum(x_j)=sum(a_j-b_j), N_-=(n-sum(x_j))/2=sum b_j is a nonnegative integer. Thus
r6 = ( (n-sum(x_j))/2 + r1+r2+r3+r4+r5 ) mod 2.

For a fixed-duration translation-only typed BRC packet, assume the source and target labels retain the changes in cumulative r1,...,r5, and each affine effect atom is an exact translation T_x. Then the r6 *increment* is determined by (source,target,packet duration,T_x). Therefore exact recoalescence of equal (positive weight,T_x) entries within one source-target block preserves that increment. The formula also applies to correctly typed serial compositions: exact translations add, duration adds, and all relevant parity increments add modulo two. This is a scoped sufficient interface theorem.

A shortest provenance witness: (+e1,-e1) and (+e2,-e2) share translation zero, duration two, unit weight and the declared phase but differ in r1. A ControlPacket encoding both in the *same* target and same effect obtains one coalesced atom of multiplicity two; assigning distinct targets retains the difference. The API does not infer path-history labels automatically.

After compressing to MomentState, even exact positive affine-effect data can be lost for nonlinear endpoint/path-history observations: Theorems A-C give an exact witness. For terminal polynomial observers of degree ≤2 under the declared affine future family, the degree-two moment projection remains exact.

## Source interface and executed verification

Read from GitHub connector at the named main snapshot: src/enterprise_math/brc_control_port.py blob 44def6b8ac787e798d3cc2c6be16f873f91b9db8 (ControlPacket.from_edges/then/alternatives/evaluate/moment_action); src/enterprise_math/brc_transport.py blob be1debe367263931bd5e93fd750be3ed54624fe1 (Affine, EffectHistogram, MomentState); src/enterprise_math/brc_histogram.py blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1. Also read p000_reality_foundation.json, Heartbeat X6 ACTIVE contract, observer preservation contract and residual-fidelity position, project portable method and continuation protocol, account math/temporal/code policies.

Executed independent exact standard-library program prefix440_exact_minimal_fiber.py: PASS. Verified n=0..2 Vandermonde rank, n=3 unique kernel, M0..2=(4,0,12), cubic gap 48, parity detector gap 4, four-branch construction for n=3..100 (98 cases), all 271453 signed native six-axis words of lengths 0..5 for r6 reconstruction, and a two-step same-target coalescence witness. All universal claims above have analytic proofs; finite checks cover only their enumerated ranges. Full raw execution evidence is in PREFIX440_EXACT_EXECUTION.log.

prefix440_native_brc_integration.py is an import-based test prepared for execution in an authorized checkout, checking the actual unmodified upstream ControlPacket/EffectHistogram/MomentState APIs and serial/parallel composition. It was syntax-compiled but NOT RUN against upstream in this run because the exact checkout/modules are absent in the local executor. The independent exact certificate is executed, but no upstream integration success is asserted. Source inspection confirms the API shape only. No native research Task CLAIM, Result, Review or Admission is claimed (gateway owner query CONTROL_QUOTA; Site research_authority_granted=false).

## Next executable scientific step

On a verified checkout: PYTHONPATH=src python research_notes/portable_direct/prefix440_native_brc_integration.py. If its assertions pass, extend to the PREFIX-439 2048-state effect-coupled model and S6 relabeling; if they fail, preserve the minimal failing input and correct the exact interface theorem. Compare a scoped cubic-moment extension with an explicit parity sector as alternative exact observer repairs, accounting for all transformation, memory and future-operation costs.
