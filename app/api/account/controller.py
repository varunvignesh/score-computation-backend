from app import cursor, jsonify, message, sqlite3


def get_account_product_details(account_id, product_id):
    """
        get the product details of a account
    """
        
    try:
        # fetch account_id from account_db
        cursor.execute("SELECT id FROM account_db WHERE id = ?", ([account_id]))

        account = cursor.fetchone()

        # not found error handling
        if account is None:
            return jsonify({
                'code': 404,
                'status': message.ERROR_STATUS,
                'message': message.ACCOUNT_NOT_FOUND
            }), 404
        
        # fetch all the data from product_db
        cursor.execute("SELECT * FROM product_db WHERE account_id = ? and id = ?", ([account_id, product_id]))
        
        records = cursor.fetchone()

        # not found error handling
        if records is None:
            return jsonify({
                'code': 404,
                'status': message.ERROR_STATUS,
                'message': message.PRODUCT_NOT_FOUND
            }), 404

        product_data = {
            "product_id": records[0],
            "account_id": records[1],
            "reference_product_id": records[2],
            "stock": records[3],
        }
        
        # success response
        return jsonify({
            'code': 200,
            'status': message.SUCCESS_STATUS,
            'data': product_data,
            'message': message.PRODUCTS_FETCH_SUCCESS
        })
    
    except sqlite3.Error as error:
        return jsonify({
            'code': 500,
            'status': message.ERROR_STATUS,
            'message': "Database error: {}".format(error)
        }), 500

def get_account_score(account_id):
    """
        get the product details of a account
    """
    try:
        # fetch account_id from account_db
        cursor.execute("SELECT id FROM account_db WHERE id = ?", ([account_id]))

        account = cursor.fetchone()

        # not found error handling
        if account is None:
            return jsonify({
                'code': 404,
                'status': message.ERROR_STATUS,
                'message': message.ACCOUNT_NOT_FOUND
            }), 404
        
        # Fetch total product count
        cursor.execute("SELECT count(id) as total_products FROM product_db WHERE account_id = ?", ([account_id]))
        
        total_product_count = cursor.fetchone()

        # Check for division by zero
        if total_product_count[0] == 0:
            availability_score = 0
        else:
            # Fetch total in-stock product count
            cursor.execute("SELECT count(id) as total_instock_products FROM product_db WHERE account_id = ? and stock = ?", ([account_id, "In Stock"]))
            
            total_instock_product_count = cursor.fetchone()

            # Calculate availability score
            availability_score= total_instock_product_count[0]/ total_product_count[0]
        
        # success response
        return jsonify({
            'code': 200,
            'status': message.SUCCESS_STATUS,
            'data': {
                'score': availability_score
            },
            'message': message.ACCOUNT_SCORE_FETCH_SUCCESS
        })
    
    except sqlite3.Error as error:
        return jsonify({
            'code': 500,
            'status': message.ERROR_STATUS,
            'message': "Database error: {}".format(error)
        }), 500
