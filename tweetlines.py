from settings import *
import time
import sys
from twitter import *

# authenticate with twitter
twitter = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

print ("Opening text file.")

#open file, tweet each line, waiting 60 seconds between
with open('849.txt', 'r') as fileinput:
  i = 1
  for line in fileinput:
    if not line: break
    twitter.statuses.update(status = line)
    def countdown(t):
      while t:
          mins, secs = divmod(t, 60)
          timeformat = '{:02d}:{:02d}'.format(mins, secs)
          sys.stdout.write("\r" + timeformat)
          sys.stdout.flush()
          time.sleep(1)
          t -= 1
    print ("\n\n" + format(i) + '. Tweeted about ' + (line.split(" (")[0]) + '.')
    countdown(60)
    i += 1
  fileinput.close()
