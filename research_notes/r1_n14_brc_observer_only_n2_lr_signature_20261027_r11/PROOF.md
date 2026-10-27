# R1/N14 — Unique coarsest observer-only quotient at depth two: conditional likelihood-ratio signatures

**2026-10-27. Author mathematical proof and exact finite rational certificate. Not a native Result, independent review, or a P000/X6 physical theorem.**

## Sources and role

GLOBAL_KNOWLEDGE_V1 immutable study snapshot: awdawmip/chatgpt-global-knowledge@8bb9a989344e8317654f0d9b79873213fad73574 (bootstrap, manual, Enterprise Math router/P000, ACTIVE worldview). Enterprise Math initial science snapshot: awdawmip/enterprise-math@0157689888f0f853a4404dd9abc9f7b24096adcd; current portable protocol docs/PORTABLE_RESEARCH_PROTOCOL.md. Immediate predecessor: research_notes/r1_n14_brc_observer_only_n2_sharp_20261027_r1/PROOF.md (sharp strictly-positive ternary N=2 seven-state instance).

Local Researcher-ID EM-R1-N2SG11, research activity RA-R1-20261027-N2-LRSIG11. No official native task CLAIM or independent review is asserted; no active owner is displaced.

BRC reuse: positively weighted labelled path masses (P(h),Q(h)) and their likelihood-ratio fibers; complete provenance is retained until a future-observer-safe quotient is proved. Declared observer is (T,D), with T separately typed as stopping time, D binary. This is **external auxiliary finite-path probability mathematics**, not a native Cell or Heartbeat evolution. There is no native X6 embedding/readout/future-operation preservation certificate, and no signed/complex amplitude cancellation is claimed.

## Model, quantifiers and state class

Finite nonempty alphabets A and B, one initial root, observations I in A at time 1 and J in B at time 2. Strictly positive laws P,Q are specified by

(1) P(I=i)=Q(I=i)=pi_i>0 and sum_i pi_i=1;
(2) P(J=j|I=i)=p_ij>0 and sum_j p_ij=1;
(3) Q(J=j|I=i)=r_j p_ij for positive r_j independent of i, with sum_j r_j p_ij=1 for each i.

Consequently Q(ij)/P(ij)=r_j; Q(i)/P(i)=1.

Full policies may use any common history-dependent randomized stopping and binary D decision at t=0,1,2. Admissible compressed policies use time-typed deterministic state z_t(h), symbol-labelled deterministic update rho_t(z_t(h),a)=z_{t+1}(ha), a common P/Q state-local stochastic decision kernel and fresh randomization without persistent hidden selector. Target: **for every full policy, there exists one law-independent compressed policy simultaneously preserving the two joint laws of (T,D)**.

Let R be the set of distinct r_j values. Define the conditional likelihood-ratio signature

mu_i(r) := sum_{j : r_j=r} p_ij,  for r in R.

This is a probability distribution on the finite likelihood-ratio alphabet R.

## Theorem: unique coarsest sufficient recursive quotient

The time-typed state

z*_0=root; z*_1(i)=mu_i; z*_2(ij)=r_j

with updates rho_0(root,i)=mu_i and rho_1(mu_i,j)=r_j is universally observer-sufficient. Indeed it preserves under P and Q the richer joint laws (T,z*_T,D).

Conversely every universally observer-sufficient deterministic time-typed right congruence z satisfies

(A) z_1(i)=z_1(k) implies mu_i=mu_k;
(B) z_2(ij)=z_2(kl) implies r_j=r_l.

Therefore z* is the unique coarsest sufficient time-typed partition (up to renaming). Its exact minimal state profile is

(1, |{mu_i}|, |R|),  total 1+|{mu_i}|+|R|.

### Proof: constructive sufficiency

Copy the full policy's initial root stop/decision. Conditional on root continuation let c_i be its probability of continuing after I=i; on first-time stopping let e_i be its D=1 probability. For a first-state group G of equal signatures, put Pi_G=sum_{i in G}pi_i and

c_G = sum_{i in G}pi_i c_i / Pi_G.

If Pi_G(1-c_G)>0, set e_G=[sum_{i in G}pi_i(1-c_i)e_i]/[Pi_G(1-c_G)], otherwise choose 0. Because the initial marginal pi is the same under P and Q, both first-time stopped masses and D decisions, even per G, are preserved.

For each G and ratio r, the original P arrival mass after continuation is

sum_{i in G}pi_i c_i mu_i(r) = Pi_G c_G mu_G(r),

which equals the quotient P arrival mass. The corresponding Q arrival mass is exactly r times this value, in both the full and compressed histories. Let d_ij be the full terminal D=1 conditional probability (given continuation and terminal history). Put

A_r=sum_{i,j:r_j=r}pi_i c_i p_ij,
U_r=sum_{i,j:r_j=r}pi_i c_i p_ij d_ij.

At terminal quotient state r choose D=1 with d_r=U_r/A_r if A_r>0, else 0. Under P the D=1 mass is U_r; under Q it is r U_r. D=0 follows from matched arrival masses. The root, T=1 and T=2 distributions of (T,z*_T,D) now agree under each law. Every randomization used is a fresh current-state coin. This proves universal sufficiency for all full policies, not only rational policies. □

### Proof: terminal-ratio necessity

Take full policies which certainly continue until T=2. Since all prefixes have strictly positive P mass, any matching compressed policy must also continue with probability one on every first-stage quotient state. At time 2 its D=1 choice is constant within each terminal quotient state S. For any real threshold a, the maximum of the observable linear form Q(T=2,D=1)-a P(T=2,D=1) is, for full histories,

sum_h P(h)[Q(h)/P(h)-a]_+,

whereas for the quotient it is

sum_S [sum_{h in S}(Q(h)-aP(h))]_+.

If a terminal state S mixes two distinct terminal ratios, choose a strictly between them. Both signs occur with positive masses, so positive-part subadditivity is STRICT on that state. Then the full maximum is strictly larger, contradicting universal sufficiency. Thus terminal states cannot mix distinct r_j. □

### Proof: first-symbol signature necessity, via exact support separation

For arbitrary reals u,v define b_j=u+v r_j and

s_i(u,v)=sum_j p_ij [b_j]_+ = sum_{r in R}mu_i(r)[u+v r]_+.

Consider the linear functional of observable law-pairs

L = u P(T=2,D=1) + v Q(T=2,D=1) - lambda P(T=2),

with real lambda. Because P(I)=Q(I)=pi, the exact full-policy maximum is

F_full = sum_i pi_i[s_i(u,v)-lambda]_+.

Indeed after I=i one continues when s_i>lambda and at T=2 chooses D=1 on b_j>0; root stopping cannot improve the nonnegative maximum. If a compressed state merges first-symbol histories in groups G, its continuation probability must be constant within G. Even if we unrealistically give it full terminal-history access, its maximum is bounded by

F_group = sum_G Pi_G[ (sum_{i in G}pi_i s_i /Pi_G) -lambda ]_+.

If some group contains s_i != s_k, choose lambda strictly between those values. Positivity of pi makes the positive-part Jensen inequality strict on that group and non-strict elsewhere:

F_full > F_group >= F_compressed.

Thus such a merge contradicts universal observer sufficiency. Each first-state fiber must have s_i(u,v) constant for all (u,v). Setting (u,v)=(-a,1), this says the finite call-payoff transforms

a -> sum_{r in R}mu_i(r)(r-a)_+

agree for all real a. Their piecewise-linear slope jumps at every r recover exactly the atom masses mu_i(r), so equality of transforms implies equality of entire signatures mu_i. This proves first-state necessity. □

The constructed z* attains both necessary partitions and is recursively updateable, establishing uniqueness of the coarsest quotient and the exact minimum. The theorem assumes the shared time-1 marginal and factorized r_j; it makes no general N>=3 uniqueness claim.

## Exact executable checks

Companion VERIFY.py uses Python standard-library Fraction only; RESULT.json is the exact rational result certificate. The **universal quantified theorem is proved above, not by enumerating policies**.

Instance A (reuses the predecessor's 13 prefixes): pi=(1/3,1/3,1/3), r=(2,1,1/2), P rows (1/4,1/4,1/2), (1/12,3/4,1/6), (1/6,1/2,1/3). All three mu_i differ and the three ratios differ, so profile (1,3,3) gives exactly 7 states. For support vector (u,v)=(-1,1), first-time scores s=(1/4,1/12,1/6). All four nontrivial set partitions of the first-symbol histories yield strictly positive support gaps by exact rational computations; see RESULT.json.

Instance B (genuine nontrivial safe merge): pi=(1/2,1/2), r=(2,2,1/2,1), P rows (1/16,3/16,1/2,1/4) and (3/16,1/16,1/2,1/4). Raw rows differ but both conditional LR histograms equal mu(2)=1/4, mu(1)=1/4, mu(1/2)=1/2. The unique minimum profile is (1,1,3), total 5 states. The full policy 'continue only if I=0; D=1 iff terminal r=2' and quotient 'continue with probability 1/2; D=1 iff terminal r=2' agree exactly on P(T=2,D=1)=1/8 and Q(T=2,D=1)=1/4.

Review boundaries: AUTHOR proof and local exact Fraction checks, not independent Driver review or Lean formal verification. Prior-art and native six-dimensional Cell bridge are pending. No change to P000's axioms or the ACTIVE worldview is proposed.
