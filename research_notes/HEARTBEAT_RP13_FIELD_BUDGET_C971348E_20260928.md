# RP13-FIELD-BUDGET: exact remainder energy, child-field precision budgets, and seed-independent cost accounting

Progress-Event-ID: RP13-FIELD-BUDGET-C971348E-20260928
Status: AUTHOR_DERIVATION_ONLY / LOCAL_NUMERICAL_VALIDATION_PENDING / UNREVIEWED / NOT_ADMITTED
Date: 2026-09-28 Asia/Taipei
Global read snapshot: 4045cca748e572a142dcce5d4abd3cb79c3f8150
EM intake and publication preflight: ac646d388662328a45580bb61a84adce4f264ad6
Logical conversation: chat-stage101-c971348e64294a5882dfc50fcc8217f1

## 0. Evidence and non-execution boundary

The exact attached RP12_REPLICA_EXEC report, proof and delivery were read in full through Files. They identify the parent runtime ZIP as BRC_RidgePrecision_RP12_REPLICA_EXEC_RUN_20260928.zip, 165833129 bytes, recorded SHA256 bce6c67b4c18d4f877e53a4cb1eb9c722eaab8489ad2e379a76f3b9677dde63b; parent engine SHA256 1638600820afb95223ced844d840f1d4edc0ea57a0204e977b2174f45b5e3d44. These are inherited recorded hashes, NOT newly computed hashes in this turn.

Container execution, analysis Python and visible Python each returned ClientError. No archive extraction, numerical BRC call, new output distribution, timing, binary hash validation or runtime implementation is claimed here. The visible Python integrity/extraction request did not complete. This note captures symbolic derivations and an explicit proposed algorithm, not an executed RP13 sampler. Parent results remain at their existing author-executed, not independently admitted strength.

P000 and the residual-faithful position are unchanged. The carrier is the actual RP12 H18 representative space, with positive diagonal BRC metric W: one weight2, one weight6, sixteen weights1, sum24. Original b12 gates, signed complete row semantics, exact dyadic exponents, work labels, modular incidence, gate order and terminal factor verification are unchanged. No new ideal-QFT reference, pi/trigonometry, higher gate precision or known order/factor input is introduced.

## 1. Exact remainder energy, not norm loss as a surrogate

For one raw row x=n*2^e and K>=1 let s=max(0,maxbit(abs(n))-K), q_i=sign(n_i)*(abs(n_i)>>s), and z=q*2^(e+s). Define signed discarded integer residues r_i=n_i-2^s q_i. Zero rows use canonical zero. Then, exactly in the inherited diagonal BRC observer:

E(x,K)=Q_W(x-z)=2^(2e) sum_i w_i r_i^2.
L(x,K)=Q_W(x)-Q_W(z)=E(x,K)+2^(2e+s+1) sum_i w_i q_i r_i.

Each q_i*r_i>=0, so 0<=E<=L. This is a rearrangement of the already established RP12 inward-truncation identity, now used as an error-accounting interface. It is not new numerical BRC execution. Preserve each row's exponent when adding error energies across labels; equal mantissas with different exponents are not equal fields.

It is unsafe for efficiency to equate E with L. The symbolic inward scalar pair x=1,z=1-tau, 0<tau<1, has E=tau^2 but L=2tau-tau^2. This illustrates the difference, not a claim that Q_K(1) produces that pair, nor a reachable BRC fixture. A loss-only gate can demand much more precision than an exact-error gate. Error-residue extraction/squaring/alignment has costs; it is not automatically free just because branch masses are already computed.

## 2. Child-field error budgets allow heterogeneous row precision

At a fixed history h, first form the complete raw bit-b child a_hb by the inherited actual BRC instrument. Let A_hb=sum_w Q_W(a_hb(w)). Only then select the mantissa caps K_(h,b,w), using a deterministic policy of this complete child and declared public parameters. Let z_hb(w)=Q_K(a_hb(w)), retaining all label associations, signs and dyadic scales. Define:

Delta_hb=sum_w E(a_hb(w),K_(h,b,w));
C_hb=sum_w Q_W(z_hb(w)).

For A_hb>0 accept the precision assignment as an approximation only when Delta_hb<=epsilon_i^2*A_hb, where i is this nonterminal depth. This is a field-level condition, not the stronger requirement that every row have relative error<=epsilon_i. If a row has mass fraction p_w and relative squared error d_w^2, then Delta/A=sum_w p_w*d_w^2. A low-mass row can therefore consume a larger relative error while the full joint field still obeys the same bound. This is controlled approximation, not exact identification of unequal rows and not permission to discard labels.

Because each row is inward-truncated, C<=A. A nonzero row is not deliberately erased: one of its maximal mantissa components survives for K>=1. Exact zero children are skipped without dividing by zero. No per-row normalization is introduced: relative strengths remain in the exact exponents and mantissas.

The policy must not depend on a private latent walker, arbitrary query order, factor-event mask, future outcome, timing jitter or success-biased seed selection. It may depend on the full current child, as the current full-field implementation already materializes that child. This is NOT a cheap point-query construction. Precision selection changes the target; it is not a same-random-tape rewrite of the old fixed-K target.

## 3. A finite proposed selector with a hard upper cap

A deliberately simple first implementation can try one common K for all rows of a child, in the predeclared order 8,10,12,14,16,17. Form each candidate from the ORIGINAL raw child, not from an already rounded earlier candidate. Choose the first K passing the exact Delta/A test. All attempts at candidate evaluation must be charged.

Set epsilon_i=2^-13. The inherited all-row bound at K17 is 5*2^(1-17)=5/65536<1/8192=epsilon_i. Therefore the K17 candidate must pass on every nonzero field in the certified H18 carrier, under exact arithmetic and the specified exponent semantics. This gives at most six candidate passes and a stored representative-magnitude cap<=17 bits. A failure at K17 is an implementation/certificate failure, not permission to silently relax the budget. An explicit exact-row fallback remains a separate safety route and voids the hard17-bit claim for that record.

This upper cap is an algebraic sufficiency result, not an observed typical K. There is no evidence yet that K8/10/12 often passes. A later per-row selector can improve allocation, but solving or greedily approximating the multiple-choice error/storage tradeoff has its own cost and does not automatically optimize wall time. Do not describe the six-pass prototype as cheaper than fixed-K until it is timed.

## 4. Sampling and complete-history guarantee

Let M_h be the squared norm of the approximate surviving field at h, normalized so M_empty=1. The inherited two-arm isometry gives A_h0+A_h1=M_h. Choose b with probability A_hb/M_h and retain the whole-attempt correction C_hb/A_hb. A rejection ends the entire attempt and restarts the standard initial state. Compression-candidate rejection merely selects a finer candidate or exact fallback and must not be confused with random trial rejection.

Induction gives Pr(reach h after all preceding corrections)=M_h, since M_h*(A_hb/M_h)*(C_hb/A_hb)=C_hb=M_hb. Hence surviving terminal masses m_k determine Z=sum_k m_k and P(k)=m_k/Z. Keeping the latent label and retrying only the current bit is not this distribution.

For each depth, concatenate all complete classical histories, labels and weighted internal modes in their declared direct-sum carrier. The raw gate map L_i is an isometry. If every positive-mass child satisfies Delta<=epsilon_i^2 A, the aggregate approximation error at this layer is at most epsilon_i times the aggregate input norm; the quantizer also contracts norm. With initial norm1:

TV(P_new,P_exact_same_b12)<=min(1,sum_i epsilon_i);
Z>=product_i(1-epsilon_i)^2.

Proof: write V_i=L_i V_(i-1), U_i=L_i U_(i-1)-e_i. Then ||V_i-U_i||<=||V_(i-1)-U_(i-1)||+||e_i||, and ||U_i||<=1. At the end, for u=U/||U|| and a=<V,u>, 1-|a|^2<=||V-U||^2. The classical readout TV is bounded by the resulting pure-state distance. This is the same explicit algebraic bridge as the parent, with the per-row condition replaced by a proved child-field condition; no assertion that arbitrary nonlinear quantization is pairwise nonexpansive is used.

At t16 there are15 nonterminal boundaries. Epsilon=2^-13 gives TV_new_to_exact<=15/8192. The original active21/K16 target has TV_old_to_exact<=75/32768 under the parent's dimension constant5. Therefore:

TV(P_new,P_old21K16)<=135/32768<1/200.

This is a sufficient absolute event-probability difference bound, NOT 99.5% factoring success, not a bound to ideal QFT/b64, and not an observed probability. The original b12 bank error and all work-label/query complexity remain separate.

## 5. A posteriori error-energy and survival bounds

Let Z_i=||U_i||^2, Z_0=1, and let D_i=||e_i||^2=sum_(h,b at i) Delta_hb. Because each inward truncator obeys squared error<=norm loss:

0<=D_i<=Z_(i-1)-Z_i.

The same direct-sum argument yields:

TV(P_new,P_exact)<=min(1,sum_i sqrt(D_i))
                 <=min(1,sqrt(s*sum_i D_i))
                 <=min(1,sqrt(s*(1-Z_s))).

The first bound uses the actual errors; the last uses only total surviving mass and may be MUCH weaker than the fixed-K or epsilon_i bound. When several certificates are available, take the smallest valid bound rather than claim the new expression dominates them. These D_i and Z_i sum over the FULL unnormalized history tree, not one sampled trajectory and not separately renormalized conditionals.

Do not replace Z by 'we observed no rejection'. In a predeclared fixed-n experiment of independent attempts, observing n successes gives the one-sided exclusion Z>=alpha^(1/n) at error probability alpha (other outcomes require a different confidence calculation). Combining with the survival-only bound requires n>=log(alpha)/log(1-epsilon^2/s) to certify TV<=epsilon from zero failures. The sufficient estimate n>=s*log(1/alpha)/epsilon^2 follows from -log(1-x)>=x. These are symbolic statistical-resource formulas, not new tests, and continuous peeking would need an anytime-valid treatment. High empirical survival alone is not a cheap strong accuracy certificate.

## 6. Seed-independent expected work to a verified factor

Fix one complete policy and one input. An attempt starts at the standard initial state and ends at either a correction rejection or a terminal output. Let Gamma be the unchanged precise factor-verifier event; it is used only at the terminal observer, never fed back into evolution. Define:

Z=sum_k m_k;
p=sum_(k in Gamma)m_k/Z;
gamma=sum_(k in Gamma)m_k=Z*p.

Let C be the conditional-on-start EXPECTED complete attempt work, including unsuccessful attempts. For independent identically distributed restarts, with stationary cost distribution and gamma>0:

E[work until verified factor]=C/gamma.

Cost and success within an attempt need not be independent. The first-step identity is T=C+(1-gamma)T. A preparation cost B paid once gives B+C/gamma. A zero-success policy has infinite expected solver work under this stopping rule, even if its attempts terminate quickly. Warm caches or changing precision across trials can break stationarity; reset them or explicitly model their changing cost state before using this formula. This is a renewal identity, not a newly invented theorem and not a wall-clock measurement.

An exact finite-tree work audit can remove seed luck without assuming a free full-tree oracle. Let c_h be the conditional expected local work incurred after entering surviving history h and before moving to its next surviving child or ending the attempt; let v_k be terminal-verifier work. Then:

C=sum_(nonterminal h) M_h*c_h + sum_(terminal k) m_k*v_k.

In an implementation that prepares both raw arms before choosing b and quantizes only the selected child, split this as sum_h M_h*p_h + sum_(h,b) A_hb*q_hb + sum_k m_k*v_k, with random-bit/correction overhead explicitly assigned to the appropriate reward. Other execution orders need their own reward placement. Gate applications, integer operations, row visits or a declared bit-cost surrogate can be counted exactly; these are not exact CPU seconds. Full-tree enumeration may itself cost exponentially in t and is an OFFLINE DIAGNOSTIC, not a proposed free online sampler.

For baseline0 and candidate1, the real improvement condition is C1/C0 < gamma1/gamma0, after appropriate setup accounting. If p0 is known, |p1-p0|<=delta and Z1>=z_min, then gamma1>=z_min*max(0,p0-delta). For p0>delta, C1/C0 < z_min*(p0-delta)/(Z0*p0) is sufficient. No blanket 'lower precision is faster' follows.

As a further boundary, with independent fresh restarts and no setup differences, one cheap attempt followed by a fixed high-precision solver has expected cost C_L+(1-gamma_L)*C_H/gamma_H. It beats starting with H precisely when C_L/gamma_L<C_H/gamma_H (gamma_L>0). Merely arranging coarse then fine is not an extra source of speed. Deferred setup costs, informative observations or reusable state require a separate model and can change the comparison.

## 7. Concrete next execution unit

Implement the original-raw-child six-cap selector and error-energy ledger using the unchanged RP12 weighted BRC observer. First check signs, exact exponents, zero children, K17 guarantee, no factor-mask access, deterministic replay and complete-trial rejection. Use the already frozen N21/a2/t12 law only as regression, not new discovery. Then predeclare new complete-law inputs N33/a5/t12 and N77/a2/t12, both inside the already certified maximum gate level16. Compare active21/K16, rep18/K16 and the new adaptive-child target. Compute all probabilities, Z, gamma and exact declared work rewards before interpreting sampled until-factor times. Do not silently extend the18-coordinate carrier beyond the certified bank or call t12 the default factoring width for every input.

A separate timing phase must include selection passes and failed attempts, compare fixed setup versus amortized setup, and report all unfavorable outcomes. A useful stopping point is a reproducible new full-law/work comparison, not another dimension count. This turn has NOT executed any of these planned tests.

## 8. Literature, control and persistence scope

External checks were limited to official abstracts/publication records for Bravyi/Gosset/Liu arXiv:2112.08499, Gao arXiv:1410.5688 / PRA92,052331, and Oskouei/Mancini/Wilde arXiv:1804.08144. Sequential disturbance bounds and amplitude-query sampling are prior art; their statements are not silently transferred to this nonlinear BRC quantizer. No full-text novelty-completeness review is claimed. All displayed inequalities above have their explicit derivation rather than relying on those abstracts.

Status request2565 (status-rp13-budget-c971348e-20260928-01) returned matching SUCCEEDED transport, version0.6.8, original session start stage101-session-c971348e-02, research_authority_granted=false. No new session, RA, CLAIM, run, formal Result or independent review is asserted. Parent permission/registration issues are not resolved by this note.

GitHub and Drive write actions are available this turn, unlike the parent turn. This file records the math only; actual publication readback and any Drive backup result are reported separately. LOCAL_NUMERICAL_VALIDATION_PENDING remains. Do not claim a new runtime ZIP or a newly verified parent hash. Preserve the RP12 recorded evidence and pending-sync history. The parent research objective remains open; no general efficient label-query algorithm, polynomial classical Shor result or hardware/physics advantage is established.
