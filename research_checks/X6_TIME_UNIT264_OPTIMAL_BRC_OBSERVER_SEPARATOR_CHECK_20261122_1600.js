'use strict';
// Unit264, exact shortest-path finite BRC graph, Source-frozen model. Native physical operations are not simulated.
const runUnit264=function runUnit264() {
 const P=12,B=48,START=[0,2,0,0],GOAL=[0,2,-12,12],S=START.join(','),G=GOAL.join(',');
 const known={'6,0':'LKJIHGMALKJIHGMdefghijklabAc','8,2':'LKJdefghimIHGFEDCBAcdefghimc'};
 function solve(i,j){
  const dist=new Map([[S,0]]),states=new Map([[S,START]]),layers=[[S]],edges=new Map(),q=[S];
  for(let h=0;h<q.length;h++){const k=q[h],a=states.get(k),d=dist.get(k);if(d===28)continue;
   const e=[];
   for(let t=0;t<2;t++){const u=a[t],moves=u===P?[[j,0]]:[[(u+1)%12,1],[(u+11)%12,-1],...(u===i?[[P,0]]:[])];
    for(const [v,w]of moves){if(v===a[1-t])continue;const b=a.slice();b[t]=v;b[t+2]+=w;
     if(Math.max(Math.abs(b[2]),Math.abs(b[3]))>B)continue;
     const z=b.join(',');if(!dist.has(z)){dist.set(z,d+1);states.set(z,b);q.push(z);(layers[d+1]??=[]).push(z);}
     if(dist.get(z)===d+1)e.push(z);
    }
   }edges.set(k,e);
  }
  if(dist.get(G)!==28)throw Error('cost mismatch');
  const suffix=new Map([[G,1]]);for(let t=27;t>=0;t--)for(const k of layers[t])suffix.set(k,(edges.get(k)||[]).reduce((s,z)=>s+(suffix.get(z)||0),0));
  if(suffix.get(S)!==2832)throw Error('count mismatch');
  const forward=new Map([[S,1]]),snap=[];
  for(let t=0;t<=28;t++){const a=[];
    for(const k of layers[t]){const n=(forward.get(k)||0)*(suffix.get(k)||0);
     if(!n)continue;
     a.push({state:states.get(k),count:n});
     if(t<28)for(const z of edges.get(k)||[])if(suffix.get(z))forward.set(z,(forward.get(z)||0)+(forward.get(k)||0));
    }
    if(a.reduce((s,z)=>s+z.count,0)!==2832)throw Error('weighted mismatch '+t);
    a.sort((v,w)=>v.state.join(',').localeCompare(w.state.join(',')));
    snap.push(a);
  }
  let cur=START.slice(),eventProof=[];const word=known[[i,j].join(',')];
  for(let t=1;t<=word.length;t++){const ch=word[t-1],who=ch===ch.toUpperCase()?0:1,v=ch.charCodeAt(0)-(who?97:65),u=cur[who];
   if(v===cur[1-who])throw Error('occupied');
   const w=u===P||v===P?0:v===(u+1)%12?1:v===(u+11)%12?-1:999;
   if(w===999||(u===P&&v!==j)||(v===P&&u!==i))throw Error('bad witness');
   cur[who]=v;cur[who+2]+=w;
   if([1,3,6,7].includes(t))eventProof.push({t,mover:who?'B':'A',src:u,dest:v,kind:u===P||v===P?'PORT':'OUTER',after:cur.slice()});
  }
  if(cur.join(',')!==G)throw Error('bad terminal');
  return {port:[i,j],histories:suffix.get(S),states:snap,source_witness:word,eventProof};
 }
 const a=solve(6,0),b=solve(8,2),rows=[];
 for(let t=0;t<=28;t++){const aa=a.states[t],bb=b.states[t],as=new Set(aa.map(x=>x.state.join(','))),bs=new Set(bb.map(x=>x.state.join(',')));
  const ap=new Set(aa.map(x=>x.state.slice(0,2).join(','))),bp=new Set(bb.map(x=>x.state.slice(0,2).join(',')));
  rows.push({t,states60:aa.length,states82:bb.length,intersection:[...as].filter(x=>bs.has(x)).length,
   positionsIntersection:[...ap].filter(x=>bp.has(x)).length,
   histories60AtCommon:aa.filter(x=>bs.has(x.state.join(','))).reduce((s,x)=>s+x.count,0)});
 }
 if(rows.slice(4,8).map(x=>x.intersection).join(',')!=='3,2,1,0')throw Error('split mismatch');
 if(rows.slice(7,28).some(x=>x.intersection))throw Error('long split mismatch');
 if(rows[7].positionsIntersection||rows[28].intersection!==1)throw Error('observer mismatch');
 return {schema:'X6_TIME_UNIT264_BRC_OPTIMAL_OBSERVER_SEPARATOR_CERT_V1',date:'2026-11-22',
  task:'RS-X6-NATIVE-TIME-DYNAMICS',science_pin:'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  original_pin:'f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json',
  model:'CONDITIONAL_TWO_INTACT_LABELED_TRIADS_SERIAL_SIGNED_OUTER_DIRECTED_CENTER_PORT_EMPTY_TARGET',
  total_optimal_histories:5664,minimum_steps:28,unit251_252_original_observer_events:[3,7],timeline:rows,
  observer_support:{t3:{port60:a.states[3],port82:b.states[3]},t6:{port60:a.states[6],port82:b.states[6]},t7:{port60:a.states[7],port82:b.states[7]}},
  witnesses:[{port:a.port,route:a.source_witness,sampled_events:a.eventProof},{port:b.port,route:b.source_witness,sampled_events:b.eventProof}],
  first_forced_distinguishable_event:7,disjoint_complete_BRC_states_for_events_7_through_27:true,
  event7_positions_also_disjoint:true,original_C24_C3_sensors_executed:false,native_source_move_executed:false,
  review:'UNREVIEWED',admission:'NOT_ADMITTED'};
};
console.log(JSON.stringify(runUnit264(),null,2));
