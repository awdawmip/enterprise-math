'use strict';
// R762DH exact, finite author verification of sparse triangle bases.
// Run: node R762DH_SPARSE_TRIANGLE_VERIFY.js
const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a;};
const mod=(x,q)=>((x%q)+q)%q;
function tri(area,sign,i,j,k,n,q) {
 function v(a,b){return sign[a]*sign[b]*(a<b?area[a*n+b]:-area[b*n+a]);}
 return mod(v(i,j)+v(j,k)+v(k,i),q);
}
function framePatterns(n,kind){
 const mask=ids=>Array.from({length:n},(_,i)=>ids.includes(i)?-1:1);
 if(kind==='id')return [];
 if(kind==='one')return [mask([0])];
 if(kind==='complement')return [mask([0]),mask(Array.from({length:n-1},(_,j)=>j+1))];
 if(kind==='two')return [mask([0]),mask([1])];
 if(kind==='cross')return [mask([0,1]),mask([0,2])];
 throw Error('unknown frame case');
}
function selected(n,patterns) {
 const signs=[Array(n).fill(1),...patterns], edges=[];
 for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
  let w=patterns.findIndex(s=>s[i]===s[j]&&s.some(v=>v!==s[i]));
  if(w>=0)edges.push({frame:w+1,i,j,k:Array.from({length:n},(_,x)=>x).find(x=>patterns[w][x]!==patterns[w][i])});
 }
 const parent=Array.from({length:n},(_,i)=>i),root=x=>{while(parent[x]!==x)x=parent[x];return x;};
 const forest=[];
 for(const e of edges){const a=root(e.i),b=root(e.j);if(a!==b){parent[a]=b;forest.push(e);}}
 const components=new Set(Array.from({length:n},(_,i)=>root(i))).size;
 const base=[];for(let i=1;i<n;i++)for(let j=i+1;j<n;j++)base.push({frame:0,i:0,j:i,k:j});
 return {signs,base,forest,components};
}
function readZero(area,frames,probes,n,q){
 return probes.every(p=>tri(area,frames[p.frame],p.i,p.j,p.k,n,q)===0);
}
function allProbes(n,signs){
 const result=[];for(let f=0;f<signs.length;f++)for(let i=0;i<n;i++)
  for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++)result.push({frame:f,i,j,k});
 return result;
}
function checkGradient(n,q,kind){
 const s=selected(n,framePatterns(n,kind)), full=allProbes(n,s.signs);
 let unseen=0,disagreements=0,checks=q**(n-1);
 for(let t=0;t<checks;t++){
  let k=t, u=[0],area=Array(n*n).fill(0);
  for(let i=1;i<n;i++){u[i]=k%q;k=Math.floor(k/q);}
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)area[i*n+j]=mod(u[j]-u[i],q);
  const sparse=readZero(area,s.signs,s.forest,n,q);
  const complete=readZero(area,s.signs,full,n,q);
  if(sparse!==complete)disagreements++;
  if(complete)unseen++;
 }
 const expected=q**(s.components-1)*gcd(q,2)**(n-s.components);
 if(unseen!==expected||disagreements)throw Error('gradient mismatch '+JSON.stringify({n,q,kind,unseen,expected,disagreements}));
 return {n,q,kind,components:s.components,identity_queries:s.base.length,extra_queries:s.forest.length,
  predicted_unseen:expected,checked:checks};
}
function checkAllPairs(n,q,kind){
 const s=selected(n,framePatterns(n,kind)),full=allProbes(n,s.signs),m=n*(n-1)/2,checks=q**m;
 for(let t=0;t<checks;t++){
  let k=t,area=Array(n*n).fill(0);
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){area[i*n+j]=k%q;k=Math.floor(k/q);}
  const sparse=readZero(area,s.signs,s.base.concat(s.forest),n,q);
  const complete=readZero(area,s.signs,full,n,q);
  if(sparse!==complete)throw Error('all pair mismatch '+JSON.stringify({n,q,kind,t}));
 }
 return checks;
}
const kinds=['id','one','complement','two','cross'], gradientRows=[];
for(const n of [4,5,6])for(const q of [2,3,4,5,6])for(const kind of kinds)
 gradientRows.push(checkGradient(n,q,kind));
let pairAssignments=0;
for(const n of [4,5])for(const q of (n===4?[2,3,4,5]:[2,3]))
 for(const kind of ['id','one','two','cross'])
  pairAssignments+=checkAllPairs(n,q,kind);
console.log(JSON.stringify({status:'PASS',type:'AUTHOR_EXACT_INTEGER_VERIFICATION',
 configurations:gradientRows.length,
 gradients_checked:gradientRows.reduce((z,r)=>z+r.checked,0),
 pair_area_assignments_checked:pairAssignments,
 all_disagreements:0,coverage:{n:[4,5,6],q:[2,3,4,5,6],
 frame_languages:kinds,full_pairs:'n4 q2..5; n5 q2..3, four languages'},rows:gradientRows},null,2));
