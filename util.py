import twiminer
import pickle

masterlist = {}

def mine(userID):
	m = twiminer.Miner()
	userScreenName = m.mineUser(userID)
	print "mined: " + userScreenName

def printMinedUsers():
	with open('masterlist.pickle', 'r') as filepath:
	    masterList = pickle.load(filepath)

	for ID in masterList:
		print masterList[ID]['screen_name'] + " : " + str(ID)

def printAllData():
	with open('masterlist.pickle', 'r') as filepath:
	    masterList = pickle.load(filepath)

	for ID in masterList:
		userInfo = masterList[ID]
		print ''
		print 'screen_name: ' + userInfo['screen_name']
		print 'id: ' + str(userInfo['id'])
		print 'name: ' + userInfo['name']
		print 'friends: ' + str(userInfo['friends'][:5]).rstrip(']') + ', ...]'
		print 'followers: ' + str(userInfo['followers'][:5]).rstrip(']') + ', ...]'

def mineIndex(idx):
	with open('masterlist.pickle', 'r') as filepath:
	    masterList = pickle.load(filepath)

	userInfo = masterList['179651009']
	mine(userInfo['friends'][idx])

def mineHundred():
	i = 0
	while i < 100:
		mineIndex(i)
		i += 1