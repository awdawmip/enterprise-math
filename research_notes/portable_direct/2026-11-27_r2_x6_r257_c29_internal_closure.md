# X6 R257 — complete c=29 internal closure by coupled three-polar incidence

2026-11-27. Author proof and exact computation, NOT_REVIEWED. Frozen R247/R253/R254/R255 inputs unchanged, same necessary-wall and suffix capacity premises. Native read r2-20261127-0711-x6-read, Source e59d205c8495d5e5cacd7a4a385ccde9894f6b83, NO_CANONICAL_PUBLICATION_DIRECTORY, directory absence only. Own researcher binding and live owner projection unconfirmed. No CLAIM, Result, Review or shared state changes. P000 V5 and residual/observer fidelity retained; auxiliary coefficient arithmetic.

For c=29 the split budget is one, so in R254 enumerate each target label as an allowed exception. A partition with no split is covered as well (any one exception is allowed but not forced to split). For every candidate triple and every such exception, merge germ components across all other labels and all endpoints outside the triple, fix the exact coupled local masks, and enumerate every free component sign. This is a complete relaxation of exactly-three-mixed nonsingular Q. All 14 c=29 targets completed, no cutoff or survivor. Common prefix 3,275,335, total 11,474,837, incremental 8,199,502 checks. Columns as R254; conflicts/branch visits sum over label exceptions, patterns counted before exceptions.
```
33cf3010fffe7f304fffc030 286 8 2696 61714 36402 1750 205987
33cf3303fffc0f300ffffff0 560 14 4698 125145 25647 1374 151300
3fd3fcfef0003a3dfb0003fcf 560 10 5084 126052 814334 50366 5899899
32cb3010fffe7d304fffc030 220 6 2316 45793 48617 2257 254464
12cb3010fffefd304fffc030 220 6 2316 45793 48729 2284 136583
32cf3010fffe7f304fffc030 286 8 2696 61714 36060 1692 22951
12cf3010fffeff30cfffc030 286 8 2696 61714 36526 1778 97718
12cf3010fffeff304fffc030 286 8 2696 61714 36136 1709 49053
12cf3010fffe7f304fffc030 286 8 2696 61714 35746 1640 0
20f3018fffeffb0cfffc030 286 7 3132 71383 29797 1050 103130
33cb3010fffc7d304ffff030 220 9 2108 41031 48647 2417 228143
3cc35dfff0003f3dffc000fcf 560 15 5734 143589 82717 4712 581064
33cf3202fffc0f300ffffeb0 364 12 3593 93181 53116 3666 383931
12cb3010fffefd30cfffc030 220 6 2316 45793 49301 2387 85279
TOTAL 4640 125 44777 1046330 1381775 79082 8199502
```
Combine R253 (<=2 excluded) and R256 (>=4 excluded) with this result. All 14 c=29 targets fully closed, adding to all 14 c=30 targets. Only six internal targets remain, c=27 (two) and c=28 (four), each exactly three mixed endpoints; the general root case is still open and K6=1–2.

Reproduction: frozen R247 first JavaScript block as src, R254 at f1fccb394d012ac8039977842bb5cb339805f264:research_notes/portable_direct/2026-11-27_r2_x6_r254_three_polar_incidence_four_null_descent.md first JavaScript block as code.
```javascript
let old=code;
code=code.replace("roots.filter(t=>count(t)===30)","roots.filter(t=>count(t)===29)").replace("let L=tag.map(v=>v&t).filter(Boolean),E=","let L=tag.map(v=>v&t).filter(Boolean),E=").replace("let comps=E.flatMap", "for(let skip of L){let comps=E.flatMap").replace("for(let v of L){let x=v,rest=[];","for(let v of L){if(v===skip)continue;let x=v,rest=[];").replace(" }\n result.push({t:t.toString(16),triples", " }}\n result.push({t:t.toString(16),triples").replace("console.log(Function","return (Function");
if(!code.includes("for(let skip of L)")||!code.includes("if(v===skip)continue")||code===old)throw Error("patch");
console.log(Function("src",code)(src));
```
Next: for the six targets, either enumerate exact split supersets with budget 2 or 3, or use exact three-anchor two-projective-parameter arrangements with capacity pruning. No independent review or Activity association yet.
