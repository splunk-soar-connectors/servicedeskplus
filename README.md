[comment]: # "Auto-generated SOAR connector documentation"
# ServiceDeskPlus

Publisher: Splunk Inc.  
Connector Version: 1.0.1  
Product Vendor: ManageEngine  
Product Name: ServiceDeskPlus  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 6.1.1  

This App supports a variety of ticket management actions on ManageEngine ServiceDesk Plus

# Splunk> Phantom

Welcome to the open-source repository for Splunk> Phantom's servicedeskplus App.

Please have a look at our [Contributing Guide](https://github.com/Splunk-SOAR-Apps/.github/blob/main/.github/CONTRIBUTING.md) if you are interested in contributing, raising issues, or learning more about open-source Phantom apps.

## Legal and License

This Phantom App is licensed under the Apache 2.0 license. Please see our [Contributing Guide](https://github.com/Splunk-SOAR-Apps/.github/blob/main/.github/CONTRIBUTING.md#legal-notice) for further details.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a ServiceDeskPlus asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**data_centre** |  required  | string | ServiceDesk Plus Data Centre
**verify_server_cert** |  optional  | boolean | Verify server certificate
**base_url** |  optional  | string | [On-Premises] ServiceDesk Plus Server URL (e.g. https://manageengine.onprem.local)
**technician_key** |  required  | password | API Key used to authenticate

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[on poll](#action-on-poll) - Ingest tickets from ServiceDeskPlus  
[delete ticket](#action-delete-ticket) - Delete ticket (request)  
[create ticket](#action-create-ticket) - Create a ticket (request)  
[update ticket](#action-update-ticket) - Update ticket (request)  
[get ticket resolution](#action-get-ticket-resolution) - Get a resolution of the ticket (request)  
[set ticket resolution](#action-set-ticket-resolution) - Add/Update a resolution of the ticket (request)  
[list linked tickets](#action-list-linked-tickets) - Get all linked tickets under a ticket (request)  
[assign ticket](#action-assign-ticket) - Assign a ticket (request)  
[close ticket](#action-close-ticket) - Close a ticket (request)  
[list tickets](#action-list-tickets) - List tickets present in ServiceDesk Plus  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'on poll'
Ingest tickets from ServiceDeskPlus

Type: **ingest**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start_time** |  optional  | Parameter ignored in this app | numeric | 
**end_time** |  optional  | Parameter ignored in this app | numeric | 
**container_id** |  optional  | Parameter ignored in this app | string | 
**container_count** |  optional  | Maximum number of tickets to be ingested during poll now | numeric | 
**artifact_count** |  optional  | Parameter ignored in this app | numeric | 

#### Action Output
No Output  

## action: 'delete ticket'
Delete ticket (request)

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.request_id | numeric |  |  
action_result.data | string |  |  
action_result.status | string |  |   success  failed 
action_result.data.\*.response_status.messages.\*.message | string |  |  
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'create ticket'
Create a ticket (request)

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**fields** |  required  | JSON containing field values | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.fields | string |  |   {"field_name_1": "field_value_1", "field_name_2": "field_value_2"} 
action_result.data.\*.response_status.messages.\*.message | string |  |  
action_result.data.\*.request.id | numeric |  |   150 
action_result.summary.new_request_id | numeric |  |   125 
action_result.message | string |  |   Successfully created a new request 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'update ticket'
Update ticket (request)

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 
**fields** |  required  | JSON containing field values | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.fields | string |  |   {"severity": 1, "description": "User, what are you doing"} 
action_result.parameter.request_id | numeric |  |   1514128723865219 
action_result.data.\*.response_status.messages.\*.message | string |  |  
action_result.data.\*.request.id | numeric |  |   1514128723865219 
action_result.data.\*.request.subject | string |  |  
action_result.data.\*.request.status.name | string |  |   Open 
action_result.data.\*.request.update_reason | string |  |   The request is updated for this reason 
action_result.summary | string |  |  
action_result.message | string |  |   Successfully updated ticket 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'get ticket resolution'
Get a resolution of the ticket (request)

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.request_id | numeric |  |  
action_result.data.\*.response_status.messages.\*.message | string |  |  
action_result.data.\*.resolution.content | string |  |  
action_result.data.\*.resolution.submitted_by.id | numeric |  |  
action_result.data.\*.resolution.submitted_by.name | string |  |  
action_result.data.\*.resolution.submitted_by.email_id | string |  |  
action_result.data.\*.resolution.submitted_on.display_value | string |  |   Oct 4, 2017 12:21 AM 
action_result.data.\*.resolution.attachments.\*.id | string |  |  
action_result.data.\*.resolution.submitted_on.value | string |  |   1507056660521 
action_result.message | string |  |   Successfully fetched the resolution for the given request 
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'set ticket resolution'
Add/Update a resolution of the ticket (request)

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 
**content** |  required  | Resolution description | string | 
**add_to_linked_requests** |  optional  | Add resolution to linked tickets | boolean | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.request_id | numeric |  |  
action_result.parameter.content | string |  |  
action_result.parameter.add_to_linked_requests | boolean |  |  
action_result.data.\*.response_status.messages.\*.message | string |  |  
action_result.data.\*.response_status.status | string |  |  
action_result.message | string |  |   Successfully added the resolution for the given request 
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list linked tickets'
Get all linked tickets under a ticket (request)

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.request_id | numeric |  |  
action_result.data.\*.link_requests.\*.linked_request.comments | string |  |  
action_result.data.\*.response_status.messages.\*.message | string |  |  
action_result.data.\*.link_requests.\*.linked_request.subject | string |  |  
action_result.data.\*.link_requests.\*.linked_request.id | numeric |  |  
action_result.message | string |  |   Successfully fetched the linked requests 
summary.total_objects | numeric |  |   1 
action_result.summary.num_linked_tickets | numeric |  |   21 
summary.total_objects_successful | numeric |  |   1   

## action: 'assign ticket'
Assign a ticket (request)

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 
**fields** |  required  | JSON containing field values | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.request_id | numeric |  |  
action_result.parameter.fields | string |  |   {"field_name_1": "field_value_1", "field_name_2": "field_value_2"} 
action_result.data.\*.status | string |  |  
action_result.data.\*.messages.\*.message | string |  |  
action_result.message | string |  |   Successfully assigned the request 
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'close ticket'
Close a ticket (request)

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** |  required  | Ticket ID | numeric | 
**requester_ack_resolution** |  optional  | Has requester acknowledged the resolution? | boolean | 
**requester_ack_comments** |  optional  | Comments | string | 
**closure_comments** |  optional  | Ticket closure comments | string | 
**closure_code** |  optional  | Ticket closure code | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.request_id | numeric |  |  
action_result.parameter.requester_ack_resolution | boolean |  |   True  False 
action_result.parameter.requester_ack_comments | string |  |   Mail fetching is up and running now 
action_result.parameter.closure_comments | string |  |   Reset the pasword solved the issue 
action_result.parameter.closure_code | string |  |   Canceled  Failed  Moved  Postponed  Success  Unable to reproduce 
action_result.data.\*.status | string |  |  
action_result.data.\*.messages.\*.message | string |  |  
action_result.message | string |  |   Successfully assigned the request 
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'list tickets'
List tickets present in ServiceDesk Plus

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**start_index** |  optional  | Index of the first ticket that should be returned | numeric | 
**row_count** |  optional  | Number of rows that should be returned | numeric | 
**search_fields** |  optional  | Search for the specific fields in the tickets | string | 
**filter_by** |  optional  | Filter to apply to the returned tickets | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.start_index | numeric |  |   5 
action_result.parameter.row_count | numeric |  |   5 
action_result.parameter.search_fields | string |  |   {"field1": value, "field2": value} 
action_result.parameter.filter_by | string |  |   {"name":"My_Open"} 
action_result.data.\*.is_service_request | boolean |  |   True  False 
action_result.data.\*.status.name | string |  |   Open 
action_result.data.\*.cancel_requested_is_pending | boolean |  |  
action_result.data.\*.subject | string |  |  
action_result.data.\*.created_by.email_id | string |  |   testuser2@test.testdata.com 
action_result.data.\*.created_time.display_value | string |  |   Jan 26, 2024 05:51 AM 
action_result.data.\*.short_description | string |  |  
action_result.data.\*.due_by_time.display_value | string |  |   Jan 26, 2024 10:00 AM 
action_result.data.\*.id | numeric |  `servicedeskplus intelligence id`  |   53702579051 
action_result.data.\*.priority.id | numeric |  |   1  4 
action_result.message | string |  |  
action_result.summary | string |  |  
action_result.summary.num_tickets | numeric |  |   21 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 