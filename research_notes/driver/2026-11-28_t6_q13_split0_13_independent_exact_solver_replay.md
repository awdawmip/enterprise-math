# T6 q13 split (0,13): independent exact affine-search replay

2026-11-28; same informed Driver lane, prior identity EM-DVR-DEBB5E / MCP-9b4714dc46b948afa4875a86c89c713c. Shared frozen science and author's lattice basis; independent implementation of affine representative lifting, vector Gram–Schmidt and exact interval enumeration. Not a blind study or native Review. Author EM-DIRECT-D03BC9. Input 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json, Git blob bcab5ce85b368d2b65a74340ceadb4527da0f01e. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Author implementation at 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_PORTABLE_20261126/q13_split0_13.py.

## Scoped proposition and proof
For every relaxed negative high-atom roster (q,r) with q>=1, 1<=r<=12, sum q=13, no positive high atom, side cap 2331, there is no integer u in Z^12 satisfying the six congruences sum_r u_r r^{-k} = sum_(q,r) (13q+r)^{-k} mod 13^k (k=1..6) and both weighted side budgets, with w_r=13r-1 and high atom cost 13(13q+r)-1. A necessary budget condition is high cost c<=2331. Its exact roster bound is sum r <= floor((2331-169*13+length)/13). If u satisfies both budgets, weighted squared norm <=2331^2+(2331-c)^2, by sum of squares <=square of sum separately on positive and negative coordinates. The 101 unordered q partitions exhaust sum q=13; within each equal-q group use nondecreasing labels. The modular constraint map has kernel index 13^21: digit lifting from j=0..5 can solve the remaining 6-j rows over F13, using the first 6-j columns; the square matrices are Vandermonde times nonzero column factors. Thus it is onto the product of six residue rings. The supplied U rows lie in the kernel and have absolute determinant 13^21, hence form its exact basis. The implementation verifies these facts, computes cosets independently via digit lifting, and uses exact rational vector orthogonalization to compute the norm form. Backwards enumeration at coordinate i uses the full integer interval ceil((-b-h)/step) through floor((b-h)/step), where b=floor(sqrt((bound-spent)/T_i)). This is equivalent to the integer quadratic inequality and does not assume the author's two-nearest shortcut. All arithmetic is BigInt/rational, including integer square roots. No leaves occur. This proves the scoped six-congruence relaxed search exclusion; true smooth restriction is a subset. The original observation-envelope implication (including lower-prime completion and H0) and other splits are not established here.

## Execution results
{
  "totals": {
    "raw": 114945780,
    "search": 7003,
    "smooth": 1368,
    "nodes": 19271,
    "leaves": 0,
    "valid": 0
  },
  "det": "247064529073450392704413",
  "min": "78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349",
  "partitions": 101
}
All 101 rows match author raw/search/nodes/leaves/valid (505 field comparisons). Smooth count refers only to high-atom rosters under the side mass bound. No formal acceptance or Task closure.

## Reproduction
Load exact input JSON as cert, then run the following standalone JavaScript function. The output includes all 101 rows.
```js
function audit(cert){
const P=13n,B=13n**6n,N=12,CAP=2331n;
const abs=x=>x<0n?-x:x,mod=(x,m)=>(x%m+m)%m,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a},lcm=(a,b)=>a/gcd(a,b)*b;
const f=(a,b=1n)=>{if(!b)throw Error("zero divisor");if(b<0n){a=-a;b=-b}let g=gcd(a,b);return [a/g,b/g]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sum=a=>a.reduce(add,f(0n));
const floor=(a,b)=>{let q=a/b;return a<0n&&a%b?q-1n:q},ceil=(a,b)=>-floor(-a,b);
const inv=(a,m)=>{let b=m,x=1n,y=0n;a=mod(a,m);while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y]}if(a!==1n)throw Error("not unit");return mod(x,m)};
const H=Array.from({length:6},(_,k)=>Array.from({length:N},(_,r)=>inv(BigInt(r+1)**BigInt(k+1),P**BigInt(k+1))));
const W=Array.from({length:N},(_,r)=>P*BigInt(r+1)-1n),U=cert.U.map(a=>a.map(BigInt));
const check=(v,t)=>H.every((h,k)=>mod(h.reduce((s,a,i)=>s+a*v[i],0n)-t[k],P**BigInt(k+1))===0n);
for(const u of U)if(!check(u,Array(6).fill(0n)))throw Error("basis residue");
let A=U.map((row,i)=>[...row.map(x=>f(x)),...Array.from({length:N},(_,j)=>f(BigInt(i===j)))]);
let det=f(1n);
for(let i=0;i<N;i++){let j=A.findIndex((row,k)=>k>=i&&row[i][0]);if(j<0)throw Error("singular");if(j!==i){[A[j],A[i]]=[A[i],A[j]];det=mul(det,f(-1n))}let p=A[i][i];det=mul(det,p);A[i]=A[i].map(a=>div(a,p));for(let j=0;j<N;j++)if(j!==i){let c=A[j][i];A[j]=A[j].map((a,k)=>sub(a,mul(c,A[i][k])))}}
if(det[1]!==1n||abs(det[0])!==P**21n)throw Error("basis index");
const UI=A.map(r=>r.slice(N));
function lift(t){let x=Array(N).fill(0n);
 for(let j=0;j<6;j++){let q=P**BigInt(j),m=6-j;let a=H.slice(j).map((h,k)=>{let d=t[j+k]-h.reduce((s,v,i)=>s+v*x[i],0n);if(d%q)throw Error("lift residual");return [...h.slice(0,m).map(v=>mod(v,P)),mod(d/q,P)]});
 for(let k=0;k<m;k++){let l=a.findIndex((r,i)=>i>=k&&r[k]!==0n);if(l<0)throw Error("modular rank");[a[k],a[l]]=[a[l],a[k]];let s=inv(a[k][k],P);a[k]=a[k].map(v=>mod(v*s,P));for(let i=0;i<m;i++)if(i!==k){let c=a[i][k];a[i]=a[i].map((v,h)=>mod(v-c*a[k][h],P))}}
 for(let i=0;i<m;i++)x[i]+=q*a[i][m];
 }if(!check(x,t))throw Error("lift failed");return x}
const coords=new Map();
for(let q=1;q<=13;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));let x=lift(t);let v=Array.from({length:N},(_,i)=>sum(x.map((a,j)=>mul(f(a),UI[j][i]))));coords.set(q*100+r,v.map(a=>{let b=mul(a,f(B));if(b[1]!==1n)throw Error("denominator");return mod(b[0],B)}))}
const R=U.map(u=>u.map((v,i)=>v*W[i]));const dot=(a,b)=>a.reduce((s,v,i)=>add(s,mul(v,b[i])),f(0n));
// Direct vector orthogonalization, not Gram-matrix recursion.
const V=[],D=[],mu=[];
for(let i=0;i<N;i++){let r=R[i].map(x=>f(x)),v=r.slice(),m=[];for(let j=0;j<i;j++){let c=div(dot(r,V[j]),D[j]);m.push(c);v=v.map((x,k)=>sub(x,mul(c,V[j][k])))}V.push(v);D.push(dot(v,v));mu.push(m)}
let min=D.reduce((a,b)=>a[0]*b[1]<b[0]*a[1]?a:b);
if(min[0]<=2n*CAP*CAP*min[1])throw Error("GS lower bound");
if(min.join("/")!==cert.gs_min_sq)throw Error("GS source mismatch");
const L=D.map((_,i)=>mu.slice(i+1).reduce((s,r)=>lcm(s,r[i][1]),1n));
const coeff=D.map((_,i)=>mu.slice(i+1).map(r=>r[i][0]*(L[i]/r[i][1])));
const K=D.map((d,i)=>div(d,f((B*L[i])**2n))),Q=K.reduce((s,k)=>lcm(s,k[1]),1n),T=K.map(k=>k[0]*(Q/k[1]));
const sqrt=x=>{if(x<0n)throw Error("negative sqrt");if(x<2n)return x;let a=1n<<BigInt(Math.ceil(x.toString(2).length/2));while(true){let b=(a+x/a)/2n;if(b>=a)return a;a=b}};
let nodes=0,leaves=0,valid=0;
function search(pat,rs){let c=Array(N).fill(0n),mass=0n;for(let j=0;j<pat.length;j++){let v=coords.get(100*pat[j]+rs[j]);c=c.map((x,i)=>mod(x+v[i],B));mass+=P*BigInt(13*pat[j]+rs[j])-1n}
 let radius=CAP*CAP+(CAP-mass)**2n,bound=radius*Q,z=c.slice();
 function dfs(i,spent){if(i<0){leaves++;let u=Array.from({length:N},(_,t)=>{let a=z.reduce((s,v,j)=>s+v*U[j][t],0n);if(a%B)throw Error("noninteger");return a/B});
 let t=Array.from({length:6},(_,k)=>pat.reduce((s,q,j)=>s+inv(BigInt(13*q+rs[j])**BigInt(k+1),P**BigInt(k+1)),0n));if(!check(u,t))throw Error("wrong leaf");
 let mp=u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),mn=mass+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);
 if(mp<=CAP&&mn<=CAP)valid++;return}
 nodes++;let h=L[i]*c[i]+coeff[i].reduce((s,v,j)=>s+v*z[i+1+j],0n),step=B*L[i],b=sqrt((bound-spent)/T[i]);
 for(let n=ceil(-b-h,step);n<=floor(b-h,step);n++){z[i]=c[i]+B*n;dfs(i-1,spent+T[i]*(h+step*n)**2n)}z[i]=c[i];
 }dfs(N-1,0n)}
function* parts(n,lo=1){if(!n){yield [];return}for(let i=lo;i<=n;i++)for(const r of parts(n-i,i))yield [i,...r]}
const choose=(n,k)=>{let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-i+1)/BigInt(i);return a};
const smooth=x=>{for(const p of [2,3,5,7,11,13])while(x%p===0)x/=p;return x===1};
const rows=[],certMap=new Map(cert.rows.map(r=>[r.neg_pattern.join(","),r]));
if(certMap.size!==cert.rows.length)throw Error("duplicate");
for(const pat of parts(13)){let raw=1n;for(const q of new Set(pat))raw*=choose(11+pat.filter(x=>x===q).length,pat.filter(x=>x===q).length);
 let seen=0,sm=0,prev=[nodes,leaves,valid],limit=Math.floor((2331-169*13+pat.length)/13);
 function walk(rs,s){if(rs.length===pat.length){seen++;if(pat.every((q,j)=>smooth(13*q+rs[j])))sm++;search(pat,rs);return}let i=rs.length,lo=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=lo;r<=12&&s+r+pat.length-i-1<=limit;r++)walk([...rs,r],s+r)}
 walk([],0);let orig=certMap.get(pat.join(",")),row={pat,raw:Number(raw),search:seen,smooth:sm,nodes:nodes-prev[0],leaves:leaves-prev[1],valid:valid-prev[2]};
 if(!orig||row.raw!==orig.raw||row.search!==orig.search||row.nodes!==orig.nodes||row.leaves!==orig.leaves||row.valid!==orig.valid)throw Error("row mismatch "+JSON.stringify(row));
 rows.push(row)}
 if(rows.length!==101||rows.length!==certMap.size)throw Error("coverage");
 return {rows,totals:Object.fromEntries(["raw","search","smooth","nodes","leaves","valid"].map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),det:det[0].toString(),min:min.join("/")}
}
console.log(JSON.stringify(audit(cert),null,2));
```
