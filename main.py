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
import re

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

def  valid_username (username)
    USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        username_label= "<label>User Name:</label>"
        username_input = "<input type = 'message' name='username'/>"

        password_label= "<label>Password:</label>"
        password_input = "<input type = 'password' name='password'/>"

        repeatpw_label= "<label>Verify password:</label>"
        repeatpw_input = "<input type = 'password' name='repeatpw'/>"

        email_label= "<label>Email (Optional):</label>"
        email_input = "<input type = 'message' name='email'/>"

        submit = "<input type = 'submit'/>"
        clean_form = "<form method = 'get'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + username_input +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + email_input + "<br>" + submit + "</form>"

        header = "<h2>User Sign Up</h2>"
        return header + form
    self.response.write(content)

    def post(self):
            # look inside the request to figure out what the user typed
        user_name = self.request.get("username")
        escaped_user_name = cgi.escape(user_name)

        password = self.request.get("password")
        repeatpw = self.request.get("repeatpw")

        email = self.request.get("email")
        escaped_email = cgi.escape(email)


        if escaped_user_name == "":
            nousername_error =  "Please enter a username."
            nousername_form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + escaped_user_name + nousername_error +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + escaped_email + "<br>" + submit + "</form>"
            return nousername_form

        elif valid_username(escaped_user_name)=="":
            invalid_username_error = "Please enter a username using only alphanumerics."
            invalid_username_form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + escaped_user_name + invalid_username_error +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + escaped_email + "<br>" + submit + "</form>"
            return invalid_username_form

        elif valid_email (escaped_email) =="":
            invalid_email_error = "Please enter an email using only alphanumerics."
            invalid_email_form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + escaped_user_name +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + escaped_email + invalid_email_error + "<br>" + submit + "</form>"
            return invalid_email_form

        elif repeatpw != password:
            password_match_error = "Your passwords do not match."
            password_mismatch_form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + escaped_user_name +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + escaped_email + invalid_email_error + "<br>" + submit + "</form>"
            return password_mismatch_form

        elif password == ""
            no_password_error = "Your passwords do not match."
            no_password_form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + escaped_user_name +"<br>"+ password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;"  + password_input + "<br>"+ repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input + "<br>" + email_label + "&nbsp;" + escaped_email + invalid_email_error + "<br>" + submit + "</form>"
            return no_password_form

        else:
            return "Welcome, " + escaped_user_name

    self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
