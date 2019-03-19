import setuptools

setuptools.setup(
    name="hitta-genus",
    version="0.0.1",
    author="Retzudo",
    description="Hitta genuset av en eller flera substantiver",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'genus = hittagenus.__main__:main',
        ]
    },
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: Swedish",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ]
)
