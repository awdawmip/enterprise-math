# R5 — Multi-origin stop-loss dispersion theorem for a single LR collision

Scientific date: 2026-10-29 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Finite two-law auxiliary model, not a native X6/physical result or a claim of external novelty.

## Frozen provenance and authority

GLOBAL_KNOWLEDGE_V1 current canonical main **74a2ab5dbd65b9cd134e7e1a4071cbbd93fb8b89**. Project main **65839914830d41264c1e3f34faeef31504f72321**. Read both canonical entry files, P000 original and startup projection (blob **770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc** matches), ACTIVE worldview, current portable research protocol, BRC and mathematics/code/activity policies. Latest R5 input: the signed-hull proof on Draft PR #1663, commit **47cf2b7a86b7f0c23c4b13d8cc31179907ed78bd**, especially research_notes/brc_r5_all_signed_hull_cert_20261029_t0536/RESEARCH.md.

Native gateway on this run: research_authority_granted=false; active jobs 5/5; owner inventory attempt produced CONTROL_QUOTA. **No authenticated active owner, CLAIM, native Result or independent Driver review obtained.** This is independent portable author research in the existing PR and does not modify the protected worldview or taskbook.

## Model

Let m≥2 be finite. Origins i have strictly positive masses ρᵢ under each of P and Q, with Σρᵢ=1. At time 1 FULL sees i, whereas a seedless LR strategy sees only (time=1, likelihood ratio=1). Either may stop and declare P, stop and declare Q, or continue. At time 2 all histories stop after declaring P/Q. Conditional on continuing origin i, the terminal Q signature s runs over a finite ordered set S of distinct positive reals, with positive kernel qᵢ(s)>0, Σₛqᵢ(s)=1 and Σₛs qᵢ(s)=1. The conditional P kernel is exactly s qᵢ(s), making the terminal likelihood ratio s. FULL may remember i; LR can only use (time,s), and has **no persistent random seed**. Local behavior probabilities range over all real [0,1].

Observer: O=(e_P,e_Q,T_P,T_Q). Here e_P means P-probability of declaring Q, e_Q means Q-probability of declaring P, and T_P,T_Q are expected stopping times. For every signed coefficient vector w=(a,b,c,d)∈ℝ⁴ put h=c+d, Fᵢ(a,b)=Σₛqᵢ(s)min(as,b), and Dᵢ=h+Fᵢ(a,b)−min(a,b).

## Theorem 1: exact all-signed Bellman formula and complete one-collision classification — PROVED

For **every real signed** a,b,c,d and **every real** behavioral policy family,

~~~text
V_FULL(w) = min(a,b)+h + Σᵢρᵢ min(0,Dᵢ)
V_LR(w)   = min(a,b)+h + min(0,ΣᵢρᵢDᵢ)
Δ(w)      = V_LR−V_FULL
          = [Σᵢρᵢ|Dᵢ| − |ΣᵢρᵢDᵢ|]/2 ≥ 0.
~~~

The following are equivalent for this entire finite family: (i) conv(O_FULL)=conv(O_LR); (ii) **the actual real behavioral images O_FULL=O_LR**; (iii) qᵢ(s)=qⱼ(s) for every pair of origins and every signature.

**Proof of Bellman formulas.** A unit of P and Q source mass stopped at t=1 has scalar cost S₀=min(a,b)+h, because the two declarations have error costs a and b. After continuing, terminal signature s has best error cost min(as,b), independent of i since P/Q=s at s, and time cost 2h. Conditional continuation-minus-stop cost is Dᵢ. FULL chooses independently by i; LR must use one time-1 action distribution, so it compares the weighted mean D against zero. Both classes can optimize terminal declarations identically at each s for the scalar cost, even for signed coefficients. This proves both minima; the last equality uses min(0,x)=(x−|x|)/2. The argument optimizes arbitrary real behavioral coins, not a finite probability grid.

**Kernels unequal ⇒ convex hulls unequal.** For a positive threshold t define Cᵢ(t)=Σₛqᵢ(s)min(s,t) and C̄(t)=ΣᵢρᵢCᵢ(t). On intervals between successive signatures, the derivative of Cᵢ is Qᵢ(S>t), and its downward derivative jump at s is exactly qᵢ(s). Thus the full transform t↦Cᵢ(t) uniquely determines qᵢ. If any two kernels differ, choose t>0 where Cᵢ(t) are not all equal. Set (a,b)=(1,t), h=min(1,t)−C̄(t), c=h,d=0. Jensen for the concave map x↦min(x,t), using E_qᵢ s=1, yields **h≥0**. Now Dᵢ=Cᵢ(t)−C̄(t), the mean of D is zero and the displayed gap is
Δ=½Σᵢρᵢ|Cᵢ(t)−C̄(t)|>0.
This is a separating direction with **all coefficients nonnegative**. Therefore equality of all four-dimensional signed support functions forces identical kernels. Compactness of finite behavioral strategy images makes this a strict convex-hull separator.

**Kernels identical ⇒ equality of actual images.** Suppose qᵢ=q for every origin. For any FULL strategy, aggregate the P/Q/Q-conditional masses of the three time-1 actions across i. Initial P and Q origin distributions are both ρ, so one LR categorical coin at time 1 realizes those exact aggregate masses. For each terminal signature s, choose the LR declaration-P probability equal to the FULL aggregate continued Q mass declaring P at s divided by the total continued Q mass at s (arbitrary if zero). Identical q ensures that these weighted decisions preserve all Q terminal signature-declaration masses. Multiplication by s preserves the corresponding P masses. Thus the resulting *single genuine seedless LR behavioral policy* matches every stopping-time/signature/declaration joint mass under both laws, and therefore all four observers. The reverse inclusion follows since LR policies are FULL policies ignoring the origin. These constructions justify actual images rather than merely a convex mixture of deterministic LR plans. QED.

## Theorem 2: sharp information-loss coefficient and finite threshold certificate — PROVED

Fix (a,b)=(1,t) for t>0, and allow real h=c+d. Then

~~~text
max_{h∈ℝ} Δ(1,t,h,0) = ½Σᵢρᵢ|Cᵢ(t)−C̄(t)|,
and h*=min(1,t)−C̄(t)≥0 is an optimizer.

max_{t>0,h∈ℝ} Δ(1,t,h,0)
    = max_{t∈S} ½Σᵢρᵢ|Cᵢ(t)−C̄(t)|.
~~~

For rational input, the entire optimal loss is certified by finitely many exact rational operations and inequalities.

**Proof.** Write u=h+C̄(t)−min(1,t) and zᵢ=Cᵢ(t)−C̄(t), so Σρᵢzᵢ=0. For u≤0 the gap reduces to Σρᵢmax(0,u+zᵢ), nondecreasing in u; for u≥0 it reduces to Σρᵢmax(0,−u−zᵢ), nonincreasing in u. The maximum is at u=0 and equals half the weighted absolute deviation of the centered zᵢ. Between consecutive terminal signatures, every Cᵢ(t) is affine, making the sum of absolute centered values convex; its maximum on that interval occurs at an endpoint. For t≤min S all Cᵢ(t)=t; for t≥max S all Cᵢ(t)=E_i s=1. Both exterior gaps vanish. The finite breakpoint maximum follows. QED.

## Strictly positive rational 3-origin / 4-signature witness

Take ρ=(1/3,1/3,1/3), S=(1/2,3/4,5/4,3/2), and Q kernels

~~~text
q_A=(1/5,3/10,3/10,1/5)
q_B=(3/10,1/5,1/5,3/10)
q_C=(1/4,1/4,1/4,1/4).
~~~

Every entry is positive and every row has sum 1 and first moment Σs qᵢ(s)=1, so P kernels s qᵢ(s) are positive normalized rows. At t=1,

~~~text
(C_A,C_B,C_C)=(33/40,4/5,13/16);
C̄=13/16; h*=3/16;
D=(1/80,−1/80,0).
w=(1,1,3/16,0).
min_FULL(w·O)=71/60; min_LR(w·O)=19/16; gap=1/240.
~~~

FULL stops and declares Q on origins A,C at t=1; on B it continues and declares P at t=2 exactly when s>1. Its observer is

~~~text
v*=(23/30,1/6,4/3,4/3).
~~~

For **every real seedless LR strategy**, w·O≥19/16 while w·v*=71/60, implying

~~~text
||O−v*||∞ ≥ (1/240)/(1+1+3/16)=1/525.
~~~

The exact threshold certificate at S=(1/2,3/4,5/4,3/2) is respectively (0,1/240,1/240,0); the **global normalized positive-error-weight optimum over all real t>0 and h is 1/240**.

## Verification, BRC and research boundary

Actual execution: the accompanying Python Fraction verifier checks positivity, both probability-law normalizations, 18 LR deterministic plans and all 18³=5832 FULL deterministic plans for the displayed witness, 300 signed coefficient tuples against the independent Bellman calculation, all four finite breakpoints, and 5832 equal-kernel FULL plans against their LR-deterministic convex representation. The logged result is **PASS_EXACT_R5_MULTI_ORIGIN_STOP_LOSS**. These are arithmetic/regression checks; the theorems' quantifiers over all real behavior are supported by the analytical arguments.

BRC preserves source labels i and exact strictly positive Q/P branch masses ρᵢqᵢ(s), sρᵢqᵢ(s). Forgetting i can erase a genuine future-predictive residual; the transform exhibits a precise observer-relevant loss. Equal kernels instead furnish a proved **safe quotient under the declared future stop/declaration operations**, without pretending that LR is a complete universal state. No X6 native path embedding, physical calibration or BRC-Shor/heartbeat arithmetic experiment is established.

Related classical literature, not a novelty claim or a dependency of the proof: M. Ali Khan, H. Yu, Z. Zhang, *A simple proof of Blackwell's theorem on the comparison of experiments for a general state space*, Economics Letters 247 (2025), article 112146, DOI:10.1016/j.econlet.2024.112146. A constructive Blackwell exposition is available at https://python.quantecon.org/blackwell_kihlstrom.

**Next unresolved mother target:** Models with ≥2 interacting nonterminal LR decisions and origin-sensitive reconvergence. Use exact all-signed finite-deterministic convex hull LP witnesses on that class; only once a model passes full hull equality should a real semialgebraic nonmembership proof for a four-observer vector be attempted. Theorem 1 removes the entire one-collision/terminal family, not the mother question.
