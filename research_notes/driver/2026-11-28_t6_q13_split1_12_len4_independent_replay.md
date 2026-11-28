# T6 q13 split (1,12), negative length 4: independent exact replay

2026-11-28, original informed Driver lane EM-DVR-DEBB5E. Continues 7ab22f8ee19772fab74f458818c716e4a78bfbb3 (lengths 1–3). Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Source 45b97058c2b6f51eaee8af00d1ba5862547641c0. Shared basis from 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json blob bcab5ce85b368d2b65a74340ceadb4527da0f01e; author comparison certificate research_checks/T6_P13_Q13_SPLIT1_12_LEN4_AUTHOR_EXACT_CERT_20261126.json blob 1eb570c266931532c1f5ac87f23bcee83119b669.

## Scope and proof
All 15 unordered partitions of 12 of length exactly 4, all 12 positive labels and all nondecreasing labels within equal negative q groups. Include common atoms. Reject only if a high mass exceeds 2331, then enumerate the exact affine coset subject to weighted squared norm <= (2331-m_plus)^2+(2331-m_minus)^2, a necessary condition from separate side L1 bounds. Six mixed congruences use the negative inverse-power sum minus positive inverse-power sum modulo 13^k. The prior Vandermonde digit lift gives full mixed-modulus image and hence kernel index 13^21. This run separately checks every basis row, determinant, lift and rational Gram–Schmidt; min squared length exceeds 2*2331^2, so the descending coordinate interval has radius <1 and floor(center) and its successor exhaust possible integers, with exact scaled squared norm inequalities. All candidate counts and nodes are computed here, compared only after enumerating each pattern. No feasible leaves; thus these 15 patterns are excluded even without smoothness. No H0, lower-prime completion, observer implication, blind independence, native formal review or Result acceptance claimed. Independent implementation reused from Driver's preceding audit; shared basis and author comparison counts.

## Actual output
```json
{
  "rows": [
    {
      "neg_pattern": [
        1,
        1,
        1,
        9
      ],
      "raw": 52416,
      "search": 19428,
      "over": 32988,
      "common_included": 11232,
      "common_feasible": 4110,
      "nodes": 46542,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        1,
        2,
        8
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 20736,
      "common_feasible": 7535,
      "nodes": 117836,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        1,
        3,
        7
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 20736,
      "common_feasible": 7535,
      "nodes": 116839,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        1,
        4,
        6
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 20736,
      "common_feasible": 7535,
      "nodes": 116619,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        1,
        5,
        5
      ],
      "raw": 73008,
      "search": 26880,
      "over": 46128,
      "common_included": 11232,
      "common_feasible": 4110,
      "nodes": 64094,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        2,
        2,
        7
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 11232,
      "common_feasible": 4110,
      "nodes": 117052,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        2,
        3,
        6
      ],
      "raw": 248832,
      "search": 90420,
      "over": 158412,
      "common_included": 20736,
      "common_feasible": 7535,
      "nodes": 214274,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        2,
        4,
        5
      ],
      "raw": 248832,
      "search": 90420,
      "over": 158412,
      "common_included": 20736,
      "common_feasible": 7535,
      "nodes": 214870,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        3,
        3,
        5
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 11232,
      "common_feasible": 4110,
      "nodes": 116597,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        1,
        3,
        4,
        4
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 11232,
      "common_feasible": 4110,
      "nodes": 116731,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        2,
        2,
        2,
        6
      ],
      "raw": 52416,
      "search": 19428,
      "over": 32988,
      "common_included": 0,
      "common_feasible": 0,
      "nodes": 46372,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        2,
        2,
        3,
        5
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 0,
      "common_feasible": 0,
      "nodes": 117008,
      "leaves": 0,
      "valid": 0
    },
    {
      "neg_pattern": [
        2,
        2,
        4,
        4
      ],
      "raw": 73008,
      "search": 26880,
      "over": 46128,
      "common_included": 0,
      "common_feasible": 0,
      "nodes": 63602,
      "leaves": 1,
      "valid": 0
    },
    {
      "neg_pattern": [
        2,
        3,
        3,
        4
      ],
      "raw": 134784,
      "search": 49320,
      "over": 85464,
      "common_included": 0,
      "common_feasible": 0,
      "nodes": 116828,
      "leaves": 1,
      "valid": 0
    },
    {
      "neg_pattern": [
        3,
        3,
        3,
        3
      ],
      "raw": 16380,
      "search": 6168,
      "over": 10212,
      "common_included": 0,
      "common_feasible": 0,
      "nodes": 14631,
      "leaves": 0,
      "valid": 0
    }
  ],
  "totals": {
    "raw": 1843164,
    "search": 674184,
    "over": 1168980,
    "common_included": 159840,
    "common_feasible": 58225,
    "nodes": 1599895,
    "leaves": 2,
    "valid": 0
  },
  "min": "78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349",
  "det": "247064529073450392704413",
  "field_checks": 120
}
```

## Reproduction
Load U0 and cert from the two pinned JSON inputs above, call audit(U0,cert).
```js
function audit(U0,cert){
const P=13n,B=P**6n,N=12,C=2331n;
const abs=a=>a<0n?-a:a,mod=(a,m)=>(a%m+m)%m,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a},lcm=(a,b)=>a/gcd(a,b)*b;
const f=(a,b=1n)=>{if(!b)throw Error("division");if(b<0n){a=-a;b=-b}let d=gcd(a,b);return [a/d,b/d]},add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),sum=a=>a.reduce(add,f(0n));
const floor=(a,b)=>a/b-(a<0n&&a%b?1n:0n);
const inv=(a,m)=>{let b=m,x=1n,y=0n;a=mod(a,m);while(b){let q=a/b;[a,b]=[b,a-q*b];[x,y]=[y,x-q*y]}if(a!==1n)throw Error("unit");return mod(x,m)};
const H=Array.from({length:6},(_,k)=>Array.from({length:N},(_,i)=>inv(BigInt(i+1)**BigInt(k+1),P**BigInt(k+1))));
const U=U0.map(r=>r.map(BigInt)),W=Array.from({length:N},(_,i)=>P*BigInt(i+1)-1n);
const check=(v,t)=>H.every((h,k)=>mod(h.reduce((s,a,i)=>s+a*v[i],0n)-t[k],P**BigInt(k+1))===0n);
for(let u of U)if(!check(u,Array(6).fill(0n)))throw Error("kernel");
let A=U.map((r,i)=>[...r.map(x=>f(x)),...Array.from({length:N},(_,j)=>f(BigInt(i===j)))]),det=f(1n);
for(let i=0;i<N;i++){let j=A.findIndex((r,k)=>k>=i&&r[i][0]);if(j<0)throw Error("singular");if(i!==j){[A[i],A[j]]=[A[j],A[i]];det=mul(det,f(-1n))}let p=A[i][i];det=mul(det,p);A[i]=A[i].map(x=>div(x,p));for(let j=0;j<N;j++)if(j!==i){let c=A[j][i];A[j]=A[j].map((x,k)=>sub(x,mul(c,A[i][k])))}}
if(det[1]!==1n||abs(det[0])!==P**21n)throw Error("det");
const UI=A.map(r=>r.slice(N));
function lift(t){let x=Array(N).fill(0n);for(let j=0;j<6;j++){let q=P**BigInt(j),m=6-j;let a=H.slice(j).map((h,k)=>{let d=t[j+k]-h.reduce((s,v,i)=>s+v*x[i],0n);if(d%q)throw Error("lift residue");return [...h.slice(0,m).map(v=>mod(v,P)),mod(d/q,P)]});for(let k=0;k<m;k++){let l=a.findIndex((r,i)=>i>=k&&r[k]);if(l<0)throw Error("rank");[a[k],a[l]]=[a[l],a[k]];let s=inv(a[k][k],P);a[k]=a[k].map(v=>mod(v*s,P));for(let i=0;i<m;i++)if(i!==k){let c=a[i][k];a[i]=a[i].map((v,h)=>mod(v-c*a[k][h],P))}}for(let i=0;i<m;i++)x[i]+=q*a[i][m]}if(!check(x,t))throw Error("lift check");return x}
const coords=new Map();for(let q=1;q<=12;q++)for(let r=1;r<=12;r++){let t=Array.from({length:6},(_,k)=>inv(BigInt(13*q+r)**BigInt(k+1),P**BigInt(k+1)));let x=lift(t);let v=Array.from({length:N},(_,i)=>sum(x.map((a,j)=>mul(f(a),UI[j][i]))));coords.set(q*100+r,v.map(a=>{let b=mul(a,f(B));if(b[1]!==1n)throw Error("denominator");return mod(b[0],B)}))}
const dot=(a,b)=>sum(a.map((v,i)=>mul(v,b[i]))),V=[],D=[],mu=[];
for(let i=0;i<N;i++){let r=U[i].map((x,j)=>f(x*W[j])),v=r.slice(),m=[];for(let j=0;j<i;j++){let c=div(dot(r,V[j]),D[j]);m.push(c);v=v.map((x,k)=>sub(x,mul(c,V[j][k])))}V.push(v);D.push(dot(v,v));mu.push(m)}
const min=D.reduce((a,b)=>a[0]*b[1]<b[0]*a[1]?a:b);
if(min[0]<=2n*C*C*min[1])throw Error("GS bound");
const L=D.map((_,i)=>mu.slice(i+1).reduce((s,r)=>lcm(s,r[i][1]),1n)),coef=D.map((_,i)=>mu.slice(i+1).map(r=>r[i][0]*(L[i]/r[i][1]))),K=D.map((d,i)=>div(d,f((B*L[i])**2n))),Q=K.reduce((s,k)=>lcm(s,k[1]),1n),T=K.map(k=>k[0]*(Q/k[1]));
const fields=["raw","search","over","common_included","common_feasible","nodes","leaves","valid"];
const rows=[];
function* parts(n,lo=1){if(!n){yield [];return}for(let q=lo;q<=n;q++)for(let r of parts(n-q,q))yield [q,...r]}
const patterns=[...parts(12)].filter(p=>p.length===4);
for(let pat of patterns){let row={neg_pattern:pat,...Object.fromEntries(fields.map(k=>[k,0]))};
function walk(rs){if(rs.length<pat.length){let i=rs.length,lo=i&&pat[i]===pat[i-1]?rs[i-1]:1;for(let r=lo;r<=12;r++)walk([...rs,r]);return}
let mn=rs.reduce((s,r,i)=>s+P*BigInt(13*pat[i]+r)-1n,0n);
let neg=Array(N).fill(0n);for(let j=0;j<rs.length;j++){let v=coords.get(pat[j]*100+rs[j]);neg=neg.map((x,i)=>mod(x+v[i],B))}
for(let p=1;p<=12;p++){row.raw++;let common=rs.some((r,i)=>pat[i]===1&&r===p);if(common)row.common_included++;let mp=P*BigInt(13+p)-1n;if(mn>C||mp>C){row.over++;continue}row.search++;if(common)row.common_feasible++;
let c=neg.map((x,i)=>mod(x-coords.get(100+p)[i],B)),z=c.slice(),bound=((C-mp)**2n+(C-mn)**2n)*Q;
function dfs(i,spent){if(i<0){row.leaves++;let u=Array.from({length:N},(_,j)=>{let a=z.reduce((s,v,k)=>s+v*U[k][j],0n);if(a%B)throw Error("integrality");return a/B});let rhs=Array.from({length:6},(_,k)=>rs.reduce((s,r,j)=>s+inv(BigInt(13*pat[j]+r)**BigInt(k+1),P**BigInt(k+1)),-inv(BigInt(13+p)**BigInt(k+1),P**BigInt(k+1))));if(!check(u,rhs))throw Error("leaf congruence");let pp=mp+u.reduce((s,v,j)=>s+(v>0n?v*W[j]:0n),0n),nn=mn+u.reduce((s,v,j)=>s+(v<0n?-v*W[j]:0n),0n);if(pp<=C&&nn<=C)row.valid++;return}
row.nodes++;let h=L[i]*c[i]+coef[i].reduce((s,v,j)=>s+v*z[i+1+j],0n),step=B*L[i],n0=floor(-h,step);for(let n of [n0,n0+1n]){let cost=T[i]*(h+step*n)**2n;if(spent+cost<=bound){z[i]=c[i]+B*n;dfs(i-1,spent+cost)}}z[i]=c[i]}
dfs(N-1,0n)
}}
walk([]);let orig=cert.rows.find(r=>r.neg_pattern.join()===pat.join());if(!orig)throw Error("missing row");
for(let k of fields)if(row[k]!==orig[k])throw Error("mismatch "+JSON.stringify({pat,k,ours:row[k],orig:orig[k]}));rows.push(row)}
if(rows.length!==cert.rows.length)throw Error("coverage");
return {rows,totals:Object.fromEntries(fields.map(k=>[k,rows.reduce((s,r)=>s+r[k],0)])),min:min.join("/"),det:abs(det[0]).toString(),field_checks:fields.length*rows.length}
}
console.log(JSON.stringify(audit(U0,cert),null,2));
```
