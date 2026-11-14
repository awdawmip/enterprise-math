#!/usr/bin/env node
'use strict';
/** EC49FBM: exact positive-BRC-key/window feasibility with the frozen nine-state observer.
 * Run: node VERIFY_EC49FBM.js
 * Reads the 124-pair EC49FBL source report from the sibling directory.
 */
const fs=require('node:fs'),path=require('node:path');
function analyze(input){
  "use strict";
  const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
  const SIG=[0,0,4,1,16,32,8,2,0],CLASS=[0,1,1,2,3,4],CLAUSES=[18,20,33,40];
  function validNum(n){if(!Number.isSafeInteger(n))throw Error("unsafe count "+n);return n;}
  function fact(n){let q=1;for(let i=2;i<=n;i++)q*=i;return q;}
  function keyCounts(h,K){const [x,y,z]=K;const n=[z-1,x+y-h-1,z,h+1-y-2*z,h+1-x];return n.some(v=>v<0)?null:n;}
  const computed=new Map();
  function observer(h,K){
    const id=h+":"+K.join(",");if(computed.has(id))return computed.get(id);
    const cnt=keyCounts(h,K);if(!cnt){const result={signature_counts:{},accepted:0,cover4:false,cover9:false};computed.set(id,result);return result;}
    const cache=new Map();
    function visit(v,state){
      const key=v.join(",")+":"+state;if(cache.has(key))return cache.get(key);
      if(v.every(x=>x===0)){const o=Array(9).fill(0);o[state]=1;return o;}
      const out=Array(9).fill(0);
      for(let i=0;i<6;i++){const c=CLASS[i];if(v[c]>0){v[c]--;const nxt=visit(v,T[state][i]);v[c]++;for(let t=0;t<9;t++)out[t]=validNum(out[t]+nxt[t]);}}
      cache.set(key,out);return out;
    }
    const states=visit(cnt,0),signatures={};let mask=0;
    for(let s=0;s<9;s++){if(SIG[s]&&states[s]){signatures[SIG[s]]=states[s];mask|=SIG[s];}}
    const result={signature_counts:signatures,accepted:validNum(Object.values(signatures).reduce((a,b)=>a+b,0)),cover4:CLAUSES.every(c=>(mask&c)!==0),cover9:(signatures[16]??0)>0&&(signatures[32]??0)>0,signature_mask:mask};
    computed.set(id,result);return result;
  }
  if(input.aggregate.pairs!==124||input.details.length!==124)throw Error("source pair count mismatch");
  const records=[];let h9=0,fixed=0,moved=0,rank69=0,rank69pairs=0;
  for(const row of input.details){
    const L=row.L,M=row.M,windows=[];
    if(L.length!==3||M.length!==3)throw Error("invalid source key");
    for(let h=4;h<=9;h++){
      const a=observer(h,h<=6?L:M);
      windows.push({h,signature_mask:a.signature_mask??0,accepted:a.accepted,rank_clauses_satisfied:h<9?a.cover4:a.cover9});
    }
    const nine=observer(9,M),[X,Y,Z]=M;
    const keyCriterion=(X+Y===10&&Z>=1&&X>=2*Z+1&&Y>=1);
    if(nine.cover9!==keyCriterion)throw Error("H9 iff criterion mismatch "+M);
    if(keyCriterion){
      const a=Z-1,e=Z,f=X-2*Z,g=Y;
      const nf=fact(8)/(fact(a)*fact(e)*fact(f-1)*fact(g));
      const ng=fact(8)/(fact(a)*fact(e)*fact(f)*fact(g-1));
      if(nf!==nine.signature_counts[16]||ng!==nine.signature_counts[32])throw Error("multinomial count mismatch "+M);
      h9++;
    }
    const fixedPass=windows.every(v=>v.rank_clauses_satisfied);
    const alternativePass=[4,5].every(h=>observer(h,L).cover4)&&[6,7,8].every(h=>observer(h,M).cover4)&&nine.cover9;
    if(fixedPass)fixed++;
    if(alternativePass)moved++;
    const p69=row.horizons.find(q=>q.from===6&&q.to===9);
    if(p69.clause_compatible>0){rank69+=p69.clause_compatible;rank69pairs++;}
    records.push({L,M,h9_eligible:keyCriterion,fixed_L_H4_H6_M_H7_H9:fixedPass,shift_H6_to_M:alternativePass,clause_inheritance_all_windows:row.clause_compatible,clause_inheritance_H6_H9:p69.clause_compatible,windows});
  }
  if(h9!==52||fixed!==27||moved!==28||rank69!==2000||rank69pairs!==12)throw Error("unexpected aggregate "+JSON.stringify({h9,fixed,moved,rank69,rank69pairs}));
  const topFixed=records.filter(v=>v.fixed_L_H4_H6_M_H7_H9).sort((a,b)=>b.clause_inheritance_all_windows-a.clause_inheritance_all_windows).slice(0,8).map(v=>({L:v.L,M:v.M,inheritance:v.clause_inheritance_all_windows,H6H9:v.clause_inheritance_H6_H9}));
  const topShift=records.filter(v=>v.shift_H6_to_M).sort((a,b)=>b.clause_inheritance_all_windows-a.clause_inheritance_all_windows).slice(0,8).map(v=>({L:v.L,M:v.M,inheritance:v.clause_inheritance_all_windows,H6H9:v.clause_inheritance_H6_H9}));
  return {schema:"EC49FBM_EXACT_H9_SPINE_SCHEDULE_FILTER_V1",date:"2026-11-05",status:"PASS",scientific_input_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",source_report:"EC49FBL/EXACT_REPORT_EC49FBL.json@d0f10160abe2fc77fdeaa800f7536ea29445c72f",rank_signature_clauses_H4_H8:CLAUSES,rank_signature_clauses_H9:[16,32],pair_count:records.length,summary:{H9_key_eligible_pairs:h9,fixed_L_H4_H6_M_H7_H9_eligible_pairs:fixed,alternative_L_H4_H5_M_H6_H9_eligible_pairs:moved,H6_to_H9_clause_compatible_inheritances:rank69,H6_to_H9_positive_pairs:rank69pairs},top_eligible_fixed:topFixed,top_eligible_alternative:topShift,records};
}
const input=JSON.parse(fs.readFileSync(path.join(__dirname,'..','EC49FBL_SUFFIX_AUTOMATON_TRANSFER','EXACT_REPORT_EC49FBL.json'),'utf8'));
console.log(JSON.stringify(analyze(input),null,2));
