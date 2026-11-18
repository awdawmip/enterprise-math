/* EC49DJ independently executed exact native X6/BRC finite checker.
 * Run as an ECMAScript function body: new Function(source)().
 * Integer arithmetic uses BigInt; no floats or external libraries.
 */
const P=[1000003n,1000033n];
const opE=[3,1,1,-3];
const params=[
["constant",[2,2,2,2,2,2],2,1],
["equal_first",[2,2,5,2,2,2],2,1],
["equal_other",[2,2,2,3,4,5],3,2],
["different",[2,3,1,2,3,4],2,1],
["different_eq3a",[2,3,2,2,2,2],2,1],
["different_eq3b",[2,3,3,3,3,3],3,2],
["near_equal",[100,101,100,100,100,100],1,1]
];
const assert=(x,msg)=>{if(!x)throw Error(msg)};
function regime(x){return x.every(v=>v===x[0])?0:(x[0]===x[1]?1:2)}
function cores(t,m,x){
 const type=regime(x), a=t===2?1:2,b=t===2?2:1;
 const rep=(j,n)=>Array(n).fill(j);
 if(type===0){let c=({0:[],1:[2,1],2:[1,2],3:[1,2,1]})[t];return m<c.length?[]:[rep(3,m-c.length).concat(c)]}
 if(type===1){
  const q=x.findIndex((v,i)=>i>=2&&v!==x[0])+1;
  if(t===0){if(m===0)return [[]];if(m===1)return [[1],[q]];return [0,1,2].map(k=>rep(q,m-2).concat(rep(1,k),rep(q,2-k)))}
  if(t===1||t===2){if(m<2)return [];if(m===2)return [[a,b]];if(m===3)return [[a,a,b],[q,a,b]];
   return [0,1,2].map(k=>rep(q,m-4).concat(rep(a,k),rep(q,2-k),[a,b]))}
  if(m<3)return [];if(m===3)return [[1,2,1]];if(m===4)return [[1,1,2,1],[q,1,2,1]];
  return [0,1,2].map(k=>rep(q,m-5).concat(rep(1,k),rep(q,2-k),[1,2,1]))
 }
 const q=x[0]!==x[2]?1:2;
 if(t===0){if(m===0)return [[]];if(m===1)return [[1],[2]];return [0,1,2].map(k=>rep(3,m-2).concat(rep(q,k),rep(3,2-k)))}
 if(t===2){if(m<2)return [];if(m===2)return [[1,2]];if(m===3)return [[1,1,2],[1,2,2]];
  return [1,2,3].map(k=>rep(3,m-4).concat(rep(1,k),rep(2,4-k)))}
 if(t===1){if(m<2)return [];if(m===2)return [[2,1]];if(m===3)return [[2,2,1],[2,1,1]];
  return [1,2,3].map(k=>rep(3,m-4).concat(rep(2,4-k),rep(1,k)))}
 if(m<3)return [];if(m===3)return [[1,2,1],[2,1,2]];
 return [[2,1,2,2],[1,2,2,1],[1,1,2,1]].map(c=>rep(3,m-4).concat(c))
}
function complete(c,h){let counts=Array(6).fill(0);for(const j of c)counts[j-1]++;
 let w=c.slice();for(let j=1;j<=6;j++)w.push(...Array(counts[j-1]+(j===1?2*h:0)).fill(-j));
 const plen=w.length;for(let i=0;i<h;i++)w.push(...opE);
 assert(plen===2*h+2*c.length,"prefix length");let ep=Array(6).fill(0);
 for(const j of w)ep[Math.abs(j)-1]+=j>0?1:-1;
 assert(ep.every(z=>z===0),"endpoint");
 return w
}
function tag(w){let a=false,b=false;for(let i=0;i<w.length-1;i++){if(w[i]===1&&w[i+1]===2)a=true;if(w[i]===2&&w[i+1]===1)b=true}return (a?2:0)+(b?1:0)}
function row(w,x,y){let a=1n,b=1n;for(const j of w){if(j>0){a*=BigInt(x[j-1]);b*=BigInt(y[j-1])}}return [a,b,1n]}
function mod(a,p){let v=a%p;return v<0n?v+p:v}
function pow(a,e,p){let z=1n;for(a=mod(a,p);e>0n;e>>=1n,a=mod(a*a,p)){if(e&1n)z=mod(z*a,p)}return z}
function rank(rows,p){let b=rows.map(r=>r.map(v=>mod(v,p))),R=0;for(let j=0;j<3;j++){
 let k=R;while(k<b.length&&b[k][j]===0n)k++;if(k===b.length)continue;
 [b[R],b[k]]=[b[k],b[R]];let inv=pow(b[R][j],p-2n,p);for(let c=j;c<3;c++)b[R][c]=mod(b[R][c]*inv,p);
 for(let i=0;i<b.length;i++)if(i!==R){let t=b[i][j];for(let c=j;c<3;c++)b[i][c]=mod(b[i][c]-t*b[R][c],p)}
 R++;if(R===3)break
 }return R}
function det(b){return b[0][0]*(b[1][1]*b[2][2]-b[1][2]*b[2][1])-b[0][1]*(b[1][0]*b[2][2]-b[1][2]*b[2][0])+b[0][2]*(b[1][0]*b[2][1]-b[1][1]*b[2][0])}
const expect=[[1,1,3,4,4,4],[1,2,5,8,11,12],[1,2,5,9,12,12]];
let rankChecks=0,nonzeroChecks=0,pathCount=0,formulaChecks=0;
for(const [name,x,a,b] of params){
 const y=x.map(z=>a*z+b),type=regime(x),hMax=30,mMax=6;
 const pairs=type===0?[]:type===1?[[x[0],x.find((v,i)=>i>=2&&v!==x[0])]]:[[x[0],x[1]],[x[0]!==x[2]?x[0]:x[1],x[2]]];
 for(const [un,vn] of pairs){let u=BigInt(un),v=BigInt(vn),A=BigInt(a),B=BigInt(b),U=A*u+B,V=A*v+B;
  assert(u!==v,"distinct pair");
  for(const start of [0,1]){let M=[start,start+1,start+2].map(k=>[u**BigInt(k)*v**BigInt(4-k),U**BigInt(k)*V**BigInt(4-k),1n]);
   let exact=det(M),f=-A*B*(u-v)**3n*(start===0?v**2n*V**2n:u*v*U*V);
   assert(exact===f&&f!==0n,"symbolic substitution "+name);formulaChecks++
  }
 }
 for(let h=1;h<=hMax;h++)for(let m=0;m<=mMax;m++){
  let total=0;
  for(const t of [0,1,2,3]){
   let rows=[];
   for(const c of cores(t,m,x)){let w=complete(c,h);assert(tag(w)===t,"tag "+name+" "+t);rows.push(row(w,x,y));pathCount++}
   total+=rows.length;
   for(const p of P){let r=rank(rows,p);assert(r===rows.length,"rank "+name+" "+h+" "+m+" "+t+" "+p);rankChecks++;
    if(r===3){assert(mod(det(rows),p)!==0n,"minor "+name);nonzeroChecks++}
   }
  }
  assert(total===expect[type][Math.min(m,5)],"phase "+name+" "+h+" "+m);
 }
}
return {status:"PASS",parameters:params.map(z=>z[0]),h:[1,30],m:[0,6],moduli:P.map(String),rankChecks,nonzeroChecks,pathCount,formulaChecks,
 exact_phase_diagram:expect,
 note:"Exact native X6 paths, full A/B seam labels and positive integer BRC only; finite checker is separate from all-h analytic proof."};
