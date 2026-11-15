// R194 exact finite witness and reset-observer checker; Node.js >=18, no dependencies.
// Symbolic Lemmas 1 and 2 are in R194 markdown, not established by finite tests.
const validate = function validate(){
const eq=(a,b)=>a.length===b.length&&a.every((v,i)=>v===b[i]);
const star=(u,v)=>u.filter(z=>!v.includes(z)).concat(v);
function perms(a){if(a.length===0)return [[]];let out=[];for(let i=0;i<a.length;i++){let b=a.slice(0,i).concat(a.slice(i+1));for(const p of perms(b))out.push([a[i],...p])}return out}
function states(k){let res=[[]];function rec(w,used){if(w.length===k)return;for(let j=0;j<k;j++)if(!used.has(j)){let v=[...w,j];res.push(v);used.add(j);rec(v,used);used.delete(j)}}rec([],new Set());return res}
const stat={scope:"exact finite reference checks, symbolic theorem proven separately",k_range:[1,7],witness_pairs:0,appended_generator_identities:0,suffix_fix_identities:0,distinct_character_labels:0,codec_states_checked:0,codec_injections_checked:0,composition_checks:0,rank_formula_checks:0,per_k:[]};
for(let k=1;k<=7;k++){
const letters=Array.from({length:k},(_,i)=>i);
const As=letters.map(i=>[i]);for(let i=0;i<k;i++)for(let j=i+1;j<k;j++)As.push([i,j]);
let nW=0,nApp=0,nFix=0;
for(const A of As){
const R=letters.filter(c=>!A.includes(c));
for(const tail of perms(R)){
const u=A.length===1?[A[0],...tail]:[A[0],A[1],...tail];
const v=A.length===1?[...tail]:[A[1],A[0],...tail];
if(eq(u,v))throw Error("distinctness failed");
if(!eq(star(u,tail),u)||!eq(star(v,tail),v))throw Error("suffix fixedness failed");
nFix+=2;
for(const a of A){if(!eq(star(u,[a]),star(v,[a])))throw Error("A-annihilation failed");nApp++}
for(const c of R){
const Rt=star(tail,[c]);
const ua=A.length===1?[A[0],...Rt]:[A[0],A[1],...Rt];
const va=A.length===1?[...Rt]:[A[1],A[0],...Rt];
if(!eq(star(u,[c]),ua)||!eq(star(v,[c]),va))throw Error("R-invariance failed");nApp+=2
}
nW++;
}
}
stat.witness_pairs+=nW;stat.appended_generator_identities+=nApp;stat.suffix_fix_identities+=nFix;stat.distinct_character_labels+=As.length;
let nStates=0,nComps=0,nRanks=0;
if(k<=6){
const ss=states(k),features=As;
const S=w=>features.map(A=>{for(let i=w.length-1;i>=0;i--)if(A.includes(w[i]))return w[i];return -1});
const m=new Map(),sigs=[];
for(const w of ss){const sig=S(w),key=sig.join(",");if(m.has(key))throw Error("observer not injective");m.set(key,w);sigs.push(sig);nStates++}
if(k<=5) for(let i=0;i<ss.length;i++)for(let j=0;j<ss.length;j++){
const z=S(star(ss[i],ss[j]));const t=sigs[i].map((v,h)=>sigs[j][h]>=0?sigs[j][h]:v);
if(!eq(z,t))throw Error("reset composition failed");nComps++
}
for(const w of ss){
const r=new Set(w).size;
const direct=features.filter(A=>A.every(v=>!w.includes(v))).length;
const form=(k-r)+(k-r)*(k-r-1)/2;
if(direct!==form)throw Error("rank formula failed");nRanks++
}
}
stat.codec_states_checked+=nStates;stat.codec_injections_checked+=nStates;stat.composition_checks+=nComps;stat.rank_formula_checks+=nRanks;
stat.per_k.push({k,witness_pairs:nW,append_checks:nApp,suffix_fix_checks:nFix,characters:As.length,distinct_states:nStates,composition_checks:nComps,rank_checks:nRanks});
}
return stat;
};
const result = validate();
console.log(JSON.stringify(result,null,2));
