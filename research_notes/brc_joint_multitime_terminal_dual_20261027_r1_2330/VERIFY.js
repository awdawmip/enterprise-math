/* Run: node VERIFY.js. BigInt rational certificate; no floating point. */
function verify() {
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t}return a};
 const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}if(!b)throw Error("zero denominator");let g=gcd(a,b);return [a/g,b/g]};
 const add=(x,y)=>f(x[0]*y[1]+y[0]*x[1],x[1]*y[1]),neg=x=>f(-x[0],x[1]),sub=(x,y)=>add(x,neg(y));
 const mul=(x,y)=>f(x[0]*y[0],x[1]*y[1]),div=(x,y)=>f(x[0]*y[1],x[1]*y[0]);
 const cmp=(x,y)=>{let v=x[0]*y[1]-y[0]*x[1];return v>0n?1:v<0n?-1:0},max=(...a)=>a.reduce((x,y)=>cmp(x,y)>=0?x:y);
 const min=(x,y)=>cmp(x,y)<=0?x:y,abs=x=>cmp(x,f(0))<0?neg(x):x,eq=(x,y)=>cmp(x,y)===0,show=x=>x[0]+"/"+x[1];
 const z=f(0),one=f(1),r=[f(1,2),f(1),f(3,2),f(2)],n=[f(3,40),f(3,40),f(3,40),f(3,40)];
 const m=[[4,1,4,3].map(x=>f(x,40)),[3,4,1,4].map(x=>f(x,40))],ds=m.map(row=>row.map((x,i)=>sub(x,n[i])));
 const sum=a=>a.reduce(add,z),assert=(v,msg)=>{if(!v)throw Error(msg)};
 const dot=(a,b)=>sum(a.map((x,i)=>mul(x,b[i]))),mom=a=>[sum(a),dot(a,r)];
 for(let i=0;i<2;i++){assert(n.every(x=>cmp(x,z)>0)&&m[i].every(x=>cmp(x,z)>0),"positivity");assert(eq(mom(m[i])[0],f(3,10))&&eq(mom(m[i])[1],f(3,8)),"moments");assert(eq(mom(ds[i])[0],z)&&eq(mom(ds[i])[1],z),"mass conservation")}
 assert(eq(add(f(2,5),add(f(3,10),f(3,10))),one)&&eq(add(f(1,4),add(f(3,8),f(3,8))),one),"normalization");
 const call=(d,t)=>sum(d.map((x,i)=>mul(x,max(sub(r[i],t),z))));
 const h=(d,a)=>{let b=sub(one,a);if(eq(b,z))return z;let v=[z,mul(b,call(d,div(a,b)))];for(let t of r)v.push(mul(call(d,t),min(b,div(a,t))));return max(...v)};
 const h2=(d,a)=>{let b=sub(one,a),pts=[[z,z],[a,b]];for(let t of r){if(cmp(mul(b,t),a)<=0)pts.push([mul(b,t),b]);if(cmp(a,mul(b,t))<=0)pts.push([a,div(a,t)])}return max(...pts.map(([x,y])=>sum(d.map((di,i)=>mul(di,max(sub(mul(y,r[i]),x),z))))))};
 const local=ds.map(d=>max(z,...r.map(x=>div(call(d,x),add(one,x)))));
 assert(eq(local[0],f(1,160))&&eq(local[1],f(1,200)),"local deficits");
 const as=[z,...r.map(x=>div(x,add(one,x))),one],rows=as.map(a=>{let p=ds.map(d=>h(d,a));assert(p.every((x,i)=>eq(x,h2(ds[i],a))),"independent support");return {a:show(a),t3:show(p[0]),t4:show(p[1]),joint:show(sum(p))}});
 const joint=max(...as.map(a=>sum(ds.map(d=>h(d,a)))));assert(eq(joint,f(1,96)),"joint value");
 assert(eq(sub(sum(local),joint),f(1,1200)),"strict deficit");
 const oldX=[[z,z,one,one],[z,z,z,one]],newX=[[z,f(13,36),one,one],[z,z,f(4,9),one]];
 const obs=(mass,dec)=>[dot(mass,dec),dot(mass,dec.map((x,i)=>mul(x,r[i])))];
 const oldObs=m.map((mass,i)=>obs(mass,oldX[i])),newObs=[obs(n,newX[0]),obs(n,newX[1])];
 const tvq=sum(oldObs.map((x,i)=>abs(sub(x[0],newObs[i][0])))),tvp=sum(oldObs.map((x,i)=>abs(sub(x[1],newObs[i][1]))));
 assert(eq(tvq,joint)&&eq(tvp,joint),"primal P/Q witness");
 const normals=[[neg(f(1,2)),f(1,2)],[neg(f(1,2)),f(1,3)]];
 const dn=add(max(...normals.map(x=>abs(x[0]))),max(...normals.map(x=>abs(x[1]))));
 const lower=sum(ds.map((d,i)=>sum(d.map((v,j)=>mul(v,max(add(normals[i][0],mul(normals[i][1],r[j])),z))))));
 assert(eq(dn,one)&&eq(lower,joint),"dual certificate");
 return {status:"PASS_EXACT_BIGINT_FRACTION_MULTITIME",domain:"two time slices with four positive LR leaves, plus one t2 stop leaf",local_deficits:local.map(show),sum_local:show(sum(local)),joint:show(joint),strict_gap:show(sub(sum(local),joint)),rows,old_observations:oldObs.map(x=>x.map(show)),new_observations:newObs.map(x=>x.map(show)),TV_Q:show(tvq),TV_P:show(tvp),dual_norm:show(dn),dual_lower_bound:show(lower),verification:"exact BigInt two-route rectangle support; exact normalization, fractions and witness",scope:"fixed exogenous arrival masses; no adapted N4 minimax"};
}
if(typeof process!=="undefined"&&typeof console!=="undefined")console.log(JSON.stringify(verify(),null,2));
