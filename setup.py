from setuptools import setup

setup(
        name="bottle-request",
        version="0.1.0",
        url="http://github.com/turtlebender/bottle-request/",
        description="Plugin to give bottle a 'stateless' request object",
        author="Tom Howe",
        author_email = 'turtlebender@gmail.com',
        license="MIT",
        platforms="any",
        py_modules=["bottle_request"],
        install_requires= [
            'bottle>=0.9',
            ],
        classifiers = [
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
