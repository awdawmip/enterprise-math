'use strict';
// Unit245: ordered one-way ingress/egress native centre spokes, 12 ring + centre.
// Single trusted finite state model, signed six-axis coordinates, exact integer arithmetic.
const fs = require('fs');
const P = 12, N = 12, BOUND = 48;
const basis = [
  [1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,1,0,0,0],
  [-1,0,0,0,0,0], [0,-1,0,0,0,0], [0,0,-1,0,0,0]
];
const x = [];
for (let r = 0; r < 6; r++) {
  x[2*r] = basis[r];
  x[2*r+1] = basis[r].map((v,j) => v+basis[(r+1)%6][j]);
}
x[P] = [0,0,0,0,0,0];
let assertions=0, edgesChecked=0, witnessesChecked=0;
function assert(cond,msg) { assertions++; if(!cond) throw new Error(msg); }
function axis(from,to) {
  const d=x[to].map((v,j)=>v-x[from][j]);
  const nonzero=d.map((v,j)=>v!==0?[j,v]:null).filter(Boolean);
  assert(nonzero.length===1 && Math.abs(nonzero[0][1])===1,`nonprimitive ${from}->${to}`);
  return {axis:nonzero[0][0]+1, sign:nonzero[0][1]};
}
for (let i=0;i<N;i++) { axis(i,(i+1)%N); axis(i,(i+N-1)%N); }
for (let p=0;p<N;p+=2) { axis(p,P); axis(P,p); }
function moves(here,entry,exit) {
  if (here===P) return [[exit,0]];
  const m = [[(here+1)%N,1],[(here+N-1)%N,-1]];
  if (here===entry) m.push([P,0]);
  return m;
}
function id(s) { return s.join(','); }
function solve(entry,exit) {
  const start=[0,2,0,0], goal=id([0,2,-12,12]);
  const q=[start], startId=id(start);
  const parent=new Map([[startId,null]]), depths=new Map([[startId,0]]);
  let found=null;
  for (let head=0;head<q.length;head++) {
    const s=q[head], k=id(s), depth=depths.get(k);
    if(k===goal){found=k;break;}
    if (depth===BOUND) continue;
    for(let who=0;who<2;who++) {
      const here=s[who], other=s[1-who];
      for(const [to,d] of moves(here,entry,exit)) {
        if(to===other) {assert(true,'blocked occupied target');continue;}
        let t=s.slice();t[who]=to; t[2+who]+=d;
        if(Math.abs(t[2])>BOUND || Math.abs(t[3])>BOUND)continue;
        const z=id(t); if(parent.has(z))continue;
        const signed=axis(here,to);edgesChecked++;
        parent.set(z,{prev:k,who,from:here,to,delta:d, ...signed});
        depths.set(z,depth+1);q.push(t);
      }
    }
  }
  assert(found!==null,`unreachable entry ${entry}, exit ${exit}`);
  const chain=[];
  for(let k=found; k!==startId;) {
    const item=parent.get(k);assert(item!==null,'broken predecessor');
    chain.push(item);k=item.prev;
  }
  chain.reverse();
  let state=start.slice(), spokes=0, plus=0, minus=0;
  const history=[];
  for (const step of chain) {
    assert(state[step.who]===step.from,'incorrect source');
    assert(state[1-step.who]!==step.to,'double occupied');
    const allowed=moves(step.from,entry,exit).some(([target,d])=>target===step.to&&d===step.delta);
    assert(allowed,'unavailable signed Port');
    const signed=axis(step.from,step.to);
    assert(signed.axis===step.axis&&signed.sign===step.sign,'signed six-axis mismatch');
    state[step.who]=step.to; state[2+step.who]+=step.delta;
    assert(Math.abs(state[2])<=BOUND&&Math.abs(state[3])<=BOUND,'winding register error');
    if(step.delta===0)spokes++;else if(step.delta>0)plus++;else minus++;
    history.push([step.who===0?'A':'B',step.from,step.to,step.axis,step.sign,step.delta]);
  }
  assert(id(state)===goal,'final labeled Cells/wind incorrect');
  assert(chain.length===depths.get(goal),'BFS depth mismatch');
  assert(chain.length===spokes+plus+minus,'event count mismatch');
  assert(spokes%2===0,'spoke balance mismatch');
  assert(spokes>0,'ring-only opposite winding impossible');
  for(const [key,d] of depths) if(d<chain.length)assert(key!==goal,'shorter goal impossible');
  witnessesChecked++;
  return {cost:chain.length,ring_events:plus+minus,spoke_events:spokes,states_seen:parent.size,states_at_shallower_depths:[...depths.values()].filter(v=>v<chain.length).length, history};
}
const ringPositions=[0,2,4,6,8,10], cases=[];
for(const entry of ringPositions)for(const exit of ringPositions) {
  const result=solve(entry,exit);
  cases.push({entry,exit,...result});
}
const costs=ringPositions.map(e=>ringPositions.map(z=>cases.find(a=>a.entry===e&&a.exit===z).cost));
const low=Math.min(...cases.map(a=>a.cost)), high=Math.max(...cases.map(a=>a.cost));
assert(low===28&&high===48,'incorrect spectrum extremes');
assert(costs.every((row,i)=>row[i]===[30,30,32,36,36,32][i]),'Unit244 diagonal regression failed');
assert(cases.filter(c=>c.cost===28).length===2,'wrong 28-event directed cases');
assert(cases.find(c=>c.entry===6&&c.exit===0).cost===28,'exact optimal one-way portal case');
assert(cases.find(c=>c.entry===8&&c.exit===2).cost===28,'second exact optimal one-way portal case');
const output={schema:'X6_TIME_UNIT245_DIRECTIONAL_INGRESS_EGRESS_EXACT_V1',
  source:'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json',
  status:'EXACT_FINITE_EXECUTED_CONDITIONAL',
  model:{ring_cells:12,centre_cell:P,ring_signed_edges:24,one_way_ingress:'x_entry -> P',one_way_egress:'P -> x_exit',entries:ringPositions,exits:ringPositions,triads:['A','B'],start:[0,2],goal:[0,2,-12,12],guard:'whole labelled triads, serial move, target unoccupied',counter_bound:BOUND},
  cost_matrix_rows_ingress_columns_egress:costs,minimum:low,maximum:high,
  minimizers:cases.filter(c=>c.cost===low).map(({entry,exit,spoke_events,ring_events})=>({entry,exit,spoke_events,ring_events})),
  total_cases:cases.length, total_bfs_states_observed:cases.reduce((s,c)=>s+c.states_seen,0),total_witness_events:cases.reduce((s,c)=>s+c.history.length,0),
  exact_assertions:assertions,directed_edges_checked:edgesChecked,complete_witnesses_checked:witnessesChecked,errors:0,cases};
const file=process.argv[2]||'X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json';
fs.writeFileSync(file,JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify({cases:cases.length,costs,minimum:low,maximum:high,assertions,states:output.total_bfs_states_observed,witness_events:output.total_witness_events,file}));
