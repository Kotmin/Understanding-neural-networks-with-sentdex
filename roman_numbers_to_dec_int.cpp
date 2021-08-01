#include<string>
#include<iostream>

int val(char s);
int romanToInt(std::string s) {   
    int sol=0;
    int len = s.length();
    
    if(len == 0)
        return 0;
    if(len ==1)
        return val(s[0]);
    sol=val(s[len-1]);
    for(int i=len;i>=2;i--)
    {
        int act = val(s[i-1]);
        int prev = val(s[i-2]);
            
        if(act>prev)
        {
           sol=sol-prev;  
         }
         if(act<=prev)
        {
            sol=sol+prev; 
        }
        
        
        
    }
    
    return sol;
    
    }
    
int val(char s)
    {
    if(s=='M')
        return 1000;
    if(s=='D')
        return 500;
    if(s=='C')
        return 100;
    if(s=='L')
        return 50;
    if(s=='X')
        return 10;
    if(s=='V')
        return 5;
    if(s=='I')
        return 1;
    return 0;    
}


main()
{
    std::string input="MCMXCIV";
    std::cout<<"Works\n";
    //std::cout<<val('D');
    std::cout<<romanToInt(input);
    return 0;
}