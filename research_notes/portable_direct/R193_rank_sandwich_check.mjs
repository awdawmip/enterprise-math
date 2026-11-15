#!/usr/bin/env node
// R193 independent exact integer finite word-algebra verification.
// Run: node R193_rank_sandwich_check.mjs

function states(A){const out=[[]];function walk(p,rem){for(const x of rem){const q=[...p,x];out.push(q);walk(q,rem.filter(y=>y!==x))}}walk([],A);return out}

function add(s,x){return [...s.filter(y=>y!==x),x]}

function concat(s,t){return t.reduce((p,x)=>add(p,x),[...s])}

function eq(a,b){return a.length===b.length&&a.every((v,i)=>v===b[i])}

function obs(s,U){for(let n=s.length-1;n>=0;n--)if(U.includes(s[n]))return s[n]+1;return 0}

function verify(){const records=[];let sandwich=0,rightZero=0,distinct=0;
for(let k=2;k<=7;k++){const A=Array.from({length:k},(_,i)=>i);let ctS=0,ctZ=0,ctD=0;
for(let i of A){const rest=A.filter(x=>x!==i),S=states(rest);const mapped=S.map(s=>concat(s,[i]).join(","));if(new Set(mapped).size!==mapped.length)throw Error("noninjective");ctD+=mapped.length;
for(let s of S)for(let j of rest){const lhs=concat(concat(concat(s,[i]),[j]),[i]);const rhs=concat(concat(s,[j]),[i]);if(!eq(lhs,rhs))throw Error(`sandwich failed ${k} ${i} ${s} ${j}`);ctS++}}
for(let i=0;i<k;i++)for(let j=i+1;j<k;j++)for(let s of states([i,j])){if(!eq(concat(s,[i,j]),[i,j]))throw Error("rightzero failed");ctZ++}
records.push({k,partial_states:states(A).length,sandwich_checks:ctS,injective_embedded_states:ctD,pair_right_zero_checks:ctZ});sandwich+=ctS;rightZero+=ctZ;distinct+=ctD}
const Fs=[[0],[1],[0,1]];const v=s=>Fs.map(U=>obs(s,U));const a=v([0]),b=v([1]),ab=v([0,1]),ba=v([1,0]),zero=v([]);
const det3=(p,q,r)=>p[0]*(q[1]*r[2]-q[2]*r[1])-p[1]*(q[0]*r[2]-q[2]*r[0])+p[2]*(q[0]*r[1]-q[1]*r[0]);const determinant=det3(a,b,ab);if(determinant===0)throw Error("bad orbit determinant");
return {schema:"EM_R193_RANK_SANDWICH_EXACT_V1",status:"PASS",frozen_science_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",check_method:"exact integer typed-word semigroup checks; direct 3x3 integer determinant",test_k_range:[2,7],records,total_sandwich_checks:sandwich,total_injective_embedded_states:distinct,total_pair_right_zero_checks:rightZero,S2_orbit_vectors:{epsilon:zero,a,b,ab,ba},S2_affine_minor_determinant:determinant,proof_scope:"all k>=2 by mathematical argument over Q",bound:"m(2)=3; m(k)>=m(k-1)+2 for k>=3; m(k)>=2k-1",native_BRC_module:"NOT_EXECUTED",review:"NOT_REVIEWED"};}

console.log(JSON.stringify(verify(),null,2));
