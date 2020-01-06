class Worker:
    def __init__(self, id: int):
        self.id = id
        self.job = None
        self.seconds_left = 0
        self.wants_new_job = True

    def second_passed(self):
        self.seconds_left -= 1
        if self.seconds_left == 0:
            self.wants_new_job = True
    
    def give_new_job(self, new_job):
        if new_job == None:
            self.job = None
        else:
            self.seconds_left = ord(new_job) - 4
            self.job = new_job
            self.wants_new_job = False