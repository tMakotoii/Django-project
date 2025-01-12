from datetime import datetime

from requests_html import HTMLSession
from slugify import slugify
import pprint

from news.models import Author, Article, Category

from django.utils.timezone import make_aware
from concurrent.futures import ThreadPoolExecutor

AUTHOR = None



def crawl_one(url):
    global AUTHOR

    if not AUTHOR:
        AUTHOR = Author.objects.get(id=3)

    try:

        with HTMLSession() as session:
            response = session.get(url)
            name = response.html.xpath('//main/div[1]/div[1]/div/div[1]/div/h1')[0].text
            content = response.html.xpath('//main/div[1]/div[2]/div/div/div/p')
            short_description = response.html.xpath('//main/div[1]/div[2]/div/div/div[2]/p')[0].text
            image_url = response.html.xpath('//main/div[1]/div[1]/div/div[2]/figure/div/div/picture/img/@src')[0]
            pub_date = response.html.xpath('//main/div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//time')[0].text
            cats = response.html.xpath('//main/div[1]/div[4]/div/div/div/div[1]/a')

            my_content = ''
            for el in content:
                # my_content += el.text
                my_content += f"<{el.tag}>" + el.text + f"<{el.tag}>"

            image_name = slugify(name)
            img_type = image_url.split('.')[-1]

            img_path = f'images/{image_name}.{img_type}'

            with open(f'media/{img_path}', 'wb') as f:
                with HTMLSession() as session:
                    response = session.get(image_url)
                    f.write(response.content)

            pub_date = datetime.strptime(pub_date, '%d.%m.%y')

            categories = []
            for cat in cats:
                categories.append(
                    {
                        'name': cat.text.strip(),
                        'slug': slugify(cat.text)
                     }
                )

            article = {
                'name': name,
                'slug': slugify(name),
                'content': my_content,
                'short_description': short_description,
                'main_image' : img_path,
                'pub_date' : make_aware(pub_date),
                'author': AUTHOR
            }

            # article = Article(**article)
            # articles.append(article)

            article, created = Article.objects.get_or_create(**article)

            for category in categories:
                cat, created = Category.objects.get_or_create(**category)
                article.categories.add(cat)

            pprint.pp(article)

    except Exception as e:
        print(e, type(e))


def get_fresh_news():
    base_url = 'https://journal.tinkoff.ru/flows/economics/'

    with HTMLSession() as session:
        response = session.get(base_url)

    links = response.html.absolute_links
    fresh_news = [lnk for lnk in links
                  if (
                    'journal.tinkoff.ru/news' in lnk and
                    not lnk.endswith('#comments') and
                    '?q=' not in lnk and
                    'user' not in lnk and
                    '/page/' not in lnk
                  )]

    return fresh_news

def run():
    fresh_news = get_fresh_news()
    # Article.objects.all().delete()
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(crawl_one, fresh_news)

    # Article.objects.bulk_create(articles)