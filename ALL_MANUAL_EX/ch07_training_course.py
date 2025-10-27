
class TrainingClass:

    def __init__(self, title, duration, price_per_person) -> None:
        self.title = title
        self.duration = duration
        self.price_per_person = price_per_person
        self.delegates = []
    
    def addDelegate(self, delegate_name):
        self.delegates.append(delegate_name)
    
    def getTotalRevenue(self):
        revenue = self.price_per_person * len(self.delegates)
        return revenue
    
    def __str__(self) -> str:
        str_rep = f"Course, \n Title:{self.title} \n " + \
                    f"Duration : {self.duration}"
        return str_rep

    def __lt__(self, other):
        return self.getTotalRevenue() < other.getTotalRevenue()
    

python_1 = TrainingClass('Python Programming 1', 4, 1600)
python_1.addDelegate('James')
python_1.addDelegate('Fatima')
python_1.addDelegate('Stuart')
python_1.addDelegate('Sarah')

python_2 = TrainingClass('Python Programming 2', 4, 2200)
python_2.addDelegate('Fatima')
python_2.addDelegate('Stuart')
python_2.addDelegate('Sarah')

def tab_settings():
    # 1 tab
    # 4 spaces
    pass
print(python_1 > python_2)

# print(python_1.delegates)
# print(f"revenue from {python_1.title} is {python_1.getTotalRevenue()}")