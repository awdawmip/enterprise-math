# EC49FCH — 1,092 exact five-slot rigidity certificates (native signed X6 / BRC)

Date: 2026-11-06. Status: author-side exact finite result; independent Driver mathematical review pending. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Predecessor: EC49FCG at `a0b1ffb95a4378b5c0f4f30b0b079568009cf11f`.

## Theorem (exact finite domain)

Keep the EC49FBU 24-word, 158-edge witness; the two fixed H2/H3 roots; the nine-state DFA and terminal observation signatures; each slot's horizon length; native ordered signed six-axis primitive steps; and complete positive BRC keys L=(4,2,1,0,0,0) for H4–H5 and M=(7,3,2,0,0,0) for H6–H9. A legal replacement is enumerated by the published `EC49FCF_EARLY1_LATE3_150/frozen_model.py`.

Write E for the ten H4–H6 observation slots and J for the four H7 slots. For **each** five-slot subset S of either form (i) S subset E, |S|=5, or (ii) |S∩E|=4 and |S∩J|=1, the exact minimum number of distinct **nonempty ordered signed-native primitive prefixes** after simultaneously replacing all slots of S is **158**. There are C(10,5)=252 cases of form (i) and C(10,4)*4=840 of form (ii), totaling 1,092 disjoint five-slot neighborhoods.

## Soundness and completeness proof

For each fixed subset S, let F be the union of prefixes from the 19 unchanged original paths, and P(w) be the signed primitive-prefix set of legal word w. The replacement cost equals

    |F| + | union_{s in S} (P(w_s) \ F) |.

The original paths attain 158. Put d=158-|F|. Any strict improvement requires the five residual sets to have union cardinality <d. Enumerate **every** legal candidate word at each chosen slot, map every distinct signed native prefix to a distinct bit, and form its residual bitmask with F removed. Discarding candidate residuals with cardinality >=d is exact. Deduplicating equal residual masks preserves all possible final costs. Sort slots by filtered pool size; this only reorders commutative set unions.

Let D0={0}, and recursively form

    D(k+1) = { u OR r : u in Dk, r in residual_pool(k+1), popcount(u OR r)<d }.

Inductively Dk contains every strict-improvement-capable partial union. The only pruning is the exact monotonic cardinality bound and exact equality of residual masks. Thus D5 is empty if and only if no legal five-tuple strictly improves 158. The executed checker obtained **D5 empty in all 1,092 cases**. The existing 158-edge witness supplies equality.

## Computed certificate

Exact runs: 252 early-five cases and five H7 slices of 160, 160, 160, 160 and 200 cases. All groups returned minimum 158. Aggregate hypothetical raw Cartesian products: **62,781,806,592** (not actual evaluated joins). Max number of retained subthreshold masks at an intermediate step: **2,028**. Elimination stages: 20 cases at k=3, 140 at k=4, 932 at k=5. `EC49FCH_SUMMARY.json` gives the machine-readable aggregate. The canonical sorted 1,092-row JSON certificate is reconstructible by running the six commands and concatenating the JSON `rows` arrays in lexical file-name order; its uncompressed SHA-256 is `e7fae35f0ff129efe2226af1c52a3d0e41c16a763696846067489a969ca96eb0`. All scripts use standard-library Python.

    python VERIFY_EC49FCH.py --family early_five
    python VERIFY_EC49FCH.py --family early4_h7 --start 0 --stop 160
    python VERIFY_EC49FCH.py --family early4_h7 --start 160 --stop 320
    python VERIFY_EC49FCH.py --family early4_h7 --start 320 --stop 480
    python VERIFY_EC49FCH.py --family early4_h7 --start 480 --stop 640
    python VERIFY_EC49FCH.py --family early4_h7 --start 640 --stop 840
    python CROSSCHECK_EC49FCH.py

An independent direct **signed primitive tuple-prefix** set implementation (without bit-indexing) checked 13 representative cases, also obtaining 158. The 13 checks are a separate sample; the full finite proof is the complete exhaustive bitset recurrence.

## Next unit EC49FCI

Extend the exact five-slot test to four early slots plus one H8/H9 slot, then mixed late-slot families; seek a 157-edge witness or extend the rigid neighborhood. Explore different positive BRC key schedules as a separate route toward the broader nine-window target. Preserve full signed primitive provenance and observer semantics. This result does not change P000 or claim independent mathematical admission.