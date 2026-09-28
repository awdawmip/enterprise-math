# Slow structure VI: exact precombination, boundary sampling and its costs

Progress-Event-ID: slow-precombined-sampling-20260928-6f6b1c93
Research-Activity-ID: RA-SLOWSTRUCT-6F6B1C93-D5DF97E7
Researcher-ID: EM-DIRECT-6F6B1C93
Session: local-chatgpt-slowstructure-6f6b1c93 (same local key; not an authenticated platform ID)
Status: AUTHOR_SYMBOLIC_DERIVATION / NOT_ADMITTED / NO_NEW_SCIENTIFIC_EXECUTION
Global-Knowledge-Sync: main@f2566e7 / GLOBAL_KNOWLEDGE_V1
Control-source observation: enterprise-math@6623604eea1350d50a3248ae25ff27c45227abd1

## 0. Frozen predecessor and scope

The user requests continuation of the existing slow-structure line. The exact predecessor is awdawmip/enterprise-math@a230a1fe856733b1a97a2e18b385ab400b9d60b2:research_notes/direct_followups/20260928_slow_collision_intervals_6f6b1c93.md. The earlier correlation, carry and threshold notes and the native two-arm interface at 951cc16cb09635fae9f93230d96030fdaa2035b3 retain their stated scope. The current own activity record still contains the five earlier checkpoints; its observed blob is 229bbed6423294d810dd8f479f35677f8a3c3588. No other actor's identity or CLAIM is used.

P000, residual fidelity and ACTUAL_TYPED_BRC_ONLY remain unchanged. Scientific content below is symbolic composition of the source-bound signed preparation and two-arm observer laws, not a new numerical run, physical waveform model, or replacement classical propagator. Complete labels, internal coordinates and ordered feedback are retained. Exact precombination preserves the full current native vector, not merely its present intensity. The conditional-expectation theorem is a sampling representation statement, not a claim that each random sample is the physical state. Reuse: COMPOSE_APPLIED / EXTEND_EXISTING_OBSERVER. Typed integration, measured runtime and independent mathematical admission remain pending.

## 1. Precombine before sampling: a variance theorem

At a fixed history h with L preparation addresses, use the predecessor's sparse full-carrier vector X_e, with its complete signed internal contribution at the actual label c^e. For E uniform on the addresses,

    E[X_E]=v_h,  ||X_E||=1.

Fix a partition pi of addresses, independently of the production sample and fresh readout threshold. An independent pilot may choose pi; all following claims are then conditional on that pilot. For a block b define its EXACT conditional mean

    Z_b = E[X_E | pi(E)=b].

Sample blocks with their original probabilities |b|/L, not uniformly over unequal blocks. Let Z_i=Z_{pi(E_i)} for independent E_i. Then E[Z_i]=v_h. For any fixed real symmetric observable H, define the diagonal-debiased quadratic statistic

    U_H(X) = sum_{i!=j} X_i^T H X_j / [n(n-1)],  n>=2.

Its mean is v_h^T H v_h. Conditional independence of E_i given their individual block labels implies

    E[U_H(X) | pi(E_1),...,pi(E_n)] = U_H(Z).

Consequently the total-variance identity proves

    Var(U_H(Z)) <= Var(U_H(X)).                         (1)

This holds for indefinite H as well as positive H. It applies to parent mass (H=I), child masses (H=A_sigma^T A_sigma), and, conditional on the independent threshold u, the direct decision functional with H=A_plus^T A_plus-u I. It is not a variance claim for a plug-in ratio of random mass estimates.

Diagonal subtraction after replacement is sum_i Z_i^T H Z_i, NOT the old constant n. Sparse aggregation remains possible only if the block means have an economical representation. Arbitrary exact conditional means may be as expensive as the original problem. The theorem compares equal sample counts, not equal computation budgets. Approximate block means require an additional bias/error contract; (1) must not be applied as though approximate sums were exact.

## 2. A concrete exact cancellation certificate

Consider the source-permitted fixed history h=00...01, m>=1, L=2^m. The predecessor establishes

    X_e=(-1)^e E(c^e),  0<=e<L,                       (2)

where E(w) denotes the full initial internal vector embedded at label w. This notation retains all internal coordinates; it does not introduce a new propagator.

Suppose an actually available integer R is odd and has a VERIFIED return

    c^R=1 mod N.                                     (3)

R need not be the minimal order. Because both the complete label and internal sign are now matched,

    X_(e+R)=-X_e,  X_(e+2R)=X_e.                    (4)

Thus each complete block of 2R addresses cancels exactly. Put ell=L mod (2R), and define

    if 0<=ell<=R: a=0,       B=ell;
    if R<ell<2R: a=ell-R,    B=2R-ell.

Directly splitting the residual block at R proves the full-vector identity

    sum_{e=0}^{L-1} X_e = sum_{j=a}^{a+B-1} X_j,     0<=B<=R.  (5)

For ell>R the first R terms minus the first ell-R terms leave precisely the displayed suffix. This proves the formula without enumerating any cycle. When R>L there is no useful shortening. B=0 proves that this particular history has zero mass, rather than authorizing an arbitrary continuation. In the present power-of-two family, odd R>1 gives B>0; R=1 gives zero for m>=1.

The cancellation requires (2) AND (3). A modular return alone does not cancel general noncommuting feedback histories. Opposite scalar signs at different labels cannot cancel. The claim is a finite symbolic identity for this source family, not an executed fixture or a physical bandwidth theorem.

## 3. Residual-interval sampling without rare-event rejection

For B>0, draw J uniformly from the consecutive interval [a,a+B). Evaluate X_J using its original address and the same source-bound operations. Define

    v_tilde = E[X_J],  lambda=B/L.

Equation (5) is exactly

    v_h=lambda v_tilde.                             (6)

Both child masses, and every subsequent unnormalized branch mass, acquire the SAME factor lambda^2. All conditional future readout probabilities therefore agree. Retain lambda as an exact scale and keep the original h and future schedule. Do not redefine the branch's unconditional mass or pretend the compressed vector is newly normalized physical energy.

Draw directly from the B-element interval: do not sample an old L-element address and reject until a residual term is found. Exact uniform integer generation uses fair bits with rejection below the next power of two, expected fewer than two attempts; its bit cost and the actual typed address operations remain charged. No Born-distributed label oracle is assumed.

Apply the previous diagonal-debiased child estimators to these unit-norm residual samples. The quasiuniform consecutive-power count argument holds for arbitrary integer B, not only powers of two. Hence its variance/confidence construction applies with address count B and with the residual mean v_tilde. The scale cancels in the probability enclosure. This is separate from theorem (1): direct residual resampling changes the proposal law, so its gain is quantified below rather than attributed to (1) without proof.

## 4. Quantified repair of the cancellation parameter

Write Q_x for the positive collision probability of x consecutive powers of c; the starting offset does not change it. Let M_L=||v_h||^2 and M_B=||v_tilde||^2. Define gamma_L=M_L/Q_L, gamma_B=M_B/Q_B, for positive mass. Equation (6) gives

    gamma_B/gamma_L = (L/B)^2 Q_L/Q_B.               (7)

A useful elementary fact is that x Q_x is nondecreasing in the positive integer x. For analysis only let s=ord_N(c), x=qs+k, 0<=k<s. If A_x is the sum of squared occupation counts, then

    A_x=q^2 s+(2q+1)k,   x Q_x=A_x/x,
    A_(x+1)=A_x+2q+1,
    (x+1)Q_(x+1)-xQ_x=q(q+1)s/[x(x+1)] >=0.

Therefore for B<=L,

    Q_B/Q_L <= L/B,
    gamma_B >= (L/B) gamma_L.                       (8)

This is an actual improvement of the signed-cancellation parameter whenever the certified boundary is shorter. It does not reduce the cost of discovering R.

The predecessor's sufficient fixed-history sample expression is proportional to

    1/(delta gamma^2 eta^2) + 1/(sqrt(delta) gamma eta sqrt(Q)).

For the residual representation, its two terms are at most (B/L)^2 and (B/L)^(3/2), respectively, times the corresponding original expressions, using (7)-(8). These compare sufficient bounds, not measured runtimes, minimal sample requirements or end-to-end speed ratios. Confidence-set construction, fixed constants, minimum n, per-sample word work and actual interval widths still matter.

An informative analysis-only subcase is R=s, with s odd. Then B<=s, all B residual labels are distinct, and

    Q_B=M_B=1/B,   gamma_B=1.                        (9)

Thus the small original mass M_L=B/L^2 no longer forces estimating a tiny relative residual: it is retained as a known scale. The resulting sufficient sample bound is O(1/(delta eta^2)+sqrt(B)/(sqrt(delta)eta)). This is still not polynomial in log N for unrestricted B. Moreover R=s is NOT supplied as an algorithm input or certified minimal for free. For nonminimal R, collisions may remain in the boundary and gamma_B need not equal one.

## 5. Obtaining and improving a return without assuming the answer

A pilot collision at distinct addresses e,f with c^e=c^f supplies D=|e-f| and a testable return c^D=1. Duplicate sample indices with identical address give D=0 and no useful return certificate. An odd D can serve as R. For even D, halving is allowed only after verifying c^(D/2)=1; repeat while the verification succeeds. If the true order is odd this reaches an odd return. When the order has an even factor the procedure can stop at an even return, and the cancellation rule (4) is unavailable.

Two verified positive returns R_1,R_2 imply that gcd(R_1,R_2) is a return by Bezout and invertibility of c. This needs no factorization of either integer. Every discovery, equality test, gcd, halving verification and source-bound modular operation is charged. A collision may yield a return of order L, so it need not produce a short boundary. No polynomial bound on discovery of a useful R is proved here; generic collision search can retain the predecessor's square-root order scale.

The return belongs to the current c and does not automatically establish the original base's full order. Once return information is available, compare with a direct classical use of the same information; do not give the proposed simulator the certificate while withholding it from the baseline.

## 6. Strong cancellation is not automatically a rare-history exception

At fixed depth m, the address-label distribution, hence Q_m, is independent of the readout history: histories change internal signs/words, not the preparation-label map. The native instrument gives sum_{|h|=m}M_h=1 and at most L=2^m histories. Thus for any theta>0,

    Pr_native(gamma_h<=theta)
      = sum_{h: M_h<=theta Q_m} M_h
      <= min(1,L Q_m theta).                       (10)

Zero-mass histories contribute zero. This is a valid explicit mass bound but becomes weak when L Q_m is large. It does not justify treating all high-cancellation histories as rare. The new precombination result is therefore a representation repair, not an excuse to drop the difficult histories.

## 7. Generalization contract and honest stopping boundary

For a general history one may certify a partition, or an involutive pairing, at the level of FULL X_e. Exact opposite pairs preserve the entire vector when removed. If pair defects remain, retain their summed vector or bound it explicitly. A return certificate alone supplies no law for alpha(e+R) under general ordered, noncommuting feedback. Any extension must certify that law, not infer it from a smooth envelope.

To reuse the earlier probability intervals, retain actual support overlaps, variable diagonal terms, all scales, and the proof of whichever new variance bound is used. The previous 2.5-level theorem assumed deterministic prescribed-width intervals and is not newly established for this statistical scheme. Independent pilot selection avoids silently conditioning production samples on discovered convenient relations; same-batch adaptive discovery requires its own argument.

Completed here: a source-scoped Rao-Blackwell variance theorem for signed quadratic observations; an exact boundary representation for a previously costly alternating-sign family; a quantified improvement of its cancellation parameter from any useful verified odd return; and the all-history bound (10). No new scientific execution, global Shor dequantization, physical carrier/slow-time theorem, native-to-ideal error improvement or independent mathematical admission is claimed.

Next executable scientific unit: implement the return-certificate/boundary reducer through the unchanged typed backend, then the variable-diagonal batch observer. Test minimal and nonminimal verified returns, the no-shortening and zero-mass cases, invalid returns, preservation of full raw state up to the retained common scale, and equal conditional future readouts. Discovery work must appear in the same cost ledger. No historical fixture is rerun here.

## 8. Prior art and current query receipt

Rao-Blackwell conditional averaging and antithetic variance reduction are established methods, not novel principles claimed here. Original publisher metadata/abstracts were inspected:
- Casella and Robert, Rao-Blackwellisation of sampling schemes, Biometrika 83(1), 81-94 (1996), DOI 10.1093/biomet/83.1.81. https://academic.oup.com/biomet/article-abstract/83/1/81/255465
- Hammersley and Morton, A new Monte Carlo technique: antithetic variates, Mathematical Proceedings of the Cambridge Philosophical Society 52(3), 449-475 (1956), DOI 10.1017/S0305004100031455. https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/new-monte-carlo-technique-antithetic-variates/69A9BBEDC6A4F1B1AF7E0764CD422E15
These are attribution, not external proof of the native identities above. No full-PDF audit or priority claim is made.

One standard exact-title Scholar query for the first title was actually submitted and read back: Issue2572, batch4266c9f0-87aa-4f58-b7d1-2ca62590e841, turn9af578b2-00bc-45ae-9043-54b183fd1cb9, same conversation key. Request SHA256 ef12ce897e84afe1e4a0f62b4f80ce526d924e29e038764ec0e1704d9669f616. Created2026-09-28T09:33:41Z; accepted09:33:49.072185Z; completed09:34:00.512792Z. Matched result https://github.com/awdawmip/kimi-query-bridge/issues/2572#issuecomment-5867275489. Outer FAILED; child PARTIAL/retrieval_verified=true; one relevant title/metadata/abstract preview, not full text. One confirmed provider query, zero bridge model calls, upstream internal calls and billing unknown. Status PARTIAL_READBACK; no retry or completed-source cache claim.
