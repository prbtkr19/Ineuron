class dict_parsing:
    def __init__(self,d):
        self.d = d
        
    def getkeys(self):
        if type(self.d) == dict:
            #print(self.d.keys())
            return list(self.d.keys())
            
    def getvalues(self):
        if type(self.d) == dict:
            #print(self.d.values())
            return list(self.d.values())
            
    def error(self):
        try:
            
            if type(self.d)!=dict:
                #print(self.d)
                return 1
        except :
            print("not a dictionary")
            
    def userinput(self):
        self.d = eval(input())
        print(self.d,type(self.a))
        print(self.d.keys())
        print(self.d.values())
            
    def insert(self,k,v):
        
        self.d[k] = v
        