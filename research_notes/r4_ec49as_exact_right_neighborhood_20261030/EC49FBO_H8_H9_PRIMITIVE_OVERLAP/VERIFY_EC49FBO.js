'use strict';
// EC49FBO: exact signed-X6 positive-BRC primitive-prefix overlap.
const A='acdefg',P={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const S=[0,0,4,1,16,32,8,2,0];
function counts(h,x,y,z,cd){let k=x+y-h-1;return[z-1,cd==='c'?k:0,cd==='d'?k:0,z,h+1-y-2*z,h+1-x]}
function enumerate(v,cb){if(v.some(n=>n<0))return;let a=[];
 function run(){let has=false;for(let i=0;i<6;i++)if(v[i]){has=true;v[i]--;a.push(A[i]);run();a.pop();v[i]++}if(!has)cb(a)}run()}
function obs(w){let s=0;for(let a of w)s=T[s][A.indexOf(a)];return S[s]}
function prim(w){let a=[];for(let x of w)a.push(...P[x]);return a}
function insert(t,p){for(let a of p){if(!t.has(a))t.set(a,new Map());t=t.get(a)}}
function overlap(t,p){let n=0;for(let a of p){if(!t.has(a))break;n++;t=t.get(a)}return n}
function verify(){let records=[];
 for(let z=1;z<=4;z++)for(let x=2*z+1;x<=9;x++){
  const y=10-x,len=18+2*z,trie=new Map(),sigs={},hist={};let n8=0,n9=0;
  for(let cd of ['c','d'])enumerate(counts(8,x,y,z,cd),w=>{
   let s=obs(w);if(!s)return;let p=prim(w);if(p.length!==len)throw Error('H8 native length');
   insert(trie,p);n8++;sigs[s]=(sigs[s]||0)+1;
  });
  for(let s of [1,2,4,8])if(!sigs[s])throw Error('H8 signature '+x+','+y+','+z);
  enumerate(counts(9,x,y,z,'c'),w=>{let s=obs(w);if(s!==16&&s!==32)return;
   let p=prim(w);if(p.length!==len)throw Error('H9 native length');
   let k=overlap(trie,p);hist[k]=(hist[k]||0)+1;n9++;
  });
  if(!n9)throw Error('H9 empty');
  const max=Math.max(...Object.keys(hist).map(Number)),upper=z===4?1:len-3;
  if(max!==upper)throw Error('sharp maximum violated '+x+','+y+','+z);
  records.push({M:[x,y,z],h8_accepted:n8,h9_FG:n9,native_length:len,max_overlap:max,overlap_histogram:hist});
 }
 if(records.length!==16)throw Error('key count');
 return{schema:'EC49FBO_SHARP_H8_H9_NATIVE_OVERLAP_V1',date:'2026-11-05',status:'PASS',
 frozen_input:'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',records};
}
if(typeof module!=='undefined' && typeof require!=='undefined' && require.main===module)
 process.stdout.write(JSON.stringify(verify(),null,2)+'\n');
