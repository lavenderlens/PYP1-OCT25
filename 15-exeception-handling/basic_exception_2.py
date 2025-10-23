
class TrainingCourse:
    # as it stands, a TrainingCourse object may be cretaed with null or empty fields.
    # suppose we wanted to code against this:
    def __init__(self, title, duration, price_per_person):
        self.title = ''
        self.set_title(title)
        self.duration = duration
        self.price_per_person = price_per_person
        self.delegates = []
    def set_title(self, title):
        if title != "":
            self.title = title
        else:
            # print("title must not be empty")
            raise Exception("title must not be empty")

    def add_delegate(self, name):
        self.delegates.append(name)
    def get_total_revenue(self):
        return self.price_per_person *len(self.delegates)
    def __str__(self):
        return f"Course Title: {self.title}\n\
Duration (days): {self.duration}\n\
Price Per Person: {self.price_per_person}\n\
Delegates booked: {self.delegates}"
    
# python_1 = TrainingCourse("Python Programming 1", 4, 1600.00)
python_1 = None
try:
    python_1 = TrainingCourse("", 4, 1600.00)
except:
    print("course not created")
if python_1:
    print(python_1)