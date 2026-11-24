# X6 R180 — Uniform linear event refinement of dynamically clipped BRC supports

2026-11-25. AUTHOR PROOF / EXACT INTEGER EVENT CENSUS / NOT_REVIEWED. Informed independent static parameter research; no formal CLAIM. Historical lane EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317; current execution identity not established. Source: R179@350a70a907b9668b8b9b371dc5404a8fb19864a1, inherited frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@1e4ab68c4f9c91bc60c07017acc57be20829832f. Same Port 10, 1935 directions, positive w=(17t,B,22t,D), six pair capacities, exact legal optimizer term and strict 3/2 near set. P000 V5 and joint observer constraints retained; the parameter chart is auxiliary, not native spatial geometry. X6 lookup r2-20261125-0210-x6-read SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY, Source 6c0df3c516eee40e48bdd4a798c8720190745adc. No native owner inference.

## Theorem: uniform refinement by linear event rays

The R179 necessary capacity relaxation clips the actual active open intervals of each support by the first query r, retaining the two extreme closure rays per surviving support, and thereafter uses all linear query sign patterns on these fixed rays in R178's recursive endpoint relaxation. R179 proves all 47 mandatory first normals impossible. For arbitrary nonzero r, testing one representative of the 393 old surviving classes cannot by itself settle its entire class.

Work in the normalized positive weight chart sum(p)=1 (p=(t,B,D)); closures are nonnegative rays. For each support line normal l, merge contiguous active elementary intervals into closed component intervals, solely for closure-extreme purposes. A missing isolated endpoint does not affect closure extremes or open-child necessity. Preserve genuine gaps. Let E be all component endpoints; A=E union the three coordinate rays. Define a finite event set F of nonnegative primitive rays:
1. A;
2. every nonzero projective intersection x=l cross (a cross b), normalized to a nonnegative ray, for a,b in A, where x belongs to an actual closed active component of l;
3. every nonzero projective intersection x=l_i cross l_j belonging to an actual closed active component of both supports.

**Claim.** For r and r' with identical ternary signs on F, the R179 first-clipped endpoint relaxation has identical feasibility, for either open child and any remaining depth. All classes, including zeros, are included. This is a sufficient refinement, not claimed minimal. Each class has a rational representative (a relatively open rational polyhedral cone), so the continuum of root directions reduces to finitely many rational sign classes for this relaxation.

Proof. The signs at component endpoints identify surviving active intervals, whether the clipped extreme is a static endpoint or a dynamic intersection, and the identity of its support and component. If an interval with ordered endpoints u,v crosses the root strictly, the dynamic ray is proportional to r cross l with a nonzero proportionality factor of fixed sign within the root class: use the positive combination |r dot v| u + |r dot u| v, with orientation fixed by the sign of r dot u and u cross v proportional to l. If r vanishes at an endpoint, retain the static endpoint if the interval reaches the strict child. If r vanishes identically on the support, that support disappears from both open children. Genuine gaps are preserved by clipping components before taking extremes. The remaining dynamic rays all lie on r dot p=0.

Compare determinants of triples of labeled clipped endpoints, adjoining the three fixed coordinate rays for a spanning rank-three list. Three static vectors are constant. For one dynamic and two static, the determinant up to a fixed nonzero signed factor is r dot [l cross (a cross b)]. If the cross product is zero, the determinant vanishes identically. Otherwise its zero can occur in the class with this dynamic ray present only if the projective intersection belongs to the relevant active closed component. Those event rays are in F. More strongly, each ternary-sign class of F is convex in r-space; if a determinant changed sign on it, the connecting segment would contain a zero with the same endpoint selection, contradicting fixed event sign. The case of identically zero root vectors on the joining segment is excluded for a nonzero mixed-sign class; if all F signs zero, the three axes imply r=0, excluded. For two dynamic rays and one static a, use (r cross l_i) cross (r cross l_j)=det(r,l_i,l_j) r. The determinant is det(r,l_i,l_j)(r dot a) up to fixed signed factors. The second factor is fixed by A. A zero of the first while both dynamic rays exist implies their projective intersections coincide on both actual component closures, covered by item 3. The same segment argument fixes the sign. Three dynamic rays have determinant zero identically. Thus the complete rank-three signed determinant data, including all zeros and parallelisms, is invariant on a root class.

The labeled sign vectors realizable by any linear second or later query depend only on these determinant signs. Elementary justification: for a requested ternary sign vector, impose equality for zero entries and strict signed positivity for the others. In the quotient by the span of zero entries, strict separation is possible iff there is no nonzero nonnegative dependence of the signed projected strict vectors. Equivalently, in the original list augmented by both signs of zero vectors, a nonnegative dependence with at least one strict vector is an obstruction. A nonnegative dependence decomposes into minimal positive dependencies by subtracting a minimal-support positive relation and iterating. Signs of every minimal dependency are determined by rank and Cramer's rule on a maximal independent sublist extended to rank three using the auxiliary axes; the signed determinants give those signs, including rank-one/ rank-two degeneracies. Therefore the obstruction and hence every realizable query sign vector is invariant. This also proves the result when the clipped endpoint list itself has rank below three. Restrict back to the actual endpoint labels (the auxiliary axes need not be queried). R178's finite recurrence uses only the support-to-two-endpoint association and these realizable sign vectors, so its full feasibility is identical throughout the class. QED.

This is an exact finite quotient for the first-clipped R179 **necessary relaxation**, not the full adaptive problem with fresh clipping at every depth. A failed class excludes all its roots; a surviving class is not a six-query construction. Bounds remain 6<=D_linear<=7. No arbitrary-root feasibility search is claimed here.

## Actual exact replay

The R179 bank and all 47 support records were reconstructed and compared to its immutable embedded data. The code below merges active intervals, enumerates all event rays, and constructs a concrete changed-determinant witness between two roots of the same original endpoint sign class. Integer arithmetic only. No full 1935-direction re-scoring this round; inherited exact bank and prior direction evidence are used at their original scope.

```json
{
  "segments": 21842,
  "changes": 1574,
  "supports": 47,
  "components": 49,
  "splitSupports": [
    {
      "normal": [
        "51",
        "2",
        "-1"
      ],
      "components": [
        [
          [
            "1",
            "9",
            "69"
          ],
          [
            "3",
            "17",
            "187"
          ]
        ],
        [
          [
            "2",
            "5",
            "112"
          ],
          [
            "1",
            "0",
            "51"
          ]
        ]
      ]
    },
    {
      "normal": [
        "17",
        "-1",
        "0"
      ],
      "components": [
        [
          [
            "0",
            "0",
            "1"
          ],
          [
            "1",
            "17",
            "391"
          ]
        ],
        [
          [
            "1",
            "17",
            "69"
          ],
          [
            "1",
            "17",
            "22"
          ]
        ]
      ]
    }
  ],
  "oldEndpoints": 51,
  "componentEndpoints": 51,
  "staticWithAxes": 51,
  "connectorLines": 1028,
  "connectorSupportChecks": 48316,
  "oneDynamicEventRays": 7702,
  "twoDynamicEventRays": 36,
  "twoDynamicInteriorBoth": 0,
  "totalEventRays": 7702,
  "newVsOld": 7651,
  "witness": {
    "support": [
      "187",
      "12",
      "-1"
    ],
    "static": [
      [
        "2",
        "5",
        "73"
      ],
      [
        "1",
        "0",
        "0"
      ]
    ],
    "rootEvent": [
      "13",
      "935",
      "13651"
    ],
    "root1": [
      "-95876770361",
      "110883711685",
      "-7503456537"
    ],
    "root2": [
      "-95876770387",
      "110883709815",
      "-7503483839"
    ],
    "clipped1": [
      "20842233241",
      "1499023142780",
      "21885775329427"
    ],
    "clipped2": [
      "6947301249",
      "499676082760",
      "7295258326683"
    ],
    "det1": "-187224195",
    "det2": "62408065",
    "childSign": -1,
    "commonSignVector": "1,-1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1"
  }
}
```

The witness compares two root directions with the same signs on every component endpoint and the three axes, but opposite signs of the determinant of two original static endpoints and the dynamically clipped endpoint on the listed support. Both static endpoints are retained in the indicated child; the intersection is a closure extreme for that child. This establishes the need for a refinement if the clipped determinant data are to be preserved; it does not by itself prove different optimal depths.

## Reproduction (executed)
Copy the following code into Node.js, or use the same ECMAScript BigInt implementation. All input support records embedded below come from R179 at its immutable commit. The output is reproduced above.

```js
function replay(data) {
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],sg=x=>x>0n?1:x<0n?-1:0,abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=p=>{let d=p.reduce(gcd,0n);return d?p.map(x=>x/d):p},canon=p=>{p=norm(p);return (p.find(x=>x)??0n)<0n?p.map(x=>-x):p},uniq=a=>[...new Map(a.map(p=>[p.join(),p])).values()],den=p=>p.reduce((s,x)=>s+x,0n),cmp=(a,b,i)=>sg(a[i]*den(b)-b[i]*den(a));
const V=[[1,0,0],[1,3,-1],[4,-4,1],[4,-1,0],[5,-4,1],[5,-1,0],[6,-4,1],[6,-1,0],[7,-1,0],[9,-5,1]],W=[0,3,5,6,7,9],M=[30,51,42,21,58,51,20,7,23,30],E=[[17,1,0],[39,0,0],[17,0,1],[22,1,0],[0,1,1],[22,0,1]].map(x=>x.map(BigInt));
const G=V.map(([x,y,z])=>{let h=[0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z],g=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(BigInt(Math.abs(h[j]-h[i])));return g});
function terms(rows,mask){let s=new Map();for(let i of rows)G[i].forEach((g,j)=>{if(g&&(!mask||(M[i]>>j&1)))s.set(`${j},${g}`,[j,g])});return [...s.values()].sort((a,b)=>a[0]-b[0]||Number(a[1]-b[1]))}
const T=terms(W,true),H=terms(V.map((_,i)=>i),false),line=(a,b,k,l)=>canon(E[b[0]].map((x,i)=>k*a[1]*x-l*b[1]*E[a[0]][i]));
let L=[];for(let a of T){for(let b of T)L.push(line(a,b,1n,1n));for(let b of H)L.push(line(a,b,3n,2n))}L=uniq(L.filter(q=>q.some(x=>x<0n)&&q.some(x=>x>0n)));
const axes=[[1n,0n,0n],[0n,1n,0n],[0n,0n,1n]],all=L.concat(axes);let K=1n;for(let l of L)for(let m of all)if(abs(dot(l,m))>=K)K=abs(dot(l,m))+1n;
function label(p){let s=E.map(e=>dot(e,p));let fs=G.map(row=>{let a=0n,b=1n;for(let j=0;j<6;j++)if(row[j]*b>a*s[j]){a=row[j];b=s[j]}return [a,b]});let [a,b]=fs[W[0]];for(let i of W){let[c,d]=fs[i];if(c*b<a*d){a=c;b=d}}let m=0,n=0;for(let i=0;i<T.length;i++){let[j,g]=T[i];if(g*b===a*s[j])m|=1<<i}for(let i=0;i<fs.length;i++)if(2n*fs[i][0]*b<3n*a*fs[i][1])n|=1<<i;return[m,n]}
let active=[],segments=0,changes=0;
for(let l of L){let ps=uniq(all.map(m=>canon(cross(l,m))).filter(p=>p.some(x=>x>0n)&&p.every(x=>x>=0n)));let ax=[0,1,2].find(i=>ps.some(p=>cmp(p,ps[0],i)));if(ax===undefined)continue;ps.sort((a,b)=>cmp(a,b,ax));let act=[];for(let i=0;i+1<ps.length;i++){let p=norm(ps[i].map((x,j)=>x+ps[i+1][j]));if(p.some(x=>x<=0n))continue;let pp=p.map((x,j)=>K*x+l[j]),pm=p.map((x,j)=>K*x-l[j]);if(pp.some(x=>x<=0n)||pm.some(x=>x<=0n))throw Error("perturbation");let a=label(pp),b=label(pm),c=label(p);segments++;if(a[1]!==b[1]||c[1]!==a[1]||!(a[0]&b[0]&c[0])){changes++;act.push([ps[i],ps[i+1]])}}
if(act.length){let parts=[];for(let [u,v] of act){if(parts.length&&parts.at(-1)[1].join()===u.join())parts.at(-1)[1]=v;else parts.push([u,v])}active.push({l,ax,act,parts,p:[act[0][0],act.at(-1)[1]]})}}
if(JSON.stringify(active.map(x=>({normal:x.l.map(String),segments:x.act.length,endpoints:x.p.map(p=>p.map(String))})))!==JSON.stringify(data)||segments!==21842||changes!==1574)throw Error("source mismatch");
const old=uniq(active.flatMap(e=>e.p)), endpoints=uniq(active.flatMap(e=>e.parts.flat())),staticRays=uniq(endpoints.concat(axes));
const positive=p=>p.some(x=>x>0n)&&p.every(x=>x>=0n);
const inPart=(f,p,strict=false)=>positive(p)&&f.parts.some(([u,v])=>{let a=cmp(p,u,f.ax),b=cmp(p,v,f.ax);return strict?a>0&&b<0:a>=0&&b<=0});
const connector=new Map();for(let i=0;i<staticRays.length;i++)for(let j=i+1;j<staticRays.length;j++){let h=canon(cross(staticRays[i],staticRays[j]));if(h.some(Boolean))connector.set(h.join(),h)}
const events=new Map(staticRays.map(p=>[p.join(),p])),evOne=new Map(),evTwo=new Map(),insideBoth=new Map();let checks=0;
for(let f of active)for(let h of connector.values()){let p=canon(cross(f.l,h));checks++;if(inPart(f,p)){evOne.set(p.join(),p);events.set(p.join(),p)}}
for(let i=0;i<active.length;i++)for(let j=i+1;j<active.length;j++){let f=active[i],g=active[j],p=canon(cross(f.l,g.l));if(inPart(f,p)&&inPart(g,p)){evTwo.set(p.join(),p);events.set(p.join(),p);if(inPart(f,p,true)&&inPart(g,p,true))insideBoth.set(p.join(),p)}}
// Find an actual changed triple determinant inside one old sign class, with two static extremes in one open child.
let witness=null;const signKey=(r,ps)=>ps.map(p=>sg(dot(r,p))).join(",");
outer: for(let f of active)for(let i=0;i<old.length;i++)for(let j=i+1;j<old.length;j++){let a=old[i],b=old[j],h=cross(a,b),p=canon(cross(f.l,h));if(!inPart(f,p,true)||endpoints.some(e=>e.join()===p.join()))continue;
for(let n=1;n<=15;n++){let r0=cross(p,[1n,BigInt(n),BigInt(n*n+1)]);if(!r0.some(Boolean)||staticRays.some(e=>dot(r0,e)===0n))continue;
let side=sg(dot(r0,a));if(!side||side!==sg(dot(r0,b)))continue;
let k=1n;for(let e of staticRays)if(abs(dot(p,e))>=k)k=abs(dot(p,e))+1n;
let r1=r0.map((x,i)=>k*x+p[i]),r2=r0.map((x,i)=>k*x-p[i]);if(signKey(r1,staticRays)!==signKey(r2,staticRays))continue;
let part=f.parts.find(([u,v])=>dot(r0,u)*dot(r0,v)<0n);if(!part)continue;
let clip=r=>{let [u,v]=part,A=dot(r,u),B=dot(r,v);if(A*B>=0n)throw Error("cross");return norm(A<0n?u.map((x,i)=>B*x-A*v[i]):v.map((x,i)=>A*x-B*u[i]))};
let p1=clip(r1),p2=clip(r2),d1=dot(cross(a,b),p1),d2=dot(cross(a,b),p2);if(d1*d2>=0n)continue;
witness={support:f.l,static:[a,b],rootEvent:p,root1:norm(r1),root2:norm(r2),clipped1:p1,clipped2:p2,det1:d1,det2:d2,childSign:side,commonSignVector:signKey(r1,endpoints)};break outer;
}}
if(!witness)throw Error("no witness");
let result={segments,changes,supports:active.length,components:active.reduce((s,f)=>s+f.parts.length,0),splitSupports:active.filter(f=>f.parts.length>1).map(f=>({normal:f.l,components:f.parts})),oldEndpoints:old.length,componentEndpoints:endpoints.length,staticWithAxes:staticRays.length,connectorLines:connector.size,connectorSupportChecks:checks,oneDynamicEventRays:evOne.size,twoDynamicEventRays:evTwo.size,twoDynamicInteriorBoth:insideBoth.size,totalEventRays:events.size,newVsOld:[...events.keys()].filter(k=>!old.some(p=>p.join()===k)).length,witness};
return JSON.parse(JSON.stringify(result,(_,v)=>typeof v==="bigint"?String(v):v));
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
console.log(JSON.stringify(replay(data),null,2));
```

Next: use lazy subdivision of only the 393 surviving R178 root classes, with event signs as the exact first-clipped residual quotient. Evaluate representatives of nonempty strata, including lower-dimensional zero strata. Use R179 capacity recursion for uniform exclusions. Avoid enumerating the full global arrangement blindly: first test which event rays can actually vary inside each old class; the present event count is a safe global upper carrier, not a minimal per-class carrier. No owner/Activity mutation made in this round; current live identity unconfirmed.
