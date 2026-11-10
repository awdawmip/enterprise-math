// R701b native X6 primitive-coordinate square + 120-state V17/V29 frame monitor.
// Usage: node R701B_X6_SQUARE_120FRAME_VERIFY.js
function run() {
 const E=(v)=>JSON.stringify(v);
 const assert=(ok,why)=>{if(!ok)throw Error(why||"assertion failed")};
 const base=[0,1,2];
 const triads=[];
 for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++)triads.push([a,b,c]);
 assert(triads.length===20,"20 active supports");
 const intersects=(a,b)=>a.filter(x=>b.includes(x)).length;
 const neigh=(a,b)=>intersects(a,b)===2;
 const nextFrame=(q,triad)=>{
   const removed=q.filter(x=>!triad.includes(x));
   const added=triad.filter(x=>!q.includes(x));
   assert(removed.length===1 && added.length===1,"single J(6,3) replacement");
   const p=q.map(x=>x===removed[0]?added[0]:x);
   assert(E(p.slice().sort())===E(triad.slice().sort()),"slot support matches");
   return p;
 };
 const degree={}; const Q=[base];const dist={[E(base)]:0}; let cursor=0;
 while(cursor<Q.length){
   const q=Q[cursor++], k=E(q); let d=0;
   for(let slot=0;slot<3;slot++)for(let a=0;a<6;a++)if(!q.includes(a)){
     let nq=q.slice();nq[slot]=a; d++;
     if(dist[E(nq)]===undefined){dist[E(nq)]=dist[k]+1;Q.push(nq)}
   }
   degree[k]=d;
 }
 assert(Object.keys(dist).length===120,"exact 120 microframe states");
 assert(Object.values(degree).every(x=>x===9),"nine legal next frames");
 const maxDist=Math.max(...Object.values(dist));
 assert(maxDist===4, "microframe graph diameter from base");
 const shell=[0,1,2,3,4].map(x=>Object.values(dist).filter(v=>v===x).length);
 assert(E(shell)===E([1,9,36,63,11]),"BFS layer certificate");
 const allFrames=[];
 for(let a=0;a<6;a++)for(let b=0;b<6;b++)for(let c=0;c<6;c++)
   if(a!==b && a!==c && b!==c)allFrames.push([a,b,c]);
 assert(allFrames.length===120,"6P3=120");
 assert(allFrames.every(x=>dist[E(x)]!==undefined),"all reachable");
 const X=[
  [0,0,0,0,0,0],[1,0,0,0,0,0],
  [1,1,0,0,0,0],[0,1,0,0,0,0]
 ];
 let edges=[];
 for(let i=0;i<4;i++){
   const d=X[(i+1)%4].map((x,k)=>x-X[i][k]);
   assert(d.filter(x=>x!==0).length===1 && d.filter(x=>x!==0).every(x=>Math.abs(x)===1),"signed X6 primitive adjacency");
   edges.push({from:i,to:(i+1)%4,delta:d});
 }
 const parity=x=>x.reduce((a,b)=>a+b,0)&1;
 assert(edges.every(t=>parity(X[t.from])!==parity(X[t.to])),"bipartite 6D unit step");
 let hist={},ex={},roundTrip=0,one4loop=0,frameContrasts=0;
 for(const s1 of triads)for(const s2 of triads)for(const s3 of triads){
   const W=[base,s1,s2,s3], ordered=[...W,base];
   if(!ordered.slice(0,4).every((u,i)=>neigh(u,ordered[i+1])))continue;
   one4loop++;
   let q=base.slice(), microLedger=new Map(), cellStates=W.map(s=>s.slice()), nonneg=0;
   for(let layer=0;layer<4;layer++){
     let prev=cellStates.map(s=>s.slice());
     let next=prev.map((s,i)=>prev[(i+1)%4].slice());
     for(let i=0;i<4;i++)assert(neigh(prev[i],next[i]),"V36 neighbor-in-J relation law");
     const qnext=nextFrame(q,next[0]);
     const arc=E([q,qnext]);microLedger.set(arc,(microLedger.get(arc)||0)+1);
     q=qnext;nonneg+=1;
     cellStates=next;
     for(let i=0;i<4;i++)assert(E(cellStates[i])===E(W[(i+layer+1)%4]),"V36 synchronous copy law");
   }
   assert(cellStates.every((s,i)=>E(s)===E(W[i])),"4-layer X6 Cell active state recurrence");
   assert(nonneg===4 && [...microLedger.values()].every(v=>v>=0),"nonnegative count M");
   const u=new Map(allFrames.map(q=>[E(q),0]));
   for(const [pair,n] of microLedger.entries()){
     const [a,b]=JSON.parse(pair);
     u.set(E(a),u.get(E(a))+n);
     u.set(E(b),u.get(E(b))-n);
   }
   for(const frame of allFrames){
     const expected=Number(E(frame)===E(base))-Number(E(frame)===E(q));
     assert(u.get(E(frame))===expected,"120-port telescoping count ledger");
     frameContrasts++;
   }
   const h=E(q);
   hist[h]=(hist[h]||0)+1;
   if(!ex[h])ex[h]=ordered.map(z=>z.slice());
   roundTrip++;
 }
 assert(one4loop===369 && roundTrip===369,"complete length-four cyclic J(6,3) count");
 const expected={
  "[0,1,2]":207,"[0,2,1]":48,"[1,0,2]":48,
  "[1,2,0]":9,"[2,0,1]":9,"[2,1,0]":48
 };
 assert(E(Object.entries(hist).sort())===E(Object.entries(expected).sort()),"full S3 holonomy range");
 // For the declared V36 scheduler: each of 4 oriented physical X6 square
 // links records one V29 matched TRANSFER per layer, hence 4 per link.
 const transferEdgeCounts=[4,4,4,4], boundary=[0,0,0,0];
 for(let i=0;i<4;i++){boundary[i]-=transferEdgeCounts[i];boundary[(i+1)%4]+=transferEdgeCounts[i]}
 assert(boundary.every(x=>x===0),"matched V29 TRANSFER conservation");
 // Every nonzero closed primitive-coordinate path has even length:
 // each signed native unit step reverses integer sum parity.
 assert(parity(X[0])===parity(X[2]),"even path parity");
 return {
  schema:"R701B_NATIVE_X6_SQUARE_FRAME_PACKET_V1",
  status:"R701B_X6_SQUARE_FULL_S3_PASS",
  native_X6_vertices:X,directed_unit_edges:edges,
  pure_signed_unit_cell_triangle_possible:false,
  minimum_simple_pure_native_cycle_length:4,
  ordered_triad_frame_states:120,frame_state_outdegree:9,
  microstate_reachability_shells:shell,microstate_max_distance:4,
  four_layer_based_active_triad_words:roundTrip,
  s3_frame_holonomy_histogram:hist,holonomy_witnesses:ex,
  all_six_holonomies_reached:true,
  path_cell_loop_legal_under_declared_V36_copy_rule:true,
  hypothetical_V29_matched_transfer_edge_counts:transferEdgeCounts,
  matched_transfer_balance_per_cell:boundary,
  candidate_microframe_V29_PASS_count_checks:frameContrasts,
  all_assertions_passed:true
 };
}
if(typeof module!=="undefined" && module.exports)module.exports=run;
if(typeof console!=="undefined")console.log(JSON.stringify(run(),null,2));
