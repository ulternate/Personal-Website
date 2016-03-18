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

from BaseHandler import BaseHandler
import webapp2

TEMPLATE_ROOT_PATH = 'static/templates/'
        
class MainPage(BaseHandler):
  	
    def get(self):
      	self.write_template(TEMPLATE_ROOT_PATH + 'index.html', None)

# Currently 301 redirecting the old site structure to the main page as these old links are still showing in Google Search Results.
application = webapp2.WSGIApplication([webapp2.Route('/contact', webapp2.RedirectHandler, defaults={'_uri':'http://www.danielcswain.com'}),
                                       webapp2.Route('/resume', webapp2.RedirectHandler, defaults={'_uri':'http://www.danielcswain.com'}),
                                       webapp2.Route('/photos', webapp2.RedirectHandler, defaults={'_uri':'http://www.danielcswain.com'}),
                                       webapp2.Route('/projects', webapp2.RedirectHandler, defaults={'_uri':'http://www.danielcswain.com'}),
                                       ('/', MainPage)], debug=False)

