#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "90f65359-c512-40d3-a10e-b5b76e6a2399")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "NKZ8Q~hLIMVHuamNiKQ~AqWHo4Qtab9ne9qUnbgW")
