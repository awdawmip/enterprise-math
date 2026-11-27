# T6 p13 q13 split(5,8), length-five second family, final positive row

2026-11-27 | EM-DVR-DEBB5E | directed separate arithmetic implementation; author execution not replayed. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Original author line EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F. Read source certificate at 2b6c80f7a0601746b7058557f1bd966057f978ab:research_checks/T6_P13_Q13_SPLIT5_8_LEN5_NEG1_1_1_2_3_POS11111_FINAL_20261127.json; blob ac9ba27109bcef9b09fb633b6104ece586765d20. Certificate labels its scope AUTHOR_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Negative pattern (1,1,1,2,3), positive (1,1,1,1,1). Independently enumerate r=1..12 nondecreasing within equal q, mass sum(13(13q+r)-1)<=2331. All 52416 negative rosters are budget-feasible; 8085 remain when every 13q+r has all prime factors <=13, a necessary filter for genuine maximal p13. Positive raw count C(16,5)=4368; all fit. Thus 228953088 original pairs, matching the source. The six consecutive negative ranges partition [0,52416). Aggregate counts independently summed: domain 228953088, common feasible 144937728, representative searches 93045888, nodes 145379435, representative leaves 2, leaves 2, valid 0. Representative-fiber completeness and search coverage are still author-executed evidence.

Recomputed all 12 mixed congruences of the two witnesses using modular inverses and powers mod 13^k. Both have all-zero residues. Recomputed (total positive mass, total negative mass; weighted norm squared, radius squared):
- (2236,4465;1507120,1630141).
- (2670,3113;1779601,1806148).
Both violate signed budgets and contain non-13-smooth cofactor atoms. These checks exclude the reported witnesses within the true model; no independent full affine search or global q13 exclusion claimed.

Reproducible arithmetic core, separately executed with exact JSON readback:
```js
const c=JSON.parse(require("fs").readFileSync(process.argv[2],"utf8"));let raw=0,feasible=0,smooth=0;const isSmooth=n=>{for(let p of [2,3,5,7,11,13])while(n%p===0)n/=p;return n===1};function rec(i,prev,m,s){if(i===c.neg_pattern.length){raw++;if(m<=2331){feasible++;if(s)smooth++}return}let q=c.neg_pattern[i];for(let j=i&&q===c.neg_pattern[i-1]?prev:1;j<=12;j++)rec(i+1,j,m+13*(13*q+j)-1,s&&isSmooth(13*q+j))}rec(0,1,0,true);
const mod=(x,m)=>(x%m+m)%m;function inv(a,m){let [r,t,r1,t1]=[a,1n,m,0n];while(r1){let q=r/r1;[r,r1]=[r1,r-q*r1];[t,t1]=[t1,t-q*t1]}if(r!==1n)throw Error("not unit");return mod(t,m)}function pow(a,k,m){let v=1n;while(k--)v=v*a%m;return v}
const mass=v=>v.reduce((s,[q,r])=>s+13*(13*q+r)-1,0), results=c.witnesses.map(w=>{let residues=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),t=0n;for(let [q,j] of w.pos)t+=pow(inv(BigInt(13*q+j),m),k,m);for(let [q,j] of w.neg)t-=pow(inv(BigInt(13*q+j),m),k,m);for(let i=0;i<12;i++)t+=BigInt(w.u[i])*pow(inv(BigInt(i+1),m),k,m);residues.push(Number(mod(t,m)))}let A=mass(w.pos),B=mass(w.neg),u=w.u.map((x,i)=>x*(13*(i+1)-1)),masses=[A+u.reduce((s,x)=>s+Math.max(x,0),0),B+u.reduce((s,x)=>s+Math.max(-x,0),0)];return {residues,masses,norm:u.reduce((s,x)=>s+x*x,0),radius:(2331-A)**2+(2331-B)**2,allSmooth:[...w.pos,...w.neg].every(([q,j])=>isSmooth(13*q+j))}});const totals=c.counts[0].slice(2,9).map((_,i)=>c.counts.reduce((s,row)=>s+row[i+2],0));console.log({raw,feasible,smooth,expectedRawPair:feasible*4368,totals,witnesses:results,expected:c.totals})
```

Current discovered author commits include split58 length-four completion, length-five first-family completion and this second-family final positive row. Preserve author's continuation rather than dispatching stale q14 preflight. This note does not claim a fresh native CLAIM or change any frozen input.
