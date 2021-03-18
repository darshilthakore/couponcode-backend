
# Coupon Code API
  

## Setting up the Project

  

- create a virtual environment to isolate package dependencies

```

darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$ python3 -m venv couponcode-env

darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$ source couponcode-env/bin/activate

(couponcode-env) darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$

```

- django project named `couponcode` is created and an app `api` is created as well. (This steps need not be performed again, as the project is already generated)

```

(couponcode-env) darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$ django-admin startproject couponcode

(couponcode-env) darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$ cd couponcode/

(couponcode-env) darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$ django-admin startapp api

```

Project structure is as follows:

  

```

-couponcode
  -couponcode
    -api
    -couponcode
    -db.sqlite3
    -manage.py
    -README.md
    -requirements.txt

```

  

- Install the required packages from requirements.txt

  
  

```

(couponcode-env) darshil@darshil-Inspiron-5555:~/Online Learning/couponcode$ pip3 install -r requirements.txt

```

- Now we have setup our project.

  

## Creating Models

- Inside the models.py file, we have defined our model **Coupon**

  

  

## Creating `serializers.py`

- now we create a serializers.py file inside our app api

- this will define a CouponSerializer


## Setting the views

  

- now inside the views.py file, the call to the routes `/coupons` and `/applycode` is handled

  

## Start the server

  

- start the django server

```

(couponcode-env) darshil@darshil-Inspiron-5555:~/Online Learning/couponcode/couponcode$ python3 manage.py runserver

Watching for file changes with StatReloader

Performing system checks...

  

System check identified no issues (0 silenced).
March 18, 2021 - 12:01:04
Django version 3.1.7, using settings 'couponcode.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
  

```

- open the link in the browser `http://127.0.0.1:8000/`

- You can now access the app at this link in your browser

- you can test the api in postman or in the browser itself
- Also check the available coupon codes from postman by referring the below mentioned api calls, also create any new coupon codes if needed through postman.

  

### GET /coupons

Request : GET /coupons

Response: 200 OK

```
[
    {
        "id": 1,
        "code": "NEW50",
        "start_date": "2021-01-01",
        "end_date": "2021-04-04",
        "coupon_type": "FLAT",
        "discount": 100.0,
        "maximum_discount": null
    },
    {
        "id": 2,
        "code": "JOY30",
        "start_date": "2021-01-01",
        "end_date": "2021-04-04",
        "coupon_type": "PERCENTAGE",
        "discount": 30.0,
        "maximum_discount": null
    },
    {
        "id": 3,
        "code": "ZOMATO30",
        "start_date": "2021-01-01",
        "end_date": "2021-02-02",
        "coupon_type": "PERCENTAGE",
        "discount": 30.0,
        "maximum_discount": null
    }
]



```
- format for start and end date is `yyyy-mm-dd`

### POST /coupons

Request : POST /coupons
Body: `{
    "code": "DIWALI50",
    "start_date": "2021-01-01",
    "end_date": "2021-02-02",
    "coupon_type": "PERCENTAGE",
    "discount": 50
}`
 

Response: 201 Created

```
{
    "id": 4,
    "code": "DIWALI50",
    "start_date": "2021-01-01",
    "end_date": "2021-02-02",
    "coupon_type": "PERCENTAGE",
    "discount": 50.0,
    "maximum_discount": null
}

```

### GET /applycode 

Request : GET /applycode?code=NEW50&amount=456

Response: 200 OK

```
{
    "total": 356.0,
    "discount": 100.0
}

```

### GET /applycode [Accessing coupon which doesn't exist]

Request : GET /applycode?code=DUMMY&amount=456

Response: 404 Not Found

```
{
    "msg": "Coupon Not found"
}

```

### GET /applycode [Accessing coupon which is expired]

Request : GET /applycode?code=ZOMATO30&amount=456

Response: 404 Not Found

```
{
    "msg": "Coupon Expired"
}
```