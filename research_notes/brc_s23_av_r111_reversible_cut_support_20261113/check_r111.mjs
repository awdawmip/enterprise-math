const checkR111 = function checkR111(){
"use strict";
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let r=a%b;a=b;b=r;}return a||1n;};
const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("denominator zero");if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return {n:a/g,d:b/g};};
const neg=a=>Q(-a.n,a.d),add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>add(a,neg(b)),times=(a,m)=>Q(a.n*BigInt(m),a.d),over=(a,m)=>Q(a.n,a.d*BigInt(m)),cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0,key=a=>a.n+"/"+a.d;
const fl=a=>a.n<0n&&a.n%a.d!==0n?a.n/a.d-1n:a.n/a.d,ce=a=>-fl(neg(a)),fr=a=>sub(a,Q(fl(a)));
const L=Q(0),U=Q(1),x=Q(1,4),j=0,a=0,c=1;
const forms=t=>[[a,Q(0)],[c,Q(0)],[a-c,Q(0)],[t-j,x],[t-j-a,x],[t-j-c,x]];
const cutsAff=(m,d)=>{if(!m)return [];let lo=add(times(L,m),d),hi=add(times(U,m),d);if(cmp(lo,hi)>0)[lo,hi]=[hi,lo];let out=[];for(let n=ce(lo);n<=fl(hi);n++){let p=over(sub(Q(n),d),m);if(cmp(L,p)<0&&cmp(p,U)<0)out.push(p);}return out;};
const cuts=t=>{let m=new Map();for(const [s,d] of forms(t))for(const q of cutsAff(s,d))m.set(key(q),q);return [...m.values()].sort(cmp);};
const nextAff=(m,d,p)=>{if(!m)return null;let v=add(times(p,m),d),n=m>0?fl(v)+1n:ce(v)-1n;return over(sub(Q(n),d),m);};
const lazy=t=>{let p=L,out=[];for(let i=0;i<300;i++){let q=null;for(const [m,d] of forms(t)){const v=nextAff(m,d,p);if(v&&cmp(v,U)<0&&(!q||cmp(v,q)<0))q=v;}if(!q)return out;out.push(q);p=q;}throw Error("successor overflow");};
const h=z=>z?z.h:0,N=(p,count,l,r)=>({p,count,l,r,h:Math.max(h(l),h(r))+1});
const rR=z=>{const y=z.l;return N(y.p,y.count,y.l,N(z.p,z.count,y.r,z.r));};
const rL=z=>{const y=z.r;return N(y.p,y.count,N(z.p,z.count,z.l,y.l),y.r);};
const balance=z=>{if(!z)return null;const d=h(z.l)-h(z.r);if(d>1){const l=h(z.l.l)<h(z.l.r)?rL(z.l):z.l;return rR(N(z.p,z.count,l,z.r));}if(d< -1){const r=h(z.r.r)<h(z.r.l)?rR(z.r):z.r;return rL(N(z.p,z.count,z.l,r));}return z;};
const takeMin=z=>{if(!z.l)return {min:z,rest:z.r};const q=takeMin(z.l);return {min:q.min,rest:balance(N(z.p,z.count,q.rest,z.r))};};
const change=(z,p,delta)=>{if(!z){if(delta!==1)throw Error("negative support");return N(p,1,null,null);}const v=cmp(p,z.p);if(!v){const n=z.count+delta;if(n<0)throw Error("negative refcount");if(n)return N(z.p,n,z.l,z.r);if(!z.l)return z.r;if(!z.r)return z.l;const q=takeMin(z.r);return balance(N(q.min.p,q.min.count,z.l,q.rest));}return v<0?balance(N(z.p,z.count,change(z.l,p,delta),z.r)):balance(N(z.p,z.count,z.l,change(z.r,p,delta)));};
const entries=(z,o=[])=>{if(z){entries(z.l,o);o.push([key(z.p),z.count,z.p]);entries(z.r,o);}return o;};
const checkAVL=z=>{if(!z)return {height:0,first:null,last:null,n:0};const l=checkAVL(z.l),r=checkAVL(z.r);if(l.last&&cmp(l.last,z.p)>=0||r.first&&cmp(z.p,r.first)>=0)throw Error("BST order");if(Math.abs(l.height-r.height)>1||z.h!==Math.max(l.height,r.height)+1||z.count<1)throw Error("AVL metadata");return {height:z.h,first:l.first||z.p,last:r.last||z.p,n:l.n+r.n+1};};
const T=id=>Number(id.split(":")[0]),B=id=>Number(id.split(":")[1]),union=(f,g)=>new Set([...f,...g]),ts=(f,g)=>new Set([...union(f,g)].map(T));
const fresh=(f,g)=>{let z=null;for(const t of ts(f,g))for(const q of cuts(t))z=change(z,q,1);return z;};
const make=(f,g)=>({f:new Set(f),g:new Set(g),root:fresh(f,g)});
const edit=(v,side,t,b)=>{let f=new Set(v.f),g=new Set(v.g),id=t+":"+b,old=ts(f,g).has(t),set=side==="F"?f:g;set.has(id)?set.delete(id):set.add(id);const newer=ts(f,g).has(t);let z=v.root;if(old!==newer)for(const q of cuts(t))z=change(z,q,newer?1:-1);return {f,g,root:z,changed:old!==newer};};
const active=(t,p)=>{const v=fr(add(x,times(p,t-j))),l=fr(times(p,a)),r=fr(times(p,c));let d=cmp(l,r);return d<0?cmp(l,v)<=0&&cmp(v,r)<0:d>0?(cmp(v,l)>=0||cmp(v,r)<0):false;};
const top=(s,p,k)=>[...s].filter(id=>active(T(id),p)).sort((x,y)=>T(y)-T(x)||B(y)-B(x)).slice(0,k).join("|");
const shield=(f,g,p,k)=>{const C=[...f].filter(id=>g.has(id)),D=[...union(f,g)].filter(id=>f.has(id)!==g.has(id));for(const t of new Set(D.map(T))){if(!active(t,p))continue;let maxb=Math.max(...D.filter(id=>T(id)===t).map(B)),cnt=0;for(const id of C)if((T(id)>t||T(id)===t&&B(id)>maxb)&&active(T(id),p))cnt++;if(cnt<k)return {equal:false,margin:cnt-k};}return {equal:true};};
const atoms=z=>{const p=[L,...entries(z).map(e=>e[2]),U],out=[];for(let i=0;i<p.length;i++){out.push(p[i]);if(i+1<p.length)out.push(over(add(p[i],p[i+1]),2));}return out;};
let state=111129n;const rng=n=>{state=(1103515245n*state+12345n)%2147483648n;return Number(state%BigInt(n));};
let result={status:"R111_PASS",runs:0,edits:0,first_last_time_changes:0,unchanged_root_reuses:0,added_cut_points:0,removed_cut_points:0,exact_topk_and_shield_checks:0,negative_witnesses:0,retained_parent_checks:0,max_avl_nodes:0,lazy_stream_tests:0};
for(let z=0;z<3;z++){
let f=new Set(),g=new Set();for(let i=0;i<11;i++){let id=(rng(9)-4)+":"+rng(4);(rng(2)?f:g).add(id);}const history=[make(f,g)];result.runs++;
for(let step=0;step<170;step++){
const old=history[rng(history.length)],t=rng(9)-4,b=rng(4),side=rng(2)?"F":"G",before=entries(old.root),v=edit(old,side,t,b),now=entries(v.root),ref=entries(fresh(v.f,v.g));
const serial=q=>q.map(i=>i[0]+":"+i[1]).join(",");
if(serial(now)!==serial(ref))throw Error("incremental support differs from full reconstruction");
const oldSet=new Set(before.map(i=>i[0])),newSet=new Set(now.map(i=>i[0]));
for(const s of newSet)if(!oldSet.has(s))result.added_cut_points++;
for(const s of oldSet)if(!newSet.has(s))result.removed_cut_points++;
if(v.changed)result.first_last_time_changes++;else{if(v.root!==old.root)throw Error("missed root reuse");result.unchanged_root_reuses++;}
if(serial(entries(old.root))!==serial(before))throw Error("ancestor root mutated");result.retained_parent_checks++;
const tree=checkAVL(v.root);result.max_avl_nodes=Math.max(tree.n,result.max_avl_nodes);
for(const p of atoms(v.root))for(let k=1;k<=3;k++){let eq=top(v.f,p,k)===top(v.g,p,k),s=shield(v.f,v.g,p,k);if(eq!==s.equal)throw Error("rank predicate mismatch at "+key(p));if(!eq){if(s.margin>=0)throw Error("incorrect witness");result.negative_witnesses++;}result.exact_topk_and_shield_checks++;}
history.push(v);result.edits++;
}}
for(let t=-9;t<=9;t++){if(cuts(t).map(key).join(",")!==lazy(t).map(key).join(","))throw Error("lazy successor mismatch");result.lazy_stream_tests++;}
return result;
};
console.log(JSON.stringify(checkR111(), null, 2));
