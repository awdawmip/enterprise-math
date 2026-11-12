# R749SB — Exact hidden signed-source posterior, entropy budget, and Fisher-information loss under the 8:1 unsigned observer

Date: 2026-11-12. Status: AUTHOR-DERIVED / FINITE EXACTLY CHECKED / INDEPENDENT REVIEW PENDING. Researcher: EM-DIRECT-9F7D25, same verified own Site session MCP-b52a077b5aa04731bc5becbaa95d0eba and research activity RA-D46184D9060689BCC1124235 (continuation of draft PR #2170). This is scoped independent author science, not a new CLAIM/Result for RS-X6-TRIADIC-CLOSURE-DYNAMICS.

Scientific pin retained: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Consume R749N @e8c5c874aca5b7098acfdbaf8fadb8ad64a1506f and R749S/R749SA @ec7b7eec75e177e9d10c99b5cf943400189416d1. No change to P000, six native axes, three-force primitive closure, source/provenance guards, or frozen physical science. Only a finite observer Markov candidate P_p is modeled; no native PASS or physical event grant follows.

## Setup

Let the R749SA finite signed carrier D have 960 directed edges, with an unsigned directed-support observer Π:D→D_U of cardinality 120 and exactly 8 lifts per observed edge. The stationary signed initial edge is uniform. At each subsequent step, among the 16 signed adjacent choices one is the forced named-signed-Port C1 completion with mass q=(1+15p)/16, while 15 alternatives have mass r=(1-p)/16. Here p∈[0,1]. Each unsigned next-support has two signed representatives. The forced unsigned support receives total probability a=q+r=(1+7p)/8, and each of the other seven unsigned choices receives b=2r=(1-p)/8. For 0≤p<1 all legal paths have positive mass.

Given an unsigned legal n-vertex path A=(A_0,...,A_{n-1}), n≥2, put m=n-2 and K=number of its m unsigned C1 completions. A *signed lift* is any legal named signed-Port n-path Z with Π(Z)=A. For each step whose unsigned support is forced, label whether its signed lift also follows the exact forced signed-source successor.

## Theorem 1. Exact conditional source distribution and path-lift count

Every legal unsigned n-block has exactly 8·2^m signed lifts. If K=k, the number of lifts having exactly j signed-source C1 completions is

    N_A(j)=8 · 2^(m-k) · binom(k,j),       0≤j≤k,

and N_A(j)=0 otherwise. This count holds for every specific unsigned block and arbitrary n≥2; the support count does not depend on p.

Under P_p and conditioned on that unsigned block, its initial 8 signed directed-edge lifts remain equiprobable. Given the initial lift, successive hidden binary choices are conditionally independent as variables with history-dependent *labels* but state-independent *probabilities*: at each unsigned C1 step the exact signed C1 choice has probability

    t(p)=q/(q+r)=(1+15p)/(2+14p),

while at each unsigned non-C1 step the two signed lifts have probability 1/2 each. In particular,

    J = number of exact signed C1 steps | (A,K=k)  ~ Binomial(k,t(p)).

Proof. For fixed signed incoming edge and fixed unsigned next support, exactly two signed outgoing lifts exist; when that unsigned support equals the deterministic unsigned C1 successor, exactly one is also the deterministic signed C1 successor. Thus their weights are (q,r), else (r,r). The conditional probabilities are (t,1-t), else (1/2,1/2), independent of previous hidden signs. Multiplying the conditional probabilities proves the factorization. Strong lumpability of R749SA makes the likelihood of any unsigned future independent of which of the eight initial signed lifts was chosen, so the uniform 1/8 initial posterior survives all future unsigned observations. Combinatorial multiplication gives N_A(j). Boundary p=1 is interpreted only for positive-probability unsigned paths, all of which have K=m, and the signed completion becomes deterministic after its initial lift.

## Theorem 2. Exact source-residual entropy and irrecoverable initial provenance

Let H_2(t)=-t log2(t)-(1-t)log2(1-t), with H_2(0)=H_2(1)=0. For every legal observed unsigned n-block A of positive P_p probability,

    H(Z_0,...,Z_{n-1} | Π(Z)=A) = 3 + K H_2(t(p)) + (m-K).

The initial signed directed-edge lift has conditional entropy exactly 3 bits given **any** finite unsigned history, at every p∈[0,1]; it is not identified by an arbitrarily long unsigned path under this model. In expectation,

    H(Z_0,...,Z_{n-1} | unsigned n-block)
      = 3 + m[a H_2(t)+(1-a)].

The instantaneous hidden-sign uncertainty is observer- and noise-dependent: at p=0 it is exactly 3+m bits; at p=1, on the supported deterministic unsigned paths, it is exactly 3 bits.

Proof. Theorem 1 gives one uniform eight-choice initial hidden variable and m conditional independent binary choices with entropies H_2(t) at the K forced unsigned steps and one bit at each other step. Apply the entropy chain rule; E[K]=ma by R749SA. Persistence of the initial three bits follows from the strong-lumpability likelihood identity for any unsigned future.

## Theorem 3. Exact loss of parameter information and data-processing identity

Let p,p'∈(0,1), q'=q(p'), a'=a(p'), t'=t(p'). For full signed n-path law P_p^(n) and its unsigned pushforward Q_p^(n), in natural-log units,

    D(P_p^(n) || P_p'^(n)) = m d(q||q'),
    D(Q_p^(n) || Q_p'^(n)) = m d(a||a'),

where d(x||y)=x ln(x/y)+(1-x)ln((1-x)/(1-y)). Moreover the exact chain-rule difference is

    D(P_p^(n)||P_p'^(n)) - D(Q_p^(n)||Q_p'^(n))
       = m a(p) d(t(p)||t(p')).

The term is strictly positive for m>0 and p≠p' in the interior. Its only source is the sign-sensitive C1 choice conditional on unsigned C1; non-C1 hidden binary choices and the initial sign lift are independent of p.

Proof. R749N gives the signed sufficient statistic and its Bernoulli(q) likelihood; R749SA gives the unsigned Bernoulli(a) likelihood. Condition on the unsigned path and apply the KL chain rule. Its K forced unsigned steps have independent hidden Bernoulli(t), with E_p K=ma; all other hidden choices are fair, while initial signed lift is uniform for both models. The expression follows and establishes strictness since t'(p)=4/(1+7p)^2>0.

For 0<p<1, the exact Fisher information in one subsequent transition is

    I_signed(p)=15/[(1+15p)(1-p)],
    I_unsigned(p)=7/[(1+7p)(1-p)],
    I_hidden(p)=I_signed-I_unsigned
                =8/[(1+15p)(1+7p)(1-p)].

The finite n-block information is m times each expression (initial distribution carries no p-information). The ratio is

    I_unsigned/I_signed = 7(1+15p)/[15(1+7p)],

rising from the right-hand boundary limit 7/15 as p↓0 to 14/15 as p↑1. At p=1/2 the signed, unsigned and hidden information are exactly 60/17, 28/9 and 64/153 respectively; the retained fraction is 119/135. This quantifies observer-dependent information loss without a large-m approximation. Boundary p=0,1 use probability/entropy statements; regular interior Fisher calculus is not asserted at those parameter boundaries.

## Complete finite check and implications

The checker R749SB_EXACT_HIDDEN_POSTERIOR_CHECK.py builds the actual 60 signed vertices, 960 signed edges, 15 unsigned supports, 120 unsigned edges and 8 signed lifts per unsigned edge. It exhausts all 120·8²=7,680 legal unsigned four-vertex blocks and all 245,760 signed lifts, verifying for each block the complete j-histogram 8·2^(2-k)·binom(k,j), and exact rational block probability for p∈{0,1/2,1} (when defined). It checks the exact rational Fisher formulas at p=1/2. Integer aggregated count across all blocks by (K,J):
    (0,0):188160; (1,0):26880; (1,1):26880;
    (2,0):960; (2,1):1920; (2,2):960.
The all-n, all-p claims rest on the transition fiber argument, not on finite extrapolation.

Application: an unsigned support-only readout is exactly sufficient for future unsigned support events yet retains an irreducible three-bit ambiguity about initial signed-Port provenance and loses a quantified amount of information about p. For BRC-sensitive observations, safe compression requires explicitly declaring which provenance queries and operations remain admissible. The next test is a *typed* actual native Cell/Link/Port event family (with TRIADIC_CLOSURE_E/V29/V39 guard): determine whether its signed transition can be represented by this binary-fiber construction and whether an initial signed source may be gauge-identified. The present Markov interpolation is not itself evidence of such an event license.
