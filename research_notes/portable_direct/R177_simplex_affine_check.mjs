#!/usr/bin/env node
// R177: exact finite tests of the simplex-affine provenance bridge.
// No network or third-party dependencies. Run: node R177_simplex_affine_check.mjs
const verify=function verify() {
  const fail=(s)=>{throw Error(s)};
  const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
  const V=k=>Array(k).fill(0), add=(a,b)=>a.map((x,i)=>x+b[i]);
  const vtx=(n,i)=>{const x=V(n-1);if(i)x[i-1]=1;return x};
  function maps(n){let out=[];for(let t=0;t<n**n;t++){let k=t,a=[];for(let j=0;j<n;j++){a.push(k%n);k=Math.floor(k/n)}out.push(a)}return out}
  const mul=(m,n)=>m.map(i=>n[i]);
  const eye=d=>Array.from({length:d},(_,i)=>Array.from({length:d},(_,j)=>+(i===j)));
  function MM(A,B){const C=Array.from({length:A.length},()=>V(B[0].length));for(let i=0;i<A.length;i++)for(let k=0;k<B.length;k++)if(A[i][k])for(let j=0;j<B[0].length;j++)C[i][j]+=A[i][k]*B[k][j];return C}
  const MV=(A,x)=>A.map(row=>row.reduce((t,c,i)=>t+c*x[i],0));
  const then=(f,g)=>({a:MM(g.a,f.a),b:add(MV(g.a,f.b),g.b)});
  function simplex(m){const n=m.length,r=n-1,b=vtx(n,m[0]),a=Array.from({length:r},()=>V(r));for(let j=0;j<r;j++){const z=vtx(n,m[j+1]);for(let i=0;i<r;i++)a[i][j]=z[i]-b[i]}return {a,b}}
  const E=i=>{const a=V(6);a[Math.abs(i)-1]=i>0?1:-1;return a};
  const words=[[],[E(1)],[E(6)],[E(1),E(-1)],[E(2),E(5),E(-6)],[E(6),E(-6),E(-6),E(6)],[E(1),E(3),E(-2)]];
  function summary(p){let D=V(6),J=V(6);for(const s of p){if(s.length!==6||s.reduce((t,x)=>t+Math.abs(x),0)!==1)fail("invalid native step");D=add(D,s);J=add(J,D)}return {length:p.length,D,J}}
  function action(n,m,p){const r=n-1,N=12+r,s=summary(p),t=simplex(m),a=eye(N),b=V(N);for(let i=0;i<6;i++){a[6+i][i]=s.length;b[i]=s.D[i];b[6+i]=s.J[i]}for(let i=0;i<r;i++){b[12+i]=t.b[i];for(let j=0;j<r;j++)a[12+i][12+j]=t.a[i][j]}return {a,b}}
  function decode(n,x){const r=n-1,pts=Array.from({length:n},(_,i)=>vtx(n,i)),m=[];for(const z of pts){const out=Array.from({length:r},(_,i)=>x.b[12+i]+z.reduce((a,c,j)=>a+c*x.a[12+i][12+j],0));const i=pts.findIndex(v=>eq(v,out));if(i<0)fail("invalid provenance block");m.push(i)}return {m,length:x.a[6][0],D:x.b.slice(0,6),J:x.b.slice(6,12)}}
  const gcd=(x,y)=>{while(y){let t=x%y;x=y;y=t}return Math.abs(x)};
  const q=(a,b=1)=>{if(b<=0)fail("nonpositive denominator");let g=gcd(Math.abs(a),b);return [a/g,b/g]};
  const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
  function H(n,terms){const h=new Map();for(const t of terms){if(!t.c)continue;if(t.c<0||t.w[0]<=0)fail("nonpositive atom");const a=t.action||action(n,t.m,t.p),k=JSON.stringify([t.i,t.j,t.w,a]);if(h.has(k))h.get(k).c+=t.c;else h.set(k,{i:t.i,j:t.j,w:t.w,a,c:t.c})}return h}
  function rawThen(A,B){const z=[];for(const x of A)for(const y of B)if(x.j===y.i)z.push({i:x.i,j:y.j,w:qm(x.w,y.w),m:mul(x.m,y.m),p:x.p.concat(y.p),c:x.c*y.c});return z}
  function histThen(n,A,B){const z=[];for(const x of A.values())for(const y of B.values())if(x.j===y.i)z.push({i:x.i,j:y.j,w:qm(x.w,y.w),action:then(x.a,y.a),c:x.c*y.c});return H(n,z)}
  const signature=h=>JSON.stringify([...h].map(([k,x])=>[k,x.c]).sort((a,b)=>a[0].localeCompare(b[0])));
  const mk=(i,j,m)=>({i,j,m,A:q(0),L:q(0),B:Array.from({length:6},()=>q(0)),C:Array.from({length:6},()=>q(0))});
  const mkkey=(i,j,m)=>JSON.stringify([i,j,m]);
  function moments(n,h){const R=new Map();for(const t of h.values()){const s=decode(n,t.a),key=mkkey(t.i,t.j,s.m),x=R.get(key)||mk(t.i,t.j,s.m),w=qm(t.w,q(t.c));x.A=qa(x.A,w);x.L=qa(x.L,qm(w,q(s.length)));for(let k=0;k<6;k++){x.B[k]=qa(x.B[k],qm(w,q(s.D[k])));x.C[k]=qa(x.C[k],qm(w,q(s.J[k])))}R.set(key,x)}return R}
  function momThen(A,B){const R=new Map();for(const f of A.values())for(const g of B.values())if(f.j===g.i){const m=mul(f.m,g.m),key=mkkey(f.i,g.j,m),z=R.get(key)||mk(f.i,g.j,m);z.A=qa(z.A,qm(f.A,g.A));z.L=qa(z.L,qa(qm(f.L,g.A),qm(f.A,g.L)));for(let k=0;k<6;k++){z.B[k]=qa(z.B[k],qa(qm(f.B[k],g.A),qm(f.A,g.B[k])));z.C[k]=qa(z.C[k],qa(qa(qm(f.C[k],g.A),qm(f.A,g.C[k])),qm(f.B[k],g.L)))}R.set(key,z)}return R}
  const sigm=h=>JSON.stringify([...h].sort((a,b)=>a[0].localeCompare(b[0])));
  const counts={label_pairs:{},distinct_label_actions:{},joint_pairs:{},port_pairs:{},moment_products:{}};
  for(const n of [2,3,4]){const S=maps(n);if(new Set(S.map(x=>JSON.stringify(simplex(x)))).size!==S.length)fail("nonfaithful representation");counts.distinct_label_actions[n]=S.length;let c=0;for(const x of S)for(const y of S){if(!eq(then(simplex(x),simplex(y)),simplex(mul(x,y))))fail("simplex composition");c++}counts.label_pairs[n]=c}
  for(const n of [2,3]){let c=0;const S=maps(n),pairs=n===2?words.flatMap(p=>words.map(q=>[p,q])):[[words[0],words[1]],[words[1],words[2]],[words[3],words[4]],[words[5],words[6]],[words[6],words[5]]];for(const a of S)for(const b of S)for(const [p,q] of pairs){if(!eq(then(action(n,a,p),action(n,b,q)),action(n,mul(a,b),p.concat(q))))fail("joint composition");c++}counts.joint_pairs[n]=c}
  for(const n of [2,3]){let c=0,m=0;const S=maps(n),fs=[];for(let k=0;k<6;k++)fs.push([
    {i:0,j:1,w:q(1+k,2+k),m:S[(5*k+1)%S.length],p:words[(k+1)%words.length],c:1+k%3},
    {i:1,j:0,w:q(2+k,5+k),m:S[(7*k+2)%S.length],p:words[(k+3)%words.length],c:2},
    {i:0,j:0,w:q(3+k,7+k),m:S[(11*k+3)%S.length],p:words[k%words.length],c:1}
  ]);for(const F of fs)for(const G of fs){const hf=H(n,F),hg=H(n,G),lhs=H(n,rawThen(F,G)),rhs=histThen(n,hf,hg);if(signature(lhs)!==signature(rhs))fail("BRC serial mismatch");c++;if(sigm(moments(n,rhs))!==sigm(momThen(moments(n,hf),moments(n,hg))))fail("four-moment product mismatch");m++}counts.port_pairs[n]=c;counts.moment_products[n]=m}
  return {status:"R177_EXACT_SIMPLEX_PROVENANCE_LIFT_PASS",arithmetic:"exact safe integer matrices; reduced rational weight pairs; all tested integers below 2^53",ambient_native_axes:6,primitive_steps:"signed unit E_1,...,E_6",label_monoid:"full transformation monoid T_n, chronological multiplication",image_ranks:{2:1,3:2,4:3},dimensions:{2:{old_R176:16,new_R177:13},3:{old_R176:39,new_R177:14},4:{old_R176:268,new_R177:15}},checks:counts,executed_native_import:false,formal_claim:false,independent_review:false};
};
console.log(JSON.stringify(verify(),null,2));
