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
import caesar
import cgi

form = """
    <form method="post">
        <textarea name="message" value="%(encrypt_text)s">
        <br>
        <label> Amount to Rotate
            <input type="text" name="rotate_amount" value="%(rotate_amount)s">
        </label>
        <input type="submit">
    </form>
"""

def build_page(message=""):
        header = "<h2>Web Caesar</h2>"

        rot_label = "<label>Rotate by: </label>"
        rotation_input = "<input type='number' name='rotation'/>"

        message_label = "<label>Message: </label>"
        textarea = "<textarea name='message'>" + message + "</textarea>"

        submit = "<input type='submit'>"

        form = ("<form method='post'>" +
                rot_label + rotation_input + "<br>" +
                message_label + textarea + "<br>" +
                submit + "</form>")

        return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(build_page())

    def post(self):
        message = self.request.get("message")

        rotation_text = self.request.get("rotation")
        if len(rotation_text) > 0:
            rotation = int(rotation_text)
        else:
            rotation = 0

        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        self.response.write(build_page(escaped_message))


    # def write_form(self, error="", encrypt_text=""):
    #     self.response.out.write(form % {"error": error,
    #                                     "month": month,
    #                                     "day": day,
    #                                     "year": year})
    #
    # def get(self):
    #     #self.response.write(form)
    #     self.write_form()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
