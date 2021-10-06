from jinja2 import Template
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from brandItems import googleFetch
from brandItems import returnItems
from brandItems import bingFetch
from brandItems import startDriver


app = Flask(__name__)
app.debug = True



@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():

    if request.form['submit_button'] == 'submit brand':
        brandName = request.form['brand']
        #brandIndustry = request.form['industry']
        print("select st")
        select = request.form.get('ind')
        print(str(select)) # just to see what select is
        print("select end")

        items = returnItems(str(select))
        allImages = []
        counter = 0

        
        for item in items:
            counter = counter + 1
            images = googleFetch(brandName, item)
            #images = googleFetch(brandName, item)
            allImages.append(images)
            if counter == 1:
                break
        template = Template("""
        <!DOCTYPE html>
        <html>
        <head>
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script type="text/javascript" src="/static/main.js" ></script>
        <script>
            var allImages = {{allImages}};
            var items = {{items}};
            const allImagesLength = allImages.length
            const itemsLength = items.length
        </script>
        </head>
        <body>







        <style>
        img {
            display: none;
        }
        img.active {
            display: block;
        }
        </style>
        </body>
        </html>

        """)
        return template.render(items=items, allImages = allImages)
    elif request.form['submit_button'] == 'submit custom item':
        brandName = request.form['brand name custom']
        #brandIndustry = request.form['industry']
        item = request.form.get('brand item custom')

        allImages = []

        images = googleFetch(brandName, item)
        #images = googleFetch(brandName, item)

        template = Template("""
        <!DOCTYPE html>
        <html>
        <body>

        <h1 style="text-align:center;">Brand Items</h1>
        <h3 style="text-align:center;">{{item}}</h3>
        <div style = "margin-bottom: 50px;  display: flex;justify-content: center;">
            <img src="{{ images[0] }}" alt="item" style="margin:5px;width: 15vw; min-width: 150px;margin-left: auto;margin-right: auto;  border: 5px solid #555;">

            <img src="{{ images[1] }}" alt="item" style="margin:5px;width: 15vw; min-width: 150px;margin-left: auto;margin-right: auto;border: 5px solid #555;">

            <img src="{{ images[2] }}" alt="item" style="margin:5px;width: 15vw; min-width: 150px;margin-left: auto;margin-right: auto;border: 5px solid #555;">

            <img src="{{ images[3] }}" alt="item" style="margin:5px;width: 15vw; min-width: 150px;margin-left: auto;margin-right: auto;border: 5px solid #555;">

            <img src="{{ images[4] }}" alt="item" style="margin:5px;width: 15vw; min-width: 150px;margin-left: auto;margin-right: auto;border: 5px solid #555;">
        </div>
        <hr size="1" width="70%" color="gray"> 

        
        </body>
        </html>

        """)
        return template.render(items=item, images = images)


    
    #print(template.render())
    return render_template("index.html")
    '''
    return render_template('index.html', item1_image1=allImages[0][0], item1_image2 = allImages[0][1], item1_image3=allImages[0][2], item1_image4=allImages[0][3], item1_image5=allImages[0][4],
                            item2_image1=allImages[1][0], item2_image2 = allImages[1][1], item2_image3=allImages[1][2], item2_image4=allImages[1][3], item2_image5=allImages[1][4],
                            item3_image1=allImages[2][0], item3_image2 = allImages[2][1], item3_image3=allImages[2][2], item3_image4=allImages[2][3], item3_image5=allImages[2][4],
                            item1=items[0],item2=items[1],item3=items[3])
    '''    

  

if __name__== '__main__':
    app.secret_key = "difficult"
    app.run()
