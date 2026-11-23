// EC49FYI: exact search and raw-state replay; run node EC49FYI_DEPTH14_VERIFY.js
function exactDepth14(){
 const F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005];
 const check=(p,msg)=>{if(!p)throw Error(msg)};
 const bit=i=>1n<<BigInt(i), ALL=bit(50)-1n, cmp=(a,b)=>a<b?-1:a>b?1:0;
 function pc32(x){x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24}
 const pc=x=>pc32(Number(x&0xffffffffn))+pc32(Number(x>>32n));
 const mask=p=>F.reduce((v,u,i)=>p(u,i)?v|bit(i):v,0n);
 const row=Array.from({length:10},(_,t)=>mask(u=>u>>t&1));
 const sup=F.map(u=>mask(v=>u!==v&&(u&v)===u));
 const neg=F.map(u=>{const out=Array.from({length:11},()=>[]);for(let m=0;m<1024;m++)if(!(m&u))out[pc(BigInt(m))].push(mask(v=>m&v));return out});
 const canon=(a,h)=>[a,...h.slice().sort(cmp)];
 const count=s=>s.reduce((n,v)=>n+pc(v),0);
 function child(s,t,j,b){const g=b?row[t]:ALL^row[t];return canon(s[0]&g,s.slice(1).map((h,k)=>k===j?(b?0n:h):h&g))}
 function lower(s,n,d){let l=0;while(2**l<n)l++;if(l>d)return l;for(let i=0;i<50;i++)if(s[0]&bit(i)){let p=0;for(let j=1;j<12;j++)if(s[j]&bit(i))p++;const target=s[0]&sup[i];let q=0;while(q<=d-p&&q<=10&&!neg[i][q].some(v=>(v&target)===target))q++;l=Math.max(l,p+q);if(l>d)return l}return l}
 const memo=new Map();let calls=0,lowerRejects=0,childRejects=0;
 function solve(s,d){
   calls++;const n=count(s);if(n<=1)return true;if(d<=0||n>2**d)return false;
   const k=s.join(','),v=memo.get(k)||{lo:0,hi:99};
   if(v.lo>d)return false;if(v.hi<=d)return true;
   const l=lower(s,n,d);if(l>d){lowerRejects++;v.lo=Math.max(v.lo,l);memo.set(k,v);return false}
   const opts=[];
   for(let j=0;j<11;j++){if(j&&s[j+1]===s[j])continue;for(let t=0;t<10;t++){let n1=pc(s[0]&row[t]);for(let z=0;z<11;z++)if(z!==j)n1+=pc(s[z+1]&row[t]);let n0=n-n1;if(n0&&n1&&Math.max(n0,n1)<=2**(d-1))opts.push([Math.max(n0,n1),t,j,n0,n1])}}
   opts.sort((x,y)=>x[0]-y[0]||x[1]-y[1]||x[2]-y[2]);
   for(const [,t,j,n0,n1] of opts){let a=child(s,t,j,0),b=child(s,t,j,1);if(lower(a,n0,d-1)>d-1||lower(b,n1,d-1)>d-1){childRejects++;continue}if(n0<n1)[a,b]=[b,a];if(solve(a,d-1)&&solve(b,d-1)){v.hi=d;v.t=t;v.j=j;memo.set(k,v);return true}}
   v.lo=Math.max(v.lo,d+1);memo.set(k,v);return false
 }
 const root=Array(12).fill(ALL);
 check(solve(child(root,0,0,0),13)&&solve(child(root,0,0,1),13),'root row 0 search failed');
 // Construct a tree on original labeled candidates; canonical keys are recomputed from physical states.
 const states=F.flatMap((u,i)=>Array.from({length:12},(_,z)=>({id:12*i+z,u,i,z:z-1})));
 const read=(s,t,j)=>Number(Boolean((s.u>>t&1)&&s.z!==j));
 function residual(ss){let a=0n,h=Array(11).fill(0n);for(const s of ss){if(s.z<0)a|=bit(s.i);else h[s.z]|=bit(s.i)}const perm=Array.from({length:11},(_,j)=>j).sort((i,j)=>cmp(h[i],h[j])||i-j);return {key:canon(a,h),perm}}
 function build(ss,d,first=false){
   if(ss.length===1)return -1-ss[0].id;
   check(d>0,'tree exceeds depth');
   let t,j;
   if(first){t=0;j=0}else{const {key,perm}=residual(ss);check(solve(key,d),'missing subtree');const v=memo.get(key.join(','));check(v&&v.hi<=d,'missing decision');t=v.t;j=perm[v.j]}
   const a=ss.filter(s=>read(s,t,j)===0),b=ss.filter(s=>read(s,t,j)===1);check(a.length&&b.length,'degenerate node');
   return [11*t+j,build(a,d-1),build(b,d-1)]
 }
 const tree=build(states,14,true);
 // Independent replay on raw state labels, without residual keys, memo or search bounds.
 const histogram={},leaves=new Set();let maxDepth=0,sumDepth=0,internalNodes=0;
 function audit(node){if(typeof node==='number'){check(node<0,'invalid leaf');return}check(node.length===3&&node[0]>=0&&node[0]<110,'invalid query');internalNodes++;audit(node[1]);audit(node[2])}
 audit(tree);
 for(const s of states){let node=tree,d=0;while(Array.isArray(node)){const t=Math.floor(node[0]/11),j=node[0]%11;node=node[1+read(s,t,j)];d++}check(node===-1-s.id,'wrong leaf');check(d<=14,'depth overflow');leaves.add(node);histogram[d]=(histogram[d]||0)+1;maxDepth=Math.max(maxDepth,d);sumDepth+=d}
 check(leaves.size===600&&internalNodes===599&&maxDepth===14,'coverage failure');
 const U=833,V=[857,867,965];check(F.includes(U)&&V.every(v=>F.includes(v)&&(v&U)===U),'lower witness membership');const differences=V.map(v=>v^U);check(differences.every(x=>x!==0)&&!(differences[0]&differences[1])&&!(differences[0]&differences[2])&&!(differences[1]&differences[2]),'lower witness disjointness');
 return {schema:"EC49FYI_DEPTH14_CERTIFICATE_V1",science_pin:"BRC16943",frozen_parent:"EC49FYH@95214d3f9548b0df6a18e745c70b3e2076e7515e",F,root_query:[0,0],root_split:[states.filter(s=>!read(s,0,0)).length,states.filter(s=>read(s,0,0)).length],states:600,internalNodes,leaves:leaves.size,maxDepth,sumDepth,histogram,calls,memoStates:memo.size,lowerRejects,childRejects,lowerWitness:{U,V,differences},tree};
}
console.log(JSON.stringify(exactDepth14(),null,2));
