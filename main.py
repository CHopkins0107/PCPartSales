import praw
import re
from amazon import amazonSearch, walmartSearch
from parts import Part

price_regex = r'(?P<Price>\$\d+(\.\d+)?)'
scrubber_regex = r'(\[)[^\}]*(\])'
scrubber_regex2 = r'(\()[^\}]*(\))'

reddit = praw.Reddit('SalesBot')
subreddit = reddit.subreddit("buildapcsales")

part_to_search_for = ["Monitor", "Mouse"]
discount_perc = 0.4
part_list = []
big_deals = []

def strToPrice(price1, price2):
    global discount_perc
    price1 = float(price1[1:])
    price2 = float(price2[2:])



def name_scrubber(input_str):
    global price_regex
    global scrubber_regex
    global scrubber_regex2

    scrubbed_name = re.sub(scrubber_regex, '', input_str).strip()
    scrubbed_name = re.sub(scrubber_regex2, '', scrubbed_name).strip()
    scrubbed_name = scrubbed_name.replace(" - " + price.group(0), '')

    return scrubbed_name


for submission in subreddit.new(limit=50):
    if part_to_search_for:
        for part_name in part_to_search_for:
            if part_name in submission.title:
                price = re.search(price_regex, submission.title)
                if price:
                    title_str = name_scrubber(submission.title)
                    new_part = Part(part_name, title_str, price.group(0), submission.url)
                    part_list.append(new_part)
    else:
        for item in submission.title:
            part_name = re.search(r'(\[.+\])', submission.title).groups()
            price = re.search(price_regex, submission.title)
            if price:
                title_str = name_scrubber(submission.title)
                new_part = Part(part_name, title_str, price.group(0), submission.url)
                part_list.append(new_part)

for part in part_list:
    if "amazon" not in part.url.lower():
        print(amazonSearch(part.part_str))
    """else:
        print(part)
        print()
        print(walmartSearch(part.part_str))
    """
