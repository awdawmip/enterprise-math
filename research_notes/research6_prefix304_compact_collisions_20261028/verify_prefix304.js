"use strict";
/* PREFIX304: standalone exact ordered-source-pair BRC certificate.
 * Matrix input: PREFIX299 RESULTS_PREFIX299.json Git blob b6acffe158f014469235f5428d2889ff43b62810.
 * Scope: A5^3, q=1, fixed E/C and ten nonadaptive references. */
const CASES={"S4-1":[[[-5,2],[0,0],[2,0]],[[-4,1],[4,0],[-2,1]],[[-1,0],[0,-4],[-1,-6]]],"S4-5":[[[-5,-2],[0,0],[2,0]],[[-3,1],[0,0],[-5,3]],[[-2,-2],[4,4],[2,2]]],"S4-6":[[[-5,2],[0,0],[2,0]],[[-3,-1],[0,0],[-5,-3]],[[-2,-2],[4,4],[2,2]]],"S7-1":[[[-6,1],[4,0],[0,1]],[[-2,0],[0,0],[5,-2]],[[-2,1],[-4,0],[-4,1]]],"S7-2":[[[-6,-1],[4,0],[0,-1]],[[-2,-1],[-4,0],[-4,-1]],[[-2,0],[0,0],[5,2]]],"S7-3":[[[-5,3],[0,0],[-3,1]],[[-2,-2],[4,4],[2,2]],[[-2,0],[0,0],[5,2]]],"S7-5":[[[-4,-3],[0,4],[-2,1]],[[-4,1],[0,-4],[-2,-3]],[[-2,0],[0,0],[5,2]]]};
const WITNESS=[["S7-5",[0,3,0],[0,4,0],90],["S7-5",[0,1,0],[0,2,0],165],["S4-5",[0,1,0],[0,3,0],271],["S7-1",[0,1,0],[0,2,0],277],["S4-1",[0,3,0],[0,4,0],394],["S4-1",[3,4,4],[4,3,3],432],["S4-5",[0,1,0],[0,4,0],527],["S7-1",[0,3,0],[0,4,0],554],["S4-1",[0,1,0],[0,2,0],581],["S7-1",[3,4,4],[4,3,3],736],["S7-2",[1,2,2],[2,1,1],848]];
const V=[[0,0],[1,0],[-1,0],[0,1],[0,-1]];
const mul=(x,y)=>[x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]];
const conj=x=>[x[0],-x[1]];
const add=(x,y)=>[x[0]+y[0],x[1]+y[1]];
const same=(x,y)=>x.length===y.length&&x.every((v,k)=>v===y[k]);
const stats={instances:0,direct_BRC_readouts:0,ordered_source_pairs:0,gram_entries:0};
function brcMass(paths){
 let re=0,im=0;
 for(let p of paths)for(let t of paths){
  let z=mul(p.value,conj(t.value));re+=z[0];im+=z[1];stats.ordered_source_pairs++;
 }
 if(im!==0||re<0)throw Error("BRC mass invalid");
 stats.direct_BRC_readouts++;return re;
}
function observe(name,indices){
 const a=indices.map(i=>V[i]),m=CASES[name];
 const paths=[
  [{source:"src0",value:mul([4,0],a[0])},{source:"src1",value:mul([4,0],a[1])}],
  [{source:"src1",value:mul([-4,0],a[1])},{source:"src2",value:mul([4,0],a[2])}],
  ...m.map(row=>row.map((v,k)=>({source:"src"+k,value:mul(v,a[k])})))
 ];
 const K0=paths.map(brcMass);
 const extra=paths.flatMap((path,k)=>[
   brcMass([...path,{source:"independent_ref1_port"+k,value:[8,0]}]),
   brcMass([...path,{source:"independent_refi_port"+k,value:[0,8]}])
 ]);
 stats.instances++;return {K0,extra};
}
function checkGram(){
 const G=[[48,-16,0],[-16,32,16],[0,16,48]];
 for(let [name,M] of Object.entries(CASES)){
  const s=name.startsWith("S4")?[1,0,2]:[2,0,1];
  for(let j=0;j<3;j++)for(let k=0;k<3;k++){
   let v=[0,0];
   for(let row=0;row<3;row++)v=add(v,mul(conj(M[row][j]),M[row][k]));
   if(!same(v,[G[j][k]-(j===k?s[j]:0),0]))throw Error("Gram check: "+name);
   stats.gram_entries++;
  }
 }
}
function popcount(s){let n=0;for(;s;s>>=1)n+=s&1;return n;}
function solveFixed(diffs){
 const ok=[];
 for(let s=0;s<1024;s++)if(diffs.every(d=>(s&d)!==0))ok.push(s);
 const min=Math.min(...ok.map(popcount));
 return {min_reference_cost:min,optimal_mask_count:ok.filter(x=>popcount(x)===min).length,
  example_mask:ok.find(x=>popcount(x)===min)};
}
function verify(){
 checkGram();
 let rows=[];
 for(let [name,a,b,d] of WITNESS){
  const x=observe(name,a),y=observe(name,b);
  if(!same(x.K0,y.K0))throw Error("K0 witness failed");
  let observed=x.extra.reduce((m,v,k)=>m|(v!==y.extra[k]?1<<k:0),0);
  if(observed!==d)throw Error("mask witness failed "+d);
  rows.push({instrument:name,a:a.map(i=>V[i]),b:b.map(i=>V[i]),K0_times64:x.K0,difference_mask:d});
 }
 let triples=0;
 for(let i=0;i<10;i++)for(let j=i+1;j<10;j++)for(let k=j+1;k<10;k++){
  let s=(1<<i)|(1<<j)|(1<<k);triples++;
  if(!WITNESS.some(w=>(s&w[3])===0))throw Error("non-blocked triple "+s);
 }
 let paired={},union=[];
 for(let name of ["S4-6","S7-3"]){
  const groups=new Map();
  for(let i=0;i<5;i++)for(let j=0;j<5;j++)for(let k=0;k<5;k++){
   let v=observe(name,[i,j,k]),key=v.K0.join(",");
   if(!groups.has(key))groups.set(key,[]);
   groups.get(key).push(v);
  }
  let diffs=new Set(),pairs=0;
  for(let group of groups.values())for(let i=0;i<group.length;i++)for(let j=i+1;j<group.length;j++){
   let d=group[i].extra.reduce((m,v,k)=>m|(v!==group[j].extra[k]?(1<<k):0),0);
   if(!d)throw Error("ten reference menu insufficient");
   diffs.add(d);pairs++;
  }
  paired[name]={states:125,K0_collision_pairs:pairs,distinct_difference_masks:diffs.size,...solveFixed([...diffs])};
  union.push(...diffs);
 }
 const alld=[...new Set(union)];
 paired.joint={distinct_difference_masks:alld.length,...solveFixed(alld)};
 if(paired["S4-6"].min_reference_cost!==3||paired["S7-3"].min_reference_cost!==3||paired.joint.min_reference_cost!==4||!alld.every(d=>(d&0x33)!==0))
  throw Error("two-instrument claim failed");
 return {schema:"EM_PREFIX304_EXACT_BRC_COLLISION_CERTIFICATE_V1",input_git_blob:"b6acffe158f014469235f5428d2889ff43b62810",
  scope:"A5^3, fixed q=1, nonadaptive ten-bit reference menu",
  bit_order:["E+1","E+i","C+1","C+i","R1+1","R1+i","R2+1","R2+i","R3+1","R3+i"],
  eleven_pair_certificate:{rows,blocked_three_bit_choices:triples},
  two_instrument_result:paired,checks:stats,
  admission:"AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"};
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)
 console.log(JSON.stringify(verify(),null,2));
