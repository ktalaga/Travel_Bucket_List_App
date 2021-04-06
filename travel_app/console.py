import pdb

from models.country import Country
from models.city import City
from models.sight import Sight


import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.sight_repository as sight_repository

country_repository.delete_all()
city_repository.delete_all()
sight_repository.delete_all()

country_image_1 = "https://scotland5gcentre.org/wp-content/uploads/2020/06/rural-800x800.jpg"
country_1 = Country('Scotland', country_image_1, True)
country_repository.save(country_1)

country_image_2 = "https://www.parkplazalondonwaterloo.com/wp-content/uploads/2018/12/big-ben-1-800x800.jpg"
country_2 = Country('England', country_image_2)
country_repository.save(country_2)

country_image_3 = "https://i.pinimg.com/originals/b5/71/a8/b571a811e923351e8d26eb679a167ce8.jpg"
country_3 = Country('Poland', country_image_3)
country_repository.save(country_3)

country_image_4 = "https://frontier-canada.co.uk/wp-content/uploads/2020/11/british-columbia-relection800x800.jpg"
country_4 = Country('Canada', country_image_4)
country_repository.save(country_4)

country_image_5 = "https://lowseasontraveller.com/wp-content/uploads/2020/06/Ha-Long-Bay-Vietnam-800x800.jpg"
country_5 = Country('Vietnam', country_image_5)
country_repository.save(country_5)

country_image_6 = "https://format-com-cld-res.cloudinary.com/image/private/s--xqUxnkpB--/c_fill,g_center,h_800,w_800/fl_keep_iptc.progressive,q_95/v1/632fd6815c463c646feb4b47b2281d6a/001-Turkey-IMG_1186_1_-2.jpg"
country_6 = Country('Turkey', country_image_6)
country_repository.save(country_6)

country_image_7 = "https://img.travelawaits.com/filter:centercrop/quill/2/d/2/3/f/b/2d23fb646e858372d45471a1ca2f67506c4903e7.jpg?w=800&h=800"
country_7 = Country('India', country_image_7)
country_repository.save(country_7)

country_image_8 = "https://local21news.com/resources/media/d7c96631-85be-425d-a94b-4b70b7322293-large1x1_thumb_8859.png?1594202519961"
country_8 = Country('USA', country_image_8)
country_repository.save(country_8)


city_image_1 = "https://www.dentons.com/-/media/images/website/background-images/offices/aberdeen/aberdeen-city.ashx"
city_1 = City('Aberdeen', city_image_1, country_1)
city_repository.save(city_1)

city_image_2 = "https://img.travelawaits.com/filter:centercrop/quill/e/0/6/1/9/4/e0619492563020dcea1769f8d9ea0acc5b7abcfa.jpg?w=800&h=800"
city_2 = City('Glasgow', city_image_2, country_1)
city_repository.save(city_2)

city_image_3 = "https://www.danielwebster.co.uk/wp-content/uploads/2016/11/LondonAbove-800x800.jpg"
city_3 = City('London', city_image_3, country_2, True)
city_repository.save(city_3)

city_image_4 = "https://img.travelawaits.com/filter:centercrop/quill/f/e/0/6/5/c/fe065c20de439fdb60d47d4a4ec4a5711f914d14.jpg?w=800&h=800"
city_4 = City('Liverpool', city_image_4, country_2, True)
city_repository.save(city_4)

city_image_5 = "https://bubotree-files.s3-eu-west-1.amazonaws.com/production/2018-10/0E9E3BF4-31D5-4E68-AF89-E5511F3FCB52.jpg"
city_5 = City('Cracow', city_image_5, country_3, True)
city_repository.save(city_5)

city_image_6 = "https://img.travelawaits.com/filter:centercrop/quill/1/3/0/6/e/f/1306efa1306a05db6976d07e22d1359466fca5b4.jpg?w=800&h=800"
city_6 = City('Warsaw', city_image_6, country_3, True)
city_repository.save(city_6)

city_image_7 = "https://www.vb-business.at/wp-content/uploads/British-Airways-Toronto-picture-800x800.jpg"
city_7 = City('Toronto', city_image_7, country_4, True)
city_repository.save(city_7)

city_image_8 = "https://d3qu76g3gxgr45.cloudfront.net/wp-content/uploads/2020/04/19083105/yp2cYX4.jpg"
city_8 = City('Niagara Falls', city_image_8, country_4, True)
city_repository.save(city_8)

city_image_9 = "https://www.mundoasiatours.com/wp-content/uploads/2018/08/ho-chi-minh-city-attraction-s05.jpg"
city_9 = City('Ho Chi Minh', city_image_9, country_5, True)
city_repository.save(city_9)

city_image_10 = "https://www.mundoasiatours.com/wp-content/uploads/2018/08/halong-bay-attraction-s7.jpg"
city_10 = City('Ha Long', city_image_10, country_5, True)
city_repository.save(city_10)

city_image_11 = "https://i0.wp.com/www.pinkjinn.com/wp-content/uploads/2017/08/Blog-featured-image.png?resize=800%2C800&ssl=1"
city_11 = City('Istambul', city_image_11, country_6, True)
city_repository.save(city_11)

city_image_12 = "https://media-cdn.tripadvisor.com/media/photo-s/10/07/76/0b/photo9jpg.jpg"
city_12 = City('Pammukale', city_image_12, country_6, True)
city_repository.save(city_12)

city_image_13 = "https://i.pinimg.com/originals/c5/80/33/c58033c24251c622aa5095b4d3ec1c05.jpg"
city_13 = City('Agra', city_image_13, country_7, True)
city_repository.save(city_13)

city_image_14 = "https://img.travelawaits.com/filter:centercrop/quill/a/0/e/a/9/c/a0ea9c5da95af8ab63b0300308bee919419ef854.jpg?w=800&h=800"
city_14 = City('New Dehli', city_image_14, country_7, True)
city_repository.save(city_14)

city_image_15 = "https://intermountainhealthcare.org/-/media/images/modules/news/newyork.jpg?mw=800&hash=8B88D1336DEC8C87303433B5DC81348719956431"
city_15 = City('New York', city_image_15, country_8, True)
city_repository.save(city_15)

city_image_16 = "https://aws-tiqets-cdn.imgix.net/images/content/09214d1f73e045b48bdfb92e61694a29.jpg?auto=format&fit=crop&h=800&ixlib=python-3.2.1&q=70&w=800&s=b47c57e2425cf1c51bc0af572071824d"
city_16 = City('Las Vegas', city_image_16, country_8, True)
city_repository.save(city_16)




sight_image_5 = "https://aws-tiqets-cdn.imgix.net/images/content/306cbdc84c584ea8aa84d5d4f878bccb.jpg?auto=format&fit=crop&h=800&ixlib=python-3.2.1&q=70&w=800&s=0393b0e037dba33db75b006143e940ea"
sight_5 = Sight('Royal Albert Hall', sight_image_5, city_3)
sight_repository.save(sight_5)

sight_image_6 = "https://www.parkplazalondonwaterloo.com/wp-content/uploads/2018/12/big-ben-1-800x800.jpg"
sight_6 = Sight('Big Ben', sight_image_6, city_3)
sight_repository.save(sight_6)



sight_image_1 = "https://img.travelawaits.com/filter:centercrop/quill/e/b/8/5/5/8/eb8558ea2f7d05b16c4126fa8c2f94a51dd4f674.jpg?w=800&h=800"
sight_1 = Sight('Empire State Building', sight_image_1, city_15)
sight_repository.save(sight_1)

sight_image_2 = "https://news3lv.com/resources/media/b3c7482f-a258-44bc-9405-ba0fa9bd0a54-large1x1_GettyImages1216521309.jpg?1589292454611"
sight_2 = Sight('MGM Grand', sight_image_2, city_16)
sight_repository.save(sight_2)

sight_image_3 = "https://static.turbosquid.com/Preview/2014/05/27__03_48_27/Statue_of_Liberty_03.jpg73d6e874-5fdf-4740-9971-8219ff57e0acOriginal.jpg"
sight_3 = Sight('Statue of Liberty', sight_image_3, city_15)
sight_repository.save(sight_3)

sight_image_4 = "https://bubotree-files.s3-eu-west-1.amazonaws.com/production/2018-10/0E9E3BF4-31D5-4E68-AF89-E5511F3FCB52.jpg"
sight_4 = Sight('Wawel Castle', sight_image_4, city_5)
sight_repository.save(sight_4)

sight_image_7 = "https://silkroaddreamtours.com/wp-content/uploads/2020/06/Blue-Mosque-%E2%80%93-Istanbul.jpg"
sight_7 = Sight('Blue Mosque', sight_image_7, city_11)
sight_repository.save(sight_7)

sight_image_8 = "https://i.pinimg.com/originals/1a/d9/c0/1ad9c043339fb12d706539903fb721b8.jpg"
sight_8 = Sight('Taj Mahal', sight_image_8, city_13)
sight_repository.save(sight_8)







pdb.set_trace()