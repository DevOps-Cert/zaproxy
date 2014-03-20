# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright the ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This file was automatically generated.
"""

class spider(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def status(self):
        return self.zap._request(self.zap.base + 'spider/view/status/').get('status')

    @property
    def results(self):
        return self.zap._request(self.zap.base + 'spider/view/results/').get('results')

    @property
    def excluded_from_scan(self):
        return self.zap._request(self.zap.base + 'spider/view/excludedFromScan/').get('excludedFromScan')

    @property
    def option_max_depth(self):
        return self.zap._request(self.zap.base + 'spider/view/optionMaxDepth/').get('MaxDepth')

    @property
    def option_scope_text(self):
        return self.zap._request(self.zap.base + 'spider/view/optionScopeText/').get('ScopeText')

    @property
    def option_scope(self):
        return self.zap._request(self.zap.base + 'spider/view/optionScope/').get('Scope')

    @property
    def option_thread_count(self):
        return self.zap._request(self.zap.base + 'spider/view/optionThreadCount/').get('ThreadCount')

    @property
    def option_post_form(self):
        return self.zap._request(self.zap.base + 'spider/view/optionPostForm/').get('PostForm')

    @property
    def option_process_form(self):
        return self.zap._request(self.zap.base + 'spider/view/optionProcessForm/').get('ProcessForm')

    @property
    def option_skip_url_string(self):
        return self.zap._request(self.zap.base + 'spider/view/optionSkipURLString/').get('SkipURLString')

    @property
    def option_request_wait_time(self):
        return self.zap._request(self.zap.base + 'spider/view/optionRequestWaitTime/').get('RequestWaitTime')

    @property
    def option_user_agent(self):
        return self.zap._request(self.zap.base + 'spider/view/optionUserAgent/').get('UserAgent')

    @property
    def option_parse_comments(self):
        return self.zap._request(self.zap.base + 'spider/view/optionParseComments/').get('ParseComments')

    @property
    def option_parse_robots_txt(self):
        return self.zap._request(self.zap.base + 'spider/view/optionParseRobotsTxt/').get('ParseRobotsTxt')

    @property
    def option_parse_svn_entries(self):
        return self.zap._request(self.zap.base + 'spider/view/optionParseSVNEntries/').get('ParseSVNEntries')

    @property
    def option_parse_git(self):
        return self.zap._request(self.zap.base + 'spider/view/optionParseGit/').get('ParseGit')

    @property
    def option_handle_parameters(self):
        return self.zap._request(self.zap.base + 'spider/view/optionHandleParameters/').get('HandleParameters')

    @property
    def option_handle_o_data_parameters_visited(self):
        return self.zap._request(self.zap.base + 'spider/view/optionHandleODataParametersVisited/').get('HandleODataParametersVisited')

    def scan(self, apikey, url):
        return self.zap._request(self.zap.base + 'spider/action/scan/', {'url' : url})

    def scan_as_user(self, apikey, url, contextid, userid):
        return self.zap._request(self.zap.base + 'spider/action/scanAsUser/', {'url' : url, 'contextId' : contextid, 'userId' : userid})

    @property
    def stop(self, apikey):
        return self.zap._request(self.zap.base + 'spider/action/stop/').get('stop')

    @property
    def clear_excluded_from_scan(self, apikey):
        return self.zap._request(self.zap.base + 'spider/action/clearExcludedFromScan/').get('clearExcludedFromScan')

    def exclude_from_scan(self, apikey, regex):
        return self.zap._request(self.zap.base + 'spider/action/excludeFromScan/', {'regex' : regex})

    def set_option_scope_string(self, apikey, string):
        return self.zap._request(self.zap.base + 'spider/action/setOptionScopeString/', {'String' : string})

    def set_option_skip_url_string(self, apikey, string):
        return self.zap._request(self.zap.base + 'spider/action/setOptionSkipURLString/', {'String' : string})

    def set_option_handle_parameters(self, apikey, string):
        return self.zap._request(self.zap.base + 'spider/action/setOptionHandleParameters/', {'String' : string})

    def set_option_user_agent(self, apikey, string):
        return self.zap._request(self.zap.base + 'spider/action/setOptionUserAgent/', {'String' : string})

    def set_option_max_depth(self, apikey, integer):
        return self.zap._request(self.zap.base + 'spider/action/setOptionMaxDepth/', {'Integer' : integer})

    def set_option_thread_count(self, apikey, integer):
        return self.zap._request(self.zap.base + 'spider/action/setOptionThreadCount/', {'Integer' : integer})

    def set_option_post_form(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionPostForm/', {'Boolean' : boolean})

    def set_option_process_form(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionProcessForm/', {'Boolean' : boolean})

    def set_option_request_wait_time(self, apikey, integer):
        return self.zap._request(self.zap.base + 'spider/action/setOptionRequestWaitTime/', {'Integer' : integer})

    def set_option_parse_comments(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionParseComments/', {'Boolean' : boolean})

    def set_option_parse_robots_txt(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionParseRobotsTxt/', {'Boolean' : boolean})

    def set_option_parse_svn_entries(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionParseSVNEntries/', {'Boolean' : boolean})

    def set_option_parse_git(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionParseGit/', {'Boolean' : boolean})

    def set_option_handle_o_data_parameters_visited(self, apikey, boolean):
        return self.zap._request(self.zap.base + 'spider/action/setOptionHandleODataParametersVisited/', {'Boolean' : boolean})


