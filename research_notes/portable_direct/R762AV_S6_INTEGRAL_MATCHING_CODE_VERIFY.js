"use strict";
const assert=(x,s)=>{if(!x)throw Error(s)};
const choose=(n,k)=>{const out=[];function go(a,j){if(a.length===k){out.push(a);return}for(let i=j;i<n;i++)go([...a,i],i+1)}go([],0);return out};
function perfect(xs){if(!xs.length)return [[]];const [a,...rest]=xs;return rest.flatMap(b=>perfect(rest.filter(x=>x!==b)).map(t=>[[a,b],...t]))}
const states=choose(6,3),matches=perfect([0,1,2,3,4,5]),basis=[0,4,8,10,1],pivot=[0,1,2,4,5];
const sign=(S,m)=>m.some(([a,b])=>S.includes(a)===S.includes(b))?0:(m.filter(([a,b])=>S.includes(b)).length%2?-1:1);
const F=states.map(S=>matches.map(m=>sign(S,m))),B=F.map(r=>basis.map(j=>r[j]));
function det(input){const a=input.map(r=>r.map(BigInt)),n=a.length;let d=1n,sgn=1n;for(let k=0;k<n-1;k++){if(a[k][k]===0n){let l=k+1;while(l<n&&a[l][k]===0n)l++;if(l===n)return 0n;[a[k],a[l]]=[a[l],a[k]];sgn=-sgn}const p=a[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){const z=a[i][j]*p-a[i][k]*a[k][j];assert(z%d===0n,"nonexact elimination");a[i][j]=z/d}a[i][k]=0n}d=p}return sgn*a[n-1][n-1]}
const minor=pivot.map(i=>B[i]),minorDet=det(minor);assert(minorDet===1n||minorDet===-1n,"basis not unimodular on pivot");
function decode(v){return Array.from({length:5},(_,j)=>{const C=minor.map((row,i)=>row.map((x,k)=>k===j?v[pivot[i]]:x));return det(C)/minorDet})}
const coeff=matches.map((m,j)=>decode(F.map(r=>r[j])));
for(let j=0;j<15;j++)for(let i=0;i<20;i++)assert(BigInt(F[i][j])===coeff[j].reduce((z,x,k)=>z+x*BigInt(B[i][k]),0n),"matching relation");
function permute(xs){if(!xs.length)return [[]];return xs.flatMap((x,i)=>permute(xs.filter((v,j)=>j!==i)).map(p=>[x,...p]))}
const perms=permute([0,1,2,3,4,5]),index=new Map(states.map((S,i)=>[S.join(""),i]));let stabilizer=0,maxEntry=0;
const matrices=new Set(),sample=[];
for(const p of perms){const inv=Array(6);for(let i=0;i<6;i++)inv[p[i]]=i;
 const lookup=states.map(S=>index.get(S.map(x=>inv[x]).sort((a,b)=>a-b).join("")));
 const cols=basis.map(j=>decode(lookup.map(i=>F[i][j])));
 for(let i=0;i<20;i++)for(let j=0;j<5;j++)assert(BigInt(F[lookup[i]][basis[j]])===cols[j].reduce((z,v,k)=>z+v*BigInt(B[i][k]),0n),"S6 action");
 const A=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>cols[j][i]));
 assert(det(A)===1n||det(A)===-1n,"non-unimodular S6");
 if(cols.slice(0,4).every(v=>v[4]===0n))stabilizer++;
 for(const row of A)for(const x of row)maxEntry=Math.max(maxEntry,Number(x<0n?-x:x));
 matrices.add(A.map(r=>r.join(",")).join(";"));
 if(p.join(",")==="1,0,2,3,4,5")sample.push({permutation:p,action:A.map(r=>r.map(Number))});
}
assert(states.length===20&&matches.length===15&&perms.length===720,"enumeration");
assert(stabilizer===24&&matrices.size===720,"group action counts");
assert(sample.length===1&&sample[0].action[4].slice(0,4).some(x=>x!==0),"4D non-invariance");
const output={schema:"R762AV_S6_MATCHING_CODE_INTEGRAL_COVARIANCE_V1",result:"PASS",state_count:states.length,matching_count:matches.length,permutations_checked:perms.length,
 matching_pairs:matches,four_original_indices:basis.slice(0,4),integral_basis_indices:basis,
 pivot_triad_indices:pivot,pivot_triads:pivot.map(i=>states[i]),pivot_minor_det:minorDet.toString(),
 all_15_matching_integral_coefficients:coeff.map(x=>x.map(Number)),
 minimal_S6_stable_rank_containing_original_four:5,original_four_rank:4,
 stabilizer_original_four_span:stabilizer,faithful_five_dimensional_actions:matrices.size,
 maximum_absolute_action_entry:maxEntry,witness_transposition_01:sample[0],
 proof_scope:"Exact 20x15 integer matching code and S6 change-of-label action, conditional observer layer"};
if(typeof console!=="undefined")console.log(JSON.stringify(output,null,2));
