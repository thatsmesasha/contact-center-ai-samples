#!/usr/bin/env python3
# Copyright 2022 Google LLC
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

"""Script to create a public/private RSA key pair for the VPC-SC Demo server."""


from Crypto.PublicKey import RSA


def generate_key_pair(filename_pattern="{key}.pem"):
    """Create public/private RSA key pair files."""

    private_key = RSA.generate(1024)
    public_key = private_key.publickey()

    for key, val in {"private_key": private_key, "public_key": public_key}.items():
        key_pem = val.export_key().decode()
        with open(
            filename_pattern.format(key=key), "w", encoding="utf-8"
        ) as file_handle:
            file_handle.write(key_pem)


if __name__ == "__main__":  # pragma: no cover
    generate_key_pair()
