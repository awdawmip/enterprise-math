# EC49FGL — Exact support/length Pareto skeleton for original BRC 24 demands

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_EXACT_FINITE_THEOREM / FULL_DFA_ENUMERATION_PASS / UNREVIEWED / NOT_ADMITTED.

Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab (unchanged).
Frozen nine-state observer and native signed-X6 code: EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py, blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.
Catalogue provenance: EC49FGK_SEVEN_KEY_COVER_TAXONOMY_20261110/EC49FGK_key_masks.txt, blob 21149331ef01890a05e4bc3531c9fe2a82814598.
This new result is about 24-label raw-key support and individual primitive path lengths. Its claims do not establish a 7-key native-prefix cost optimum.

## Theorem 1: a complete-key path-length invariant

For a legal length-h BRC word with complete raw positive-axis key K=(x,y,z), original operation multiplicities satisfy
a=z-1; e=z; c+d=x+y-h-1; f=h+1-y-2z; g=h+1-x.
The frozen signed-X6 primitive lengths are 2 for a,f,g and 4 for c,d,e. Therefore each such word has exactly

    L(K)=2a+4(c+d)+4e+2f+2g
        =2h+2(c+d+e)
        =2(x+y+z-1)

ordered native signed microsteps, independent of operation order, terminal signature or h after K is fixed. L(K) is individual-path length, not the union-of-prefixes objective.

## Theorem 2: 14 support/length-Pareto keys and all-k counting formula

Let S(K) be the subset of the original 24 H2–H9 demand labels attainable using K. Say J strictly support/length-dominates K if S(J) contains S(K), L(J)<=L(K), and at least one strict inequality/inclusion holds. Equal support and length are not treated as domination: distinct keys remain distinct.

An independent full finite enumeration from the frozen DFA reproduces exactly 178850 accepted matching words, 94 supported raw keys, 21 distinct support masks (all equal to the pinned EC49FGK catalogue), and exactly 14 undominated keys.

| Support mask and role | All undominated keys | Count |
|---|---|---:|
| 1 / H2 forced | (3,0,1) | 1 |
| 2 / H2 forced | (2,1,1) | 1 |
| 12 / H3 forced | (3,1,1) | 1 |
| 1008 / A | (3,3,1), (4,2,1), (5,1,1) | 3 |
| 16776192 / B | (5,5,1), (6,4,1), (7,3,1) | 3 |
| 261120 / optional | (4,5,1), (5,4,1), (6,3,1), (7,2,1) | 4 |
| 15600 / optional | (5,3,1) | 1 |

A 24-label support cover that uses only these efficient keys contains the three forced keys and at least one A-key and one B-key; conversely any such choices suffice. Among the other 11 keys there are 3 A, 3 B, 5 optional. Thus for all integer 0<=k<=14 the number of unordered exactly-k-key covers restricted to this Pareto set is

    N(k)=binom(11,k-3)-2 binom(8,k-3)+binom(5,k-3),

with binom(n,r)=0 if r lies outside [0,n]. This is inclusion-exclusion; the checker also enumerates every subset of the 14 keys independently.

| k | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N(k) | 9 | 63 | 195 | 351 | 406 | 314 | 163 | 55 | 11 | 1 |
| Inclusion-minimal support covers | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

In particular, all 195 efficient-only seven-key covers contain a covering five-key subset; this does NOT imply that deleting two keys preserves the signed-native prefix optimization cost.

## Exact relevance to the open 7-key / 93-edge question

The two prior certified 7-key, 94-edge witnesses of EC49FGJ contain, respectively, (7,4,1) and (6,5,1). Each has mask 4193280 and L=22; (6,4,1), already in each witness inventory, has superset mask 16776192 and L=20. Thus both seventh keys are strictly support/length-dominated, even though they participate in valuable signed-prefix-sharing constructions. Dropping dominated keys is therefore an exploratory *priority filter* only, not a sound completeness-preserving pruning rule for C_native.

The full 7-key domain still comprises 108434 support covers (EC49FGK). Exactly 195 are supported entirely by these 14 Pareto keys; all must remain distinct from an exact all-key lower bound. Next test: signed-prefix optimization on the 195 efficient-only and 4904 inclusion-minimal support inventories as prioritized subfamilies, followed by other eligible inventories. Goal remains a seven-key <=93 witness or a global >=94 certificate.

## Evidence, execution, ownership

The adjacent Python verifier independently regenerates the 94-key mask catalogue and 178850 matching words directly from the literal frozen nine-state DFA; checks 14 efficient keys, inclusion-exclusion versus exhaustive subset enumeration for every k in 0..14, and the dominated 94-witness key cases. Local executed stdout:

    PASS frozen DFA catalogue: 94 keys, 178850 matching words
    PASS efficient 14 5/6/7/8 covers [9, 63, 195, 351] minimal 7 0

Run from repository root:

    python research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGL_SUPPORT_LENGTH_PARETO_20261110/VERIFY_EC49FGL.py research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGK_SEVEN_KEY_COVER_TAXONOMY_20261110/EC49FGK_key_masks.txt --full

Input evidence is the above immutable frozen model and existing pinned catalogue. Output file: EXACT_REPORT_EC49FGL.json.

Researcher-ID EM-DIRECT-52F078 / TASK_RESEARCH; native Research-Activity-ID RA-65693E1A8CE24C095D65015E recorded and read back in canonical Source. Exact historical task EC49AS currently returns NO_CURRENT_IMMUTABLE_PUBLICATION: no claim and no formal Result, independent Driver review pending. P000 and ACTIVE worldview are preserved unchanged.
