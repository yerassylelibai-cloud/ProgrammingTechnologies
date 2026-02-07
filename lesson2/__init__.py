import datetime

def lesson():
    dict = [
        {"название": "don't call me a Comeback ","категория":"Music", "Главная категория":"Music","Валюта":"USD", "Дедлайн":"2013-01-10","Дата публикации": "2012-12-09"},
        {"название": "Me & You Coordinating Sunglasses ","категория":"Accessories", "Главная категория":"Fashion","Валюта":"USD", "Дедлайн":"2016-11-18", "Дата публикации": "2016-10-19"},
        {"название": "New Carts for Istanbul Street Food Vendors","категория":"Food","Главная категория":"Food","Валюта":"KZT", "Дедлайн":"2015-05-17", "Дата публикации": "2015-04-17"},
        {"название": "New Improv Comedy Venue in Des Moines","категория":"Theater","Главная категория":"Theater","Валюта":"USD", "Дедлайн":"2013-06-17", "Дата публикации": "2013-05-03"},
        {"название": "The Seer and the Sword	","категория":"Shorts","Главная категория":"Film & Video","Валюта":"EUR", "Дедлайн":"2012-08-11", "Дата публикации": "2012-07-12"}
        ]

    for i in dict:
        i["Срок"]=(datetime.date.fromisoformat(i["Дедлайн"]) - datetime.date.fromisoformat(i["Дата публикации"])).days
        if i["Валюта"]=="USD":
            print(i)

lesson()