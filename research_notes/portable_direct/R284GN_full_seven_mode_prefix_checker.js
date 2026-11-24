const P=z=>Math.max(0,z),bit=(p,i)=>i?((p>>(i-1))&1):0,last=(p,i)=>{for(let d=1;d<=4;d++){let e=(i-d+4)%4;if(bit(p,e)!=bit(p,(e+1)%4))return e}};
const modes=[1,3,5,7],sum=(x,ids)=>ids.reduce((s,i)=>s+x[i],0);
function D(x,a,q){
 let U=x[3]-a[3],V=x[7]-a[7],W=P(a[1]+a[5]-q);
 let d2=Math.max(0,P(U-q)+P(V-q)-q,W+P(x[2]-q)+P(x[6]-q)-q,W+P(U+x[2]-q)+P(V+x[6]-q)-2*q);
 let s=P(a[1]+a[3]-q),l=Math.max(0,s-a[3]),h=Math.min(s,a[1]),p1=x[6],p2=x[4]+x[5]-a[5],p0=x[7]-a[7];
 let m=(t1,t2)=>Math.max(0,s-t1-t2,l-t1,s-h-t2);
 let d3=Math.max(m(q,q),P(p0-q)+m(q-p1,q-p2)-q);
 return [d2,d3];
}
function cuts(j){let out=new Map();for(let U=0;U<256;U++){let w=[],v=[];for(let p=1;p<=7;p++){let E=(1<<last(p,0))|(1<<(4+last(p,j)));if(bit(p,0)!=bit(p,j)&&(U&E)==E)w.push(p);if(bit(p,1)!=bit(p,j)&&(U&(1<<(4+last(p,j)))))v.push(p)}
let k=w.join('')+'/'+v.join(''),c=U.toString(2).replace(/0/g,'').length;if(!out.has(k)||out.get(k).c>c)out.set(k,{w,v,c})}return [...out.values()]}
function regression(){const c2=cuts(2),c3=cuts(3);let comparisons=0,prefixes=0,allocations=0;
let x=Array(8).fill(0),a=Array(8).fill(0),s=Array(8).fill(0);
function verify(q){let y=[Infinity,Infinity];function rec(k,r){if(k===4){let w=x.map((v,i)=>v-s[i]);let c=[c2,c3].map(cs=>Math.max(...cs.map(t=>sum(w,t.w)+sum(s,t.v)-q*t.c)));y=y.map((v,i)=>Math.min(v,c[i]));allocations++;return}let p=modes[k];for(let o=0;o<=Math.min(r,a[p]);o++){s[p]=a[p]-o;rec(k+1,r-o)}s[p]=0}rec(0,q);let d=D(x,a,q);if(d.some((v,i)=>v!==y[i]))throw Error(JSON.stringify({q,x,a,d,y}));prefixes++;comparisons+=2}
function hist(p){if(p===8){function pre(k){if(k===4){for(let q=0;q<=3;q++)verify(q);return}let p=modes[k];for(let v=0;v<=x[p];v++){a[p]=v;pre(k+1)}a[p]=0}pre(0);return}for(let v=0;v<=2;v++){x[p]=v;hist(p+1)}}hist(1);return {prefixes,comparisons,allocations,cutCounts:[c2.length,c3.length]};}
const G=[[[1],[3],[5,7]],[[2],[6],[1,5]],[[3],[4],[2,5]],[[7],[6],[4,5]]],O=[[2,3,6,7],[1,3,6,4]],order=[3,5,6,1,4,2,7];
function stable(x,q,u){return O.every(([a,b,c,d])=>Math.max(0,x[a]-2*q,x[b]-2*q,x[c]-2*q,x[d]-2*q,x[a]+x[b]-3*q,x[c]+x[d]-3*q,x[a]+x[c]-3*q,x[b]+x[d]-3*q,x[a]+x[b]+x[c]+x[d]-4*q)>=2*u+1)}
const rot=Array.from({length:4},(_,e)=>Array.from({length:8},(_,p)=>{let z=0;for(let i=1;i<=3;i++)z|=(bit(p,(e+i)%4)^bit(p,e))<<(i-1);return z}));
function finite(q,u){
 let n=Math.min(4*q+8*u+2,Math.max(5*q+5*u+2,6*q+4*u+2))-1,x=Array(8).fill(0),ge=0,st=0,nodes=0,pruned=0,fail=[0,0,0,0],surv=[];
 function path(y){let a=Array(8).fill(0),memo=new Map();function rec(){let key=0;for(let p of modes)key=key*(y[p]+1)+a[p];if(memo.has(key))return memo.get(key);nodes++;if(D(y,a,q).some(v=>v<2*u+1)){memo.set(key,false);return false}let full=true;for(let p of modes)if(a[p]<y[p]){full=false;a[p]++;let ok=rec();a[p]--;if(ok){memo.set(key,true);return true}}memo.set(key,full);return full}return rec()}
 function test(){ge++;if(!stable(x,q,u))return;st++;for(let e=0;e<4;e++){let y=Array(8).fill(0);for(let p=1;p<=7;p++)y[rot[e][p]]=x[p];if(!path(y)){fail[e]++;return}}surv.push(x.slice(1))}
 let future=Array.from({length:8},(_,k)=>new Set(order.slice(k)));
 function gen(k,r){for(let g of G){let total=0,best=0;for(let ids of g){let z=sum(x,ids),v=P(z-q);total+=v;if(ids.some(p=>future[k].has(p)))best=Math.max(best,P(z+r-q)-v)}if(total+best<q+4*u+1){pruned++;return}}if(k===6){x[order[k]]=r; if(G.every(g=>g.reduce((z,ids)=>z+P(sum(x,ids)-q),0)>=q+4*u+1))test();x[order[k]]=0;return}let p=order[k];for(let v=0;v<=r;v++){x[p]=v;gen(k+1,r-v)}x[p]=0}
 gen(0,n);return {q,u,n,ge,st,nodes,pruned,fail,surv};
}
if(process.argv[2]==='regression')console.log(JSON.stringify(regression()));else for(let q=+process.argv[2];q<=+process.argv[3];q++)console.log(JSON.stringify(finite(q,+process.argv[4])));
