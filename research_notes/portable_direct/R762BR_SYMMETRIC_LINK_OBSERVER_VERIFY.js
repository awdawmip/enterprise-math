'use strict';
// R762BR: exact labelled-BRC incidence, S4 covariance, and query-code distances.
// No physical time/rotation, floating point, or analytic phase operations.
const assert = require('node:assert/strict');
const six=[1,2,3,4,5,6], hidden=[3,4,5,6];
function permutations(xs){
  if(xs.length===0)return [[]];
  return xs.flatMap((x,i)=>permutations([...xs.slice(0,i),...xs.slice(i+1)]).map(y=>[x,...y]));
}
function cycleLengths(p){
  const seen=new Set(),lens=[];
  for(const i of six){
    if(seen.has(i))continue;
    let j=i,len=0;
    do{assert(!seen.has(j));seen.add(j);len++;j=p[j-1]}while(j!==i);
    lens.push(len);
  }
  return lens.sort((a,b)=>a-b);
}
const allBRC=permutations(six).filter(p=>cycleLengths(p).join(',')==='3,3')
  .sort((a,b)=>a.join(',').localeCompare(b.join(',')));
const U=allBRC.filter(p=>p[0]===2);
assert.equal(allBRC.length,40);assert.equal(U.length,8);
const key=p=>p.join(','), stateKeys=new Set(U.map(key));
const A=hidden.map(c=>[2,c]);
const B=hidden.map(c=>[c,1]);
const C=hidden.flatMap(a=>hidden.filter(b=>a!==b).map(b=>[a,b]));
const families={A,B,C};
const query=(p,[a,b])=>Number(p[a-1]===b);
const panels={A:['A'],B:['B'],C:['C'],AB:['A','B'],AC:['A','C'],BC:['B','C'],ABC:['A','B','C']};
const dist=(x,y)=>x.reduce((v,z,i)=>v+Number(z!==y[i]),0);
const results={};
for(const [name,ids] of Object.entries(panels)){
  const panel=ids.flatMap(id=>families[id]);
  const words=U.map(p=>panel.map(q=>query(p,q)));
  const distances=[];
  for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)distances.push(dist(words[i],words[j]));
  const hist={};for(const d of distances)hist[d]=(hist[d]??0)+1;
  results[name]={named_queries:panel.length,distinct_words:new Set(words.map(w=>w.join(''))).size,
    min_distance:Math.min(...distances),distance_histogram:hist};
}
assert.deepEqual(results.A,{named_queries:4,distinct_words:4,min_distance:0,distance_histogram:{0:4,2:24}});
assert.deepEqual(results.B,results.A);
assert.deepEqual(results.C,{named_queries:12,distinct_words:8,min_distance:4,distance_histogram:{4:12,6:16}});
assert.deepEqual(results.AB,{named_queries:8,distinct_words:4,min_distance:0,distance_histogram:{0:4,4:24}});
assert.deepEqual(results.AC,{named_queries:16,distinct_words:8,min_distance:6,distance_histogram:{6:16,8:12}});
assert.deepEqual(results.BC,results.AC);
assert.deepEqual(results.ABC,{named_queries:20,distinct_words:8,min_distance:6,distance_histogram:{6:4,8:12,10:12}});
const s4=permutations(hidden).map(z=>Object.fromEntries([[1,1],[2,2],...hidden.map((x,i)=>[x,z[i]])]));
assert.equal(s4.length,24);
let covarianceChecks=0;
const linkName=q=>q.join('>');
for(const g of s4){
  for(const p of U){
    const transported=six.map(a=>g[p[six.find(x=>g[x]===a)-1]]);
    assert(stateKeys.has(key(transported)));
    for(const q of [...A,...B,...C]){
      const relabelled=[g[q[0]],g[q[1]]];
      assert.equal(query(transported,relabelled),query(p,q));
      covarianceChecks++;
    }
  }
  for(const qs of [A,B,C])
    assert.deepEqual(new Set(qs.map(q=>linkName([g[q[0]],g[q[1]]]))),new Set(qs.map(linkName)));
}
assert.equal(covarianceChecks,24*8*20);
// Sign-decorated branch carrier: 8 directed-Link sources x 16 independent sign states.
function signedMinDistance(linkPanel,signRepetitions){
  const panel=linkPanel.flatMap(id=>families[id]),words=[];
  for(const p of U)for(let mask=0;mask<16;mask++){
    const w=panel.map(q=>query(p,q));
    for(let i=0;i<4;i++)for(let j=0;j<signRepetitions;j++)w.push((mask>>i)&1);
    words.push(w);
  }
  let min=Infinity;
  for(let i=0;i<words.length;i++)for(let j=i+1;j<words.length;j++)
    min=Math.min(min,dist(words[i],words[j]));
  return min;
}
const signed={
  no_errors:{panel:'C',sign_repetitions:1,query_count:16,min_distance:signedMinDistance(['C'],1)},
  one_error:{panel:'C',sign_repetitions:3,query_count:24,min_distance:signedMinDistance(['C'],3)},
  two_errors:{panel:'AC',sign_repetitions:5,query_count:36,min_distance:signedMinDistance(['A','C'],5)}
};
assert.equal(signed.no_errors.min_distance,1);
assert.equal(signed.one_error.min_distance,3);
assert.equal(signed.two_errors.min_distance,5);
const report={
  schema:'R762BR_EXACT_FINITE_BRC_INCIDENCE_V1',
  model:'conditional two ordered 3-cycles with Q_(1,2)=1, named Link Q_(a,b), hidden independent sign bits S_3..S_6',
  frozen_science:'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
  population:{all_oriented_triads:allBRC.length,conditional_link_fiber:U.length,s4_permutations:s4.length,states:U},
  query_orbits:{A,B,C},panel_results:results,signed,covariance_checks:covarianceChecks,
  coverage:{all_labelled_cycle_permutations:720,all_conditional_states:8,all_stabilizer_permutations:24,
    all_s4_named_query_checks:covarianceChecks,signed_128_state_pairs_per_panel:8128,sign_repeated_panels:3},
  independent_review:'NOT_REVIEWED'
};
process.stdout.write(JSON.stringify(report,null,2)+'\n');
