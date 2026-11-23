# R762KV — Sharp eleven-event reserve with singleton supports

2026-11-24. AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED. Continuation of R762KU, immutable 80bbd7c4b4bafa557ad2c02c263359b43f80c2b7:research_notes/portable_direct/R762KU_STREAMING_ORDERED_CODER_AND_SUFFIX_SATURATION.md, blob a79c5c97dcff26ce94cafb3f421011b62c2995f1. Frozen science P000 a72226e2430ffa4786321ac86e7f0c599d5f0389 and mandatory joint-relation companion read. Independent portable research, no Task CLAIM or PROGRESS. Original registration EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91 confirmed; own recovery r3-20261124-0620-own-recovery-v1 returned no runs and execution_authorized=false. Previous inventory r3-20261124-0521-owner-read-v1 SUCCEEDED as of 2026-11-23T21:23:15.647909Z, non-authorizing snapshot. No unrelated shared Task adopted.

## KV.1 Exact domain

Reuse KU's unsigned ordered positive unit branch model: supports s=(i,j,k) in binary cube, ordered lexicographically; Port vertices A_ij,B_ik,C_jk on 12 bits. Local edge masks are A XOR B, A XOR C, B XOR C. A word is mixed (connected three-component quotient) iff at least two of these three colors occur. E is all 2048 even-total masks, F the 512 masks even separately on each four-Port group. A reserve is a fixed suffix schedule with nonnegative integer stocks m_s. Saturation means each residual in E has at least one mixed suffix word, which also ensures a mixed complete word regardless of the preceding prefix. F-saturation is defined similarly with targets restricted to F. These are auxiliary observer theorems, not native signed dynamics. Keep all source information required by other observers.

## KV.2 Exact classification and sharp minimum

For arbitrary nonnegative stocks, put t_s=min(m_s,2). The raw (before mixed restriction) reachable boundary set is identical for stocks m and t: the local set is {0} at 0, three nonzero elements of the local binary 2-space at 1, and the whole local space at every m>=2 (KU.2). XOR Minkowski sum preserves this equality. The executed exhaustive computation below shows for every ternary stock t that raw F coverage, raw E coverage, mixed F coverage and mixed E coverage are equivalent. Specifically the four nested sets of qualifying configurations have the same counts in every total-stock stratum (mixed E subset raw E subset raw F; mixed E subset mixed F subset raw F). This proves equality of the sets, not just equal marginal totals.

For arbitrary m, if t fails raw F coverage then so does m. If t has mixed E coverage, choose the extra m_s-t_s events all in any fixed color and let their total XOR be v in E. To attain target r choose a mixed base word for r XOR v, and interleave the additional predetermined events at the fixed support schedule positions. Mixedness is preserved. Thus the same four-way equivalence holds for arbitrary stocks; the clipped stock test is exact, even though the actual multiplicity counts can differ. No monotonicity of raw reach at stock 0 to 1 is asserted.

For all ternary stocks with total n<=10, raw F coverage fails; at n=11 there are 384 successful stocks. Since clipping never increases total stock, the minimum over ALL integer stocks for either F or E saturation is exactly 11 events (KU's previous 12 applied to stocks zero or >=2). At the minimum all stocks are already clipped. The exact partition by (number empty, number singleton, number double) is (1,3,4):256, (2,1,5):72, (0,5,3):56. One explicit minimal witness in lexicographic order is (0,1,2,2,2,2,0,2), which uses only six support types; another is (1,1,1,1,1,2,2,2). For 10 events in the clipped domain the maximum mixed coverage is 2032/2048 E targets and 508/512 F targets. These are maxima of counts over the clipped domain, not a claim about unclipped mixed coverage at total 10.

Consequently KU's prefix observer theorem extends to any suffix whose clipped stock passes this test. Every one of 3^h color prefixes can extend to the same final b in F because the required residual b XOR prefix is in E, and a mixed suffix is available. Exactly ceil(log2(3^h)) bits are necessary and sufficient for the prefix-only observer. The construction reduces the universal suffix reserve by one event while retaining this observation scope. No claim is made that 11 is required for all restricted prefix schedules, where the residual target set may be smaller.

## KV.3 Exact computation proof and reproduction

For each of all 3^8 stocks, the algorithm propagates integer counts D(r) by D'(r)=sum over the three masks e of D(r XOR e), from D(0)=1. Induction on schedule length proves that each entry counts all labeled ordered words of the corresponding XOR, with no duplication or missing words. Recursing in support order visits each stock exactly once. At each nonempty stock, remove precisely the three monochromatic words, subtracting their individual indicators even when their terminal boundaries coincide; the empty word is removed separately. Quotient connectivity is exactly the complement of these words. All integers are bounded by 3^16=43046721, so Int32Array and JS arithmetic are exact throughout. The coverage counts establish the classification as a finite exhaustive proof; arbitrary stocks follow by KV.2, not by extrapolation. An independently executed Python/Numpy recurrence capped counts at 4 before subtracting up to three monochromatic words: identical connected E/F saturation counts and maximal E coverage. The cap is exact for positivity after at most three removals because counts above three remain positive.

Executed JavaScript source (Node or equivalent JS runtime):
```javascript
const masks=[];for(let i=0;i<2;i++)for(let j=0;j<2;j++)for(let k=0;k<2;k++){let a=1<<(2*i+j),b=1<<(4+2*i+k),c=1<<(8+2*j+k);masks.push([a|b,a|c,b|c])}
const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
const E=Array.from({length:4096},(_,i)=>i).filter(i=>pc(i)%2===0),F=E.filter(i=>[0,4,8].every(s=>pc(i>>s&15)%2===0));
const full=Array(17).fill(0),fonly=full.slice(),rawF=full.slice(),rawE=full.slice(),maxE=full.slice(),maxF=full.slice(),minTypes={};let tested=0;const witness={};
function rec(s,d,stock,v,n){if(s===8){tested++;let a=E.filter(r=>d[r]>0).length,b=F.filter(r=>d[r]>0).length;if(a===2048)rawE[n]++;if(b===512)rawF[n]++;let e=E.filter(r=>d[r]>(n?v.filter(x=>x===r).length:Number(r===0))).length,f=F.filter(r=>d[r]>(n?v.filter(x=>x===r).length:Number(r===0))).length;maxE[n]=Math.max(maxE[n],e);maxF[n]=Math.max(maxF[n],f);if(e===2048){full[n]++;if(n===11){let key=[0,1,2].map(i=>stock.filter(x=>x===i).length).join(",");minTypes[key]=(minTypes[key]??0)+1;witness[key]??=stock}}if(f===512)fonly[n]++;return}rec(s+1,d,[...stock,0],v,n);let z=d;for(let m=1;m<=2;m++){let q=new Int32Array(4096);for(let r=0;r<4096;r++)q[r]=masks[s].reduce((a,e)=>a+z[r^e],0);z=q;rec(s+1,z,[...stock,m],m===1?v.map((x,c)=>x^masks[s][c]):v,n+m)}}
let d=new Int32Array(4096);d[0]=1;rec(0,d,[],[0,0,0],0);
console.log(JSON.stringify({tested,full,fonly,rawE,rawF,maxE,maxF,minTypes,witness}));
```

Observed output:
```json
{
  "tested": 6561,
  "full": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    384,
    254,
    112,
    36,
    8,
    1
  ],
  "fonly": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    384,
    254,
    112,
    36,
    8,
    1
  ],
  "rawE": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    384,
    254,
    112,
    36,
    8,
    1
  ],
  "rawF": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    384,
    254,
    112,
    36,
    8,
    1
  ],
  "maxE": [
    0,
    0,
    6,
    24,
    78,
    240,
    694,
    1379,
    1881,
    1980,
    2032,
    2048,
    2048,
    2048,
    2048,
    2048,
    2048
  ],
  "maxF": [
    0,
    0,
    0,
    6,
    18,
    60,
    172,
    350,
    465,
    495,
    508,
    512,
    512,
    512,
    512,
    512,
    512
  ],
  "minTypes": {
    "1,3,4": 256,
    "2,1,5": 72,
    "0,5,3": 56
  },
  "witness": {
    "1,3,4": [
      0,
      1,
      1,
      2,
      1,
      2,
      2,
      2
    ],
    "2,1,5": [
      0,
      1,
      2,
      2,
      2,
      2,
      0,
      2
    ],
    "0,5,3": [
      1,
      1,
      1,
      1,
      1,
      2,
      2,
      2
    ]
  }
}
```

## Next

Derive a structural characterization via binary incidence constraints on cube edges, so the ternary-stock test can generalize without exhaustive enumeration. For a prescribed prefix schedule with restricted target set, compute the smaller sharp reserve directly using the observer image rather than universal E. Then connect only to the native signed event law with a typed BRC preservation certificate. No native sign, common-depth, or time data are discarded here.
