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

from flask import Flask
application = Flask(__name__)

@application.route('/')
def accueil():
    r = requests.get('https://www.openstreetmap.org/api/capabilities')
    return """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>API</title>
            </head>
        
            <body>
                <h1>{resultat}</h1>
            </body>
        </html>""".format(resultat=r)

if __name__ == '__main__':
    application.run(debug = True)
