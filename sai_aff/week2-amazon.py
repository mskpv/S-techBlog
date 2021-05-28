#!/bin/python3

from requests_html import HTMLSession
import pandas as pd


def get_asins(search):
    r = s.get(f'https://www.amazon.in/s?k={search}')
    asins = r.html.find('div.s-main-slot div[data-asin]')
    return [asin.attrs['data-asin'] for asin in asins if asin.attrs['data-asin'] != '']

def getdata(asin):
    try:
       r = s.get(f'https://www.amazon.in/dp/{asin}')
       #print(r.html.html)
       productname = r.html.find('#productTitle', first=True).full_text.strip()
       description = r.html.find('#feature-bullets', first=True).full_text.strip().replace('\n\n\n\n','\n')
       try:
           ratingscount =  r.html.find('#acrCustomerReviewText', first=True).full_text.strip()
       except:
           ratingscount = 0
       overall_ratings = r.html.find('.a-icon-alt', first=True).full_text.strip()
       pic = r.html.find('#landingImage', first=True) # (first=True) is nothing but take the first index of the list ex:[0]
       image = pic.attrs['data-old-hires']
       price = r.html.find('#priceblock_ourprice', first=True).full_text.strip()
       #reviews = r.html.find('div[data-hook=review]')
       topreviews = []
       #for rev in reviews:
       #    ratings = {
       #    'title': rev.find('a[data-hook=review-title] span', first=True).full_text,
       #    'rating': rev.find('i[data-hook=review-star-rating] span', first=True).full_text,
       #    #'image': rev.find('i[data-hook=review-star-image] span', first=True).full_text,
       #    }
       #    topreviews.append(ratings)    
       
       product = {
           'productname': productname,
           'description': description,
           'ratingscount': ratingscount,
           'overall_ratings': overall_ratings,
           #'reviews': topreviews,
           'image': image,
           'price': price,
       }
       #print(product)
       return product
    except:
       pass


def main():
    search = 'mobiles below 10000'
    asins = get_asins(search)
    #print(f'Found {len(asins)} asins')
    #print(asins)
    result = [getdata(asin) for asin in asins]
    #df = pd.DataFrame(result)
    #df.to_csv(search + '.csv', index=False)
    dic_ls = []
    for i in result:
        if i == None:
           continue
        dictionary_copy = i.copy()
        #print(i)
        dic_ls.append(dictionary_copy)
    df = pd.DataFrame(dic_ls)
    df.to_csv(search + '.csv', index=False)
    return

if __name__ == '__main__':
    s = HTMLSession()
    main()
