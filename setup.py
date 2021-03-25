from setuptools import setup, find_packages


install_requires = [
    "aiven-client>=2.11.1,<3.0.0",
    "kafka-python>=2.0.2,3.0.0",
    "python-json-logger",
]
tests_require = ["nose2", "nose2-cov==1.0a4"]

extras_requires = {"dev": install_requires + tests_require}

entry_points = {"console_scripts": ["resize_building_images = resize_building_images:main"]}

setup(
    name="python_kafka_demo",
    version="0.0.1",
    description="",
    author="github.com/raface",
    author_email="contact@rafagomes.com",
    packages=find_packages(),
    zip_safe=False,
    test_suite="nose2.collector.collector",
    install_requires=install_requires,
    entry_points=entry_points,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
)
