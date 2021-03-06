from .Calculator import Calculator
import statistics
from .helper import Helper

class StatsCalculator(Calculator):

    @Helper.validateListInput
    def mean(self,lst):
        '''
        mean
        :param lst:
        :return: mean of list
        '''
        return statistics.mean(lst)

    @Helper.validateListInput
    def median(self,lst):
        '''
        median
        :param lst:
        :return: median of list
        '''
        return statistics.median(lst)

    @Helper.validateListInput
    def mode(self,lst):
        '''
        mode
        :param lst:
        :return: mode of list
        '''
        return statistics.mode(lst)

    @Helper.validateListInput
    def stdev(self,lst):
        '''
        Standard Deviation
        :param lst:
        :return:Standard Deviation of list
        '''
        return statistics.pstdev(lst)

    @Helper.validateListInput
    def variance(self,lst):
        '''
        Variance
        :param lst:
        :return: Variance of List
        '''
        return statistics.variance(lst)

