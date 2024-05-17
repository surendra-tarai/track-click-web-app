from flask import Flask, request, render_template
from user_agent import get_user_agenet_details
from geo_location import get_geolocation
app = Flask(__name__)


@app.route('/')
def home():
    target_keys = (('HTTP_CLIENT_IP', 'IPv4'), ('HTTP_X_CLIENT_IP', 'IPv4 (If Proxy)'))
    param_values = {}
    for key, label in target_keys:
        param_values[label] = request.environ.get(key)

    ua_string = request.environ.get('HTTP_USER_AGENT')
    ua_details = get_user_agenet_details(ua_string)
    other_details = {}
    
    other_details['Referrer'] = request.referrer or 'Direct'
    other_details['UA String'] = ua_string

    device = ua_details.get('device', {})
    device['device_type'] = 'Unknown'
    if device.get('is_mobile'):
        device['device_type'] = 'Mobile'
    elif device.get('is_tablet'):
        device['device_type'] = 'Tablet'
    elif device.get('is_pc'):
        device['device_type'] = 'Computer'
    ua_details['device'] = device
    print(ua_details)
    ipv4_address = param_values.get('HTTP_CLIENT_IP')
    if ipv4_address:
        ipv4_address = ipv4_address.split(':')[0]
        param_values['HTTP_CLIENT_IP'] = ipv4_address

    ip_v4_address = ipv4_address or '127.0.0.1'
    geo_details = get_geolocation(ip_v4_address)

    return render_template('click-details-2.html', param_values=param_values, ua_details=ua_details, geo_details=geo_details, other_details=other_details)


if __name__ == '__main__':
    app.run()
