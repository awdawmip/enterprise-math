# X6 sole residual root: exact midpoint-germ refinement

2026-11-26 Driver EM-DVR-DEBB5E. Same frozen R227/R228/R229 wall relaxation and root (13,26); source 02465133d14d57ba8ae20000a5357153bf047c01, preceding independent artifact 1cef39f77d2a6d25f762f99b858e3239ecfa0991. Subdivide each clipped open interval at its primitive-ray midpoint, use both directed germs per subinterval. Every actual finite tree must retain the appropriate eventual strict signs simultaneously; thus infeasibility excludes the original root. The complete finite central arrangement face library from R229 applies to this enlarged endpoint bank, so this is exact for the refined finite relaxation, not an actual-output test. No duplicate prior exclusions. Actual results:
```json
[
  {
    "pass": false,
    "sub": 2,
    "side": 0,
    "labels": 25,
    "points": 54,
    "germs": 100,
    "rays": 1238,
    "queries": 3524,
    "checks": 298927,
    "calls": 116
  },
  {
    "pass": true,
    "sub": 2,
    "side": 1,
    "labels": 23,
    "points": 50,
    "germs": 96,
    "rays": 1075,
    "queries": 3172,
    "checks": 229633,
    "calls": 131
  }
]
```
Reproduction (input data from the pinned author file):
```js
function run(data,sub,sideIndex,cap=1500000){
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2],cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],abs=x=>x<0n?-x:x,gcd=(a,b)=>b?gcd(b,a%b):abs(a),norm=(a,ray=false)=>{let g=a.reduce(gcd,0n);if(!g)return a;if(ray&&a.find(Boolean)<0n)g=-g;return a.map(x=>x/g)},sg=x=>x>0n?1:x<0n?-1:0;
const N=data.map(e=>e.normal.map(BigInt)),parts=data.map((e,k)=>(k===5?[[[1,9,69],[3,17,187]],[[2,5,112],[1,0,51]]]:k===16?[[[0,0,1],[1,17,391]],[[1,17,69],[1,17,22]]]:[e.endpoints]).map(pair=>pair.map(p=>norm(p.map(BigInt)))));
function split(segs,q){let out=[[],[]];for(let [a,b] of segs){let A=dot(q,a),B=dot(q,b),sa=sg(A),sb=sg(B);if(sa*sb<0){let p=norm(a.map((x,k)=>abs(B)*x+abs(A)*b[k]));out[sa>0?0:1].push([a,p]);out[sb>0?0:1].push([p,b]);}else if(sa||sb)out[(sa||sb)>0?0:1].push([a,b]);}return out}
function root(i,j){let ss=[[],[]];for(let k=0;k<N.length;k++){if(k===i||k===j)continue;let [p,n]=split(parts[k],N[i]),[pp,pn]=split(p,N[j]),[np,nn]=split(n,N[j]);for(let [h,es] of [[0,[...pp,...nn]],[1,[...pn,...np]]])for(let [a,b] of es)ss[h].push({k,a,b})}return ss}
let side=root(13,26)[sideIndex];let P=[],idx=new Map(),G=[],L=new Map();function id(p){let k=p.join();if(!idx.has(k)){idx.set(k,P.length);P.push(p)}return idx.get(k)}for(let {k,a,b} of side){let pts=[];for(let j=0;j<=sub;j++)pts.push(id(norm(a.map((x,i)=>BigInt(sub-j)*x+BigInt(j)*b[i]))));for(let j=0;j<sub;j++)for(let [u,v] of [[pts[j],pts[j+1]],[pts[j+1],pts[j]]]){let bit=1n<<BigInt(G.length);G.push([u,v,bit]);L.set(k,(L.get(k)||0n)|bit)}}let rays=new Map();for(let i=0;i<P.length;i++)for(let j=i+1;j<P.length;j++){let q=norm(cross(P[i],P[j]),true);if(q.some(Boolean))rays.set(q.join(),q)}let qs=[],keys=new Set();function add(s){let a=0n,b=0n;for(let [u,v,bit] of G){let z=s[u]||s[v];if(z>0)a|=bit;else if(z<0)b|=bit}if(a>b)[a,b]=[b,a];let k=a+","+b;if(!keys.has(k)){keys.add(k);qs.push([a,b])}}for(let v of rays.values()){let sv=P.map(p=>sg(dot(v,p)));add(sv);for(let i=0;i<P.length;i++)if(!sv[i]){let w=cross(v,P[i]);let sw=P.map((p,j)=>sv[j]?0:sg(dot(w,p))),su=P.map((p,j)=>sv[j]||sw[j]?0:sg(dot(P[i],p)));for(let e of [-1,1]){add(sv.map((z,j)=>z||e*sw[j]));for(let f of [-1,1])add(sv.map((z,j)=>z||e*sw[j]||f*su[j]))}}}let memo=new Map(),cm=new Map(),calls=0,checks=0;function count(s){if(cm.has(s))return cm.get(s);let t=0;for(let m of L.values())if(s&m)t++;cm.set(s,t);return t}function rec(s,d){calls++;let c=count(s);if(c<=d)return true;if(c>(1<<d)-1)return false;let key=d+":"+s;if(memo.has(key))return memo.get(key);let lim=(1<<(d-1))-1,opts=[],seen=new Set();for(let [a,b] of qs){if(++checks>cap)throw Error("budget");let x=a&s,y=b&s;if(x>y)[x,y]=[y,x];let k=x+","+y;if(seen.has(k))continue;seen.add(k);let cx=count(x),cy=count(y);if(cx>lim||cy>lim)continue;if(cx<=d-1&&cy<=d-1){memo.set(key,true);return true}opts.push([x,y,Math.max(cx,cy),cx+cy])}opts.sort((a,b)=>a[2]-b[2]||a[3]-b[3]);for(let [x,y] of opts){if(count(x)<count(y))[x,y]=[y,x];if(rec(x,d-1)&&rec(y,d-1)){memo.set(key,true);return true}}memo.set(key,false);return false}let pass=null;try{pass=rec((1n<<BigInt(G.length))-1n,5)}catch(e){if(e.message!=="budget")throw e}return {pass,sub,side:sideIndex,labels:L.size,points:P.length,germs:G.length,rays:rays.size,queries:qs.length,checks,calls}
}
```
Execute run(data,2,0) and run(data,2,1). Null means cap, true is relaxed feasibility only. No formal Review, Result, Task or parent acceptance.
