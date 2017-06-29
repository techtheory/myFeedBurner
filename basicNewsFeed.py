import feedparser, time
import sys, os

subreddit = input("\nEnter the subreddit (eg 'worldnews') to view: ")
no_of_items = int(input("How many headlines do you want to show? "))
show_urls = input("Show URLs as well? y/n: ")
filter = input("Enter a word or term you want to filter out: ")

while 1:
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    myfeed = feedparser.parse("https://www.reddit.com/r/" + subreddit \
        + "/.rss")

    print(myfeed)
    sys.exit(1)

    if len(myfeed["entries"]) == 0:
        print("Subreddit not valid!")
        sys.exit(1)

    x = 1

    for post in myfeed.entries:
        if len(filter) > 0:
            if post.title.lower().find(filter.lower()) == -1:
                print("* " + post.title)
                if show_urls == "y":
                    print("  (" + post.link + ")")
        else:
            print("* " + post.title)
            if show_urls == "y":
                print("  (" + post.link + ")")
        x += 1
        if x > no_of_items:
            break

    time.sleep(60)
