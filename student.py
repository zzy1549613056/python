#!/usr/local/bin/python3
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score


    @property
    def name(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('分数范围在0～100')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >60:
            return 'B'
        else:
            return 'C'

if __name__ == '__main__':
    zzy = Student('zzy',88)
    print('zzy:%s %s'%(zzy.get_score(),zzy.get_grade()))        