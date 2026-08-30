
# Approach

## Check conditions to meet

- Implement 5 methods of Twitter
  - Twitter()
  - void postTweet(int userId, int tweetId)
  - List<Integer> getNewsFeed(int userId)
  - void follow(int followerId, int followeeId)
  - void unfollow(int followerId, int followeeId)
- 1<= userId, followerId, followeeId <= 500
- 0<=tweetId<=10^4
  - tweetID, userId are unique
- `postTweet`, `getNewsFeed`, `follow`, and `unfollow` <= 3 * 10^4 calls
- A user cannot follow themself

## Key idea 

- maintain user to following dict => {userId(self): [userIds](followings)}
- maintain per user 10-sized min-heap only keeping most recent 10 tweets of each user
  - use a tweet counter to track tweet order

## Complexity
- time:
  - postTweet: O(log k)
    - k=10 because 10-sized min heap, therefore O(log10)=O(1)
  - getNewsFeed: O(klogk * (user's following # + 1)) + O(klogk) for sorting
    - because k=10 and user's following # <= 500, it's also O(1) 
  - follow: O(1) / unfollow : O(1)
- space: 
  - self.users: O(followings per user) = O(500*500) = O(1)
  - self.tweets: O(# of users * k) = O(500 * 10) = O(1)

## Caveat and Reflection (Claude-assisted)

- Wrong assumption: tweetId increases strictly, so larger tweetId = the most recent tweet 
