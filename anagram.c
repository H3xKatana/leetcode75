#include <stdbool.h>

bool isAnagram(char * s, char * t){
    
    if (strlen(s) != strlen(t))
    {
        return false;
    }

int table1[26]={0};
int table2[26]={0};
for (int i = 0; i < strlen(s); i++)
{
table1[s[i]-'a']++;//tablea[s[i]-97]
table2[t[i]-'a']++;
}
for (int i = 0; i < 25; i++)
{
    if (table1[i] != table2[i])
    {
        return false;
    }
    
}
return true ;

  
}
