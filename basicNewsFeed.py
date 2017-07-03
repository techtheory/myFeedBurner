## Load Modules
import feedparser
import sys, os, time

## Get input from user
subreddit = input("\nEnter the subreddit (eg 'python') to view: ")
num_items = int(input("How many headlines do you want to show? "))
show_urls = input("Show URLs as well? y/n: ")
filter_word = input("Enter a word or term you want to filter out: ")

## Clear screen between refreshes
while 1:
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

## Load Feed
    myfeed = feedparser.parse("https://www.reddit.com/r/" + subreddit \
        + "/.rss")



## Subreddit sanity check
    if len(myfeed["entries"]) == 0:
        print("Subreddit not valid!")
        sys.exit(1)

    x = 1
## Filter out exclusions
    for post in myfeed.entries:
        if len(filter_word) > 0:
            if post.title.lower().find(filter_word.lower()) == -1:
                print("* " + post.title)
## Show urls?
                if show_urls == "y":
                    print("  (" + post.link + ")")
        else:
            print("* " + post.title)
            if show_urls == "y":
                print("  (" + post.link + ")")
## Limit entries to desired number
        x += 1
        if x > num_items:
            break
## Refresh interval  	
    time.sleep(60)
