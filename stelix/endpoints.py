'''List of all endpoints Stelix knows about.'''

ROOT = 'https://dev.sellix.io/v1'
API_PATH  = {
    'order'             : ROOT + '/orders',
    'coupon'            : ROOT + '/coupons',
    'products'          : ROOT + '/products',
    'feedback'          : ROOT + '/feedback',
    'blacklists'        : ROOT + '/blacklists',
    'categories'        : ROOT + '/categories',

    # Generic Endpoints

    'queries'           : ROOT + '/queries',
    'queries-reply'     : ROOT + '/queries/reply',
    'queries-close'     : ROOT + '/queries/close',
    'queries-reopen'    : ROOT + '/queries/reopen',

    # Specific Query Endpoints
}
API_DATA = {
    'categories': {
        'title': 1,
        'unlisted': 0,
        'sort_priority': 0,
        'products_bound': 0
    },
    'blacklists': {
        'type': 1,
        'data': 1,
        'note': 0
    },
    'feedback': {
        'reply': 1
    },
    'products': {
        'title': 1,
        'description': 1,
        'price': 1,
        'gateways': 1,
        'type': 1,
        'discount_value': 1,
        'currency': 0,
        'quantity': 0,
        'stock_delimiter': 0,
        'serials': 0,
        'serials_remove_duplicates': 0,
        'delivery_text': 0,
        'service_text': 0,
        'stock': 0,
        'custom_fields': 0,
        'crypto_confirmations_needed': 0,
        'max_risk_leve': 0,
        'block_vpn_proxies': 0,
        'sort_priority': 0,
        'unlisted': 0,
        'terms_of_service': 0,
        'warranty': 0,
        'warranty_text': 0,
        'private': 0,
        'webhooks': 0
    },
    'coupon': {
        'code': 1,
        'discount_value': 1,
        'max_uses': 0,
        'products_bound': 0
    },
    'queries-reply': {
        'reply': 1
    }
}
