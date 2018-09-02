from flask import Flask
from flask_restful import Resource, Api
from alien_dictionary import AlienTranslator

app = Flask(__name__)
api = Api(app)

temp_nonce = b'\xca\xdd%\x9b\x15\xc9\x19\xbc/\xacQ\xc7\xc1\xf6\xaf\xca'
temp_key = b'\nk\xb5\xa4/\xe2\xabJw\xa3\x85$v\xc2\xa7\x16\x17\xcbI\xd2}\xc6\x87\xd4\xd1o\xbf\x08("2\xce'

m2e_dic = {0: "[微笑]", 1: "[色]", 2: "[坏笑]", 3: "[悠闲]", 4: "/::P", 5: "/:8-)", 6: "/:B-)", 7: "/:,@!", 8: "/:heart",
           9: "/:ladybug", 10: "/::*", 11: "/:coffee", 12: "/:basketb", 13: "/:@>", 14: "/:<@", 15: "/:beer"}


translator = AlienTranslator(m2e_dic, temp_key, temp_nonce)


class Student(Resource):
    def get(self, name):
        return {'student': translator.encrypt_to_code(name)}


api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)
