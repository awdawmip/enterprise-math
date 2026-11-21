'use strict';
// Exact integer exhaustive proof certificate for the conditional D=4 BRC observer.
// Run: node x6_r83_ports39_124_verify.js > x6_r83_ports39_124_results.json
const vectors = {
  s3:[3,-4,1], s7:[6,-4,1], s10:[9,-5,1], s11:[10,-5,1],
  s16:[15,-6,1], b21:[21,-7,1], s27:[24,-14,3], s39:[36,-16,3],
  s43:[39,-20,4], b47:[42,-24,5], s49:[45,-21,4], b71:[66,-28,5],
  two47:[84,-48,10]
};
function q(a){let p=0,n=0;for(const x of a){p+=Math.max(x,0);n+=Math.max(-x,0)}return Math.max(p,n)}
function gaps([x,y,z]){
  const v=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z],g=[];
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)g.push(Math.abs(v[i]-v[j])/2);
  return g;
}
function dom(a,b){return a.every((x,i)=>x<=b[i])}
function eq(a,b){return a.every((x,i)=>x===b[i])}
function assert(v,s){if(!v)throw Error(s)}
const blocks=[
  {range:[39,42],core:['s3','s7','s10','s11','s16','s27','s39'],exception:['b21'],mincore:['s7','s10','s11','s16','s27','s39'],nExpected:127967},
  {range:[43,48],core:['s7','s10','s11','s16','s27','s39','s43'],exception:['b21','b47'],mincore:['s7','s10','s11','s16','s27','s39','s43'],nExpected:190168},
  {range:[49,124],core:['s7','s10','s11','s16','s27','s39','s43','s49'],exception:['b47','b71','two47'],mincore:['s7','s10','s11','s16','s27','s39','s43','s49'],nExpected:3216374}
];
const witness={
  s7:[[1,1,1,33],6,17],s10:[[1,1,7,15],3,8],s11:[[1,1,1,1],1,2],
  s16:[[7,1,1,15],3,8],s27:[[1,1,15,1],3,8],s39:[[15,1,1,1],3,8],
  s43:[[7,15,1,1],3,8],s49:[[1,15,7,1],3,8]
};
const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
for(const b of blocks){
  b.gg=b.core.map(x=>gaps(vectors[x])); b.counts=b.core.map(()=>0);
  b.misses=[]; b.domain=0;
  b.tests=b.mincore.map(key=>{const [w,n,d]=witness[key];return{key,w,value:n+'/'+d,n,d,
    ds:pairs.map(([i,j])=>w[i]+w[j]),same:0,better:0,other_minimizers:[]};});
}
for(let x=-124;x<=124;x++)for(let y=-124;y<=124;y++)for(let z=-124;z<=124;z++){
  const first=x||y||z;if(first<=0)continue;
  const a=[x,y,z],p=q(a);if(p>124)continue;
  const gg=gaps(a);
  for(const b of blocks){if(p>b.range[1])continue;
    b.domain++;
    const which=b.gg.findIndex(t=>dom(t,gg));
    if(which>=0)b.counts[which]++;
    else b.misses.push(a);
    for(const t of b.tests){let high=false,equal=false;
      for(let i=0;i<6;i++){
        const d=gg[i]*t.d-t.n*t.ds[i];
        if(d>0){high=true;break}
        if(d===0)equal=true;
      }
      if(!high){if(equal){t.same++;if(!eq(a,vectors[t.key]))t.other_minimizers.push(a)}else t.better++}
    }
  }
}
const result={schema:'X6_R83_PORTS39_124_GLOBAL_MINIMUM_WEIGHTED_CORES_V1',
 source_pin:'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 model:'conditional four-channel positive-count BRC star histogram; common additive offset',
 core_ranges:blocks.map(b=>({range:b.range,unoriented_domain:b.domain,
   coordinate_domination_core:b.core,domination_counts:b.counts,
   undominated:b.misses,minimal_weight_core:b.mincore,
   strict_global_witnesses:b.tests.map(t=>({vector:t.key,w:t.w,eta:t.value,
     global_equal_unoriented_minimizers:t.same,strictly_better:t.better,
     other_minimizers:t.other_minimizers}))})),
 symbolic_lemmas:['min(F_s39,F_s11)<=F_s3','min(F_s11,F_s27)<=F_b21',
 'min(F_s27,F_s39)<=F_b47 and <=F_b71','F_two47=2*F_b47'],
 formal_review:'NOT_INDEPENDENTLY_REVIEWED'};
for(const b of blocks){
  assert(b.domain===b.nExpected,'domain '+b.range);
  assert(b.misses.length===b.exception.length && b.misses.every((a,i)=>eq(a,vectors[b.exception[i]])),'exception '+b.range);
  assert(b.tests.every(t=>t.same===1&&t.better===0&&t.other_minimizers.length===0),'global strict '+b.range);
  assert(b.counts.reduce((a,x)=>a+x,0)+b.misses.length===b.domain,'coverage '+b.range);
}
process.stdout.write(JSON.stringify(result,null,2)+'\n');
