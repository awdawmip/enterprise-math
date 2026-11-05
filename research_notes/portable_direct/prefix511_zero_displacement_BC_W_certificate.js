"use strict";
// PREFIX-511 independent ten signed-direction DP; no path multiplicity.
const gates={aab:[0,0,1],aba:[0,1,0]},colors=[0,4,1,2,3,3,4,4,4,4],sources={1:"B",2:"B",3:"C"};
const rules={
aab:[["B",0,0,1,0],["B",1,1,1,0],["B",2,2,1,0],["B",3,2,1,0],["C",0,0,0,1],["C",1,1,0,1],["C",2,2,0,1],["C",3,2,1,1]],
aba:[["B",0,0,1,0],["B",1,1,1,0],["B",2,1,1,0],["B",3,2,1,0],["C",0,0,0,1],["C",1,1,0,1],["C",2,1,1,1],["C",3,2,1,1]]};
const phi=h=>h<0?0:(h+1)*(3*h+2)/2;
function terminal(seq,g){for(let k=Math.min(3,seq.length);k>0;k--)if(seq.slice(-k).every((x,i)=>x===g[i]))return k;return 0;}
function predicted(m,g,w){const s=new Set();for(const [t,q,A,B,C] of rules[g])if(w>=C&&w<=m-A-B)for(let v=B;v<=2*m-w-2*A-B-C;v++)s.add([v,q,t].join(":"));return s;}
function prefix(m,g,j){return rules[g].reduce((tot,[t,q,A,B,C])=>{const k=Math.max(0,Math.min(j,m-A-B+1)-C);return tot+k*(2*m-2*A-2*B-C+1)-k*(2*C+k-1)/2;},0);}
function total(m,g){return g==="aab"?2*phi(m-1)+2*phi(m-2)+3*phi(m-3)+phi(m-4):2*phi(m-1)+3*phi(m-2)+2*phi(m-3)+phi(m-4);}
function run(maxN=8){
 const r={status:"ALL_CHECKS_PASS",frozen_science:"f42f2906d77f24085c123f3ccfe9667d41caa96d",scope:"X6 signed ten-direction five-axis subfamily, zero displacement",native_n_max:maxN,gates:{},native_row_checks:0,native_prefix_checks:0,native_support_checks:0,algebra_m_range:[0,60]};
 for(const [name,gate] of Object.entries(gates)){
  let states=new Set([JSON.stringify([[0,0,0,0,0],0,0,0,"N"])]),rows=[];
  for(let n=0;n<=maxN;n++){
   if(n%2===0){
    const m=n/2,obs=new Map();
    for(const st of states){const [y,V,W,q,t]=JSON.parse(st);if(y.every(x=>x===0)&&(t==="B"||t==="C")){if(!obs.has(W))obs.set(W,new Set());obs.get(W).add([V,q,t].join(":"));}}
    let count=0;
    for(let w=0;w<=m;w++){const actual=obs.get(w)||new Set(),want=predicted(m,name,w);if(actual.size!==want.size||[...actual].some(x=>!want.has(x)))throw Error("state mismatch "+name+" "+n+" "+w);count+=actual.size;r.native_row_checks++;r.native_support_checks+=actual.size;}
    if(count!==total(m,name))throw Error("total mismatch "+name+" "+n);
    for(let j=0;j<=m+2;j++){let direct=0;for(let w=0;w<Math.min(j,m+1);w++)direct+=(obs.get(w)||new Set()).size;if(direct!==prefix(m,name,j))throw Error("prefix mismatch "+name+" "+n+" "+j);r.native_prefix_checks++;}
    rows.push({n,m,BC_states:count});
   }
   if(n===maxN)break;
   const next=new Set();
   for(const st of states){const [y,V,W,q,t]=JSON.parse(st);for(let i=0;i<10;i++){
    const ax=Math.floor(i/2),sgn=i%2?-1:1,z=y.slice(),cancel=z[ax]*sgn<0?1:0;z[ax]+=sgn;
    const nv=V+cancel*(ax===1||ax===4?1:ax===3?2:0),nw=W+cancel*(ax===2||ax===4?1:0);
    const nq=terminal(gate.slice(0,q).concat([colors[i]]),gate);
    next.add(JSON.stringify([z,nv,nw,nq,t==="N"?(sources[colors[i]]||"N"):t]));
   }}
   states=next;
  }
  r.gates[name]=rows;
  for(let m=0;m<=60;m++){if(prefix(m,name,m+1)!==total(m,name))throw Error("formula mismatch");for(const j of [0,1,Math.floor(m/2),m,m+1,m+2]){let s=0;for(let w=0;w<Math.min(j,m+1);w++)s+=predicted(m,name,w).size;if(prefix(m,name,j)!==s)throw Error("m mismatch");}}
 }
 return r;
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
