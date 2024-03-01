import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import list_orders, retrieve_order, add_order, delete_order, update_metal, list_metals


class JSONServer(HandleRequests):
    """server class to handle incoming http requests for kneel diamonds"""
    def do_GET(self):
        """Handle GET requests from a client"""
        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"]!=0:
                response_body = retrieve_order(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
                
            response_body = list_orders(url)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        elif url["requested_resource"] == "metals":
            if url["pk"] !=0:
                response_body = "this works"
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            response_body = list_metals()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        else: "It's broken"
        
    def do_POST(self):
        """Handle POST requests from a client"""

        url=self.parse_url(self.path)
        pk=url["pk"]

        content_len = int(self.headers.get('content-length',0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "orders":
            if pk == 0:
                successfully_added = add_order(request_body)
                if successfully_added:
                    return self.response("", status.HTTP_201_SUCCESS_CREATED.value)
            
        return self.response("Requested Resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_PUT(self):
        """Handle PUT requests"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            if pk != 0:
                successfully_updated = update_metal(pk, request_body)
                if successfully_updated:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        
        return self.response("requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
    


    def do_DELETE(self):
        """Handle DELETE requests from client"""

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"]== "orders":
            if pk != 0:
                successfully_deleted = delete_order(pk)
                if successfully_deleted:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else: self.response("not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)


def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()