# Adaptive precision and modular summation: usable bridges

Status: SHARED_CONTEXT / SYMBOLIC_SYNTHESIS / NOT_ADMITTED. This unit contains source reading, one unsuccessful professional query, and symbolic derivations. It reports no new scientific BRC execution. Existing frozen source and raw scientific evidence were not changed.

## 1. Current source alignment

The complete RP1 heartbeat was fetched at EM commit `3d2e729c4cce0f8df228795599266e4582be3505`, path `research_notes/HEARTBEAT_RP1_LOW_PRECISION_RIDGE_20260927.md`, blob `ce983db7cf6610c9400450f649ce189c6b2398ec`. `RP1_READBACK.json` preserves that response. It changes the actual full 61-mode native word bank while retaining target brackets, output width and exact evolving state. It is not evolving-state rounding. Its bounded low-bit results support testing cheaper actual banks; they do not certify a uniformly adequate fixed precision. In particular, its adverse low-bit example has visible peaks but worse verified-factor probability than the stated uniform-readout baseline. Repeated timings with the same seeds do not create additional independent success observations.

The heartbeat's bundle identifier `cced867b76d106c34e5a610688f470c0b68d184e` did not resolve as an EM Git commit during a direct proof-file fetch. The actual 404 is retained in `RP1_BUNDLE_COMMIT_REMOTE_UNAVAILABLE.json`. This review therefore does not claim to have read or reproduced that bundle's full code, raw data or proof; it relies on the complete heartbeat and its stated scope.

The earlier `MASS_WEIGHTED_APPROXIMATION_BOUND.md` was fetched at EM `951cc16cb09635fae9f93230d96030fdaa2035b3`, path `research_notes/directed_recovery/20260927_C6438C/qft_row_queries/point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md`, blob `32b746b30b9a0602715e44c662cae5c5a15044a0`. Its current constant is one: consistent complete row approximations with the same feedback operator obey terminal joint TV at most `sum_i sqrt(sum_h E_h)`. It is not a theorem that inexpensive approximations or error certificates exist.

Changing a native bank also changes the current feedback. Thus applying that same-operator row theorem directly to RP1 would omit an error term. The new sibling `precision_theory/ADAPTIVE_NATIVE_PRECISION_INTERFACE.md` is the appropriate current interface: it compares two actual instruments on the same low-policy prefix covariance. Its complete symbolic text was read. Its covariance certificate, word-ledger and source-binding requirements are retained; this literature unit does not implement them.

## 2. Two distinct certificates should remain distinct

**Distribution fidelity.** Let the actual low-prefix covariance be C, M=tr(C)>0, and A=tr((T-S)C(T-S)^T), where T and S are complete orthogonal feedback operators and the work permutation is common. The sibling proof uses the local coherent overlap `1-A/(4M)` and charge `sqrt(A/(2M)-A^2/(16M^2))`. Low-prefix/reference-suffix hybrids justify averaging charges under the actual low-policy history law. This avoids propagating the high-prefix state, but obtaining C or a sufficient action certificate remains a charged task. A uniform exact mass/Gram oracle cannot be treated as free.

**Useful output.** Independently certified proper-factor indicators estimate the actual selected algorithm's success, without knowing an order or a useful-peak mask. Such estimates do not establish TV fidelity. Conversely, a small TV certificate supplies a useful-success bound only together with a valid reference success bound. RP1's visible-peak failure makes this distinction operationally necessary.

For completeness, an alternate row comparison can include changed current gates explicitly. Let E=sum_w ||v_w-u_w||^2, M=sum_w ||v_w||^2, and delta>=||T-S||, with T,S orthogonal. The two local arm errors have squared sum at most

    E + (sqrt(E) + delta sqrt(M))^2.

This follows by writing Tv-Su=S(v-u)+(T-S)v and applying Minkowski. The exact-reference proposal and the existing normalized-score lemma then bound the prefix's weighted local TV by

    min(M, sqrt((M/2)[E+(sqrt(E)+delta sqrt(M))^2]))
      <= min(M, sqrt(ME)+delta M/sqrt(2)).

The latter inequality is the triangle inequality in two dimensions. Sum these charges over depths and exact-reference history masses. The same complete u(h,w) must serve every private latent label and query; the work permutations and history meanings must agree. This is an optional comparison, not a replacement for the more direct low-covariance theorem or evidence of a cheap row oracle.

## 3. A concrete anytime selection lemma for a finite bank menu

The primary confidence-sequence paper by Howard, Ramdas, McAuliffe and Sekhon was read at Section 4.1, Theorem 4. It permits bounded adapted observations and predictable predictions; its target is the average conditional mean. Its time-uniform coverage is useful under optional stopping. It does not turn changing policies into samples from one fixed policy, and naively substituting empirical variance into an unrelated normal boundary is not covered. [Primary paper, Theorem 4](https://arxiv.org/pdf/1810.08240).

Here is a simpler self-contained sufficient lemma, offered as a specification rather than an implemented statistical observer. Fix J admitted banks or complete frozen policies before validation. For bank b expose a fresh independent trial stream `(Y_b,n,C_b,n)`, with verified-factor indicator `Y in {0,1}` and charged cost `0<=C<=Cmax`. Every abort is a recorded failed trial with its cost; there is no conditioning on completion. The stream for each bank has a fixed trial law. Adaptive scheduling may choose which bank to sample next from past information only.

For alpha in (0,1), define

    r_n = sqrt(log(4 J n(n+1)/alpha)/(2n)).

With probability at least 1-alpha, simultaneously for every bank and all n>=1,

    |mean(Y_b,1:n)-p_b| <= r_n,
    |mean(C_b,1:n)/Cmax-c_b/Cmax| <= r_n.                 (A)

Proof. For a variable X in [0,1], the convexity/chord bound on its exponential and the Bernoulli tilted variance bound <=1/4 give `E exp(lambda(X-EX)) <= exp(lambda^2/8)`. Independence, the exponential Markov inequality and optimization give two-sided sample-mean tail at most `2 exp(-2 n r^2)`. At r=r_n this is alpha/[2J n(n+1)]. Sum over two observables, J streams and all n, using sum 1/[n(n+1)]=1. Streamwise simultaneous coverage makes adaptive scheduling and stopping harmless. No independence between Y and C within a trial is needed.

Consequently, put `L_b=max(0,meanY-r_n)` and `U_b=Cmax min(1,meanC/Cmax+r_n)`. If L_b>0, the true expected future cost per verified success satisfies

    c_b/p_b <= U_b/L_b.                                  (B)

For fresh iid future trials the repeat-until-success expectation is c_b/p_b: condition on the first trial and use the independence of all future trials from its outcome. Thus a selected policy can carry an explicit cost/success certificate, in addition to all training and setup costs. The selected bank's actual trial definition, input/base distribution, decoder, random source and cost cap are part of the certificate.

Warm caches, altered policies, shared seeds and repeated timing runs require care. They do not meet the fixed independent stream premise merely by being called repetitions. One can freeze a reset/warm-state protocol, or use a valid adapted-process bound with its actual changing estimand. Unbounded wall time is not bounded cost; capped typed-operation counts with charged aborts are one possible observable. The logarithm/square-root expression above has not been executed through BRC; a future observer must certify conservative thresholds or use the sibling's rational, fixed-sample alternative. Formula (A) alone is not a license for unbounded retraining on validation data.

The most useful immediate experiment specification is therefore: compare an admitted finite menu using fresh verified-factor trials, count cold admission and certification separately, and freeze the chosen policy before an independent deployment draw. This evaluates useful success. To claim distribution fidelity, also obtain the instrument action certificate from Section 2.

## 4. What regular-sequence summation does and does not supply

Heuberger and Krenn's Section 3.1 defines a finite digital linear representation. Their Lemma 12.2, including its proof, was read: interval summation admits a digit recurrence once the representation is supplied. The zero-word convention contributes a correction when f(0)=I but A0 differs from I. Their asymptotic theorem uses a joint spectral radius bound and eigenvalues of the sum of digit matrices; a leading-term approximation needs its hypotheses and finite error constants before it can certify this task's error. [Primary paper, Sections 3 and 12.2](https://arxiv.org/pdf/1810.13178v5).

The relevant cost barrier can be made explicit without any spectral approximation. Suppose a length-i binary address has a *given* layer-dependent weight

    F(n)=A_(i-1,n_(i-1)) ... A_(0,n_0) v,

where bits are consumed in chronological high-to-low order. The unfiltered sum is an ordered product of digit sums and is easy. For the arithmetic progression n=r mod R, maintain a vector X_j(c) for every current residue c and update

    X_(j+1)((2c+d) mod R) += A_(j,d) X_j(c),  d=0,1.

With X_0(0)=v this computes the exact progression-restricted sum and preserves noncommutative order. For an explicit K-dimensional representation it uses O(i R K^2) generic scalar work and O(R K) state, before arithmetic bit costs. Kronecker or two-carry matrix observables change K, not the residue count. A clock coordinate can encode finitely many different layers into a single larger representation, but that construction does not remove R. Likewise, a finite native gate alphabet alone does not prove a small quotient for arbitrary feedback histories.

This is a constructive upper bound, not a lower bound on all algorithms. A special arithmetic identity, provable quotient or low-degree counting formula can do better. The sibling `nonzero_structure/ACTIVE_WINDOW_FLOOR_MOMENTS.md` supplies just such a sufficient condition: only ell chronological operators are nonidentity, with exact full-carrier identity intervals before and after. Grouping the free-address coordinates leaves triangular modular counts. Its simultaneous ten floor moments of total degree <=3 have an explicit Euclidean recurrence with O(log(R+1)) arithmetic layers. Full signed coefficients then cost O(2^ell ell) carry layers plus O(2^ell log(R+1)) scalar stages, with native action and bit costs still charged.

Our source-specific review of that candidate is in `ACTIVE_WINDOW_REVIEW.md`. No scientific floor-moment implementation was executed here. The benefit is conditional on a short *actual* nonidentity window and already acquired period/target information. Long zero bits after a nonzero bit are insufficient for an untruncated bank; the full feedback can remain nonidentity. Known finite-tail banks can satisfy the premise, but their separate precision/TV limitations persist.

## 5. Deduplication, query accounting and next mathematical target

The previous KQB2497 Shor/decision-diagram metadata remains PARTIAL/CONFLICT and was actually reread from GK archive `ed11167f4102d004e010643d74c00f0c658556a0`. It was not promoted to NO_HIT or repeated. Prior MPS odd-part, weighted-automaton and Pohlig-Hellman findings are reused with their existing scope; odd-part dependence is not presented as new.

One genuinely new query targeted digital regular sequences and summation. Issue [2499](https://github.com/awdawmip/kimi-query-bridge/issues/2499), batch `ac21bbbe-25b6-4e3b-a486-0616d792db7b`, returned `FAILED` with child `PROVIDER_ERROR`, zero records, incomplete coverage and retrieval_verified=false. One provider call was confirmed; fee and provider request ID were not supplied. The complete matching issue/intake/result readbacks are retained. This is neither a successful cache nor evidence that relevant literature is absent. No resubmission was made.

The next precise mathematical target is a certified reduction of typical reached histories to a small representation or small action-defect observable, with its construction and error costs included. Confidence sequences can certify measured performance, and active-window counting can compress a proved special structure; neither solves generic large-period discovery or guarantees that this structure occurs on enough probability mass. A native prototype should first implement the bounded floor-moment identity and complete per-step word ledger, then measure total certificate cost against the operations it saves.

Global-Knowledge-Sync: main@06788df / GLOBAL_KNOWLEDGE_V1
