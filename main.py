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

def build_page(textarea_content):
    username_label= "<label>User Name:</label>"
    username_input = "<input type = 'text' name='username'/>"
    username_chunk = username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + username_input
    username_error = "<text-style = 'color:red'> Please input a valid username.</text>"

    password_label= "<label>Password:</label>"
    password_input = "<input type = 'password' name='password'/>"
    password_chunk = password_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;" + password_input

    repeatpw_label= "<label>Verify password:</label>"
    repeatpw_input = "<input type = 'password' name='repeatpw'/>"
    repeatpw_chunk = repeatpw_label + "&nbsp;&nbsp;" + repeatpw_input
    password_error: "<text-style = 'color:red'> Your passwords do not match.</text>"

    email_label= "<label>Email (Optional):</label>"
    email_input = "<input type = 'email' name='email'/>"
    email_chunk = email_label + "&nbsp;" + email_input
    email_error = "<text-style = 'color:red'> Please input a valid email.</text>"

    submit = "<input type = 'submit'/>""<br>"+

    clean_form = "<form method = 'post'>" + username_chunk + "<br>" + password_chunk + "<br>" + repeatpw_chunk + "<br>" + email_chunk + "<br>"+ submit + "</form>"
    username_error_form = "<form method = 'post'>" + username_label + "&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;" + username_input + username + username_error "<br>" + password_chunk + "<br>" + repeatpw_chunk + "<br>" + email_chunk + "<br>"+ submit + "</form>"
    password_mismatch_form = "<form method = 'post'>" + username_chunk + "<br>" + password_chunk + "<br>" + repeatpw_chunk + password_error + "<br>" + email_chunk + "<br>"+ submit + "</form>"
    invalid_email_form= "<form method = 'post'>" + username_chunk + "<br>" + password_chunk + "<br>" + repeatpw_chunk + "<br>" + email_label + "&nbsp;" + email_input + email + email_error + "<br>"+ submit + "</form>"

    header = "<h2>User Sign Up</h2>"
    return header + clean_form

def valid_username(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def valid_email (email):
    EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.usersignup.com/
    """

    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        content = build_page("")
        self.response.write(content)

class Form_Submitted(webapp2.RequestHandler):
    """ Handles requests coming in to '/submit'
        e.g. www.usersignup.com/submit
    """

    def post(self):
        username = self.request.get("username")
        escaped_user_name = cgi.escape(username)
        valid_username = valid_username(escaped_user_name)
        if valid_username == "":
            return header + username_error_form

        password = self.request.get("password")
        repeatpw = self.request.get("repeatpw")
        elif password != repeatpw:
            return header + password_mismatch_form

        email = self.request.get("email")
        elif email != "":
            and if valid_email(email)=="":
                return header + invalid_email_form

        else:
            return "<h2> Welcome  + valid_username + ! </h2>"

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/submit", Form_Submitted),
], debug=True)
