# For-Teams.pw
Using the API, you can upload a product, as well as view information about the catalog and products. Inside this directory, you can get examples of using all API methods, in Python.

## Authorization
Authorization goes with the help of a token consisting of 48 characters, this token can be obtained inside the telegram bot. The token is used for every request. Example:

`GET: http://marketwain.com/users/?apikey=yVkkbrhJcat1b8wKnrbsFDKGYngTwdWy5VWZjeu9Fs0z7DOd`
    
### API Base URI
`http://marketwain.com`
### Method
- GET
- POST
- PUT

### Rate Limited
 - default request - 100 in 60 sek
 - check sub/product - 25 in 3600 sek

#### Responses 422


    {
      "detail": [
        {
          "loc": [
            "string",
            0
          ],
          "msg": "string",
          "type": "string"
        }
      ]
    }


## Users

### GET `/users`

Personal information

#### Successful Response

    {
      "id": 0,
      "username": "string",
      "lolz": "string",
      "status": 0,
      "baned": 0,
      "balance": 0,
      "joining_date": "2022-10-18T17:31:57.462Z"
    }
Parameters:

 * apikey (required): Your key that you received inside the telegram bot

### PUT `/users/refresh_apikey`

Allows you to reissue your private key

#### Successful Response

    {
      "apikey": "",
    }
Parameters:

 * apikey (required): Your key that you received inside the telegram bot

## Product

### POST `/products/`

You can upload your own files. If there was a successful download, you can get the session ID, you can track the status of the check by it, at the end of the check, the bot will send you a notification
#### Correct file structure(Exemple):
```
└───My_log.zip(400mb)
	└───BR82F66B30B8764BD732C7665B4F7CBBB1_2022_09_11T05_01_26_712597(dict)
	│	└──Cookies
	│   	├───Google_[Chrome]_Default Network.txt
	│   	├───Google_[Chrome]_Profile 3 Network.txt
	│   	└───Microsoft_[Edge]_Default Network.txt
	
```	
#### Successful Response


    {
      "id": "",
      "owner_id": 0,
      "message": "to check status use products/status/{id}"
    }
Parameters:
    
 * apikey (required)(query): Your key that you received inside the telegram bot 
 * load_file (required)(body): Your log, byte string

### GET `/products/{product_id}`

You can get information about a product by its id

#### Successful Response

    {
      "id": "string",
      "owner_id": 0,
      "activity": 0,
      "creating_date": "2022-10-18T17:56:06.123Z",
      "sub_products": []
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * product_id (required)(path): Product ID, not session

### GET `/products/sub/{sub_product_id}`

Each product contains sub products, you can get information about the sub product by its id

#### Successful Response

    {
      "id": "string",
      "product_id": "string",
      "service": "string",
      "price": 0,
      "activity": 0,
      "creating_date": "2022-10-18T17:58:49.212Z",
      "data": {}
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * sub_product_id (required)(path): Sub product ID, not product
 
### GET `/products/status/{session_id}`

During the verification, you can find out the status, the verification status is stored for 48 hours, after which it will be lost

#### Successful Response

    {
      "id": "",
      "owner_id": 0,
      "status": "",
      "message": ""
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * session_id (required)(path): session id, obtained when loading a product

### GET `/products/check/{id_}`

You can check the product for validity, we remind you that the limit is 25 requests per hour

#### Successful Response

    {
        "status": "",
        "count_un_valid": 0,
        "count_valid": 0
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * id_ (required)(path):  product/sub product id

### POST `/products/buy/{id_}`

You can make a purchase, id_ can be either a product id or a product id. Please note that the product is not tested before purchase, you must submit a request yourself.

#### Successful Response

    {
    "string(bytes)"
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * id_ (required)(path): product/sub product id

## Catalog

### GET `/catalog/`

View product catalog

#### Successful Response

    {
      "totalProducts": 0,
      "products": []
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * skip (optional)(query): Zero product pass
 * limit (optional)(query): Maximum number of products received
 * my_product (opetional)(query): Boolean value, if specified, the user's products will be returned

### GET `/catalog/{service_id}`

Browse the catalog for individual services, that is, under products

#### Successful Response

    {
      "totalProducts": 0,
      "sub_products": []
    }
Parameters:

 * apikey (required)(query): Your key that you received inside the telegram bot
 * service_id (required)(path): Service you want to view
 * skip (optional)(query): Zero product pass
 * limit (optional)(query): Maximum number of products received
 * You can pass any filters suitable for this service, the list of filters can be obtained:
 `/catalog/filter/{service_id}`

## That's all, if you have any questions, feel free to contact the bot support, we will be happy to help you set everything up
