from flask import Blueprint, jsonify
from helper import helper

solutions = Blueprint('solutions', __name__)

@solutions.route('/projecteuler-python/api/<qno>')
def get_solution(qno):
    if qno == '1':
        answer = helper.get_solution_1()
        solution = jsonify({ "qno": 1, "answer": answer })
        return solution
    elif qno == '2':
        answer = helper.get_solution_2()
        solution = jsonify({ "qno": 2, "answer": answer })
        return solution
    else:
        return jsonify(results = { "qno": 0, "answer": 0 })
