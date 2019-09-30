class Grade():

    def __init__(self):

        self.__score = 100


    def set_score(this,num):

        if num > this.__score:

            this.__score = num

    def get_score(self):

        return self.__score

    num = property(get_score,set_score)

score = Grade()

score.num = 200

print(score.num)
