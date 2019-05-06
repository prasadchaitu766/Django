class student():
    def set_details(self,id,name,address):
        self.id=id
        self.name=name
        self.address=address
    def get_details(self):
        return self.id,self.name,self.address
