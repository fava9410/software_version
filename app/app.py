from packaging import version
from packaging.version import InvalidVersion
from flask import Flask, jsonify, request, abort, Response
import re

app = Flask(__name__)

EQUAL = 'equal'
BEFORE = 'before'
AFTER = 'after'
STRING_RESPONSE = '"%s" is %s "%s"'

def compare(version_1, version_2):
    if version_1 < version_2:
        comparison = BEFORE
    elif version_1 > version_2:
        comparison = AFTER
    else:
        comparison = EQUAL
    
    return comparison

@app.route('/check_versions', methods=['GET'])
def check_versions():
    """
    This endpoint validates software version using packaging.version lib,
    it supports with letters even. For more information please check
    https://www.python.org/dev/peps/pep-0440/
    """
    if request.json == None:
        abort(400, 'no parameters')

    if 'version_1' in request.json and 'version_2' in request.json:
        version_1 = request.json.get('version_1')
        version_2 = request.json.get('version_2')
    else:
        abort(400, 'missing parameters')

    # check versions format
    try:
        version.Version(version_1)
        version.Version(version_2)
        version_1 = version.parse(version_1)
        version_2 = version.parse(version_2)
    
    except InvalidVersion:
        abort(400, 'format error')

    comparison = compare(version_1, version_2)

    return jsonify({'comparison': STRING_RESPONSE % (version_1, comparison, version_2)})

@app.route('/check_versions_basic', methods=['GET'])
def check_versions_basic():
    """
    This endpoint validates software version only in the next format:
    "int.int.int", it parses input strings to tuples for comparison.
    """

    if request.json == None:
        abort(400, 'no parameters')

    if 'version_1' in request.json and 'version_2' in request.json:
        version_1 = request.json.get('version_1')
        version_2 = request.json.get('version_2')
    else:
        abort(400, 'missing parameters')

    # check format with a regular expression
    format_regex = '^\d{1,5}(?:\.\d{1,5}){0,2}$'
    format_error = False

    if re.search(format_regex, version_1) == None or re.search(format_regex, version_2) == None:
        format_error = True

    if format_error:
        abort(400, 'format error')

    version_1_tuple = tuple(int(x) for x in version_1.split('.'))
    version_2_tuple = tuple(int(x) for x in version_2.split('.'))

    comparison = compare(version_1_tuple, version_2_tuple)

    return jsonify({'comparison': STRING_RESPONSE % (version_1, comparison, version_2)})

