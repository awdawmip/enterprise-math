"use strict";
// Run with Node.js 18+: node R279_verify_bivariate.js
// Exact integer checker; tests cannot by themselves prove infinite claims.
const run=function check(maxN=150){
  const E=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
  let cur=new Map([["0,1,0,0",1n]]),raw=[];
  for(let n=0;n<=maxN;n++){
    const h=new Map(),next=new Map();
    for(const [id,v] of cur){
      const [q,e,k,p]=id.split(",").map(Number);
      if(q===0){const key=e+","+k;h.set(key,(h.get(key)||0n)+v)}
      if(n===maxN)continue;
      for(let bit=0;bit<=1;bit++){
        if(p&&bit===0)continue;
        const [q2,eta,b]=E[q][bit],key=[q2,eta*e,eta*k+b,bit===0?1:0].join(",");
        next.set(key,(next.get(key)||0n)+v);
      }
    }raw.push(h);cur=next;
  }
  const src={1:new Map([["0,0",1n],["2,0",1n],["4,0",1n],["1,-1",-1n],["1,1",-1n],["3,1",-1n]]),
    "-1":new Map([["4,-2",1n],["5,-1",-1n]])};
  let pred=[],mom={1:[], "-1":[]},total={1:[], "-1":[]},matched=0;
  function g(n,e,k){return n<0?0n:(pred[n].get(e+","+k)||0n)}
  for(let n=0;n<=maxN;n++){
    const h=new Map();
    for(let e of [1,-1])for(let k=-n;k<=n;k++){
      let v=src[e].get(n+","+k)||0n;
      v+=-g(n-2,e,k)-2n*g(n-4,e,k)-g(n-6,e,k)+g(n-8,e,k);
      for(let d of [-1,1])v+=g(n-1,e,k+d)+g(n-3,e,k+d);
      if(v<0n)throw Error("negative coefficient at "+n+","+e+","+k);
      if(v)h.set(e+","+k,v);
    }pred.push(h);
    if(h.size!==raw[n].size)throw Error("different support "+n);
    for(const [k,v] of h){if(raw[n].get(k)!==v)throw Error("different coefficient "+n+","+k);matched++}
    for(const e of [1,-1]){
      let a=0n,b=0n;
      for(const [id,v] of h){let [ee,k]=id.split(",").map(Number);if(ee===e){a+=v;b+=BigInt(k)*v}}
      total[e].push(a);mom[e].push(b);
    }
    if(total[1][n]-total[-1][n]!==((n%3===0)?1n:0n))throw Error("sign difference "+n);
  }
  const H1=[[0,1n],[1,-2n],[2,1n],[3,-2n],[4,2n],[6,1n],[8,-1n]];
  for(let n=0;n<=maxN;n++)for(let e of [1,-1]){
    let v=0n;for(const [j,a] of H1)if(j<=n)v+=a*mom[e][n-j];
    const want=e===1&&n===3?-1n:e===-1&&n===4?-2n:e===-1&&n===5?1n:0n;
    if(v!==want)throw Error("signed moment "+n+","+e);
  }
  return {status:"PASS",depth_inclusive:maxN,checked_nonzero_coefficients:matched,
    checked:"six-edge clean q0 raw counts = rational Laurent recurrence; every n sign difference and both moment recurrences",
    population_n150:{plus:total[1][maxN].toString(),minus:total[-1][maxN].toString()},
    arithmetic:"BigInt exact",infinite_claim_basis:"separate algebraic and analytic proof"};
};
console.log(JSON.stringify(run(150),null,2));
