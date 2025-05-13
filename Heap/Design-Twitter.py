import heapq 
from typing import List
class Twitter:

    def __init__(self):
        self.isFollowing = {} # * Key: userID --> Value: List[userIDs...] 
        self.hasTweeted = {} # * userID --> Value: List[List[time, tweetId]]
        self.time = 0 # ! time starts @ 0 --> Decrements by 1, everytime a tweet has been posted
    def postTweet(self, userId: int, tweetId: int) -> None:
        # setdefault instantiates an empty List as the value to the userId, if the userId does not exist (user never posted before)
        # ? I am pretty sure this means List[time, tweetId] is mapped to an unique userId
        self.hasTweeted.setdefault(userId, []).append([self.time, tweetId])
        self.time -= 1 # Increment time by 1 after each post
        print(f"postTweet: userId={userId}, tweetId={tweetId}, hasTweeted={self.hasTweeted}, time={self.time}")

    def getNewsFeed(self, userId: int) -> List[int]:
        # ? Use heap to produce O(n + klog(n)) ? 
        # Loop through each tweet to heapify, must be the one that matches userId
        print(f"getNewsFeed: userId={userId}")
        candidate = [] # TODO: Stores the only the userId relevant tweet -> I'm sure there is better way in doing this

        # 1) Get his own tweets
        for tweet in self.hasTweeted.get(userId): 
            candidate.append(tweet)
        print(f"getNewsFeed: candidate before heapify={candidate}")

        #2) Get tweets from people they follow 
        # Iterate through each user ID that the current user (userId) follows
        for followeeMembers in self.isFollowing.get(userId, []): # followeeMembers = userId --> of one of the followees
            # For each followed user, get their tweets
            print(f"getNewsFeed: processing tweets for followeeMemberId={followeeMembers}")
            for followeeTweets in self.hasTweeted.get(followeeMembers, []): # followeeTweets = List[time, tweetId]
                candidate.append(followeeTweets) 
                print(f"getNewsFeed: appending tweet={followeeTweets} from followeeMemberId={followeeMembers}")

        # * Heapify the candidates -> Since each tweet is structured as [time, tweetId], the heap heapifies it (min-heap) by indexing the time  
        heapq.heapify(candidate)
        print(f"getNewsFeed: candidate after heapify={candidate}")
        answer = []
        # Pop the first k 
        for index in range(10): 
            # Finished popping
            if len(candidate) == 0: 
                break
            else: 
            # Pop the most recent tweet --> [1] to obtain the tweetId obly
                answer.append((heapq.heappop(candidate))[1]) 
        print(f"getNewsFeed: answer={answer}")
        return answer


    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId starts following followeeId --> followerId isFollowing{} followeeId
        self.isFollowing.setdefault(followerId, []).append(followeeId)
        print(f"follow: followerId={followerId}, followeeId={followeeId}, isFollowing={self.isFollowing}")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (len(self.isFollowing.get(followerId)) > 0):
            self.isFollowing.get(followerId).remove(followeeId)
        print(f"unfollow: followerId={followerId}, followeeId={followeeId}, isFollowing={self.isFollowing}")
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)