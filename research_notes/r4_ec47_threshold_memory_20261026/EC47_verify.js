/* EC47 exact integer verifier for the positive-source exponential witness.
   Run: node EC47_verify.js
   All integers remain below Number.MAX_SAFE_INTEGER in checked k=1..8. */
function assert(c,msg){if(!c)throw new Error(msg);}
function family(k){
  const H=2**k, rows=[];
  for(let mask=0;mask<H;mask++){
    let count=0;for(let j=0;j<k;j++)if(mask&(1<<j))count++;
    const P=[3*k-2*count],Q=[4*k];
    for(let j=0;j<k;j++){P.push(mask&(1<<j)?4:2);Q.push(1);}
    assert(Math.min(...P,...Q)>0,"positive");
    assert(P.reduce((x,y)=>x+y,0)==5*k,"P row");
    assert(Q.reduce((x,y)=>x+y,0)==5*k,"Q row");
    rows.push({P,Q});
  }
  return rows;
}
let totalPairs=0;const results=[];
for(let k=1;k<=8;k++){
  const rows=family(k),H=rows.length,M=5*k*H;
  const sign1=rows.map(({P,Q})=>P.map((v,j)=>Math.sign(v-Q[j])));
  const first=JSON.stringify(sign1[0]);
  assert(sign1.every(s=>JSON.stringify(s)===first),"lambda1 graph empty");
  assert(sign1[0][0]<0&&sign1[0].slice(1).every(x=>x>0),"lambda1 signs");
  const sign3=rows.map(({P,Q})=>P.map((v,j)=>Math.sign(v-3*Q[j])));
  assert(sign3.every(s=>s.every(t=>t!==0)),"lambda3 no ties");
  assert(new Set(sign3.map(s=>s.join(","))).size===H,"lambda3 distinct");
  let pairs=0;
  for(let i=0;i<H;i++)for(let j=i+1;j<H;j++){
    pairs++;assert(sign3[i].some((x,v)=>x*sign3[j][v]<0),"complete G3");
  }
  totalPairs+=pairs;
  function full(L){return rows.reduce((s,{P,Q})=>s+P.reduce((a,v,j)=>a+Math.max(v-L*Q[j],0),0),0);}
  function K1(L){let s=0;for(let y=0;y<=k;y++){let a=0,b=0;for(const {P,Q} of rows){a+=P[y];b+=Q[y];}s+=Math.max(a-L*b,0);}return s;}
  assert(full(1)*5===M*2 && full(1)===K1(1),"Bayes2/5");
  assert(full(3)*10===M&&K1(3)===0,"lambda3 1/10 vs zero");
  results.push({k,histories:H,terminal_labels:k+1,total_positive_sources_each:M,
    lambda_1_chromatic:1,lambda_3_chromatic:H,exact_region_memory:H,
    complete_graph_pair_checks:pairs,unrestricted_support_lambda_3:"1/10",
    one_memory_support_lambda_3:"0",Bayes_error_sum_lambda_1:"3/5"});
}
const P=[[5,1],[3,1]],Q=[[2,3],[2,3]];
function fullTiny(L){let s=0;for(let h=0;h<2;h++)for(let y=0;y<2;y++)s+=Math.max(P[h][y]-L*Q[h][y],0);return s;}
function oneTiny(L){let s=0;for(let y=0;y<2;y++)s+=Math.max(P[0][y]+P[1][y]-L*(Q[0][y]+Q[1][y]),0);return s;}
assert(fullTiny(1)===4&&oneTiny(1)===4,"tiny Bayes");
assert(fullTiny(2)===1&&oneTiny(2)===0,"tiny second threshold");
assert(totalPairs===43435,"pair count");
const report={schema:"EM_R4_EC47_JS_EXACT_V1",all_checks:"PASS",
 arithmetic:"Exact safe-range JavaScript integer operations, no floating source comparison",
 checked_k:"1..8",pairwise_graph_checks:totalPairs,witness_family:results,
 tiny_witness:{P,Q,total:10,Bayes_error_sum:"3/5",full_lambda_2:"1/10",K1_lambda_2:"0",entire_region_memory:2},
 proof_status:"Universal theorem is algebraic; finite checks corroborate only the stated family",
 native_X6_validation:"NOT_EXECUTED"};
if(typeof console!=="undefined")console.log(JSON.stringify(report,null,2));
