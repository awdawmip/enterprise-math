# R5: Unbounded switch-only Q with coverage-coupled (2,1) attachments

Date: 2026-11-15. Scope: auxiliary *one-dimensional integer indexed-center observer* of the frozen 954-event R5 research (scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`). Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED m=1..6 / NOT_REVIEWED**. Previous exact seven-event core: `CONNECTED_N7_SWITCH_ONLY_FINITE_THEOREM.md`, same portable-direct folder.

## Unbounded theorem

For every integer **m>=1**, take the n=5+2m integer events with consecutive gaps

    (3,2,2,3,(2,1)^m).

The two zero-based cuts a=0 and b=3 are independently shortened from gap length 3 to 2. Select exactly **K=3+m** center indices and minimize the sum of all nearest-center integer distances while covering every event within radius **rho=2**. Let Ft(m), t in {0,a,b,ab}, be the complete optimal center-set families.

Let Gt be the corresponding complete **seven-event** optimizer families for gaps (3,2,2,3,2,1), K=4, as certified by the exact prior theorem. For j=1,...,m-1 let Cj={5+2j,6+2j}, and define H'_(m-1) as the family of sets choosing exactly one member of each such pair. H'_0 contains only the empty set.

Then for **every m>=1** and every mask t:

1. **Optimum and entire optimizer family:** Jt(m)=m+4 and Ft(m)={S union H : S in Gt, H in H'_(m-1)}.
2. **Exponential joint residual:** optimizer counts are (5,12,9,17)*2^(m-1). The intersection residual P=(Fa intersect Fb) minus F0 is empty, while Q=Fab minus (Fa union Fb) consists precisely of `{1,2,3,6} union H` for H in H'_(m-1), so |Q|=2^(m-1).
3. **No neutral joint-only rank arc:** representing each optimizer as an increasing path with center-index *and center-rank* labels, including source and terminal arcs, Eab(m)=Ea(m) union Eb(m). Every joint-only optimum arises solely from switching preexisting singly admissible rank arcs.
4. No appended individual center index is forced across any complete optimizer family. All appended inter-pair **gaps equal 2**, within the covering radius; no radius-separated-block decomposition explains the extension. Original gap lengths remain at most 3, while n,K and |Q| grow without bound.

## Proof: an exact local prefix-cost barrier

Call the first five events the prefix, and each pair Cj={5+2j,6+2j}, j=0,...,m-1, an appended pair. Consecutive pairs have internal distance 1 and inter-pair gap **2**. The prefix's last event and first appended event likewise have gap 2. Hence an outside center can influence prefix distances only if its index is **5**; a later appended index is at least 3 units beyond the last prefix event. In all closure masks this property remains true.

Let q be the number of selected centers in the five-event prefix. Exact inspection of all C(5,q) choices, for each of the four masks and with or without the external candidate center at index 5, proves the following *minimum possible prefix contribution under radius-2 coverage*:

| q | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| smallest feasible prefix distance sum | infeasible | 6 | 4 | 2 | 0 |

In particular, every feasible full center set must have q>=2 and has prefix distance sum >=10-2q. This table is an **exhaustive 5-index finite lemma** reverified independently in the attached executable. Its q=2 value permits assistance from the first appended center and applies equally to all four masks.

Now let r count appended pairs having *no* chosen center, and s count pairs having *both* chosen centers. The other m-r-s pairs have exactly one chosen center. For an empty pair, its left and right events lie at distance **at least 2** from any center outside the pair, because the nearest external possible events are the preceding pair's last index and the following pair's first index, each at distance 2 from the respective adjacent member. Therefore an empty pair contributes distance sum >=4 (or is infeasible); a single-center pair contributes exactly 1; a two-center pair contributes 0.

The exact center budget gives

    q + (m-r-s) + 2s = m+3,
    hence q = 3+r-s.

Adding the prefix and pair contributions yields, for **every feasible** center set,

    J >= (10-2q) + 4r + (m-r-s)
      = (10-2(3+r-s)) + m+3r-s
      = m+4+r+s.

The seven-event core supplies configurations of cost 5 with exactly three prefix centers, one center in the first pair, and any choice among its certified Gt optimizer family. Extending each such configuration with one center from each later pair gives cost **m+4**: the later centers do not improve the already distance-1 missing member of any earlier selected pair, nor can they influence the prefix. Thus the lower bound is attained.

Equality forces **r=s=0** and q=3. Every appended pair must therefore supply exactly one center, while the prefix's exact cost must be 4. The first-pair and prefix choices are *exactly* those enumerated in the seven-event Gt core: these first seven events have cost 5, no later center can improve any of their distances (the already selected center in the first pair is distance 1 from its other event). Every later pair has two independent choices, giving the entire product formula Ft(m)=Gt × H'_(m-1). No additional global optimizer exists.

## Residuals and path edges

Since G0,Ga,Gb,Gab satisfy P=empty, Q={{1,2,3,6}} and Eab=Ea union Eb on the **complete seven-event rank-labeled paths**, adjoining the same independent H' suffix to all four families preserves intersections, differences and unions. Thus Q becomes exactly the advertised 2^(m-1) distinct center-index sets.

For rank arcs, partition extended paths into seven-event source/internal arcs, one boundary arc (last seven-event center to first later selected index), and later suffix arcs plus sink. The base-seven terminal rank arc support determines its last-center index support. Under full independent suffix choices, boundary arc support is the product of this last-center support with the same two first-suffix choices, which commutes with unions. All suffix arcs are common. The seven-event Eab=Ea union Eb identity therefore lifts to all m. Since each later pair has independent choices, no member of any later pair is forced; the seven-event core also has neither index 5 nor 6 forced in any mask.

## Exact verification and remaining frontier

`VERIFY_R5_COUPLED_21_UNBOUNDED.py` independently enumerates the **prefix cost barrier** (q=1..5 with/without index 5), exact seven-event core, and all C(5+2m,3+m) possible center sets for each mask for m=1..6. It checks the whole optimizer families (not just counts), the product bijection, P,Q, rank-arc equality and costs. Actual local result: `PASS_R5_UNBOUNDED_COUPLED_21_BLOCKS`. For m=6: n=17, K=9, J=10, family counts [160,384,288,544], |Q|=32, neutral arcs 0. Arbitrary-m validity follows from the exact budget inequality and product argument, independently of finite truncation.

Next: understand *which* rank/coverage compatibility invariant forbids this mixed-color switching at cuts 8 and 9 in the frozen 954-event special model; examine whether the above local prefix-cost-barrier idea can be generalized to a negative switch certificate.

No formal Task/CLAIM/Result/Review or native X6 promotion is claimed by this author-scoped note.
