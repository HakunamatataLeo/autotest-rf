from HttpLibrary import HTTP

class JsonLib(object):

    def load_json_data_from_file(self, filepath):
        """ Don't forget to document the keyword!!!
        """
        json_string = open(filepath).read()
        HTTP().should_be_valid_json(json_string)
        return json_string
