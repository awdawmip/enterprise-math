# N-coupled G_poly-loc: general-modulus support and idempotent audit

Status: DRIVER SCIENTIFIC AUDIT / SUPPLEMENTAL THEOREMS / NOT NATIVE RESULT ACCEPTANCE
Date: 2026-11-13
Driver lane: EM-DVR-DEBB5E / CONTROL_PLANE
Original scientific author: EM-NCAS1-5F7A3C; Gen2 integrity refreeze author: EM-NCASR2-C9BCF9
Original Result: RR-13ED25CE1AA8899BCFEC (Task RS-N-COUPLED-ASYMMETRIC-SINGULARIZATION-PRIMITIVE, publication TP2-7D97568CBD5F6DE776A3)
Original frozen Source: awdawmip/enterprise-math@3e5b9420910ffc9624f485145c162fb725f4f53d
Original return: research_returns/N_COUPLED_ASYMMETRIC_SINGULARIZATION_PRIMITIVE_RETURN_20260830.md
Frozen Result SHA256: aee5a3398d30b198db14acda0c1528e4a68a8e04a4173a482151e82e8efa43cf

## 1. The exact scope being audited

Keep the original *fixed finite-step, fixed-dimensional* grammar G_poly-loc. Matrix/tensor entries arise from fixed integer constants, the public integer N, polynomial/ring operations, contractions and fixed rational denominators that are units modulo N. Initialization must also be generated in that grammar (for example the constant identity matrix), not supplied by an arbitrary outside N-dependent oracle or integer-representative procedure. There is no adaptive branching on gcd/rank/nonunit outcomes and no N-dependent loop count.

For every generated observable A(N), the structural-induction N-erasure theorem gives A(N) = A(0) modulo N, interpreting fixed denominators as invertible classes. It is this base-case condition that supports the induction; arbitrary externally supplied initial matrices are outside the assertion.

This audit retains the original distinction between *unlabeled asymmetric channel behavior* and the stronger problem of constructing a hidden factor selector.

## 2. Determinantal support at a general modulus

**Theorem A (rank-drop prime support).** Let N >= 2 be any integer, with admissible fixed denominators coprime to N. Let A(N) be a generated m-by-n matrix observable. Clear a common fixed denominator d with gcd(d,N)=1, and set B=d A(0), an integer matrix. If k=rank_Q(B)>0, let

    Delta_k(B) = gcd( |det B[I,J]| : |I|=|J|=k ) > 0.

For every prime p dividing N,

    rank_{F_p}(A(N) mod p) < k    iff    p | Delta_k(B).

Indeed A(N) mod p is (d inverse mod p) times B mod p. A scalar unit leaves rank invariant; all (k+1)-minors of B vanish integrally, and its k-minors all vanish modulo p exactly when p divides their gcd. If k=0, all channel ranks equal zero.

Write N = product p^{e_p}. Then

    gcd(N,Delta_k(B)) = product over p|N of p^{min(e_p,v_p(Delta_k(B)))}.

Consequently, if one hidden prime channel has rank below k while another has rank k, this *ordinary scalar gcd* lies strictly between 1 and N. In particular, no mixed prime-channel rank-drop pattern produced by this grammar hides all nontrivial factors from gcd.

**Squarefree exactness.** If N is squarefree, this gcd is exactly the product of the prime factors whose channels drop rank. For N=pq, this recovers the frozen theorem's exact singular-side factor. For nonsquarefree N, the gcd reports the correct prime support but not necessarily the complete prime-power component.

This extension is a statement about reduction ranks and integer minors. It does not assume rank over Z/p^e Z behaves as rank over a field, and does not claim an integer-factorization complexity lower bound.

## 3. General complementary factor readout from an idempotent

**Theorem B (all composite moduli).** For any N>=2, let d be coprime to N, and suppose b=a*d^{-1} mod N is an idempotent, b^2=b mod N. Define

    u=gcd(N,a),    v=gcd(N,a-d).

Then u*v=N and gcd(u,v)=1. Moreover b is neither 0 nor 1 modulo N if and only if both u and v are greater than 1. Thus any nontrivial fixed-grammar idempotent already exhibits an explicit proper coprime factorization, at any modulus.

*Proof.* For each prime power p^e exactly dividing N, b(b-1)=0 mod p^e; since gcd(b,b-1)=1 in integers, p^e divides precisely one of b or b-1. Because d is a unit, p^e divides precisely one of a or a-d. It cannot divide both because p does not divide d. Therefore the full prime-power components partition between gcd(N,a) and gcd(N,a-d), giving the product and coprimality. Both are nontrivial exactly when b takes both CRT values 0 and 1 on distinct prime-power components.

For N=pq, the two factors are p and q in some order, as in the original frozen Result. No assumption about knowing the hidden prime labels is required.

## 4. Independent finite regression of the original envelope

An independent exact-integer enumeration was run for all 7^4=2,401 integer 2-by-2 matrices with entries in [-3,3], the original eight affine N-coefficient templates, and all 28 products of two distinct primes in (3,5,7,11,13,17,19,23). Its 537,824 semiprime/template checks agree with the original certificate. It found the same rank distribution [1,288,2112] for ranks [0,1,2], the same 72,960 one-sided support cases, and zero mismatches in the gcd criterion. Independent direct enumeration of c in [-100,100] gives 170 nontrivial idempotent cases and zero mismatches in complementary gcd endpoints.

This finite regression checks a bounded exact arithmetic family. Theorems A and B are established by the preceding proofs, not inferred from this enumeration. The original researcher's checker and certificate remain immutable, with their actual source authorship preserved.

## 5. Review and authority status

This note provides a Driver-owned supplemental derivation and a scope audit. It neither changes original Result bytes nor substitutes for native independent acceptance. The historical review DR-5A1D83F27C4E906B2F71 is retained as exact historical evidence; current operational review state is separately subject to Source authority. The current Driver has consulted the original proof, Result, and earlier summaries, so this work has **shared control context** and makes no assertion of a clean independent review.

The original semiprime G_poly-loc obstruction and its surviving frontier CRT_PRODUCT_NATURALITY_BREAK_WITHOUT_SCALAR_SUPPORT_EXPOSURE are retained. No new Task publication, CLAIM, Result acceptance, Working Truth, Foundation, or parent objective closure is asserted.
