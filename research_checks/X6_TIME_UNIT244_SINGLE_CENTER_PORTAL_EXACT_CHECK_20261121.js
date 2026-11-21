// Unit244: exact minimum native event count for one available bidirectional centre spoke.
// All 12 original OUTER ring edges remain; one already source-defined P spoke selected.
// Conditional intact-triad serial occupied-source / empty-target signed Port dynamics.
// State = [Cell_A, Cell_B, ring_increment_A, ring_increment_B].
// Winding-bound |L_i| <= 36 is exhaustive for any competitor shorter than 36 native steps.
'use strict';
const assert=require('node:assert/strict');
const AX=Array.from({length:6},(_,j)=>Array.from({length:6},(_,i)=>(j===i?1:0)));
const a=[AX[0],AX[1],AX[2],AX[0].map(x=>-x),AX[1].map(x=>-x),AX[2].map(x=>-x)];
const cell=[];
for(let r=0;r<6;r++) {cell[2*r]=a[r];cell[2*r+1]=a[r].map((v,i)=>v+a[(r+1)%6][i]);}
cell[12]=[0,0,0,0,0,0];
assert.equal(new Set(cell.map(x=>x.join(','))).size,13);
function stepAxis(u,v) {
  const d=cell[v].map((w,i)=>w-cell[u][i]);
  const nz=d.filter(v=>v!==0);assert.equal(nz.length,1);assert.equal(Math.abs(nz[0]),1);
  const idx=d.findIndex(z=>z!==0);return {axis:idx,sign:nz[0]};
}
const ring=Array.from({length:13},()=>[]);
for(let u=0;u<12;u++)for(let signed of [1,-1]){
  const v=(u+signed+12)%12;ring[u].push({to:v,delta:signed,...stepAxis(u,v),kind:'ring'});
}
const START=[0,2,0,0],GOAL='0,2,-12,12';
function exactSearch(port){
  const edges=ring.map(xs=>xs.slice());
  edges[port].push({to:12,delta:0,...stepAxis(port,12),kind:'spoke'});
  edges[12].push({to:port,delta:0,...stepAxis(12,port),kind:'spoke'});
  const key=s=>s.join(',');const dist=new Map([[key(START),0]]),previous=new Map(),queue=[START];
  let head=0, solution=null;let occupancyChecks=0,primitiveChecks=0;
  while(head<queue.length){
    const s=queue[head++], current=key(s),d=dist.get(current);
    if(current===GOAL){solution={dist:d,end:s};break;}
    for(let who=0;who<2;who++)for(const e of edges[s[who]]){
      occupancyChecks++;
      if(e.to===s[1-who])continue;
      const t=s.slice();t[who]=e.to;t[2+who]+=e.delta;
      if(Math.abs(t[2+who])>36)continue;
      primitiveChecks++;
      const next=key(t);if(dist.has(next))continue;
      dist.set(next,d+1);previous.set(next,{prior:current,who,u:s[who],v:e.to,ring_delta:e.delta,kind:e.kind,signed_axis:e.sign*(e.axis+1)});queue.push(t);
    }
  }
  assert.ok(solution,`no witness for portal ${port}`);
  const path=[];let at=GOAL;
  while(at!==key(START)){
    const edge=previous.get(at);assert.ok(edge);
    path.push({triad:'AB'[edge.who],from:edge.u,to:edge.v,kind:edge.kind,signed_axis:edge.signed_axis,ring_increment:edge.ring_delta});at=edge.prior;
  }
  path.reverse();assert.equal(path.length,solution.dist);
  const pos=[0,2],w=[0,0];let ringSteps=0,spokeSteps=0;
  for(const e of path){const who=e.triad==='A'?0:1;assert.equal(pos[who],e.from);assert.notEqual(pos[1-who],e.to);assert.equal(stepAxis(e.from,e.to).axis+1,Math.abs(e.signed_axis));
    pos[who]=e.to;w[who]+=e.ring_increment;if(e.kind==='ring')ringSteps++;else spokeSteps++;
  }
  assert.deepEqual(pos,[0,2]);assert.deepEqual(w,[-12,12]);
  return {portal_shell_position:port,portal_signed_axis_from_shell_to_P:stepAxis(port,12).sign*(stepAxis(port,12).axis+1),shortest_native_events:solution.dist,ring_events:ringSteps,spoke_events:spokeSteps,bfs_states_seen_until_first_goal:dist.size,bfs_expanded_until_first_goal:head,occupancy_checks:occupancyChecks,primitive_checks:primitiveChecks,witness:path};
}
const all=[0,2,4,6,8,10].map(exactSearch);
assert.deepEqual(all.map(s=>s.shortest_native_events),[30,30,32,36,36,32]);
assert.deepEqual(all.map(s=>s.spoke_events),[2,2,2,2,2,2]);
const result={schema:'X6_TIME_UNIT244_SINGLE_CENTER_PORTAL_SHARP_COST_CERT_V1',evidence_status:'CONDITIONAL_EXACT_FINITE',frozen_p000_commit:'a72226e2430ffa4786321ac86e7f0c599d5f0389',start_cells:{A:0,B:2},target_signed_ring_counts:{A:-12,B:12},source_defined_cells:13,original_ring_directed_edges:24,enabled_spoke_directed_edges_per_case:2,bfs_winding_bound:36,search_completeness:'Any shorter history than the achieved <=36 steps has |L_i|<=36, hence no shorter candidate is clipped.',single_portal_cases:all,assertion_failures:0};
console.log(JSON.stringify(result,null,2));
