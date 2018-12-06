# Copyright (c) 2015 Pepijn Oomen <oomen@piprograms.com>
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
import requests
import json
from flask import Flask
application = Flask(__name__)

@application.route('/')
def accueil():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["ISO3166-1"="DE"][admin_level=2];
    (node["amenity"="biergarten"](area);
    way["amenity"="biergarten"](area);
    rel["amenity"="biergarten"](area);
    );
    out center;
    """
    response = requests.get(overpass_url, 
                            params={'data': overpass_query})
    data = response.json()
    return str(data)

if __name__ == '__main__':
    application.run(debug = True)
