'use strict';
// EC49FXZ; original frozen P10 and BRC16943.
const check=(x,s)=>{if(!x)throw Error(s)},mod=(x,m)=>(x%m+m)%m;
const gcd=(a,b)=>b?gcd(b,a%b):a;
const inv=(a,m)=>{for(let k=1;k<m;k++)if(a*k%m===1)return k;throw Error('inverse')};
const slopes={'0,0':[3],'0,1':[0,3,4,5],'1,0':[2,3,4,5],'1,1':[2,3]};
function P(h,n){h=mod(h,10);n=mod(n,10);if(h%5===0&&n%5===0)return false;
return slopes[`${h%2},${n%2}`].includes(h%5===0?5:mod(n*inv(h%5,5),5))}
const masks=new Set();let dirs=0;
for(let a=0;a<10;a++)for(let c=0;c<10;c++)if(gcd(gcd(a,c),10)===1){
 dirs++;let x=-1,y=-1;
 outer:for(let xx=0;xx<10;xx++)for(let yy=0;yy<10;yy++)if(mod(c*xx-a*yy+1,10)===0){x=xx;y=yy;break outer}
 check(x>=0,'representative');
 let u=0;for(let t=0;t<10;t++)if(P(x+a*t,y+c*t))u|=1<<t;
 masks.add(u)
}
check(dirs===72&&masks.size===50&&!masks.has(0),'frozen 50-mask census');
const U=[...masks].sort((a,b)=>a-b),states=[];
const base=833,superMasks=[857,867,965];
check(U.includes(base)&&superMasks.every(x=>U.includes(x)),'four frozen lower-bound masks');
const extras=superMasks.map(x=>x&~base);
check(superMasks.every(x=>(x&base)===base)&&extras.every(x=>x>0)&&
      (extras[0]&extras[1])===0&&(extras[0]&extras[2])===0&&(extras[1]&extras[2])===0,
      'three disjoint extra supports');
for(const u of U)for(let z=-1;z<11;z++)states.push({u,z});
const q=(s,t,j)=>Number((s.u>>t&1)===1&&s.z!==j);
let internal=0,leafCount=0,maxDepth=0,depthSum=0,root=null;
const histogram={};
function build(ids,depth){
 if(ids.length===1){leafCount++;maxDepth=Math.max(maxDepth,depth);depthSum+=depth;
 histogram[depth]=(histogram[depth]||0)+1;return {leaf:ids[0]}}
 let best=null;
 for(let t=0;t<10;t++)for(let j=0;j<11;j++){
  let n1=0;for(const id of ids)n1+=q(states[id],t,j);
  if(n1===0||n1===ids.length)continue;
  const worst=Math.max(n1,ids.length-n1);
  if(best===null||worst<best.worst)best={t,j,worst};
 }
 check(best!==null,'inseparable words');internal++;
 const no=[],yes=[];for(const id of ids)(q(states[id],best.t,best.j)?yes:no).push(id);
 if(!root)root={t:best.t,j:best.j,no:no.length,yes:yes.length};
 return {t:best.t,j:best.j,no:build(no,depth+1),yes:build(yes,depth+1)};
}
const tree=build(states.map((_,i)=>i),0);
for(let k=0;k<states.length;k++){
 let p=tree,d=0;while(p.leaf===undefined){p=q(states[k],p.t,p.j)?p.yes:p.no;d++;check(d<=16,'depth bound')}
 check(p.leaf===k,'wrong decision leaf');
}
let columnPairs=0;
for(const u of U)for(let j=0;j<11;j++){
 const full={u,z:-1},hole={u,z:j};let differences=0;
 for(let t=0;t<10;t++)for(let v=0;v<11;v++)if(q(full,t,v)!==q(hole,t,v)){
  check(v===j,'difference outside hole column');differences++;
 }
 check(differences>0,'empty column');columnPairs++;
}
check(internal===599&&leafCount===600&&maxDepth===16&&root.t===8&&root.j===0&&root.no===303&&root.yes===297,'certificate mismatch');
console.log(JSON.stringify({schema:'EC49FXZ_BOOLEAN_ONLY_MINIMAX_V1',pin:'BRC16943',status:'ALL_PASS',
 genuine_state_image:'600 via EC49FXU; masks reconstructed here',states:600,masks:50,sites:110,lowerWitness:{base,superMasks,extras},
 theoretical_lower:14,constructive_upper:16,internal,leafCount,maxDepth,
 averageDepth:depthSum/600,root,leafDepths:histogram,columnPairs,treePathsChecked:600,
 claim:'14<=exact worst-case Boolean-only adaptive identification cost<=16; optimum pending',
 verification:'exact integer arithmetic, deterministic lexicographic tie break; frozen original P10 mask reconstructed'},null,2));