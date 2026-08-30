from typing import List
from collections import defaultdict
from heapq import heappush, heapreplace


class Twitter:
    def __init__(self):
        self.users = defaultdict(set)  # userId: {followings}
        self.tweets = defaultdict(list)  # userId: min_heap(tweets)
        self._tweet_order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets or len(self.tweets[userId]) < 10:
            heappush(self.tweets[userId], (self._tweet_order, tweetId))
        else:
            heapreplace(self.tweets[userId], (self._tweet_order, tweetId))
        self._tweet_order += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []  # 10-sized min-heap

        candidates = {userId}
        if userId in self.users:
            candidates.update(self.users[userId])

        for user in candidates:
            if user in self.tweets:
                for tweet in self.tweets[user]:
                    if len(result) < 10:
                        heappush(result, tweet)
                    elif result[0] < tweet:
                        heapreplace(result, tweet)

        return [i[1] for i in sorted(result, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 3)
    twitter.postTweet(1, 4)
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 6)
    twitter.postTweet(1, 7)
    twitter.postTweet(1, 8)
    twitter.postTweet(1, 9)
    twitter.postTweet(1, 10)
    twitter.postTweet(1, 11)
    print(twitter.getNewsFeed(1))  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    twitter.follow(2, 1)
    print(twitter.getNewsFeed(2))  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    twitter.unfollow(2, 1)
    print(twitter.getNewsFeed(2))  # []
