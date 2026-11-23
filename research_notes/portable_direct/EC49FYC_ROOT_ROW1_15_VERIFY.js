'use strict';
// EC49FYC — pinned BRC16943; normalized auxiliary P10/C11 observer.
const check=(x,m)=>{if(!x)throw Error(m)},mod=(x,m)=>(x%m+m)%m;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inv5=x=>{for(let k=1;k<5;k++)if(k*x%5===1)return k;throw Error('inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);
 if(h%5===0&&n%5===0)return false;
 return slopes[`${h%2},${n%2}`].includes(h%5===0?5:mod(n*inv5(h%5),5));
}
let directions=0;const M=new Set();
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
 directions++;let p=null;
 outer:for(let x=0;x<10;x++)for(let y=0;y<10;y++)if(mod(c*x-a*y+1,10)===0){p=[x,y];break outer;}
 check(p!==null,'missing primitive direction representative');
 let u=0;for(let t=0;t<10;t++)if(P(p[0]+a*t,p[1]+c*t))u|=1<<t;
 M.add(u);
}
const U=[...M].sort((a,b)=>a-b);
check(directions===72&&U.length===50&&!M.has(0),'frozen P10 mask census');
const states=[];for(const u of U)for(let z=-1;z<11;z++)states.push({u,z});
check(states.length===600,'state count');
const read=(s,t,j)=>Number(!!(s.u&(1<<t))&&s.z!==j);
// Exact hard witness. All 15 words share row-1 answer zero.
const base=788,s={u:base,z:-1},sup=[789,828,980],extra=sup.map(u=>u&~base);
check(M.has(base)&&sup.every(u=>M.has(u)),'witness outside frozen 50');
check(extra[0]===1&&extra[1]===40&&extra[2]===192,'extra-row witness');
check(extra.every((a,i)=>extra.every((b,j)=>i===j||!(a&b))),'extra rows overlap');
check([base,...sup].every(u=>!(u&2)),'row 1 must be absent');
const support=[2,4,8,9];
check(support.every(t=>(base>>t)&1)&&
 [0,1,3,5,6,7].every(t=>!((base>>t)&1)),'base support mismatch');
for(let j=0;j<11;j++){
 const hole={u:base,z:j};let diff=0;
 for(let t=0;t<10;t++)for(let k=0;k<11;k++)
  if(read(s,t,k)!==read(hole,t,k)){check(k===j&&support.includes(t),'wrong hole support');diff++;}
 check(diff===4,'hole must differ on 4 sites only');
 check(read(hole,1,j)===read(s,1,j),'forbidden row distinguishes a hole');
}
for(let i=0;i<3;i++)for(let t=0;t<10;t++)for(let j=0;j<11;j++){
 const other={u:sup[i],z:-1};
 if(read(s,t,j)!==read(other,t,j))check(!!(extra[i]&(1<<t)),'supermask difference');
 check(read(other,1,j)===0,'forbidden row distinguishes a supermask');
}
// Each of the 11 holes forces a positive read in its own column;
// each disjoint supermask extras forces a separate negative read.
// Thus a depth<=14 path for (788,-1) cannot contain any row-1 read.

const tests=[];for(let t=0;t<10;t++)for(let j=0;j<11;j++){
 let q=0n;
 for(let id=0;id<states.length;id++)if(read(states[id],t,j))q|=1n<<BigInt(id);
 tests.push(q);
}
const count=x=>{let n=0;for(;x;x&=x-1n)n++;return n};
function xorshift32(x){x^=x<<13;x>>>=0;x^=x>>>17;x^=x<<5;return x>>>0}
function priority(seed){
 let x=seed>>>0,a=Array.from({length:110},(_,i)=>i);
 for(let i=109;i>0;i--){x=xorshift32(x);let j=x%(i+1);[a[i],a[j]]=[a[j],a[i]]}
 return a;
}
const order=priority(1);
let internal=0,leaves=0,maxDepth=0,totalDepth=0;const hist={};
function build(S,d){
 const n=count(S);
 if(n===1){
  leaves++;maxDepth=Math.max(maxDepth,d);totalDepth+=d;hist[d]=(hist[d]||0)+1;
  let id=0;while(!(S&(1n<<BigInt(id))))id++;
  return {leaf:id};
 }
 let q=d===0?11:-1,best=Infinity;
 if(d!==0)for(const k of order){
  let yes=count(S&tests[k]),worst=Math.max(yes,n-yes);
  if(yes>0&&yes<n&&worst<best){q=k;best=worst}
 }
 check(q>=0,'no separator');
 const yes=S&tests[q],no=S^yes;
 check(no!==0n&&yes!==0n,'degenerate query');
 internal++;
 return {query:q,no:build(no,d+1),yes:build(yes,d+1)};
}
const root=build((1n<<600n)-1n,0);
let firstNo=0,firstYes=0;
for(let i=0;i<states.length;i++){
 let node=root,depth=0;
 if(read(states[i],1,0))firstYes++;else firstNo++;
 while(node.leaf===undefined){
  const q=node.query;
  node=read(states[i],Math.floor(q/11),q%11)?node.yes:node.no;
  depth++;check(depth<=15,'exceeded 15 reads');
 }
 check(node.leaf===i,'wrong leaf '+i);
}
check(root.query===11&&firstNo===314&&firstYes===286,'root partition');
check(internal===599&&leaves===600&&maxDepth===15&&totalDepth===6516,'tree certificate changed');
const result={
 schema:'EC49FYC_ROOT_ROW1_EXACT_15_V1',date:'2026-11-23',
 frozen_scientific_pin:'BRC16943',status:'ALL_PASS',
 domain:{primitive_directions:directions,support_masks:U.length,states:states.length,sites:110},
 lower_bound:{base_full_mask:788,support_rows:support,eleven_hole_columns:11,
   strict_full_supermasks:sup,disjoint_extra_rows:[[0],[3,5],[6,7]],
   forbidden_row:1,required_useful_reads:14,
   statement:'Any row-1 read on path for (788,-1) forces at least 15 total queries.'},
 upper_bound:{first_query:[1,0],seed:1,tie_priority:'xorshift32 Fisher-Yates',
   max_depth:maxDepth,total_leaf_depth:totalDepth,uniform_mean_exact:'6516/600',
   first_no:firstNo,first_yes:firstYes,internal_nodes:internal,
   leaves,validated_paths:600,leaf_depth_histogram:hist},
 theorem:'Q_root_row1 = 15 for any first site (1,j), 0<=j<11',
 unrestricted:'Q in {14,15}, still open',
 verification:'Full integer 72-to-50 P10 atlas and all 600 state paths; analytical 11+3+1 witness.'
};
console.log(JSON.stringify(result,null,2));
