import psycopg2
import geojson

# Database connection parameters
db_params = {
    'dbname': 'Test',          # Database name
    'user': 'postgres',
    'password': 'example@2024',
    'host': 'localhost',
    'port': '5432'
}

# Query to fetch data (replace 'your_table' with your actual table name 'locations')
query = """
SELECT id, ST_AsGeoJSON(geom) as geom, name, description
FROM locations;
"""

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Execute the query
cur.execute(query)
rows = cur.fetchall()

# Create GeoJSON features
features = []
for row in rows:
    feature = geojson.Feature(
        geometry=geojson.loads(row[1]),
        properties={"id": row[0], "name": row[2], "description": row[3]}
    )
    features.append(feature)

# Create a GeoJSON FeatureCollection
feature_collection = geojson.FeatureCollection(features)

# Save the GeoJSON data to a file
with open('data.geojson', 'w') as f:
    geojson.dump(feature_collection, f)

# Close the database connection
cur.close()
conn.close()
