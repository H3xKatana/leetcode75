int* twoSum(int* nums, int numsSize, int target, int* returnSize){
*returnSize = 2;   
int *solu=malloc((*returnSize)*sizeof(int));
   
 for (int i = 0; i < numsSize-1; i++)
 {
    for (int g= i+1; g < numsSize ; g++)
    {
        
        if ( nums[i]+nums[g] == target)
        {
         
             solu[0]=i;
            solu[1]=g;
             break;
        }
        
    }
    
 }
    
    
    return solu;
}