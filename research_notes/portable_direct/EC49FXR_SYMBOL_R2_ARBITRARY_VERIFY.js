'use strict';
// EC49FXR: exact five-color collision optimization for r=2 whole-activation symbols.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const mod = (x,n) => (x%n+n)%n;
const groups = Array.from({length:5}, (_,i)=>Array.from({length:11},(_,z)=>i+5*z));

function describe(A) {
  const T=groups.map(g=>g.filter(x=>!A.has(mod(2*x,55))));
  const hist=groups.map(g=>g.filter(x=>A.has(x)).length);
  assert(hist.every(h=>h>0),'requires all five phase colors');
  return {T,hist};
}
function exactOptimize(A) {
  const {T,hist}=describe(A);
  let assignments=0;
  let best={L:-1,E:[],x:[],pairs:{},S:[]};
  function visit(i,E,x) {
    if(i===5) {
      assignments++;
      if(x.some((xi,a)=>x.slice(a+1).some(xj=>A.has(mod(xi+xj,55))))) return;
      const pairs={}; let L=E.length;
      for(let j=0;j<5;j++) if(!E.includes(j)) {
        const allowed=T[j].filter(y=>x.every(xi=>!A.has(mod(y+xi,55))));
        if(allowed.length>=2) {pairs[j]=allowed.slice(0,2);L++;}
      }
      if(L>best.L) {
        const doubles=Object.fromEntries(E.map((c,a)=>[c,x[a]]));
        const S=[];
        for(let j=0;j<5;j++) {
          if(Object.hasOwn(doubles,j)) S.push(doubles[j],doubles[j]+55);
          else if(Object.hasOwn(pairs,j)) S.push(...pairs[j]);
          else S.push(...groups[j].slice(0,3));
        }
        best={L,E:[...E],x:[...x],pairs,S:S.sort((a,b)=>a-b)};
      }
      return;
    }
    visit(i+1,E,x);
    for(const site of T[i]) {E.push(i);x.push(site);visit(i+1,E,x);E.pop();x.pop();}
  }
  visit(0,[],[]);
  assert(best.L>=0 && best.L<=5);
  const optimum=15-best.L;
  assert.equal(best.S.length,optimum);
  assert.equal(new Set(best.S).size,optimum);
  return {optimum,hist,safe_counts:T.map(t=>t.length),assignments,best};
}
function distance(S,d,i,j) {
  let g=0;
  for(const t of S) {
    if((t%5===i && t%11!==j)||(mod(d-t,5)===i && mod(d-t,11)!==j))g++;
  }
  return g;
}
function check(A,S,r=2) {
  let checked=0,min=110,worst=null;
  for(const d of [...A].sort((a,b)=>a-b))for(let i=0;i<5;i++)for(let j=0;j<11;j++) {
    const v=distance(S,d,i,j);
    checked++;
    if(v<min){min=v;worst=[d,i,j];}
    assert(v>=r,'violation d='+d+' i='+i+' j='+j+' distance='+v);
  }
  return {checked,min,worst};
}
const good=new Set([...groups[0].filter(x=>x!==0),...groups[2].filter(x=>x!==2 && x!==7),1,3,19]);
const bad=new Set([...groups[0].filter(x=>x!==0),...groups[2].filter(x=>x!==2 && x!==7),1,3,4]);
const examples={};let rowTotal=0;
for(const [name,A] of [['good',good],['bad',bad]]) {
  const o=exactOptimize(A),w=check(A,o.best.S);
  assert.equal(o.optimum,name==='good'?10:11);
  assert.deepEqual(o.hist,[10,1,9,1,1]);
  rowTotal+=w.checked;
  examples[name]={A:[...A].sort((a,b)=>a-b),hist:o.hist,T:o.safe_counts,optimum:o.optimum,
    search_assignments:o.assignments,chosen_E:o.best.E,doubled_groups:o.best.x,
    chosen_distinct_pairs:o.best.pairs,physical_layout:o.best.S,verification:w};
}
const manualGood=[0,2,7,24,31,33,38,55,79,86];
const manualBad=[0,1,3,4,5,7,8,9,10,12,31];
assert.deepEqual(examples.good.physical_layout,manualGood);
assert.deepEqual(examples.bad.physical_layout,manualBad);
let smallCases=0,smallRows=0;
for(let mask=0;mask<32;mask++) {
  const A=new Set(Array.from({length:5},(_,c)=>c+5*((mask>>c)&1)));
  const o=exactOptimize(A),w=check(A,o.best.S);
  assert.equal(o.optimum,10);
  smallCases++;smallRows+=w.checked;
}
let state=49231123;
function rnd(){state=(Math.imul(state,1664525)+1013904223)>>>0;return state;}
let generated=0,generatedRows=0,distribution={};
for(let trial=0;trial<600;trial++) {
  const A=new Set();
  for(let c=0;c<5;c++) {
    const g=[...groups[c]];
    for(let z=10;z>0;z--){const j=rnd()%(z+1);[g[z],g[j]]=[g[j],g[z]];}
    const h=trial<400?1+rnd()%11:9+rnd()%3;
    for(let z=0;z<h;z++)A.add(g[z]);
  }
  const o=exactOptimize(A),w=check(A,o.best.S);
  generated++;generatedRows+=w.checked;
  distribution[o.optimum]=(distribution[o.optimum]||0)+1;
}
rowTotal+=smallRows+generatedRows;
const report={schema:'EC49FXR_SYMBOL_R2_ARBITRARY_RESULT_V1',scientific_pin:'BRC16943',
 model:'FROZEN_FAREY_CRT_WHOLE_ACTIVATION_SYMBOL',r:2,
 claim:'N_2(A)=15-max_{E,x}(|E|+#nonE_colors_with_at_least_two_safe_groups_avoiding_all_doubled_sums)',
 examples,small_full_color_cases:smallCases,small_rows:smallRows,
 generated_cases:generated,generated_rows:generatedRows,random_seed:49231123,
 optimum_distribution:distribution,total_exact_rows:rowTotal,status:'PASS',independent_review:'NOT_REVIEWED'};
const output=process.argv[2]||'EC49FXR_SYMBOL_R2_ARBITRARY_OUTPUT.json';
fs.writeFileSync(output,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,witness_optima:[examples.good.optimum,examples.bad.optimum],
 total_exact_rows:rowTotal,generated,generated_rows:generatedRows,distribution,output}));
