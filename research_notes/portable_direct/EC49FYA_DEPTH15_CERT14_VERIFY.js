'use strict';
// EC49FYA; frozen P10 and BRC16943, own 15-query improvement of EC49FXZ.
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
 if(depth===0)best={t:0,j:0,worst:600};
 check(best!==null,'inseparable words');internal++;
 const no=[],yes=[];for(const id of ids)(q(states[id],best.t,best.j)?yes:no).push(id);
 if(!root)root={t:best.t,j:best.j,no:no.length,yes:yes.length};
 return {t:best.t,j:best.j,no:build(no,depth+1),yes:build(yes,depth+1)};
}
const tree=build(states.map((_,i)=>i),0);
for(let k=0;k<states.length;k++){
 let p=tree,d=0;while(p.leaf===undefined){p=q(states[k],p.t,p.j)?p.yes:p.no;d++;check(d<=15,'depth bound')}
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
check(internal===599&&leafCount===600&&maxDepth===15&&root.t===0&&root.j===0&&root.no===193&&root.yes===407,'certificate mismatch');

/* Exact finite certificate witnesses: 50 full-factor states and
   50 deletion-at-column-zero states. All other deletion columns
   follow by the C11 cyclic column translation; checked below. */
const fullHex="0306080a1217181a1f2c316167 0f111217181e2c2f31354c67 02030406080a12262c353d43 02030508172c373b3d3e414b6167 0203081214262c3b3d4143 020305080a172c33353d5153 0203040506081216171f5761 0203050812214b4e51535761 020305080a122c353d4e5153 02030508122c3b3d414b4e 02030508172c33353d4146 0206080a12222c315b5c5f6166 02030506080a12172c535c61 01020305060812172141445c61 0205081216173d415b5c5f6164 02080a1216173d475b5c5e61 12292c3143444c5b5c5e61 08121617183d41475b5c61 0208122c313d41435b5c61 020305070812161753575c6167 030d122126292c4e53575b5c61 0d122c313d4e5355575b5c61 02171826292c575b5c5e5f61 0203050812172c3d415c61 02030508213d4e53575c5f61 17181e213d4753575b5c5f61 121617181e4753575b5c61 0203050812214143535c61 0203050812172c353d4167 03080a17182c3133354867 0d111222292c313566676d 020812173d3e414b6163666768 0308121617183d414b6768 12141617181e4b5357666768 020308090a2631373e4e536768 0203080a17222c3133353d67 030818222c3133353d4167 1214171821535557666768 0203082c33353d4e53576768 02082c3335414353666768 0317181e2c313d535b5e5f61676d 02030506080a172c535f6167 17181e262c333d41616667 020306080a2c3d43474b535f6367 02080a2c3133435b5e6167 02081241435b5e61636768 0208172c313d415b5f6167 02030607080a3d4e61636768 17182c2f31334b53555767 02081617263d415b5f6167".split(' ');
const holeHex="2a2c334b67 051b2c5266 060e1c2c3d53 1142484f67 2a2c3d4b5e 10262c5d67 152128455f 0005313b5b 121d282c3e 090c222c3d56 1733373b4b 01172c3843 17232c394e 05121b3747 0c213b5967 0c16223d5e 062c535e66 1626314651 18232c3152 242f4b585b 01212a2e44 172c2f535e 03122c3167 2c353d4a67 12184d5767 090c424a66 032f373d 17373d5361 02122c4467 030d2c3967 03192c66 1253616367 1416355661 061618445f 081e294a4d 17262c4b67 02182a2c4b67 0244535e63 202c3b5767 11172c3d43 05262c475d 062c3d4866 0a262c41 111c275e63 202c316167 14585c69 2c434e5b65 1623314a5368 2c2f43575b 0516222d67".split(' ');
check(fullHex.length===U.length && holeHex.length===U.length,'certificate atlas');
const certHist={full:{},hole:{}};
let certTargets=0,maxCert=0;
for(let m=0;m<U.length;m++)for(let z=-1;z<11;z++){
 const raw=(z===-1?fullHex[m]:holeHex[m]);
 check(raw.length%2===0,'malformed certificate');
 const ks=[];
 for(let x=0;x<raw.length;x+=2){
  const k=parseInt(raw.slice(x,x+2),16);
  check(k>=0&&k<110,'invalid physical site');
  const t=Math.floor(k/11),j=k%11;
  ks.push([t,z>0?(j+z)%11:j]);
 }
 check(new Set(ks.map(a=>a[0]*11+a[1])).size===ks.length,'duplicate certificate site');
 check(ks.length<=14,'certificate exceeds 14');
 const s={u:U[m],z};
 for(const other of states)if(other.u!==s.u||other.z!==s.z)
  check(ks.some(([t,j])=>q(s,t,j)!==q(other,t,j)),'non-isolating certificate');
 const kind=z===-1?'full':'hole';
 certHist[kind][ks.length]=(certHist[kind][ks.length]||0)+1;
 maxCert=Math.max(maxCert,ks.length);certTargets++;
}
check(certTargets===600&&maxCert===14,'exact per-state 14-certificate coverage');

console.log(JSON.stringify({schema:'EC49FYA_ROOT_SPLIT15_AND_STATE_CERT14_V1',pin:'BRC16943',status:'ALL_PASS',
 genuine_state_image:'600 via EC49FXU; masks reconstructed here',states:600,masks:50,sites:110,lowerWitness:{base,superMasks,extras},
 theoretical_lower:14,constructive_upper:15,exact_certificate_max:14,certificate_targets_checked:certTargets,certificate_length_histogram:certHist,internal,leafCount,maxDepth,
 averageDepth:depthSum/600,root,leafDepths:histogram,columnPairs,treePathsChecked:600,
 claim:'14<=exact worst-case Boolean-only adaptive identification cost<=15; whether Q=14 or 15 is open',
 verification:'exact integer arithmetic, deterministic lexicographic tie break; frozen original P10 mask reconstructed'},null,2));