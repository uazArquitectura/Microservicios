from twython import Twython
import sys
import requests.packages.urllib3

reload(sys)
requests.packages.urllib3.disable_warnings()
sys.setdefaultencoding("utf-8")

ConsumerKey = "jfij525430WHSqo46VCXiTA95"
ConsumerSecret = "BfFZ6iSPTj7u699apBGY3Yu4RHMLOVR61QGASVenGVLdjh6lRb"
AccessToken = "3290922366-kDNgrRkVLYnVQXDTtKbJqH1wCj0fkVKJy3PotjV"
AccessTokenSecret = "Ulb7EPn9VQ4rWa8wIXflzGvMuNrZ1yBtVYQ6MSTvtl1We"

twitter = Twython(ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret)

result = twitter.search(q="@netflix #13ReasonsWhy", count=100)

for status in result["statuses"]:
    print 'Tweet from @' + status["user"]['screen_name']
    print '\tstatus: {0}'.format(status['text']).replace('\n', '\n\t')
    print '\tcreated_at: {0}'.format(status['created_at'])
