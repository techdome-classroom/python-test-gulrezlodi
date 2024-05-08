from operator import indexOf


def decode_message( s: str, p: str) -> bool:
        
        if(len(s)!= len(p)):
             if(p[0]!="*" and p[0]!="?"):
                return False
             else:
                return True
        
        for i in s: 
          if (i==p[s.index(i)] or i== "*" or s== "?"):
                return True
  
        return False


 