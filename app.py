from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr
    
    return f'Home Page <br> <br> Your IP address: {ip_address}'

if __name__ == '__main__':
   app.run()