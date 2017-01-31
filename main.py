#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title> User SignUp </title>
    <style = "text/css">
        .error {
            color: red;
        }
    </style>
    </head>
    <body>
        <h1>
            <a href="/">User Sign Up</a>
        </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

def build_page(textarea_content):
    username_label= "<label>User Name:</label>"
    username_input = "<input type = 'message' name='username'/>"

    password_label= "<label>Password:</label>"
    password_input = "<input type = 'message' name='password'/>"

    repeatpw_label= "<label>Verify password:</label>"
    repeatpw_input = "<input type = 'message' name='repeatpw'/>"

    email_label= "<label>Email (Optional):</label>"
    email_input = "<input type = 'message' name='email'/>"

    submit = "<input type = 'submit'/>"
    form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + username_input +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + email_input + "<br>" + submit + "</form>"

    header = "<h2>User Sign Up</h2>"
    return header + form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
