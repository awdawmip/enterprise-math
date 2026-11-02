(function runPrefix454Certificate(){
  const lines=[];
  const check=(cond,msg)=>{if(!cond)throw Error("FAIL "+msg)};
  const mono=(a,x)=>a.reduce((v,e,i)=>v*(x[i]**e),1);
  function indices(dim,degree){
    const out=[];function visit(a){if(a.length===dim){if(a.reduce((s,x)=>s+x,0)<=degree)out.push(a);return}for(let j=0;j<=degree;j++)visit([...a,j])}
    visit([]);return out;
  }
  const cubic=indices(6,3),quad=cubic.filter(a=>a.reduce((s,x)=>s+x,0)<=2);
  const Y=indices(5,3).filter(a=>!(a.reduce((s,x)=>s+x,0)===3&&(a.includes(3)||a.filter(v=>v>0).length===3)));
  check(cubic.length===84&&quad.length===28&&Y.length===41,"basis counts");
  const yIndex=new Map(Y.map((a,i)=>[a.join(","),i]));
  const bval=(j,z,y)=>j<41?mono(Y[j],y):j<46?z*y[j-41]:j<51?z*y[j-46]**2:z*(z-1);
  function support(q,N){
    let state=new Map([["0|0,0,0,0,0,0",1]]);
    for(let t=0;t<N;t++){
      const nxt=new Map();
      for(const [key,mass] of state){
        const [r0,coords]=key.split("|"),r=Number(r0),x=coords.split(",").map(Number);
        for(let axis=0;axis<6;axis++)for(const s of [-1,1]){
          const y=x.slice();y[axis]+=s;const rr=(r+(axis===0&&s===-1?1:0))%q;
          const k=rr+"|"+y.join(",");nxt.set(k,(nxt.get(k)||0)+mass);
        }
      }state=nxt;
    }
    const bins=[...state].map(([k,w])=>{const [r,x]=k.split("|");return {r:Number(r),x:x.split(",").map(Number),w}});
    check(bins.reduce((s,b)=>s+b.w,0)===12**N,"total ordered paths q"+q);
    return bins;
  }
  const P=1000003,mod=v=>(v%P+P)%P;
  function inv(a){let t=0,nt=1,r=P,nr=a;while(nr!==0){const q=Math.floor(r/nr);[t,nt]=[nt,t-q*nt];[r,nr]=[nr,r-q*nr]}check(r===1,"modular inverse");return mod(t)}
  function rank(rowFns,points){
    const piv=[];
    for(const f of rowFns){
      let v=points.map(pt=>mod(f(pt)));
      for(const [j,u] of piv)if(v[j]!==0){
        const k=v[j];for(let i=0;i<v.length;i++)v[i]=mod(v[i]-k*u[i]);
      }
      const col=v.findIndex(x=>x!==0);
      if(col>=0){const a=inv(v[col]);for(let i=0;i<v.length;i++)v[i]=mod(v[i]*a);piv.push([col,v]);piv.sort((x,y)=>x[0]-y[0])}
    }
    return piv.length;
  }
  function decodeDoubled(a,q){
    const c=-(q-1),ay=a.slice(1),factor=c**a[0],B=Array(41).fill(0);
    const degree=ay.reduce((s,z)=>s+z,0);
    if(degree===3&&ay.includes(3)){
      const i=ay.indexOf(3),unit=Array(5).fill(0);unit[i]=1;
      B[yIndex.get(unit.join(","))]+=4*factor;
      for(let j=0;j<5;j++)if(j!==i){const m=Array(5).fill(0);m[i]=1;m[j]=2;B[yIndex.get(m.join(","))]-=3*factor}
    }else if(!(degree===3&&ay.filter(z=>z>0).length===3)){
      B[yIndex.get(ay.join(","))]+=factor;
    }
    const base=y=>B.reduce((s,w,j)=>s+w*mono(Y[j],y),0),out=B.map(v=>2*v);
    for(let i=0;i<5;i++){
      const yp=Array(5).fill(0),ym=Array(5).fill(0);yp[i]=1;ym[i]=-1;
      const rp=(c+1)**a[0]*mono(ay,yp)-base(yp);
      const rm=(c+1)**a[0]*mono(ay,ym)-base(ym);
      out.push(rp-rm);
      // delayed quadratic coefficients placed after all linear coefficients
    }
    for(let i=0;i<5;i++){
      const yp=Array(5).fill(0),ym=Array(5).fill(0);yp[i]=1;ym[i]=-1;
      const rp=(c+1)**a[0]*mono(ay,yp)-base(yp);
      const rm=(c+1)**a[0]*mono(ay,ym)-base(ym);
      out.push(rp+rm);
    }
    const z2=Array(5).fill(0),res=(c+2)**a[0]*mono(ay,z2)-base(z2);
    out.push(res);
    check(out.length===52,"decoder dimension");
    return out;
  }
  function encodeBytes(bins,q,N,codec){
    const sorted=bins.slice().sort((a,b)=>a.r-b.r||a.x.findIndex((v,i)=>v!==b.x[i])<0?-1:0);
    // Use a stable numeric lexicographic comparator to match Python's tuple order.
    sorted.sort((a,b)=>{if(a.r!==b.r)return a.r-b.r;for(let i=0;i<6;i++)if(a.x[i]!==b.x[i])return a.x[i]-b.x[i];return 0});
    let data;
    if(codec==="HIST")data=sorted.map(b=>[b.r,b.x,b.w,1]);
    else{
      data=[];
      for(let r=0;r<q;r++){
        const cells=bins.filter(b=>b.r===r),last=r===q-1&&codec==="SLIM3";
        const fns=last?Array.from({length:52},(_,i)=>x=>bval(i,x[0]+q-1,x.slice(1))):
          (codec==="M2"?quad:cubic).map(a=>x=>mono(a,x));
        data.push([r,fns.map(f=>[cells.reduce((s,b)=>s+b.w*f(b.x),0),1])]);
      }
    }
    return JSON.stringify({N,codec,data,q}).length;
  }
  for(const q of [3,4]){
    const N=q+1,bins=support(q,N),groups=Array.from({length:q},(_,r)=>bins.filter(b=>b.r===r).map(b=>b.x));
    const r2=groups.map(g=>rank(quad.map(a=>x=>mono(a,x)),g));
    const r3=groups.map(g=>rank(cubic.map(a=>x=>mono(a,x)),g));
    check(r2.every(n=>n===28),"quadratic rank "+q);
    check(r3.every((v,i)=>v===(i===q-1?52:84)),"cubic rank "+q);
    check(groups[q-1].length===62,"last support 62");
    for(const a of cubic){
      const coef=decodeDoubled(a,q);
      for(const x of groups[q-1]){
        const z=x[0]+q-1,y=x.slice(1);
        const reconstructed=coef.reduce((s,v,j)=>s+v*bval(j,z,y),0);
        check(reconstructed===2*mono(a,x),"exact integer decoder "+q);
      }
    }
    lines.push("SHARP_CUBIC_RANK q="+q+" N="+N+" bins="+bins.length+" quadratic="+r2.join(",")+" cubic="+r3.join(",")+" decoder=PASS");
    if(q===3){
      const A=[[-2,-2,0,0,0,0,1],[-2,1,0,0,0,-1,4],[-2,1,0,0,0,1,4]];
      const B=[[-2,0,0,0,0,-2,1],[-2,0,0,0,0,0,4],[-2,0,0,0,0,2,1],[-2,2,0,0,0,0,3]];
      const moment=(source,a)=>source.reduce((v,point)=>v+point[6]*mono(a,point.slice(0,6)),0);
      check(quad.every(a=>moment(A,a)===moment(B,a)),"nine-path quadratic");
      check(moment(A,[0,3,0,0,0,0])===0&&moment(B,[0,3,0,0,0,0])===24,"nine-path cubic");
      lines.push("NINE_PATH_CUBIC_WITNESS quadratic_equal=PASS cubic_values=0,24");
      for(const [typ,src] of [["dense",bins],["one",[bins[0]]]]){
        const enc={};for(const c of ["HIST","M2","M3","SLIM3"])enc[c]=encodeBytes(src,q,N,c);
        if(typ==="dense")check(enc.HIST===25739&&enc.M2===631&&enc.M3===1700&&enc.SLIM3===1491,"dense JSON parity with Python");
        lines.push("BYTES "+typ+" "+JSON.stringify(enc));
      }
    }
  }
  lines.push("SUCCESS scope=q=3,4,N=q+1; exact integer arithmetic and finite modular rank p=1000003");
  return lines;
})().forEach(s=>console.log(s));
