# Lowest-bit lift: shared-context symbolic review

Status: `PASS_SYMBOLIC_REVIEW_NO_SUBSTANTIVE_FINDING`. Reviewed `LSB_LIFT.md`, SHA-256 `98006fbb6256355fcc1b34ae6ec5e7ef13f1b0df00c40b272128d7f1de6574bf`. No implementation or numerical experiment was run. This is a shared-context review, not independent admission or a novelty claim.

For every ordered pair, multiplying both real weights by their lowest-bit signs multiplies the pair product by `(-1)^(x+y)=(-1)^(y-x)`. If `R` is even, every integer displacement congruent to `r` has parity `r`, giving the claimed single-query factor. If `R` is odd, the class modulo `R` is the disjoint union of classes `r` and `r+R` modulo `2R`; these have opposite parity. The claimed signed difference of two queries follows term by term. Negative displacements need no extra orientation convention or factor of two.

The two odd-modulus residues are canonical because `0<=r<R`. This also covers `r=0` and `R=1`; there is no division by, or inversion of, a group element. Empty classes and finite intervals of arbitrary length cause no problem. The interval and ordered-pair domain stay unchanged, so the raw `4^-g` factor in the bit-gap application is unchanged. For `k=0`, the repeated sign cancels to the unsigned query; for `k>=1`, the new mask has exactly the two distinct negative bits `{0,k}`.

Replacing a supplied counting modulus by `2R` is legal for the scalar observer. It neither identifies a new multiplicative order nor pays for an unknown target address. The conditional cost statement is correct: one or two underlying queries and one extra modulus bit preserve a polynomial public-bit-length bound if the underlying routine already has that bound. This does not establish a general Walsh-mask result or an empirical speedup.

The fixed-weight qualification is essential and is present in the proof. Changing a semiclassical history bit can also change later native matrices; this scalar identity does not justify holding those induced matrices fixed in an actual program without a separate operator/carry contract. A future implementation must retain typed parity, doubled modulus, both odd-branch query receipts, and the outer signed subtraction/multiplication, with a fresh verifier. The existing 31 single-bit results are not execution evidence for the new two-bit family.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
