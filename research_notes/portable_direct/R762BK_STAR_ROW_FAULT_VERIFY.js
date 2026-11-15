'use strict';
// R762BK: exact finite cross-check of Port-1 star coordinate row distance and mixed faults.
// Requires Node.js built-ins only; all numeric comparisons use exact integers.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const EDGES = [];
for (let i=0;i<5;i++) for(let j=i+1;j<5;j++) EDGES.push([i,j]);
assert.equal(EDGES.length,10);
const degree = (rows,v) => rows.reduce((s,[a,b])=>s+Number(a===v||b===v),0);
const profile = {0:{minRows:Infinity,optimal:0,all:0},1:{minRows:Infinity,optimal:0,all:0},2:{minRows:Infinity,optimal:0,all:0},3:{minRows:Infinity,optimal:0,all:0},4:{minRows:Infinity,optimal:0,all:0}};
const eligible = {};
for(let t=0;t<=2;t++) for(let e=0;e<=3;e++) eligible['t'+t+'e'+e]={qualifyingFamilies:0,minRows:null,optimalFamilies:0};
let familyChecks=0, minDistanceChecks=0, binaryPairChecks=0, mixedBudgetChecks=0;
const binaryStates=Array.from({length:32},(_,v)=>Array.from({length:5},(_,i)=>(v>>i)&1));
for(let mask=0;mask<(1<<10);mask++) {
  const rows=EDGES.filter((_,i)=>((mask>>i)&1)!==0);
  const m=rows.length, d=Math.min(...Array.from({length:5},(_,v)=>degree(rows,v)));
  familyChecks++;
  let observedMin=Infinity;
  for(let a=0;a<binaryStates.length;a++) for(let b=a+1;b<binaryStates.length;b++) {
    const x=binaryStates[a],y=binaryStates[b];
    let disagreements=0;
    for(const [i,j] of rows) disagreements+=Number(x[i]!==y[i]||x[j]!==y[j]);
    if(disagreements<observedMin) observedMin=disagreements;
    binaryPairChecks++;
  }
  assert.equal(observedMin,d,'row distance must equal min vertex degree');
  minDistanceChecks++;
  const p=profile[d]; p.all++;
  if(m<p.minRows){p.minRows=m;p.optimal=1;} else if(m===p.minRows){p.optimal++;}
  for(let t=0;t<=2;t++) for(let e=0;e<=3;e++) {
    const q=eligible['t'+t+'e'+e], admissible=d>=2*t+e+1;
    mixedBudgetChecks++;
    if(admissible) {
      q.qualifyingFamilies++;
      if(q.minRows===null||m<q.minRows){q.minRows=m;q.optimalFamilies=1;}
      else if(m===q.minRows)q.optimalFamilies++;
    }
  }
}
assert.deepEqual(Object.fromEntries([1,2,3,4].map(d=>[d,[profile[d].minRows,profile[d].optimal]])),
  {1:[3,30],2:[5,12],3:[8,15],4:[10,1]});
assert.equal(eligible.t1e0.minRows,8); assert.equal(eligible.t1e0.optimalFamilies,15);
assert.equal(eligible.t1e1.minRows,10); assert.equal(eligible.t1e1.optimalFamilies,1);
assert.equal(eligible.t2e0.qualifyingFamilies,0);
const full=EDGES, unitWitness=full.filter(([i,j])=>i===0||j===0);
assert.equal(unitWitness.length,4);
const rowOf=(x,[i,j])=>[x[i],x[j]];
const x=[0,0,0,0,0], y=[1,0,0,0,0];
let split=0;
const received=full.map(row=>row.includes(0)?rowOf(split++<2?x:y,row):rowOf(x,row));
const dR=z=>full.reduce((n,row,k)=>n+Number(JSON.stringify(rowOf(z,row))!==JSON.stringify(received[k])),0);
assert.deepEqual([dR(x),dR(y)],[2,2]);
let oneFaultMajorityChecks=0;
for(let mask=0;mask<1024;mask++) {
  const rows=EDGES.filter((_,i)=>mask>>i&1);
  const d=Math.min(...Array.from({length:5},(_,v)=>degree(rows,v)));
  if(d<3)continue;
  for(const z of binaryStates) for(let bad=-1;bad<rows.length;bad++) {
    const samples=Array.from({length:5},()=>[]);
    rows.forEach(([i,j],r)=>{
      samples[i].push(z[i]^(r===bad?1:0));
      samples[j].push(z[j]^(r===bad?1:0));
    });
    const decoded=samples.map(vals=>Number(vals.filter(v=>v===1).length>vals.length/2));
    assert.deepEqual(decoded,z);
    oneFaultMajorityChecks++;
  }
}
const evidence={
  schema:'EM_R762BK_EXACT_INTEGER_EVIDENCE_V1',
  model:'signed native X6 relative Cell; coordinate Port-1 star rows; adversarial corrupted labelled rows and known erasures',
  theorem:'minimum row Hamming distance=min degree of G_H; unique recovery from t errors and e erasures iff 2t+e<d; vertex-wise strict majority decoder',
  family_checks:familyChecks,binary_state_pairs_per_family:496,binary_pair_checks:binaryPairChecks,
  min_distance_checks:minDistanceChecks,mixed_budget_checks:mixedBudgetChecks,
  profile,eligible,one_fault_majority_checks:oneFaultMajorityChecks,
  sharp_2_error_ambiguity:{full_rows:10,minimum_distance:4,distinct_states:['00000','10000'],received_distance_from_each:2},
  source_scope:'Enumerates all 1024 graph families, all 32 binary relative charts and their pairs, listed budgets; all Z^6 follows from proof.',
  formal_verification:'NOT_PERFORMED',independent_review:'NOT_REVIEWED'
};
const serialized=JSON.stringify(evidence,null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],serialized);
process.stdout.write(serialized);
