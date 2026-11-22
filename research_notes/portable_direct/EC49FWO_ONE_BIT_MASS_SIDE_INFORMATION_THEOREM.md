# EC49FWO supplement — One half-density bit is sufficient and worst-case necessary

**Date:** 2026-11-22 (Asia/Shanghai). **Depends on:** EC49FWO mass-augmented CRT inverse in this branch; same frozen BRC16943, auxiliary static CRT scope. **Status:** AUTHOR_PROVED / EXACT_INTEGER_EXAMPLES / PARENT_DEPENDENT / NOT_REVIEWED.

## Sharp theorem

Let n,q be known positive coprime moduli, q odd, M=nq, and let the unknown nonempty support W=U×V with nonempty U⊆Z/n and V⊆Z/q. The complete **indexed** reflection-defect array Δ_W(a,b) **plus just one global Boolean observation**

H(W)=1 if 2|W|>M, and 0 otherwise,

uniquely determines both factor cardinalities, the entire odd-factor positional support V (and its unknown hole count and exact hole locations), and the shorter-factor self-convolution K_U and defect spectrum Δ_U.

The one-bit side observation is **worst-case optimal** among deterministic additional binary/no-information observers over this model family when n>=1 and q>=3 odd: the defect array alone admits different valid products with distinct V.

## Proof

Write s=|W|. Counting ordered pairs of W according to their sum over the full group G=Z/M gives Σ_c K_W(c)=s², while Δ_W(c)=2(s−K_W(c)). Hence

Σ_c Δ_W(c)=2s(M−s).

The observed quantity D=Σ_c Δ_W(c) yields the exact integer discriminant

M²−2D=(M−2s)².

Thus the two algebraic candidate masses are

s_−=(M−√(M²−2D))/2,    s_+=(M+√(M²−2D))/2.

The bit H selects s_− when H=0, and s_+ when H=1; at equality they coincide and either convention returns s=M/2. Consequently s is recovered **exactly by integer arithmetic**, and the EC49FWO theorem recovers the stated factor data.

For the lower bound, choose U=Z/n and a proper nonempty V⊊Z/q with |V| ≠ q/2 (automatic when q is odd). W=U×V and W'=U×(Z/q\V) are complementary supports, yet both are admissible nonempty products. Complementation preserves every indexed reflection defect Δ_W=Δ_W', while V≠V'. They cannot be distinguished from Δ alone. Therefore zero extra bits do not suffice uniformly; the exhibited half-density bit achieves one. QED.

## Exact witness and crosscheck

Take n=10, q=11, U=Z/10 and V={2,7}. The complements W and W' have respectively s=20 and s'=90, with identical indexed Δ arrays and identical total defect sum D=3,600. The discriminant is 110²−2·3,600=4,900=70², giving unordered masses {20,90}. Their half-density bits are 0 and 1, so they are separated.

For U={0,1,2,3,4} and V=Z/11\{1,2,3}, s=40 and D=5,600, yielding candidate masses {40,70}; H=0 selects 40. All counts were checked by exact integer recomputation alongside the parent Python verifier.

## Scope and next question

This is a sharp **one-bit global side-information** result for the complete indexed static defect observer and fixed product-model factorization. It does not establish that a single *local position probe* suffices or that this compression is preserved by a native time update. An informative next problem is to characterize the minimum fixed **local** probes replacing H, and to bind the resulting observer to the actual frozen moving-Farey update and its admissible future operations. Original even-factor U membership ambiguity persists.
