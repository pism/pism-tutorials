# Copyright (C) 2025 Andy Aschwanden
#
# This file is part of pism-tutorials.
#
# PISM-TUTORIALS is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# PISM-TUTORIALS is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License
# along with PISM; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# pylint: disable=broad-exception-caught

"""
Module provides download functions.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import boto3
from tqdm.notebook import tqdm


def s3_download(
    s3_bucket: str,
    s3_object_key: str,
    local_file_name: str,
    s3_client: boto3.client = boto3.client("s3"),
    tqdm_position: int = 1,
) -> None:
    """
    Download a file from an S3 bucket.

    Parameters
    ----------
    s3_bucket : str
        Name of the S3 bucket.
    s3_object_key : str
        Key of the object in the S3 bucket.
    local_file_name : str
        Path to save the downloaded file locally.
    s3_client : boto3.client, optional
        Boto3 S3 client instance, by default boto3.client("s3").
    tqdm_position : int, optional
        Position of the progress bar in the notebook, by default 1.
    """
    meta_data = s3_client.head_object(Bucket=s3_bucket, Key=s3_object_key)
    total_length = int(meta_data.get("ContentLength", 0))
    with tqdm(
        total=total_length,
        desc=s3_object_key,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        position=tqdm_position,
    ) as pbar:
        with open(local_file_name, "wb") as f:
            s3_client.download_fileobj(
                s3_bucket, s3_object_key, f, Callback=pbar.update
            )


def download_files(
    s3_bucket: str, files: list[str], max_workers: int = 4, overwrite: bool = False
) -> None:
    """
    Download multiple files from an S3 bucket concurrently.

    Parameters
    ----------
    s3_bucket : str
        Name of the S3 bucket.
    files : list of str
        List of object keys to download from the S3 bucket.
    max_workers : int, optional
        Maximum number of threads to use for downloading, by default 4.
    overwrite : bool, optional
        Whether to overwrite existing files, by default False.
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for url in files:
            if not Path(url).is_file() or overwrite:
                futures.append(executor.submit(s3_download, s3_bucket, url, url))
        for future in as_completed(futures):
            try:
                future.result()
            except BaseException as e:  # Catching a more specific exception
                print(f"An error occurred: {e}")
