#!/usr/bin/env node
'use strict';
/* Independent integer signed-X6 path simulation and nine-state rank audit for EC49ES.
   No imports from Python: tests all six Pareto witnesses, exact p keys, no phantom
   axes, native step prefixes, and all legal rank-nine p-fiber counts h=2..6.
*/
const fs=require('fs');
const ops={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const states=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const B=['N','A','B','AB','BA'];const MOD=1000003;
function assert(cond,msg){if(!cond)throw new Error(msg)}
function steps(w){return [...w].flatMap(c=>ops[c])}
function counts(w){const s=steps(w);return Array.from({length:6},(_,i)=>s.filter(x=>x==i+1).length)}
function disp(w){const s=steps(w);return Array.from({length:6},(_,i)=>s.filter(x=>x==i+1).length-s.filter(x=>x==-i-1).length)}
function transfer(w){const S=steps(w);return states.map(([evt,p0])=>{let p=p0,e=evt;for(const t of S){if(p==1&&t==2){if(e==='N')e='A';else if(e==='B')e='BA'}else if(p==2&&t==1){if(e==='N')e='B';else if(e==='A')e='AB'}p=t}return B.indexOf(e)})}
const sigKey=(t)=>t.join(',');
function modPow(a,n){let out=1;while(n){if(n&1)out=out*a%MOD;a=a*a%MOD;n=Math.floor(n/2)}return out}
function rankQViaPrime(trs){const col=[];for(const t of trs)for(let b=0;b<5;b++)col.push(t.map(x=>Number(x===b)));
 const A=Array.from({length:9},(_,i)=>col.map(c=>c[i]));const nr=A.length,nc=col.length;
 let r=0;for(let c=0;c<nc&&r<nr;c++){let p=r;while(p<nr&&A[p][c]===0)p++;if(p===nr)continue;
 [A[r],A[p]]=[A[p],A[r]];const inv=modPow(A[r][c],MOD-2);
 for(let j=c;j<nc;j++)A[r][j]=A[r][j]*inv%MOD;
 for(let i=r+1;i<nr;i++){const f=A[i][c];if(!f)continue;for(let j=c;j<nc;j++)A[i][j]=(A[i][j]-f*A[r][j]%MOD+MOD)%MOD;}
 r++}return r;
}
const BASE=['ce','de','ec','ed'];
function validateWitness(name,byH,target){const pre=new Set(),keys=new Set(),sigs=new Set();
 for(const h of [2,3,4,5,6]){const W=(h===2?BASE:byH[String(h)]);assert(W&&W.length>0,`${name} missing ${h}`);
  const ps=new Set(W.map(w=>JSON.stringify(counts(w))));assert(ps.size===1,`${name} broken BRC key h=${h}`);
  const ts=[...new Map(W.map(w=>[sigKey(transfer(w)),transfer(w)])).values()];
  assert(rankQViaPrime(ts)===9,`${name} rank<9 h=${h}`);
  for(const w of W){assert(w.length===h,`${name} horizon ${h}/${w}`);assert(JSON.stringify(disp(w))===JSON.stringify([2,0,0,0,0,0]),`${name} illegal return ${w}`);
    const s=steps(w);for(let i=1;i<=s.length;i++)pre.add(s.slice(0,i).join(','));
    keys.add(JSON.stringify(counts(w)));sigs.add(sigKey(transfer(w)));}
 }
 const v=[pre.size,keys.size,sigs.size];assert(JSON.stringify(v)===JSON.stringify(target),`${name} resources actual=${v} expected=${target}`);
 return {name,resources:v,words_by_h:{'2':BASE,...byH}};
}
const r=JSON.parse(fs.readFileSync('EC49ES_EXECUTED.json','utf8'));
const old=JSON.parse(fs.readFileSync('EC49ER_ALL_M3_EXECUTED.json','utf8'));
const two=JSON.parse(fs.readFileSync('EC49ER_EXECUTED.json','utf8'));
const cases=[
 ['H6-M2-S6',two.M2_exact_cases[0].chosen_words_by_h,[90,2,6]],
 ['H6-M3-S6',old.out['6'].witness,[68,3,6]],
 ['H6-M3-S4',old.out['4'].witness,[84,3,4]],
 ['H6-M4-S6',Object.fromEntries([3,4,5,6].map(h=>[h,['feg'+'f'.repeat(h-3),'gef'+'f'.repeat(h-3)]])),[54,4,6]],
 ['H6-M4-S4',r.results['4'].witness,[72,4,4]],
 ['H6-M5-S4',r.results['5'].witness,[60,5,4]]
];
const results=cases.map(([n,w,v])=>validateWitness(n,w,v));
const countsByH={},fullFibersByH={};
const alphabet=Object.keys(ops);
for(let h=2;h<=6;h++){
 const byP=new Map();let count=0;
 function visit(w){if(w.length===h){if(JSON.stringify(disp(w))!==JSON.stringify([2,0,0,0,0,0]))return;count++;
  const p=JSON.stringify(counts(w));if(!byP.has(p))byP.set(p,new Map());
  const sig=transfer(w);byP.get(p).set(sigKey(sig),sig);return}
  for(const x of alphabet)visit(w+x)}
 visit('');countsByH[h]=count;fullFibersByH[h]=[...byP.values()].filter(s=>rankQViaPrime([...s.values()])===9).length;
}
assert(JSON.stringify([2,3,4,5,6].map(h=>countsByH[h]))===JSON.stringify([8,51,304,1770,10224]),'word counts mismatch');
assert(JSON.stringify([2,3,4,5,6].map(h=>fullFibersByH[h]))===JSON.stringify([1,4,9,17,28]),'fiber counts mismatch');
const output={unit:'EC49ES',status:'PASS',engine:'independent Node.js signed native X6 + mod-prime Gaussian elimination',prime:MOD,countsByH,fullFibersByH,verifiedParetoWitnesses:results.map(({name,resources})=>({name,resources})),model:'seven operation primitive-token prefix-free code; rational-rank9 via exact 9x9 determinant bound 3^9 < 1000003'};
fs.writeFileSync('EC49ES_INDEPENDENT_EXECUTED.json',JSON.stringify(output,null,2));
console.log(JSON.stringify(output,null,2));
