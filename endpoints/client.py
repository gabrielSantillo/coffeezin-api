from flask import request, make_response
from apihelpers import check_endpoint_info, organize_client_response
import json
from dbhelpers import run_statement

def post():
    is_valid = check_endpoint_info(request.json, ['email'])
    if(is_valid != None):
        return make_response(json.dumps(is_valid, default=str), 400)

    results = run_statement('CALL add_client(?)', [request.json.get('email')])

    if(type(results) == list and len(results) != 0):
        return make_response(json.dumps(results[0], default=str), 200)
    else:
        return make_response(json.dumps("Sorry, an error has occured.", default=str), 500)
    
def get():
    results = run_statement('CALL get_all_clients()')
    
    if(type(results) == list and len(results) != 0):
        results = organize_client_response(results)
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps('Sorry, an error has occurred.', default=str), 500)