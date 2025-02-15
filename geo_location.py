import geoip2.database

DB_FILE_PATH = 'databases/GeoLite2-City.mmdb'

# Load the GeoLite2 database
reader = geoip2.database.Reader(DB_FILE_PATH)  # Path to your database file

# Function to get geolocation data from IP address
def get_geolocation(ip_address):
    geolocation_data = {}
    try:
        response = reader.city(ip_address)
        # Extract geolocation data
        
        geolocation_data = {
            'country': response.country.name,
            'country_code': response.country.iso_code,
            'city': response.city.name,
            'latitude (approximate)': response.location.latitude,
            'longitude (approximate)': response.location.longitude,
        }
        
    except Exception as e:
        geolocation_data['error'] = str(e)
    finally:
        return geolocation_data

# Example usage
# ip_address = '122.172.83.160'  # Replace with the actual IP address
# geolocation_data = get_geolocation(ip_address)

# print(geolocation_data)
