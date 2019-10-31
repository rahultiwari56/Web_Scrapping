from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = 'https://www.flipkart.com/search?q=i%20phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"_1UoZlX"})


filename = "product.csv"
f = open(filename,"w")

'''

#print(len(containers))

#print(soup.prettify(containers[0]))
#a = soup.prettify(containers[0])

container = containers[0]
#print(container.div.img["alt"])

price = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)

ratings = container.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)

'''

header = "Product Name,Pricing,Rating\n"
f.write(header)

for container in containers:
    product_name = container.div.img["alt"]
    
    price_container = container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()
    
    rating_container = container.findAll("div",{"niH0FQ"})
    rating = rating_container[0].text.strip()
 
    
    trim_price = ''.join(price.split(','))
    rupee = trim_price.split("₹")
    add_rs = "Rs. "+rupee[1]
    split_price = add_rs.split('E')
    final_price = split_price[0]
    
    split_rating = rating.split(" ")
    final_rating = split_rating[0]
    
    print(product_name.replace(",","|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",","|") + "," + final_price + "," + final_rating + "\n")
    
f.close()



   