# PREFIX-643 — Exact factored BRC phase vectors (author-side)

**Date:** 2026-11-10, Asia/Shanghai. **Status:** Algebraic proof and executable exact tests; independent review pending. **Researcher-ID:** EM-X6-36D045. **Research-Activity-ID:** RA-C15073313ABF1FFEB92402BB. **Task:** RS-X6-NATIVE-ROTATION-DYNAMICS; publication TP2-6A1F9D8C2047E3B51C01. **Formal CLAIM:** none.

## Inputs and precise claim

The original task freezes scientific inputs at source commit a72226e2430ffa4786321ac86e7f0c599d5f0389. The present observer implementation inherits the author-side native BRC-action pin f42f2906d77f24085c123f3ccfe9667d41caa96d. It uses 48 STAR phases, 96 original ports, 576 numbered and weighted BRC actions, and the seven-state Aho–Corasick observer of action motifs (485,316,52,174) and (52,174). Each state pair carries the exact six-moment integer jet (Z,U0,U1,V00,V01,V11), as in PREFIX-638/640.

Question: Given period p and L-step history window, recover exact six-moment readouts for p start phases without materializing p complete 672-state-by-672-state phase-result matrices.

Let J denote the associative commutative six-jet algebra defined in PREFIX-640. The chronological one-step BRC integer-jet matrices are N_i (N_(i+p)=N_i), with common rational-gate denominators tracked separately. Define Q=N_0 ... N_(p-1), source row vectors v_r supported at true original 96 ports with AC start state 0, and a terminal all-one column e. Put L=qp+s, q≥1, 0≤s<p.

**Theorem:** The exact six-jet readouts are

    r = 0:  v_0 · Q^q · (N_0 ... N_(s-1)) · e.

    1 ≤ r < p:
       j=(r+s) mod p; δ=1 if r+s≥p, otherwise 0.
       v_r · (N_r ... N_(p-1)) · Q^(q-1+δ)
                      · (N_0 ... N_(j-1)) · e.

Empty products are identities. Compute Q^(q-1), Q^q once for all phases. Evaluate each occurrence from left to right as a **row-vector update**; the short boundary products may be applied as original native one-step row updates, requiring no stored phase, prefix or suffix result matrices. For L<p, evaluate the L native steps directly.

**Proof:** This is the chronological factorization proved for matrices in PREFIX-642. The complete AC state is carried through every adjacent native step, including boundary-spanning motif hits. Associativity of jet-matrix multiplication gives (vAB)e=((vA)B)e. Scalar clearing for a gate a/b replaces every one-step gated weight by a and each ungated w by bw with one denominator b; this is a genuine common scaling of the original native step. Jet multiplication is bilinear, so the denominator after a chronological product is the product of these b, including if a=0. Initial rational masses use one common denominator. Final normalization returns exactly the original six rational moments. QED.

**Cost:** With original per-step native sparse operators and a fixed 672-state carrier, the streaming implementation forms Q with O(p) matrix products, the two shared powers with O(log(1+L/p)) products, and executes at most O(p²) one-step sparse **vector** updates and O(p) powered-block sparse vector updates for all p phase readouts. Storage contains the p original one-step operators, Q and two shared powers; it does not contain the p complete phase matrices or all prefix/suffix matrices. Bit complexity depends on exact integer size and is measured separately.

**Observer scope:** This representation computes the stated six moments. Ordered individual action/path identities remain the distinct observer interface of PREFIX-633's provenance-preserving path DAG. This note therefore makes no unrestricted path-quotient or physical rotation claim.

## Executed verification

Script: PREFIX643_phase_factored_vector.py (archived alongside this note in the attached code-and-evidence bundle, with original PREFIX-638/640/642 dependencies available from the earlier source). Executed on Python 3 with exact integer and Fraction arithmetic; exit code 0.

Gate classes: p1=all-one; p2=positive rational; p3=rational with zero; p4=rational with zero; p2=all-zero. All classes were checked at L=1,2,3,4,7,8,16,32,64; p1/p3/p4 additionally at L=256,1024.

Full exact 6-jet phase-matrix equalities: **108**. Independent literal-original-action dynamic-programming six-moment comparisons: **72**. Independent 96-port zeroth-moment propagation comparisons for long windows: **24**. Streaming-vs-factorized six-jet equalities: **124**, including 16 further long readouts for which streaming was also compared with complete exact phase matrices. All assertions passed.

Single-process timing, measured for all p phase readouts including shared-power preparation but excluding construction of initial native start vectors and the PeriodCompiler constructor; values below are a single run and not a confidence interval:

| Gate class | p | L | Streaming | Full phase compiler | Full / streaming |
|:---|---:|---:|---:|---:|---:|
| rational with zero | 4 | 16 | 0.0325 s | 0.1481 s | 4.55x |
| rational with zero | 4 | 64 | 0.0827 s | 0.1502 s | 1.82x |
| rational with zero | 4 | 256 | 0.1453 s | 0.2162 s | 1.49x |
| rational with zero | 4 | 1024 | 0.3045 s | 0.4151 s | 1.36x |

Note: these are exact-operator in-memory query timings, with initial-source recovery, period certification of uncompressed inputs and exact bit-cost accounting outside the timed region. For p=1, the full compiler may be faster.

## Reproduction and next scientific unit

The companion code-and-results archive contains exact Python source, all observed JSON, run.log and SHA256 checks. The full handoff tarball also contains unchanged original dependencies. Run the script in a folder containing PREFIX640_fraction_free_rolling_jet.py, PREFIX642_single_base_periodic.py and PREFIX638/PREFIX638_native_jet_support.py; expected stdout begins:

    ALL_ASSERTIONS_PASS 108 72 24 124

Further experiment: for few source phases, compute a right-side terminal functional under powers of Q rather than explicitly caching the powered full Q matrix. Compare matrix versus functional binary lifting using exact sparse product counts, bit sizes and memory; separately retain path-DAG observer for provenance demands.

Parent scientific objective remains open: arbitrary-oriented triadic signed C6, generated six-axis group, and operation-safe original Cell/path lifting. This is a reusable exact BRC-observer computation, not native physical-rotation closure.
