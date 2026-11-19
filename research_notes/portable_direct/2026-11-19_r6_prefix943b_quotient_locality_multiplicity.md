# PREFIX-943B — Exact quotient-locality theorem and multiplicity audit

Date 2026-11-19. Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d. Companion to PREFIX-943, k=17. Scope: auxiliary named-XOR two-port observer, strict 19-bit odd moduli; not a native X6 theorem. Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_ENUMERATORS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Quotient-locality theorem (general h and L)

Let h>=0, k>=1 and let the two named histories F_0^i, F_(ka)^j collide at ordered ports (a,b), with 0<=i,j<=h, b>=L>0. Every constructive witness satisfies

    (ka XOR 2^j)-2^i=t*b,   t>=1.

Write epsilon_j(ka)=1-2*bit_j(ka) in {-1,+1} and c=2^i-epsilon_j(ka)*2^j. Then ka=t*b+c. The correction is bounded

    1-2^h <= c <= 2^(h+1).

For any two named witnesses belonging to the same ordered pair (a,b), with quotients t,t' and corrections c,c', subtraction gives (t-t')*b=c'-c. Consequently

    |t-t'| <= floor((3*2^h-1)/L).        (QL)

**Proof:** The correction interval has width 3*2^h-1 and b>=L, so |t-t'|*L<=|c'-c|<=3*2^h-1. QED. This bound uses no average, approximation or assumption about bit distributions.

For the frozen experiment h=18 and L=262145=2^18+1, (3*2^18-1)=786431<3L=786435; thus |t-t'|<=2. Every pair belongs to one, two or three distinct quotient buckets, all within two steps. In particular P_t intersection P_u is empty for |t-u|>=3, and no four different quotient buckets intersect. Here P_t denotes the set of ordered pairs with at least one named witness of quotient t.

For fixed t and pair (a,b), c=ka-tb is uniquely determined: **different correction classes c within one t cannot represent the same pair.** Duplication within t is a question of source-bit and sign descriptions with equal c, not an overlap between different correction lines.

Therefore for any complete finite t-range the exact pair-union size is

    |union_t P_t| =
        sum_t |P_t|
      - sum_t |P_t intersection P_(t+1)|
      - sum_t |P_t intersection P_(t+2)|
      + sum_t |P_t intersection P_(t+1) intersection P_(t+2)|.

The last term removes the triple over-subtraction. Higher intersections vanish by (QL).

## Full exact k=17 quotient-support classification

Two differently organized full finite C++17 programs were executed: (A) direct a,j,i,t enumeration; (B) arithmetic-progression signed-bit CRT enumeration of j,i,t,sign,h. Each encoded (pair ID << 6)|t, sorted and removed duplicate (pair,t) occurrences, and classified each ordered pair by its distinct t-support. They agree *exactly*:

| Distinct t-support | Ordered modulus pairs |
|---|---:|
| Exactly one t | 15,136,473 |
| Exactly two adjacent t,t+1 | 257 |
| Exactly two gap-two t,t+2 | 2 |
| Exactly three t,t+1,t+2 | 4 |
| **Total distinct pairs** | **15,136,736** |

Additional crosscheck:
- Raw (a,i,j,t) witnesses: 19,318,164 (matches PREFIX-943).
- Different (pair,t) keys: **15,137,003**.
- Raw repetitions within t: 19,318,164-15,137,003=**4,181,161**.
- Duplications when joining quotient buckets: 15,137,003-15,136,736=**267**.
- Pairs with more than one distinct quotient: 257+2+4=**263**.
- Pairs violating quotient gap theorem: 0.

For THIS finite k17 model, the actual major multiplicity bottleneck is within-quotient source description, not cross-quotient overlap. This makes signed-bit correction class grouping the next computational target.

## Reproducibility and status

Exact output of direct implementation:

    raw=19318164
    pair_t=15137003
    unique=15136736
    one=15136473
    two_adj=257
    two_gap2=2
    three=4
    problem=0

Independent CRT implementation returned identical counts with bad=0. Full programs named PREFIX943_R6_QUOTIENT_LOCALITY_CPP.cpp and PREFIX943B_R6_QUOTIENT_LOCALITY_CRT.cpp; see companion evidence/handoff. Both use 64-bit integers and exhaustively enumerate the frozen Q (131,072 odd moduli), i,j in [0,18], t in [1,34]. This author-level exact verification does not substitute for an independent mathematical review or Source CLI Activity audit.

Next: count distinct sources for each (t,c) affine line ka=t*b+c by a finite bit-mask/digit-DP union of arithmetic progression cells, then use the quotient locality theorem to subtract the small possible adjacent/two-apart overlaps. Preserve the exact source-labelled identities before any projection or BRC/X6 transport. B_fix,odd(32) in {19,20} remains OPEN.
