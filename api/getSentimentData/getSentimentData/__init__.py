import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    topic = req.params.get('topic')
    if not topic:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            topic = req_body.get('topic')

    if topic:
        payload = json.dumps({'topic' : topic, "version": 1})
        return func.HttpResponse(payload)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a topic  in the query string or in the request body for a personalized response.",
             status_code=200
        )