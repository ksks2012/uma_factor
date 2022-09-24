#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup  # pylint: disable=import-error
from setuptools import find_packages

setup(name="umafactor",
		version="0.1.0",
		description="An simple program for record and calculate UMA factors",
		packages=find_packages(),
		install_requires=[
			"google-cloud-vision >= 3.1.0",
		],
		entry_points={
				'console_scripts': [
						'uma-factor = umafactor.cmd.main:main',
				],
		},
		classifiers=[
				"Development Status :: 3 - Alpha",
				"Intended Audience :: Developers",
				"Operating System :: POSIX",
				"Programming Language :: Python :: 3.10.6",
		],
		)

# vim: tabstop=4 shiftwidth=4
