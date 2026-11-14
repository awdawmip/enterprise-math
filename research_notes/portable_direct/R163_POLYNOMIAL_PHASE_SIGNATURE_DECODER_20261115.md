# R163 — Polynomial-time exact inversion of finite-Sturmian phase signatures

Date: 2026-11-15 Asia/Shanghai. Status: AUTHOR_PROVED / NOT_REVIEWED.
Scope: external finite-Sturmian tied-phase scalar observer; unchanged frozen scientific input pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Builds on R162, immutable proof commit f451da2665923179eed166c488a1e8063222ca29. This is an external scalar coding result, not native X6 or a formal Result/Review.

## 1. Inversion theorem

Fix m>=1. For a reduced rational signature s=(alpha,beta,U,V) in the image of the finite-Sturmian word map S_m, write alpha=a/b, beta=c/d (b,d>0), A=U/b-1, B=V/d. Define

Delta=beta-alpha>0,
x0=1+A=U/b,
t=(B-x0)/Delta.

**Theorem R163 (exact quadratic-arithmetic decoder).** All admitted words w of length m with S_m(w)=s can be computed in O(m^2) exact rational arithmetic operations without enumerating the 2^m binary strings. The decoder constructs at most two candidate words from a one-sided infinitesimal floor rule and verifies their exact signatures. Its output is precisely the full preimage S_m^{-1}(s), including all endpoint and constant-word cases. On valid inputs, the number of candidates is at most two. R162 proves that one extra bit can distinguish the candidates when both survive; this algorithm constructs them explicitly.

For every prefix index i=0,...,m, let z_i=x0+i*alpha and v_i=t+i. The decoder chooses the prefix p_i using:

- If z_i is nonintegral, p_i=floor(z_i).
- If z_i is integral and v_i>0, p_i=z_i.
- If z_i is integral and v_i<0, p_i=z_i-1.
- If z_i is integral and v_i=0, p_i may be z_i-1 or z_i.

The last case can occur for at most one i since v_i=t+i=0 is injective in i. For each of the at most two resulting prefix vectors, require p_0=0 and p_i-p_{i-1} in {0,1} for i=1,...,m; then recompute the exact reduced signature and retain the word iff it matches s. This is an explicit nonexponential decoder. When the ambiguous index is j, t=-j and z_j=(U+ja)/b is an integer, refining the necessary collision test of R162.

## 2. Proof

Take an admitted preimage w of s. By R162 the entire chord from (alpha,1+A) to (beta,B) lies in its closed floor-feasibility polygon; it has parameterization x(theta)=x0+t(theta-alpha).

Choose theta=alpha+epsilon with epsilon>0 sufficiently small. For each fixed prefix i the chord evaluation is

x(theta)+i*theta=z_i+(t+i)*epsilon=z_i+v_i*epsilon.

If z_i is nonintegral, this number stays in its original open unit interval for small epsilon, giving p_i=floor(z_i). If z_i is integral and v_i>0, its right-hand value is just above the integer, so p_i=z_i. If v_i<0, it lies just below the integer and p_i=z_i-1. If both integrality and v_i=0 hold, the chord lies exactly on the integer boundary for index i, and the closed coding constraints permit exactly the two integers z_i-1 and z_i. Because the set of indices is finite, one common positive epsilon can be chosen to make all these statements hold simultaneously.

Thus the true prefix vector of EVERY preimage is among the decoder's at most two candidates. Prefix differences recover the binary word. Conversely, each returned candidate is explicitly checked by the exact original signature map, so all outputs are admitted words of signature s. That proves soundness and completeness.

To compute the signature of an m-bit candidate, inspect the O(m^2) contiguous factors and their exact reduced rational inequalities, then the O(m) prefix cuts U,V; only two candidates are tested. The arithmetic-operation count is therefore O(m^2); bit complexity is polynomial in m and the input rational encoding length. No floating-point operations or exponential word scan are needed.

The all-length proof does not require that the rational input s actually be valid. If s is invalid, the same finite candidate-generation plus signature tests returns an empty list.

## 3. Reproducible exact check

R163_decoder_check.py independently computes all binary words for lengths m=1..15, groups admitted words by the exact (alpha,beta,U,V) signature, and verifies that this polynomial decoder returns exactly each group, including singleton and doubleton classes. The complete finite test covers 65,534 binary candidates, 1,760 distinct signatures, and all observed two-word fibers. It uses Python Fraction and integer arithmetic, with no floating point. The reproducible marker is R163_EXACT_DECODER_PASS. R163_verification.json records the per-length results.

The complete test is a finite corroboration; the symbolic chord and one-sided-floor argument proves the decoder for every m.

## 4. Research implications and next problem

R162's one-bit loss bound is now constructive: a finite-Sturmian exact signature can be inverted using O(m^2) arithmetic and at most one orientation bit if the fiber has two words. The expensive search of 2^m candidates is unnecessary. The resulting minimal repair is scoped to the fixed-length word-identity observer; a future BRC operation can discard additional coordinates only after its actual future-operation preservation law is proven.

Remaining: seek a direct signature-only criterion for a two-word fiber that avoids even the two candidate signature recomputations, and test how the one-bit repair propagates under word concatenation and BRC port composition. Separate native-X6 embeddings require explicit typed construction.
