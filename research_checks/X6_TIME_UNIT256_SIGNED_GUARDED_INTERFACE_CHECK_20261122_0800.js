// Reproduce Unit256 exact signed atomic-triad interface analysis on the frozen Unit245 certificate.
// Run: node X6_TIME_UNIT256_SIGNED_GUARDED_INTERFACE_CHECK_20261122_0800.js <path-to-Unit245-original-results.json>
const audit=function audit(c){
 const b=[[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]];
 const x=Array.from({length:12},(_,i)=>i%2===0?b[i/2].slice():b[(i-1)/2].map((v,j)=>v+b[((i+1)/2)%6][j]));x.push([0,0,0]);
 let assertion_count=0,event_count=0,eligible=[];
 const ok=(test,label)=>{assertion_count++;if(!test)throw Error(label)};
 ok(c.cases.length===36,"case_count");
 for(const q of c.cases){
  let loc=[0,2],w=[0,0],trace=[],neg=new Set;
  for(let z=0;z<q.route.length;z++){
   const ch=q.route[z],k=ch>="A"&&ch<="M"?0:1,dst=ch.charCodeAt(0)-(k?97:65),src=loc[k];
   ok(dst>=0&&dst<=12,"destination_range");ok(src!==loc[1-k],"source_separation");ok(dst!==loc[1-k],"target_empty");
   const dif=x[dst].map((v,a)=>v-x[src][a]),a=dif.findIndex(v=>v!==0),nz=dif.filter(v=>v!==0),sgn=dif[a],port=(src===12||dst===12);
   ok(nz.length===1&&Math.abs(sgn)===1,"primitive_signed_six_axis");
   ok(port?(src===q.ingress&&dst===12)||(src===12&&dst===q.egress):((dst-src+12)%12===1||(dst-src+12)%12===11),"declared_port_or_ring");
   if(!port)w[k]+=(dst-src+12)%12===1?1:-1;
   const e={t:z+1,triad:k?"B":"A",src:src===12?"P":"x"+src,dst:dst===12?"P":"x"+dst,step:(sgn>0?"+":"-")+"e"+a,kind:port?"PORT":"RING"};
   trace.push(e);if(sgn<0)neg.add(`${src}>${dst}:${a}`);
   loc[k]=dst;event_count++;
  }
  ok(loc[0]===0&&loc[1]===2,"terminal_cell_return");
  ok(w[0]===-12&&w[1]===12,"terminal_signed_winding");
  ok(q.cost===trace.length,"certificate_length");
  if(q.cost===28){
   const negs=trace.filter(v=>v.step.startsWith("-"));
   ok(negs.length===14&&negs.every(v=>v.kind==="RING"),"negative_event_28");
   ok(trace.filter(v=>v.kind==="PORT").length===4,"spoke_count_28");
   eligible.push({ingress:q.ingress,egress:q.egress,cost:q.cost,route:q.route,negative_event_count:negs.length,negative_axis_counts:[0,1,2].map(a=>negs.filter(v=>v.step==="-e"+a).length),negative_directed_links:[...neg].sort(),first_event:trace[0],spoke_events:trace.filter(e=>e.kind==="PORT"),trace});
  }
 }
 ok(event_count===1312,"event_count");
 ok(eligible.length===2&&eligible[0].ingress===6&&eligible[0].egress===0&&eligible[1].ingress===8&&eligible[1].egress===2,"exact_two_reported_minimizers");
 const a=new Set(eligible[0].negative_directed_links),d=new Set(eligible[1].negative_directed_links);
 const shared=[...a].filter(v=>d.has(v)).sort(),union=[...new Set([...a,...d])].sort();
 ok(a.size===10&&d.size===10&&shared.length===8&&union.length===12,"directed_negative_edge_family");
 ok(eligible.every(v=>v.first_event.src==="x0"&&v.first_event.dst==="x11"&&v.first_event.step==="-e2"),"common_earliest_rejection_probe");
 return {schema:"X6_TIME_UNIT256_SIGNED_GUARDED_INTERFACE_CERT_V1",model:"CONDITIONAL_SYMMETRIC_SIGNED_ATOMIC_TRIAD_TRANSFERS_WITH_SERIAL_EMPTY_TARGET_GUARD",input:{repository:"awdawmip/enterprise-math",commit:"f56840285cafeb9f5767ea91e903e1f53808186f",path:"research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json"},total_paths:36,total_events:event_count,integer_assertions:assertion_count,optimal_witness_count:eligible.length,shared_required_negative_links:shared,union_negative_links:union,unique_negative_link_counts:eligible.map(v=>v.negative_directed_links.length),minimizers:eligible,unexecuted:"SOURCE_ADMISSION_AND_ENVIRONMENT_RESPONSE_NOT_OBTAINED"};
};
const fs=require("fs");
const a=audit(JSON.parse(fs.readFileSync(process.argv[2],"utf8")));
process.stdout.write(JSON.stringify(a,null,2)+"\n");
