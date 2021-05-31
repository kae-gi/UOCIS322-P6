from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class listAll(Resource):
    def get(self, dtype):
        topk = request.args.get('top',-1)
        if dtype == 'csv':
            return csv_form()
        return json_form()

# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll/<string:dtype>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
