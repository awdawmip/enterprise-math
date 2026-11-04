# PREFIX-492 — Intermediate KMP q=1,2 and exact BRC source-fiber theorems

Date: 2026-11-04 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Prior proof: PREFIX-491, research_notes/portable_direct/2026-11-04_prefix491_full_kmp_suffix_shift_universality.md. Current normative rules independently loaded from canonical main.

## Exact observer and scope

This is a declared restricted observer in P000's six-axis Heartbeat World, with the sixth special-axis usage fixed at zero and the ten ordinary signed symbols a/A,b/B,c/C,d/D,e/E retained. No lower-dimensional native geometry is introduced. All ordered words are legal; there is no pattern avoidance. For signed occupancy u_i,v_i, let y_i=u_i-v_i, p_i=min(u_i,v_i), n=sum_i(u_i+v_i), V=p_b+2p_d+p_e, W=p_c+p_e. Count **distinct** fibers (n,y,V,W,q_g), not ordered words. KMP state q_g is the longest suffix equal to a prefix of gate g, including q_g=3 for full matches. The fiber's source mask records attainable N (no b/B/c/C yet), B (first b/B), C (first c/C).

From PREFIX-491, define

    H(z)=(1+z)^2(1+2z^2)/(1-z)^8.

For any fixed signed suffix of length L, the generating function for distinct (n,y,V,W) fibers admitting that terminal suffix is z^L H(z). PREFIX-491 proves this by a translated integer cancellation polygon.

## Theorem A — q=2 equality of totals, infinite source distinction

For g=aab, q_g=2 is equivalent to ending in "aa". For g=aba, q_g=2 is equivalent to ending in "ab". Neither ending can also be a full length-3 match. Consequently, for every n>=0,

    F_{aab,2}(z)=F_{aba,2}(z)=z^2 H(z).

However the number of q=2 fibers **admitting source tag N** is

    N_{aab,2}(z)=z^2/(1-z)^6,
    N_{aba,2}(z)=0.

Proof. A word ending aa has source N exactly when b/B/c/C do not occur. Only a,d,e axes remain, with independent signed displacements and cancellation counts p_a+p_d+p_e=m. At fixed m, (V,W)=(2p_d+p_e,p_e) determines the triple uniquely, giving binomial(m+2,2) possible values. Reserving suffix aa shifts the a occupancy by two; the three displacement series multiply to ((1+z)/(1-z))^3 and the cancellation series is (1-z^2)^(-3). Thus z^2 ((1+z)/(1-z))^3 (1-z^2)^(-3)=z^2/(1-z)^6. For gate aba the q=2 suffix ab already introduces source B, so N never occurs. For n>=2, the first count is binomial(n+3,5). QED.

## Theorem B — q=1 exact difference and pointwise mask comparison

For aab, q=1 precisely when the word ends in a, but not aa; this is possible for every occupancy with at least one a and at least one non-a, plus the singleton a. For aba, q=1 precisely when the word ends in a but not aba; every occupancy with at least one a admits such an ordering. Hence for all n>=0,

    F_{aba,1}(z)=z H(z),
    F_{aab,1}(z)=z H(z)-z^2/(1-z).

In fact, the q=1 source masks at each fixed (n,y,V,W) coincide except on the unique all-a fiber a^n for each n>=2; this fiber supports N for aba q=1 and no q=1 witness for aab.

Proof. For any multiset with an a and a non-a, and for any desired attainable first-source B or C, put a representative of the desired source class before the other source class, reserve a non-a penultimate letter (choose from the other class if both occur), and place a last. When no source letters occur, reserve a non-a from A/d/D/e/E. This realizes the same tag and q=1 under aab. Conversely under aba, two or more a can be placed finally as aa, and a single a can be placed last (then suffix aba is impossible because it needs two a). Therefore every desired tag in the suffix-a family is attained. The missing all-a occupancy n>=2 has y_a=n and other y_i=0, so no alternative occupancy exists in that fiber. Subtract exactly one fiber per n>=2. QED.

## Exact pilot slice

At zero cancellation with y_b=1,y_c=0,y_a=k>=0 and all other displacements zero, all words are a^i b a^(k-i), i=0..k, with source tag B. For k=0 the possible terminal states are {0} for both gates; k=1 gives {0,1} for aab and {1,2} for aba; every k>=2 gives {1,2,3} for both. This follows by inspecting the placements of b and suffixes b/ba/aa versus ab/aba/aa. The pilot's finite difference coexists with the proven infinite whole-observer q=1/q=2 source distinctions.

## Executed certificate

An actual Python 3 standard-library exact-integer program compared raw ordered-word (KMP state x source state x ten direction occupancies) DP against independent terminal-suffix occupancy images, with full per-fiber source masks at n=0..7 for both gates. It also checked q=1/q=2 counts, q=2 N-admitting counts, and the pilot slice k=0..10. All assertions passed; the corresponding log ends ALL_CHECKS_PASS.

At n=7: q=1 fibers aab=4841 and aba=4842; q=2 fibers aab=aba=1972; q=2 N-admitting fibers aab=252 and aba=0. The arbitrary-n proof is the suffix/ordering construction above combined with the PREFIX-491 proven polygon. This is author-side mathematical work. Formal CLAIM, independent review, and admission are pending.

## Reusable references and next problem

KMP pattern matching: D. E. Knuth, J. H. Morris Jr., V. R. Pratt, "Fast Pattern Matching in Strings" (1977), DOI 10.1137/0206024. Parikh/semilinear comparison (background, not a substitute for proof): A. Widjaja To, "Parikh Images of Regular Languages: Complexity and Applications" (2010), arXiv:1002.1464.

PREFIX-493: classify q=0 source masks and generating functions using exact Parikh-automaton images; avoid subtracting overlapping observation-image sets. Combine q=0 with proven q=1,2,3 results for the full observer and test the memory and update cost of retaining KMP and source history.
