/* Unit259 reproducible exact conditional BRC event-clock check; Node.js >=18. */
const result=(function checker(){
  const PORTS=[[6,0],[8,2]],START=[0,2,0,0],LIMIT=28;let assertions=0;
  const eq=(v,msg)=>{assertions++;if(!v)throw Error("ASSERT "+msg);};
  const key=s=>s.join(",");
  const parityPos=x=>x===12?1:(x&1);
  const observableParity=s=>parityPos(s[0])^parityPos(s[1]);
  function edges(s,ingress,egress){
    const out=[];
    for(let t=0;t<2;t++){
      const x=s[t],other=s[1-t];
      const opts=x===12?[[egress,0]]:[[(x+1)%12,1],[(x+11)%12,-1],...(x===ingress?[[12,0]]:[])];
      for(const [y,w] of opts){
        if(y===other)continue;
        const z=s.slice();z[t]=y;z[t+2]+=w;
        out.push({actor:t,from:x,to:y,windingDelta:w,state:z});
      }
    }
    return out;
  }
  const portResults=[];
  for(const [i,j] of PORTS){
    eq(i%2===0&&j%2===0,"center Port even endpoints");
    const foundLoop1=edges(START,i,j).find(e=>e.actor===0&&e.from===0&&e.to===1);
    eq(!!foundLoop1&&foundLoop1.windingDelta===1,"signed first loop edge");
    const foundLoop2=edges(foundLoop1.state,i,j).find(e=>e.actor===0&&e.from===1&&e.to===0);
    eq(!!foundLoop2&&foundLoop2.windingDelta===-1&&key(foundLoop2.state)===key(START),"2-event legal return");
    let layer=new Map([[key(START),START]]);
    const layerSizes=[],phases=new Map();let checkedTransitions=0;
    for(let d=0;d<=LIMIT;d++){
      layerSizes.push(layer.size);
      const next=new Map();
      for(const [k,s] of layer){
        eq(observableParity(s)===(d%2),"event parity recovered at depth "+d);
        phases.set(k,(phases.get(k)||0)|(1<<(d%4)));
        if(d===LIMIT)continue;
        for(const e of edges(s,i,j)){
          eq(observableParity(e.state)===1-observableParity(s),"one event toggles parity");
          checkedTransitions++;
          next.set(key(e.state),e.state);
        }
      }
      layer=next;
    }
    const mixed=[...phases.values()].filter(mask=>mask===5||mask===10).length;
    eq(layerSizes[LIMIT]===1814,"depth 28 reachable layer");
    eq(phases.size===3711,"distinct reachable full BRC states up to 28");
    eq(mixed===3039,"phase-ambiguous full BRC states up to 28");
    eq(phases.get(key(START))===5,"initial state phase 0 and 2");
    portResults.push({port:[i,j],max_depth:LIMIT,layer_depth_28:layerSizes[LIMIT],distinct_full_BRC_states_through_28:phases.size,full_BRC_states_with_both_time_mod4_phases:mixed,initial_state_time_mod4_mask:phases.get(key(START)),checked_primitive_transitions:checkedTransitions,first_15_layer_sizes:layerSizes.slice(0,15)});
  }
  const repairTests=[];
  for(let m=1;m<=10;m++){
    const modulus=2**m,extra=2**(m-1),seen=new Set();
    for(let k=0;k<extra;k++)seen.add((2*k)%modulus);
    eq(seen.size===extra,"return-loop time fiber cardinality m="+m);
    for(let t=0;t<2*modulus;t++){
      const q=t%2,h=Math.floor(t/2)%extra;
      const qp=1-q,hp=(h+q)%extra;
      eq((2*h+q)%modulus===t%modulus,"clock reconstruction m="+m);
      eq((2*hp+qp)%modulus===(t+1)%modulus,"half-clock carry m="+m);
    }
    repairTests.push({m,modulus,possible_initial_state_phases:extra,necessary_extra_bits:m-1});
  }
  eq(portResults[0].distinct_full_BRC_states_through_28===portResults[1].distinct_full_BRC_states_through_28,"port replication");
  return {schema:"X6_TIME_UNIT259_BIPARTITE_EVENT_CLOCK_REPAIR_CERT_V1",model:"CONDITIONAL_SIGNED_SERIAL_TWO_TRIAD_BRC",frozen_scientific_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",original_BRC_commit:"f56840285cafeb9f5767ea91e903e1f53808186f",starting_state:START,center_cell:12,port_results:portResults,clock_repair_tests:repairTests,unit_loop:["A:x0->x1,+e1","A:x1->x0,-e1"],parity_rule:"t mod 2 = kappa(posA) XOR kappa(posB), with kappa(outer x_r)=r mod 2, kappa(P)=1",repair_rule:"For t mod 2^m use q=kappa(A) XOR kappa(B) and h=floor(t/2) mod 2^(m-1); update q'=1-q, h'=h+q mod 2^(m-1)",assertions_checked:assertions,all_passed:true,native_physical_execution:false,independent_review:false,formal_task_admitted:false};
})();
process.stdout.write(JSON.stringify(result,null,2)+'\n');
