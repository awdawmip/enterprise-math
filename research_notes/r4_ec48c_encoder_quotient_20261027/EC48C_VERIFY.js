#!/usr/bin/env node
"use strict";
function verifyEC48C() {
  const shapes=[[1,1],[2,1],[3,1],[4,1],[2,2],[3,2],[4,2],[2,3],[3,3],[4,3]];
  const table=[];
  for(const [H,Y] of shapes) {
    const all=3**(H*Y);let eligible=0,spanning=0;
    for(let code=0;code<all;code++){
      let t=code;const signs=Array.from({length:H},()=>Array(Y).fill(0));
      for(let h=0;h<H;h++)for(let y=0;y<Y;y++){signs[h][y]=t%3-1;t=Math.floor(t/3)}
      const profiles=(tie)=>new Set(signs.map(row=>row.map(s=>s||tie).join(","))).size;
      if(Math.max(profiles(-1),profiles(1))>2)continue;
      eligible++;
      const Q=signs.flat().filter(s=>s===0).length;
      const enc=new Map();
      for(let f=0;f<(1<<H);f++){
        const forced=Array(2*Y).fill(0);let valid=true;
        for(let h=0;h<H&&valid;h++)for(let y=0;y<Y;y++){
          const s=signs[h][y],idx=((f>>h)&1)*Y+y;
          if(s&&forced[idx]&&forced[idx]!==s){valid=false;break}
          if(s)forced[idx]=s;
        }
        if(!valid)continue;
        let lo=0,hi=Q;
        for(let h=0;h<H;h++)for(let y=0;y<Y;y++)if(signs[h][y]===0){
          const v=forced[((f>>h)&1)*Y+y];
          if(v===1)lo++;if(v===-1)hi--;
        }
        enc.set(f,{forced,lo,hi});
      }
      const parent=new Map([...enc.keys()].map(k=>[k,k]));
      const root=(x)=>{while(parent.get(x)!==x){parent.set(x,parent.get(parent.get(x)));x=parent.get(x)}return x};
      for(const [f,v] of enc)for(let h=0;h<H;h++){
        const g=f^(1<<h),u=enc.get(g);if(!u)continue;
        if(v.forced.every((a,i)=>a===0||u.forced[i]===0||a===u.forced[i])){
          const a=root(f),b=root(g);if(a!==b)parent.set(b,a);
        }
      }
      const bounds=new Map();
      for(const [f,v] of enc){
        const k=root(f);
        if(!bounds.has(k))bounds.set(k,[v.lo,v.hi]);
        else {const a=bounds.get(k);a[0]=Math.min(a[0],v.lo);a[1]=Math.max(a[1],v.hi)}
      }
      if(![...bounds.values()].some(([lo,hi])=>lo===0&&hi===Q))
        throw Error("UNFILLED_FACE "+JSON.stringify({H,Y,signs,bounds:[...bounds.values()]}));
      spanning++;
    }
    table.push({H,Y,all,eligible,spanning});
  }
  return {schema:"EC48C_EXACT_SIGN_CERTIFICATE_V1",method:"exact integer signs; deterministic enumeration",table,
    checked_all:table.reduce((a,b)=>a+b.all,0),eligible:table.reduce((a,b)=>a+b.eligible,0),
    scope:"all ternary sign matrices H<=4,Y<=3,K_hull<=2; optimal encoder graph has a component joining tied endpoints; extends to all positive source weights",
    counterexample_found:false};
}
console.log(JSON.stringify(verifyEC48C(), null, 2));
