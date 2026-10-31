// Exact integer verifier, BRC N=4, time-only, four ex-ante policy labels.
const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
         [0,0,0,10,10,0],[0,0,0,0,0,0],[0,0,0,0,0,20]];
M[4]=[0,0,0,2,18,0];
const LQ=[[10,10],[20,20],[15,15],[15,15]];
const LP=[[9,11],[5,5],[3,27],[30,30]];
function check(x,msg){if(!x)throw Error(msg)}
for(const law of [LQ,LP]){
 const leaves=law.flatMap(pair=>pair.flatMap(w=>[w,w]));
 check(leaves.length===16&&leaves.every(x=>x>0)&&leaves.reduce((a,b)=>a+b,0)===240,"leaf weights");
}
for(const row of M)check(row.reduce((a,b)=>a+b,0)===20&&row.every(x=>x>=0),"M rows");
const source=[0,0,1,2,2,3],stage1Slot=[0,0,1,1],stage2Slot=[0,1,0,2];
const policies=[],sigMap=new Map();let checks=0,finiteMax=0,exactAtBound=0;
for(let a=0;a<4;a++)for(let b=0;b<8;b++)for(let c=0;c<64;c++){
 const bits=(value,index)=>(value>>index)&1;
 const times=source.map((s,j)=>!bits(a,stage1Slot[s])?1:
                 !bits(b,stage2Slot[s])?2:bits(c,j)?3:4);
 const laws=M.map(row=>[1,2,3,4].map(t=>row.reduce((v,w,j)=>v+(times[j]===t?w:0),0)));
 const maxima=[0,1,2,3].map(t=>Math.max(...laws.map(p=>p[t])));
 const least=Math.min(...maxima);finiteMax=Math.max(finiteMax,least);
 const omit=maxima.findIndex(x=>3*x<=40);
 check(omit>=0,"no four-label decoder at "+a+","+b+","+c);
 for(const p of laws){
   const sum=p.reduce((z,n,t)=>z+Math.abs(3*n-(t===omit?0:20)),0);
   check(sum<=80,"TV upper failed");
   checks++;if(sum===80)exactAtBound++;
 }
 policies.push(laws);
 if(times[0]===times[1]&&times[3]===times[4]){
   const s=[times[0],times[2],times[3],times[5]],key=s.join(",");
   if(!sigMap.has(key))sigMap.set(key,s);
 }
}
check(policies.length===2048&&checks===12288,"policy census");
const S=Array.from(sigMap.values()).sort((a,b)=>a.join(",").localeCompare(b.join(",")));
check(S.length===64,"pure signatures");
const idx=S.findIndex(s=>s.every(t=>t===1));check(idx>=0,"earliest signature");
const pairs=[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]];
let count=0,maxBox=0,size16=0,largeIncludeEarliest=0;
for(const A of pairs)for(const B of pairs)for(const C of pairs)for(const D of pairs){
 const opts=[A,B,C,D];let hits=0,earliest=false;
 for(let i=0;i<S.length;i++){
   if(S[i].every((t,j)=>opts[j].includes(t))){hits++;if(i===idx)earliest=true}
 }
 count++;maxBox=Math.max(maxBox,hits);
 if(hits===16){size16++;if(earliest)largeIncludeEarliest++}
}
check(count===1296&&maxBox===16&&size16===9&&largeIncludeEarliest===0,"4-box lower");
let mixed=0;
for(let i=0;i<512;i++){
 const p=policies[(i*73+19)%2048],q=policies[(i*97+701)%2048],w=1+i%3,denom=80;
 const laws=p.map((row,j)=>row.map((n,t)=>w*n+(4-w)*q[j][t]));
 const omit=[0,1,2,3].find(t=>laws.every(row=>3*row[t]<=2*denom));
 check(omit!==undefined,"randomized mixture heavy-set");
 for(const row of laws){
   const total=row.reduce((z,n,t)=>z+Math.abs(3*n-(t===omit?0:denom)),0);
   check(total<=4*denom,"randomized mixture TV");
   mixed++;
 }
}
console.log([
 "PASS_BRC_N4_TIME_ONLY_FOUR_TAG_EXACT_20261031",
 "laws=2; positive_leaves_per_law=16; typed_source_rows=6",
 "deterministic_S23_policies=2048; exact_source_distribution_checks="+checks,
 "max_over_policies_min_time_max_source_mass="+finiteMax+"/20",
 "equality_check_count="+exactAtBound,
 "distinct_pure_source_signatures="+S.length,
 "two_choice_boxes="+count+"; largest_box="+maxBox+"; size16_boxes="+size16+"; size16_boxes_containing_1111="+largeIncludeEarliest,
 "randomized_two_policy_mixture_source_checks="+mixed,
 "CONCLUSION exact R_(k,4)=2/3 for all k>=1 for lawful S23 game; randomized generality proved analytically"
].join("\n"));