#include <array>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
using X=array<int,7>;
const int q=5,u=2;
int bit(int p,int i){return i?((p>>(i-1))&1):0;}
int last(int p,int i){for(int d=1;d<=4;++d){int e=(i-d+4)%4;if(bit(p,e)!=bit(p,(e+1)%4))return e;}return -1;}
struct Cut{int mask,limit;};vector<Cut> cuts[4][4];
int adj[4][4]={};
void init(){for(int i=0;i<4;i++){for(int p=1;p<=7;p++)if(bit(p,i)!=bit(p,(i+1)%4))adj[i][last(p,i)]|=1<<(p-1);for(int j=i+1;j<4;j++){int best[128];for(int &v:best)v=9;for(int U=1;U<256;U++){int M=0;for(int p=1;p<=7;p++)if(bit(p,i)!=bit(p,j)){int e=(1<<last(p,i))|(1<<(4+last(p,j)));if((U&e)==e)M|=1<<(p-1);}if(M)best[M]=min(best[M],__builtin_popcount((unsigned)U));}for(int M=1;M<128;M++)if(best[M]<9)cuts[i][j].push_back({M,q*best[M]+2*u});}}}
int sum(const X&x,int mask){int s=0;while(mask){int p=__builtin_ctz((unsigned)mask);s+=x[p];mask&=mask-1;}return s;}
long long checked=0,ge=0,stable=0,nonheavy=0;X x{};
void test(){checked++;for(int i=0;i<4;i++){int S=0;for(int m:adj[i])S+=max(0,sum(x,m)-q);if(S<q+4*u+1)return;}ge++;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){bool ok=false;for(auto c:cuts[i][j])if(sum(x,c.mask)>c.limit){ok=true;break;}if(!ok)return;}stable++;int heavy=(x[2]>=2*q+2*u)+(x[4]>=2*q+2*u)+(x[5]>=2*q+2*u);nonheavy+=heavy<2;for(int v:x)cout<<v<<' ';cout<<'\n';}
void gen(int i,int rem){if(i==7){test();return;}for(int a=0;a<=rem;a++){x[i]=a;gen(i+1,rem-a);}}
int main(){init();gen(0,37);cerr<<checked<<' '<<ge<<' '<<stable<<' '<<nonheavy<<'\n';}
