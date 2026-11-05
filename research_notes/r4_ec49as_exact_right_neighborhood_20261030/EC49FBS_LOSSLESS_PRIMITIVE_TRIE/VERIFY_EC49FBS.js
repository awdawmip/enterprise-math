"use strict";
const OPS="acdefg";
const STEP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const SIGN=[0,0,4,1,16,32,8,2,0], VALID=new Set([1,2,4,8,16,32]);
const ROOT=["fe","ge","feg","gef"];
const CASES={
 M641:["fegc","fegd","gefc","gefd","fegfg","geffg","fegccc","fegddd","gefccc","gefddd","fegccfg","fegddgf","gefccfg","gefddgf","fegffggc","fegffggd","gefffggc","gefffggd","fegffgggf","gefffgggf"],
 M732:["cefg","degf","fegd","gefc","feggf","geffg","ceceac","dedead","eaeccc","eaeddd","ceceafg","dedeagf","eaeccfg","eaeddgf","fegaefgc","fegaefgd","gefaefgc","gefaefgd","fegaefggf","gefaefggf"]
};
function nativeCost(words){
 const s=new Set();for(const w of words){let p="";
 for(const c of w)for(const a of STEP[c]){p+=a+",";s.add(p);}}
 return s.size;
}
function compressed(words){
 const trie=new Map();
 for(const w of words){let p="";for(const c of w){
 if(!trie.has(p))trie.set(p,new Set());trie.get(p).add(c);p+=c;}}
 let weighted=0,cf=0,dg=0,operationEdges=0;
 for(const outs of trie.values()){
 operationEdges+=outs.size;
 for(const c of outs)weighted+=STEP[c].length;
 if(outs.has("c")&&outs.has("f"))cf++;
 if(outs.has("d")&&outs.has("g"))dg++;
 }
 return {operation_prefixes:trie.size,operation_edges:operationEdges,weighted_operation_edges:weighted,collision_cf:cf,collision_dg:dg,cost:weighted-cf-dg};
}
function check(words){const n=nativeCost(words),v=compressed(words);
 if(n!==v.cost)throw Error("compressed cost mismatch");
 return {native_edges:n,...v};}
function enumerate(h,key){
 let [x,y,z]=key,nc=x+y-h-1;
 let q={a:z-1,c:0,d:0,e:z,f:h+1-y-2*z,g:h+1-x},out=[];
 if(nc<0||Object.values(q).some(v=>v<0))return out;
 for(let k=0;k<=nc;k++){
 q.c=k;q.d=nc-k;
 function rec(st,left,w){
 if(left===0){if(VALID.has(SIGN[st]))out.push(w);return;}
 for(let j=0;j<6;j++){const c=OPS[j],ns=T[st][j];
 if(q[c]&&ns!==8){q[c]--;rec(ns,left-1,w+c);q[c]++;}}
 }
 rec(0,h,"");
 }
 return out;
}
const witness={};for(const [name,words] of Object.entries(CASES))witness[name]=check(ROOT.concat(words));
if(witness.M641.native_edges!==116 || witness.M732.native_edges!==166)throw Error("FBR witness mismatch");
const perWindow={},candidates=ROOT.slice(),pairDomain=[];
for(let h=4;h<=9;h++){
 const arr=enumerate(h,h<6?[4,2,1]:[7,3,2]);perWindow[h]=arr.length;
 candidates.push(...arr);if(h<=6)pairDomain.push(...arr);
}
const full=check(candidates);
if(full.native_edges!==109972||full.operation_edges!==41438||full.collision_cf!==2203||full.collision_dg!==2203)throw Error("candidate trie mismatch");
let pairCount=0;
for(let i=0;i<pairDomain.length;i++)for(let j=i+1;j<pairDomain.length;j++){check([pairDomain[i],pairDomain[j]]);pairCount++;}
if(pairCount!==18336)throw Error("pair count mismatch");
for(const word of candidates)check([word]);
console.log(JSON.stringify({
 schema:"EC49FBS_LOSSLESS_NATIVE_TRIE_CERTIFICATE_V1",
 scientific_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
 cases:witness,per_window_candidate_counts:perWindow,
 all_candidate_words_including_four_frozen_root:candidates.length,
 full_candidate_trie:full,
 exhaustive_pair_verification:{domain:"H4(L)+H5(L)+H6(M732)",candidate_words:pairDomain.length,unordered_pairs:pairCount,failures:0},
 singleton_verification:{count:candidates.length,failures:0}
},null,2));