console.log((function check(){
const S=[[1,120,240,-1],[1,240,120,-1],[2,60,180,0],[2,60,60,0],[2,180,60,1],[2,60,60,1],[3,30,108,2],[3,30,72,2],[3,30,45,3],[3,30,15,3],[3,90,36,4],[3,90,24,4],[3,20,40,5],[3,40,20,5]];
const F=[[-1,0,0,0],[-1,1,-1,360],[-1,2,-3,360],[1,0,0,35],[3,-4,5,2280],[3,-2,1,120],[4,-3,2,380],[4,3,-2,1560],[7,4,-15,0],[9,-2,5,3240],[13,16,-45,360],[21,2,-1,1455],[23,-14,5,120],[26,3,-2,1890],[28,12,-5,7680],[31,-18,5,0],[76,-2,5,4580],[92,16,-5,11880],[135,12,-5,9285],[192,11,3,15120],[195,-14,45,33480],[195,16,-5,13425],[212,88,-35,57240],[732,-14,45,44220]];
const C=[0x00b,0x00a,0x012,0x100,0x809,0x004,0x805,0x10a,0,0x90b,0x410,0x192,0x024,0x112,0x18a,0,0x985,0x1c7,0x992,0x997,0xb13,0x9d6,0x1cb,0xb95];
const ok=(p,m)=>{if(!p)throw Error(m)},gcd=(a,b)=>b?gcd(b,a%b):a,keys=[],idx=[];
for(let i=0;i<14;i++){let [t,p,q]=S[i],d=gcd(p,q),k=t+":"+p/d+"/"+q/d,j=keys.indexOf(k);if(j<0){j=keys.length;keys.push(k)}idx.push(j)}
ok(keys.length===12&&idx[3]===idx[5]&&idx[9]===idx[13],"keys");
for(let i=0;i<14;i++){let [t,p,q,pa]=S[i],children=S.filter(s=>s[3]===i);ok(p>0&&q>0,"mass");if(children.length)ok(children.length===2&&children.reduce((a,s)=>a+s[1],0)===p&&children.reduce((a,s)=>a+s[2],0)===q,"conserve");
for(let c of [0,1]){let pn=(20+5*t)*p+(t+1)*q,qn=(1200-100*t+3*(i===9||i===13?c:0))*q+15*(t+2)*p;ok(0<pn&&pn<100*p&&0<qn&&qn<3000*q,"errors");if(t===3){pn=40*p+5*q;qn=800*q+90*p;ok(0<pn&&pn<100*p&&0<qn&&qn<3000*q,"t4 errors")}}}
function image(m,lr){let alive=Array(14).fill(false),r=0,x=0,y=0;for(let i=0;i<14;i++){let [t,p,q,pa]=S[i],reach=pa<0||alive[pa],stop=reach&&!!(m&(1<<(lr?idx[i]:i)));alive[i]=reach&&!stop;if(stop){if(i===9||i===13)r+=q;x+=(4-t)*p;y+=(4-t)*q}}return [r,x,y]}
const L=Array.from({length:4096},(_,i)=>image(i,true)),H=Array.from({length:16384},(_,i)=>image(i,false)),key=v=>v.join(","),dot=(f,v)=>f[0]*v[0]+f[1]*v[1]+f[2]*v[2];
ok(new Set(L.map(key)).size===272&&new Set(H.map(key)).size===647,"corners");
const B=[[0,-1,0,0],[0,1,0,1080],[0,0,-1,0],[0,0,1,1080]],P=F.concat(B);
for(const f of P)for(const v of H)ok(dot(f,v)<=f[3],"hull containment");
const det=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]),bb=P.map(f=>f.map(BigInt)),V=new Map();let nonsing=0;
for(let i=0;i<28;i++)for(let j=i+1;j<28;j++)for(let k=j+1;k<28;k++){let [a,b,c]=[bb[i],bb[j],bb[k]],d=det(a.slice(0,3),b.slice(0,3),c.slice(0,3));if(d===0n)continue;nonsing++;
let X=det([a[3],a[1],a[2]],[b[3],b[1],b[2]],[c[3],c[1],c[2]]),Y=det([a[0],a[3],a[2]],[b[0],b[3],b[2]],[c[0],c[3],c[2]]),Z=det([a[0],a[1],a[3]],[b[0],b[1],b[3]],[c[0],c[1],c[3]]);if(d<0n){d=-d;X=-X;Y=-Y;Z=-Z}
if(bb.some(f=>f[0]*X+f[1]*Y+f[2]*Z>f[3]*d))continue;
ok(X%d===0n&&Y%d===0n&&Z%d===0n,"fractional vertices");let v=[Number(X/d),Number(Y/d),Number(Z/d)];V.set(key(v),v)}
ok(V.size===31&&nonsing===3075&&[...V.keys()].every(v=>new Set(L.map(key)).has(v)),"vertices");
for(const f of B)ok([...V.values()].filter(v=>dot(f,v)===f[3]).length===1,"box extra facet");
let count=[],sizes=[],inc=Array(24).fill(0),edges=0;
for(let i=0;i<24;i++){let f=F[i],E=new Set();for(let m=0;m<4096;m++)if(dot(f,L[m])===f[3])E.add(m);ok(E.has(C[i]),"center");
for(const m of E)for(let bit=0;bit<12;bit++)if((m^C[i])&(1<<bit))ok(E.has(m^(1<<bit)),"downset");let vv=[...V.values()].filter(v=>dot(f,v)===f[3]);ok(vv.length>=3,"facet vertices");
let rank2=false;for(let a=0;a<vv.length;a++)for(let b=a+1;b<vv.length;b++)for(let c=b+1;c<vv.length;c++){let u=vv[b].map((x,i)=>x-vv[a][i]),v=vv[c].map((x,i)=>x-vv[a][i]);if(u[1]*v[2]-u[2]*v[1]||u[2]*v[0]-u[0]*v[2]||u[0]*v[1]-u[1]*v[0])rank2=true}ok(rank2,"rank2 facet");count.push(E.size);sizes.push(vv.length)}
for(let i=0;i<24;i++)for(let j=0;j<i;j++){let f=F[i],g=F[j],ends=[...V.values()].filter(v=>dot(f,v)===f[3]&&dot(g,v)===g[3]);if(ends.length<2)continue;ok(ends.length===2,"edge endpoints");let E=new Set();for(let m=0;m<4096;m++)if(dot(f,L[m])===f[3]&&dot(g,L[m])===g[3])E.add(m);ok(ends.every(v=>[...E].some(m=>key(L[m])===key(v))),"edge vertices attained");
let unseen=new Set(E),queue=[unseen.values().next().value];unseen.delete(queue[0]);while(queue.length){let m=queue.pop();for(let b=0;b<12;b++){let z=m^(1<<b);if(unseen.delete(z))queue.push(z)}}ok(!unseen.size,"edge disconnect");edges++;inc[i]++;inc[j]++}
ok(edges===53&&inc.every((v,i)=>v===sizes[i])&&31-edges+24===2,"Euler and edges");
return ["EXACT_TREE nodes=14 LR_keys=12 P_and_Q_positive=True collision_pairs=2","TERMINAL_RATES eta=1/1000 equal_c=0_or_1 strict_validity=True","CORNERS full=16384 lr=4096 distinct_full=647 distinct_lr=272","POLYTOPE planes=28 intersections=3276 nonsingular=3075 vertices=31 facets=24 edges=53","FACET_DOWNSETS proved=24/24 optimizing_masks="+count.join(","),"EDGE_GRAPH connected=53/53","FACET_PERIMETERS "+inc.join(",")+" Euler=31-53+24=2","THEOREM (analytic face lifting): equal_a_b actual_FULL=actual_LR=entire_common_convex_hull","COMBINED_WITH_PREDECESSOR: actual_images_equal_if_and_only_if_a_equals_b","PASS_EXACT_R5_REAL_IMAGE_DEGREE_CLASSIFICATION"].join("\n")+"\n"})());
