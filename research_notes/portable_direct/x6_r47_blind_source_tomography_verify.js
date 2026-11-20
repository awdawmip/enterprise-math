/* X6 R47 finite exact root BRC audit, mirroring the published R44 transition grammar. */
function next(s,p){const [a,b,o,t]=s,edges=[];
  if(o!==0)edges.push(['R',[a,b,0,t],1]);
  if(t===0&&o===0&&((a<0)!==(b<0))){const used=a>=0?a:b;edges.push(['T',[a,b,used===0?(a>=0?1:2):0,1],1]);}
  if(a<0)for(let i=0;i<p;i++)if(i!==0||o===0)edges.push(['F',[i,b,i===0?1:o,t],'a']);
  if(b<0)for(let i=0;i<p;i++)if(i!==0||o===0)edges.push(['F',[a,i,i===0?2:o,t],'b']);
  return edges;
}
function coeff(word,p,a,b){let q=new Map([['-1,-1,0,0',1]]);
  for(const symbol of word){const out=new Map();for(const [key,mass] of q){
    const s=key.split(',').map(Number);for(const [e,d,w] of next(s,p)){if(e!==symbol)continue;
      const k=d.join(',');out.set(k,(out.get(k)||0)+mass*(w==='a'?a:w==='b'?b:1));}}q=out;}
  return [...q.values()].reduce((x,y)=>x+y,0);
}
const samples=[[1,1],[1,2],[2,3],[3,5],[7,11]],rows=[];
for(let p=1;p<=30;p++)for(const [a,b] of samples){
  const F=coeff('F',p,a,b),FT=coeff('FT',p,a,b),FF=coeff('FF',p,a,b),FRF=coeff('FRF',p,a,b);
  if(F!==p*(a+b)||FT!==(p-1)*(a+b)||FF!==2*(p*p-1)*a*b||FRF!==2*p*a*b)
    throw Error('coefficient mismatch: '+[p,a,b]);
  if(F/(F-FT)!==p || FF*p!==FRF*(p*p-1))throw Error('reconstruction mismatch');
  rows.push([p,a,b,F,FT,FF,FRF]);
}
const wordsTo=(depth)=>{const out=[''];for(let k=1;k<=depth;k++)for(let i=0;i<3**k;i++){
  let x=i,w='';for(let j=0;j<k;j++){w='FRT'[x%3]+w;x=Math.floor(x/3);}out.push(w);
}return out;};
for(const w of wordsTo(2))if(coeff(w,1,1,3)!==coeff(w,1,2,2))throw Error('p=1 sharp horizon');
if(coeff('FRF',1,1,3)!==6||coeff('FRF',1,2,2)!==8)throw Error('p=1 depth-3 witness');
process.stdout.write(JSON.stringify({schema:'X6_R47_ROOT_OBSERVER_CHECK_V1',status:'PASS',
cases:rows.length,p_range:[1,30],weight_pairs:samples,sharp_depth_3_p1:true,
example_p3_a1_b2:rows.find(r=>r[0]===3&&r[1]===1&&r[2]===2)},null,2)+'\n');
