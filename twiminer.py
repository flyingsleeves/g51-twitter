import twitter
import pickle

# userMap = {'anthonydiraddo':'792776432', 'TexasSuperAngel':'179651009'}

class Miner:
    def __init__(self):
        self.api = twitter.Api(consumer_key='0MHVKaQTwrzcCQHgrtklSY58Z',
                        consumer_secret='x0xEDrzwDt3JLxMco6GpPyqDMtksbBvtiLiTZ3Z5v91ukni7qb',
                        access_token_key='792776432-by9xYK1GGeopTJPdOZmhMsi5cEs54TljegEXPSzy',
                        access_token_secret='W5cKhlEQiaTmc1PwxVQMfzjbDpolTcuqmi9wxZZybyNC0')

    def mineUser(self, userID):
        
        friends = self.api.GetFriendIDs(userID)
        followers = self.api.GetFollowerIDs(userID)

        user = self.api.GetUser(userID)

        userInfo = {}
        userInfo['screen_name'] = user.screen_name
        userInfo['id'] = user.id
        userInfo['name'] = user.name
        userInfo['friends'] = friends
        userInfo['followers'] = followers

        masterList = {}

        with open('masterlist.pickle', 'r') as filepath:
            masterList = pickle.load(filepath)
            
        masterList[userID] = userInfo

        with open('masterlist.pickle', 'w') as filepath:
            pickle.dump(masterList, filepath)

        return user.screen_name