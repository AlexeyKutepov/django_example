__author__ = 'Alexey Kutepov'

from time import sleep

class Processor():

    def process(self, count=1):
        for i in range(count):
            sleep(1) #спим одну секунду
            print(i)