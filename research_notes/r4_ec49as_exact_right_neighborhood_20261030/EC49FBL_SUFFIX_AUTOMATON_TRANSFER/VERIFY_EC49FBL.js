'use strict';
// Exact reproducible EC49FBL integer suffix-transfer scan; Node.js standard library only.
const PAIRS=[[[3,2,1],[6,4,1]],[[3,3,1],[5,5,1]],[[3,3,1],[6,4,1]],[[3,3,1],[6,5,1]],[[3,3,1],[7,3,1]],[[3,3,1],[7,3,2]],[[3,3,1],[7,4,1]],[[3,3,1],[7,5,1]],[[4,1,1],[6,4,1]],[[4,2,1],[5,5,1]],[[4,2,1],[6,4,1]],[[4,2,1],[6,5,1]],[[4,2,1],[7,3,1]],[[4,2,1],[7,3,2]],[[4,2,1],[7,4,1]],[[4,2,1],[7,5,1]],[[4,3,1],[4,6,1]],[[4,3,1],[5,5,1]],[[4,3,1],[5,6,1]],[[4,3,1],[6,4,1]],[[4,3,1],[6,4,2]],[[4,3,1],[6,5,1]],[[4,3,1],[6,6,1]],[[4,3,1],[7,3,1]],[[4,3,1],[7,3,2]],[[4,3,1],[7,4,1]],[[4,3,1],[7,4,2]],[[4,3,1],[7,5,1]],[[4,3,1],[7,6,1]],[[4,3,1],[8,2,1]],[[4,3,1],[8,2,2]],[[4,3,1],[8,2,3]],[[4,3,1],[8,3,1]],[[4,3,1],[8,3,2]],[[4,3,1],[8,4,1]],[[4,3,1],[8,4,2]],[[4,3,1],[8,5,1]],[[4,3,1],[8,6,1]],[[5,1,1],[5,5,1]],[[5,1,1],[6,4,1]],[[5,1,1],[6,5,1]],[[5,1,1],[7,3,1]],[[5,1,1],[7,3,2]],[[5,1,1],[7,4,1]],[[5,1,1],[7,5,1]],[[5,1,2],[5,5,1]],[[5,1,2],[6,4,1]],[[5,1,2],[6,5,1]],[[5,1,2],[7,3,1]],[[5,1,2],[7,3,2]],[[5,1,2],[7,4,1]],[[5,1,2],[7,5,1]],[[5,2,1],[4,6,1]],[[5,2,1],[5,5,1]],[[5,2,1],[5,6,1]],[[5,2,1],[6,4,1]],[[5,2,1],[6,4,2]],[[5,2,1],[6,5,1]],[[5,2,1],[6,6,1]],[[5,2,1],[7,3,1]],[[5,2,1],[7,3,2]],[[5,2,1],[7,4,1]],[[5,2,1],[7,4,2]],[[5,2,1],[7,5,1]],[[5,2,1],[7,6,1]],[[5,2,1],[8,2,1]],[[5,2,1],[8,2,2]],[[5,2,1],[8,2,3]],[[5,2,1],[8,3,1]],[[5,2,1],[8,3,2]],[[5,2,1],[8,4,1]],[[5,2,1],[8,4,2]],[[5,2,1],[8,5,1]],[[5,2,1],[8,6,1]],[[5,3,1],[3,7,1]],[[5,3,1],[4,6,1]],[[5,3,1],[4,7,1]],[[5,3,1],[5,5,1]],[[5,3,1],[5,5,2]],[[5,3,1],[5,6,1]],[[5,3,1],[5,7,1]],[[5,3,1],[6,4,1]],[[5,3,1],[6,4,2]],[[5,3,1],[6,5,1]],[[5,3,1],[6,5,2]],[[5,3,1],[6,6,1]],[[5,3,1],[6,7,1]],[[5,3,1],[7,3,1]],[[5,3,1],[7,3,2]],[[5,3,1],[7,3,3]],[[5,3,1],[7,4,1]],[[5,3,1],[7,4,2]],[[5,3,1],[7,5,1]],[[5,3,1],[7,5,2]],[[5,3,1],[7,6,1]],[[5,3,1],[7,7,1]],[[5,3,1],[8,2,1]],[[5,3,1],[8,2,2]],[[5,3,1],[8,2,3]],[[5,3,1],[8,3,1]],[[5,3,1],[8,3,2]],[[5,3,1],[8,3,3]],[[5,3,1],[8,4,1]],[[5,3,1],[8,4,2]],[[5,3,1],[8,5,1]],[[5,3,1],[8,5,2]],[[5,3,1],[8,6,1]],[[5,3,1],[8,7,1]],[[5,3,1],[9,1,1]],[[5,3,1],[9,1,2]],[[5,3,1],[9,1,3]],[[5,3,1],[9,1,4]],[[5,3,1],[9,2,1]],[[5,3,1],[9,2,2]],[[5,3,1],[9,2,3]],[[5,3,1],[9,3,1]],[[5,3,1],[9,3,2]],[[5,3,1],[9,3,3]],[[5,3,1],[9,4,1]],[[5,3,1],[9,4,2]],[[5,3,1],[9,5,1]],[[5,3,1],[9,5,2]],[[5,3,1],[9,6,1]],[[5,3,1],[9,7,1]]];
const result=(function compute(PAIRS){
 const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
 const S=[0,0,4,1,16,32,8,2,0];
 const R={4:[1,2,4,8],5:[1,2,4,8],6:[16,32],7:[1,2,4,8],8:[1,2,4,8],9:[16,32]};
 const symbols="acdefg";
 const n6=()=>Array(9).fill(0);
 const valid=x=>{if(!Number.isSafeInteger(x))throw Error("unsafe integer "+x);return x};
 function exactCounts(h,K){
   const [x,y,z]=K;
   const n={a:z-1,cd:x+y-h-1,e:z,f:h+1-y-2*z,g:h+1-x};
   return Object.values(n).some(v=>v<0)?null:n;
 }
 function initialStates(h,K){
   const n=exactCounts(h,K);
   if(!n)return n6();
   const memo=new Map();
   function visit(state){
     const mk=Object.values(n).join(",")+":"+state;
     if(memo.has(mk))return memo.get(mk);
     if(Object.values(n).every(v=>v===0)){const a=n6();a[state]=1;return a}
     const out=n6();
     for(let i=0;i<6;i++){
       const ch=symbols[i],key=ch==="c"||ch==="d"?"cd":ch;
       if(n[key]){
         n[key]--;
         const nxt=visit(T[state][i]);n[key]++;
         for(let j=0;j<9;j++)out[j]=valid(out[j]+nxt[j]);
       }
     }
     memo.set(mk,out);return out;
   }
   return visit(0);
 }
 function suffixStateCounts(h,H,L,M,state){
   const [x,y,z]=L,[X,Y,Z]=M,d=H-h;
   const n={a:Z-z,cd:(X-x)+(Y-y)-d,e:Z-z,f:d-(Y-y)-2*(Z-z),g:d-(X-x)};
   if(Object.values(n).some(v=>v<0))return n6();
   const memo=new Map();
   function visit(st){
     const mk=Object.values(n).join(",")+":"+st;
     if(memo.has(mk))return memo.get(mk);
     if(Object.values(n).every(v=>v===0)){const a=n6();a[st]=1;return a}
     const out=n6();
     for(let i=0;i<6;i++){
       const ch=symbols[i],key=ch==="c"||ch==="d"?"cd":ch;
       if(n[key]){
         n[key]--;
         const nxt=visit(T[st][i]);n[key]++;
         for(let j=0;j<9;j++)out[j]=valid(out[j]+nxt[j]);
       }
     }
     memo.set(mk,out);return out;
   }
   return visit(state);
 }
 const memoEarly=new Map(), detail=[],aggregate={pairs:PAIRS.length,positive_pairs:0,zero_pairs:0,all_nonzero_terminal_prefix_pairs:0,clause_compatible_terminal_prefix_pairs:0,same_signature_terminal_prefix_pairs:0};
 for(const [L,M] of PAIRS){
   let total=0,clause=0,same=0;
   const horizons=[];
   for(let h=4;h<=6;h++){
     const ek=h+":"+L.join();
     if(!memoEarly.has(ek))memoEarly.set(ek,initialStates(h,L));
     const base=memoEarly.get(ek);
     for(let H=7;H<=9;H++){
       let all=0,fit=0,preserve=0;
       for(let s=0;s<9;s++){
         if(!S[s]||base[s]===0)continue;
         const out=suffixStateCounts(h,H,L,M,s);
         for(let t=0;t<9;t++){
           if(!S[t]||!out[t])continue;
           const n=valid(base[s]*out[t]);
           all=valid(all+n);
           if(R[h].includes(S[s])&&R[H].includes(S[t])) fit=valid(fit+n);
           if(S[s]===S[t]) preserve=valid(preserve+n);
         }
       }
       total=valid(total+all);clause=valid(clause+fit);same=valid(same+preserve);
       horizons.push({from:h,to:H,all,clause_compatible:fit,same_signature:preserve});
     }
   }
   if(total)aggregate.positive_pairs++;else aggregate.zero_pairs++;
   aggregate.all_nonzero_terminal_prefix_pairs=valid(aggregate.all_nonzero_terminal_prefix_pairs+total);
   aggregate.clause_compatible_terminal_prefix_pairs=valid(aggregate.clause_compatible_terminal_prefix_pairs+clause);
   aggregate.same_signature_terminal_prefix_pairs=valid(aggregate.same_signature_terminal_prefix_pairs+same);
   detail.push({L,M,all:total,clause_compatible:clause,same_signature:same,horizons});
 }
 const get=(L,M)=>detail.find(v=>v.L.join()===L.join()&&v.M.join()===M.join());
 const anchors=[
   {L:[4,3,1],M:[8,2,1],expected:[0,0,0]},
   {L:[5,2,1],M:[8,2,1],expected:[194,194,194]},
   {L:[4,3,1],M:[7,4,2],expected:[4920,1440,4320]},
   {L:[4,2,1],M:[7,3,2],expected:[2304,1440,2016]}
 ];
 for(const a of anchors){
   const p=get(a.L,a.M);
   if(!p||[p.all,p.clause_compatible,p.same_signature].some((v,i)=>v!==a.expected[i]))throw Error("anchor mismatch "+JSON.stringify(a));
 }
 if(aggregate.pairs!==124||aggregate.positive_pairs!==94||aggregate.zero_pairs!==30||aggregate.all_nonzero_terminal_prefix_pairs!==141920||aggregate.clause_compatible_terminal_prefix_pairs!==39576||aggregate.same_signature_terminal_prefix_pairs!==129828)throw Error("aggregate mismatch");
 const sorted=[...detail].sort((a,b)=>b.clause_compatible-a.clause_compatible||b.all-a.all);
 return {schema:"EC49FBL_TERMINAL_SUFFIX_TRANSFER_V1",date:"2026-11-05",status:"PASS",frozen_scientific_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",feasible_pair_source:"awdawmip/enterprise-math@26d3b584ca34ff7439ba0c5879f93a1cc40ee29a:research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FBH_ALL_LATE_KEY_EARLY70/EXACT_REPORT_EC49FBH.json#pairs[minH2H6!=null]",universe:"124 previously feasible early H2-H6 L/M pairs; independently count possible early H4-6 to late H7-9 terminal-prefix pairs; no assumption each fixed schedule has a full H9 rank witness",observer_signature:S,required_signatures:R,aggregate,top_by_clause_compatible:sorted.slice(0,8).map(({L,M,all,clause_compatible,same_signature})=>({L,M,all,clause_compatible,same_signature})),details:detail};
})(PAIRS);
console.log(JSON.stringify(result,null,2));
