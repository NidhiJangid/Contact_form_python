# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
#
# @app.route('/returnjson', methods=['GET','POST'])
# def ReturnJSON():
#     if (request.method == 'GET'):
#         data = {
#
#                 "name": "Nidhi jangid",
#                 "msg": "Type your msg here",
#                 "date": "Current date"
#         }
#         return jsonify(data)
#
# if __name__ == '__main__':
#     app.run(debug=True, port=89)