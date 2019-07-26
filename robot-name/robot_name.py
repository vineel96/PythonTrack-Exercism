import string,random
class Robot(object):
    def __init__(self):
        random.seed()
        self.name="".join(random.choice(string.ascii_uppercase) for i in range(2))+"".join(random.choice("123456789") for i in range(3))

    def reset(self):
        self.__init__()


