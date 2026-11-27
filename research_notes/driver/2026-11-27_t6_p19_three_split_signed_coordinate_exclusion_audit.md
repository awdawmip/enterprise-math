# T6 p19 three-split independent signed-coordinate exclusion audit

Driver EM-DVR-DEBB5E, 2026-11-27. Nonblind independent implementation of the signed-coordinate exclusion, reusing the author's frozen integer basis and affine representatives, not a new author of the original layer proof. Original author EM-T6SM-B134BD; earlier contributor EM-T6-BFF294. Preserve their contributions and the nonterminal original RR-C428294CF760BD8D99AA/DR-0D8591E64A4073A61E6A. Input pin: 6cdc7b061d6579d6993f2fbc30d396d9a5c29047:research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/input.json, blob e2f33462b95e1f0fc4ccc5a38f3bb922a4ade388. Frozen PROOF.md blob 2928642008b2ea563954429ff7e5c8131aa4ce65. RR SHA256 4d2ebdb11a15bdc1a52a3baca99e8045188bc206414cb3e61b22153171359976.

## Mathematical test

For p=19, the 18 q0 coordinates have weights W_r=19r-1. For each positive/negative vertical state, use the frozen representative for its necessary six mixed reciprocal congruences. The integer kernel is saturated: independently checked all basis congruences and Bareiss determinant abs(det U)=19^21; first six columns are a unit Vandermonde minor modulo 19 and surject onto the six mixed moduli. Independently verify every atom representative, weighted basis, exact integer projector orthogonality and triangular entries. For any weighted completion w, signed residual budgets A,B imply A*l_i-B*h_i <= g_i·w <= A*h_i-B*l_i, with l_i=min(0,min g_i), h_i=max(0,max g_i). In affine w=v+sum z_j b_j, at reverse coordinate i only j>=i appear. Put d_i=g_i·b_i>0; maximum possible interval width (A+B)(h_i-l_i) is strictly below d_i for each of the three tested splits (verified using exact upper residual budgets). At most one integer z_i exists; use exact signed ceil and reject when it exceeds the upper bound. Every possible feasible completion must survive all coordinates. All tested pairs reject before full candidate recovery, so no final candidate norm or side cost check is needed. Unlike the original sphere norm proof, this directly uses two signed budget halfspaces; no floating point, no original candidate solver. The enumeration reproduces the complete relaxed carrier (not smooth-only), nondecreasing multiset indices and support disjointness; equal split uses k>j. All arithmetic of large integers uses BigInt. This is auxiliary exact arithmetic on the frozen BRC observer congruences, not a native physical metric or new P000 axiom.

## Actual execution result

```json
{
  "index": "714209495693373205673756419",
  "basisCongruences": 108,
  "representativeCongruences": 588,
  "atoms": 98,
  "rosters": {
    "3": 1482,
    "5": 8506,
    "6": 262
  },
  "results": [
    {
      "split": [
        6,
        6
      ],
      "pairs": 20265,
      "survive": 0,
      "depth": [
        19776,
        479,
        10,
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
        0,
        0,
        0,
        0
      ]
    },
    {
      "split": [
        3,
        6
      ],
      "pairs": 335374,
      "survive": 0,
      "depth": [
        261694,
        60124,
        11218,
        1897,
        357,
        77,
        5,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    },
    {
      "split": [
        5,
        6
      ],
      "pairs": 1513179,
      "survive": 0,
      "depth": [
        1441953,
        67647,
        3373,
        200,
        6,
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
        0,
        0
      ]
    }
  ]
}
```

Only these three branches (6,6),(3,6),(5,6) are independently exhausted by this new implementation. Remaining (4,5),(4,6),(5,5) retain original execution and prior independent domain-count evidence. No global T6 closure, formal Result admission or new CLAIM. Original reference-v3 receipt FAILED SOURCE_MAIN_CAS_RETRY_LIMIT; no replay. Current continuation dvr-20261127-2104-t6-cas-continuation-v1 and NEEDS_DISPATCH query dvr-20261127-2104-needs-dispatch-observation-v1 submitted read-only.

## Executed reproduction

Use the exact raw JSON text as input to audit(raw); do not parse large numeric tokens as Number first.

```javascript
function audit(raw) {
 const x=JSON.parse(raw.replace(/(?<!["\w])(-?\d{15,})(?!["\w])/g,'"$1"')),p=19n,n=18,B=2331;
 const assert=(q,m)=>{if(!q)throw Error(m)};
 const mat=a=>a.map(row=>row.map(BigInt)), W=Array.from({length:n},(_,i)=>p*BigInt(i+1)-1n), U=mat(x.unweighted_basis), b=mat(x.weighted_basis), G=mat(x.projector_numerators), D=x.projector_denominators.map(BigInt), R=mat(x.atom_representatives);
 const dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0n), mod=(a,m)=>((a%m)+m)%m;
 function det(A){A=A.map(a=>a.slice());let sign=1n,d=1n;for(let k=0;k<n-1;k++){if(!A[k][k]){let i=k+1;while(i<n&&!A[i][k])i++;assert(i<n,"rank");[A[k],A[i]]=[A[i],A[k]];sign=-sign}let t=A[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){let v=A[i][j]*t-A[i][k]*A[k][j];assert(v%d===0n,"Bareiss");A[i][j]=v/d}A[i][k]=0n}d=t}return sign*A[n-1][n-1]}
 const idx=det(U);assert(idx===p**21n||idx===-(p**21n),"index");
 function inv(a,m){let [r,s,t,u]=[m,mod(a,m),0n,1n];while(s){let q=r/s;[r,s,t,u]=[s,r-q*s,u,t-q*u]}assert(r===1n,"inverse");return mod(t,m)}
 for(let k=1;k<=6;k++){const m=p**BigInt(k), coeff=W.map((_,i)=>inv(BigInt(i+1),m)**BigInt(k)%m);for(const u of U)assert(mod(dot(u,coeff),m)===0n,"kernel");for(let a=0;a<R.length;a++){const [q,r]=x.atoms[a];assert(mod(dot(R[a],coeff)+inv(BigInt(19*q+r),m)**BigInt(k),m)===0n,"representative")}}
 const M=G.map(g=>b.map(v=>dot(g,v))), low=G.map(g=>g.reduce((v,t)=>t<v?t:v,0n)), high=G.map(g=>g.reduce((v,t)=>t>v?t:v,0n));
 for(let i=0;i<n;i++){assert(b[i].every((v,j)=>v===U[i][j]*W[j]),"weight");assert(M[i][i]===D[i]&&D[i]>0n,"denom");for(let j=0;j<i;j++){assert(M[i][j]===0n,"annihilation");assert(dot(G[i],G[j])===0n,"orthogonal")}}
 // Derive full signed interval bound for these splits, using actual maximum residuals.
 const A=x.atoms, expected=[];for(let q=1;q<=6;q++)for(let r=1;r<19;r++){let w=361*q+19*r-1;if(w<=B)expected.push([q,r,w])}
 assert(JSON.stringify(A)===JSON.stringify(expected),"atom carrier");
 const proj=R.map(u=>G.map(g=>dot(g,u.map((v,j)=>v*W[j]))));
 const state={};for(const q of [3,5,6]){let out=[];function rec(i,Q,c,mask,vec){if(!Q){out.push({budget:BigInt(B-c),mask,vec});return}for(let j=i;j<A.length;j++){const [a,_,w]=A[j];if(a<=Q&&c+w<=B)rec(j,Q-a,c+w,mask|(1n<<BigInt(j)),vec.map((v,k)=>v+proj[j][k]))}}rec(0,q,0,0n,Array(n).fill(0n));state[q]=out}
 assert(state[3].length===1482&&state[5].length===8506&&state[6].length===262,"rosters");
 function floor(a,b){let q=a/b;return a<0n&&a%b?q-1n:q}
 const results=[];
 for(const [a,c,count] of [[6,6,20265],[3,6,335374],[5,6,1513179]]){
  let Amax=BigInt(B-361*a-18),Bmax=BigInt(B-361*c-18);
  for(let i=0;i<n;i++)assert((Amax+Bmax)*(high[i]-low[i])<D[i],"nonbranch interval");
  let pairs=0,survive=0,depth=Array(n).fill(0);
  for(let j=0;j<state[a].length;j++){let u=state[a][j];for(let k=a===c?j+1:0;k<state[c].length;k++){let v=state[c][k];if(u.mask&v.mask)continue;pairs++;let zs=Array(n).fill(0n),ok=true;for(let i=n-1;i>=0;i--){let h=u.vec[i]-v.vec[i];for(let t=i+1;t<n;t++)h+=zs[t]*M[i][t];let lo=u.budget*low[i]-v.budget*high[i],hi=u.budget*high[i]-v.budget*low[i];let z=-floor(h-lo,D[i]);if(h+z*D[i]>hi){depth[n-1-i]++;ok=false;break}zs[i]=z}if(ok)survive++}}
  assert(pairs===count,"pair count");assert(survive===0,"surviving interval candidate");results.push({split:[a,c],pairs,survive,depth});
 }
 return {index:idx.toString(),basisCongruences:n*6,representativeCongruences:R.length*6,atoms:A.length,rosters:Object.fromEntries(Object.entries(state).map(([q,v])=>[q,v.length])),results};
}
```
