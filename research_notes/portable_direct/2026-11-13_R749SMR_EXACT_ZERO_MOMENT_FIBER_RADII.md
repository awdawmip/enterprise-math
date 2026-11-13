# R749SMR — Exact zero-moment fiber Chebyshev radii of the exceptional five-circuit and its complement

Date: 2026-11-13 (Asia/Shanghai). Continuation of R749SMQ, PR #2233. Author-side proof and bounded exact enumeration; independent review pending. Scientific input: the frozen finite signed-source/Walsh model at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, unchanged. Four binary source bits are **not** native P000 spatial dimensions; no native V29/V39 event permission is asserted.

## Statement

Let G=F_2^4, χ_a(x)=(-1)^{a·x}, C={1,2,4,8,15}, and B=G\({0}∪C). Define the zero-moment fiber F_U(0)={p∈Δ(G): Σ_x p_x χ_a(x)=0 for all a∈U}. For the identity source observer, let r_U(0)=min_{q∈Δ(G)} max_{p∈F_U(0)} TV(q,p).

**Theorem.** r_C(0)=3/4 and r_B(0)=1/2. The uniform law u(x)=1/16 is a minimax center in both fibers. By GL(4,2) equivariance, this holds for all 168 five-circuits and their 168 complements identified in R749SMQ.

This evaluates the **single zero-moment fiber**. The global nonlinear risks R_U(I)=inf_D sup_p TV(D(m_U(p)),p), allowing all moment vectors, remain open.

## 1. Uniform center lemma

Translation T_h p(x)=p(x+h) preserves F_U(0), since m_a(T_h p)=χ_a(h)m_a(p)=0. For any center q, average its 16 translates, obtaining u. Convexity of TV in the center and invariance of the fiber imply sup_{p∈F_U(0)} TV(u,p)≤sup_{p∈F_U(0)} TV(q,p). Thus r_U(0)=max_{p∈F_U(0)} TV(u,p).

## 2. Five-circuit C

The sign map x↦(χ_a(x))_{a∈C} bijects G with the 16 length-five even-parity sign words. Their minus-sign counts are 0, 2 or 4. Every pair of distinct words shares a coordinate, since an antipodal pair is impossible in odd length with even parity.

Fix p∈F_C(0), any subset S⊂G, and m=p(S). For |S|=1, translate the chosen sign word to all +. Under p the expected number of negative signs is 5/2, while at most four negatives occur off S, giving 5/2≤4(1-m), hence m≤3/8.

For |S|=2, the two sign words share a sign coordinate; its total expectation vanishes, implying m≤1/2.

For |S|=3, denote the sign words v_1,v_2,v_3. If one sign coordinate is constant across the triple, then m≤1/2. Otherwise let n_j count sign coordinates where v_j is the unique minority. The Hamming distances of each pair are n_i+n_j, all even; therefore n_1,n_2,n_3 have the same parity. There are five coordinates and no all-equal column, so their sum is 5. Hence they are all positive odd integers. With conditional masses w_1+w_2+w_3=1, choose j with w_j≤1/3 and a coordinate where j is the minority. Its absolute conditional sign average is |1-2w_j|≥1/3. Since the unconditional sign average is zero and the complement has mass 1-m, m/3≤1-m and m≤3/4.

Now TV(p,u)=max_{S⊆G}[p(S)-|S|/16]. Subsets of sizes 0,1,2,3 contribute at most 0,5/16,3/8,9/16. Every S of size≥4 contributes at most 1-4/16=3/4. Therefore TV(p,u)≤3/4.

For equality take H={0,7,8,15}, a two-dimensional binary subspace with H^⊥={0,3,5,6} disjoint from C. The uniform p_H on H has m_C(p_H)=0 and TV(p_H,u)=1-4/16=3/4.

## 3. Ten-character complement B

Fourier inversion says p∈F_B(0) iff p_x=(1+Σ_{i=1}^5 c_i χ_{a_i}(x))/16, (a_i)=C, for c in the bounded polytope P={c∈R^5:1+v·c≥0 for all 16 even-parity sign words v}.

**Finite vertex lemma.** The vertices of P are precisely the ten vectors ±e_i and the sixteen vectors v/3, with v any even-parity sign word.

Here is an exhaustive rational certificate for this *finite* assertion. Every vertex of this bounded full-dimensional five-variable polytope has five linearly independent active facet equations. Enumerate all binom(16,5)=4368 sets of five facets, solve the nonsingular systems v_j·c=-1 by exact Fraction Gaussian elimination, check all 16 inequalities, and deduplicate. The attached standalone checker returns exactly 26 feasible vertices: the displayed ten ±e_i and sixteen v/3. Its observed enumeration has 1360 singular five-facet bases and 336 feasible nonsingular bases. All listed candidates are indeed feasible with independent active facets. Thus no other vertices exist.

For ±e_i the corresponding source law is uniform on an eight-point parity hyperplane, giving TV(p,u)=1/2. For c=v/3, the law has one atom 1/6, ten atoms 1/12, and five zero atoms, giving TV(p,u)=5/16. Since TV(·,u) is convex and every p in the fiber is a convex combination of the 26 vertex laws, the maximum is 1/2, attained at ±e_i.

## 4. Verification, scope and next question

Companion files: R749SMR_ZERO_MOMENT_CIRCUIT_CHECK.py and R749SMR_ZERO_MOMENT_RESULTS.json. Standard-library exact integers and fractions, all 120 sign pairs, all 560 triples, all 4368 facet bases, 16 positivity inequalities per candidate, and exact vertex TV classification; local run PASS.

This resolves the zero-moment Chebyshev radii only. The global bounds from R749SMQ remain 3/4≤R_C(I)≤5/6 and 1/2≤R_B(I)≤5/8. Next: construct a decoder attaining the zero-fiber bound uniformly over **every** nonzero moment vector, or exhibit an exact nonzero fiber with greater radius. Later native X6 Cell/Link/Port attribution requires actual event licensing, preserving joint provenance.
