// R284GI finite exact fixed-order decision at q=5,u=2, n<=37.
#include <array>
#include <algorithm>
#include <iostream>
#include <vector>
#include <functional>
#include <cassert>
using namespace std;
using Hist=array<int,8>;
const int q=5,u=2,N=37;
Hist x{};long long total=0,stable=0,adj=0,nh=0,passed=0,nodes=0,masks=0;int fail[4]={};
int bit(int p,int i){return i?((p>>(i-1))&1):0;}
int last(int p,int i){for(int d=1;d<=4;d++){int e=(i+4-d)%4;if(bit(p,e)!=bit(p,(e+1)%4))return e;}assert(false);return -1;}
bool diag(int a,int b){int y=x[3],z=x[6],s=x[a],t=x[b];return max({y,z,s,t})>=2*q+2*u+1||max(y,z)+max(s,t)>=3*q+2*u+1||y+z+s+t>=4*q+2*u+1;}
bool ge(int a,int b,int c,int d){return max(0,x[a]-q)+max(0,x[b]-q)+max(0,x[c]+x[d]-q)>=q+4*u+1;}
// Compress the exact 256-cut calculation into affine expressions in the four
// changing-pattern success counts. Drop only provably insufficient cuts.
struct Cut{int c;array<int,4>a;};
bool edge(int i){int t=(i+1)%4;vector<int> ch;for(int p=1;p<8;p++)if(bit(p,i)!=bit(p,t))ch.push_back(p);assert(ch.size()==4);
 array<int,4> ext{},a{},s{};int size=1;for(int k=0;k<4;k++){ext[k]=x[ch[k]];size*=ext[k]+1;}
 vector<Cut> cuts[2];int jj=0;
 for(int j=0;j<4;j++)if(j!=i&&j!=t){for(int m=0;m<256;m++){
  Cut c{};c.c=-q*__builtin_popcount((unsigned)m);
  for(int p=1;p<8;p++){
   int l=1<<last(p,i), r=1<<(4+last(p,j));
   bool unw=(bit(p,i)!=bit(p,j))&&((m&(l|r))==(l|r));
   bool wr=(bit(p,t)!=bit(p,j))&&((m&r)==r);
   c.c+=x[p]*int(unw);
   for(int k=0;k<4;k++)if(ch[k]==p)c.a[k]=int(wr)-int(unw);
  }
  int mx=c.c;for(int k=0;k<4;k++)mx+=max(0,c.a[k])*ext[k];if(mx>2*u)cuts[jj].push_back(c);
 }jj++;}
 auto index=[&](const array<int,4>&v){int z=0;for(int k=0;k<4;k++)z=z*(ext[k]+1)+v[k];return z;};
 vector<signed char> danger(size,-1),reach(size,0);reach[0]=1;
 auto bad=[&](){int z=index(s);if(danger[z]>=0)return bool(danger[z]);++masks;for(auto &cc:cuts){bool sep=false;for(auto &c:cc){int v=c.c;for(int k=0;k<4;k++)v+=c.a[k]*s[k];if(v>2*u){sep=true;break;}}if(!sep){danger[z]=1;return true;}}danger[z]=0;return false;};
 function<bool(int,int)> safe=[&](int k,int rem){if(k==4)return !bad();for(int d=0;d<=min(a[k],rem);d++){s[k]=a[k]-d;if(!safe(k+1,rem-d))return false;}return true;};
 // Mixed radix order is a topological ordering of increment edges.
 for(int z=0;z<size;z++){if(z){int v=z;for(int k=3;k>=0;k--){a[k]=v%(ext[k]+1);v/=ext[k]+1;}bool prev=false;for(int k=0;k<4;k++)if(a[k]){--a[k];prev|=reach[index(a)];++a[k];}if(!prev)continue;}++nodes;reach[z]=safe(0,q);}
 return bool(reach.back());
}
void visit(){++total;if(!diag(2,7)||!diag(1,4))return;++stable;if(!ge(1,3,5,7)||!ge(2,6,1,5)||!ge(4,3,2,5)||!ge(7,6,4,5))return;++adj;
 if((x[3]>=2*q+2*u)+(x[5]>=2*q+2*u)+(x[6]>=2*q+2*u)<2)++nh;
 for(int i=0;i<4;i++)if(!edge(i)){++fail[i];return;}
 ++passed;for(int p=1;p<8;p++)cout<<x[p]<<',';cout<<" PASSES ALL\n";
}
void rec(int p,int left){if(p==7){x[p]=left;visit();return;}for(int v=0;v<=left;v++){x[p]=v;rec(p+1,left-v);}}
int main(){for(int n=0;n<=N;n++)rec(1,n);cerr<<"hist="<<total<<" diagonals="<<stable<<" GE="<<adj<<" nonheavy="<<nh<<" pass="<<passed<<" fail=";for(int a:fail)cerr<<a<<',';cerr<<" nodes="<<nodes<<" unique_success_checks="<<masks<<'\n';}
