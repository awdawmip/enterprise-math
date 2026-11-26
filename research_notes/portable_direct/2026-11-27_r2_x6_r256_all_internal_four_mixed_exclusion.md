# X6 R256 — all 34 internal targets exclude four or more mixed endpoints

2026-11-27. Author proof and exact computation, NOT_REVIEWED. Same source, frozen inputs, role and inherited capacity assumptions as R254/R255. Native read r2-20261127-0711-x6-read Source e59d205c8495d5e5cacd7a4a385ccde9894f6b83, directory absence only, no owner projection or own identity confirmed. No CLAIM, Result, Review or shared-state change.

Extend the complete four-null rank-two sweep of R255, 8cf5d54bd2d3fdfaf8796d0251b54971fc5ea0f9:research_notes/portable_direct/2026-11-27_r2_x6_r255_four_anchor_event_sweep.md (blob 67c1b8064c15db792ff4bd74e89bba8bca45b00a), to the remaining 20 targets of c=27,28,29. Replace the zero split test with the exact budget split<=30-c(T); both complete strict branches must contain <=15 labels. All other event, rank, mixed-anchor, and exact suffix capacity tests are unchanged. This covers every Q with at least four mixed endpoints (not exactly four), by selecting any four of them.

Executed all 20 target masks; zero survivors and no cutoff. Common prefix 3,275,335 checks, total 3,361,070, incremental 85,735. Columns as R255 except labelOK is now split-budget passing, not necessarily zero split.
```
33cf3010fffe7f304fffc030 715 77 39992 14255 121 1 47
3cc35cfff0003f3dff0000fcf 1365 126 74261 21640 2251 74 58586
33cf3303fffc0f300ffffff0 1820 176 112860 29955 149 1 0
33cf3202fffc0c300ffffe30 1001 126 55063 12181 1075 19 7380
3fd3fcfef0003a3dfb0003fcf 1820 124 114886 38692 311 9 2648
2cb3010fffe7d304fffc030 495 51 24974 10480 1031 12 4920
32cb3010fffe7d304fffc030 495 51 26750 11232 316 3 2272
12cb3010fffefd304fffc030 495 51 26420 11142 141 3 2272
2cb3010fffefd304fffc030 495 51 25532 10760 632 6 47
32cf3010fffe7f304fffc030 715 77 38996 13933 258 1 0
12cf3010fffeff30cfffc030 715 77 39850 14367 69 1 0
12cf3010fffeff304fffc030 715 77 38576 13785 107 1 0
12cf3010fffe7f304fffc030 715 77 37720 13491 265 1 0
20f3018fffeffb0cfffc030 715 67 38268 16955 50 0 0
33cb3010fffc7d304ffff030 495 75 26116 8549 62 1 0
3cc35dfff0003f3dffc000fcf 1820 186 100212 31044 214 2 94
33cf3202fffc0f300ffffeb0 1001 126 56101 18113 105 1 0
12cb3010fffefd30cfffc030 495 51 27306 11654 99 3 2272
2cb3010fffefd30cfffc030 495 51 26418 11272 455 6 47
32cb3010fffe7c304fffc030 495 51 26558 9439 752 15 5150
TOTAL 17077 1748 956859 322939 8463 160 85735
```
Together with R255, all 34 targets exclude >=4 mixed endpoints. Together with R253 and R254, the only remaining internal case is EXACTLY THREE mixed endpoints on the 20 lower-label targets. All 14 c=30 targets are fully closed. The general quadratic root case remains open, K6=1–2.

Reproduction: fetch frozen R247 as src and first JavaScript block of R255 as code, then execute the following exact substitutions:
```javascript
let old=code;
code=code.replace("roots.filter(t=>count(t)===30)","roots.filter(t=>count(t)<30)").replace("for(let l of L)if((x&l)&&((t^x)&l))return;labelOK++;\n   if(count(x)!==15)return;","let split=0;for(let l of L)if((x&l)&&((t^x)&l))split++;if(split>30-L.length)return;labelOK++;\n   if(count(x)>15||count(t^x)>15)return;").replace("console.log(Function","return (Function");
if(code===old||!code.includes("split>30-L.length"))throw Error("patch mismatch");
console.log(Function("src",code)(src));
```
Activity association and independent mathematical review pending.
