from flask import Flask, jsonify, request
from ssh_util import ssh_connect


app = Flask(__name__) # create an instance of Flask class


if __name__ == "__main__":
    command_to_execute = "ls"  # Replace with any command you want to execute remotely

    output = ssh_connect(command_to_execute)
    print(output)


if __name__ == '__main__':
    app.run(debug=True)