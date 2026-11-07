"use strict";
// EC49FAM. Frozen X6 native-operation and full positive BRC-key verifier.
// Run: node VERIFY_EC49FAM.js > EXACT_REPORT_EC49FAM.json
// Independent direct ordered-word census: 7^h words for each h=2..7.
const OPS={"a":[-1,-1],"b":[-2,-2],"c":[1,2,-1,-2],"d":[2,1,-2,-1],"e":[3,1,1,-3],"f":[1,-1],"g":[2,-2]};
function proofCheck(){
const letters=Object.keys(OPS);
const keyOf=(w)=>{let k=Array(6).fill(0);for(const c of w)for(const v of OPS[c])if(v>0)k[v-1]++;return k.join(",")};
const netOf=(w)=>{let k=Array(6).fill(0);for(const c of w)for(const v of OPS[c])k[Math.abs(v)-1]+=Math.sign(v);return k.join(",")};
const native=(w)=>[...w].flatMap(c=>OPS[c]);
const binom2=n=>n>=2?n*(n-1)/2:0;
const direct=(h)=>{const seen=new Set();let words=0;function rec(w){if(w.length===h){if(netOf(w)==="2,0,0,0,0,0"){words++;seen.add(keyOf(w))};return}for(const a of letters)rec(w+a)}rec("");return {seen,words}};
const formSet=(h)=>{const set=new Set();for(let z=1;2*z<=h+1;z++){const n=h+1-2*z;for(let r=0;r<=n;r++)for(let f=0;f<=n-r;f++){let g=n-r-f;set.add([2*z+r+f,r+g,z,0,0,0].join(","))}}return set};
const qCount=(h)=>{let m=Math.floor(h/2);return h%2===0?m*(m+1)*(4*m+5)/6:(m+1)*(m+2)*(4*m+3)/6};
const overlapFormula=(h,t)=>{let total=0;for(let z=1;2*z<=h+1;z++){let n=h+1-2*z;if(n>=t)total+=binom2(n-t+2)}return total};
const directCensuses=[];
for(let h=2;h<=7;h++){let {seen,words}=direct(h), formula=formSet(h);if(seen.size!==formula.size||[...formula].some(k=>!seen.has(k))||seen.size!==qCount(h))throw Error("key mismatch at h="+h);directCensuses.push({h,valid_ordered_words:words,key_count:seen.size})}
let pairsChecked=0;
const counts=[];
for(let h=2;h<=20;h++){let A=formSet(h);if(A.size!==qCount(h))throw Error("closed form");for(let t=0;t<=6;t++){let B=formSet(h+t);let intersection=[...A].filter(k=>B.has(k)).length;if(intersection!==overlapFormula(h,t))throw Error("overlap error "+h+"/"+t);pairsChecked++;if(h===8||h===9)counts.push({h,t,intersection})}}
const words=[""];for(let len=1;len<=3;len++){function rec(w){if(w.length===len){words.push(w);return}for(let a of letters)rec(w+a)}rec("")}
const nativePairs={};
for(let a of letters)for(let b of letters)if(a!==b){
let A=OPS[a],B=OPS[b],i=0;while(i<Math.min(A.length,B.length)&&A[i]===B[i])i++;
nativePairs[a+b]=i;
if(i>1)throw Error("two-symbol distinguishability failed")
}
let prefixChecked=0, sharedPartial=0;
for(const u of words)for(const v of words){
const X=native(u),Y=native(v);let actual=0;while(actual<Math.min(X.length,Y.length)&&X[actual]===Y[actual])actual++;
let i=0,prefix=0;while(i<Math.min(u.length,v.length)&&u[i]===v[i]){prefix+=OPS[u[i]].length;i++}
let expected=(i===Math.min(u.length,v.length))?prefix:prefix+nativePairs[u[i]+v[i]];
if(actual!==expected)throw Error("native LCP error "+u+"/"+v);
prefixChecked++;if(expected>prefix)sharedPartial++;
}
const replacements=[];
for(const a of letters)for(const b of letters)for(const c of letters){if(netOf(a)===netOf(b+c)&&keyOf(a)===keyOf(b+c))replacements.push(a+"->"+b+c)}
if(replacements.sort().join(",")!==["c->fg","c->gf","d->fg","d->gf"].join(","))throw Error("replacement class mismatch "+replacements);
return {native_model:"signed X6 primitive operation code",scientific_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",key_counts_direct_full_word_enumeration:directCensuses,key_pair_formula_checks:pairsChecked,h8_h9_overlap_samples:counts,prefix_word_pair_cases:prefixChecked,partial_native_step_cases:sharedPartial,local_replacements:replacements,tests:"PASS"};
}
console.log(JSON.stringify(proofCheck(),null,2));
