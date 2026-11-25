# PREFIX-1081 — Critical sublinear window and two-bin phase competition

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Independent continuation of R6, own session metadata recovered through em_site_control recovery_status (original registration r6-20261123-2358-session-start-own-v1, SID MCP-f6d93209fc8e4c5bb2c3b44f69a47174, researcher EM-DIRECT-780BBE, TASK_RESEARCH, RA-0ABD84561C86E53067DB0322). No CLAIM or shared Task mutation. Prior owner query r6-20261125-1450-owner-read succeeded with empty LEASED filter; new read r6-20261125-1550-owner-read admitted, current terminal result not yet observed at writing.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Stage46 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full paired X6 Cell, port, phase/sign and ordered multiplicity inherited; scalar analytic readouts below are not native spatial or time coordinates.

Parents:
- aab4dd2e200a0f2da10c32b8406164042da8f4c9:research_notes/portable_direct/2026-11-25_r6_prefix1080_negative_mass_lattice_prefactor.md, sections 1–3 (derivative and polynomial bound), section 4 (fixed critical offset).
- 71d4c7bd8025bf3ccc634c00eca5e4d0fa45cccc:research_notes/portable_direct/2026-11-25_r6_prefix1079_negative_mass_rate.md.
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md.
- b47b157958692d0a62f438a3d546baa044168341:research_notes/portable_direct/2026-11-25_r6_prefix1076_uniform_beta_tail_transport.md.

## 1. Critical sublinear theorem

Write D_m(k)=L(x^m(1-x)^k), M=m+r, p=b_last in (0,1/9), rho=(1-p)/p, h=(d+1)/2 for the odd local zero order d. Near p, g(p+y)=A y^d+O(y^(d+1)), A<0. Use the exact continuous last crossing z_M=rho M+c+o(1), K=ceil(z_M)-1, delta=z_M-K in (0,1]. These definitions use the actual crossing, not its rounded asymptotic. Let s=K-k. Assume k->infinity, m=o(k), r/k->1/rho, and s>=1, s=o(k); bounded positive s is included. D_m(k)>0 by inherited uniform positivity. Define
    W(t)=binom(t+r-1,r-1) B(M+1,k+t+1), t>=0,
    q_k=W(s-1)/W(s)=s/(s+r-1) * (M+k+s+1)/(k+s).
Then q_k~s/(p k)->0, and q_k>=c1/k for some constant c1>0. Inherit H=(-A)d!![p^2(1-p)]^h/(1-p)>0 and G_M(Q)=D_M(Q)/B(M+1,Q+1).

The total negative joint mass has the uniform two-bin law
    N_r = W(s) H M^(-h)/D_m(k) * [delta+q_k(delta+1)] * (1+o(1)).  (1)
The relative o(1) holds for arbitrary phase sequences, even delta smaller than every inverse power of k. In addition the fraction of total negative mass in offsets j>=2 (where j=K-(k+S_r)) is O(q_k), uniformly in phase. Thus retaining the final two bins of the negative measure discards at most O(q_k) of its mass; no assertion of lossless native state reduction is made. With exact normalization of the retained bins, total variation error equals the discarded probability mass. The negative mass itself is strictly positive under these assumptions.

If delta/q_k->c in [0,infinity], then the normalized negative mass has a two-point limit:
    P(J=0)->c/(1+c), P(J=1)->1/(1+c)
with the natural convention at c=infinity. In particular the second-last negative bin dominates when delta/q_k->0, and the last bin dominates when delta/q_k->infinity. For bounded s>=1 the same conclusion applies. If s=0, there is only one available bin and N_r=W(0) H M^(-h) delta/D_m(k)*(1+o(1)); its magnitude can be arbitrarily sensitive to the actual phase. If s<0, N_r=0 by the inherited global last-negative support theorem.

## 2. Proof with uniform control of distant bins

The exact grouped joint negative measure has weight W(t)[-G_M(k+t)]_+/D_m(k); this retains every ordered composition with its exact multiplicity. By the support theorem t>s has zero weight. The parent 1080 near-boundary derivative theorem, which is stated for any fixed L0>0 and |Q-rho M|<=L0 log M, gives
    -G_M(K-j)=H M^(-h)(delta+j)(1+epsilon_{M,j})
uniformly for integer 0<=j<=min(s,L0 log M), with sup |epsilon_{M,j}|->0. The proof integrates the derivative from the exact zero; hence it remains relative even at arbitrarily tiny delta. This derivative result does not require theta>1/rho: its proof is in M,Q alone. Since M/k->1/rho>0, the same window can be chosen as L log k.

For t=1,...,s the exact W(t-1)/W(t)=t/(t+r-1)*(M+k+t+1)/(k+t). In the critical regime r~M~k/rho, s=o(k), uniformly the ratio is <=C s/k <= C' q_k, for constants independent of phase. At t=s its exact value is q_k. Consequently W(s-j)/W(s)<=q_k(C' q_k)^(j-1) for j>=1, and in particular the j>=2 near tail divided by W(s) H M^(-h) is O(q_k^2): sum (delta+j) q_k(C' q_k)^(j-1) for j>=2 is bounded by a constant times q_k^2 once C' q_k<=1/2. The j=0 and j=1 weights divided by that same factor are delta(1+o(1)) and q_k(delta+1)(1+o(1)), respectively.

For j>L log k, reuse the global finite-order estimate |G_M(k+t)|<=C k^4 for 0<=t<=s. Its parent proof only needs M/k bounded above/below and beta saddles in a compact subinterval of (0,1); both hold uniformly here because t<=s=o(k). The far tail after dividing by W(s) H M^(-h) is bounded by C k^(4+h) q_k^2 (1/2)^(floor(L log k)-2), with a constant absorbing C' and the geometric series. Choose L>(5+h)/log 2 to make this o(q_k^2). If s is below the cutoff the far sum is empty. Thus all remaining bins together contribute O(q_k^2) in these units. The two-bin sum is at least q_k, so their relative discarded fraction is O(q_k); the uniform derivative error is o(1) relative to their sum. This proves (1), including arbitrarily small phase. Conditional probabilities of the retained bins are proportional to delta and q_k(delta+1), with multiplicative errors tending to zero. Their limiting ratio yields the two-point law. No independent positivity of the global spectral distribution is needed.

The exact q_k has asymptotic q_k~(s/k)*rho/(1-p)=s/(pk). The result includes s growing arbitrarily slowly or as any o(k) sequence. It also resolves the possible loss of the final negative observation when delta nearly vanishes: a two-bin observer retains the leading negative mass whenever s>=1. It does not certify the sign by evaluating an approximate z_M.

## 3. Factorial onset in the narrower window

Define lambda_k=r(k+1)/(M+k+2)~p k. The exact product
    W(s)/W(0)=(r)^(rising s) (k+1)^(rising s) / [s! (M+k+2)^(rising s)]
follows from the binomial multiplicity and the beta recurrence. Since r,M,k are of order k, the log of the ratio to lambda_k^s/s! is O(s^2/k), by summing log(1+i/a)=O(i/a) for 0<=i<s=o(k). Hence for 1<=s=o(sqrt(k)),
    N_r ~ [B(M+1,k+1) H M^(-h)/D_m(k)]
          * lambda_k^s/s! * [delta+(s/lambda_k)(delta+1)].  (2)
Indeed q_k/(s/lambda_k)->1 uniformly in this window (the exact recurrence shows the error O((s+1)/k)); replacement is relative even if delta tends to zero, because all bracket terms are positive. Keep exact lambda_k and B(M+1,k+1) to avoid losing contributions of m or r rounding. For sqrt(k)-scale or larger s, use the exact rising-factorial product, not the simplified factorial approximation. This is an analytic readout identity, not a new classical/native computation.

## 4. Precision implications and scope

For s>=1 the phase bracket in (1) is between q_k and 1+2q_k. The phase-sensitive part of minus log2(N_r), with the other exact factors fixed, is therefore at most log2(k/s)+O(1) above its order-one phase value; if delta=o(q_k) it attains log2(k/s)+O(1). This gives a critical-window precision correction not present at fixed supercritical theta. The exact distance to probability distributions is 2N_r by parent 1078/1079. This is a norm-separation statement, not a mantissa guarantee. For s=0 no such uniform bound in phase is asserted. Conditional ordered compositions within a bin remain exactly uniform as in the parents; sign, port, phase, branch identity and multiplicity of the original carrier are not discarded by this readout theorem.

Validation: complete analytic argument conditional on the inherited finite-order observer, last-negative support and local derivative. No new native kernel/path enumeration, classical numerical comparison, pi/trig evaluation, independent review or formalization. Actual p, d and lattice phase remain uncertified numerically. The mother objective B_fix,odd(32) remains open.

Next: certify p and d on the authorized BRC carrier; develop interval-certified evaluation of the continuous crossing/derivative or directly of the adjacent signed differences so phase classification does not rely on rounding an asymptotic zero. Explore the transition s~sqrt(k) by retaining the quadratic correction in the exact product; the present theorem already covers all s=o(k) with exact W.
