# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import requests
import json

api_key1 = "gJsZ7jenunpxezRbN0FQ4cNCP"

@borg.on(events.NewMessage(pattern=r".ig (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    sample_url = "http://api.farzain.com/ig_profile.php?apikey={}&id={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(input_str, api_key1)).json()
    if response_api["cod"] == 200:
        await event.edit(input_str + "\n `" + json.dumps(response_api["count"]) + "`\n")
    else:
        await event.edit(response_api["message"])
