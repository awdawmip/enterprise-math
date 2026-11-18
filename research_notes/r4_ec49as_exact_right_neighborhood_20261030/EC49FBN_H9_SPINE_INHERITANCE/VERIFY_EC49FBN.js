#!/usr/bin/env node
'use strict';
// EC49FBN exact native-BRC-key F/G spine verifier. Reads frozen EC49FBM report.
const fs=require('node:fs'),path=require('node:path');
const analyze=function analyze(d){
 const fact=n=>{let x=1;for(let i=2;i<=n;i++)x*=i;return x},multi=a=>{if(a.some(v=>v<0))return 0;const p=a.reduce((x,v)=>x*fact(v),1),n=fact(a.reduce((x,v)=>x+v,0));if(n%p)throw Error('bad multinomial');return n/p};
 const cnt=(h,k)=>{const[x,y,z]=k,c=[z-1,z,h+1-y-2*z,h+1-x,x+y-h-1];return c.every(x=>x>=0)?c:null};
 const cache=new Map();
 function words(h,k){
  const id=h+':'+k.join();if(cache.has(id))return cache.get(id);
  let c=cnt(h,k),set=new Set();
  if(c&&c[4]===0){let v=c.slice(0,4),b=[],chars='aefg';function rec(){
    if(v.every(x=>x===0)){if(b[0]==='f'||b[0]==='g')set.add(b.join(''));return}
    for(let i=0;i<4;i++)if(v[i]){v[i]--;b.push(chars[i]);rec();b.pop();v[i]++}
  }rec()}
  cache.set(id,set);return set;
 }
 function coefficient(h,L,M){
  const a=cnt(h,L),b=cnt(9,M);if(!a||!b||L[0]+L[1]!==h+1||M[0]+M[1]!==10)return 0;
  const diff=b.slice(0,4).map((x,i)=>x-a[i]);if(diff.some(x=>x<0))return 0;
  const nf=a[2]?multi([a[0],a[1],a[2]-1,a[3]]):0,ng=a[3]?multi([a[0],a[1],a[2],a[3]-1]):0;
  return (nf+ng)*multi(diff);
 }
 if(d.records.length!==124||d.summary.H9_key_eligible_pairs!==52)throw Error('upstream universe');
 const summary={},records=[];
 for(let schedule of ['fixed','shift']){
  let n=0,positive=0,total=0,by_h={},max={pairs:-1};
  for(const r of d.records){
   if(!r[schedule==='fixed'?'fixed_L_H4_H6_M_H7_H9':'shift_H6_to_M'])continue;
   n++;const L=r.L,M=r.M,hits=[];let pairs=0;
   for(let h=4;h<=8;h++){
    const K=h<=(schedule==='fixed'?6:5)?L:M,analytic=coefficient(h,K,M),early=words(h,K),late=words(9,M);
    let direct=0;for(const w of late)if(early.has(w.slice(0,h)))direct++;
    if(analytic!==direct)throw Error('formula/enumeration differ '+schedule+':'+L+':'+M+':'+h);
    if(analytic){pairs+=analytic;hits.push({h,pairs:analytic});by_h[h]=(by_h[h]||0)+1}
   }
   total+=pairs;if(pairs)positive++;
   if(pairs>max.pairs)max={L,M,pairs};
   records.push({schedule,L,M,hits,terminal_inheritance_pairs:pairs});
  }
  summary[schedule]={configurations:n,with_inheritance:positive,without_inheritance:n-positive,total_pairs:total,by_h,max};
 }
 if(summary.fixed.configurations!==27||summary.fixed.with_inheritance!==12||summary.fixed.total_pairs!==2000||summary.shift.configurations!==28||summary.shift.with_inheritance!==13||summary.shift.total_pairs!==1792)throw Error('expected aggregate failed');
 const native={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
 const witnesses=[{schedule:'shift',h:5,L:[4,2,1],M:[7,3,2],H:['fefgg','geffg'],H9:['fefggaefg','geffgaefg']},{schedule:'fixed',h:6,L:[4,3,1],M:[7,3,2],H:['fefggg','geffgg'],H9:['fefgggaef','geffggaef']}];
 for(const t of witnesses){
  let edges=new Set();
  for(let i=0;i<2;i++){
   if(!t.H9[i].startsWith(t.H[i])||!words(t.h,t.L).has(t.H[i])||!words(9,t.M).has(t.H9[i]))throw Error('bad signed witness');
   const p=[...t.H9[i]].flatMap(c=>native[c]),q=[...t.H[i]].flatMap(c=>native[c]),disp=Array(6).fill(0),key=Array(6).fill(0);
   if(p.length!==22||q.length!==2*t.L.reduce((a,b)=>a+b,0)-2||q.join()!==p.slice(0,q.length).join())throw Error('primitive prefix error');
   for(let j=0;j<p.length;j++){let x=p[j],k=Math.abs(x)-1;disp[k]+=Math.sign(x);if(x>0)key[k]++;edges.add(p.slice(0,j+1).join())}
   if(disp.join()!=='2,0,0,0,0,0'||key.join()!==t.M.concat(0,0,0).join())throw Error('native endpoint/key');
  }
  if(edges.size!==44)throw Error('native edges');t.native_edges=44;t.extra_early_edges=0;
 }
 return {schema:'EC49FBN_H9_EXACT_SPINE_INHERITANCE_V1',date:'2026-11-05',status:'PASS',frozen_scientific_input:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',source:'EC49FBM@a891301880c100f7b803f9e5328064c0aac97e18',summary,witnesses,records};
};
const input=JSON.parse(fs.readFileSync(path.join(__dirname,'..','EC49FBM_H9_SPINE_RANK_FEASIBILITY','EXACT_REPORT_EC49FBM.json'),'utf8'));
console.log(JSON.stringify(analyze(input),null,2));
