# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonpageItem


class AmazonlistSpider(scrapy.Spider):
    name = 'amazonlist'
    page_number = 2
    start_urls = ['https://www.amazon.in/Test-Exclusive-TST_Exclusive1043-3GB-Storage/product-reviews/B07S6BW832']

    def parse(self, response):
        items = AmazonpageItem()

        all_data = response.css("#cm_cr-review_list .celwidget")

        for resp in all_data:
            name = resp.css(".a-profile-name::text").extract()
            title = resp.css(".a-text-bold span::text").extract()
            reviews = resp.css(".a-icon-alt::text").extract()
            comments = resp.css(".review-text-content span::text").extract()

            items['name'] = name
            items['title'] = title
            items['reviews'] = reviews
            items['comments'] = comments

            yield items

            next_page = 'https://www.amazon.in/Test-Exclusive-TST_Exclusive1043-3GB-Storage/product-reviews/B07S6BW832/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber=' + str(AmazonlistSpider.page_number)
            if AmazonlistSpider.page_number <= 5:  # Change the page number as per your requirement
                AmazonlistSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse)

