from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


#todoid = address
#todo = COORDS

def abort_if_coord_doesnt_exist(address):
    if address not in ADDRESS:
        abort(404, message="ADDRESS {} doesn't exist".format(address))


parser = reqparse.RequestParser()
parser.add_argument('coordinates', action='append')


# For individual address
# class Coords(Resource):
    # def get(self, address):
    #     abort_if_coord_doesnt_exist(address)
    #     return COORDS[address]

    # def delete(self, address):
    #     abort_if_coord_doesnt_exist(address)
    #     del COORDS[address]
    #     return '', 204

    # def put(self, address):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     COORDS[address] = task
    #     return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class CoordsList(Resource):
    def get(self):
        return ADDRESS

    def post(self):
        args = parser.parse_args()
        for urg in args:
        	print "HELLOOOOOOOOOOOOO"
        	print urg;
        exit(0);
        address = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(CoordsList, '/coords')
# api.add_resource(Coords, '/coords/<address>')


if __name__ == '__main__':
    app.run(debug=True)





