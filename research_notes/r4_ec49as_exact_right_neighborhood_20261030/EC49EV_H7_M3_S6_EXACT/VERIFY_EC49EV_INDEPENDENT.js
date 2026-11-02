#!/usr/bin/env node
'use strict';
// Independent finite-language and witness checker; no Python/model imports.
const assert = require('assert').strict;
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const STATE=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const BUCKETS=['N','A','B','AB','BA'];
const prime=1000003;
function native(w){return [...w].flatMap(x=>OPS[x]);}
function key(s){const p=[0,0,0,0,0,0];for(const a of s)if(a>0)p[a-1]++;return p.join(',');}
function displacement(s){const x=[0,0,0,0,0,0];for(const a of s)x[Math.abs(a)-1]+=Math.sign(a);return x;}
function sig(s){return STATE.map(([start,pr])=>{let state=start,prev=pr;for(const d of s){if(prev===1&&d===2)state=({N:'A',B:'BA'})[state]||state;else if(prev===2&&d===1)state=({N:'B',A:'AB'})[state]||state;prev=d;}return BUCKETS.indexOf(state)}).join(',');}
function signatures(w){return sig(native(w));}
function rank(S){const piv={};let result=0;for(const str of S){const t=str.split(',').map(Number);for(let b=0;b<5;b++){const v=t.map(x=>Number(x===b));for(let i=0;i<9;i++){if(!v[i])continue;if(piv[i]){let mul=v[i];for(let j=i;j<9;j++)v[j]=((v[j]-mul*piv[i][j])%prime+prime)%prime;}else{let inv=1,exp=prime-2,q=v[i];while(exp>0){if(exp%2)inv=inv*q%prime;q=q*q%prime;exp=Math.floor(exp/2);}piv[i]=v.map(x=>x*inv%prime);result++;break;}}}}return result;}
const base=['ce','de','ec','ed'];const T4=new Set(base.map(signatures));const T2=new Set(['feg','gef'].map(signatures));
assert.equal(T4.size,4);assert.equal(T2.size,2);assert.equal(rank(T4),9);assert.equal(rank(T2),9);
const horizon={}, returnsByH={}, allFibersByH={};const universe=new Set();let total=0;
for(let h=2;h<=7;h++){
 const F=new Map();let returns=0;
 function visit(prefix,n,sum1,sum2){if(n===h){if(sum1!==2||sum2!==0)return;let w=prefix,s=native(w);let k=key(s),t=sig(s);if(!F.has(k))F.set(k,new Set());F.get(k).add(t);universe.add(t);returns++;return;}
 for(const [a,code] of Object.entries(OPS)){
 let delta=[0,0,0];for(const d of code)delta[Math.abs(d)-1]+=Math.sign(d);
 visit(prefix+a,n+1,sum1+delta[0],sum2+delta[1]);
 }}
 visit('',0,0,0);horizon[h]=F;returnsByH[h]=returns;allFibersByH[h]=F.size;total+=returns;
}
const extras=[...universe].filter(x=>!T4.has(x)).sort();assert.equal(extras.length,7);assert.equal(universe.size,11);
function subset(a,b){for(const x of a)if(!b.has(x))return false;return true;}
function scheduleCount(fibers){let count=0;function dfs(h,used){if(h===8){if(used.size===3)count++;return;}
 for(const p of fibers[h]){const next=new Set(used);next.add(p);if(next.size<=3)dfs(h+1,next);}}
 const p0=key(native('ce'));assert.equal(fibers[2].length,1);assert.equal(fibers[2][0],p0);dfs(3,new Set([p0]));return count;}
let byPair=[];
for(let i=0;i<extras.length;i++)for(let j=i+1;j<extras.length;j++){
 const allowed=new Set([...T4,extras[i],extras[j]]);const fibers={};
 for(let h=2;h<=7;h++){
  fibers[h]=[];
  for(const [k,S] of horizon[h]){
    const intersection=new Set([...S].filter(s=>allowed.has(s)));
    if(rank(intersection)<9)continue;
    const is4=subset(T4,intersection),is2=subset(T2,intersection);
    assert(is4||is2,'Unexpected rank-nine type for '+h+' '+k+' pair '+i+','+j);
    assert(!(is4&&is2));
    fibers[h].push(k);
  }
 }
 const count=scheduleCount(fibers);byPair.push({pair:[i,j],schedules:count});
 assert.equal(count,(T2.has(extras[i])&&T2.has(extras[j]))?465:3);
}
const allwords={2:['ce','de','ec','ed'],3:['feg','gfe'],4:['degf','fegc','fegd','gfec'],5:['fegfg','gfefg'],6:['degffg','fegcgf','fegfgd','gfefgc'],7:['fegfggf','gfefgfg']};
const countKeys=new Set(),allTypes=new Set(),prefixes=new Set(),cert={};
for(let h=2;h<=7;h++){
 const words=allwords[h],K=new Set(),S=new Set();
 for(const w of words){const n=native(w);assert.equal(w.length,h);assert.deepEqual(displacement(n),[2,0,0,0,0,0]);K.add(key(n));S.add(sig(n));for(let i=1;i<=n.length;i++)prefixes.add(n.slice(0,i).join(','));}
 assert.equal(K.size,1);assert.equal(rank(S),9);for(const k of K)countKeys.add(k);for(const s of S)allTypes.add(s);
 cert[h]={p:[...K][0].split(',').map(Number),types:S.size,rank:rank(S),words};
}
assert.equal(countKeys.size,3);assert.equal(allTypes.size,6);assert.equal(prefixes.size,86);
const report={status:'PASS',input_scope:'full 7-operation returning words h2..h7; exact prime rank; 21 global signature pairs',all_returning_by_h:returnsByH, all_fibers_by_h:allFibersByH,distinct_signatures:universe.size,extra_signature_pairs:byPair.length,full_3key_schedules_for_T2_pair:465,three_key_schedules_for_other_pairs:3,witness:{E:prefixes.size,M:countKeys.size,S:allTypes.size,horizons:cert}};
assert.deepEqual(returnsByH,{'2':8,'3':51,'4':304,'5':1770,'6':10224,'7':58947});
console.log(JSON.stringify(report,null,2));
