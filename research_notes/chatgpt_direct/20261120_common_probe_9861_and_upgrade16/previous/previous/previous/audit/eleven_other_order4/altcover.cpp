#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
using U=uint64_t;struct Row{U q;int r,c,s;};std::vector<Row>v;std::vector<int>by[45],path;U once,twice,full;int best=11292;int dp[12][126][6][11][3];struct Type{int r,s,a,b,c;};int pc(U q){return __builtin_popcountll(q);}int w(U q){return pc(q)*4-3*pc(q&once)-2*pc(q&twice);}long long nodes;std::vector<std::unordered_map<U,int>>memo(36);
void search(U free,int k,int th,int paid){++nodes;int n=w(free),a=pc(free&once),b=pc(free&twice);if(paid+dp[k][n][a][b][th]>=best)return;if(!free){if(!k){best=paid;std::cout<<"hit "<<best;for(int i:path)std::cout<<' '<<v[i].q<<':'<<v[i].r;std::cout<<std::endl;}return;}if(!k)return;auto &d=memo[3*k+th];auto it=d.find(free);if(it!=d.end()&&it->second<=paid)return;if(d.size()<200000)d[free]=paid;
 int rare=-1,few=100000000;std::vector<int>opts;
 // Try fixed-point columns early. All such columns must use a length-one label.
 U active=free&once;if(!active)active=(free&twice)?free&twice:free;
 for(U z=active;z;z&=z-1){int p=__builtin_ctzll(z);std::vector<int>x;for(int i:by[p]){auto &r=v[i];if(r.r>k||r.q&~free)continue;int t=th-(r.s==13?r.r:0);if(t<0)continue;int aa=pc(r.q&once),bb=pc(r.q&twice);if(paid+r.c+dp[k-r.r][n-r.s*r.r][a-aa][b-bb][t]>=best)continue;x.push_back(i);if(x.size()>=few)break;}if(x.size()<few){rare=p;few=x.size();opts.swap(x);if(!few)return;}}
 for(int i:opts){auto &r=v[i];path.push_back(i);search(free^r.q,k-r.r,th-(r.s==13?r.r:0),paid+r.c);path.pop_back();}}
int main(int argc,char**argv){std::ifstream g(argv[1]);int map[125];for(int&x:map)g>>x;bool h[125]{};int norb=0;
 for(int i=0;i<125;i++)if(!h[i]){int j=i,s=0;do{h[j]=true;j=map[j];s++;}while(j!=i);U b=U(1)<<norb++;if(s==1)once|=b;if(s==2)twice|=b;}full=(U(1)<<norb)-1;std::vector<Type>types;int cap[5][14][6][11];for(auto&a:cap)for(auto&b:a)for(auto&c:b)for(auto&v:c)v=1000000;
 for(int j=0;j<3;j++){std::ifstream f(argv[2+j]);U q,lo,hi;int unit,s;int r=(1<<j);while(f>>q>>unit){if(j==0)f>>s;else{f>>lo>>hi;s=w(q)/r;}
 int a=pc(q&once),b=pc(q&twice);int &mc=cap[r][s][a][b];mc=std::min(mc,unit*r);v.push_back({q,r,unit*r,s});}}
 for(int r:{1,2,4})for(int s=1;s<=13;s++)for(int a=0;a<=5;a++)for(int b=0;b<=10;b++)if(cap[r][s][a][b]<1000000)types.push_back({r,s,a,b,cap[r][s][a][b]});
 std::sort(v.begin(),v.end(),[](auto&a,auto&b){return a.c-186*a.s*a.r<b.c-186*b.s*b.r;});for(int j=0;j<(int)v.size();j++)for(U q=v[j].q;q;q&=q-1)by[__builtin_ctzll(q)].push_back(j);
 for(auto&aa:dp)for(auto&bb:aa)for(auto&cc:bb)for(auto&dd:cc)for(int&v:dd)v=1000000;for(int t=0;t<3;t++)dp[0][0][0][0][t]=0;
 for(int k=1;k<=11;k++)for(int n=1;n<=125;n++)for(int a=0;a<=pc(once);a++)for(int b=0;b<=pc(twice);b++)for(int t=0;t<=2;t++)for(auto z:types){int e=(z.s==13?z.r:0);if(z.r<=k&&z.s*z.r<=n&&z.a<=a&&z.b<=b&&e<=t)dp[k][n][a][b][t]=std::min(dp[k][n][a][b][t],dp[k-z.r][n-z.s*z.r][a-z.a][b-z.b][t-e]+z.c);}
 search(full,11,2,0);std::cerr<<nodes<<' '<<best<<'\n';}
