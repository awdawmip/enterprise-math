// Exact-author certificate for BRC S23: full F4([0,1]^4), pinned science.
// To reproduce: node VERIFY.js (no packages).
function verifyF4() {
  "use strict";
  const N=3600, GRID=6, LIMIT=4*N/3;
  const check=(condition,message)=>{if(!condition)throw new Error(message);};
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
    [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const A=[0,0,0,1,1,1],B=[2,2,3,2,2,4],C=[5,6,7,8,9,10],G=[0,0,1,2,2,3];
  const PAIRS=["34 24 34 24","34 23 34 34","34 34 34 23","24 24 12 12",
    "12 13 23 24","23 34 12 13","24 34 12 14"];
  const FREE=[
    "2/5 0 2/5 1/5;2/5 2/5 0 1/5;3/5 0 0 2/5;2/5 2/5 0 1/5",
    "1/2 1/2 0 0;1/2 0 0 1/2;0 0 1/2 1/2;0 0 1/2 1/2",
    "0 1/2 1/2 0;0 1 0 0;0 1 0 0;0 0 1/2 1/2"];
  const names=["D1","D2","D3","D4","D6","D7","D8","K1_new","K2","K3"];
  const scale=s=>{const [a,b="1"]=String(s).split("/").map(Number);const n=N*a/b;check(Number.isSafeInteger(n),"nonintegral fraction "+s);return n;};
  const mix=rows=>M.map((ws,i)=>{
    const row=[0,1,2,3].map(j=>{
      const numerator=ws.reduce((sum,w,k)=>sum+w*rows[k][j],0);
      check(Number.isSafeInteger(numerator)&&numerator%20===0,"nonintegral mixed source "+i);
      return numerator/20;
    });
    check(row.every(x=>x>=0)&&row.reduce((s,x)=>s+x,0)===N,"row normalization "+i);
    return row;
  });
  const kernel=rows=>{check(rows.length===4&&rows.every(r=>r.length===4&&r.every(Number.isSafeInteger)&&r.every(x=>x>=0)&&r.reduce((x,y)=>x+y,0)===N),"invalid decoder kernel");return mix(G.map(i=>rows[i]));};
  const pair=s=>kernel(s.split(" ").map(w=>[1,2,3,4].map(i=>N*w.split("").filter(d=>Number(d)===i).length/2)));
  const free=s=>kernel(s.split(";").map(w=>w.trim().split(/\s+/).map(scale)));
  const bank=[...PAIRS.map(pair),...FREE.map(free)];
  check(bank.length===10,"decoder bank size");
  const prepare=(i,j,k,l)=>{
    check([i,j,k,l].every(x=>Number.isSafeInteger(x)&&x>=0&&x<=GRID),"non-grid strategy");
    const z=[i*N/GRID,j*N/GRID,k*N/GRID,l*N/GRID,0,N,0,0,0,0,0];
    const src=A.map((a,p)=>{
      const x=z[a],b=z[B[p]],c=z[C[p]],tail=(N-x)*(N-b)/N,mid=(N-x)*b/N,last=tail*c/N;
      check([x,tail,mid,last].every(Number.isSafeInteger),"nonintegral source");
      const row=[x,mid,last,tail-last];
      check(row.every(y=>y>=0)&&row.reduce((sum,y)=>sum+y,0)===N,"source normalization");
      return row;
    });
    return mix(src);
  };
  const risk2=(p,q)=>Math.max(...p.map((row,i)=>row.reduce((sum,x,j)=>sum+Math.abs(x-q[i][j]),0)));
  const idx=(i,j,k,l)=>(((i*7+j)*7+k)*7+l);
  const risks=Array(7**4);
  for(let i=0;i<=GRID;i++)for(let j=0;j<=GRID;j++)for(let k=0;k<=GRID;k++)for(let l=0;l<=GRID;l++){
    const p=prepare(i,j,k,l);risks[idx(i,j,k,l)]=bank.map(q=>risk2(p,q));
  }
  const selected=[],counts=Object.fromEntries(names.map(n=>[n,0]));
  let maxCell=0,worstCell=null;
  for(let i=0;i<GRID;i++)for(let j=0;j<GRID;j++)for(let k=0;k<GRID;k++)for(let l=0;l<GRID;l++){
    const worst=bank.map((_,index)=>{
      let m=0;
      for(let a=0;a<=1;a++)for(let b=0;b<=1;b++)for(let c=0;c<=1;c++)for(let d=0;d<=1;d++)
        m=Math.max(m,risks[idx(i+a,j+b,k+c,l+d)][index]);
      return m;
    });
    const m=Math.min(...worst),ix=worst.indexOf(m);
    check(m<=LIMIT,`uncovered cell ${[i,j,k,l]} risk2=${m}`);
    if(m>maxCell){maxCell=m;worstCell=[i,j,k,l];}
    selected.push(ix);counts[names[ix]]++;
  }
  check(selected.length===1296,"incomplete grid");
  const exactPoint=risks[idx(2,0,6,3)];
  const witness=[2*N,2*N,2*N,2*N,LIMIT,2*N,LIMIT,2*N,2*N,LIMIT];
  check(exactPoint.every((x,i)=>x===witness[i]),"sharp witness errors changed");
  let outerMax=0;
  for(let a=0;a<=1;a++)for(let b=0;b<=1;b++)for(let c=0;c<=1;c++)for(let d=0;d<=1;d++)
    outerMax=Math.max(outerMax,Math.min(...risks[idx(6*a,6*b,6*c,6*d)]));
  check(outerMax===6*N/5,"16 outer corner maximum changed");
  const edge={D8_v0:risks[idx(2,0,6,0)][6],D8_vhalf:risks[idx(2,0,6,3)][6],K3_vhalf:risks[idx(2,0,6,3)][9],K3_v1:risks[idx(2,0,6,6)][9]};
  check(edge.D8_v0===N&&edge.D8_vhalf===LIMIT&&edge.K3_vhalf===LIMIT&&edge.K3_v1===N,"edge certificate changed");
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const fraction=r=>{let g=gcd(r,2*N);return `${r/g}/${2*N/g}`;};
  const evidence={
    pass:"PASS_BRC_S23_F4_6POWER4_CELLS_SHARP_BANK_TWO_THIRDS_20261102",
    source_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
    prior_bank_commit:"de0ddc3371ec886be1eb906958cb16e3b4db0978",
    source_model:"six labeled positive-weight observation sources, original M and common encoder; four-stop outputs",
    strategy_family:"F4(s,t,u,v)=(s,t,u,v,0;1,0,0,0,0,0)",
    quantifier_scope:"sup over [0,1]^4 of min risk in this specified 10-decoder bank; no reoptimization over its three free kernels",
    result:"2/3",probability_scale:N,tv_denominator:2*N,
    decoders:names,vertices:7**4,cells:6**4,corners_per_cell:16,
    certified_max_cell_risk:fraction(maxCell),worst_cell:worstCell,
    cell_decoder_counts:counts,cell_decoder_indices: selected.join(""),
    exact_witness:"F4(1/3,0,1,1/2)",per_decoder_tv:exactPoint.map(fraction),
    outer_corner_count:16,outer_corner_max_min_tv:fraction(outerMax),
    one_dimensional_edge_endpoints:Object.fromEntries(Object.entries(edge).map(([key,v])=>[key,fraction(v)])),
    edge_unique_max:"v=1/2; D8 and K3 convex endpoint bounds",
    lower_status:"point certificate for fixed bank only",
    upper_status:"exact integer full 1296-cell common-decoder certificate plus analytic multi-affinity/TV convexity",
    reoptimized_radius_bounds:"3/5 <= R4 <= 2/3; sharp reoptimized value not proved",
    review_status:"author-only; not independently reviewed or admitted"
  };
  check(counts.K1_new===669&&counts.D4===201&&counts.D6===128&&counts.D1===73&&counts.D8===68&&counts.K2===116&&counts.K3===41,"coverage counts disagree with independent checker");
  return evidence;
}
if(typeof require !== "undefined" && require.main===module)console.log(JSON.stringify(verifyF4(),null,2));
