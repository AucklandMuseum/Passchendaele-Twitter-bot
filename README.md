# Commemorating Passchendaele
On October 12, 1917, more than 845 New Zealand servicemen lost their lives in [the First Battle of Passchendaele](https://en.wikipedia.org/wiki/First_Battle_of_Passchendaele), near Ypres, Belgium. In military-history terms it has become known as New Zealand's ["darkest day"](http://www.aucklandmuseum.com/war-memorial/online-cenotaph/features/remembering-nzs-darkest-day).

We wanted to commemorate the soldiers who lost their lives a century ago, and thought of memorialising them through a tweet-stream. Our aim was to tweet at least the name and link to the [Online Cenotaph](http://www.aucklandmuseum.com/cenotaph) record for each serviceman, but we found that in some cases we could supplement this with more data, such as the soldier's rank, and the age at which he died.

We used this simple Python script to run a bot on the account [@OnlineCenotaph](https://www.twitter.com/onlinecenotaph) on October 12, 2017. Our source data, which we saved to a text file, was the maniuplated results of a query to [our SPARQL endpoint](http://yasgui.org/short/rJqj_gNR-).

## Code
`tweetlines.py` takes a text file<sup id="a1">[1](#f1)</sup> and, using Twitter's own Python library, tweets it line-by-line, one per minute. The code expects a file called `settings.py` which should contain Twitter API credentials.

## Results
After a few hiccups owing to the rate at which we initially set the bot to tweet (once every 40 seconds), our bot got underway and tweeted consistently until late into the night.

Over the day, the account earned more than 15,500 impressions, outperforming our expectations. It was also mentioned in news roundups of events on the day, such as [this one from Newshub](http://www.newshub.co.nz/home/new-zealand/2017/10/live-updates-passchendaele-memorial-ceremony.html).

---
#### Notes
<b id="f1">1.</b> Our file is called `849.txt` because it lists 849 servicemen who were killed. Many sources list 846 servicemen, however [Online Cenotaph](http://www.aucklandmuseum.com/cenotaph) returns more than that for a query based on "October 22 1917" as date of death.[↩](#a1)
