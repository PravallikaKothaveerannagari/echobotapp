#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "da381970-4799-4e5c-82c5-3d64234aa6d6")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Y2U8Q~n3GboWO5NWuueu-QUrss4ViGqv9oWt2aL6")
