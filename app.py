from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr
    
    ipv4_address = request.access_route[0] if request.access_route else None
    ipv6_address = request.access_route[1] if len(request.access_route) > 1 else None

    return f"""
                Home Page <br> <br> 
                Your IP address: {ip_address} <br> <br> 
                Your ipv4_address: {ipv4_address} <br> <br> 
                Your ipv6_address: {ipv6_address} <br> <br> 
            """

if __name__ == '__main__':
   app.run()