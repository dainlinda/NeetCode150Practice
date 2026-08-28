from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.shalf = []  # max_heap
        self.lhalf = []  # min_heap

    def addNum(self, num: int) -> None:
        heappush(self.shalf, -num)
        to_large = heappop(self.shalf)
        heappush(self.lhalf, -to_large)  # negate back

        if len(self.shalf) < len(self.lhalf):
            to_small = heappop(self.lhalf)
            heappush(self.shalf, -to_small)  # negate

    def findMedian(self) -> float:
        if len(self.shalf) != len(self.lhalf):  # odd
            return -self.shalf[0]
        else:  # even
            return (-self.shalf[0] + self.lhalf[0]) / 2


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(-1)
    medianFinder.addNum(-2)
    print(medianFinder.findMedian())
    medianFinder.addNum(-3)
    print(medianFinder.findMedian())
    medianFinder.addNum(-4)
    print(medianFinder.findMedian())
    medianFinder.addNum(-5)
    print(medianFinder.findMedian())
