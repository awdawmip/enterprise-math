# X6 continuation — exact clipped-root residual at all six levels (2026-11-25)

AUTHOR PROOF / EXACT FINITE RELAXATION / NOT_REVIEWED. Independent informed static BRC parameter chart, not native spatial/time model. Historical lane EM-DIRECT-AE5AD5; live identity and owner not established; no CLAIM. Frozen inputs R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f inherited through R177 and R178; same Port 10, w=(17t,B,22t,D), positive weights, 1935 directions, exact legal optimizer term and strict 3/2 near set. P000 V5 and ACTIVE worldview loaded. R177@2cb3a23a9bd4b92bcbc1a9946b53a4de8f1ba9ca:research_notes/portable_direct/2026-11-24_r2_x6_r177_two_level_support_capacity.md and R178@4765928190367b00d1e8a19e4a27d952897e4f98 supply bank, supports, clipping and endpoint recursion. No new full direction evaluation.

## New result
For each of the four mandatory root normals passing R177's exact two-level necessary capacity test, reconstruct all active intervals, clip by the fixed root, then use the exact closure extremes in each open child as the initial rays for R178's full-depth finite relaxation. A nonempty support in the child requires a query on that support somewhere in the subtree. When a retained endpoint has a strict query sign it remains in the corresponding child closure; a zero endpoint is retained only when the companion has strict sign, in which case the active sequence approaching the zero endpoint necessarily has that sign. The proof applies to any current clipped extreme pair, not just original global endpoints; gaps are handled by clipping every actual elementary interval before taking extremes. After the fixed first query the remaining depth is 5; enumerate all possible ternary sign patterns on the clipped rays by exact cross-product vertices, adjacent arcs and adjacent chambers with lexicographic infinitesimals (R178). The same finite pattern set is used at all descendants, which retain subsets of these rays. For each candidate second query require both descendants to satisfy the R178 necessary recurrence with remaining depth 4 and lookahead 0,1,2,3,4 respectively. Query signs identified up to reversal; capacities apply to both open children. The recurrence rejects n>2^d-1, accepts at zero lookahead or n<=d (query each retained support normal), otherwise tries every sign class. Each rejection is uniform over all later real linear queries. A surviving class is only feasible in the relaxation. The computation discards new intersections after the first exact clipping, so it is a lower-bound test and not an exact full decision-tree solver. All bit masks of supports are <=31 bits for these eight halves.

## Executed results
```json
{
  "segments": 21842,
  "changes": 1574,
  "fixed": [
    {
      "r": [
        9,
        -1,
        0
      ],
      "halves": [
        {
          "newRays": 8,
          "supports": 26,
          "rays": 38,
          "classes": 2223,
          "counts": [
            73,
            11,
            2,
            2,
            2
          ],
          "cache": 90,
          "scans": 125412
        },
        {
          "newRays": 8,
          "supports": 29,
          "rays": 31,
          "classes": 1391,
          "counts": [
            1,
            0,
            0,
            0,
            0
          ],
          "cache": 2,
          "scans": 1811
        }
      ]
    },
    {
      "r": [
        61,
        0,
        -1
      ],
      "halves": [
        {
          "newRays": 2,
          "supports": 23,
          "rays": 27,
          "classes": 1213,
          "counts": [
            153,
            109,
            96,
            96,
            96
          ],
          "cache": 919,
          "scans": 426245
        },
        {
          "newRays": 2,
          "supports": 27,
          "rays": 30,
          "classes": 1423,
          "counts": [
            4,
            0,
            0,
            0,
            0
          ],
          "cache": 2,
          "scans": 2846
        }
      ]
    },
    {
      "r": [
        69,
        0,
        -1
      ],
      "halves": [
        {
          "newRays": 3,
          "supports": 27,
          "rays": 32,
          "classes": 1697,
          "counts": [
            4,
            4,
            0,
            0,
            0
          ],
          "cache": 10,
          "scans": 10609
        },
        {
          "newRays": 3,
          "supports": 23,
          "rays": 27,
          "classes": 1153,
          "counts": [
            157,
            118,
            98,
            98,
            98
          ],
          "cache": 972,
          "scans": 357170
        }
      ]
    },
    {
      "r": [
        198,
        5,
        -4
      ],
      "halves": [
        {
          "newRays": 6,
          "supports": 28,
          "rays": 30,
          "classes": 1525,
          "counts": [
            3,
            3,
            0,
            0,
            0
          ],
          "cache": 6,
          "scans": 7387
        },
        {
          "newRays": 6,
          "supports": 26,
          "rays": 33,
          "classes": 1751,
          "counts": [
            66,
            24,
            22,
            13,
            13
          ],
          "cache": 166,
          "scans": 138117
        }
      ]
    }
  ]
}
```
A zero final count in either half excludes the corresponding exact fixed root from any depth-six tree. A nonzero count is not a full-domain construction. The mother bound remains 6<=D_linear<=7 unless all arbitrary roots are excluded. No general arbitrary-root class exclusion follows from a fixed representative. The counts track second-query sign classes on the newly clipped rays, not original R178 root classes.

## Reproduction
The following code reconstructs R177's 21842 elementary segments, 1574 active segments and all 47 exact records, checks the pinned data, then performs the eight full-depth finite relaxations using exact integer signs. Code executed in this turn. Next: use dynamic intersections beyond the first cut; classify arbitrary roots uniformly by oriented incidence changes, rather than promoting representative-only tests.
```js
function compute(data){
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},canon=p=>{p=norm(p);return (p.find(x=>x)??0n)<0n?p.map(x=>-x):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()];
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],W=[0,3,5,6,7,9],M=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(x=>x.map(BigInt));
const G=V.map(([x,y,z])=>{let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z],g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(BigInt(Math.abs(h[j]-h[i])));return g});
function terms(rows,mask){let s=new Map();for(let i of rows)G[i].forEach((g,j)=>{if(g&&(!mask||(M[i]>>j&1)))s.set(`${j},${g}`,[j,g])});return [...s.values()].sort((a,b)=>a[0]-b[0]||Number(a[1]-b[1]))}
const T=terms(W,true),H=terms(V.map((_,i)=>i),false),line=(a,b,k,l)=>canon(E[b[0]].map((x,i)=>k*a[1]*x-l*b[1]*E[a[0]][i]));
let L=[];for(let a of T){for(let b of T)L.push(line(a,b,1n,1n));for(let b of H)L.push(line(a,b,3n,2n))}L=uniq(L.filter(q=>q.some(x=>x<0n)&&q.some(x=>x>0n)));
const all=L.concat([[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]]);let K=1n;for(let l of L)for(let m of all)if(abs(dot(l,m))>=K)K=abs(dot(l,m))+1n;
function label(p){let s=E.map(e=>dot(e,p));let fs=G.map(row=>{let a=0n,b=1n;for(let j=0;j<6;j++)if(row[j]*b>a*s[j]){a=row[j];b=s[j]}return [a,b]});let [a,b]=fs[W[0]];for(let i of W){let[c,d]=fs[i];if(c*b<a*d){a=c;b=d}}let m=0,n=0;for(let i=0;i<T.length;i++){let[j,g]=T[i];if(g*b===a*s[j])m|=1<<i}for(let i=0;i<fs.length;i++)if(2n*fs[i][0]*b<3n*a*fs[i][1])n|=1<<i;return[m,n]}
let active=[],segments=0,changes=0;const den=p=>p.reduce((s,x)=>s+x,0n),cmp=(a,b,i)=>sg(a[i]*den(b)-b[i]*den(a));
for(let l of L){let ps=uniq(all.map(m=>canon(cross(l,m))).filter(p=>p.some(x=>x>0n)&&p.every(x=>x>=0n)));let ax=[0,1,2].find(i=>ps.some(p=>cmp(p,ps[0],i)));if(ax===undefined)continue;ps.sort((a,b)=>cmp(a,b,ax));let act=[];for(let i=0;i+1<ps.length;i++){let p=norm(ps[i].map((x,j)=>x+ps[i+1][j]));if(p.some(x=>x<=0n))continue;let pp=p.map((x,j)=>K*x+l[j]),pm=p.map((x,j)=>K*x-l[j]);if(pp.some(x=>x<=0n)||pm.some(x=>x<=0n))throw Error("perturbation");let a=label(pp),b=label(pm),c=label(p);segments++;if(a[1]!==b[1]||c[1]!==a[1]||!(a[0]&b[0]&c[0])){changes++;act.push([ps[i],ps[i+1]])}}if(act.length)active.push({l,ax,act,p:[act[0][0],act.at(-1)[1]]})}
if(JSON.stringify(active.map(x=>({normal:x.l.map(String),segments:x.act.length,endpoints:x.p.map(p=>p.map(String))})))!==JSON.stringify(data)||segments!==21842||changes!==1574)throw Error("source mismatch");
function clip(r,s){let edges=[];for(let f of active){let parts=[];for(let [u0,v0] of f.act){let u=u0,v=v0,a=s*dot(r,u),b=s*dot(r,v);if(a<=0n&&b<=0n)continue;if(a<0n)u=norm(u.map((x,i)=>b*x-a*v[i]));else if(b<0n)v=norm(v.map((x,i)=>a*x-b*u[i]));parts.push([u,v])}if(parts.length)edges.push({l:f.l,p:[parts[0][0],parts.at(-1)[1]]})}return edges}
function solve(edges){
const P=uniq(edges.flatMap(e=>e.p)),ix=new Map(P.map((p,i)=>[p.join(),i])),S=new Map();
function rec(r,t=null,p=null,s=1,u=1){let a=0n,b=0n;for(let i=0;i<P.length;i++){let x=sg(dot(r,P[i]));if(!x&&t)x=s*sg(dot(t,P[i]));if(!x&&p)x=u*sg(dot(p,P[i]));if(x>0)a|=1n<<BigInt(i);if(x<0)b|=1n<<BigInt(i)}let k=a<b?`${a},${b}`:`${b},${a}`;if(!S.has(k))S.set(k,[a,b])}
for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let r=cross(P[i],P[j]);if(!r.some(Boolean))continue;rec(r);for(let k=0;k<P.length;k++)if(!dot(r,P[k])){let t=cross(r,P[k]);for(let s of [-1,1]){rec(r,t,null,s);for(let u of [-1,1])rec(r,t,P[k],s,u)}}}
const Q=[...S.values()].map(([a,b])=>{let au=0,av=0,bu=0,bv=0;edges.forEach((e,i)=>{let x=1n<<BigInt(ix.get(e.p[0].join())),y=1n<<BigInt(ix.get(e.p[1].join())),z=1<<i;if(a&x)au|=z;if(a&y)av|=z;if(b&x)bu|=z;if(b&y)bv|=z});return[au,av,bu,bv]});
const cnt=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24};
const mask=2**edges.length-1;
function split(u,v,[au,av,bu,bv]){let pa=(u&au)|(v&av),pb=(u&bu)|(v&bv);return[u&~bu&pa,v&~bv&pa,u&~au&pb,v&~av&pb]}
let cache=new Map(),scans=0;
function f(u,v,d,k){let n=cnt(u|v);if(n>2**d-1)return false;if(!k||n<=d)return true;let key=`${u},${v},${d},${k}`;if(cache.has(key))return cache.get(key);let ans=false;for(let q of Q){scans++;let[a,b,c,e]=split(u,v,q);if(cnt(a|b)>2**(d-1)-1||cnt(c|e)>2**(d-1)-1)continue;if(f(a,b,d-1,k-1)&&f(c,e,d-1,k-1)){ans=true;break}}cache.set(key,ans);return ans}
let roots=Q.map(q=>split(mask,mask,q)),counts=[];for(let k=0;k<5;k++){roots=roots.filter(([a,b,c,d])=>f(a,b,4,k)&&f(c,d,4,k));counts.push(roots.length)}
return{supports:edges.length,rays:P.length,classes:Q.length,counts,cache:cache.size,scans}}
const roots=[[9,-1,0],[61,0,-1],[69,0,-1],[198,5,-4]],original=new Set(active.flatMap(e=>e.p.map(p=>p.join())));
const fixed=roots.map(r=>({r,halves:[1n,-1n].map(s=>{let es=clip(r.map(BigInt),s);let newRays=uniq(es.flatMap(e=>e.p)).filter(p=>!original.has(p.join())).length;return{newRays,...solve(es)}})}));
return{segments,changes,fixed}
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
console.log(JSON.stringify(compute(data),null,2));
```
