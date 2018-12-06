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
    mots = ["bonjour", "à", "toi,", "visiteur."]
    puces = ''.join("<li>{}</li>".format(m) for m in mots)
    return """<!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8" />
                <title>{titre}</title>
            </head>
        
            <body>
                <h1>{titre}</h1>
                <ul>
                    {puces}
                </ul>
            </body>
        </html>""".format(titre="Bienvenue !", puces=puces)

if __name__ == '__main__':
    application.run(debug = True)
