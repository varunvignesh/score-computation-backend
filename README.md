# Score computation Backend

## Requirements

- Python 3.8.x
- flask 3.0.x

## Setup

1. Clone the repository

2. Create a virtual environment

   ```
   python3.8 -m venv ./venv
   ```

3. Activate the virtual environment

   ```
   source venv/bin/activate
   ```

4. Install the requirements

   ```
   pip install -r requirements.txt
   ```

5. Create a .env file and add the following variables from .env.example

6. Run the server

   ```
   python app.py
   ```

## Endpoints

**GET** **{base_url}/api/v1/accounts/<account_id>/products/<product_id>** - fetches the individual products by the account

### sample response

```
{
    "code": 200,
    "data": {
        "account_id": 1,
        "product_id": 1,
        "reference_product_id": "2800021730",
        "stock": "In Stock"
    },
    "message": "Products fetched successfully",
    "status": "SUCCESS"
}
```

**GET** **{base_url}/api/v1/accounts/<account_id>/score** - fetches the score of an account

### sample response

```
{
    "code": 200,
    "data": {
        "score": 0.5
    },
    "message": "Account score fetched successfully",
    "status": "SUCCESS"
}
```
