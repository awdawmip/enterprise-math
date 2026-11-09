# BRC-X6: finite nine-bit trial family — 64 exact reducibility certificates (2026-11-10)

**Status:** AUTHOR EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED. This is a scoped negative result for 64 specified candidates, not a universal nine-bit impossibility claim.

**Scientific source:** SHA256 f42f2906d77f24085c123f3ccfe9667d41caa96d. Original 96 ports, six labeled actions, nine signed full seven-variable joint roots; native source ports (6,7,28,29), signs (+,-,-,+); exactly 38 legal deterministic policies and binary incidence C of shape 24x38.

The previously author-verified 10-bit D=1023, minSupport=13 positive result is at GitHub commit c7710f3a7fe4b6ddd7ce66af6df02ca95a275888.

## New finite exact result

With the same original 13-policy chart I=(2,8,15,21,24,28,29,31,37,0,1,3,5), check 64 distinct strictly-positive integer 13-weight vectors of total **D=511** (nine bits). One family fixes the first eight binary weights (1,2,4,8,16,32,64,128) and varies the last five; the other fixes the first seven (1,2,4,8,16,32,64) and varies the last six. The exact list of all tested weights is in the portable certificate archive.

For **each of the 64 vectors**, an explicitly recorded exact nonnegative rational representation using **at most 12 original legal policies** reproduces all 24 source-action coordinates of the proposed 13-term distribution. The exact alternative support counts are **1 candidate with 10 policies, 36 with 11, and 27 with 12**. Mixed-integer optimization was used only to propose alternative active policy IDs. For each case a separate SymPy exact-rational reconstruction verifies all weights are nonnegative and that C * alternative_coefficients = C[:,I] * candidate_weight_vector. The original 38 policies were also rebuilt and verified over all nine roots.

The reproducible archive contains the complete list of 64 proposed weight vectors, every exact alternative policy set and rational coefficient, a new exact native verifier, the frozen native kernel and reproduction instructions. It was rechecked from a clean extraction. Archive SHA256 **5d5cea0b9a955338642fa3d9d967cd89f3c3f49039c32ab9f90d90c9b350429d**. JSON exact certificate SHA256 **1e4bc5001645e113ac32b4cde3e7adcfadcd6046b14283ac1e13aaecf005e0e2**.

This establishes finite reducibility for these particular 64 nine-bit proposals. It leaves other nine-bit strategies and other 13-policy charts open; a modified parameter construction or a quantified family obstruction is the next scientific question. Author-independent review and canonical task admission remain pending.

The separate canonical D25/H0-B0 Source frontier, live owner/CLAIM and authentic historical UR V2 94,687-byte bundle target SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 are unchanged. No Source Task Result/Review is asserted.
