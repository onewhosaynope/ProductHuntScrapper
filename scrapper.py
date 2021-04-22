from ph_helper.product_hunt_client import ProductHuntClient
from langdetect import detect
from helper_surname import check
from datetime import datetime
import data


def scrap():

    client_id = data.client_id
    client_secret = data.client_secret
    redirect_uri = data.redirect_uri

    phc = ProductHuntClient(client_id, client_secret, redirect_uri)

    count_ru_posts = 0
    count_all_posts = 0

    for post in phc.get_todays_posts():
        found = False
        count_all_posts = count_all_posts + 1
        list_of_makers = []
        for maker in post.makers:
            list_of_makers.append(maker.name)
            if (detect(maker.name) == "ru" or check(maker.name)):
                found = True

        if found == True:
            count_ru_posts = count_ru_posts + 1
            message = "Name:\n" + post.name + "\n\nDescription:\n" + post.tagline + "\n\nMakers:\n" + ", ".join(list_of_makers) + "\n\nProductHunt Link:\n" + "https://www.producthunt.com/posts/" + str(post.id) + "\n\nRedirect Link:\n" + post.redirect_url
            print(message)

    message = "Totall posts today: " + str(count_all_posts) + "\nWith makers from CIS: " + str(count_ru_posts)
    print(message)

scrap()