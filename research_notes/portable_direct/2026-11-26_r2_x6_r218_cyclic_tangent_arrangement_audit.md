# X6 R218 — independent cyclic tangent-sector replay of both sign arrangements

2026-11-26. AUTHOR CROSS-IMPLEMENTATION CHECK / NOT_REVIEWED. Same frozen static six-pair BRC model as R216/R217. P000 V5 retained; auxiliary coefficient geometry only. No native Task/CLAIM mutation. Source 4765928190367b00d1e8a19e4a27d952897e4f98:research_notes/portable_direct/2026-11-25_r2_x6_r178_recursive_endpoint_capacity.md, blob aaca3d6e3cb979dbab76bded956284e11ecd07a3; R213 e39b9de2671fc0ba71a2ca03f89b74670f19d0e5; R216 0b5f89c35844559a07c3cd49c25f882ae1c7472f. This audit checks the arrangement and generator construction, not the full capacity replay or formal independent review.

## Alternate enumeration proof

For a finite rank-three list of nonzero normal rays, the sign classes on the nonzero coefficient vectors are the relatively open faces of its central hyperplane arrangement. The closure of each is a pointed polyhedral cone (if both x and -x belong to its closure, every normal annihilates x, hence x=0). Every extreme ray lies on two independent arrangement walls; each nonzero face closure has an extreme ray. Conversely each arrangement vertex ray compatible with a face closure is an extreme ray of that closure: its two independent zero walls are either boundary constraints or identically zero on the face, and their intersection is one-dimensional. Thus the complete set of extreme rays can be collected from local incidences at all vertices.

At each projective vertex v, take the signed primitive tangents ±(v cross p) for every incident normal p and deduplicate them. These are exactly the wall rays in the two-dimensional auxiliary tangent coordinate space. There are at least two distinct wall lines, so consecutive oriented tangents in their exact cyclic ordering have angular gap strictly less than a half-turn. Their positive sum lies strictly inside the intervening sector. A lexicographic sign test at (v,t) enumerates the arc for a tangent, and at (v,t+u) enumerates the chamber for consecutive tangents. Nonincident signs remain those of v. Include the vertex itself and quotient by simultaneous sign reversal. This gives every face and collects exactly its extreme rays (not merely a representative ray). It is an alternative to R213's three-stage (vertex,tangent,wall normal) perturbation, requiring only exact cyclic orientation and two-stage signs.

The implementation checks strict consecutive orientation and that each sector sample avoids every incident wall. It compares complete ternary sign keys AND each oriented primitive generator set against the original three-stage construction; it checks that the sum of each generator set is in its declared relative interior. For 51 endpoint rays, the independent census is 1028 rank-one, 2124 rank-two and 1097 rank-three classes, total 4249. For 47 support normals it is 821,1722,902, total 3445 antipodal nonzero classes. Both exact comparisons have zero mismatches, supporting the R213 projection-bank coverage premise. No original capacity solver was rerun. All original endpoint and support labels are retained.

## Actual result
```json
{
  "P": {
    "normals": 51,
    "vertices": 1028,
    "tangentIncidences": 4248,
    "wedges": 4248,
    "classes": 4249,
    "byRank": [
      1028,
      2124,
      1097
    ],
    "oldClasses": 4249,
    "signMismatches": 0,
    "generatorSetMismatches": 0
  },
  "N": {
    "normals": 47,
    "vertices": 821,
    "tangentIncidences": 3444,
    "wedges": 3444,
    "classes": 3445,
    "byRank": [
      821,
      1722,
      902
    ],
    "oldClasses": 3445,
    "signMismatches": 0,
    "generatorSetMismatches": 0
  }
}
```

## Standalone exact replay
```javascript
function auditBoth(data){
 const d=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0n),c=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],neg=a=>a.map(x=>-x),sg=x=>x>0n?1:x<0n?-1:0,add=(a,b)=>a.map((x,i)=>x+b[i]),gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a,prim=a=>{let g=a.reduce(gcd,0n);return a.map(x=>x/g)},orient=a=>{a=prim(a);return a.find(x=>x!==0n)<0n?neg(a):a},key=a=>a.join(),unique=a=>[...new Map(a.map(x=>[key(x),x])).values()];
 function audit(P){
 const V=unique(P.flatMap((p,i)=>P.slice(i+1).map(q=>c(p,q))).filter(v=>v.some(Boolean)).map(orient)),faces=new Map(),old=new Map();
 function record(map,v,s){let a=key(s),b=key(neg(s));if(b<a){a=b;v=neg(v)}if(!map.has(a))map.set(a,new Set());map.get(a).add(key(v))}
 let rayInc=0,wedges=0;
 for(const v of V){
  const I=P.filter(p=>!d(v,p)),base=P.map(p=>sg(d(v,p)));record(faces,v,base);record(old,v,base);
  const T=unique(I.flatMap(p=>{let t=prim(c(v,p));return [t,neg(t)]})); const x=T[0],y=c(v,x);
  const half=t=>d(y,t)>0n||d(y,t)===0n&&d(x,t)>0n?0:1;
  T.sort((a,b)=>half(a)-half(b)||-sg(d(v,c(a,b))));
  for(let i=0;i<T.length;i++){let t=T[i],u=T[(i+1)%T.length];if(d(v,c(t,u))<=0n)throw Error("bad cyclic order");const mid=add(t,u);const s=P.map((p,j)=>base[j]||sg(d(t,p))),z=P.map((p,j)=>base[j]||sg(d(mid,p)));record(faces,v,s);record(faces,v,z);rayInc++;wedges++;if(I.some(p=>!d(mid,p)))throw Error("interior tangent on wall")}
  for(const p of I)for(const sign of [-1n,1n]){const t=c(v,p).map(x=>x*sign);record(old,v,P.map((p,j)=>base[j]||sg(d(t,p))));for(const u of [-1n,1n])record(old,v,P.map((q,j)=>base[j]||sg(d(t,q))||sg(u*d(p,q))))}
 }
 let mismatch=0,extremeMismatch=0;for(const [k,a] of faces){let b=old.get(k);if(!b){mismatch++;continue}if(a.size!==b.size||[...a].some(x=>!b.has(x)))extremeMismatch++}for(const k of old.keys())if(!faces.has(k))mismatch++;
 let ranks=[0,0,0,0];for(const [k,a] of faces){let s=k.split(",").map(Number),Z=P.filter((p,i)=>s[i]===0),rank=Z.length===0?3:Z.some(p=>c(Z[0],p).some(Boolean))?1:2;ranks[rank]++;const v=[...a].map(x=>x.split(",").map(BigInt)).reduce(add,[0n,0n,0n]);if(key(P.map(p=>sg(d(v,p))))!==k)throw Error("generator sum not in relative interior")}
 return {normals:P.length,vertices:V.length,tangentIncidences:rayInc,wedges,classes:faces.size,byRank:ranks.slice(1),oldClasses:old.size,signMismatches:mismatch,generatorSetMismatches:extremeMismatch}
 }
 return {P:audit(unique(data.flatMap(x=>x.endpoints.map(p=>p.map(BigInt))))),N:audit(data.map(x=>x.normal.map(BigInt)))};
}
const data=[{"normal":["187","12","-1"],"segments":9,"endpoints":[["0","1","12"],["1","17","391"]]},{"normal":["204","11","-1"],"segments":9,"endpoints":[["0","1","11"],["1","17","391"]]},{"normal":["5","-2","0"],"segments":51,"endpoints":[["2","5","73"],["2","5","5"]]},{"normal":["9","-1","0"],"segments":4,"endpoints":[["1","9","74"],["1","9","69"]]},{"normal":["85","7","-2"],"segments":10,"endpoints":[["1","9","74"],["3","17","187"]]},{"normal":["51","2","-1"],"segments":9,"endpoints":[["1","9","69"],["1","0","51"]]},{"normal":["0","1","-1"],"segments":2,"endpoints":[["2","5","5"],["1","0","0"]]},{"normal":["34","1","-1"],"segments":7,"endpoints":[["2","5","73"],["1","0","34"]]},{"normal":["187","20","-9"],"segments":5,"endpoints":[["6","15","158"],["1","1","23"]]},{"normal":["68","1","-3"],"segments":8,"endpoints":[["2","5","47"],["3","0","68"]]},{"normal":["176","22","-9"],"segments":4,"endpoints":[["6","15","154"],["19","28","440"]]},{"normal":["22","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","22"]]},{"normal":["61","0","-1"],"segments":78,"endpoints":[["0","1","0"],["1","17","61"]]},{"normal":["74","0","-1"],"segments":14,"endpoints":[["1","9","74"],["1","4","74"]]},{"normal":["126","0","-1"],"segments":103,"endpoints":[["0","1","0"],["1","30","126"]]},{"normal":["4","-1","0"],"segments":35,"endpoints":[["1","4","152"],["1","4","74"]]},{"normal":["17","-1","0"],"segments":44,"endpoints":[["0","0","1"],["1","17","22"]]},{"normal":["156","-1","-1"],"segments":46,"endpoints":[["1","4","152"],["1","30","126"]]},{"normal":["69","0","-1"],"segments":16,"endpoints":[["1","17","69"],["1","9","69"]]},{"normal":["9","0","-1"],"segments":47,"endpoints":[["0","1","0"],["1","17","9"]]},{"normal":["235","0","-3"],"segments":84,"endpoints":[["0","1","0"],["3","77","235"]]},{"normal":["87","0","-1"],"segments":107,"endpoints":[["0","1","0"],["1","17","87"]]},{"normal":["104","-1","-1"],"segments":60,"endpoints":[["1","4","100"],["3","77","235"]]},{"normal":["38","0","-3"],"segments":57,"endpoints":[["0","1","0"],["3","40","38"]]},{"normal":["5","0","-2"],"segments":72,"endpoints":[["0","1","0"],["2","5","5"]]},{"normal":["39","-1","-1"],"segments":50,"endpoints":[["3","1","116"],["1","17","22"]]},{"normal":["40","0","-3"],"segments":63,"endpoints":[["0","1","0"],["3","38","40"]]},{"normal":["26","-1","-1"],"segments":39,"endpoints":[["2","5","47"],["3","53","25"]]},{"normal":["25","0","-3"],"segments":52,"endpoints":[["0","1","0"],["3","53","25"]]},{"normal":["83","0","-2"],"segments":69,"endpoints":[["0","1","0"],["2","34","83"]]},{"normal":["102","-7","-1"],"segments":14,"endpoints":[["1","4","74"],["3","17","187"]]},{"normal":["204","-11","1"],"segments":51,"endpoints":[["0","1","11"],["1","30","126"]]},{"normal":["395","0","-2"],"segments":119,"endpoints":[["0","1","0"],["2","73","395"]]},{"normal":["289","18","-1"],"segments":10,"endpoints":[["0","1","18"],["1","17","595"]]},{"normal":["66","2","-1"],"segments":11,"endpoints":[["1","4","74"],["1","0","66"]]},{"normal":["132","5","-1"],"segments":16,"endpoints":[["1","17","217"],["1","0","132"]]},{"normal":["44","1","-1"],"segments":9,"endpoints":[["1","17","61"],["1","11","55"]]},{"normal":["88","3","-1"],"segments":7,"endpoints":[["1","4","100"],["1","0","88"]]},{"normal":["88","7","-3"],"segments":5,"endpoints":[["1","17","69"],["1","11","55"]]},{"normal":["132","-7","-1"],"segments":14,"endpoints":[["1","9","69"],["1","11","55"]]},{"normal":["153","8","-1"],"segments":7,"endpoints":[["1","9","225"],["1","0","153"]]},{"normal":["153","5","-4"],"segments":1,"endpoints":[["3","1","116"],["4","0","153"]]},{"normal":["117","-2","-2"],"segments":42,"endpoints":[["2","5","112"],["2","34","83"]]},{"normal":["198","8","-1"],"segments":5,"endpoints":[["1","4","230"],["1","0","198"]]},{"normal":["198","5","-4"],"segments":11,"endpoints":[["2","8","109"],["2","0","99"]]},{"normal":["306","17","-1"],"segments":8,"endpoints":[["1","17","595"],["1","0","306"]]},{"normal":["234","-1","-1"],"segments":43,"endpoints":[["1","4","230"],["2","73","395"]]}];
console.log(JSON.stringify(auditBoth(data),null,2));
```

Next: verify the R176 active-support premises and R213 component clipping/endpoint invariant independently of the prior author code, or address R217's polynomial-sign depth-six question. Formal independent review and Activity association remain pending. Same native topic lookup as R217: no publication directory, no owner projection, no CLAIM.
