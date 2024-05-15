from flask import Flask, request, render_template
from user_agent import get_user_agenet_details
from geo_location import get_geolocation
app = Flask(__name__)

@app.route('/')
def home():
    target_keys = ('REMOTE_ADDR', 'HTTP_CLIENT_IP', 'HTTP_X_CLIENT_IP')
    param_values = {}
    for key in target_keys:
        param_values[key] = request.environ.get(key)
    
    ua_string = request.environ.get('HTTP_USER_AGENT')
    ua_details = get_user_agenet_details(ua_string)
    
    ip_v4_address = param_values.get('HTTP_CLIENT_IP') or '127.0.0.1'
    geo_details = get_geolocation(ip_v4_address)
    
    return render_template('click-details.html', param_values=param_values, ua_details=ua_details, geo_details=geo_details)

if __name__ == '__main__':
   app.run()