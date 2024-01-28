from app import app
from app.api.account import controller
from app.helpers import localization as message


# Mount routes
app.add_url_rule(
    '/api/v1/accounts/<int:account_id>/products/<int:product_id>', view_func=controller.get_account_product_details, methods=['GET'])

app.add_url_rule(
    '/api/v1/accounts/<int:account_id>/score', view_func=controller.get_account_score, methods=['GET'])