#!/usr/bin/env python
# Copyright 2010 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class HTTPArchive(dict):
  """Keys are HTTPRequest objects and values are responses."""
  pass


class HTTPRequest(object):
  def __init__(self, host, path, request_body):
    self.host = host
    self.path = path
    self.request_body = request_body

  def __key__(self):
    return self.host, self.path, self.request_body
