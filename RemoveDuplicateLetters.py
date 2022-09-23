class Solution(object):
    
    #Main funtion
    def removeDuplicateLetters(self, s):
      List=self.stringToList(self, s)
      List.sort()
      return self.removeDupsListSorted(self,List)
    
    #convert string to list function
    def stringToList(self,str):
      temp=[]
      for x in str:
        temp.append(x)
      return temp
    
    #convert List to String
    def ListToString(self,List):
      return ''.join(List)
    
    #Remove duplicates from the Lists
    def removeDupsListSorted(self,List):
      res_index=1
      ip_index=1
      
      #Remove duplicates
      #res_index=3
      #ip_index=4
      #[abbccdef]
      while ip_index!=len(List):
        if List[ip_index]!=List[ip_index-1]:
          List[res_index]=List[ip_index]
          res_index+=1
        ip_index+=1
      
      #After removing convert the List to String from 0-res_index
      newString=self.ListToString(self,List[0:res_index])
      
      return newString

test_data="dsauvewnvoiasdfeofvoirfiojaresadoijforijouforia"
print(Solution.removeDuplicateLetters(Solution,test_data))