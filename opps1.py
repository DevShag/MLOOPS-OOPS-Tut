class employee:

    def  __init__(self):
        self.id = 123
        self.designation = "SDE"
        self.salary = 50000


    
    def travel(self, designation):
        print(f"Employee is now traveling to {designation}")



sam = employee()
sam.name = 'Sam Kumar'
sam.travel('Kerala')