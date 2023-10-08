
class Labirinth:
    def __init__(self,file_name :str) -> None:
        file=open(file_name,"r")
        self.table=list()
        tmp=file.read()
        sorok=tmp.split("\n")
        for i in sorok:
            self.table.append(i.split(" "))
    
    def print(self):
        for i in self.table:
            print(i)
    def getTable(self):
        return self.table
        
