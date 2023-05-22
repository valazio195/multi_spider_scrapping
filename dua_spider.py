import scrapy
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.utils.project import get_project_settings

from mantul.spiders.dapo_1 import Dapo1Spider
from mantul.spiders.dapo_2 import Dapo2Spider
from mantul.spiders.dapo_3 import Dapo3Spider
from mantul.spiders.dapo_4 import Dapo4Spider
from mantul.spiders.dapo_5 import Dapo5Spider
from mantul.spiders.dapo_6 import Dapo6Spider
from mantul.spiders.dapo_7 import Dapo7Spider
from mantul.spiders.dapo_8 import Dapo8Spider




settings = get_project_settings() #import settings
process = CrawlerProcess(settings)


crawl_part1 = Crawler(Dapo1Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_1.csv": {"format":"csv"},
            },
        },
)

crawl_part2 = Crawler(Dapo2Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_2.csv": {"format":"csv"},
            },
        },
)

crawl_part3 = Crawler(Dapo3Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_3.csv": {"format":"csv"},
            },
        },
)

crawl_part4 = Crawler(Dapo4Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_4.csv": {"format":"csv"},
            },
        },
)

crawl_part5 = Crawler(Dapo5Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_5.csv": {"format":"csv"},
            },
        },
)

crawl_part6 = Crawler(Dapo6Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_6.csv": {"format":"csv"},
            },
        },
)


crawl_part7 = Crawler(Dapo7Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_7.csv": {"format":"csv"},
            },
        },
)

crawl_part8 = Crawler(Dapo8Spider,
        settings={
            **settings,
            "FEEDS":{
                "dapodik_sulawesi_selatan_part_8.csv": {"format":"csv"},
            },
        },
)





process.crawl(crawl_part1)
process.crawl(crawl_part2)
process.crawl(crawl_part3)
process.crawl(crawl_part4)
process.crawl(crawl_part5)
#process.crawl(crawl_part6)
#process.crawl(crawl_part7)
#process.crawl(crawl_part8)



process.start()


