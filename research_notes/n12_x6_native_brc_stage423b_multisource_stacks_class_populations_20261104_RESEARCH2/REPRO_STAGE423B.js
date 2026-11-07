#!/usr/bin/env node
"use strict";
// Stage423-B: exact finite cross-check; formal k-source stacks, not physical BRC dynamics.
function classKey(n,r,s,i){
  function tail(positions,L){let w="";for(let k=n-L+1;k<=n;k++)w+=positions.includes(k)?"B":"A";return w;}
  if(s===n-5)return "B_cap";
  if(i<=n-3)return "R:"+tail([i],6)+":"+tail([r,s],6);
  return "F:"+i+":"+tail([r,s],7);
}
function expected(n){
  const m=new Map();
  for(const [sz,num] of [[(n-8)*(n-9),1],[2*(n-8),1],[n-7,6],[n-8,2],[1,14]])
    m.set(sz,(m.get(sz)||0)+num);
  return [...m].sort((a,b)=>a[0]-b[0]);
}
function census(){
  let total=0, snapshots={};
  for(let n=11;n<=100;n++){
    const m=new Map();
    for(let r=2;r<=n-3;r++)for(let s=r+2;s<=n-1;s++)for(const i of [r,s]){
      const key=classKey(n,r,s,i);m.set(key,(m.get(key)||0)+1);total++;
    }
    if(m.size!==24)throw Error("class count at "+n);
    const histogram=new Map();
    for(const size of m.values())histogram.set(size,(histogram.get(size)||0)+1);
    const got=[...histogram].sort((a,b)=>a[0]-b[0]), want=expected(n);
    if(JSON.stringify(got)!==JSON.stringify(want))throw Error("counts at "+n);
    if(got.reduce((a,x)=>a+x[0]*x[1],0)!==(n-3)*(n-4))throw Error("fiber at "+n);
    if([11,12,16,30,100].includes(n))snapshots[n]={histories:(n-3)*(n-4),classes:24,sizes:Object.fromEntries(got)};
  }
  return {total,snapshots};
}
function multisource(){
  const deletion=[];
  for(let a=0;a<=2;a++)for(let b=0;b<=2;b++)for(let c=0;c<=2;c++)
    if(a+b+c)deletion.push([a,b,c]);
  const start=Array(10).fill(0), key=s=>s.join(",");
  const seen=new Set([key(start)]);let layer=[start],edges=0;
  for(let depth=0;depth<5;depth++){
    const next=[];
    for(const st of layer){
      const succ=[];
      const app=st.slice();for(let j=0;j<3;j++)app[j]++;succ.push(app);
      for(let j=1;j<=2;j++)if(st[j]+4-st[3+j]>0){
        const x=st.slice();if(x[j])x[j]--;else x[3+j]++;x[5+j]++;succ.push(x);
      }
      for(const b of deletion)if(b.every((v,j)=>st[j]+4-st[3+j]>=v)){
        const x=st.slice();
        for(let j=0;j<3;j++){x[j]=Math.max(0,st[j]-b[j]);x[3+j]+=Math.max(0,b[j]-st[j]);}
        x[8]+=Math.max(0,b[1]-b[0]);x[9]+=Math.max(0,b[2]-b[0]);succ.push(x);
      }
      for(const x of succ){
        edges++;
        if(x[4]>x[3]+x[6]+x[8]||x[5]>x[3]+x[7]+x[9])
          throw Error("multisource frontier failed depth "+depth+": "+x);
        const k=key(x);if(!seen.has(k)){seen.add(k);next.push(x);}
      }
    }
    layer=next;
  }
  if(edges!==175678||seen.size!==29252)throw Error("independent Python cross-check count mismatch");
  return {sources:3,original_length_each:4,depth:5,deletion_arities:deletion.length,
          distinct_states:seen.size,checked_transitions:edges,
          tight_counterexample:{P:"AA",Q:"AB",operator:"Q-only inverse CANCEL",dP:0,dQ:2,tQ:0,extra:2}};
}
function verify(){
  const c=census(),stack=multisource();
  return {marker:"STAGE423B_MULTISOURCE_BOUND_CLASS_POPULATIONS_PASS",
    date:"2026-11-04",frozen_global:"bf84bd7c61a2444b59b1da96be57df0e9ae47e53",
    frozen_em:"2af3fc484eb11060b69e0afc1b562bcaf5ad1419",
    p000_blob:"bcc2590d3168a28f72e8b9f0f9b1f76faadcd488",
    theorem:"d_j <= d_anchor + t_j + sum_e max(0,b_ej-b_eanchor)",
    populations:"(n-8)(n-9) x1; 2(n-8) x1; (n-7) x6; (n-8) x2; 1 x14; all n>=11 conditional on Stage422 24-class quotient",
    n_range:[11,100],total_original_pairs_checked:c.total,snapshots:c.snapshots,stack,
    evidence_status:"FINITE_EXACT_EXECUTED; UNBOUNDED_RESULT_WRITTEN_PROOF; UNREVIEWED/NOT_ADMITTED",
    physical_BRC_experiment_executed:false};
}
if(require.main===module)process.stdout.write(JSON.stringify(verify(),null,2)+"\n");