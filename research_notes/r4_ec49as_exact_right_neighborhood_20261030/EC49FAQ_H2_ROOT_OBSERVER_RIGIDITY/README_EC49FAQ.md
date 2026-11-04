# EC49FAQ — H2-root BRC observer rigidity and nine-window lower-bound exclusion

Date: 2026-11-04. Evidence class: author-side analytic theorem, exact finite checks, independent rational row reduction. Native Driver review/admission pending.

## Frozen inputs and precise model

Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent EC49FAP: `be53f6d8f2fd26c1920ac50adec16817615e6d1b`. Use the same signed native six-axis primitive words, complete positive six-coordinate BRC cache key, nine-history five-bucket observer automaton, six permitted global signatures, and four fixed H2–H7 schedules numbered 1512, 1513, 2200, 2203. All four have exactly 72 existing nonempty native primitive prefix edges. The four H2 words are `de, ed, ce, ec`. The six-signature vocabulary is the union of their four signatures and the two H3 signatures (`feg, gef`); it is common to all four fixed schedules.

We investigate the newly opened H2-rooted path family: each H8 or H9 word starts with one of those four H2 operation words and adds an arbitrary ordered zero-signed-X6-net operation suffix. The root is an operation-word prefix; all edge costs use the expanded ordered signed-X6 primitive trie.

## Theorem A: H2-root observer rigidity (all future operation lengths)

The original observer has buckets N,A,B,AB,BA. Along additional native steps it permits N→A or B on its first transition and thereafter only A→AB, B→BA; AB and BA are absorbing. After any H2 root in `de,ed,ce,ec`, every one of the nine initial-history states is in A,B,AB or BA. Coordinatewise subsequent observations may therefore only stay fixed or move A→AB / B→BA.

Direct coordinate comparison with the six original allowed nine-history signatures gives **exactly one** compatible permitted signature for each root: its own signature. Hence for every ordered continuation `s` of arbitrary length and any H2 root `r`, if `obs(rs)` remains among the original six, then `obs(rs)=obs(r)`. This is an analytic statement, independent of the suffix enumeration length or zero-net restriction.

The four root signatures, in root order `de,ed,ce,ec`, are:

```
de: (2,3,2,3,3,2,4,3,4)
ed: (2,2,2,3,3,2,2,3,4)
ce: (1,1,4,1,3,4,4,3,4)
ec: (1,1,1,1,1,4,4,3,4)
```

Encode each signature as five 0/1 bucket-membership rows with nine columns (one column per initial history). Exact rational elimination gives rank 3 for any one, 5 for any two, 7 for any three, and 9 for all four. A 9×9 integer minor using rows `(de,2),(de,3),(de,4),(ed,2),(ed,3),(ce,1),(ce,3),(ec,1),(ec,3)` has determinant **−1**, giving an independent exact certificate for the full rank. Therefore, H8/H9 words sourced **exclusively from H2 roots** reach rank nine precisely when all four different root signature types are represented.

## Theorem B: exact full-BRC-key feasibility and counts for H2-rooted words

For horizon `h≥2`, any legal word has operation multiplicities `n_e=n_a+1`, `n_b=0`. Write `k=n_a`, `p=n_c+n_d`, `q=n_f`, `r=n_g`. Then

```
h = 2k+1+p+q+r,
K=(x,y,z,0,0,0) = (2(k+1)+p+q, p+r, k+1,0,0,0).
```

A full legal key is realizable with one of the four H2 roots if and only if **`p≥1`**, equivalently **`x+y≥h+2`**. Necessity follows because every root has one c or d; sufficiency follows by ordering one c/d and one e as a H2 root, then the remaining operations, preserving the multiset, complete key and signed six-axis net displacement. The observer condition is a separate filter; this theorem concerns complete-key and net feasibility.

For each `k` with `0≤k≤floor((h−2)/2)`, the number of nonnegative `(p−1,q,r)` with sum `h−2k−2` is `binom(h−2k,2)`. Consequently, the exact count of distinct H2-rooted feasible complete keys is

```
A(h) = sum_{k=0..floor((h−2)/2)} binom(h−2k,2).
A(2m)   = m(m+1)(4m−1)/6    (m≥1).
A(2m+1) = m(m+1)(4m+5)/6    (m≥1).
```

This is an all-horizon identity retaining the complete native BRC key, not an observer quotient.

## Theorem C: H8 all-H2-rooted rank-nine selections are costly

Fix any of the four H2–H7 schedules, with 72 existing native prefix edges, and suppose **all** selected H8 paths start from those H2 operation roots. As the vocabulary contains only the four H2-root signatures for such paths and their exact nine-history rank is 9 only when all four occur, H8 must include an extension of every H2 root.

At the same H8 complete key, all four H2-rooted suffixes have six operations. If `p'=n_c+n_d−1≥0` is their number of c/d operations after the root, their primitive suffix length is `L=2·6+2p'=12+2p'`. The four H2 roots are distinct signed-primitive prefixes of length eight; their outgoing paths share no primitive edges after those roots. The fixed earlier H2–H7 schedule can prepay at most 4,4,0,0 such edges respectively for roots `de,ed,ce,ec` in schedules 1512/1513, and 0,0,0,0 in schedules 2200/2203 (direct full-primitive-prefix comparison). Therefore the new H8 edges are at least `4L−8≥40` for 1512/1513, and `4L≥48` for 2200/2203. The corresponding full nine-window cost, even before H9 edges, obeys:

```
Schedule 1512 or 1513:  E >= 72+40 = 112.
Schedule 2200 or 2203:  E >= 72+48 = 120.
```

This eliminates the **H8-all-H2-rooted** family from a ≤93-edge search for these four fixed early schedules. Mixed H2/H3/H4/H5/H6 paths at H8 remain a separate optimization question; H2 is not globally ruled out.

## Actually executed exact checks

The adjacent `VERIFY_EC49FAQ.py` was run with Python's exact integers and `fractions.Fraction`; `EXACT_REPORT_EC49FAQ.json` is the resulting report. Complete ordered zero-net suffix enumeration used no `b` operation and equal multiplicities of `a,e`. For H8 it checked 13,236 zero-net six-operation suffixes, yielding 15,956 permitted H2-rooted words across 50 distinct feasible keys; for H9 it checked 73,392 seven-operation suffixes, yielding 73,932 permitted H2-rooted words across 70 keys. At each key the exact permitted signature set equals the four distinct root signatures, each rank nine collectively. The enumeration's key sets equal the analytic complete-key formula's sets. Four fixed schedules and their prior primitive prefix sets were checked independently; every claimed new-edge bound above uses the exact native primitive trie.

The all-horizon mathematical statements are analytic. The finite enumeration covers only H8 and H9, and the fixed schedule edge exclusions are local to the four named schedules. The unrestricted H9 mother problem retains the author-side bound `80≤E*_H9≤94`.

## Next EC49FAR

Audit the **mixed** H2 and H3–H6 source pools for the same four fixed H2–H7 schedules; use Theorem A's root-signature restriction to prune H2 words before a joint signature-mask primitive-trie dynamic program. Seek either a genuine ≤93-edge H9 construction or a scoped strict lower bound. In parallel, consider varying earlier H2–H7 schedules; the fixed-family exclusions do not choose that route's answer.

Native CLAIM/Result and independent Driver review require currently valid Source role/owner authority. GitHub evidence is author-side persistence, not formal admission.
