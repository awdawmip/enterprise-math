# Stage400-B — minimal two-source joint BRC witness and exact synchronized transfer

Date: 2026-11-03. Classification: **author-side mathematical proof plus executed exact computation; UNREVIEWED / NOT_ADMITTED**. Parent Stage399-B: `65aee6f53e8262bba9ace6067f130823a3441c36`, Research2 draft PR #1736. Inherited frozen scientific inputs: Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, global scientific input `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, original P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative context read separately at global main `720e1242d1e0598adbaffcc7c71a822693922a70` and EM main `28933bcf5fab061599dd19dad28d7e6e5d69c27c`.

## Exact objects

All word letters belong to the twelve signed primitive native X6 directions `A={±E_1,...,±E_6}`; their six-component integer displacements are chart-relative to a chosen Cell. For a finite ordered path w of length m, set `z(w)=Σ_i e(w_i)`, and `J_w(a,b)=#{i<m:(w_i,w_(i+1))=(a,b)}`. Preserve the source label (P or Q), endpoint z, length m, full directed J, all 20 relative triple readouts and common depth, per-direction multiplicative nonzero rational signed trace `Omega(w)`, the unweighted native BRC endpoint count `N_m(z)` and independently the positive rational weighted BRC endpoint mass `W_m^p(z)`. The weights depend only on the signed direction. In this specific model, the last three observables are determined by (m,z,J) and fixed source parameters: if t is the final letter, `n_a=out_J(a)+1_[a=t]`, and `z=Σ_a n_a e(a)`. These endpoint kernels are not individual-history masses.

Two source-tagged histories w and v have a **declared synchronized position index** (not a seventh spatial axis), with equal length m. Introduce the joint relational observer `K(w,v)=Σ_(i=1)^m 1_[w_i=v_i]`. For the inherited future memory theorem, condition on K at the current time, then allow *independent source-local* APPEND of arbitrary signed letters and at most C inverse-terminal-pair CANCELs per source, observing the individual source histories but not re-reading K after operations. This is the frozen-K regime; live re-evaluation of K under paired future operations is the next research question.

The parent Stage398 exact single-source signature is recursively `S_0(w)=last(w)` (EMPTY for empty w), and for c>=1 `S_c(w)=(S_(c-1)(w), S_(c-1)(pred(w)), S_(c-1)(pred^2(w)) if last two letters are inverse else ABSENT)`; correct EMPTY cases apply. Its dependence is limited to the last `min(m,2c+1)` letters; under the parent theorem it exactly classifies source-local future observation classes. In the frozen-K regime the pair of source signatures therefore exactly classifies the jointly observed future after conditioning the starting population.

## Theorem 400.1 — a shortest possible joint-observation counterexample

For every word with m<=3, the pair (z,J) uniquely determines the word over the **full twelve-direction alphabet**. The first possible ambiguity occurs at m=4. Let `A=+E_1`, `B=-E_1`, and put

`w=(A,A,B,A)`, `v=(A,B,A,A)`.

Both have m=4, z=2E_1 and exactly `J(A,A)=J(A,B)=J(B,A)=1`, all other entries zero. Conversely the endpoint fixes the signed-axis multiplicities (three A and one B, with all other letters absent, since the stated directed histogram has no others), and the histogram forces B to be interior: the entire marginal fiber is exactly {w,v}. They share turn count 2, all native coordinate observers and any per-direction multiplicative signed trace. With native positive BRC weights p_A=2, p_B=3, and p_d=1 on the other ten directions, the full native twelve-direction recurrence gives

`N_4(2E_1)=64`, `W_4^p(2E_1)=336`.

Indeed 3 A + 1 B gives 4 paths, and 2 A plus an inverse pair on each of the other five axes gives 5*(4!/2!)=60 paths. Their positive masses total 4*2^3*3 + 60*2^2=336. Independently choose signed factors lambda_A=2, lambda_B=-3, lambda_other=1; both path traces are Omega=-24. The S_1 signatures differ because w ends in inverse pair B,A (CANCEL enabled), while v ends in A,A (CANCEL disabled).

Give each separately tagged source the same fixed marginal fiber {w,v}. The unconstrained Cartesian population is {(w,w),(w,v),(v,w),(v,v)} and has **four** distinct source-signature pairs. Its synchronized joint observer has the exact matrix

```
             Q=w  Q=v
P=w            4    2
P=v            2    4
```

Conditioning on current K=4 leaves precisely {(w,w),(v,v)}. Conditioning on K=2 leaves precisely {(w,v),(v,w)}. Each conditional fiber has **two** distinct inherited source-signature pairs and therefore requires **one fixed binary bit** of extra future history information in the explicitly declared frozen-K future language, versus **two bits** for the unconditional four-pair product. The classes are distinct since a source-local inverse-pair CANCEL distinguishes w from v. This disproves the unqualified claim that independent source-signature distributions may be multiplied *after conditioning on a joint readout*.

To see shortest-length minimality, m=0 and m=1 are immediate, m=2 has its sole directed edge specifying the word. For m=3, J contains two consecutive directed edges. If multiple Euler traversals exist, they form a two-edge directed cycle A→B→A, whose possible words ABA and BAB have endpoints differing by e(A)-e(B)≠0 for distinct primitive signed directions. Otherwise the word is fixed. Thus a common (z,J) fiber has size one for m<=3, and the witness at m=4 is minimal.

## Theorem 400.2 — exact coupled-source transfer for any finite length

Fix an arbitrary m>=1, exact nonnegative 12×12 directed integer edge histograms J_P,J_Q with total edge count m-1, required six-component endpoints z_P,z_Q, and cancellation budget C>=0. Define

`D_C(r,sigma,tau)=#{(w,v): individual (z,J) agree with prescribed data, |w|=|v|=m, K(w,v)=r, S_C(w)=sigma, S_C(v)=tau}`.

There is an **exact finite integer dynamic program** computing D_C without enumerating every complete word pair.

A state at paired-prefix length i contains `(R_P,R_Q,a,b,u,v,r)`: remaining edge counts; terminal letters a,b; stored suffixes u,v of length at most k=min(m,2C+1); and matched-position count r. Initialize one state of multiplicity 1 for every initial letter pair (a,b), with full R=J, suffixes (a),(b), and r=1_[a=b]. From such a state choose (a',b') with R_P(a,a')>0 and R_Q(b,b')>0. Subtract one of each directed edge, append/truncate the respective suffix, increment r by 1_[a'=b'], and add the integer multiplicity to the resulting state. At depth m keep exactly zero-residual states satisfying

`z_P=Σ_a out_(J_P)(a)e(a)+e(a_last)`, and likewise for Q.

This endpoint identity holds because tails of the m-1 directed edges are exactly the first m-1 letters. The additional specified signed trace and endpoint BRC readings are checked from the source direction multiplicities, which are fixed by J and the last label. Bin each accepted state's exact integer count under (r,S_C(u),S_C(v)).

**Proof.** By induction on paired-prefix length, each paired transition sequence is in bijection with a pair of labeled source words having precisely the consumed directed edges and accumulated r. Every pair of full words has exactly one initial pair and one ordered sequence of transitions. Conversely zero-residual states reconstruct exactly J_P,J_Q, and the endpoint filter gives exactly the selected marginal fibers. The additive equality increments sum to K. The inherited S_C only reads k final letters, so terminal suffixes determine the exact signatures. Therefore each valid pair is counted exactly once and the DP output equals D_C. Empty paths are handled separately as a unique (EMPTY,EMPTY) state. QED.

Let `d_P(sigma)` and `d_Q(tau)` denote individual marginal signature counts. The exact unconditional factorization is

`Σ_r D_C(r,sigma,tau) = d_P(sigma) d_Q(tau)`.

In contrast a fixed-r conditional product need not factor. In particular **the full unconditioned Cartesian population is retained at one K=r0 iff K is constant r0 on the entire product**. This is a scope-specific factorization criterion, not an assertion of statistical independence of an arbitrary observed conditional distribution.

## Resource accounting, verified evidence and next unit

Each source carries 144 directed counters (288 jointly), a 12×12 pair of last letters, a coincidence count 0..m, and two suffixes of length up to k. A crude state upper bound is `O((m+1)*12^(2+2k)*Π_(a,b)(J_P(a,b)+1)*Π_(a,b)(J_Q(a,b)+1))` with at most 144 successors per state. Counting is pseudo-polynomial in integer edge counts and potentially exponential in C, **not polynomial in binary input length**. Constructing J from explicit histories costs O(m); the number of output bits for exact counts can be O(m).

Executed `REPRO_STAGE400B_COMPACT.py` with Python standard-library exact integers twice; it produced identical stdout. The full source verification also executed 903 direct-pair-vs-dynamic-transfer distribution comparisons: every fiber at m<=3, every non-singleton (z,J) fiber of length 4 and 5 for C=0,1,2, and 144 mixed nontrivial marginal-source fiber pairs at length 4. Enumerated alphabet was {±E1,±E2}; group counts by m=0..5 were 1,4,16,64,244,856 with 0,0,0,0,12,156 nonsingleton groups. Independently executed `CROSSCHECK_STAGE400B.js` using JavaScript BigInt for the native twelve-direction BRC recurrence and the K matrix. Certificate: `STAGE400B_COUPLED_TRANSFER_PASS` (903 checks), `STAGE400B_INDEPENDENT_JS_PASS`. The proof applies to the full twelve-direction finite-word domain and arbitrary finite m; exhaustive code coverage is only the stated finite subset. A fuller author-side proof and larger diagnostic code are also preserved as conversation artifacts.

**Next Stage401-B:** Introduce a *live* synchronized-K future observation under explicitly aligned paired APPEND and terminal inverse-pair CANCEL; test whether `(K,S_C(P),S_C(Q))` is sufficient for future K updates and whether its induced quotient is sharp. Compare with a joint-pair suffix or cross-histogram repair. Investigate sparse-J coupled Euler/generating-function transfer with honest input/preprocessing/output bit complexity. P000, source science pins and the original role/admission boundaries remain intact.