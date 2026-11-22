'use strict';
// Unit257: exact all-optimal BRC finite graph, independent stored-unit Python verifier also executed.
const runUnit257 = function runUnit257(){
 const N=12,P=12,START=[0,2,0,0],GOAL=[0,2,-12,12],BOUND=48;
 const key=s=>s.join(","), gk=key(GOAL), sk=key(START);
 const basis=[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[-1,0,0,0,0,0],[0,-1,0,0,0,0],[0,0,-1,0,0,0]];
 const x=Array(13);for(let r=0;r<6;r++){x[2*r]=basis[r];x[2*r+1]=basis[r].map((z,i)=>z+basis[(r+1)%6][i]);}x[P]=[0,0,0,0,0,0];
 const axis=(u,v)=>{let d=x[v].map((z,i)=>z-x[u][i]),p=d.map((z,i)=>[i,z]).filter(z=>z[1]);if(p.length!==1||Math.abs(p[0][1])!==1)throw Error("nonprimitive");return (p[0][1]>0?"+":"-")+"e"+p[0][0]};
 const cases=[];
 for(const [ingress,egress] of [[6,0],[8,2]]){
   const dist=new Map([[sk,0]]), nodes=new Map([[sk,START]]), levels=[[sk]], q=[sk],adj=new Map();
   for(let ix=0;ix<q.length;ix++){
     const k=q[ix],s=nodes.get(k),dep=dist.get(k);if(dep>=28)continue;
     let out=[];
     for(let who=0;who<2;who++){
       let u=s[who],moves=u===P?[[egress,0]]:[[(u+1)%N,1],[(u+11)%N,-1],...(u===ingress?[[P,0]]:[])];
       for(let [v,w] of moves){
         if(v===s[1-who])continue;let t=s.slice();t[who]=v;t[who+2]+=w;if(Math.max(Math.abs(t[2]),Math.abs(t[3]))>BOUND)continue;
         let tk=key(t);if(!dist.has(tk)){dist.set(tk,dep+1);nodes.set(tk,t);q.push(tk);if(!levels[dep+1])levels[dep+1]=[];levels[dep+1].push(tk)}
         if(dist.get(tk)===dep+1)out.push({tk,who,u,v,w,sign:axis(u,v)});
       }
     }
     adj.set(k,out);
   }
   if(dist.get(gk)!==28)throw Error("distance not 28");
   const suffix=new Map([[gk,1]]);for(let depth=27;depth>=0;depth--){for(const k of levels[depth]){suffix.set(k,(adj.get(k)||[]).reduce((n,e)=>n+(suffix.get(e.tk)||0),0));}}
   let first={},presence=new Map(),multiplicity={},positions=new Set(),precontexts=new Map(),enumerated=0,alt=null;
   const rec=(k,trace)=>{
     if(k===gk){
       if(trace.length!==28)throw Error("length");
       enumerated++;let e=trace[0],name=(e.who===0?"A":"B")+":x"+e.u+"->x"+e.v;first[name]=(first[name]||0)+1;
       let count=new Map();for(let step of trace){let ek=step.u+">"+step.v;count.set(ek,(count.get(ek)||0)+1);}
       for(let [ek,m] of count){presence.set(ek,(presence.get(ek)||0)+1);if(ek==="0>11")multiplicity[m]=(multiplicity[m]||0)+1;}
       if(e.who===1&&alt===null)alt=trace.map(({who,u,v,sign})=>[(who?"B":"A"),u===P?"P":"x"+u,v===P?"P":"x"+v,sign]);
       return;
     }
     for(const e of adj.get(k)||[]){if(!(suffix.get(e.tk)>0))continue;if(e.u===0&&e.v===11){positions.add(trace.length+1);precontexts.set((trace.length+1)+":"+k,[trace.length+1,...nodes.get(k),e.who])}rec(e.tk,[...trace,e]);}
   };rec(sk,[]);
   if(enumerated!==suffix.get(sk))throw Error("path count mismatch");
   let mandatory=[...presence.entries()].filter(([_,v])=>v===enumerated).map(([ek])=>{let [u,v]=ek.split(">").map(Number);return [u,v,axis(u,v)]}).sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
   let negative=mandatory.filter(x=>x[2].startsWith("-"));
   cases.push({ingress,egress,cost:28,all_shortest_histories:enumerated,bfs_states_through_depth28:dist.size,first_event_counts:first,
     mandatory_negative_native_links:negative,mandatory_directed_links:mandatory,x0_x11_multiplicity:multiplicity,
     x0_x11_possible_event_positions:[...positions].sort((a,b)=>a-b),x0_x11_precontexts:[...precontexts.values()].sort((a,b)=>a[0]-b[0]),B_first_optimal_example:alt});
 }
 if(cases.some(c=>c.all_shortest_histories!==2832)||cases[0].first_event_counts["A:x0->x11"]!==2200||cases[1].first_event_counts["A:x0->x11"]!==632)throw Error("crosscheck");
 const c2=new Set(cases[1].mandatory_negative_native_links.map(x=>x.join(":")));
 const shared=cases[0].mandatory_negative_native_links.filter(x=>c2.has(x.join(":")));
 if(shared.length!==8||cases[0].x0_x11_precontexts.length!==10||cases[1].x0_x11_precontexts.length!==16)throw Error("cut mismatch");
 return {schema:"X6_TIME_UNIT257_ALL_OPTIMAL_BRC_NEGATIVE_CUT_CERT_V1",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",
  frozen_science:"enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
  original:"f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json",
  model:"CONDITIONAL_SIGNED_WHOLE_TRIAD_SERIAL_OCCUPANCY_DIRECTED_PORT",cases,
  total_all_optimal_histories:cases.reduce((n,x)=>n+x.all_shortest_histories,0),
  shared_mandatory_negative_native_links:shared,
  physical_native_execution:false,author_proved:true,independent_review:false,admission:false};
};
const certificate=runUnit257();
console.log(JSON.stringify(certificate,null,2));
