class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.model_validate(item)
                self.parsed_object = parsed_object
        else:
            schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self

    def get_parsed_objet(self):
        return self.parsed_object

    def __str__(self):
        return (
            f"\nStatus code: {self.response_status} \n"
            f"Requested url: {self.response.url} \n"
            f"Response body: {self.response_json}"
        )
