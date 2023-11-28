#!/usr/bin/env python
# coding: utf-8

# In[1]:


##module1.py로 저장!
def calc(*para):
    result = [] ##결과값들은 리스트로 저장
    res1 = 0
    res2 = para[0]
    res3 = 1  ##곱셈을 하니까!
    
    for num in para:
        res1 +=num
        res3 *=num
        
    for num in range(1,len(para)):
        res2 -=para[num]
        
    
    result.append(res1)    ##result[0]
    result.append(res2)    ##result[1]
    result.append(res3)    ##result[2]
    
    #print("덧셈의 결과는 %d"%result[0])
    #print("뺼셈의 결과는 %d"%result[1])
    #>> 이렇게 말고!!
    
    return result


# In[ ]:




