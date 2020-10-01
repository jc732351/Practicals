import wikipedia

while True:
    page_title = input("Please enter the page title: ")"Let users use the wiki to find answers"
    if page_title !="":"Cannot enter empty"
        print(wikipedia.search(page_title))
        print(wikipedia.suggest(page_title))
        print(wikipedia.summary(page_title))
    else:
        break