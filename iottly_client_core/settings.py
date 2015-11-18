"""

Copyright 2015 Stefano Terna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import os
import pytz


TIMEZONE = pytz.timezone(pytz.country_timezones['it'][0])

# python iso format stringtom
TIME_FMT = "%Y-%m-%dT%H:%M:%S"


# Tornado specific settings, see http://www.tornadoweb.org/en/stable/web.html#tornado.web.Application.settings
static_path = os.path.join("/iottly_client_UI", "static")
template_path = os.path.join("/iottly_client_UI", "templates")
debug = True


try:
    from localsettings import *
except ImportError:
    pass

