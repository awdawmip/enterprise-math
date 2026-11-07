# EC49EXB — Early-repeat exact theorem and reduction of the H7/M5/S4 optimum

Date: 2026-11-03. Predecessor: EC49EXA, Git commit `60ae5af2153e335c9d4d133c2e94393cfbb6c70d`, Draft PR #1730.
Status: author-side analytic lemma, exhaustive finite enumeration, two independently executed checkers; unreviewed and not canonically admitted.

## Frozen scientific model

Global scientific input pin `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral rules separately read from current canonical main. P000 and ACTIVE worldview unchanged.

Operation words expand to signed primitive native-X6 steps:

~~~text
a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1)
e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2).
~~~

At horizons h=2,...,7 each selected operation word has h letters, displacement (2,0,0,0,0,0), and the same complete six-axis positive step-count p_h within its horizon. Each horizon's nine seam-history 5-bucket observer has rank 9. Let E be the number of distinct nonempty **primitive signed native step prefixes**; M the number of distinct full p_h keys, indexing the two symbolic BRC monomial factors; S the number of distinct nine-history transfer signatures.

## Lemma 1: Four-signature horizons add at least eight native prefix edges

The seven operation codewords, over the signed native primitive alphabet, are prefix-free. Every returning length-h word's last two primitive edges cannot occur in a shorter (<h)-operation word: a matching primitive prefix uniquely decodes h-1 full operations followed by a nonempty prefix of the hth operation, and a shorter operation word ends no later than the h-1 boundary.

For a fixed h and a fixed complete p_h, distinct returning words also cannot share the primitive prefix obtained by removing the final **two** primitive steps. Their expanded primitive length L is fixed by (p_h,displacement). Shared first L-2 native steps would force their first h-1 operation codes to agree, by unique prefix decoding and each code length at least two. Their final codes would then have identical positive-count vectors and signed displacement. Among the seven codes, the only unequal same-positive-count pairs are (c,d) and (a,b): c,d differ already in their first primitive positive axis, and a,b have different signed displacement. Thus their last-two-edge suffixes are disjoint.

Consequently every four distinct required signatures at a common h and p_h add at least eight **new** primitive native prefix edges relative to all shorter horizons. This lemma is specific to the frozen operation code and full BRC p_h, not a generic claim about arbitrary codes.

## Theorem EC49EXB-1: The early-repeat subclass has exact optimum E=80

The h=2 basis forces T4={sig(ce),sig(de),sig(ec),sig(ed)}. Exact nine-history observation ranks for every T4 subset of sizes 1,2,3,4 are respectively 3,5,7,9. With global S<=4, each horizon must therefore realize all four T4 signatures. Exhaustive returning-word enumeration gives the T4-complete positive-key fiber counts for h=2..7:
`(1,3,7,13,22,34)`.

There are 204,204 ordered candidate key schedules. Exactly **26,037** schedules have M=5. Since there are six horizons, each has exactly one duplicate pair. The complete exact partition is:

| Repeated horizon pair | schedules |
|---|---:|
| (3,4) | 9,257 |
| (4,5) | 6,513 |
| (4,6) | 1,215 |
| (5,6) | 4,598 |
| (5,7) | 1,251 |
| (6,7) | 3,203 |
| **Total** | **26,037** |

The first four classes total **21,583**: their repeated key appears entirely by h=6, so horizons 2..6 have M=4 and S=4. By the previously proved exact EC49ES H6/M4/S4 result, E(2..6)>=72. Lemma 1 adds >=8 at h7. Hence **E>=80 for every one of these 21,583 schedules**.

Equality is attained by the EC49EXA all-H construction: h2 ce,de,ec,ed; h3 cec,ded,ecc,edd; and for h>=4 the four words (cefg,degf,ecfg,edgf) each followed by exactly h-4 repetitions of f. At H=7 this yields E=80,M=5,S=4 and duplicate pair (3,4). Therefore:

**min E over the entire early-repeat H7/M5/S<=4 subclass = 80 (exact).**

The only schedules that might improve on 80 now number **4,454**, comprising repeated pair (5,7):1,251 and (6,7):3,203. The full unrestricted five-key/four-signature optimum is *not* yet proved to be 80. For late-repeat schedules the inherited H6/M5/S4 bound 60 plus Lemma 1 gives E>=68, while EC49EXA gives a full-subproblem upper bound E<=80.

## Executed evidence and reproduction

`VERIFY_EC49EXB.py` was executed with Python 3 against the immutable prior EC49ER helper `VERIFY_EC49ER.py`, re-enumerated returning words (8,51,304,1770,10224,58947), checked exact Fraction observer ranks, all 204,204 key schedules, the 21,583/4,454 partition, full primitive prefix 80-edge witness, and zero same-(h,p) terminal-2 prefix collisions. Result: PASS.

`VERIFY_EC49EXB_INDEPENDENT.js` independently re-enumerated the full operation language and signatures using Node.js, without Python imports; all six repeated-pair counts and 204,204 schedule totals agreed exactly. Result: PASS.

`EC49EXB_EXECUTED_SUMMARY.json` records the two executed checkers' shared finite results. These results certify finite enumeration. The new exact 80 theorem also uses the analytic terminal-edge lemma and the precisely scoped inherited H6 theorem. Heuristic search is not evidence against a sub-80 late-repeat schedule.

## Next exact unit: EC49EXC

Restrict full primitive-prefix OR-mask optimization to the remaining 4,454 late-repeat schedules. Apply H6 key-specific lower bounds and at-least-eight native terminal edges before bounded DP; prove E>=80 across survivors or exhibit an exact returning rank-nine six-axis counterexample E<80. Separately keep the H7/M4/S<=6 frontier (known E<=72) open. Preserve task identity, frozen scientific pins, author history and independent Driver admission.
