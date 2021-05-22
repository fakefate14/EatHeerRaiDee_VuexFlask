from flask import Flask , request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

eat_item = [
    {"name":"ข้าวผัดหมู",
    "url":"https://www.haveazeed.com/wp-content/uploads/2019/08/3.%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%9C%E0%B8%B1%E0%B8%94%E0%B8%AB%E0%B8%A1%E0%B8%B9-1.png"},
    
    {"name":"ซี่โครงหมูทอดกระเทียมพริกไทย",
    "url":"https://lh3.googleusercontent.com/proxy/Mu_M6ycrBwljbLw_sBCJ-7_zXx9Dnd6OKblgt9ivlXQ8Dj44CiuN6a77FyEZWtYZnvwQdWuip-ZfJFGUy-NFA3XSELYXcJ8g63IoKzT_6aMsGeqEnV2xMlu2"},
    
    {"name":"ข้าวมันไก่",
    "url":"https://i0.wp.com/shopee.co.th/blog/wp-content/uploads/2020/10/%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%A1%E0%B8%B1%E0%B8%99%E0%B9%84%E0%B8%81%E0%B9%88.jpg?resize=1280%2C720&ssl=1"},
    
    ]




@app.route("/eat",methods=["GET"]) #,"POST"
@cross_origin()
def post():
    if request.method == "GET":
        # print("*GET*")
        for item in eat_item:
            print(item["name"])
            print(item["url"])

        # datas = {eat_item}



        return (json.dumps({"message":eat_item}),200)


if __name__ == "__main__":
	app.run(debug=True)