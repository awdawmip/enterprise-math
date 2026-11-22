#!/usr/bin/env node
"use strict";
// Exhaustively compute all unoriented nonzero integer triples with Port<=10.
// Reproduce all Pareto fronts, list the 18-row universal bank and verify
// coordinatewise domination at every Port 1..10.
const verifySmallPort = function verifySmallPort() {
  const q=([x,y,z])=>Math.max(Math.max(x,0)+Math.max(y,0)+Math.max(z,0),Math.max(-x,0)+Math.max(-y,0)+Math.max(-z,0));
  const gap=([x,y,z])=>{const t=x+3*y+6*z,m=x+4*y+10*z,n=x+6*y+20*z;return [Math.abs(t),3*Math.abs(m),Math.abs(t+6*n),Math.abs(3*m-t),6*Math.abs(n),Math.abs(t+6*n-3*m)]};
  const candidates=[];
  for(let x=-10;x<=10;x++)for(let y=-10;y<=10;y++)for(let z=-10;z<=10;z++){
    if(x===0&&y===0&&z===0)continue;
    const first=x!==0?x:y!==0?y:z;
    if(first<0)continue;
    const a=[x,y,z],port=q(a);
    if(port<=10)candidates.push({a,p:port,g:gap(a)});
  }
  const dominated=(a,b)=>a.g.every((v,i)=>v<=b.g[i])&&a.g.some((v,i)=>v<b.g[i]);
  const totals=[],fronts=[],used=new Map();
  for(let p=1;p<=10;p++){
    const pool=candidates.filter(r=>r.p<=p);
    const fr=pool.filter(r=>!pool.some(s=>dominated(s,r)));
    totals.push(pool.length);fronts.push(fr.length);
    for(const r of fr){let k=r.a.join(",");let v=used.get(k);if(v)v.last=p;else used.set(k,{...r,first:p,last:p});}
  }
  const rows=[...used.values()].sort((a,b)=>a.p-b.p||a.a.join(",").localeCompare(b.a.join(",")));
  const expectedTotals=[6,27,73,154,280,461,707,1028,1434,1935];
  const expectedFronts=[1,2,4,5,7,9,10,10,11,12];
  if(JSON.stringify(totals)!==JSON.stringify(expectedTotals)||JSON.stringify(fronts)!==JSON.stringify(expectedFronts)||rows.length!==18)throw Error("finite certificate mismatch");
  const qs=rows.map(r=>r.a.join(","));
  const expected=["1,0,0","0,2,-1","1,-3,1","2,-3,1","3,-1,0","1,3,-1","3,-4,1","4,-1,0","3,2,-1","4,-4,1","5,-1,0","5,-4,1","6,-1,0","3,-7,2","6,-4,1","7,-1,0","7,2,-1","9,-5,1"];
  if(JSON.stringify([...qs].sort())!==JSON.stringify([...expected].sort()))throw Error("candidate catalog drift");
  for(let p=1;p<=10;p++){
    const pool=candidates.filter(r=>r.p<=p);
    const bank=rows.filter(r=>r.p<=p);
    for(const r of pool){if(!bank.some(s=>s.g.every((v,i)=>v<=r.g[i])))throw Error("bank dominance failure "+p+":"+r.a);}
  }
  return {status:"PASS",model:"conditional four-positive-weight six-pair BRC",domain:"all real A,B,C,D>0; 1<=integer Port<=10",total_direction_counts:totals,pareto_counts:fronts,bank:rows,checks:{unique_unoriented_directions_at_p10:candidates.length,domination_verified_each_p:true,pure_integer_arithmetic:true}};
};
console.log(JSON.stringify(verifySmallPort(), null, 2));
