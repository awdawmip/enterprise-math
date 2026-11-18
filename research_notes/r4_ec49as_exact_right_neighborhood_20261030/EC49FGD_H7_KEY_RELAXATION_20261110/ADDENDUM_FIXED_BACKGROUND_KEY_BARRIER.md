# EC49FGD addendum — sharp fixed-background five-key barrier

Date: 2026-11-10. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Author-side exact finite deduction from the already-published 34-key table and independently checked 24-word witness.

## Statement

Keep the **20 original-mother H2/H3/H4/H5/H6/H8/H9 words fixed** as displayed in `README_EC49FGD.md`. Let B be their ordered signed-six-axis microstep-prefix union, `|B|=89`.

These 20 words use the following **six distinct raw full-key triples**, all with the remaining three positive-axis counts zero:

```text
(2,1,1)   H2:ge
(3,0,1)   H2:fe  [not strictly positive: second component 0]
(3,1,1)   H3:feg,gef
(4,2,1)   H4,H5
(5,3,1)   H6
(6,4,1)   H8,H9
```

**Corollary A (count all distinct raw complete keys):** Every full 24-label completion keeping this B has at least six raw complete keys, irrespective of the four H7 word choices. Hence no such fixed-background completion can satisfy a budget of **at most five raw complete keys**.

**Corollary B (count only strictly positive full keys):** The background B already occupies five strictly positive keys, namely `(2,1,1),(3,1,1),(4,2,1),(5,3,1),(6,4,1)`. Under a budget of at most five **strictly positive** keys, every H7 word must use one of these existing keys. The necessary exact count law `r=c+d=x+y-8` gives, for the five keys in order, `r=-5,-4,-2,0,2`. Each H7 low signature 1,2,4,8 requires at least one `c` or `d` operation in the original nine-state DFA; thus only `K=(6,4,1)` can realize low labels among the existing keys. The already-published exhaustive H7 fixed-background calculation at this key (1260 legal low-signature words) gives **exactly 15 fresh primitive prefixes**. Consequently:

```text
min cost for this B with no new strictly-positive H7 key = 89+15 = 104.
```

A legal 104-edge witness with K7=(6,4,1) is shown in EC49FGC `ADDENDUM_ORIGINAL_H7_FIXED_104.md`.

Thus within this **precise fixed-background family**, reaching the 93-prefix construction of the main EC49FGD paper necessarily requires **changing the background words and/or changing its full-key allocation** to restore the five-key constraint. This is a scoped obstruction, not a no-go result for the original unrestricted mother objective.

## Independent check relation

Using `CHECK_WITNESS_EC49FGD.py`, exclude the four H7 words and compute distinct `key(w)` for the 20 background words, both including all keys and filtering `min(key)>0`. Verify sets listed above. Using `VERIFY_EC49FGD.py` or `EXACT_MATRIX_EC49FGD.json`, read the row K=(6,4,1) → `pool_total=1260, extra=15, total=104`. All statements are exact signed-native/observer-local computations.

Researcher: `EM-DIRECT-E7770A`; native activity `RA-118B1A402E7E8240CC10EF43`. This addendum is author-side evidence pending formal Driver review, without CLAIM.
