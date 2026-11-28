// EC49GCJ exact auxiliary strict-Hall replay; node maximal_atom_replay.js
function replay(){
let seed=20261128>>>0;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return (seed>>>0)%n};
const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
const z={models:0,strictHallLabelSubsets:0,oracleStates:0,queryChecks:0,overlapUnionChecks:0,atomEntries:0,oracleDenseEntries:0,transitionBranches:0,transitionCoordinates:0,sparseScanVisits:0,selectedAtoms:0,maxAtoms:0,friendship:[],disagreements:0};
const check=(a,msg)=>{if(!a){z.disagreements++;throw Error(msg)}};
function atoms(D,closed,b){
 const A=[];
 for(let w=1;w<(1<<b);w++)if(closed[w]){
 let v=0;
 for(let q=(w-1)&w;q;q=(q-1)&w)if(closed[q]){
 v=Math.max(v,D[q]);let r=w^q;if(closed[r])v=Math.max(v,D[q]+D[r]);
 }
 if(D[w]>v)A.push([w,D[w]]);
 }
 return A.sort((x,y)=>pc(y[0])-pc(x[0])||x[0]-y[0]);
}
function query(A,w,count=true){let used=0,d=0;for(const [a,v] of A){if(count)z.sparseScanVisits++;if((a&w)===a&&!(a&used)){used|=a;d+=v;if(count)z.selectedAtoms++}}return d}
function profile(sup,caps,ok,S,F){
 const b=caps.length,N=1<<b;
 const memo=new Map([[0,0]]);
 function rank(q){if(memo.has(q))return memo.get(q);let r=0;if(ok[q|S])r=pc(q);else for(let a=q;a;a&=a-1){r=Math.max(r,rank(q^(a&-a)));if(r===pc(q)-1)break}memo.set(q,r);return r}
 const D=[],cnt=[],closed=[],fmask=[];
 for(let w=0;w<N;w++){let f=0,u=0;for(let a=F;a;a&=a-1){let bit=a&-a,i=31-Math.clz32(bit);if((sup[i]&w)===sup[i]){f|=bit;u|=sup[i]}}fmask[w]=f;cnt[w]=pc(f);closed[w]=u===w;D[w]=cnt[w]-rank(f)}
 const A=atoms(D,closed,b);z.oracleStates++;z.atomEntries+=A.length;z.oracleDenseEntries+=closed.filter(Boolean).length;z.maxAtoms=Math.max(z.maxAtoms,A.length);
 const aset=new Set(A.map(x=>x[0]));
 for(let i=0;i<A.length;i++)for(let j=i+1;j<A.length;j++)if(A[i][0]&A[j][0]){z.overlapUnionChecks++;check(aset.has(A[i][0]|A[j][0]),"union closure")}
 for(let w=0;w<N;w++){let elig=A.filter(([a])=>(a&w)===a);let mx=elig.filter(([a])=>!elig.some(([v])=>v!==a&&(v&a)===a));let used=0,sum=0;for(let [a,v] of mx){check(!(used&a),"maximal overlap");used|=a;sum+=v}check(sum===D[w]&&query(A,w)===D[w],"query");z.queryChecks++}
 return {D,cnt,closed,A};
}
for(let model=0;model<350;model++){
 const b=2+rnd(6),n=5+rnd(8),caps=Array.from({length:b},()=>1+rnd(3)),sup=[];
 for(let i=0;i<n;i++)sup.push(i&&rnd(3)===0?sup[rnd(i)]:1+rnd((1<<b)-1));
 const c=Array.from({length:1<<b},(_,w)=>caps.reduce((s,v,i)=>s+((w>>i&1)?v:0),0));
 const ok=[true],un=[0];for(let x=1;x<(1<<n);x++){let bit=x&-x;un[x]=un[x^bit]|sup[31-Math.clz32(bit)];let v=pc(x)<c[un[x]];for(let a=x;v&&a;a&=a-1)v=ok[x^(a&-a)];ok[x]=v;z.strictHallLabelSubsets++}
 let S=0,F=(1<<n)-1,P=profile(sup,caps,ok,S,F);
 while(F){
 let E=sup[31-Math.clz32(F&-F)],H=0;for(let i=0;i<n;i++)if((F>>i&1)&&sup[i]===E)H|=1<<i;
 const Fn=F^H;
 let children=[],R=0;
 for(let t=0;t<=pc(H);t++){
 if(t)R|=(H^R)&-(H^R);
 if(!ok[S|R])break;
 const T=profile(sup,caps,ok,S|R,Fn);
 // Old persistent state is only A; dense T is the independent verifier.
 const A=P.A;
 const oldn=w=>{let m=0;for(let i=0;i<n;i++)if((F>>i&1)&&(sup[i]&w)===sup[i])m++;return m};
 const g=w=>oldn(w)-query(A,w);
 const NN=1<<b,DD=Array(NN).fill(0),out=[];
 for(let w=1;w<NN;w++)if(T.closed[w]){
 let base=0;for(let q=(w-1)&w;q;q=(q-1)&w)if(T.closed[q]){base=Math.max(base,DD[q]);if(T.closed[w^q])base=Math.max(base,DD[q]+DD[w^q])}
 const raw=T.cnt[w]-Math.min(g(w),g(w|E)-t);
 DD[w]=Math.max(base,raw);if(raw>base)out.push([w,raw]);
 check(DD[w]===T.D[w],"child rank");z.transitionCoordinates++;
 }
 out.sort((x,y)=>pc(y[0])-pc(x[0])||x[0]-y[0]);
 check(JSON.stringify(out)===JSON.stringify(T.A),"child atoms");
 children.push({R,T});z.transitionBranches++;
 }
 const child=children[rnd(children.length)];S|=child.R;F=Fn;P=child.T;
 }
 z.models++;
}
// Independent graph-nullity oracle for friendship family, all port masks k<=7.
for(let k=1;k<=7;k++){
 const b=2*k+1,N=1<<b,sup=[];
 for(let i=0;i<k;i++){let a=1<<(2*i+1),v=1<<(2*i+2);sup.push(1|a,1|v,a|v)}
 const D=[],closed=[];
 for(let w=0;w<N;w++){
 let parent=Array.from({length:b},(_,i)=>i),find=i=>{while(parent[i]!==i)i=parent[i];return i},d=0,u=0;
 for(let e of sup)if((e&w)===e){u|=e;let a=e&-e,bb=e^a,ia=find(31-Math.clz32(a)),ib=find(31-Math.clz32(bb));if(ia===ib)d++;else parent[ia]=ib}
 D[w]=d;closed[w]=u===w;
 }
 const A=atoms(D,closed,b);check(A.length===(1<<k)-1,"friendship count");
 for(let w=0;w<N;w++){let d=0;for(let i=0;i<k;i++){let e=1|(1<<(2*i+1))|(1<<(2*i+2));if((e&w)===e)d++}check(D[w]===d&&query(A,w,false)===d,"friendship query")}
 z.friendship.push({k,ports:b,labels:3*k,atoms:A.length,portQueries:N});
}
return z
}
console.log(JSON.stringify(replay(),null,2));
