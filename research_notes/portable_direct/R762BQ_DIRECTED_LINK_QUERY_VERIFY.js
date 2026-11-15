"use strict";
// Exact signed six-Port BRC candidate incidence calculation. Node.js >= 18.
// Boolean named-Link observations; physical TRIADIC_CLOSURE_E unasserted.
function exactCertificate(){
 const full=[];
 function walk(rest,p){if(!rest.length){full.push(p.slice());return} const a=rest[0];
  for(let i=1;i<rest.length;i++)for(let j=i+1;j<rest.length;j++){
   const b=rest[i],c=rest[j],left=rest.filter(x=>x!==a&&x!==b&&x!==c);
   for(const [v,w] of [[b,c],[c,b]]){const q=p.slice();q[a]=v;q[v]=w;q[w]=a;walk(left,q)}
  }
 }
 walk([0,1,2,3,4,5],Array(6).fill(-1));
 full.sort((a,b)=>a.join(",").localeCompare(b.join(",")));
 function ck(ok,label){if(!ok)throw Error("R762BQ check failed: "+label)}
 ck(full.length===40&&new Set(full.map(p=>p.join(","))).size===40,"40 branches");
 const F=full.filter(p=>p[0]===1);ck(F.length===8,"8-fiber");
 const info=[], map=new Map();
 for(let a=0;a<6;a++)for(let b=0;b<6;b++)if(a!==b){
  let m=0;for(let i=0;i<8;i++)if(F[i][a]===b)m|=1<<i;
  if(m===0||m===255)continue;
  const q=`${a+1}->${b+1}`;info.push({query:q,mask:m});
  if(!map.has(m))map.set(m,[]);map.get(m).push(q);
  ck(Array.from({length:8},(_,i)=>!!(m&(1<<i))).filter(Boolean).length===2,"yes fiber");
 }
 const unique=[...map.keys()].sort((a,b)=>a-b);
 ck(info.length===20&&unique.length===16,"20 named 16 unique");
 const nbr=Array.from({length:8},()=>new Set());
 for(const m of unique){const e=Array.from({length:8},(_,i)=>i).filter(i=>m&(1<<i));nbr[e[0]].add(e[1]);nbr[e[1]].add(e[0])}
 const col=Array(8).fill(-1);col[0]=0;
 for(let k=0;k<8;k++)for(let i=0;i<8;i++)if(col[i]!==-1)for(const j of nbr[i]){if(col[j]===-1)col[j]=1-col[i];else ck(col[j]!==col[i],"bipartite")}
 ck(nbr.every(x=>x.size===4)&&col.filter(x=>x===0).length===4&&col.filter(x=>x===1).length===4,"K44");
 const pop=x=>{let n=0;while(x){x&=x-1;n++}return n};
 const mem=new Map();
 function opt(s){if(pop(s)<=1)return 0;if(mem.has(s))return mem.get(s);let best=100;
  for(const m of unique){const yes=s&m,no=s&(~m&255);if(yes&&no)best=Math.min(best,1+Math.max(opt(yes),opt(no)))}
  mem.set(s,best);return best;
 }
 const adaptive=opt(255);ck(adaptive===4,"adaptive optimum");
 function split(ms){return new Set(Array.from({length:8},(_,i)=>ms.map(m=>(m>>i)&1).join(""))).size===8}
 function chooseCount(xs,k){let n=0,arr=[];function rec(from){if(arr.length===k){if(split(arr))n++;return}
  for(let i=from;i<=xs.length-(k-arr.length);i++){arr.push(xs[i]);rec(i+1);arr.pop()}}
  rec(0);return n;
 }
 const zeros=[1,2,3,4].map(i=>chooseCount(unique,i));
 const nDistinct=chooseCount(unique,5),nNamed=chooseCount(info.map(x=>x.mask),5);
 ck(zeros.every(x=>x===0)&&nDistinct===672&&nNamed===1944,"nonadaptive census");
 const panel=["2->3","2->4","2->5","3->4","5->6"],pm=panel.map(t=>info.find(q=>q.query===t).mask);
 ck(split(pm),"five-query witness");
 const dup=[...map.values()].filter(x=>x.length>1);
 ck(dup.length===4&&dup.every(x=>x.length===2),"duplicates");
 return {
  schema:"ENTERPRISE_MATH_R762BQ_LINK_QUERY_CERTIFICATE_V1",
  generated_by:"R762BQ_DIRECTED_LINK_QUERY_VERIFY.js",
  arithmetic:"EXACT_FINITE_BOOLEAN_TYPED_BRC_BRANCH_CARRIER_WITH_UNIT_RATIONAL_WEIGHTS",
  scope:"CONDITIONAL_INCIDENCE_CANDIDATE_NOT_ADMITTED_NATIVE_TRIADIC_CLOSURE",
  sources:["P000 V5 frozen a72226e2430ffa4786321ac86e7f0c599d5f0389","R762BP 131bd4d77341d0fc16e9a25c85fe44ac4d5ce726"],
  count_all:full.length,
  fixed_link:"1->2",
  eight_conditional_permutations:F.map((p,index)=>({index,sigma:p.map(x=>x+1)})),
  informative_named_queries:info.length,distinct_true_sets:unique.length,
  repeated_query_name_pairs:dup,
  true_states_per_informative_query:2,
  query_graph:"K4,4",
  graph_parts:[0,1].map(v=>col.map((u,i)=>u===v?i:null).filter(i=>i!==null)),
  adaptive_minimax_extra_link_queries:adaptive,
  nonadaptive_minimal_extra_link_queries:5,
  no_separating_panels_of_sizes_1_to_4:zeros,
  distinct_five_query_panels:nDistinct,
  named_five_query_panels:nNamed,
  example_panel:panel,
  example_codes:Array.from({length:8},(_,i)=>pm.map(m=>(m>>i)&1).join("")),
  signed_fiber_size:128,hidden_sign_bits:4,
  signed_adaptive_min_total_atomic_queries:8,
  signed_nonadaptive_min_total_atomic_queries:9,
  exhaustive:{all_source_branches:40,all_conditional_branches:8,all_potential_directed_link_queries:30,all_distinct_masks:16,all_five_mask_panels:4368,all_five_named_panels:15504,dynamic_program_states:mem.size},
  math_review:"NOT_REVIEWED"
 };
}
process.stdout.write(JSON.stringify(exactCertificate(),null,2)+"\n");
