# T6 q13 six-atom completion and seven-atom nine-pattern coverage audit
2026-11-28; EM-DVR-DEBB5E informed Driver, alternative combinatorial audit of EM-DIRECT-D03BC9 author certificates (shared frozen context); not an independent affine solver run or formal admission. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, p=q=13, valuation 1, split (6,7), side budget 2331. Reuse per-roster proof at 6425a7e23e2ba623af5a1f1056a3e57eea241c1a and forecast a68de3bed1825942cee4399ce5854ce070f4efe2.

## Pinned inputs
All paths research_checks/T6_P13_Q13_SPLIT6_7_<tag>_CERT_20261128.json. Same initializer prefix SHA256 22d0469739581b7cac3c5bdd3064859ef77255e656618e792af53d3a1427bee8 and kernel blob 89e0f5aea7f6efcfd79dc32f29b84fa510f5d95e.
| tag | commit | blob |
|---|---|---|
|LEN6_POS111111_SHARD20000_40000|36c53cbe5a2e6906cae7703e4c46d33e5c048253|28501d94f17805ca59d70c3b1d76e3affe5c3507|
|LEN6_POS111111_SHARD40000_52416|6c6fce8aec3d117829d877d1315bd9f7cd79c3e4|56c4a4138ddd00bff49ed3cc68cce6032977ecd7|
|LEN7_POS6_TO114|233e45c2acd6da8adc46801cf98d1852feac0255|1b9fa13408189cba3073a6f0406ed0f2cefcddb0|
|LEN7_POS123_POS222|3eed54b5134bf675c11c40a0b44235e6aabed394|c802f81ae9d43870b5331ab0696988291e302973|
|LEN7_POS1113|d93640cd97aa596ad8adefc864ae436a2a7bc27b|db12ee0bebc22f9fdf33e86381ebb9bef44be230|
|LEN7_POS1122|03e5634cb3ef5e0f7feb0408d3aff54a9b9cfee4|89199b9e1dd9a62525b7f04a0758a4f7744bb698|
|LEN7_POS11112_SHARD0_5000|5fd72387bf088a14d5722c27d6eba0c7e92ea0af|7687f646fc6ae370d37a4f8ec96878581f2bbf2f|

## Executed results
33 new shard rows, 99 raw/common/representative comparisons, zero differences. Actual new shard boundaries used (not the earlier forecast's 2500 block grid). All nine completed seven-atom positive patterns cover [0,31824) contiguously; tenth covers [0,5000). For neg (1,1,1,1,1,2), the two new six-atom certificates cover [20000,52416), completing the previously audited [0,20000) positive (1,1,1,1,1,1) family. This verifies combinatorial coverage only; affine solver exhaustiveness remains author evidence.

|negative length / positive pattern or range|raw|common|representatives|author nodes|
|---|---:|---:|---:|---:|
|6 / [20000,40000)|247520000|206890928|40629072|59074595|
|6 / [40000,52416)|153660416|121789808|31870608|45752650|
|7 / 6|381888|0|381888|634294|
|7 / 1,5|4582656|1782144|2949024|4744660|
|7 / 2,4|4582656|0|4582656|7355151|
|7 / 3,3|2482272|0|2482272|3984908|
|7 / 1,1,4|29787264|17926272|13066560|20414863|
|7 / 1,2,3|54991872|21385728|35388288|55175136|
|7 / 2,2,2|11583936|0|11583936|18017661|
|7 / 1,1,1,3|139007232|101097360|43475796|66033700|
|7 / 1,1,2,2|193617216|116520768|84932640|128726595|
|7 / 1,1,1,1,2 partial|81900000|64918788|25727952|39242017|
|total new|924097408|652311796|297070692|449156230|

For completed six-atom final pattern including earlier audit: raw 648700416, common 534570048, reps 137025648; exact forecast matched. One author affine witness (LEN7_POS1122): independently recalculated masses (3001,3313), six residues all zero; nonsmooth d entries 31,17,19,19. Both masses exceed 2331, so invalid. No independent solver exhaustion asserted.

## Reproduction (executed JS algorithm, adapted to local JSON array certs)
```js
const C=(n,k)=>{if(k<0||k>n)return 0;let z=1;for(let i=1;i<=k;i++)z=z*(n-i+1)/i;return Math.round(z)},M=(n,k)=>k===0?1:C(n+k-1,k);
function multi(n,k){let out=[];function r(v,last){if(v.length===k){out.push(v);return}for(let i=last;i<n;i++)r([...v,i],i)}r([],0);return out}
function counts(p){let a={};for(const q of p)a[q]=(a[q]??0)+1;return a}
const rosters={6:multi(12,5),7:multi(12,7)};
function audit(certs){let bad=[],tot=[0,0,0,0],fields=0;
for(const j of certs){let n=(j.neg??j.neg_pattern).length,cols=j.shard_columns??j.columns;for(const g of j.groups??[{pos:j.pos_pattern.join(","),shards:j.shards}]){let a=counts(g.pos.split(",").map(Number));for(const row of g.shards){let [lo,hi]=row,raw=0,dis=0,rep=0;for(let i=lo;i<hi;i++){let v=n===6?{1:rosters[6][Math.floor(i/12)],2:[i%12]}:{1:rosters[7][i]};let R=1,D=1,P=1;for(const q of Object.keys(a)){let k=a[q],v0=v[q]??[],z=v0.filter(x=>x===0).length;R*=M(12,k);D*=M(12-new Set(v0).size,k);let t=0;for(let c=0;c<=Math.min(k,z);c++)t+=M(12-new Set(v0.slice(c)).size,k-c);P*=t}raw+=R;dis+=D;rep+=P}let expect=[raw,raw-dis,rep],names=["search_domain","common_feasible","representative_search"];fields+=3;for(let i=0;i<3;i++)if(expect[i]!==row[cols.indexOf(names[i])])bad.push({pos:g.pos,lo,field:i,expected:expect[i],actual:row[cols.indexOf(names[i])]});tot=tot.map((x,i)=>x+(i<3?expect[i]:row[cols.indexOf("nodes")]))}}}return {bad,tot,fields}}
function pow(a,e,m){let r=1n;while(e>0n){if(e&1n)r=r*a%m;a=a*a%m;e>>=1n}return r}
function witness(w){let a=w.pos.reduce((s,[q,r])=>s+13*(13*q+r)-1,0),b=w.neg.reduce((s,[q,r])=>s+13*(13*q+r)-1,0);for(let i=0;i<12;i++){a+=Math.max(0,w.u[i])*(13*(i+1)-1);b+=Math.max(0,-w.u[i])*(13*(i+1)-1)}let res=[];for(let k=1;k<=6;k++){let m=13n**BigInt(k),phi=m-m/13n;let inv=s=>pow(BigInt(s),phi-BigInt(k),m);let v=0n;for(let i=0;i<12;i++)v+=BigInt(w.u[i])*inv(i+1);for(let [q,r] of w.pos)v+=inv(13*q+r);for(let [q,r] of w.neg)v-=inv(13*q+r);res.push(Number((v%m+m)%m))}return {a,b,res,nonsmooth:[...w.pos,...w.neg].map(([q,r])=>13*q+r).filter(d=>{for(let p of [2,3,5,7,11,13])while(d%p===0)d/=p;return d!==1})}}
```
## Control frontier
Own managed recovery dvr-20261128-1305-recovery-v1 succeeded, original Driver SID unchanged, recent 50 requests no pending writes in returned scope; F7 flow and T6 synthesis terminal SUCCEEDED, no replay. Fresh P12 read dvr-20261128-1306-p12-current-owner-v1 RUNNING at last observation; consume original receipt, no actual new claim. No new native Review, Result admission, Task or parent closure. Next: consume further seven-atom author evidence from index 5000 and final pattern; nonauthor F7 A6 review and P12 actual handoff remain open. No scheduling changes.
