# Stage308-B — exact eight-rate Pareto endpoint tangent; strict local symmetry breaking

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Author: local portable Researcher-2, not an authenticated native Source researcher/CLAIM. This is an external finite positive-rational BRC branch/observer model, NOT P000 X6 dynamics or an independently reviewed theorem.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@66563d16db1da2eb54f5fdaa74f4e62d6eceaadc (original P000 V4 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc); Enterprise Math main@1d6845f8f03cbd6d6647a57d5ad25877f0d06a7e (original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; ACTIVE source/portable protocol). Source owner query: CONTROL_QUOTA; current active owner UNKNOWN. Site research_authority_granted=false. Predecessors: Stage307-B.1 commit 505192696012143fbbbc8a4cbd690bd59112568d; Stage307-B.2 commit 128d2ce6aeb0299cdf842d0ad65082a64ba9d475.

## Frozen model and exact objectives

S is fair. Conditional on S=s, J,W,Y are independent; J identifies s with probability 7/8, W identifies s with probability 3/4, and Y is Bernoulli(p_s), with p_0=1/4,p_1=3/4. The visible initial fiber is G=(W,Y). The private h=(J,W,Y) branches in order 000,001,010,011,100,101,110,111 have pairs (256 Pr(S=0,h),256 Pr(S=1,h))=(63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63). All 16 masses are strictly positive.

True F outputs are conditionally IID Bernoulli(p_S). The compressed F port fixes one real rate t_h in [0,1] per private h, unchanged during 3 visits; its F outputs are conditionally IID Bernoulli(t_h). H is independent fair. For each rate table, the worst public-history-adaptive H/F trace total variation with G retained is P(t); with original S,J also revealed at the end, it is T(t). As proved in Stage307-B.1 §2, all potential F and H bits may be presampled, and any randomized adaptive trace is a common Markov image. All-F is a permitted policy, so BOTH worst TVs exactly equal the always-F TV for each t, not a restricted heuristic.

Define b_k(z)=z^k(1-z)^(3-k); D_3(u,v)=1/2 sum_{k=0}^3 binom(3,k)|b_k(u)-b_k(v)|. With a_h=Pr(S=0,h), b_h=Pr(S=1,h), m_h=a_h+b_h, the exact functions are

P(t)=1/2 sum_{g,k} binom(3,k)|sum_j [a_{jg}b_k(p_0)+b_{jg}b_k(p_1)-m_{jg}b_k(t_{jg})]|,
T(t)=sum_h [a_h D_3(p_0,t_h)+b_h D_3(p_1,t_h)].

The unique joint minimizer t^MAP chooses p_0 if a_h>b_h and p_1 otherwise. Prior exact result: T_*=77/1024, P_0=P(t^MAP)=11/256. Define the FULL eight-real-rate Pareto value F(p)=min{T(t):P(t)≤p}; it is well-defined for P_min≤p≤P_0, where Stage307-B.2 establishes P_min<P_0.

## Theorem 308B.1 — sharp one-sided slope of the FULL Pareto envelope

lim_{p up to P_0, p<P_0} [F(p)-T_*]/[P_0-p] = 13/32.

Proof: Compactness gives minimizers. For every h, the TV triangle inequality yields a_h D_3(p_0,t)+b_h D_3(p_1,t)≥min(a_h,b_h)D_3(p_0,p_1), with equality ONLY at the majority-source rate because a_h≠b_h. Thus t^MAP is unique, and T(t_n)→T_* forces t_n→t^MAP.

At a branch with a>b and t^MAP=p_0, a small positive displacement δ toward p_1 has D_3(p_0,p_0+δ)=(27/16)δ+O(δ²) and D_3(p_1,p_0+δ)=11/16-(9/8)δ+O(δ²). Its joint cost slope is (27a-18b)/4096 for the integer-over-256 weights; the away-direction cost slope is the strictly larger (27a+18b)/4096. For a branch with b>a and MAP=p_1 the bit-reflected formulas hold. The minimum toward slope over all 8 h is 117/4096, attained only at h=100 and 011; h=000 and 111 have 1683/4096. Hence in a small MAP neighborhood T-T_*≥c ||t-MAP||_1 with c>0, and all one-sided expansions have O(||t-MAP||²) remainder.

At MAP the two middle public G fibers 01 and 10 have TV zero and cannot decrease P. At G=00 the strict binomial residual signs are (+,+,-,-); the first-order public *decrease* from its two rates is (9/32)(t_000-1/4)+(9/128)(t_100-1/4). At reflected G=11 it is (9/128)(3/4-t_011)+(9/32)(3/4-t_111). All other terms are nonnegative public errors or quadratic remainders. A wrong-signed displacement has nonpositive public-decrease contribution, so dropping it only enlarges the decrease bound.

Compare the positive direction coefficients with λ=13/32. For h=100/011, joint slope 117/4096 = λ(9/128); for h=000/111, joint slope 1683/4096 > λ(9/32). All remaining directions have nonnegative joint cost. Thus for some C, locally

T(t)-T_* ≥ λ(P_0-P(t)) - C||t-MAP||_1².     (1)

A feasible matching construction changes only h=100 from p_0 to p_0+u. The exact polynomial calculation below gives P=P_0+f(u), T=T_*+g(u), where -f'(0)=9/128 and g'(0)=117/4096. For sufficiently small ε>0, the inverse -f(u)=ε gives F(P_0-ε)-T_*≤λε+O(ε²). Any minimizer t_ε consequently satisfies T(t_ε)→T_*, hence t_ε→MAP by uniqueness. Positive local linear growth gives ||t_ε-MAP||_1=O(ε); substitute in (1) and use P(t_ε)≤P_0-ε to get F(P_0-ε)-T_*≥λε-O(ε²). Matching upper/lower limits yield 13/32. QED.

This is an endpoint tangent, not a claim that the entire global curve equals a one-fiber candidate.

## Theorem 308B.2 — strict dominance of a mirrored split within two outer fibers

Restrict to t_100=p_0+u, t_011=p_1-v and the other six rates MAP, with u,v≥0 and u+v≤1/50. Let A(z)=1-3z²+2z³=Pr_{Bern(z)^⊗3}(K≤1). Over z∈[1/4,27/100], b_0 decreases, b_1,b_2,b_3 increase, and the exact G=00 public residual signs remain (+,+,-,-) (check b_0 and b_2,b_3 at z=27/100, b_1 at z=1/4). Bit reflection gives G=11. The source-conditional TV sign partitions also remain fixed.

The resulting identities on this ENTIRE real interval are

P(u,v)=P_0+f(u)+f(v),  T(u,v)=T_*+g(u)+g(v),
f(z)=-9z/128-3z²/32+z³/8,
g(z)=117z/4096-123z²/1024+23z³/256.

Indeed, f(z)=[A(1/4+z)-A(1/4)]/16, and the h=100 joint increment is g(z)=[9(27/64-(3/4-z)^3)+7(A(1/4+z)-A(1/4))]/256; expansion gives the displayed cubics. Hence, whenever u,v>0 and u+v≤1/50,

P(u,v)-P(u+v,0)=(3uv/16)[1-2(u+v)]>0,
T(u,v)-T(u+v,0)=(uv/512)[123-138(u+v)]>0.

Both identities follow by expanding the cubic powers, with strictly positive rational brackets throughout the declared interval. The concentrated strategy (u+v,0) strictly Pareto dominates the split (u,v), even under the entire allowed adaptive H/F policy class because all-F is worst. A mirrored u=v split is thus NOT automatically Pareto efficient.

Exact all-rational witness: split u=v=1/100 produces (P,T)=(5193/125000,9695073/128000000); concentrated (1/50,0) yields (20763/500000,9692067/128000000); exact gains are 9/500000 and 1503/64000000, respectively. The claim is about this explicitly restricted two-fiber family; it does NOT establish that concentrating is globally Pareto-optimal among all eight rates or locate the next global breakpoint.

## Checks, BRC reuse, and open obligation

The actual executed Fraction proof-check program REPRO_STAGE308B.py rebuilds 8 positive source/label fibers, exact public and joint 3-F outputs, polynomial identities, rational sign/derivative inequalities and the witness; VERIFY_STAGE308B.py independently regenerates conditional source masses and enumerates every length-three binary word. Their actual outputs end STAGE308B_SHARP_ENDPOINT_AND_SYMMETRY_BREAKING_EXACT_PASS and INDEPENDENT_BRC_SOURCE_GENERATION_AND_THREE_BIT_WORDS_PASS. Finite tests are cross-checks; the continuum argument is in the two proofs above.

BRC REUSE_APPLIED: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json blob f375a059fa4af8c6eefaddb4d4a8689a0c063674, positive rational source/J/G branch accumulation with provenance and public-vs-joint observer scopes retained. P000 native X6 path/triadic closure/independent time/registered Cell-address correspondence remains unproved and independent.

Next Stage309-B: prove or refute that for a rational δ>0 the full F(p) actually equals the concentrated one-fiber cubic parameterization on [P_0-δ,P_0], with complete active-set or semialgebraic exclusion of all other coordinates; otherwise exhibit an exact rational improving 8-rate counterexample. Then locate the first sharp transition and continue the full Pareto frontier.
