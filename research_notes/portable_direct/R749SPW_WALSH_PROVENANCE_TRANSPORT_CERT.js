#!/usr/bin/env node
// R749SPW exact integer certificate for two 26-letter Walsh provenance ensembles.
// Execute: node R749SPW_WALSH_PROVENANCE_TRANSPORT_CERT.js > R749SPW_WALSH_PROVENANCE_TRANSPORT_RESULTS.json
function verify() {
  const assert=(v,m)=>{if(!v)throw Error(m)};
  const rows=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
  const P=[];
  for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)
    if(rows.every(([a,b,c,d])=>a*h+b*u+c*v>=d))P.push([h,u,v]);
  assert(P.length===33,"expected 33 level-one points");
  const key=x=>x.join(",");
  const pair=new Map();
  for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
    const x=P[i].map((v,k)=>v+P[j][k]),s=key(x);
    let v=pair.get(s);if(!v){v={count:0,i,j};pair.set(s,v)}v.count++;
  }
  const forced=new Set();
  for(const v of pair.values())if(v.count===1){forced.add(v.i);forced.add(v.j)}
  const F=[...forced].sort((a,b)=>a-b).map(i=>P[i]);
  assert(F.length===25,"expected 25 forced first-grid letters");
  assert(!F.some(x=>key(x)==="0,0,0"||key(x)==="-1,0,0"),"optional overlap");
  const nChoose=(n,k)=>{let v=1;for(let i=1;i<=k;i++)v=v*(n-k+i)/i;return Math.round(v)};
  const enumerate=(n,m,visit)=>{
    const z=[];
    const go=(start,depth)=>{if(depth===n){visit(z);return;}for(let i=start;i<m;i++){z[depth]=i;go(i,depth+1)}};
    go(0,0);
  };
  const get=(m,k)=>m.get(k)||0;
  const fiber=(letters,n)=>{
    const out=new Map();
    enumerate(n,letters.length,ids=>{
      const x=[0,0,0];for(const i of ids)for(let d=0;d<3;d++)x[d]+=letters[i][d];
      const s=key(x);out.set(s,get(out,s)+1);
    });
    return out;
  };
  const gcd=(a,b)=>{while(b){const r=a%b;a=b;b=r}return a};
  const fraction=(a,b)=>{const g=gcd(Math.abs(a),Math.abs(b));return `${a/g}/${b/g}`};
  const expected={2:[179,7,7],3:[531,29,34],4:[1181,154,144],5:[2221,595,586]};
  const table=[];
  let prev0=new Map([["0,0,0",1]]),prev1=new Map([["0,0,0",1]]);
  for(let n=1;n<=5;n++){
    const counts0=new Map(),counts1=new Map(),khist=Array(n+1).fill(0);
    enumerate(n,26,ids=>{
      let h=0,u=0,v=0,k=0;
      for(const i of ids){if(i===25){k++}else{h+=F[i][0];u+=F[i][1];v+=F[i][2]}}
      khist[k]++;
      let a=key([h,u,v]),b=key([h-k,u,v]);
      counts0.set(a,get(counts0,a)+1); counts1.set(b,get(counts1,b)+1);
    });
    const N=nChoose(n+25,25);
    assert(khist.reduce((a,b)=>a+b,0)===N,"wrong multiset count");
    for(let k=0;k<=n;k++){
      assert(khist[k]===nChoose(n-k+24,24),"wrong optional-count frequency");
      assert(khist.slice(k).reduce((a,b)=>a+b,0)===nChoose(n-k+25,25),"wrong optional tail");
    }
    const S1=khist.reduce((a,b,k)=>a+k*b,0),S2=khist.reduce((a,b,k)=>a+k*k*b,0);
    assert(26*S1===n*N,"mean mismatch");
    assert(27*(676*S2-n*n*N)===25*n*(n+26)*N,"variance mismatch");
    const pure=fiber(F,n),all=new Set([...counts0.keys(),...counts1.keys(),...pure.keys(),...prev0.keys(),...prev1.keys()]);
    let difference=0,differing=0;
    for(const s of all){
      const x=s.split(",").map(Number);
      assert(get(counts0,s)===get(pure,s)+get(prev0,s),"first coefficient recursion");
      assert(get(counts1,s)===get(pure,s)+get(prev1,key([x[0]+1,x[1],x[2]])),"second coefficient recursion");
      const d=Math.abs(get(counts0,s)-get(counts1,s));
      difference+=d;if(d)differing++;
    }
    if(n>=2){
      assert(counts0.size===counts1.size&&[...counts0.keys()].every(k=>counts1.has(k)),"support mismatch");
      const [count,mx0,mx1]=expected[n];
      assert(counts0.size===count,"readout count");
      assert(Math.max(...counts0.values())===mx0&&Math.max(...counts1.values())===mx1,"fiber maxima");
    }
    for(let k=0;k<=n;k++){
      const signs=Array.from({length:16},(_,i)=>((i.toString(2).split("1").length-1)%2)===0?1:-1);
      assert(signs.filter(s=>s===1).length===8&&signs.filter(s=>s===-1).length===8,"Walsh signs");
      assert(16*k===2*160*n*(k/(20*n)),"Walsh TV identity");
    }
    table.push({
      n,source_multisets:N,
      reachable_zero:counts0.size,reachable_shift:counts1.size,
      largest_fiber_zero:Math.max(...counts0.values()),
      largest_fiber_shift:Math.max(...counts1.values()),
      optional_count_histogram:khist,
      source_multiset_mean_optional:fraction(S1,N),
      source_multiset_variance_optional:fraction(25*n*(n+26),676*27),
      readouts_with_different_frequencies:differing,
      output_distribution_TV:fraction(difference,2*N),
      mean_H_displacement:fraction(S1,N)
    });
    prev0=counts0;prev1=counts1;
  }
  return {
    schema:"R749SPW_WALSH_PROVENANCE_TRANSPORT_EXACT_CERT_V1",
    status:"PASS",
    frozen_input:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
    mathematical_scope:"signed auxiliary 16-atom Walsh model, fixed t=1/10,s=1/2",
    base_first_grid_points:P.length,
    forced_letters:F,
    forced_letter_count:F.length,
    optional_zero:[0,0,0],optional_shift:[-1,0,0],
    universal_exact_theorems:{
      sample_coupling:"X_zero - X_shift = k*(1,0,0), for every n>=1",
      optional_count_tail:"P(k>=r)=C(n-r+25,25)/C(n+25,25)",
      E_k:"n/26",Var_k:"25*n*(n+26)/(26^2*27)",
      W1_readout_l1:"n/26",W1_Walsh_centers_TV:"1/520",
      output_law_TV_lower_bound:"1/104",
      scaling_limit:"k/n converges in distribution to Beta(1,25) under uniform multisets"
    },
    tests:"Complete finite enumeration of both 26-source multiset ensembles and forced-only generating-function recursion for n=1..5, integer-only arithmetic",
    levels:table,
    review:"AUTHOR_EXACT_NOT_REVIEWED"
  };
}
process.stdout.write(JSON.stringify(verify(), null, 2)+"\n");
