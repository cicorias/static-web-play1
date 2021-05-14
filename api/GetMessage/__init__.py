import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # return func.HttpResponse(json.dumps({"message": f"Hello, {name}. This HTTP triggered function executed successfully."}))
        return return_response(to_dict("message", f"Hello, {name}."))
    else:
        return return_response(to_dict("message", "no name passed but hello anyway"))

def return_response(object: dict, status_code:int = 200) -> func.HttpResponse:
    return func.HttpResponse(json.dumps(object), headers={"content-type": "application/json"}, status_code=status_code)

def to_dict(root_node: str, message: str) -> dict:
    return {root_node: message}