// Stage401-B independent BigInt + exact future-behavior automaton (Node >=18).
const A=[1,-1,2,-2,3,-3,4,-4,5,-5,6,-6];
const delta=a=>Array.from({length:6},(_,i)=>Math.abs(a)==i+1?Math.sign(a):0);
const end=w=>w.reduce((z,a)=>z.map((v,i)=>v+delta(a)[i]),[0,0,0,0,0,0]);
const hist=w=>{let x={};for(let i=1;i<w.length;i++){let k=w[i-1]+','+w[i];x[k]=(x[k]||0)+1;}return Object.entries(x).sort()};
const obs=W=>{const p=W.map(x=>x[0]),q=W.map(x=>x[1]);return JSON.stringify([W.length,end(p),hist(p),end(q),hist(q),W.filter(x=>x[0]==x[1]).length]);};
const inverse=(x,y)=>x[0]==-y[0]&&x[1]==-y[1];
const g=(W,c)=>{if(!c)return JSON.stringify(W.length?W.at(-1):['EMPTY']);return JSON.stringify([g(W,c-1),g(W.slice(0,-1),c-1),W.length>1&&inverse(W.at(-2),W.at(-1))?g(W.slice(0,-2),c-1):'ABSENT']);};
const s=(w,c)=>{if(!c)return JSON.stringify(w.length?w.at(-1):'EMPTY');return JSON.stringify([s(w,c-1),s(w.slice(0,-1),c-1),w.length>1&&w.at(-2)==-w.at(-1)?s(w.slice(0,-2),c-1):'ABSENT']);};
function countBRC(m,z){let d=new Map([['0,0,0,0,0,0',1n]]);for(let i=0;i<m;i++){let n=new Map();for(let [key,v] of d){let c=key.split(',').map(Number);for(let a of A){let x=c.map((t,j)=>t+delta(a)[j]).join(',');n.set(x,(n.get(x)||0n)+v);}}d=n;}return (d.get(z.join(','))||0n).toString();}
function words(alpha,n){let out=[[]];for(let i=0;i<n;i++)out=out.flatMap(w=>alpha.map(a=>[...w,a]));return out;}
function check(alpha,nmax=4,R=3){const cached=new Map(),intern=new Map();function f(W,c,r){let k=JSON.stringify([W,c,r]);if(cached.has(k))return cached.get(k);let app=r?alpha.map(a=>f([...W,a],c,r-1)):[];let cancel=c&&W.length>1&&inverse(W.at(-2),W.at(-1))?f(W.slice(0,-2),c-1,r):null;let sig=JSON.stringify([obs(W),app,cancel]);if(!intern.has(sig))intern.set(sig,intern.size+1);cached.set(k,intern.get(sig));return cached.get(k);}let totals=[];for(let c=0;c<=2;c++){let pairs=0,same=0,groups=0;for(let n=0;n<=nmax;n++){let classes=new Map();for(let W of words(alpha,n)){let key=obs(W);if(!classes.has(key))classes.set(key,[]);classes.get(key).push(W);}for(let G of classes.values()){if(G.length<2)continue;groups++;pairs+=G.length*(G.length-1)/2;let bySig=new Map();for(let W of G){let key=g(W,c);if(!bySig.has(key))bySig.set(key,[]);bySig.get(key).push(W);}let ids=[];for(let S of bySig.values()){let v=new Set(S.map(W=>f(W,c,R)));if(v.size!==1)throw Error('noncongruence');ids.push([...v][0]);same+=S.length*(S.length-1)/2;}if(new Set(ids).size!==ids.length)throw Error('unseparated signatures');}}totals.push([c,pairs,same,groups]);}return totals;}
const p=[1,1,-1,1,-1],pp=[1,-1,1,1,-1],q=[3,3,3,3,3],W=p.map((a,i)=>[a,q[i]]),V=pp.map((a,i)=>[a,q[i]]);
if(obs(W)!==obs(V)||s(p,1)===s(pp,1)||g(W,1)!==g(V,1)||g(W,2)===g(V,2))throw Error('witness failure');
if(countBRC(5,[1,0,0,0,0,0])!=='1660'||countBRC(5,[0,0,5,0,0,0])!=='1')throw Error('BRC failure');
const shared=[[1,1],[1,-1],[-1,1],[-1,-1]],apart=[[1,3],[1,-3],[-1,3],[-1,-3]];
console.log('BRC5=',countBRC(5,[1,0,0,0,0,0]),countBRC(5,[0,0,5,0,0,0]));
console.log('SHARED_ALPHABET=',JSON.stringify(check(shared)));
console.log('DISJOINT_ALPHABET=',JSON.stringify(check(apart)));
console.log('WITNESS_G1_EQ_S1_NE_G2_NE_PASS');
console.log('STAGE401B_INDEPENDENT_JS_EXACT_PASS');
