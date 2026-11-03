#!/usr/bin/env node
'use strict';
/* Independent direct 5-key weighted-clique census.
 * Derive keys with (r,f,g,w) constraints; assign singletons via a flat
 * non-recursive odometer; use explicit 31-bit clique masks and adjacency bitsets.
 * ECMAScript Number holds all actual integer values exactly.
 */
const H=[2,3,4,5,6,7,8];
function types(h){
  const a=new Map();
  for(let w=1;w<=Math.floor((h+1)/2);w++)for(let r=0;r<=h;r++)for(let f=0;f<=h;f++){
    let g=h-2*w+1-r-f;
    if(g<0)continue;
    let u=r+f+2*w, v=r+g, k=[u,v,w];
    // Derived from native operation counts: r+f+g+2w-1=h.
    // u=r+f+2w; v=r+g. A valid n+2 tally is r+g, yes.
    if(r===0 && !(f>=1 && g>=1))continue;
    let key=k.join(',');
    if(a.has(key) && a.get(key)!==(r?4:2))throw Error('type collision');
    a.set(key,r?4:2);
  }
  return a;
}
const T=new Map(H.map(h=>[h,types(h)]));
const expected=[1,4,9,17,28,43,62];
for(let i=0;i<H.length;i++)if(T.get(H[i]).size!==expected[i])throw Error('eligible mismatch at '+H[i]+': '+T.get(H[i]).size);
const Tkeys=new Map(H.map(h=>[h,[...T.get(h).keys()]]));
const dec=k=>k.split(',').map(Number);
function cap(a,b){let aa=dec(a),bb=dec(b);return 2*(Math.min(aa[0],bb[0])+Math.min(aa[1],bb[1])+Math.min(aa[2],bb[2]))-2;}
function B(assign){
  let G=new Map();
  for(let h of H){let k=assign.get(h);if(!G.has(k))G.set(k,{n:0,m:0,L:2*(dec(k).reduce((a,b)=>a+b,0)-1)});
    let g=G.get(k);g.n++;g.m+=T.get(h).get(k);}
  if(G.size!==5)throw Error('keys != 5');
  let k=[...G.keys()], gs=k.map(x=>G.get(x)), caps=Array.from({length:5},()=>Array(5).fill(0));
  for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)caps[i][j]=caps[j][i]=cap(k[i],k[j]);
  let E=0,Lmax=Math.max(...gs.map(x=>x.L));
  for(let d=1;d<=Lmax;d++){
    let q=gs.map(x=>d>x.L?0:d>=x.L-1?x.m:d===x.L-2?x.n:1);
    let max=0;
    for(let mask=1;mask<32;mask++){
      let weight=0,clique=true;
      for(let i=0;i<5;i++)if((mask>>>i)&1){weight+=q[i];
        for(let j=i+1;j<5;j++)if((mask>>>j)&1 && caps[i][j]>=d){clique=false;break;}
        if(!clique)break;
      }
      if(clique && weight>max)max=weight;
    }
    E+=max;
  }
  return E;
}
let hist=new Map(),byTriple=[],samples=new Map(),count=0;
for(let a=0;a<7;a++)for(let b=a+1;b<7;b++)for(let c=b+1;c<7;c++){
  let tri=[H[a],H[b],H[c]], single=H.filter(h=>!tri.includes(h));
  let cnt=0,lo=1e9,hi=-1,excluded80=0,excluded81=0;
  for(let shared of Tkeys.get(tri[0])){
    if(!T.get(tri[1]).has(shared)||!T.get(tri[2]).has(shared))continue;
    let assign=new Map(tri.map(h=>[h,shared]));
    function search(i, used) {
      if(i===4){
        let e=B(assign);
        hist.set(e,(hist.get(e)||0)+1);
        if(!samples.has(e))samples.set(e,Object.fromEntries([...assign].sort((x,y)=>x[0]-y[0])));
        count++;cnt++;lo=Math.min(lo,e);hi=Math.max(hi,e);
        if(e>=80)excluded80++;
        if(e>80)excluded81++;
        return;
      }
      let h=single[i];
      for(let kk of Tkeys.get(h))if(!used.has(kk)){
        assign.set(h,kk);used.add(kk);search(i+1,used);used.delete(kk);
      }
      assign.delete(h);
    }
    search(0,new Set([shared]));
  }
  if(cnt)byTriple.push({windows:tri,schedules:cnt,lower_bound_min:lo,lower_bound_max:hi,E_lt_80_excluded:excluded80,E_le_80_excluded:excluded81});
}
if(count!==123147)throw Error('schedule count '+count);
const excluded=Object.entries(Object.fromEntries(hist)).filter(x=>Number(x[0])>=80).reduce((n,[k,v])=>n+v,0);
const out={status:'PASS', scope:'native signed X6 8 horizons five cache keys triple-key schedules',
  frozen_scientific_pins:{global:'773d538180bfb49e24cffeb35c3ee75eb0628e2e',enterprise_math:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'},
  schedules:count,lb_histogram:Object.fromEntries([...hist].sort((x,y)=>x[0]-y[0])),
  E_lt_80_excluded:excluded,E_lt_80_survivors:count-excluded,
  E_le_80_excluded:[...hist].filter(x=>x[0]>80).reduce((n,x)=>n+x[1],0),
  min_lb:Math.min(...hist.keys()),max_lb:Math.max(...hist.keys()),
  per_triple:byTriple,example_lb90:samples.get(90)};
console.log(JSON.stringify(out,null,2));