from flask import Flask

FAI=Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return'This is my First view of Flask'


@FAI.route('/secondstringResponse')
def secondstringResponse():
    return'This is my Second view of Flask'


if __name__=='__main__':
    FAI.run(debug=True)