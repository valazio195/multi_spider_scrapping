import scrapy
from scrapy_splash import SplashRequest
from mantul.items import Dapo_1_Item



class Dapo1Spider(scrapy.Spider):
    name = 'dapo_1'
    


    def start_requests(self):
        url = ['https://dapo.kemdikbud.go.id/progres/1/190000'] #Sulsel
        for urls in url:
            yield SplashRequest(url=urls,
                            callback=self.parse_kab,
                            endpoint='render.html',
                            args={
                                'wait': 3,
                               # 'lua_source' : script_iter
                                })
    
    
    def parse_kab(self, response):
        table_kab = response.css('#DataTables_Table_0 tbody')
        kab_lst = table_kab.css('tr.data td a::attr(href)').getall()
        kab_batch_1 = kab_lst[0:7]
        
        for url in kab_batch_1:
            yield SplashRequest(url='https://dapo.kemdikbud.go.id' + url,
                            callback=self.parse_kec,
                            endpoint='render.html',
                            args={
                                'wait': 5
                                })
            #yield response.follow(url='https://dapo.kemdikbud.go.id' + url, callback=self.parse_kec)
    
    def parse_kec(self, response):
        table_kab = response.css('#DataTables_Table_0 tbody')
        kec_lst = table_kab.css('tr.data td a::attr(href)').getall()
        for url in kec_lst:
            yield SplashRequest(url='https://dapo.kemdikbud.go.id' + url,
                            callback=self.parse_sekolah,
                            endpoint='render.html',
                            args={
                                'wait': 5
                                })
            #yield response.follow(url='https://dapo.kemdikbud.go.id' + url, callback=self.parse_sekolah)
    
    def parse_sekolah(self, response):
        table_kab = response.css('#dataTables tbody')
        sekolah_lst = table_kab.css('tr.data td a::attr(href)').getall()
        for url in sekolah_lst:
            yield response.follow(url='https://dapo.kemdikbud.go.id' + url, callback=self.parse_detail)
    
    def parse_detail(self, response):
        data_sekolah = Dapo_1_Item()
        #profile = response.css('#profil')
       # rekap = response.css('#rekapitulasi')
       # kontak = response.css('#kontak')
        
        #Di tab utama
        data_sekolah['nama_sekolah'] = response.css('h2.name::text').get()
        data_sekolah['kecamatan'] = response.css('.breadcrumb > li:nth-child(5) > a:nth-child(1) > span:nth-child(1)::text').get()
        data_sekolah['kabupaten'] = response.css('.breadcrumb > li:nth-child(4) > a:nth-child(1) > span:nth-child(1)::text').get()
        data_sekolah['provinsi'] = response.css('.breadcrumb > li:nth-child(3) > a:nth-child(1) > span:nth-child(1)::text').get()
        data_sekolah['npsn'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)::text').get()
        data_sekolah['status'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)::text').get()
        data_sekolah['bp'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(3)::text').get()
        data_sekolah['stat_kep'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(4)::text').get()
        data_sekolah['sk_pendirian_sekolah'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(5)::text').get()
        data_sekolah['tanggal_sk'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(6)::text').get()
        data_sekolah['sk_izin'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(7)::text').get()
        data_sekolah['tanggal_sk_izin'] = response.css('div.col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(8)::text').get()
        data_sekolah['keb_khusus_dilayani'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)::text').get()
        data_sekolah['bank'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)::text').get()
        data_sekolah['cabang_kcp'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(3)::text').get()
        data_sekolah['rekening'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(4)::text').get()
        data_sekolah['status_bos'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1)::text').get()
        data_sekolah['waktu_penyelenggaraan'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(2)::text').get()
        data_sekolah['sert_iso'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(3)::text').get()
        data_sekolah['sumber_listrik'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(4)::text').get()
        data_sekolah['daya_listrik'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(5)::text').get()
        data_sekolah['akses_isp'] = response.css('div.col-md-6:nth-child(2) > div:nth-child(2) > div:nth-child(2) > p:nth-child(6)::text').get()

        data_sekolah['ref_url'] = response.url


        yield data_sekolah
    


