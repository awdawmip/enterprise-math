'use strict';
// Exact native signed-step DP and independently specified PREFIX-512 fibers.
const gates={aab:[0,0,1],aba:[0,1,0]},colors=[0,4,1,2,3,3,4,4,4,4],src={1:'B',2:'B',3:'C'};
const rules={
aab:[['B',0,0,0,'P'],['B',1,1,0,'P'],['B',2,2,0,'P'],['B',3,2,0,'R'],['C',0,0,1,'P'],['C',1,1,1,'P'],['C',2,2,1,'P'],['C',3,2,1,'P']],
aba:[['B',0,0,0,'P'],['B',1,1,0,'P'],['B',2,1,0,'R'],['B',3,2,0,'R'],['C',0,0,1,'P'],['C',1,1,1,'P'],['C',2,1,1,'P'],['C',3,2,1,'P']]};
function terminal(s,g){for(let q=Math.min(s.length,3);q>0;q--)if(s.slice(-q).every((c,i)=>c===g[i]))return q;return 0;}
function P(m,A,C,j){let J=Math.max(0,Math.min(j,m-A+1)-C);return J*(2*m-2*A-C+1)-J*(2*C+J-1)/2;}
function R(m,A,j){let h=m-A;if(h<0)return 0;let J=Math.max(0,Math.min(j,h+1));return P(m,A,0,J)-Math.max(0,Math.min(J,h)-1)-(J>h&&h>0?h:0);}
function predicted(m,g,w){let ans=new Set();for(const [t,q,A,C,k] of rules[g]){let h=m-A;if(k==='P'){if(C<=w&&w<=h)for(let v=0;v<=2*h-w-C;v++)ans.add([v,q,t].join(':'));}else if(0<=w&&w<=h){let vs=w===0?Array.from({length:2*h+1},(_,i)=>i):w===h?[h]:Array.from({length:2*h-w},(_,i)=>i+1);for(let v of vs)ans.add([v,q,t].join(':'));}}return ans;}
function prefix(m,g,j){return rules[g].reduce((acc,[t,q,A,C,k])=>acc+(k==='R'?R(m,A,j):P(m,A,C,j)),0);}
function run(maxN=9){let out={status:'ALL_CHECKS_PASS',frozen_science:'f42f2906d77f24085c123f3ccfe9667d41caa96d',target_y:[0,1,0,0,0],maxN,native_rows:0,native_states:0,prefix_checks:0,algebra_checks:0,gate_results:{}};
for(const [name,gate] of Object.entries(gates)){
let ss=new Set([JSON.stringify([[0,0,0,0,0],0,0,0,'N'])]),rows=[];
for(let n=0;n<=maxN;n++){
if(n%2===1){let m=(n-1)/2,obs=new Map();for(const s of ss){let [y,v,w,q,t]=JSON.parse(s);if(y.join(',')==='0,1,0,0,0'){if(!obs.has(w))obs.set(w,new Set());obs.get(w).add([v,q,t].join(':'));}}
let total=0;for(let w=0;w<=m;w++){let got=obs.get(w)||new Set(),want=predicted(m,name,w);if(got.size!==want.size||[...got].some(x=>!want.has(x)))throw Error("support "+name+" n="+n+" w="+w);total+=got.size;out.native_rows++;out.native_states+=got.size;}
for(let j=-1;j<=m+3;j++){let actual=[...obs].reduce((s,[w,row])=>s+(w<j?row.size:0),0);if(prefix(m,name,j)!==actual)throw Error("prefix "+name+" n="+n+" j="+j);out.prefix_checks++;}
rows.push({n,m,total});}
if(n===maxN)break;let nxt=new Set();for(const s of ss){let [y,v,w,q,t]=JSON.parse(s);for(let i=0;i<10;i++){let ax=i>>1,sign=i%2?-1:1,z=y.slice(),c=z[ax]*sign<0?1:0;z[ax]+=sign;let V=v+c*(ax===1||ax===4?1:ax===3?2:0),W=w+c*(ax===2||ax===4?1:0),Q=terminal(gate.slice(0,q).concat([colors[i]]),gate),T=t==='N'?(src[colors[i]]||'N'):t;nxt.add(JSON.stringify([z,V,W,Q,T]));}}
ss=nxt;}out.gate_results[name]=rows;
for(let m=0;m<=60;m++)for(let j=-1;j<=m+3;j++){let actual=0;for(let w=0;w<=m;w++)if(w<j)actual+=predicted(m,name,w).size;if(actual!==prefix(m,name,j))throw Error("algebra "+name+" m="+m+" j="+j);out.algebra_checks++;}}
return out;}
if(require.main===module)console.log(JSON.stringify(run(),null,2));
