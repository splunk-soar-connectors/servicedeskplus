# Define your constants here

SDP_BACKFILL_DAYS = 7

SDP_TICKET_ARTIFACT_LABEL = "servicedeskplus_ticket"
SDP_TICKET_JSON_ID = "id"

SDP_DATA_CENTERS = {
    'United States': {
        'base_url': 'https://sdpondemand.manageengine.com',
        'oauth': 'https://accounts.zoho.com/oauth/v2/token'
    },
    'Europe': {
        'base_url': 'https://sdpondemand.manageengine.eu',
        'oauth': 'https://accounts.zoho.eu/oauth/v2/token'
    },
    'India': {
        'base_url': 'https://sdpondemand.manageengine.in',
        'oauth': 'https://accounts.zoho.in/oauth/v2/token'
    },
    'China': {
        'base_url': 'https://servicedeskplus.cn',
        'oauth': 'https://accounts.zoho.com.cn/oauth/v2/token'
    },
    'Australia': {
        'base_url': 'https://servicedeskplus.net.au',
        'oauth': 'https://accounts.zoho.com.au/oauth/v2/token'
    },
    'Japan': {
        'base_url': 'https://servicedeskplus.jp',
        'oauth': 'https://accounts.zoho.com.jp/oauth/v2/token'
    },
    'Canada': {
        'base_url': 'https://servicedeskplus.ca',
        'oauth': 'https://accounts.zoho.ca/oauth/v2/token'
    },
    'United Kingdom': {
        'base_url': 'https://servicedeskplus.uk',
        'oauth': 'https://accounts.zoho.uk/oauth/v2/token'
    }
}

REQUEST_FIELDS = ['subject', 'description', 'request_type', 'impact', 'status', 'mode', 'level', 'urgency', 'priority',
                  'service_category', 'requester', 'assets', 'site', 'group', 'technician', 'category', 'subcategory',
                  'item', 'email_ids_to_notify', 'is_fcr', 'resources', 'udf_fields', 'update_reason']

FIELDS_WITH_NAME = ['request_type', 'impact', 'status', 'mode', 'level', 'urgency', 'priority', 'service_category',
                    'requester', 'site', 'group', 'technician', 'category', 'subcategory', 'item']

SDP_API_VERSION = '/api/v3/'
API_GET_REQUESTS = f"{SDP_API_VERSION}requests"

# Constants relating to 'get_error_message_from_exception'
ERR_CODE_MSG = "Error code unavailable"
ERR_MSG_UNAVAILABLE = "Error message unavailable. Please check the asset configuration and|or action parameters."
PARSE_ERR_MSG = "Unable to parse the error message. Please check the asset configuration and|or action parameters."

# Constants relating to 'validate_integer'
SDP_VALID_INT_MSG = "Please provide a valid integer value in the {param}"
SDP_NON_NEG_NON_ZERO_INT_MSG = "Please provide a valid non-zero positive integer value in {param}"
SDP_NON_NEG_INT_MSG = "Please provide a valid non-negative integer value in the {param}"
SDP_START_INDEX_KEY = "'start_index' action parameter"
SDP_MAX_RESULTS_KEY = "'max_results' action parameter"
SDP_CONTAINER_COUNT_KEY = "'Maximum containers' configuration parameter"

# Constants relating to error messages
SDP_ERR_FETCHING_TICKET = "Error occurred while fetching ticket {ticket_id}: {error}"
SDP_ERR_FETCHING_TICKETS = "Error occurred while fetching tickets: {error}"
SDP_ERR_RETRIEVE_TICKETS = "Could not retrieve tickets"
SDP_ERR_INVALID_CONFIGURATION = "ServiceDesk Plus is [On-Premises]: please provide its Server URL"
SDP_ERR_NO_VALUE = "Could not extract value '{value}' from fetched requests."
SDP_ERR_NOT_IMPLEMENTED = "Integration with ManageEngine ServiceDesk Plus Cloud not available yet."

# JSON returned from ManageEngine
# SDP_JSON_ACCESS_TOKEN = "access_token"
SDP_JSON_LIST_INFO = "list_info"